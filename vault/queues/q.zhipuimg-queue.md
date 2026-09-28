---
id: q.zhipuimg-queue
type: queue
name: zhipuimg-queue
fifo: true
physical_name: zhipuimg-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.zhipuimg-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.zhipuimg-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.zhipuimg-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.zhipuimg-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.zhipuimg-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.zhipuimg-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.zhipuimg-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.zhipuimg-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# zhipuimg-queue

## Links
- HAS_FIELD [[fld.zhipuimg-queue.budget]], [[fld.zhipuimg-queue.context]], [[fld.zhipuimg-queue.global-usage-event]], [[fld.zhipuimg-queue.input]], [[fld.zhipuimg-queue.resource-group-id]], [[fld.zhipuimg-queue.resource-id]], [[fld.zhipuimg-queue.resource-type]], [[fld.zhipuimg-queue.version]]
