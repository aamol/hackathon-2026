---
id: q.fileparse-queue
type: queue
name: fileparse-queue
fifo: true
physical_name: fileparse-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.fileparse-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.fileparse-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.fileparse-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.fileparse-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.fileparse-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.fileparse-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.fileparse-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.fileparse-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# fileparse-queue

## Links
- HAS_FIELD [[fld.fileparse-queue.budget]], [[fld.fileparse-queue.context]], [[fld.fileparse-queue.global-usage-event]], [[fld.fileparse-queue.input]], [[fld.fileparse-queue.resource-group-id]], [[fld.fileparse-queue.resource-id]], [[fld.fileparse-queue.resource-type]], [[fld.fileparse-queue.version]]
