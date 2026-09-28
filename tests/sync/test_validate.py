import json
import re

from sync.validate import main, stale_facts_warnings, validate_vault
from tests.sync.factories import asset_facts, build_vault_dir, init_git_repo, insight_facts, write_fake_unite


def errors(problems):
    return "\n".join(str(problem) for problem in problems if problem.severity == "error")


def built_vault(tmp_path):
    vault = tmp_path / "vault"
    build_vault_dir(vault, [asset_facts(), insight_facts()])
    return vault


def test_valid_vault_has_no_problems(tmp_path):
    assert validate_vault(built_vault(tmp_path)) == []


def test_dangling_edge_target(tmp_path):
    vault = built_vault(tmp_path)
    (vault / "events" / "evt.asset.asset-created.md").unlink()
    assert "points to missing note 'evt.asset.asset-created'" in errors(validate_vault(vault))


def test_missing_frontmatter(tmp_path):
    vault = built_vault(tmp_path)
    (vault / "services" / "svc.asset.md").write_text("# no frontmatter\n")
    assert "missing frontmatter" in errors(validate_vault(vault))


def test_schema_error_on_edge(tmp_path):
    vault = built_vault(tmp_path)
    note = vault / "services" / "svc.insight.md"
    note.write_text(re.sub(r"^\s+evidence: .*serverless\.yml:8\n", "", note.read_text(), flags=re.M))
    assert "'evidence' is a required property" in errors(validate_vault(vault))


def test_file_name_must_equal_id(tmp_path):
    vault = built_vault(tmp_path)
    (vault / "services" / "svc.asset.md").rename(vault / "services" / "svc.renamed.md")
    assert "file name must equal id" in errors(validate_vault(vault))


def test_note_in_wrong_folder(tmp_path):
    vault = built_vault(tmp_path)
    (vault / "services" / "svc.asset.md").rename(vault / "events" / "svc.asset.md")
    assert "does not belong in events/" in errors(validate_vault(vault))


def test_hand_written_note_with_unquoted_timestamp_is_valid(tmp_path):
    note = tmp_path / "vault" / "externals" / "ext.google-genai.md"
    note.parent.mkdir(parents=True)
    note.write_text(
        "---\nid: ext.google-genai\ntype: external\nname: google-genai\n"
        "generated_at: 2026-09-28T16:00:00Z\ncontract_version: \"0.2\"\nsources: [creative]\nedges: []\n"
        "---\n# google-genai\n"
    )
    assert validate_vault(tmp_path / "vault") == []


def test_stale_facts_warning(tmp_path):
    unite = write_fake_unite(tmp_path / "Unite")
    head = init_git_repo(unite)
    facts_dir = tmp_path / "vault" / "_facts"
    facts_dir.mkdir(parents=True)
    (facts_dir / "insight.json").write_text(json.dumps({"source_commit": head[:12]}))
    assert stale_facts_warnings(facts_dir, unite) == []
    (facts_dir / "insight.json").write_text(json.dumps({"source_commit": "abc1234"}))
    warnings = stale_facts_warnings(facts_dir, unite)
    assert len(warnings) == 1 and warnings[0].severity == "warning"
    assert "--changed" in warnings[0].message


def test_cli_exit_codes(tmp_path):
    vault = built_vault(tmp_path)
    assert main([str(vault)]) == 0
    (vault / "events" / "evt.asset.asset-created.md").unlink()
    assert main([str(vault)]) == 1
