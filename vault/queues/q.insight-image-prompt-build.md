---
id: q.insight-image-prompt-build
type: queue
name: insight-image-prompt-build
dlq: q.insight-image-prompt-build-dlq
owner_service: insight
physical_name: insight-image-prompt-build-${self:custom.T.STAGE}
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.insight-image-prompt-build.job-id
  evidence: Unite/services/insight/src/application/handlers/http/v1/image-prompts/build-image-prompt.ts:24
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight-image-prompt-build.project-id
  evidence: Unite/services/insight/src/application/handlers/http/v1/image-prompts/build-image-prompt.ts:25
  confidence: 0.9
  via: service-code
- type: HAS_FIELD
  to: fld.insight-image-prompt-build.request
  evidence: Unite/services/insight/src/application/handlers/http/v1/image-prompts/build-image-prompt.ts:26
  confidence: 0.9
  via: service-code
---
# insight-image-prompt-build

## Links
- HAS_FIELD [[fld.insight-image-prompt-build.job-id]], [[fld.insight-image-prompt-build.project-id]], [[fld.insight-image-prompt-build.request]]
