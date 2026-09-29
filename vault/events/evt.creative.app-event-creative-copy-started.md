---
id: evt.creative.app-event-creative-copy-started
type: event
name: app-event::creative.copy.started
detail_type: app-event::creative.copy.started
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-started.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-started.event.ts:5
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-started.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-started.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-started.target-creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-started.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-started.version-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-started.event.ts:8
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.copy.started

## Links
- HAS_FIELD [[fld.creative.app-event-creative-copy-started.creative-id]], [[fld.creative.app-event-creative-copy-started.project-id]], [[fld.creative.app-event-creative-copy-started.target-creative-id]], [[fld.creative.app-event-creative-copy-started.version-id]]
