---
id: evt.creative.app-event-creative-rasterization-started
type: event
name: app-event::creative.rasterization.started
detail_type: app-event::creative.rasterization.started
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-started.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-started.event.ts:10
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-started.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-started.event.ts:11
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-started.rasterization-type
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-started.event.ts:13
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-started.version-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-started.event.ts:12
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.rasterization.started

## Links
- HAS_FIELD [[fld.creative.app-event-creative-rasterization-started.creative-id]], [[fld.creative.app-event-creative-rasterization-started.project-id]], [[fld.creative.app-event-creative-rasterization-started.rasterization-type]], [[fld.creative.app-event-creative-rasterization-started.version-id]]
