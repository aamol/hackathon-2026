---
id: evt.creative.app-event-creative-bulk-download-prepared
type: event
name: app-event::creative.bulk-download.prepared
detail_type: app-event::creative.bulk-download.prepared
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-bulk-download-prepared.download-url
  evidence: Unite/packages/wss-app-events/src/creative/creative-bulk-download-prepared.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-bulk-download-prepared.included-creative-ids
  evidence: Unite/packages/wss-app-events/src/creative/creative-bulk-download-prepared.event.ts:8
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-bulk-download-prepared.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-bulk-download-prepared.event.ts:5
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-bulk-download-prepared.skipped-creative-ids
  evidence: Unite/packages/wss-app-events/src/creative/creative-bulk-download-prepared.event.ts:9
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-bulk-download-prepared.user-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-bulk-download-prepared.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.bulk-download.prepared

## Links
- HAS_FIELD [[fld.creative.app-event-creative-bulk-download-prepared.download-url]], [[fld.creative.app-event-creative-bulk-download-prepared.included-creative-ids]], [[fld.creative.app-event-creative-bulk-download-prepared.project-id]], [[fld.creative.app-event-creative-bulk-download-prepared.skipped-creative-ids]], [[fld.creative.app-event-creative-bulk-download-prepared.user-id]]
