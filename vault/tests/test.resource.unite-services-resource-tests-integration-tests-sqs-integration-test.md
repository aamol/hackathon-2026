---
id: test.resource.unite-services-resource-tests-integration-tests-sqs-integration-test
type: test
name: sqs.integration.test.ts
file: Unite/services/resource/tests/integration/tests/sqs.integration.test.ts
framework: jest
generated_at: '2026-09-28T09:35:50Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: TESTS
  to: fn.resource.handle-resource-queue
  evidence: Unite/services/resource/tests/integration/tests/sqs.integration.test.ts:10
  confidence: 0.9
  via: service-code
---
# sqs.integration.test.ts

## Links
- TESTS [[fn.resource.handle-resource-queue]]
