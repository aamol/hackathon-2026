---
id: evt.creative.app-event-creative-bulk-download-failed
type: event
name: app-event::creative.bulk-download.failed
detail_type: app-event::creative.bulk-download.failed
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-bulk-download-failed.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-bulk-download-failed.event.ts:5
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-bulk-download-failed.skipped-creative-ids
  evidence: Unite/packages/wss-app-events/src/creative/creative-bulk-download-failed.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-bulk-download-failed.user-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-bulk-download-failed.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.bulk-download.failed

## Links
- HAS_FIELD [[fld.creative.app-event-creative-bulk-download-failed.project-id]], [[fld.creative.app-event-creative-bulk-download-failed.skipped-creative-ids]], [[fld.creative.app-event-creative-bulk-download-failed.user-id]]
