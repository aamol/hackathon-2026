---
id: q.insight-brand-colours-extract-queue
type: queue
name: insight-brand-colours-extract-queue
dlq: q.insight-brand-colours-extract-dlq
owner_service: insight
physical_name: insight-brand-colours-extract-queue-${self:custom.T.STAGE}
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight-brand-colours-extract-queue.data
  evidence: Unite/services/insight/src/application/handlers/events/eb/canvas.ts:29
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight-brand-colours-extract-queue.id
  evidence: Unite/services/insight/src/application/handlers/events/eb/canvas.ts:27
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight-brand-colours-extract-queue.timestamp
  evidence: Unite/services/insight/src/application/handlers/events/eb/canvas.ts:28
  confidence: 0.9
  via: service-code
---
# insight-brand-colours-extract-queue

## Links
- HAS_FIELD [[fld.insight-brand-colours-extract-queue.data]], [[fld.insight-brand-colours-extract-queue.id]], [[fld.insight-brand-colours-extract-queue.timestamp]]
