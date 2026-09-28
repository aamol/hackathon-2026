"""Yarn workspace graph of the Unite monorepo: which workspace packages a service depends on."""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

WORKSPACE_MANIFEST_GLOBS = ("packages/*/package.json", "services/*/package.json")
WORKSPACE_PROTOCOL = "workspace:"
PACKAGE_DIRECTORY_DEPTH = 2  # e.g. packages/asset or services/insight


@dataclass(frozen=True)
class WorkspacePackage:
    name: str
    directory: str
    workspace_deps: frozenset[str]


class Workspace:
    def __init__(self, packages: dict[str, WorkspacePackage]):
        self._packages = packages
        self._by_directory = {package.directory: package for package in packages.values()}
        self._transitive_cache: dict[str, list[WorkspacePackage]] = {}

    @classmethod
    def load(cls, unite_root: Path) -> Workspace:
        packages: dict[str, WorkspacePackage] = {}
        for pattern in WORKSPACE_MANIFEST_GLOBS:
            for manifest in sorted(unite_root.glob(pattern)):
                package = _read_manifest(manifest, unite_root)
                packages[package.name] = package
        return cls(packages)

    def service_package(self, service: str) -> WorkspacePackage:
        package = self._by_directory.get(f"services/{service}")
        if package is None:
            raise KeyError(f"no package.json for service {service!r} under services/")
        return package

    def direct_deps(self, package_name: str) -> list[WorkspacePackage]:
        dependencies = self._packages[package_name].workspace_deps
        return [self._packages[name] for name in sorted(dependencies) if name in self._packages]

    def transitive_deps(self, package_name: str) -> list[WorkspacePackage]:
        if package_name not in self._transitive_cache:
            seen: set[str] = set()
            pending = list(self._packages[package_name].workspace_deps)
            while pending:
                name = pending.pop()
                if name in seen or name not in self._packages:
                    continue
                seen.add(name)
                pending.extend(self._packages[name].workspace_deps)
            seen.discard(package_name)
            self._transitive_cache[package_name] = [self._packages[name] for name in sorted(seen)]
        return self._transitive_cache[package_name]

    def scope_packages(self, service: str, transitive: bool = False) -> list[WorkspacePackage]:
        package_name = self.service_package(service).name
        return self.transitive_deps(package_name) if transitive else self.direct_deps(package_name)

    def owner_of_path(self, repo_relative_path: str) -> WorkspacePackage | None:
        parts = repo_relative_path.split("/")
        if len(parts) <= PACKAGE_DIRECTORY_DEPTH:
            return None
        return self._by_directory.get("/".join(parts[:PACKAGE_DIRECTORY_DEPTH]))

    def services_affected_by(self, repo_relative_path: str, services: list[str]) -> list[str]:
        owner = self.owner_of_path(repo_relative_path)
        if owner is None:
            return []
        affected = []
        for service in services:
            if owner == self.service_package(service) or owner in self.scope_packages(service):
                affected.append(service)
        return sorted(affected)


def _read_manifest(manifest: Path, unite_root: Path) -> WorkspacePackage:
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"cannot read {manifest}: {error}") from error
    if "name" not in data:
        raise ValueError(f"{manifest} has no name")
    dependencies = data.get("dependencies", {})
    return WorkspacePackage(
        name=data["name"],
        directory=manifest.parent.relative_to(unite_root).as_posix(),
        workspace_deps=frozenset(name for name, version in dependencies.items()
                                 if str(version).startswith(WORKSPACE_PROTOCOL)),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m sync.workspace",
                                     description="List the workspace packages a Unite service depends on.")
    parser.add_argument("--unite", type=Path, required=True)
    parser.add_argument("--transitive", action="store_true", help="include indirect workspace dependencies")
    parser.add_argument("service", help="folder name under services/")
    args = parser.parse_args(argv)
    workspace = Workspace.load(args.unite)
    try:
        package = workspace.service_package(args.service)
    except KeyError as error:
        print(f"ERROR {error.args[0]}", file=sys.stderr)
        return 2
    print(json.dumps({
        "service": args.service,
        "package": package.name,
        "directory": package.directory,
        "workspace_packages": [{"name": dep.name, "directory": dep.directory}
                               for dep in workspace.scope_packages(args.service, args.transitive)],
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
