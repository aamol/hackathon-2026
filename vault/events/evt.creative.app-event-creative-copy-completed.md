---
id: evt.creative.app-event-creative-copy-completed
type: event
name: app-event::creative.copy.completed
detail_type: app-event::creative.copy.completed
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-completed.copied-by
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-completed.event.ts:9
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-completed.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-completed.event.ts:5
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-completed.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-completed.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-completed.target-creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-completed.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-completed.version-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-completed.event.ts:8
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.copy.completed

## Links
- HAS_FIELD [[fld.creative.app-event-creative-copy-completed.copied-by]], [[fld.creative.app-event-creative-copy-completed.creative-id]], [[fld.creative.app-event-creative-copy-completed.project-id]], [[fld.creative.app-event-creative-copy-completed.target-creative-id]], [[fld.creative.app-event-creative-copy-completed.version-id]]
