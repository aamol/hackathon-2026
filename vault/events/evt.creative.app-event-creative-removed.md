---
id: evt.creative.app-event-creative-removed
type: event
name: app-event::creative.removed
detail_type: app-event::creative.removed
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-removed.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-removed.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-removed.entity-type
  evidence: Unite/packages/wss-app-events/src/creative/creative-removed.event.ts:9
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-removed.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-removed.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-removed.removed-by
  evidence: Unite/packages/wss-app-events/src/creative/creative-removed.event.ts:8
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.removed

## Links
- HAS_FIELD [[fld.creative.app-event-creative-removed.creative-id]], [[fld.creative.app-event-creative-removed.entity-type]], [[fld.creative.app-event-creative-removed.project-id]], [[fld.creative.app-event-creative-removed.removed-by]]
