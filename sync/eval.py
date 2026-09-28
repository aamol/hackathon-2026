"""Extraction quality: precision/recall vs hand-labelled ground truth, run-to-run agreement, edge diffs."""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from sync.build_vault import MANAGED_FOLDERS
from sync.validate import read_frontmatter

EdgeKey = tuple[str, str, str]  # (from id, edge type, to id)
GROUND_TRUTH_COLUMNS = frozenset({"src", "type", "dst"})
OVERALL = "ALL"


@dataclass(frozen=True)
class Score:
    true_positives: int
    predicted: int
    expected: int

    @property
    def precision(self) -> float | None:
        return self.true_positives / self.predicted if self.predicted else None

    @property
    def recall(self) -> float | None:
        return self.true_positives / self.expected if self.expected else None


def score(predicted: set[EdgeKey], expected: set[EdgeKey]) -> dict[str, Score]:
    edge_types = sorted({key[1] for key in predicted | expected})
    scores = {edge_type: _score_subset({k for k in predicted if k[1] == edge_type},
                                       {k for k in expected if k[1] == edge_type})
              for edge_type in edge_types}
    scores[OVERALL] = _score_subset(predicted, expected)
    return scores


def _score_subset(predicted: set[EdgeKey], expected: set[EdgeKey]) -> Score:
    return Score(len(predicted & expected), len(predicted), len(expected))


def restrict_to_labelled_sources(predicted: set[EdgeKey], expected: set[EdgeKey]) -> set[EdgeKey]:
    labelled_sources = {key[0] for key in expected}
    return {key for key in predicted if key[0] in labelled_sources}


def load_ground_truth(csv_path: Path) -> set[EdgeKey]:
    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = GROUND_TRUTH_COLUMNS - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"{csv_path}: missing columns {sorted(missing)}")
        return {(row["src"].strip(), row["type"].strip(), row["dst"].strip())
                for row in reader if (row["src"] or "").strip()}


def load_vault_edges(vault_dir: Path) -> set[EdgeKey]:
    edges = set()
    for folder in MANAGED_FOLDERS:
        for path in sorted((vault_dir / folder).glob("*.md")):
            frontmatter = read_frontmatter(path)
            edges |= {(frontmatter["id"], edge["type"], edge["to"]) for edge in frontmatter.get("edges") or []}
    return edges


def _edges_of(facts: dict) -> set[EdgeKey]:
    return {(edge["from"], edge["type"], edge["to"]) for edge in facts["edges"]}


def load_facts_edges(path: Path) -> set[EdgeKey]:
    return _edges_of(json.loads(path.read_text(encoding="utf-8")))


def agreement(first: set[EdgeKey], second: set[EdgeKey]) -> float:
    union = first | second
    return len(first & second) / len(union) if union else 1.0


def previous_facts_edges(path: Path, ref: str = "HEAD") -> set[EdgeKey] | None:
    result = subprocess.run(["git", "-C", str(path.parent), "show", f"{ref}:./{path.name}"],
                            capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return None
    return _edges_of(json.loads(result.stdout))


def render_eval(scores: dict[str, Score], truth_path: Path) -> str:
    lines = ["# Extraction eval", "", f"Ground truth: `{truth_path}`", "",
             "| edge type | predicted | expected | true positives | precision | recall |",
             "|---|---|---|---|---|---|"]
    for edge_type in [key for key in scores if key != OVERALL] + [OVERALL]:
        item = scores[edge_type]
        lines.append(f"| {edge_type} | {item.predicted} | {item.expected} | {item.true_positives} | "
                     f"{_ratio(item.precision)} | {_ratio(item.recall)} |")
    return "\n".join(lines) + "\n"


def _ratio(value: float | None) -> str:
    return "–" if value is None else f"{value:.2f}"


def _format_edge(key: EdgeKey) -> str:
    return " ".join(key)


def _print_difference(added: set[EdgeKey], removed: set[EdgeKey]) -> None:
    for key in sorted(added):
        print(f"+ {_format_edge(key)}")
    for key in sorted(removed):
        print(f"- {_format_edge(key)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m sync.eval", description="Measure extraction quality.")
    commands = parser.add_subparsers(dest="command", required=True)
    score_parser = commands.add_parser("score", help="precision/recall vs ground truth")
    score_parser.add_argument("--vault", type=Path, default=Path("vault"))
    score_parser.add_argument("--truth", type=Path, default=Path("ground-truth/edges.csv"))
    score_parser.add_argument("--out", type=Path, help="write markdown here (default: <vault>/_meta/eval.md)")
    agreement_parser = commands.add_parser("agreement", help="compare two facts files of the same service")
    agreement_parser.add_argument("first", type=Path)
    agreement_parser.add_argument("second", type=Path)
    diff_parser = commands.add_parser("diff", help="edges added/removed vs the committed facts file")
    diff_parser.add_argument("facts_file", type=Path)
    args = parser.parse_args(argv)

    if args.command == "score":
        expected = load_ground_truth(args.truth)
        predicted = restrict_to_labelled_sources(load_vault_edges(args.vault), expected)
        text = render_eval(score(predicted, expected), args.truth)
        out = args.out or args.vault / "_meta" / "eval.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(text)
    elif args.command == "agreement":
        first, second = load_facts_edges(args.first), load_facts_edges(args.second)
        print(f"agreement: {agreement(first, second):.2f} ({len(first & second)} shared / {len(first | second)} total)")
        _print_difference(added=second - first, removed=first - second)
    else:
        current = load_facts_edges(args.facts_file)
        previous = previous_facts_edges(args.facts_file)
        service = args.facts_file.stem
        if previous is None:
            print(f"{service}: new ({len(current)} edges)")
        else:
            added, removed = current - previous, previous - current
            print(f"{service}: +{len(added)} -{len(removed)} edges (was {len(previous)}, now {len(current)})")
            _print_difference(added, removed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
