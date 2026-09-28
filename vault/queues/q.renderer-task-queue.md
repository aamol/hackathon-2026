---
id: q.renderer-task-queue
type: queue
name: renderer-task-queue
fifo: true
physical_name: renderer-${STAGE}-task-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.renderer-task-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-task-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-task-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-task-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-task-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-task-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-task-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-task-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# renderer-task-queue

## Links
- HAS_FIELD [[fld.renderer-task-queue.budget]], [[fld.renderer-task-queue.context]], [[fld.renderer-task-queue.global-usage-event]], [[fld.renderer-task-queue.input]], [[fld.renderer-task-queue.resource-group-id]], [[fld.renderer-task-queue.resource-id]], [[fld.renderer-task-queue.resource-type]], [[fld.renderer-task-queue.version]]
