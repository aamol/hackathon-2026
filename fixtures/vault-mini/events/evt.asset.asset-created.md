---
id: evt.asset.asset-created
type: event
name: AssetCreated
detail_type: AssetCreated
source: service.asset
generated_at: '2026-09-28T12:00:00Z'
contract_version: '0.2'
sources:
- asset
- insight
edges:
- type: HAS_FIELD
  to: fld.asset.asset-created.asset-id
  evidence: Unite/packages/asset/src/events/asset-created.ts:31
  confidence: 0.8
  via: package:asset
---
# AssetCreated

## Links
- HAS_FIELD [[fld.asset.asset-created.asset-id]]
