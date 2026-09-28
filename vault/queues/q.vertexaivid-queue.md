---
id: q.vertexaivid-queue
type: queue
name: vertexaivid-queue
fifo: true
physical_name: vertexaivid-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.vertexaivid-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivid-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivid-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivid-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivid-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivid-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivid-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.vertexaivid-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# vertexaivid-queue

## Links
- HAS_FIELD [[fld.vertexaivid-queue.budget]], [[fld.vertexaivid-queue.context]], [[fld.vertexaivid-queue.global-usage-event]], [[fld.vertexaivid-queue.input]], [[fld.vertexaivid-queue.resource-group-id]], [[fld.vertexaivid-queue.resource-id]], [[fld.vertexaivid-queue.resource-type]], [[fld.vertexaivid-queue.version]]
