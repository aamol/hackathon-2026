---
id: evt.resource.resource-failed
type: event
name: resource.failed
bus: unite-bus
detail_type: resource.failed
source: service.resource
generated_at: '2026-09-28T12:00:00Z'
contract_version: '0.2'
sources:
- asset
- insight
- resource
edges:
- type: HAS_FIELD
  to: fld.resource.resource-failed.created-by
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:61
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.resource.resource-failed.resource-id
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:60
  confidence: 0.8
  via: package:resource-manager
---
# resource.failed

## Links
- HAS_FIELD [[fld.resource.resource-failed.created-by]], [[fld.resource.resource-failed.resource-id]]
