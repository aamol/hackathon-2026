---
id: test.insight.svc-application-handlers-http-v1-insights-list-insights-spec
type: test
name: list-insights.spec.ts
file: Unite/services/insight/src/application/handlers/http/v1/insights/list-insights.spec.ts
framework: jest
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: TESTS
  to: api.insight.get-v1-insight-proxy
  evidence: Unite/services/insight/src/application/handlers/http/v1/insights/list-insights.spec.ts:1
  confidence: 0.9
  via: service-code
---
# list-insights.spec.ts

## Links
- TESTS [[api.insight.get-v1-insight-proxy]]
