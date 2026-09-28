---
id: q.minimaxvid-queue
type: queue
name: minimaxvid-queue
fifo: true
physical_name: minimaxvid-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.minimaxvid-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.minimaxvid-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.minimaxvid-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.minimaxvid-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.minimaxvid-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.minimaxvid-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.minimaxvid-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.minimaxvid-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# minimaxvid-queue

## Links
- HAS_FIELD [[fld.minimaxvid-queue.budget]], [[fld.minimaxvid-queue.context]], [[fld.minimaxvid-queue.global-usage-event]], [[fld.minimaxvid-queue.input]], [[fld.minimaxvid-queue.resource-group-id]], [[fld.minimaxvid-queue.resource-id]], [[fld.minimaxvid-queue.resource-type]], [[fld.minimaxvid-queue.version]]
