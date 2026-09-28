import json

import pytest

from sync.workspace import Workspace, WorkspacePackage, main
from tests.sync.factories import write_fake_workspace


@pytest.fixture
def workspace(tmp_path):
    return Workspace.load(write_fake_workspace(tmp_path / "Unite"))


def names(packages):
    return [package.name for package in packages]


def test_transitive_workspace_deps_ignore_external_packages(workspace):
    assert names(workspace.transitive_deps("svc1-service")) == ["a", "b", "c"]
    assert names(workspace.transitive_deps("svc2-service")) == ["c"]


def test_scope_is_direct_deps_unless_transitive(workspace):
    assert names(workspace.direct_deps("a")) == ["b"]  # lodash is not a workspace package
    assert names(workspace.scope_packages("svc1")) == ["a"]
    assert names(workspace.scope_packages("svc1", transitive=True)) == ["a", "b", "c"]


def test_transitive_deps_survive_cycles():
    cyclic = Workspace({
        "x": WorkspacePackage("x", "packages/x", frozenset({"y"})),
        "y": WorkspacePackage("y", "packages/y", frozenset({"x"})),
    })
    assert names(cyclic.transitive_deps("x")) == ["y"]


def test_service_package_by_folder(workspace):
    assert workspace.service_package("svc1").name == "svc1-service"
    with pytest.raises(KeyError, match="nope"):
        workspace.service_package("nope")


def test_owner_of_path(workspace):
    assert workspace.owner_of_path("packages/b/src/x.ts").name == "b"
    assert workspace.owner_of_path("services/svc2/serverless.yml").name == "svc2-service"
    assert workspace.owner_of_path("README.md") is None
    assert workspace.owner_of_path("services/t.yml") is None


@pytest.mark.parametrize(
    "path, expected",
    [
        ("packages/a/src/x.ts", ["svc1"]),
        ("packages/b/src/x.ts", []),  # only an indirect dependency of svc1: outside the extraction scope
        ("packages/c/src/x.ts", ["svc2"]),
        ("services/svc2/serverless.yml", ["svc2"]),
        ("packages/unused/index.ts", []),
        ("README.md", []),
    ],
)
def test_services_affected_by(workspace, path, expected):
    assert workspace.services_affected_by(path, ["svc1", "svc2"]) == expected


def test_cli_prints_packages(tmp_path, capsys):
    unite = write_fake_workspace(tmp_path / "Unite")
    assert main(["--unite", str(unite), "svc1"]) == 0
    output = json.loads(capsys.readouterr().out)
    assert output["package"] == "svc1-service"
    assert output["directory"] == "services/svc1"
    assert output["workspace_packages"] == [{"name": "a", "directory": "packages/a"}]
    assert main(["--unite", str(unite), "--transitive", "svc1"]) == 0
    assert [item["name"] for item in json.loads(capsys.readouterr().out)["workspace_packages"]] == ["a", "b", "c"]


def test_cli_unknown_service(tmp_path):
    unite = write_fake_workspace(tmp_path / "Unite")
    assert main(["--unite", str(unite), "nope"]) == 2
