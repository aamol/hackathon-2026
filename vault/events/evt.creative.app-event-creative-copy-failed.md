---
id: evt.creative.app-event-creative-copy-failed
type: event
name: app-event::creative.copy.failed
detail_type: app-event::creative.copy.failed
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-failed.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-failed.event.ts:5
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-failed.error
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-failed.event.ts:9
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-failed.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-failed.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-failed.target-creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-failed.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-copy-failed.version-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-copy-failed.event.ts:8
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.copy.failed

## Links
- HAS_FIELD [[fld.creative.app-event-creative-copy-failed.creative-id]], [[fld.creative.app-event-creative-copy-failed.error]], [[fld.creative.app-event-creative-copy-failed.project-id]], [[fld.creative.app-event-creative-copy-failed.target-creative-id]], [[fld.creative.app-event-creative-copy-failed.version-id]]
