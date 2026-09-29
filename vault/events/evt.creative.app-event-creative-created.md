---
id: evt.creative.app-event-creative-created
type: event
name: app-event::creative.created
detail_type: app-event::creative.created
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.app-event-creative-created.created-by
  evidence: Unite/packages/wss-app-events/src/creative/creative-created.event.ts:10
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-created.creative-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-created.event.ts:6
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-created.entity-type
  evidence: Unite/packages/wss-app-events/src/creative/creative-created.event.ts:11
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-created.name
  evidence: Unite/packages/wss-app-events/src/creative/creative-created.event.ts:8
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-created.project-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-created.event.ts:7
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-created.template-id
  evidence: Unite/packages/wss-app-events/src/creative/creative-created.event.ts:12
  confidence: 0.8
  via: package:wss-app-events
- type: HAS_FIELD
  to: fld.creative.app-event-creative-created.type
  evidence: Unite/packages/wss-app-events/src/creative/creative-created.event.ts:9
  confidence: 0.8
  via: package:wss-app-events
---
# app-event::creative.created

## Links
- HAS_FIELD [[fld.creative.app-event-creative-created.created-by]], [[fld.creative.app-event-creative-created.creative-id]], [[fld.creative.app-event-creative-created.entity-type]], [[fld.creative.app-event-creative-created.name]], [[fld.creative.app-event-creative-created.project-id]], [[fld.creative.app-event-creative-created.template-id]], [[fld.creative.app-event-creative-created.type]]
