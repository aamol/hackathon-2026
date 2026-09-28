"""Merge checked facts files into vault notes (contract v0.2 §3) and write the vault."""
from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from sync import ids
from sync.facts import CONTRACT_VERSION, CheckedFacts, FactsError, Problem, check_facts, load_facts

NOTE_EDGE_KEYS = ("type", "to", "evidence", "confidence", "via", "filter")
LEADING_KEYS = ("id", "type", "name")
BODY_ONLY_KEYS = frozenset({"summary"})
# Several services describe the same node in their own words; that is not a conflict.
SILENTLY_MERGED_KEYS = frozenset({"summary"})
NO_LINKS_TEXT = "_No outgoing links._"


@dataclass
class VaultNode:
    properties: dict
    sources: set[str] = field(default_factory=set)
    edges: list[dict] = field(default_factory=list)
    generated_at: str = ""

    @property
    def id(self) -> str:
        return self.properties["id"]


def merge(checked_files: list[CheckedFacts]) -> tuple[dict[str, VaultNode], list[Problem]]:
    nodes: dict[str, VaultNode] = {}
    problems: list[Problem] = []
    for checked in sorted(checked_files, key=lambda item: item.facts.service):
        for node in checked.nodes:
            problems += _merge_node(nodes, node, checked.facts.service, checked.facts.extracted_at)
        for edge in checked.edges:
            _add_edge(nodes[edge["from"]], edge)
    return nodes, problems


def _merge_node(nodes: dict[str, VaultNode], node: dict, service: str, extracted_at: str) -> list[Problem]:
    existing = nodes.get(node["id"])
    problems: list[Problem] = []
    if existing is None:
        existing = nodes[node["id"]] = VaultNode(properties=dict(node))
    else:
        problems = _merge_properties(existing, node, service)
    existing.sources.add(service)
    existing.generated_at = max(existing.generated_at, extracted_at)
    return problems


def _merge_properties(existing: VaultNode, node: dict, service: str) -> list[Problem]:
    problems = []
    for key, value in node.items():
        if key not in existing.properties:
            existing.properties[key] = value
        elif existing.properties[key] != value and key not in SILENTLY_MERGED_KEYS:
            first_source = sorted(existing.sources)[0]
            problems.append(Problem(
                "warning", f"node {node['id']}",
                f"{key!r}: keeping {existing.properties[key]!r} from {first_source}, ignoring {value!r} from {service}",
            ))
    return problems


def _add_edge(node: VaultNode, edge: dict) -> None:
    note_edge = {key: edge[key] for key in NOTE_EDGE_KEYS if key in edge}
    identity = _edge_identity(note_edge)
    if all(_edge_identity(existing) != identity for existing in node.edges):
        node.edges.append(note_edge)


def _edge_identity(edge: dict) -> tuple[str, str, str]:
    return edge["type"], edge["to"], edge["evidence"]


def render_note(node: VaultNode) -> str:
    frontmatter = yaml.safe_dump(_frontmatter(node), sort_keys=False, allow_unicode=True, width=1000)
    return f"---\n{frontmatter}---\n{_body(node)}"


def _frontmatter(node: VaultNode) -> dict:
    properties = {key: value for key, value in node.properties.items() if key not in BODY_ONLY_KEYS}
    ordered = {key: properties[key] for key in LEADING_KEYS}
    ordered |= {key: properties[key] for key in sorted(properties) if key not in LEADING_KEYS}
    ordered["generated_at"] = node.generated_at
    ordered["contract_version"] = CONTRACT_VERSION
    ordered["sources"] = sorted(node.sources)
    ordered["edges"] = sorted(node.edges, key=_edge_identity)
    return ordered


def _body(node: VaultNode) -> str:
    lines = [f"# {node.properties['name']}", ""]
    summary = node.properties.get("summary")
    if summary:
        lines += ["## Summary", summary, ""]
    lines.append("## Links")
    targets_by_type: dict[str, set[str]] = {}
    for edge in node.edges:
        targets_by_type.setdefault(edge["type"], set()).add(edge["to"])
    if not targets_by_type:
        lines.append(NO_LINKS_TEXT)
    for edge_type in sorted(targets_by_type):
        links = ", ".join(f"[[{target}]]" for target in sorted(targets_by_type[edge_type]))
        lines.append(f"- {edge_type} {links}")
    return "\n".join(lines) + "\n"


MANAGED_FOLDERS = tuple(folder for _, folder in ids.NODE_TYPES.values())
PACKAGE_VIA_PREFIX = "package:"
RUN_REPORT_PATH = Path("_meta") / "run-report.md"


@dataclass(frozen=True)
class WriteResult:
    written: tuple[str, ...]
    unchanged: int
    deleted: tuple[str, ...]


