---
id: q.asset-pmh-sync-queue
type: queue
name: asset-pmh-sync-queue
fifo: true
owner_service: asset
physical_name: asset-${self:custom.T.STAGE}-PmhSync-queue.fifo
generated_at: '2026-09-28T09:36:30Z'
contract_version: '0.2'
sources:
- asset
edges:
- type: HAS_FIELD
  to: fld.asset-pmh-sync-queue.created-by
  evidence: Unite/packages/asset-types/src/pmh.ts:61
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset-pmh-sync-queue.creative-id
  evidence: Unite/packages/asset-types/src/pmh.ts:81
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset-pmh-sync-queue.creative-name
  evidence: Unite/packages/asset-types/src/pmh.ts:86
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset-pmh-sync-queue.entity-type
  evidence: Unite/packages/asset-types/src/pmh.ts:60
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset-pmh-sync-queue.id
  evidence: Unite/packages/asset-types/src/pmh.ts:58
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset-pmh-sync-queue.project-id
  evidence: Unite/packages/asset-types/src/pmh.ts:57
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset-pmh-sync-queue.submission-uuid
  evidence: Unite/packages/asset-types/src/pmh.ts:59
  confidence: 0.8
  via: package:asset-types
- type: HAS_FIELD
  to: fld.asset-pmh-sync-queue.wpp-object-url
  evidence: Unite/packages/asset-types/src/pmh.ts:87
  confidence: 0.8
  via: package:asset-types
---
# asset-pmh-sync-queue

## Links
- HAS_FIELD [[fld.asset-pmh-sync-queue.created-by]], [[fld.asset-pmh-sync-queue.creative-id]], [[fld.asset-pmh-sync-queue.creative-name]], [[fld.asset-pmh-sync-queue.entity-type]], [[fld.asset-pmh-sync-queue.id]], [[fld.asset-pmh-sync-queue.project-id]], [[fld.asset-pmh-sync-queue.submission-uuid]], [[fld.asset-pmh-sync-queue.wpp-object-url]]
