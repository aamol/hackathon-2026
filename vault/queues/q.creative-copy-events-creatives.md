---
id: q.creative-copy-events-creatives
type: queue
name: creative-copy-events-creatives
dlq: q.creative-events-dlq
owner_service: svc.creative
physical_name: creative-${self:custom.T.STAGE}-copy-events-creatives
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative-copy-events-creatives.id
  evidence: Unite/services/creative/src/models/copy-creative-event-dto.ts:21
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.creative-copy-events-creatives.job-type
  evidence: Unite/services/creative/src/models/copy-creative-event-dto.ts:9
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.creative-copy-events-creatives.source-project-id
  evidence: Unite/services/creative/src/models/copy-creative-event-dto.ts:13
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.creative-copy-events-creatives.target-project-id
  evidence: Unite/services/creative/src/models/copy-creative-event-dto.ts:17
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.creative-copy-events-creatives.version-id
  evidence: Unite/services/creative/src/models/copy-creative-event-dto.ts:26
  confidence: 0.9
  via: service-code
---
# creative-copy-events-creatives

## Links
- HAS_FIELD [[fld.creative-copy-events-creatives.id]], [[fld.creative-copy-events-creatives.job-type]], [[fld.creative-copy-events-creatives.source-project-id]], [[fld.creative-copy-events-creatives.target-project-id]], [[fld.creative-copy-events-creatives.version-id]]
