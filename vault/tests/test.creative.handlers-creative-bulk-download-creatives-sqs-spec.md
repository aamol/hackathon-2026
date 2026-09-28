---
id: test.creative.handlers-creative-bulk-download-creatives-sqs-spec
type: test
name: bulk-download-creatives.sqs.spec.ts
file: Unite/services/creative/src/handlers/creative/bulk-download-creatives.sqs.spec.ts
framework: jest
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: TESTS
  to: fn.creative.bulk-download-creatives-worker
  evidence: Unite/services/creative/src/handlers/creative/bulk-download-creatives.sqs.spec.ts:52
  confidence: 0.9
  via: service-code
---
# bulk-download-creatives.sqs.spec.ts

## Links
- TESTS [[fn.creative.bulk-download-creatives-worker]]