def write_vault(nodes: dict[str, VaultNode], vault_dir: Path) -> WriteResult:
    produced = {
        vault_dir / ids.folder_of(node.properties["type"]) / f"{node.id}.md": render_note(node)
        for node in nodes.values()
    }
    written: list[str] = []
    unchanged = 0
    for path, content in sorted(produced.items()):
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.is_file() and path.read_text(encoding="utf-8") == content:
            unchanged += 1
            continue
        path.write_text(content, encoding="utf-8")
        written.append(str(path.relative_to(vault_dir)))
    deleted: list[str] = []
    for folder in MANAGED_FOLDERS:
        for path in sorted((vault_dir / folder).glob("*.md")):
            if path not in produced:
                path.unlink()
                deleted.append(str(path.relative_to(vault_dir)))
    return WriteResult(tuple(written), unchanged, tuple(deleted))


def render_run_report(nodes: dict[str, VaultNode], problems: list[Problem]) -> str:
    services = sorted({source for node in nodes.values() for source in node.sources})
    edges = [(node, edge) for node in nodes.values() for edge in node.edges]
    errors = sum(problem.severity == "error" for problem in problems)
    newest = max((node.generated_at for node in nodes.values()), default="-")
    lines = [
        "# Vault build report", "",
        f"- Facts files: {', '.join(services) or '(none)'}",
        f"- Newest extraction: {newest}",
        f"- Notes: {len(nodes)} · Edges: {len(edges)} · Errors: {errors} · Warnings: {len(problems) - errors}",
        "",
    ]
    lines += _count_table("Nodes by type", Counter(node.properties["type"] for node in nodes.values()))
    lines += _count_table("Edges by type", Counter(edge["type"] for _, edge in edges))
    lines += _package_table(edges)
    lines += ["## Problems"] + ([f"- {problem}" for problem in problems] or ["_None._"])
    return "\n".join(lines) + "\n"


def _count_table(title: str, counts: Counter) -> list[str]:
    rows = [f"| {key} | {counts[key]} |" for key in sorted(counts)]
    return [f"## {title}", "", "| type | count |", "|---|---|", *rows, ""]


def _package_table(edges: list[tuple[VaultNode, dict]]) -> list[str]:
    counts: Counter = Counter()
    services: dict[str, set[str]] = defaultdict(set)
    for node, edge in edges:
        if edge["via"].startswith(PACKAGE_VIA_PREFIX):
            package = edge["via"].removeprefix(PACKAGE_VIA_PREFIX)
            counts[package] += 1
            services[package] |= node.sources
    rows = [f"| {package} | {counts[package]} | {', '.join(sorted(services[package]))} |" for package in sorted(counts)]
    return ["## Package attribution", "", "| package | edges | services |", "|---|---|---|",
            *(rows or ["| – | 0 | – |"]), ""]


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    facts_dir = args.facts or args.vault / "_facts"
    paths = sorted(facts_dir.glob("*.json"))
    if not paths:
        print(f"ERROR no facts files in {facts_dir}", file=sys.stderr)
        return 2
    unite_root = None if args.skip_evidence_check else args.unite
    if unite_root is not None and not unite_root.is_dir():
        print(f"ERROR Unite checkout not found: {unite_root}", file=sys.stderr)
        return 2
    try:
        facts_files = [load_facts(path) for path in paths]
    except FactsError as error:
        print(f"ERROR {error}", file=sys.stderr)
        return 2
    checked = [check_facts(facts, unite_root) for facts in facts_files]
    nodes, merge_problems = merge(checked)
    problems = [problem for item in checked for problem in item.problems] + merge_problems
    result = write_vault(nodes, args.vault)
    report_path = args.vault / RUN_REPORT_PATH
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(render_run_report(nodes, problems), encoding="utf-8")
    for problem in problems:
        print(problem, file=sys.stderr)
    print(f"notes: {len(nodes)}  written: {len(result.written)}  unchanged: {result.unchanged}  "
          f"deleted: {len(result.deleted)}  report: {report_path}")
    has_errors = any(problem.severity == "error" for problem in problems)
    return 1 if has_errors and not args.allow_drops else 0


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="python -m sync.build_vault", description="Build vault notes from facts files.")
    parser.add_argument("--vault", type=Path, default=Path("vault"))
    parser.add_argument("--facts", type=Path, help="facts directory (default: <vault>/_facts)")
    evidence = parser.add_mutually_exclusive_group(required=True)
    evidence.add_argument("--unite", type=Path, help="Unite checkout used to verify evidence lines")
    evidence.add_argument("--skip-evidence-check", action="store_true", help="fixtures only")
    parser.add_argument("--allow-drops", action="store_true", help="exit 0 even if invalid nodes/edges were dropped")
    return parser.parse_args(argv)


if __name__ == "__main__":
    sys.exit(main())
