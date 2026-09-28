---
id: evt.asset.asset-hard-deleted
type: event
name: AssetHardDeleted
detail_type: AssetHardDeleted
source: service.asset
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- asset
- creative
edges:
- type: HAS_FIELD
  to: fld.asset.asset-hard-deleted.asset-public
  evidence: Unite/packages/asset-types/src/index.ts:814
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-hard-deleted.entity-ids
  evidence: Unite/packages/asset-types/src/index.ts:813
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-hard-deleted.entity-type
  evidence: Unite/packages/asset-types/src/index.ts:812
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-hard-deleted.record
  evidence: Unite/packages/asset-types/src/index.ts:811
  confidence: 0.9
  via: package:asset-types
---
# AssetHardDeleted

## Links
- HAS_FIELD [[fld.asset.asset-hard-deleted.asset-public]], [[fld.asset.asset-hard-deleted.entity-ids]], [[fld.asset.asset-hard-deleted.entity-type]], [[fld.asset.asset-hard-deleted.record]]
