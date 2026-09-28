---
id: evt.insight.canvas-deleted
type: event
name: CANVAS.DELETED
bus: default
detail_type: CANVAS.DELETED
source: insight
generated_at: '2026-09-28T09:36:16Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight.canvas-deleted.data
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:31
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.canvas-deleted.entity-type
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:30
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.canvas-deleted.operation
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:20
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight.canvas-deleted.previous-data
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:32
  confidence: 0.9
  via: service-code
---
# CANVAS.DELETED

## Links
- HAS_FIELD [[fld.insight.canvas-deleted.data]], [[fld.insight.canvas-deleted.entity-type]], [[fld.insight.canvas-deleted.operation]], [[fld.insight.canvas-deleted.previous-data]]
