---
id: evt.insight.canvas-created
type: event
name: CANVAS.CREATED
bus: default
detail_type: CANVAS.CREATED
source: insight
generated_at: '2026-09-28T09:36:16Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight.canvas-created.data
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:31
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.canvas-created.entity-type
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:30
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.canvas-created.operation
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:20
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.canvas-created.previous-data
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:32
  confidence: 0.9
  via: service-code
---
# CANVAS.CREATED

## Links
- HAS_FIELD [[fld.insight.canvas-created.data]], [[fld.insight.canvas-created.entity-type]], [[fld.insight.canvas-created.operation]], [[fld.insight.canvas-created.previous-data]]
