---
id: test.resource.http-spec
type: test
name: http.spec.ts
file: Unite/services/resource/src/handlers/http.spec.ts
framework: jest
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: TESTS
  to: fn.resource.request-post
  evidence: Unite/services/resource/src/handlers/http.spec.ts:6
  confidence: 0.9
  via: service-code
---
# http.spec.ts

## Links
- TESTS [[fn.resource.request-post]]
