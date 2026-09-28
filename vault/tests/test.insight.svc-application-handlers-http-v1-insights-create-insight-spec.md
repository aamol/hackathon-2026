---
id: test.insight.svc-application-handlers-http-v1-insights-create-insight-spec
type: test
name: create-insight.spec.ts
file: Unite/services/insight/src/application/handlers/http/v1/insights/create-insight.spec.ts
framework: jest
generated_at: '2026-09-28T09:36:16Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: TESTS
  to: api.insight.post-v1-insight-proxy
  evidence: Unite/services/insight/src/application/handlers/http/v1/insights/create-insight.spec.ts:47
  confidence: 0.9
  via: service-code
---
# create-insight.spec.ts

## Links
- TESTS [[api.insight.post-v1-insight-proxy]]
