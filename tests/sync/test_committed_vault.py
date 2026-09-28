from pathlib import Path

from sync.build_vault import main
from tests.sync.test_vault_mini import managed_notes

REPO_ROOT = Path(__file__).resolve().parents[2]
FACTS_DIR = REPO_ROOT / "vault" / "_facts"
VAULT_DIR = REPO_ROOT / "vault"


def test_committed_vault_is_up_to_date_with_its_facts(tmp_path):
    assert main(["--vault", str(tmp_path), "--facts", str(FACTS_DIR), "--skip-evidence-check"]) == 0
    assert managed_notes(tmp_path) == managed_notes(VAULT_DIR), (
        "vault/ is stale: python -m sync.build_vault --vault vault --unite ../Unite"
    )
