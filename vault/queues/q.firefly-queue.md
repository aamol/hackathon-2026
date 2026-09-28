---
id: q.firefly-queue
type: queue
name: firefly-queue
fifo: true
physical_name: firefly-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.firefly-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.firefly-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.firefly-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.firefly-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.firefly-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.firefly-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.firefly-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.firefly-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# firefly-queue

## Links
- HAS_FIELD [[fld.firefly-queue.budget]], [[fld.firefly-queue.context]], [[fld.firefly-queue.global-usage-event]], [[fld.firefly-queue.input]], [[fld.firefly-queue.resource-group-id]], [[fld.firefly-queue.resource-id]], [[fld.firefly-queue.resource-type]], [[fld.firefly-queue.version]]
