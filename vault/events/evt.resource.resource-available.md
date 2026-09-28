---
id: evt.resource.resource-available
type: event
name: resource.available
detail_type: resource.available
source: service.resource
generated_at: '2026-09-28T09:36:30Z'
contract_version: '0.2'
sources:
- asset
- resource
edges:
- type: HAS_FIELD
  to: fld.resource.resource-available.output
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:59
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.resource.resource-available.resource-callback-source
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:63
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.resource.resource-available.resource-group-id
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:61
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.resource.resource-available.resource-id
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:60
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.resource.resource-available.resource-type
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:62
  confidence: 0.8
  via: package:resource-manager
---
# resource.available

## Links
- HAS_FIELD [[fld.resource.resource-available.output]], [[fld.resource.resource-available.resource-callback-source]], [[fld.resource.resource-available.resource-group-id]], [[fld.resource.resource-available.resource-id]], [[fld.resource.resource-available.resource-type]]
