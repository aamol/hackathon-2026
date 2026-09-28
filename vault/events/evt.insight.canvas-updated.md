---
id: evt.insight.canvas-updated
type: event
name: CANVAS.UPDATED
bus: default
detail_type: CANVAS.UPDATED
source: insight
generated_at: '2026-09-28T09:36:16Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight.canvas-updated.data
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:31
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.canvas-updated.entity-type
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:30
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.canvas-updated.operation
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:20
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.canvas-updated.previous-data
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:32
  confidence: 0.9
  via: service-code
---
# CANVAS.UPDATED

## Links
- HAS_FIELD [[fld.insight.canvas-updated.data]], [[fld.insight.canvas-updated.entity-type]], [[fld.insight.canvas-updated.operation]], [[fld.insight.canvas-updated.previous-data]]
