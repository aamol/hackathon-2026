---
id: evt.creative.app-event-creative-version-created
type: event
name: app-event::creative.version.created
detail_type: app-event::creative.version.created
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-version-created.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-version-created.event.ts:5
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-version-created.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-version-created.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-version-created.saved-by
  evidence: Unite/packages/wss-app-events/src/creative/creative-version-created.event.ts:8
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-version-created.version-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-version-created.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.version.created

## Links
- HAS_FIELD [[fld.creative.app-event-creative-version-created.creative-id]], [[fld.creative.app-event-creative-version-created.project-id]], [[fld.creative.app-event-creative-version-created.saved-by]], [[fld.creative.app-event-creative-version-created.version-id]]
