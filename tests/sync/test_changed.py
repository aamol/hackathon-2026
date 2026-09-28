import json

import pytest

from sync.changed import affected_services, main, services_to_resync
from sync.workspace import Workspace
from tests.sync.factories import commit_all, init_git_repo, write_fake_workspace


@pytest.fixture
def unite(tmp_path):
    root = write_fake_workspace(tmp_path / "Unite")
    init_git_repo(root)
    return root


@pytest.fixture
def facts_dir(tmp_path, unite):
    directory = tmp_path / "vault" / "_facts"
    directory.mkdir(parents=True)
    head = commit_all(unite, "baseline")
    for service in ("svc1", "svc2"):
        (directory / f"{service}.json").write_text(json.dumps({"source_commit": head[:12]}))
    return directory


def test_shared_config_change_affects_every_service(unite):
    workspace = Workspace.load(unite)
    assert affected_services(["services/t.yml"], ["svc1", "svc2"], workspace) == ["svc1", "svc2"]


def test_package_change_affects_dependents(unite):
    workspace = Workspace.load(unite)
    assert affected_services(["packages/a/src/x.ts"], ["svc1", "svc2"], workspace) == ["svc1"]
    assert affected_services(["docs/readme.md"], ["svc1", "svc2"], workspace) == []


def test_no_changes_means_nothing_to_resync(unite, facts_dir):
    assert services_to_resync(facts_dir, unite, Workspace.load(unite)) == []


def test_untracked_file_in_package_triggers_dependents(unite, facts_dir):
    (unite / "packages" / "a" / "src").mkdir(parents=True)
    (unite / "packages" / "a" / "src" / "new.ts").write_text("export const x = 1;\n")
    assert services_to_resync(facts_dir, unite, Workspace.load(unite)) == ["svc1"]


def test_committed_change_since_facts_commit(unite, facts_dir):
    manifest = unite / "packages" / "c" / "package.json"
    manifest.write_text(manifest.read_text() + "\n")
    commit_all(unite, "touch c")
    assert services_to_resync(facts_dir, unite, Workspace.load(unite)) == ["svc2"]  # c is direct only for svc2


def test_cli_prints_services(unite, facts_dir, capsys):
    (unite / "services" / "svc2" / "handler.ts").write_text("export {};\n")
    assert main(["--unite", str(unite), "--vault", str(facts_dir.parent)]) == 0
    assert capsys.readouterr().out == "svc2\n"


def test_cli_unknown_commit_is_an_error(unite, facts_dir):
    (facts_dir / "svc1.json").write_text(json.dumps({"source_commit": "deadbeef"}))
    assert main(["--unite", str(unite), "--vault", str(facts_dir.parent)]) == 2


def test_cli_facts_for_service_without_package_is_an_error(unite, facts_dir, capsys):
    (facts_dir / "ghost.json").write_text((facts_dir / "svc1.json").read_text())
    (unite / "services" / "svc1" / "handler.ts").write_text("export {};\n")
    assert main(["--unite", str(unite), "--vault", str(facts_dir.parent)]) == 2
    assert capsys.readouterr().err == "ERROR no package.json for service 'ghost' under services/\n"
