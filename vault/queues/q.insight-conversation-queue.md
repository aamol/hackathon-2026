---
id: q.insight-conversation-queue
type: queue
name: insight-conversation-queue
dlq: q.insight-conversation-dlq
owner_service: insight
physical_name: insight-conversation-queue-${self:custom.T.STAGE}
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight-conversation-queue.canvas-id
  evidence: Unite/packages/insight-types/src/types.ts:459
  confidence: 0.8
  via: package:insight-types
- type: HAS_FIELD
  to: fld.insight-conversation-queue.insight-id
  evidence: Unite/packages/insight-types/src/types.ts:461
  confidence: 0.8
  via: package:insight-types
- type: HAS_FIELD
  to: fld.insight-conversation-queue.project-id
  evidence: Unite/packages/insight-types/src/types.ts:458
  confidence: 0.8
  via: package:insight-types
- type: HAS_FIELD
  to: fld.insight-conversation-queue.user-id
  evidence: Unite/packages/insight-types/src/types.ts:460
  confidence: 0.8
  via: package:insight-types
---
# insight-conversation-queue

## Links
- HAS_FIELD [[fld.insight-conversation-queue.canvas-id]], [[fld.insight-conversation-queue.insight-id]], [[fld.insight-conversation-queue.project-id]], [[fld.insight-conversation-queue.user-id]]
