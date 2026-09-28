"""Shared test data for tests/sync."""
from __future__ import annotations

import copy
import subprocess
from pathlib import Path

# Line numbers matter: facts below point at these exact lines.
FAKE_UNITE_FILES = {
    "services/insight/serverless.yml": (
        "service: insight\n"                                   # 1
        "functions:\n"                                         # 2
        "  assetCreated:\n"                                    # 3
        "    events:\n"                                        # 4
        "      - eventBridge:\n"                               # 5
        "          pattern:\n"                                 # 6
        "            source:\n"                                # 7
        "              - service.asset.${self:custom.T.STAGE}\n"  # 8
    ),
    "packages/insight-core/src/repo.ts": (
        "import { PutCommand } from '@aws-sdk/lib-dynamodb';\n"  # 1
        "export const save = () => client.send(new PutCommand({ TableName: process.env.INSIGHT_ENTITY_TABLE_NAME }));\n"  # 2
    ),
    "packages/asset/src/events.ts": (
        "await sendEventBridge({ source: `service.asset.${STAGE}`, detailType: 'AssetCreated',\n"  # 1
        "  detail: JSON.stringify({ assetId }) });\n"                                             # 2
    ),
}

_INSIGHT_FACTS = {
    "facts_version": "0.2",
    "service": "insight",
    "source_commit": "abc1234",
    "extracted_at": "2026-09-28T16:00:00Z",
    "nodes": [
        {"id": "svc.insight", "type": "service", "name": "insight", "path": "Unite/services/insight",
         "summary": "Generates insights."},
        {"id": "evt.asset.asset-created", "type": "event", "name": "AssetCreated",
         "source": "service.asset", "detail_type": "AssetCreated"},
        {"id": "tbl.dynamodb.insight-entities", "type": "table", "name": "insight-entities",
         "db": "dynamodb", "physical_name": "insight-${self:custom.T.STAGE}-Entities"},
    ],
    "edges": [
        {"from": "svc.insight", "type": "CONSUMES", "to": "evt.asset.asset-created",
         "evidence": "Unite/services/insight/serverless.yml:8", "snippet": "- service.asset",
         "confidence": 1.0, "via": "serverless.yml", "filter": {"record.sourceType": ["RESOURCE_MANAGER"]}},
        {"from": "svc.insight", "type": "WRITES", "to": "tbl.dynamodb.insight-entities",
         "evidence": "Unite/packages/insight-core/src/repo.ts:2", "snippet": "new PutCommand",
         "confidence": 0.8, "via": "package:insight-core"},
    ],
}

_ASSET_FACTS = {
    "facts_version": "0.2",
    "service": "asset",
    "source_commit": "abc1234",
    "extracted_at": "2026-09-28T15:00:00Z",
    "nodes": [
        {"id": "svc.asset", "type": "service", "name": "asset", "path": "Unite/services/asset"},
        {"id": "evt.asset.asset-created", "type": "event", "name": "AssetCreated",
         "source": "service.asset", "detail_type": "AssetCreated"},
        {"id": "fld.asset.asset-created.asset-id", "type": "field", "name": "assetId",
         "owner": "evt.asset.asset-created", "data_type": "string", "pii": False, "pii_category": "none"},
    ],
    "edges": [
        {"from": "svc.asset", "type": "PUBLISHES", "to": "evt.asset.asset-created",
         "evidence": "Unite/packages/asset/src/events.ts:1", "snippet": "sendEventBridge",
         "confidence": 0.8, "via": "package:asset"},
        {"from": "evt.asset.asset-created", "type": "HAS_FIELD", "to": "fld.asset.asset-created.asset-id",
         "evidence": "Unite/packages/asset/src/events.ts:2", "snippet": "assetId",
         "confidence": 0.8, "via": "package:asset"},
    ],
}


def insight_facts() -> dict:
    return copy.deepcopy(_INSIGHT_FACTS)


def asset_facts() -> dict:
    return copy.deepcopy(_ASSET_FACTS)


def write_fake_unite(root: Path) -> Path:
    for relative_path, content in FAKE_UNITE_FILES.items():
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    return root


def build_vault_dir(vault_dir: Path, datasets: list[dict]) -> None:
    from sync.build_vault import merge, write_vault
    from sync.facts import check_facts, parse_facts

    nodes, _ = merge([check_facts(parse_facts(data, data["service"]), None) for data in datasets])
    write_vault(nodes, vault_dir)


def _git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True)
    return result.stdout.strip()


def init_git_repo(root: Path) -> str:
    root.mkdir(parents=True, exist_ok=True)
    _git(root, "init", "-q")
    _git(root, "config", "user.email", "test@example.com")
    _git(root, "config", "user.name", "test")
    return commit_all(root, "init")


def commit_all(root: Path, message: str) -> str:
    _git(root, "add", "-A")
    _git(root, "commit", "-q", "--allow-empty", "-m", message)
    return _git(root, "rev-parse", "HEAD")
