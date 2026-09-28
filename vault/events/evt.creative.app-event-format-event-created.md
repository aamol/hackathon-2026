---
id: evt.creative.app-event-format-event-created
type: event
name: app-event::format.event.created
detail_type: app-event::format.event.created
source: service.creative
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-format-event-created.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/format-event-created.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-format-event-created.creative-version-id
  evidence: Unite/packages/wss-app-events/src/creative/format-event-created.event.ts:10
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-format-event-created.event-type
  evidence: Unite/packages/wss-app-events/src/creative/format-event-created.event.ts:9
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-format-event-created.format-id
  evidence: Unite/packages/wss-app-events/src/creative/format-event-created.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-format-event-created.format-version-id
  evidence: Unite/packages/wss-app-events/src/creative/format-event-created.event.ts:8
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-format-event-created.project-id
  evidence: Unite/packages/wss-app-events/src/creative/format-event-created.event.ts:5
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-format-event-created.timestamp
  evidence: Unite/packages/wss-app-events/src/creative/format-event-created.event.ts:11
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::format.event.created

## Links
- HAS_FIELD [[fld.creative.app-event-format-event-created.creative-id]], [[fld.creative.app-event-format-event-created.creative-version-id]], [[fld.creative.app-event-format-event-created.event-type]], [[fld.creative.app-event-format-event-created.format-id]], [[fld.creative.app-event-format-event-created.format-version-id]], [[fld.creative.app-event-format-event-created.project-id]], [[fld.creative.app-event-format-event-created.timestamp]]
