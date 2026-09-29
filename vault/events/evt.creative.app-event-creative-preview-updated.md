---
id: evt.creative.app-event-creative-preview-updated
type: event
name: app-event::creative.preview.updated
detail_type: app-event::creative.preview.updated
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-preview-updated.asset-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-preview-updated.event.ts:10
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-preview-updated.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-preview-updated.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-preview-updated.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-preview-updated.event.ts:8
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-preview-updated.url
  evidence: Unite/packages/wss-app-events/src/creative/creative-preview-updated.event.ts:11
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-preview-updated.user-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-preview-updated.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-preview-updated.version
  evidence: Unite/packages/wss-app-events/src/creative/creative-preview-updated.event.ts:9
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.preview.updated

## Links
- HAS_FIELD [[fld.creative.app-event-creative-preview-updated.asset-id]], [[fld.creative.app-event-creative-preview-updated.creative-id]], [[fld.creative.app-event-creative-preview-updated.project-id]], [[fld.creative.app-event-creative-preview-updated.url]], [[fld.creative.app-event-creative-preview-updated.user-id]], [[fld.creative.app-event-creative-preview-updated.version]]
