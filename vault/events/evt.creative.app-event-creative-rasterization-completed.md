---
id: evt.creative.app-event-creative-rasterization-completed
type: event
name: app-event::creative.rasterization.completed
detail_type: app-event::creative.rasterization.completed
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-completed.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-completed.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-completed.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-completed.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-completed.rasterization-type
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-completed.event.ts:9
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-completed.version-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-completed.event.ts:8
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.rasterization.completed

## Links
- HAS_FIELD [[fld.creative.app-event-creative-rasterization-completed.creative-id]], [[fld.creative.app-event-creative-rasterization-completed.project-id]], [[fld.creative.app-event-creative-rasterization-completed.rasterization-type]], [[fld.creative.app-event-creative-rasterization-completed.version-id]]
