---
id: evt.asset.asset-deleted
type: event
name: AssetDeleted
detail_type: AssetDeleted
source: service.asset
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- asset
- creative
edges:
- type: HAS_FIELD
  to: fld.asset.asset-deleted.asset-public
  evidence: Unite/packages/asset-types/src/index.ts:814
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-deleted.entity-ids
  evidence: Unite/packages/asset-types/src/index.ts:813
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-deleted.entity-type
  evidence: Unite/packages/asset-types/src/index.ts:812
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-deleted.record
  evidence: Unite/packages/asset-types/src/index.ts:811
  confidence: 0.8
  via: package:asset-types
---
# AssetDeleted

## Links
- HAS_FIELD [[fld.asset.asset-deleted.asset-public]], [[fld.asset.asset-deleted.entity-ids]], [[fld.asset.asset-deleted.entity-type]], [[fld.asset.asset-deleted.record]]
