from sync.build_vault import main
from tests.sync.factories import asset_facts, insight_facts


def build(tmp_path, fake_unite, *extra):
    return main(["--vault", str(tmp_path / "vault"), "--facts", str(tmp_path / "facts"),
                 "--unite", str(fake_unite), *extra])


def note_bytes(vault):
    return {path.relative_to(vault): path.read_bytes() for path in sorted(vault.rglob("*.md"))}


def test_build_writes_notes_into_type_folders(tmp_path, fake_unite, write_facts):
    write_facts(insight_facts())
    write_facts(asset_facts())
    assert build(tmp_path, fake_unite) == 0
    vault = tmp_path / "vault"
    assert (vault / "services" / "svc.insight.md").is_file()
    assert (vault / "events" / "evt.asset.asset-created.md").is_file()
    assert (vault / "fields" / "fld.asset.asset-created.asset-id.md").is_file()
    assert (vault / "_meta" / "run-report.md").is_file()


def test_rebuild_is_byte_identical_and_writes_nothing(tmp_path, fake_unite, write_facts, capsys):
    write_facts(insight_facts())
    build(tmp_path, fake_unite)
    before = note_bytes(tmp_path / "vault")
    capsys.readouterr()
    assert build(tmp_path, fake_unite) == 0
    assert note_bytes(tmp_path / "vault") == before
    assert "written: 0" in capsys.readouterr().out


def test_orphan_notes_deleted_and_unmanaged_files_kept(tmp_path, fake_unite, write_facts):
    write_facts(insight_facts())
    vault = tmp_path / "vault"
    for relative in ("services/svc.old.md", "_impact/x.canvas", ".obsidian/app.json", "Home.md"):
        (vault / relative).parent.mkdir(parents=True, exist_ok=True)
        (vault / relative).write_text("keep?")
    assert build(tmp_path, fake_unite) == 0
    assert not (vault / "services" / "svc.old.md").exists()
    assert (vault / "_impact" / "x.canvas").exists()
    assert (vault / ".obsidian" / "app.json").exists()
    assert (vault / "Home.md").exists()


def test_invalid_edge_is_dropped_reported_and_fails_the_build(tmp_path, fake_unite, write_facts):
    data = insight_facts()
    data["edges"][0]["snippet"] = "service.nothing"
    write_facts(data)
    assert build(tmp_path, fake_unite) == 1
    vault = tmp_path / "vault"
    assert "CONSUMES" not in (vault / "services" / "svc.insight.md").read_text()
    assert "not found on line 8" in (vault / "_meta" / "run-report.md").read_text()
    assert build(tmp_path, fake_unite, "--allow-drops") == 0


def test_unusable_facts_file_writes_nothing(tmp_path, fake_unite, write_facts):
    write_facts(insight_facts())
    (tmp_path / "facts" / "asset.json").write_text("{")
    assert build(tmp_path, fake_unite) == 2
    assert not (tmp_path / "vault" / "services").exists()


def test_no_facts_files_is_an_error(tmp_path, fake_unite):
    (tmp_path / "facts").mkdir()
    assert build(tmp_path, fake_unite) == 2


def test_skip_evidence_check_builds_without_unite(tmp_path, write_facts):
    data = insight_facts()
    data["edges"][0]["snippet"] = "service.nothing"
    write_facts(data)
    assert main(["--vault", str(tmp_path / "vault"), "--facts", str(tmp_path / "facts"),
                 "--skip-evidence-check"]) == 0


def test_run_report_counts_and_package_attribution(tmp_path, fake_unite, write_facts):
    write_facts(insight_facts())
    build(tmp_path, fake_unite)
    report = (tmp_path / "vault" / "_meta" / "run-report.md").read_text()
    assert "- Facts files: insight" in report
    assert "- Notes: 3 · Edges: 2 · Errors: 0 · Warnings: 0" in report
    assert "| insight-core | 1 | insight |" in report
    assert "| CONSUMES | 1 |" in report
    assert "## Problems\n_None._" in report
