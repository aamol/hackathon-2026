"""Which already-extracted services need re-extraction after Unite code changes."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from sync.unite_git import UniteGitError, changed_files
from sync.workspace import Workspace

# Files every service reads through ${self:custom.T...}
SHARED_CONFIG_FILES = frozenset({"services/t.yml"})


def affected_services(files: list[str], services: list[str], workspace: Workspace) -> list[str]:
    affected: set[str] = set()
    for path in files:
        if path in SHARED_CONFIG_FILES:
            affected.update(services)
        else:
            affected.update(workspace.services_affected_by(path, services))
    return sorted(affected)


def services_to_resync(facts_dir: Path, unite_root: Path, workspace: Workspace) -> list[str]:
    files_by_commit: dict[str, list[str]] = {}
    result: set[str] = set()
    for service, commit in sorted(_facts_commits(facts_dir).items()):
        if commit not in files_by_commit:
            files_by_commit[commit] = changed_files(unite_root, commit)
        result.update(affected_services(files_by_commit[commit], [service], workspace))
    return sorted(result)


def _facts_commits(facts_dir: Path) -> dict[str, str]:
    commits = {}
    for path in sorted(facts_dir.glob("*.json")):
        try:
            commits[path.stem] = json.loads(path.read_text(encoding="utf-8"))["source_commit"]
        except (OSError, json.JSONDecodeError, KeyError) as error:
            raise ValueError(f"{path}: cannot read source_commit: {error}") from error
    return commits


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m sync.changed",
                                     description="Print services whose facts are affected by Unite changes.")
    parser.add_argument("--unite", type=Path, required=True)
    parser.add_argument("--vault", type=Path, default=Path("vault"))
    args = parser.parse_args(argv)
    try:
        services = services_to_resync(args.vault / "_facts", args.unite, Workspace.load(args.unite))
    except (UniteGitError, ValueError) as error:
        print(f"ERROR {error}", file=sys.stderr)
        return 2
    except KeyError as error:  # a facts file for a service with no package.json under services/
        print(f"ERROR {error.args[0]}", file=sys.stderr)
        return 2
    if not services:
        print("vault is up to date", file=sys.stderr)
    for service in services:
        print(service)
    return 0


if __name__ == "__main__":
    sys.exit(main())
