---
id: test.asset.application-handlers-sqs-pmh-sync-worker-spec
type: test
name: pmh-sync-worker.spec.ts
file: Unite/services/asset/src/application/handlers/sqs/pmh-sync-worker.spec.ts
framework: jest
generated_at: '2026-09-28T09:36:30Z'
contract_version: '0.2'
sources:
- asset
edges:
- type: TESTS
  to: fn.asset.process-pmh-sync-queue
  evidence: Unite/services/asset/src/application/handlers/sqs/pmh-sync-worker.spec.ts:1
  confidence: 0.9
  via: service-code
---
# pmh-sync-worker.spec.ts

## Links
- TESTS [[fn.asset.process-pmh-sync-queue]]
