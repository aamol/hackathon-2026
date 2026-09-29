---
id: q.insight-image-prompt-generation-queue
type: queue
name: insight-image-prompt-generation-queue
dlq: q.insight-image-prompt-generation-dlq
owner_service: insight
physical_name: insight-image-prompt-generation-queue-${self:custom.T.STAGE}
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight-image-prompt-generation-queue.data
  evidence: Unite/services/insight/src/application/handlers/events/eb/image-generation.ts:95
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight-image-prompt-generation-queue.id
  evidence: Unite/services/insight/src/application/handlers/events/eb/image-generation.ts:93
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight-image-prompt-generation-queue.timestamp
  evidence: Unite/services/insight/src/application/handlers/events/eb/image-generation.ts:94
  confidence: 0.9
  via: service-code
---
# insight-image-prompt-generation-queue

## Links
- HAS_FIELD [[fld.insight-image-prompt-generation-queue.data]], [[fld.insight-image-prompt-generation-queue.id]], [[fld.insight-image-prompt-generation-queue.timestamp]]
