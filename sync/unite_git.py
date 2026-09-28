"""Read-only git queries against the Unite checkout."""
from __future__ import annotations

import subprocess
from pathlib import Path


class UniteGitError(Exception):
    """A git command against the Unite checkout failed."""


def _git(unite_root: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(unite_root), *args], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise UniteGitError(f"git {' '.join(args)} failed in {unite_root}: {result.stderr.strip()}")
    return result.stdout


def git_head(unite_root: Path) -> str:
    return _git(unite_root, "rev-parse", "HEAD").strip()
