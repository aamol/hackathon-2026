---
id: q.insight-editing-queue
type: queue
name: insight-editing-queue
dlq: q.insight-editing-dlq
fifo: true
owner_service: insight
physical_name: insight-editing-queue-${self:custom.T.STAGE}.fifo
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight-editing-queue.canvas-id
  evidence: Unite/packages/insight-types/src/types.ts:353
  confidence: 0.8
  via: package:insight-types
- type: HAS_FIELD
  to: fld.insight-editing-queue.insight-id
  evidence: Unite/packages/insight-types/src/types.ts:352
  confidence: 0.8
  via: package:insight-types
- type: HAS_FIELD
  to: fld.insight-editing-queue.project-id
  evidence: Unite/packages/insight-types/src/types.ts:354
  confidence: 0.8
  via: package:insight-types
---
# insight-editing-queue

## Links
- HAS_FIELD [[fld.insight-editing-queue.canvas-id]], [[fld.insight-editing-queue.insight-id]], [[fld.insight-editing-queue.project-id]]
