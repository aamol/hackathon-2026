---
id: evt.asset.asset-updated
type: event
name: AssetUpdated
detail_type: AssetUpdated
source: service.asset
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- asset
- creative
edges:
- type: HAS_FIELD
  to: fld.asset.asset-updated.asset-public
  evidence: Unite/packages/asset-types/src/index.ts:814
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-updated.entity-ids
  evidence: Unite/packages/asset-types/src/index.ts:813
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-updated.entity-type
  evidence: Unite/packages/asset-types/src/index.ts:812
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-updated.record
  evidence: Unite/packages/asset-types/src/index.ts:811
  confidence: 0.9
  via: package:asset-types
---
# AssetUpdated

## Links
- HAS_FIELD [[fld.asset.asset-updated.asset-public]], [[fld.asset.asset-updated.entity-ids]], [[fld.asset.asset-updated.entity-type]], [[fld.asset.asset-updated.record]]
