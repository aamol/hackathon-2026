---
id: evt.asset.asset-pmh-sync-started
type: event
name: AssetPmhSyncStarted
detail_type: AssetPmhSyncStarted
source: service.asset
generated_at: '2026-09-28T10:17:00Z'
contract_version: '0.2'
sources:
- asset
edges:
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-started.created-by
  evidence: Unite/packages/asset-types/src/pmh.ts:151
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-started.creative-id
  evidence: Unite/packages/asset-types/src/pmh.ts:152
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-started.display-name
  evidence: Unite/packages/asset-types/src/pmh.ts:154
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-started.entity-type
  evidence: Unite/packages/asset-types/src/pmh.ts:149
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-started.id
  evidence: Unite/packages/asset-types/src/pmh.ts:148
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-started.project-id
  evidence: Unite/packages/asset-types/src/pmh.ts:147
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-started.results
  evidence: Unite/packages/asset-types/src/pmh.ts:153
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-started.status
  evidence: Unite/packages/asset-types/src/pmh.ts:155
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset.asset-pmh-sync-started.submission-uuid
  evidence: Unite/packages/asset-types/src/pmh.ts:150
  confidence: 0.8
  via: package:asset-types
---
# AssetPmhSyncStarted

## Links
- HAS_FIELD [[fld.asset.asset-pmh-sync-started.created-by]], [[fld.asset.asset-pmh-sync-started.creative-id]], [[fld.asset.asset-pmh-sync-started.display-name]], [[fld.asset.asset-pmh-sync-started.entity-type]], [[fld.asset.asset-pmh-sync-started.id]], [[fld.asset.asset-pmh-sync-started.project-id]], [[fld.asset.asset-pmh-sync-started.results]], [[fld.asset.asset-pmh-sync-started.status]], [[fld.asset.asset-pmh-sync-started.submission-uuid]]
