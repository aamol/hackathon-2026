---
id: q.insight-bulk-operation-queue
type: queue
name: insight-bulk-operation-queue
dlq: q.insight-bulk-operation-dlq
owner_service: insight
physical_name: insight-bulk-operation-queue-${self:custom.T.STAGE}
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight-bulk-operation-queue.canvas-id
  evidence: Unite/packages/insight-types/src/types.ts:473
  confidence: 0.8
  via: package:insight-types
- type: HAS_FIELD
  to: fld.insight-bulk-operation-queue.insight-id
  evidence: Unite/packages/insight-types/src/types.ts:472
  confidence: 0.8
  via: package:insight-types
- type: HAS_FIELD
  to: fld.insight-bulk-operation-queue.job-id
  evidence: Unite/packages/insight-types/src/types.ts:475
  confidence: 0.8
  via: package:insight-types
- type: HAS_FIELD
  to: fld.insight-bulk-operation-queue.project-id
  evidence: Unite/packages/insight-types/src/types.ts:474
  confidence: 0.8
  via: package:insight-types
---
# insight-bulk-operation-queue

## Links
- HAS_FIELD [[fld.insight-bulk-operation-queue.canvas-id]], [[fld.insight-bulk-operation-queue.insight-id]], [[fld.insight-bulk-operation-queue.job-id]], [[fld.insight-bulk-operation-queue.project-id]]
