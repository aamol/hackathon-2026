---
id: q.renderer-worker-queue
type: queue
name: renderer-worker-queue
fifo: true
physical_name: renderer-${STAGE}-worker-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.renderer-worker-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-worker-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-worker-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-worker-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-worker-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-worker-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-worker-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.renderer-worker-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# renderer-worker-queue

## Links
- HAS_FIELD [[fld.renderer-worker-queue.budget]], [[fld.renderer-worker-queue.context]], [[fld.renderer-worker-queue.global-usage-event]], [[fld.renderer-worker-queue.input]], [[fld.renderer-worker-queue.resource-group-id]], [[fld.renderer-worker-queue.resource-id]], [[fld.renderer-worker-queue.resource-type]], [[fld.renderer-worker-queue.version]]
