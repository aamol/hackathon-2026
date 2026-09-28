"""Validate a built vault against contract v0.2 (python -m sync.validate vault/)."""
from __future__ import annotations

import argparse
import datetime
import json
import sys
from pathlib import Path

import jsonschema
import yaml

from sync import ids
from sync.facts import Problem, format_schema_error, load_schema
from sync.unite_git import UniteGitError, git_head

FRONTMATTER_OPEN = "---\n"
FRONTMATTER_CLOSE = "\n---\n"


class NoteError(Exception):
    """A note file cannot be parsed."""


def read_frontmatter(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise NoteError(f"cannot read note: {error}") from error
    if not text.startswith(FRONTMATTER_OPEN):
        raise NoteError("missing frontmatter")
    end = text.find(FRONTMATTER_CLOSE, len(FRONTMATTER_OPEN) - 1)
    if end == -1:
        raise NoteError("unterminated frontmatter")
    try:
        data = yaml.safe_load(text[len(FRONTMATTER_OPEN):end])
    except yaml.YAMLError as error:
        raise NoteError(f"invalid YAML: {error}") from error
    if not isinstance(data, dict):
        raise NoteError("frontmatter is not a mapping")
    return _stringify_dates(data)


def _stringify_dates(value):
    # Hand-written notes may have unquoted timestamps, which YAML turns into datetime objects.
    if isinstance(value, datetime.datetime):
        if value.tzinfo is not None:
            return value.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        return value.isoformat()
    if isinstance(value, datetime.date):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: _stringify_dates(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_stringify_dates(item) for item in value]
    return value


def validate_vault(vault_dir: Path) -> list[Problem]:
    notes, problems = _load_notes(vault_dir)
    return problems + _dangling_edges(notes)


def _load_notes(vault_dir: Path) -> tuple[dict[str, dict], list[Problem]]:
    validator = jsonschema.Draft202012Validator(load_schema("vault-note.schema.json"))
    notes: dict[str, dict] = {}
    problems: list[Problem] = []
    for node_type, (_, folder) in ids.NODE_TYPES.items():
        for path in sorted((vault_dir / folder).glob("*.md")):
            where = str(path.relative_to(vault_dir))
            try:
                frontmatter = read_frontmatter(path)
            except NoteError as error:
                problems.append(Problem("error", where, str(error)))
                continue
            schema_errors = sorted(validator.iter_errors(frontmatter), key=lambda error: error.json_path)
            problems += [Problem("error", where, format_schema_error(error)) for error in schema_errors]
            problems += _placement_problems(where, path, folder, node_type, frontmatter)
            note_id = frontmatter.get("id")
            if note_id in notes:
                problems.append(Problem("error", where, f"duplicate id {note_id!r}"))
            elif isinstance(note_id, str):
                notes[note_id] = frontmatter
    return notes, problems


def _placement_problems(where: str, path: Path, folder: str, node_type: str, frontmatter: dict) -> list[Problem]:
    problems = []
    if frontmatter.get("id") != path.stem:
        problems.append(Problem("error", where, f"file name must equal id ({frontmatter.get('id')!r})"))
    if frontmatter.get("type") != node_type:
        problems.append(Problem("error", where, f"type {frontmatter.get('type')!r} does not belong in {folder}/"))
    return problems


def _dangling_edges(notes: dict[str, dict]) -> list[Problem]:
    problems = []
    for note_id, frontmatter in sorted(notes.items()):
        for edge in frontmatter.get("edges") or []:
            if isinstance(edge, dict) and edge.get("to") not in notes:
                problems.append(Problem("error", note_id,
                                        f"edge {edge.get('type')} points to missing note {edge.get('to')!r}"))
    return problems


def stale_facts_warnings(facts_dir: Path, unite_root: Path) -> list[Problem]:
    head = git_head(unite_root)
    problems = []
    for path in sorted(facts_dir.glob("*.json")):
        try:
            commit = json.loads(path.read_text(encoding="utf-8"))["source_commit"]
        except (OSError, json.JSONDecodeError, KeyError) as error:
            problems.append(Problem("warning", path.name, f"cannot read source_commit: {error}"))
            continue
        if not head.startswith(commit):
            problems.append(Problem("warning", path.name,
                                    f"extracted at {commit}, Unite HEAD is {head[:12]}; run /enginav-sync --changed"))
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m sync.validate", description="Validate a built vault.")
    parser.add_argument("vault", type=Path)
    parser.add_argument("--unite", type=Path, help="Unite checkout; enables the stale-facts check")
    args = parser.parse_args(argv)
    problems = validate_vault(args.vault)
    if args.unite:
        try:
            problems += stale_facts_warnings(args.vault / "_facts", args.unite)
        except UniteGitError as error:
            problems.append(Problem("warning", "stale-check", str(error)))
    for problem in problems:
        print(problem, file=sys.stderr)
    error_count = sum(problem.severity == "error" for problem in problems)
    print(f"{'FAIL' if error_count else 'OK'}: {error_count} errors, {len(problems) - error_count} warnings")
    return 1 if error_count else 0


if __name__ == "__main__":
    sys.exit(main())
