---
id: q.python-markitdown-queue
type: queue
name: python-markitdown-queue
fifo: true
physical_name: python-markitdown-${STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.python-markitdown-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.python-markitdown-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.python-markitdown-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.python-markitdown-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.python-markitdown-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.python-markitdown-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.python-markitdown-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.python-markitdown-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# python-markitdown-queue

## Links
- HAS_FIELD [[fld.python-markitdown-queue.budget]], [[fld.python-markitdown-queue.context]], [[fld.python-markitdown-queue.global-usage-event]], [[fld.python-markitdown-queue.input]], [[fld.python-markitdown-queue.resource-group-id]], [[fld.python-markitdown-queue.resource-id]], [[fld.python-markitdown-queue.resource-type]], [[fld.python-markitdown-queue.version]]
