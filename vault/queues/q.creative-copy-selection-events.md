---
id: q.creative-copy-selection-events
type: queue
name: creative-copy-selection-events
dlq: q.creative-events-dlq
owner_service: creative
physical_name: creative-${self:custom.T.STAGE}-copy-selection-events
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative-copy-selection-events.entity-type
  evidence: Unite/services/creative/src/models/copy-selection-event-dto.ts:9
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.creative-copy-selection-events.id
  evidence: Unite/services/creative/src/models/copy-selection-event-dto.ts:25
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.creative-copy-selection-events.mode
  evidence: Unite/services/creative/src/models/copy-selection-event-dto.ts:13
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.creative-copy-selection-events.source-project-id
  evidence: Unite/services/creative/src/models/copy-selection-event-dto.ts:17
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.creative-copy-selection-events.target-project-id
  evidence: Unite/services/creative/src/models/copy-selection-event-dto.ts:21
  confidence: 0.9
  via: service-code
---
# creative-copy-selection-events

## Links
- HAS_FIELD [[fld.creative-copy-selection-events.entity-type]], [[fld.creative-copy-selection-events.id]], [[fld.creative-copy-selection-events.mode]], [[fld.creative-copy-selection-events.source-project-id]], [[fld.creative-copy-selection-events.target-project-id]]
