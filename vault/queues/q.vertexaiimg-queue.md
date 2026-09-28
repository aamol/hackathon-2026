---
id: q.vertexaiimg-queue
type: queue
name: vertexaiimg-queue
fifo: true
physical_name: vertexaiimg-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.vertexaiimg-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaiimg-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaiimg-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaiimg-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaiimg-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaiimg-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaiimg-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaiimg-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# vertexaiimg-queue

## Links
- HAS_FIELD [[fld.vertexaiimg-queue.budget]], [[fld.vertexaiimg-queue.context]], [[fld.vertexaiimg-queue.global-usage-event]], [[fld.vertexaiimg-queue.input]], [[fld.vertexaiimg-queue.resource-group-id]], [[fld.vertexaiimg-queue.resource-id]], [[fld.vertexaiimg-queue.resource-type]], [[fld.vertexaiimg-queue.version]]
