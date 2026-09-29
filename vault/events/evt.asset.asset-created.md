---
id: evt.asset.asset-created
type: event
name: AssetCreated
detail_type: AssetCreated
source: service.asset
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- asset
- creative
- insight
edges:
- type: HAS_FIELD
  to: fld.asset.asset-created.asset-public
  evidence: Unite/packages/asset-types/src/index.ts:814
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-created.entity-ids
  evidence: Unite/packages/asset-types/src/index.ts:813
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-created.entity-type
  evidence: Unite/packages/asset-types/src/index.ts:812
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-created.record
  evidence: Unite/packages/asset-types/src/index.ts:811
  confidence: 0.8
  via: package:asset-types
---
# AssetCreated

## Links
- HAS_FIELD [[fld.asset.asset-created.asset-public]], [[fld.asset.asset-created.entity-ids]], [[fld.asset.asset-created.entity-type]], [[fld.asset.asset-created.record]]
