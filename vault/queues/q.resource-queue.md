---
id: q.resource-queue
type: queue
name: resource-queue
fifo: true
owner_service: resource
physical_name: resource-${self:custom.T.STAGE}-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.resource-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:305
  confidence: 0.8
  via: package:resource-manager
---
# resource-queue

## Links
- HAS_FIELD [[fld.resource-queue.resource-type]]
