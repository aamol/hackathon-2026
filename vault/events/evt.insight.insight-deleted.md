---
id: evt.insight.insight-deleted
type: event
name: INSIGHT.DELETED
bus: default
detail_type: INSIGHT.DELETED
source: insight
generated_at: '2026-09-28T09:36:16Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight.insight-deleted.data
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:25
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.insight-deleted.entity-type
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:24
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.insight-deleted.operation
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:20
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.insight-deleted.previous-data
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:26
  confidence: 0.9
  via: service-code
---
# INSIGHT.DELETED

## Links
- HAS_FIELD [[fld.insight.insight-deleted.data]], [[fld.insight.insight-deleted.entity-type]], [[fld.insight.insight-deleted.operation]], [[fld.insight.insight-deleted.previous-data]]
