---
id: q.bedrockvect-queue
type: queue
name: bedrockvect-queue
fifo: true
physical_name: bedrockvect-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.bedrockvect-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvect-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvect-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvect-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvect-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvect-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvect-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvect-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# bedrockvect-queue

## Links
- HAS_FIELD [[fld.bedrockvect-queue.budget]], [[fld.bedrockvect-queue.context]], [[fld.bedrockvect-queue.global-usage-event]], [[fld.bedrockvect-queue.input]], [[fld.bedrockvect-queue.resource-group-id]], [[fld.bedrockvect-queue.resource-id]], [[fld.bedrockvect-queue.resource-type]], [[fld.bedrockvect-queue.version]]
