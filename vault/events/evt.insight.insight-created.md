---
id: evt.insight.insight-created
type: event
name: INSIGHT.CREATED
bus: default
detail_type: INSIGHT.CREATED
source: insight
generated_at: '2026-09-28T09:36:16Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight.insight-created.data
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:25
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.insight-created.entity-type
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:24
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.insight-created.operation
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:20
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.insight-created.previous-data
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:26
  confidence: 0.9
  via: service-code
---
# INSIGHT.CREATED

## Links
- HAS_FIELD [[fld.insight.insight-created.data]], [[fld.insight.insight-created.entity-type]], [[fld.insight.insight-created.operation]], [[fld.insight.insight-created.previous-data]]
