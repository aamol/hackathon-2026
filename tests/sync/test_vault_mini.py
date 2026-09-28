from pathlib import Path

from sync.build_vault import MANAGED_FOLDERS, main
from sync.validate import read_frontmatter, validate_vault

REPO_ROOT = Path(__file__).resolve().parents[2]
FACTS_DIR = REPO_ROOT / "fixtures" / "vault-mini-facts"
VAULT_DIR = REPO_ROOT / "fixtures" / "vault-mini"


def managed_notes(vault: Path) -> dict[str, str]:
    return {str(path.relative_to(vault)): path.read_text()
            for folder in MANAGED_FOLDERS for path in sorted((vault / folder).glob("*.md"))}


def test_vault_mini_is_valid():
    assert [str(p) for p in validate_vault(VAULT_DIR) if p.severity == "error"] == []


def test_vault_mini_is_up_to_date_with_its_facts(tmp_path):
    assert main(["--vault", str(tmp_path), "--facts", str(FACTS_DIR), "--skip-evidence-check"]) == 0
    assert managed_notes(tmp_path) == managed_notes(VAULT_DIR), (
        "fixtures/vault-mini is stale: python -m sync.build_vault --vault fixtures/vault-mini "
        "--facts fixtures/vault-mini-facts --skip-evidence-check"
    )


def test_vault_mini_shape():
    notes = managed_notes(VAULT_DIR)
    assert len(notes) == 15
    created_by = read_frontmatter(VAULT_DIR / "fields" / "fld.resource.resource-failed.created-by.md")
    assert created_by["pii"] is True
    tested = {edge["to"] for path in (VAULT_DIR / "tests").glob("*.md") for edge in read_frontmatter(path)["edges"]}
    assert "svc.insight" in tested
    assert "svc.asset" not in tested  # asset is the "untested consumer" in the demo question
