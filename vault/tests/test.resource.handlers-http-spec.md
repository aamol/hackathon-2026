---
id: test.resource.handlers-http-spec
type: test
name: http.spec.ts
file: Unite/services/resource/src/handlers/http.spec.ts
framework: jest
generated_at: '2026-09-28T09:35:50Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: TESTS
  to: api.resource.options-v1-resource-request-resource-group-id
  evidence: Unite/services/resource/src/handlers/http.spec.ts:6
  confidence: 0.9
  via: service-code
- type: TESTS
  to: api.resource.post-v1-okta-resource-request-resource-group-id
  evidence: Unite/services/resource/src/handlers/http.spec.ts:6
  confidence: 0.9
  via: service-code
- type: TESTS
  to: api.resource.post-v1-resource-request-resource-group-id
  evidence: Unite/services/resource/src/handlers/http.spec.ts:6
  confidence: 0.9
  via: service-code
---
# http.spec.ts

## Links
- TESTS [[api.resource.options-v1-resource-request-resource-group-id]], [[api.resource.post-v1-okta-resource-request-resource-group-id]], [[api.resource.post-v1-resource-request-resource-group-id]]
