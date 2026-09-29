---
id: test.insight.svc-eventbridge-asset-created-listener-spec
type: test
name: asset-created-listener.spec.ts
file: Unite/services/insight/src/eventbridge/asset-created-listener.spec.ts
framework: jest
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: TESTS
  to: fn.insight.asset-created-listener-handler
  evidence: Unite/services/insight/src/eventbridge/asset-created-listener.spec.ts:1
  confidence: 0.9
  via: service-code
---
# asset-created-listener.spec.ts

## Links
- TESTS [[fn.insight.asset-created-listener-handler]]
