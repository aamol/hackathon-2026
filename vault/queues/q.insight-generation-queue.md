---
id: q.insight-generation-queue
type: queue
name: insight-generation-queue
dlq: q.insight-generation-dlq
owner_service: insight
physical_name: insight-generation-queue-${self:custom.T.STAGE}
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight-generation-queue.canvas-id
  evidence: Unite/services/insight/src/domain/types/queue-messages.ts:16
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight-generation-queue.insight-id
  evidence: Unite/services/insight/src/domain/types/queue-messages.ts:15
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight-generation-queue.project-id
  evidence: Unite/services/insight/src/domain/types/queue-messages.ts:17
  confidence: 0.9
  via: service-code
---
# insight-generation-queue

## Links
- HAS_FIELD [[fld.insight-generation-queue.canvas-id]], [[fld.insight-generation-queue.insight-id]], [[fld.insight-generation-queue.project-id]]
