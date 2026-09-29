---
id: evt.creative.app-event-creative-rasterization-failed
type: event
name: app-event::creative.rasterization.failed
detail_type: app-event::creative.rasterization.failed
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-failed.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-failed.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-failed.error
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-failed.event.ts:9
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-failed.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-failed.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-failed.rasterization-type
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-failed.event.ts:10
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-rasterization-failed.version-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-rasterization-failed.event.ts:8
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.rasterization.failed

## Links
- HAS_FIELD [[fld.creative.app-event-creative-rasterization-failed.creative-id]], [[fld.creative.app-event-creative-rasterization-failed.error]], [[fld.creative.app-event-creative-rasterization-failed.project-id]], [[fld.creative.app-event-creative-rasterization-failed.rasterization-type]], [[fld.creative.app-event-creative-rasterization-failed.version-id]]
