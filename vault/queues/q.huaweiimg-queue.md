---
id: q.huaweiimg-queue
type: queue
name: huaweiimg-queue
fifo: true
physical_name: huaweiimg-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.huaweiimg-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.huaweiimg-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.huaweiimg-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.huaweiimg-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.huaweiimg-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.huaweiimg-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.huaweiimg-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.huaweiimg-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# huaweiimg-queue

## Links
- HAS_FIELD [[fld.huaweiimg-queue.budget]], [[fld.huaweiimg-queue.context]], [[fld.huaweiimg-queue.global-usage-event]], [[fld.huaweiimg-queue.input]], [[fld.huaweiimg-queue.resource-group-id]], [[fld.huaweiimg-queue.resource-id]], [[fld.huaweiimg-queue.resource-type]], [[fld.huaweiimg-queue.version]]
