---
id: evt.insight.insight-updated
type: event
name: INSIGHT.UPDATED
bus: default
detail_type: INSIGHT.UPDATED
source: insight
generated_at: '2026-09-28T09:36:16Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight.insight-updated.data
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:25
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.insight-updated.entity-type
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:24
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.insight-updated.operation
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:20
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.insight-updated.previous-data
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:26
  confidence: 0.9
  via: service-code
---
# INSIGHT.UPDATED

## Links
- HAS_FIELD [[fld.insight.insight-updated.data]], [[fld.insight.insight-updated.entity-type]], [[fld.insight.insight-updated.operation]], [[fld.insight.insight-updated.previous-data]]
