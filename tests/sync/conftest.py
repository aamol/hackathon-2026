import json
from pathlib import Path

import pytest

from tests.sync.factories import write_fake_unite


@pytest.fixture
def fake_unite(tmp_path) -> Path:
    return write_fake_unite(tmp_path / "Unite")


@pytest.fixture
def write_facts(tmp_path):
    facts_dir = tmp_path / "facts"
    facts_dir.mkdir()

    def _write(data: dict, file_name: str | None = None) -> Path:
        path = facts_dir / (file_name or f"{data['service']}.json")
        path.write_text(json.dumps(data))
        return path

    return _write
