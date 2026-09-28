---
id: evt.resource.resource-failed
type: event
name: resource.failed
detail_type: resource.failed
source: service.resource
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.resource.resource-failed.output
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:59
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.resource.resource-failed.resource-callback-source
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:63
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.resource.resource-failed.resource-group-id
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:61
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.resource.resource-failed.resource-id
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:60
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.resource.resource-failed.resource-type
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:62
  confidence: 0.8
  via: package:resource-manager
---
# resource.failed

## Links
- HAS_FIELD [[fld.resource.resource-failed.output]], [[fld.resource.resource-failed.resource-callback-source]], [[fld.resource.resource-failed.resource-group-id]], [[fld.resource.resource-failed.resource-id]], [[fld.resource.resource-failed.resource-type]]
