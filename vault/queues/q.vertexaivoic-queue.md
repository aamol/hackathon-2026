---
id: q.vertexaivoic-queue
type: queue
name: vertexaivoic-queue
fifo: true
physical_name: vertexaivoic-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.vertexaivoic-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivoic-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivoic-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivoic-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivoic-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivoic-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivoic-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivoic-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# vertexaivoic-queue

## Links
- HAS_FIELD [[fld.vertexaivoic-queue.budget]], [[fld.vertexaivoic-queue.context]], [[fld.vertexaivoic-queue.global-usage-event]], [[fld.vertexaivoic-queue.input]], [[fld.vertexaivoic-queue.resource-group-id]], [[fld.vertexaivoic-queue.resource-id]], [[fld.vertexaivoic-queue.resource-type]], [[fld.vertexaivoic-queue.version]]
