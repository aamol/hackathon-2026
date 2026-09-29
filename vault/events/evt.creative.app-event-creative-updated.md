---
id: evt.creative.app-event-creative-updated
type: event
name: app-event::creative.updated
detail_type: app-event::creative.updated
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-updated.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-updated.event.ts:5
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-updated.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-updated.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-updated.updated-fields
  evidence: Unite/packages/wss-app-events/src/creative/creative-updated.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.updated

## Links
- HAS_FIELD [[fld.creative.app-event-creative-updated.creative-id]], [[fld.creative.app-event-creative-updated.project-id]], [[fld.creative.app-event-creative-updated.updated-fields]]
