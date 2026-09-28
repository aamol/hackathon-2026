---
id: test.insight.application-handlers-http-v1-insights-delete-insight-spec
type: test
name: delete-insight.spec.ts
file: Unite/services/insight/src/application/handlers/http/v1/insights/delete-insight.spec.ts
framework: jest
generated_at: '2026-09-28T09:36:16Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: TESTS
  to: api.insight.delete-v1-insight-proxy
  evidence: Unite/services/insight/src/application/handlers/http/v1/insights/delete-insight.spec.ts:78
  confidence: 0.85
  via: service-code
---
# delete-insight.spec.ts

## Links
- TESTS [[api.insight.delete-v1-insight-proxy]]
