---
id: q.bedrockvid-queue
type: queue
name: bedrockvid-queue
fifo: true
physical_name: bedrockvid-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.bedrockvid-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvid-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvid-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvid-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvid-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvid-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvid-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bedrockvid-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# bedrockvid-queue

## Links
- HAS_FIELD [[fld.bedrockvid-queue.budget]], [[fld.bedrockvid-queue.context]], [[fld.bedrockvid-queue.global-usage-event]], [[fld.bedrockvid-queue.input]], [[fld.bedrockvid-queue.resource-group-id]], [[fld.bedrockvid-queue.resource-id]], [[fld.bedrockvid-queue.resource-type]], [[fld.bedrockvid-queue.version]]
