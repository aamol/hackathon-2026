---
id: test.asset.svc-application-handlers-sqs-enrich-asset-worker-spec
type: test
name: enrich-asset-worker.spec.ts
file: Unite/services/asset/src/application/handlers/sqs/enrich-asset-worker.spec.ts
framework: jest
generated_at: '2026-09-28T10:17:00Z'
contract_version: '0.2'
sources:
- asset
edges:
- type: TESTS
  to: fn.asset.process-enrich-asset-queue
  evidence: Unite/services/asset/src/application/handlers/sqs/enrich-asset-worker.spec.ts:104
  confidence: 0.9
  via: service-code
---
# enrich-asset-worker.spec.ts

## Links
- TESTS [[fn.asset.process-enrich-asset-queue]]
