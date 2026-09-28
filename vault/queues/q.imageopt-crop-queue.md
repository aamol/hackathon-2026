---
id: q.imageopt-crop-queue
type: queue
name: imageopt-crop-queue
fifo: true
physical_name: imageopt-${STAGE}-crop-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.imageopt-crop-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.imageopt-crop-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.imageopt-crop-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.imageopt-crop-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.imageopt-crop-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.imageopt-crop-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.imageopt-crop-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.imageopt-crop-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# imageopt-crop-queue

## Links
- HAS_FIELD [[fld.imageopt-crop-queue.budget]], [[fld.imageopt-crop-queue.context]], [[fld.imageopt-crop-queue.global-usage-event]], [[fld.imageopt-crop-queue.input]], [[fld.imageopt-crop-queue.resource-group-id]], [[fld.imageopt-crop-queue.resource-id]], [[fld.imageopt-crop-queue.resource-type]], [[fld.imageopt-crop-queue.version]]
