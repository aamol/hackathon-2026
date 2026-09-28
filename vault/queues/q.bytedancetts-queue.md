---
id: q.bytedancetts-queue
type: queue
name: bytedancetts-queue
fifo: true
physical_name: bytedancetts-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.bytedancetts-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bytedancetts-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bytedancetts-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bytedancetts-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bytedancetts-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bytedancetts-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bytedancetts-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.bytedancetts-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# bytedancetts-queue

## Links
- HAS_FIELD [[fld.bytedancetts-queue.budget]], [[fld.bytedancetts-queue.context]], [[fld.bytedancetts-queue.global-usage-event]], [[fld.bytedancetts-queue.input]], [[fld.bytedancetts-queue.resource-group-id]], [[fld.bytedancetts-queue.resource-id]], [[fld.bytedancetts-queue.resource-type]], [[fld.bytedancetts-queue.version]]
