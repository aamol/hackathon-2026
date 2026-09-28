"""Load and check one Claude-written facts file (contract v0.2 §5)."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from functools import cache, lru_cache
from pathlib import Path

import jsonschema

from sync import ids

CONTRACT_VERSION = "0.2"
SCHEMA_DIR = Path(__file__).resolve().parent.parent / "schema"
EVIDENCE_PATTERN = re.compile(r"^Unite/(?P<path>.+):(?P<line>[1-9][0-9]*)$")
PLACEHOLDER_TIMESTAMP = "2000-01-01T00:00:00Z"

# edge type -> (allowed source node types, allowed target node types); contract v0.2 §3.2
ALLOWED_EDGES: dict[str, tuple[frozenset[str], frozenset[str]]] = {
    "EXPOSES": (frozenset({"service"}), frozenset({"api", "function"})),
    "CALLS": (frozenset({"service"}), frozenset({"api", "function", "external", "unresolved"})),
    "PUBLISHES": (frozenset({"service"}), frozenset({"event", "queue", "unresolved"})),
    "CONSUMES": (frozenset({"service"}), frozenset({"event", "queue"})),
    "READS": (frozenset({"service"}), frozenset({"table", "unresolved"})),
    "WRITES": (frozenset({"service"}), frozenset({"table", "unresolved"})),
    "HAS_FIELD": (frozenset({"event", "queue", "api", "table"}), frozenset({"field"})),
    "TESTS": (frozenset({"test"}), frozenset({"service", "api", "function"})),
    "DEPENDS_ON": (frozenset({"service"}), frozenset({"external"})),
}
# A service owns ids with these prefixes followed by its own slug, e.g. api.<svc>.*
OWNED_ID_PREFIXES = ("api", "fn", "test")
# ...and the targets of these edges from its service node (so it may declare their fields).
OWNERSHIP_EDGES = frozenset({"PUBLISHES", "WRITES"})
# via -> the one confidence allowed for direct evidence; anything else must be inferred (<= INFERRED_CONFIDENCE_MAX).
DECLARATIVE_VIAS = frozenset({"serverless.yml", "t.yml"})
SERVICE_CODE_VIA = "service-code"
PACKAGE_VIA_PREFIX = "package:"
DECLARATIVE_CONFIDENCE = 1.0
SERVICE_CODE_CONFIDENCE = 0.9
PACKAGE_CONFIDENCE = 0.8
INFERRED_CONFIDENCE_MAX = 0.6


class FactsError(Exception):
    """A facts file cannot be used at all (unreadable or schema-invalid)."""


@dataclass(frozen=True)
class Problem:
    severity: str  # "error" | "warning"
    where: str
    message: str

    def __str__(self) -> str:
        return f"{self.severity.upper()} {self.where}: {self.message}"


@dataclass(frozen=True)
class FactsFile:
    service: str
    source_commit: str
    extracted_at: str
    nodes: tuple[dict, ...]
    edges: tuple[dict, ...]


@dataclass(frozen=True)
class CheckedFacts:
    facts: FactsFile
    nodes: tuple[dict, ...]
    edges: tuple[dict, ...]
    problems: tuple[Problem, ...]


@cache
def load_schema(name: str) -> dict:
    return json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))


def format_schema_error(error: jsonschema.ValidationError) -> str:
    return f"{error.json_path}: {error.message}"


def parse_facts(raw: object, origin: str) -> FactsFile:
    validator = jsonschema.Draft202012Validator(load_schema("facts.schema.json"))
    errors = sorted(validator.iter_errors(raw), key=lambda error: error.json_path)
    if errors:
        raise FactsError(f"{origin}: {format_schema_error(errors[0])}")
    return FactsFile(
        service=raw["service"],
        source_commit=raw["source_commit"],
        extracted_at=raw["extracted_at"],
        nodes=tuple(raw["nodes"]),
        edges=tuple(raw["edges"]),
    )


def load_facts(path: Path) -> FactsFile:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise FactsError(f"{path}: cannot read facts file: {error}") from error
    facts = parse_facts(raw, str(path))
    if path.stem != facts.service:
        raise FactsError(f"{path}: file must be named {facts.service}.json")
    return facts


def owned_ids(facts: FactsFile) -> set[str]:
    service_node = ids.service_id(facts.service)
    service_slug = ids.slug(facts.service)
    prefixes = tuple(f"{prefix}.{service_slug}." for prefix in OWNED_ID_PREFIXES)
    owned = {service_node}
    owned |= {node["id"] for node in facts.nodes if node["id"].startswith(prefixes)}
    owned |= {edge["to"] for edge in facts.edges if edge["from"] == service_node and edge["type"] in OWNERSHIP_EDGES}
    return owned


@lru_cache(maxsize=512)
def _read_lines(path: Path) -> tuple[str, ...]:
    return tuple(path.read_text(encoding="utf-8", errors="replace").splitlines())


def evidence_error(evidence: str, snippet: str, unite_root: Path) -> str | None:
    match = EVIDENCE_PATTERN.match(evidence)
    if match is None:
        return f"evidence {evidence!r} is not Unite/<path>:<line>"
    root = unite_root.resolve()
    file_path = (root / match["path"]).resolve()
    if not file_path.is_relative_to(root):
        return "evidence path escapes the Unite checkout"
    if not file_path.is_file():
        return f"evidence file does not exist: {match['path']}"
    lines = _read_lines(file_path)
    line_number = int(match["line"])
    if line_number > len(lines):
        return f"evidence line {line_number} is past end of file ({len(lines)} lines)"
    if snippet not in lines[line_number - 1]:
        return f"snippet {snippet!r} not found on line {line_number}"
    return None


def check_facts(facts: FactsFile, unite_root: Path | None) -> CheckedFacts:
    nodes, problems = _check_nodes(facts)
    declared = {node["id"] for node in nodes}
    owned = owned_ids(facts)
    edges = []
    for edge in facts.edges:
        where = f"{facts.service}: {edge['from']} {edge['type']} {edge['to']}"
        edge_messages = _edge_errors(edge, declared, owned, unite_root)
        edge_messages += _via_errors(edge, facts.service)
        problems += [Problem("error", where, message) for message in edge_messages]
        if not edge_messages:
            edges.append(edge)
    return CheckedFacts(facts, tuple(nodes), tuple(edges), tuple(problems))


def _check_nodes(facts: FactsFile) -> tuple[list[dict], list[Problem]]:
    validator = jsonschema.Draft202012Validator(load_schema("vault-note.schema.json"))
    seen: set[str] = set()
    valid: list[dict] = []
    problems: list[Problem] = []
    for node in facts.nodes:
        where = f"{facts.service}: node {node['id']}"
        if node["id"] in seen:
            problems.append(Problem("error", where, "declared twice"))
            continue
        seen.add(node["id"])
        message = _node_error(node, validator)
        if message:
            problems.append(Problem("error", where, message))
        else:
            valid.append(node)
    return valid, problems


def _node_error(node: dict, validator: jsonschema.Draft202012Validator) -> str | None:
    if ids.type_of(node["id"]) != node["type"]:
        return f"id prefix does not match type {node['type']!r}"
    # Validate as the note it will become, so type-specific properties are enforced early.
    candidate = {**node, "generated_at": PLACEHOLDER_TIMESTAMP, "contract_version": CONTRACT_VERSION,
                 "sources": ["check"], "edges": []}
    errors = sorted(validator.iter_errors(candidate), key=lambda error: error.json_path)
    return format_schema_error(errors[0]) if errors else None


def _edge_errors(edge: dict, declared: set[str], owned: set[str], unite_root: Path | None) -> list[str]:
    messages = [f"{end} node {edge[end]!r} is not declared in this facts file"
                for end in ("from", "to") if edge[end] not in declared]
    if edge["from"] not in owned:
        messages.append("from node is not owned by this service (see ownership rules)")
    from_types, to_types = ALLOWED_EDGES[edge["type"]]
    from_type, to_type = ids.type_of(edge["from"]), ids.type_of(edge["to"])
    if from_type not in from_types or to_type not in to_types:
        messages.append(f"{edge['type']} is not allowed from {from_type} to {to_type}")
    if "filter" in edge and edge["type"] != "CONSUMES":
        messages.append("filter is only allowed on CONSUMES")
    if unite_root is not None:
        problem = evidence_error(edge["evidence"], edge["snippet"], unite_root)
        if problem:
            messages.append(problem)
    return messages


def _via_errors(edge: dict, service: str) -> list[str]:
    """The via must match where the evidence lives, and the confidence must fit the via's tier."""
    via, confidence = edge["via"], edge["confidence"]
    evidence_path = edge["evidence"].rsplit(":", 1)[0]
    messages = []
    if via in DECLARATIVE_VIAS:
        direct_confidence = DECLARATIVE_CONFIDENCE
        if Path(evidence_path).name != via:
            messages.append(f"via {via} requires evidence in a {via} file")
    elif via == SERVICE_CODE_VIA:
        direct_confidence = SERVICE_CODE_CONFIDENCE
        expected_prefix = f"Unite/services/{service}/"
        if not evidence_path.startswith(expected_prefix):
            messages.append(f"via {via} requires evidence under {expected_prefix}")
    else:
        direct_confidence = PACKAGE_CONFIDENCE
        # No workspace access here: a package lives in packages/<its name without npm scope>.
        package_directory = via[len(PACKAGE_VIA_PREFIX):].rsplit("/", 1)[-1]
        expected_prefix = f"Unite/packages/{package_directory}/"
        if not evidence_path.startswith(expected_prefix):
            messages.append(f"via {via} requires evidence under {expected_prefix}")
    if confidence != direct_confidence and confidence > INFERRED_CONFIDENCE_MAX:
        messages.append(f"confidence {confidence} not allowed for via {via} "
                        f"(expected {direct_confidence} or ≤{INFERRED_CONFIDENCE_MAX})")
    return messages


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m sync.facts", description="Check one facts file.")
    parser.add_argument("facts_file", type=Path)
    parser.add_argument("--unite", type=Path, required=True, help="Unite checkout used to verify evidence")
    args = parser.parse_args(argv)
    try:
        facts = load_facts(args.facts_file)
    except FactsError as error:
        print(f"ERROR {error}", file=sys.stderr)
        return 2
    checked = check_facts(facts, args.unite)
    for problem in checked.problems:
        print(problem, file=sys.stderr)
    print(f"nodes ok: {len(checked.nodes)}/{len(facts.nodes)}  edges ok: {len(checked.edges)}/{len(facts.edges)}")
    return 1 if checked.problems else 0


if __name__ == "__main__":
    sys.exit(main())
