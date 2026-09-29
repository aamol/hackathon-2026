---
id: evt.creative.app-event-creative-shared
type: event
name: app-event::creative.shared
detail_type: app-event::creative.shared
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-shared.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-shared.event.ts:5
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-shared.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-shared.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-shared.share-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-shared.event.ts:8
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-shared.shared-by
  evidence: Unite/packages/wss-app-events/src/creative/creative-shared.event.ts:9
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-shared.version-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-shared.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.shared

## Links
- HAS_FIELD [[fld.creative.app-event-creative-shared.creative-id]], [[fld.creative.app-event-creative-shared.project-id]], [[fld.creative.app-event-creative-shared.share-id]], [[fld.creative.app-event-creative-shared.shared-by]], [[fld.creative.app-event-creative-shared.version-id]]
