---
id: evt.asset.asset-pmh-sync-completed
type: event
name: AssetPmhSyncCompleted
detail_type: AssetPmhSyncCompleted
source: service.asset
generated_at: '2026-09-28T10:17:00Z'
contract_version: '0.2'
sources:
- asset
edges:
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-completed.created-by
  evidence: Unite/packages/asset-types/src/pmh.ts:151
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-completed.creative-id
  evidence: Unite/packages/asset-types/src/pmh.ts:152
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-completed.display-name
  evidence: Unite/packages/asset-types/src/pmh.ts:154
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-completed.entity-type
  evidence: Unite/packages/asset-types/src/pmh.ts:149
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-completed.id
  evidence: Unite/packages/asset-types/src/pmh.ts:148
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-completed.project-id
  evidence: Unite/packages/asset-types/src/pmh.ts:147
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-completed.results
  evidence: Unite/packages/asset-types/src/pmh.ts:153
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-completed.status
  evidence: Unite/packages/asset-types/src/pmh.ts:155
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-completed.submission-uuid
  evidence: Unite/packages/asset-types/src/pmh.ts:150
  confidence: 0.8
  via: package:asset-types
---
# AssetPmhSyncCompleted

## Links
- HAS_FIELD [[fld.asset.asset-pmh-sync-completed.created-by]], [[fld.asset.asset-pmh-sync-completed.creative-id]], [[fld.asset.asset-pmh-sync-completed.display-name]], [[fld.asset.asset-pmh-sync-completed.entity-type]], [[fld.asset.asset-pmh-sync-completed.id]], [[fld.asset.asset-pmh-sync-completed.project-id]], [[fld.asset.asset-pmh-sync-completed.results]], [[fld.asset.asset-pmh-sync-completed.status]], [[fld.asset.asset-pmh-sync-completed.submission-uuid]]
