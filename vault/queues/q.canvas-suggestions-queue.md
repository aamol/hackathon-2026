---
id: q.canvas-suggestions-queue
type: queue
name: canvas-suggestions-queue
dlq: q.canvas-suggestions-dlq
owner_service: insight
physical_name: canvas-suggestions-queue-${self:custom.T.STAGE}
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.canvas-suggestions-queue.job-id
  evidence: Unite/packages/insight-types/src/types.ts:495
  confidence: 0.8
  via: package:insight-types
---
# canvas-suggestions-queue

## Links
- HAS_FIELD [[fld.canvas-suggestions-queue.job-id]]
