---
id: q.bedrockimg-queue
type: queue
name: bedrockimg-queue
fifo: true
physical_name: bedrockimg-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.bedrockimg-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockimg-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockimg-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockimg-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockimg-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockimg-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockimg-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockimg-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# bedrockimg-queue

## Links
- HAS_FIELD [[fld.bedrockimg-queue.budget]], [[fld.bedrockimg-queue.context]], [[fld.bedrockimg-queue.global-usage-event]], [[fld.bedrockimg-queue.input]], [[fld.bedrockimg-queue.resource-group-id]], [[fld.bedrockimg-queue.resource-id]], [[fld.bedrockimg-queue.resource-type]], [[fld.bedrockimg-queue.version]]
