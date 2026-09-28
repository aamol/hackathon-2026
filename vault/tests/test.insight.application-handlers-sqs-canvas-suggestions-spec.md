---
id: test.insight.application-handlers-sqs-canvas-suggestions-spec
type: test
name: canvas-suggestions.spec.ts
file: Unite/services/insight/src/application/handlers/sqs/canvas-suggestions.spec.ts
framework: jest
generated_at: '2026-09-28T09:36:16Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: TESTS
  to: fn.insight.canvas-suggestions-worker-handler
  evidence: Unite/services/insight/src/application/handlers/sqs/canvas-suggestions.spec.ts:154
  confidence: 0.9
  via: service-code
---
# canvas-suggestions.spec.ts

## Links
- TESTS [[fn.insight.canvas-suggestions-worker-handler]]
