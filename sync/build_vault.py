"""Merge checked facts files into vault notes (contract v0.2 §3) and write the vault."""
from __future__ import annotations

from dataclasses import dataclass, field

import yaml

from sync.facts import CONTRACT_VERSION, CheckedFacts, Problem

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
