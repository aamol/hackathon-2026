---
id: svc.resource
type: service
name: resource
packages:
- ai-hub-constants
- api-response-builder
- auth
- aws-singleton
- base-utils
- brand-intelligence
- error-resolver
- filesign
- global-pass
- global-pass-types
- global-usage
- global-usage-types
- observability-node
- open-api-client
- resource-manager
- resource-types
- validator
path: Unite/services/resource
generated_at: '2026-09-28T09:35:50Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: CALLS
  to: ext.wpp-open
  evidence: Unite/services/resource/src/handlers/http.ts:131
  confidence: 0.9
  via: service-code
- type: CONSUMES
  to: q.resource-queue
  evidence: Unite/services/resource/serverless.yml:94
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.resource.delete-v1-okta-resource-request-resource-group-id-resource-id
  evidence: Unite/services/resource/serverless.yml:140
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.resource.get-v1-resource-id-resource-id
  evidence: Unite/services/resource/serverless.yml:156
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.resource.get-v1-resource-resource-group-id-list
  evidence: Unite/services/resource/serverless.yml:176
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.resource.options-v1-resource-id-resource-id
  evidence: Unite/services/resource/serverless.yml:163
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.resource.options-v1-resource-request-resource-group-id
  evidence: Unite/services/resource/serverless.yml:119
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.resource.options-v1-resource-resource-group-id-list
  evidence: Unite/services/resource/serverless.yml:187
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.resource.post-v1-okta-resource-request-resource-group-id
  evidence: Unite/services/resource/serverless.yml:123
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.resource.post-v1-resource-request-resource-group-id
  evidence: Unite/services/resource/serverless.yml:112
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.resource.external-update-resource
  evidence: Unite/services/resource/serverless.yml:197
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.resource.handle-resource-queue
  evidence: Unite/services/resource/serverless.yml:64
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.resource.handle-resource-stream
  evidence: Unite/services/resource/serverless.yml:46
  confidence: 1.0
  via: serverless.yml
- type: PUBLISHES
  to: evt.resource.resource-available
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:8
  confidence: 0.8
  via: package:resource-manager
- type: PUBLISHES
  to: evt.resource.resource-failed
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:9
  confidence: 0.8
  via: package:resource-manager
- type: PUBLISHES
  to: q.agentexec-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.audioopt-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.azureimg-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.azurevid-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.bedrockimg-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.bedrockvect-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.bedrockvid-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.bria-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.bytedanceimg-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.bytedancetts-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.bytedancevid-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.convsummary-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.echo-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.elevenlabs-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.ffmpeg-concat-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.ffmpeg-edit-audio-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.ffmpeg-extract-audio-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.ffmpeg-split-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.fileopt-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.fileparse-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.firefly-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.huaweiimg-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.huaweivid-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.imageopt-crop-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.imageopt-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.minimaxvid-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.podcast-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.python-markitdown-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.renderer-task-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.renderer-worker-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.resource-queue
  evidence: Unite/packages/resource-manager/src/resource/create-resource.ts:106
  confidence: 0.8
  via: package:resource-manager
- type: PUBLISHES
  to: q.resource-queue
  evidence: Unite/services/resource/src/utils/sqs-utils.ts:69
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.resourcename-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.vertexaiimg-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.vertexaimus-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.vertexaivid-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.vertexaivoic-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.videoextf-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.videoopt-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.zhipuimg-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.zhipuvid-queue
  evidence: Unite/services/resource/src/handlers/sqs.ts:357
  confidence: 0.9
  via: service-code
- type: READS
  to: tbl.dynamodb.relation-relation-generic
  evidence: Unite/services/resource/src/handlers/stream.ts:92
  confidence: 0.6
  via: service-code
- type: READS
  to: tbl.dynamodb.resource-resources
  evidence: Unite/packages/resource-manager/src/resource/index.ts:144
  confidence: 0.8
  via: package:resource-manager
- type: READS
  to: tbl.dynamodb.resource-resources
  evidence: Unite/packages/resource-manager/src/resource/index.ts:184
  confidence: 0.8
  via: package:resource-manager
- type: READS
  to: tbl.dynamodb.resource-resources
  evidence: Unite/packages/resource-manager/src/resource/index.ts:33
  confidence: 0.8
  via: package:resource-manager
- type: READS
  to: tbl.dynamodb.resource-resources
  evidence: Unite/packages/resource-manager/src/resource/index.ts:75
  confidence: 0.8
  via: package:resource-manager
- type: READS
  to: tbl.dynamodb.resource-resources
  evidence: Unite/packages/resource-manager/src/resource/pull-prioritized-resource.ts:45
  confidence: 0.8
  via: package:resource-manager
- type: WRITES
  to: tbl.dynamodb.relation-relation-generic
  evidence: Unite/services/resource/src/handlers/stream.ts:92
  confidence: 0.6
  via: service-code
- type: WRITES
  to: tbl.dynamodb.resource-resources
  evidence: Unite/packages/resource-manager/src/resource/create-resource.ts:49
  confidence: 0.8
  via: package:resource-manager
- type: WRITES
  to: tbl.dynamodb.resource-resources
  evidence: Unite/packages/resource-manager/src/resource/delete-resource.ts:20
  confidence: 0.8
  via: package:resource-manager
- type: WRITES
  to: tbl.dynamodb.resource-resources
  evidence: Unite/packages/resource-manager/src/resource/index.ts:195
  confidence: 0.8
  via: package:resource-manager
- type: WRITES
  to: tbl.dynamodb.resource-resources
  evidence: Unite/packages/resource-manager/src/resource/pull-prioritized-resource.ts:186
  confidence: 0.8
  via: package:resource-manager
- type: WRITES
  to: tbl.dynamodb.resource-resources
  evidence: Unite/packages/resource-manager/src/resource/update-resource.ts:266
  confidence: 0.8
  via: package:resource-manager
---
# resource

## Summary
Generic async resource request/queue/priority orchestration hub: exposes request/list/lookup APIs, fans SQS work out to ~40 downstream microservice queues by resource type, and emits EventBridge callbacks on completion.

## Links
- CALLS [[ext.wpp-open]]
- CONSUMES [[q.resource-queue]]
- EXPOSES [[api.resource.delete-v1-okta-resource-request-resource-group-id-resource-id]], [[api.resource.get-v1-resource-id-resource-id]], [[api.resource.get-v1-resource-resource-group-id-list]], [[api.resource.options-v1-resource-id-resource-id]], [[api.resource.options-v1-resource-request-resource-group-id]], [[api.resource.options-v1-resource-resource-group-id-list]], [[api.resource.post-v1-okta-resource-request-resource-group-id]], [[api.resource.post-v1-resource-request-resource-group-id]], [[fn.resource.external-update-resource]], [[fn.resource.handle-resource-queue]], [[fn.resource.handle-resource-stream]]
- PUBLISHES [[evt.resource.resource-available]], [[evt.resource.resource-failed]], [[q.agentexec-queue]], [[q.audioopt-queue]], [[q.azureimg-queue]], [[q.azurevid-queue]], [[q.bedrockimg-queue]], [[q.bedrockvect-queue]], [[q.bedrockvid-queue]], [[q.bria-queue]], [[q.bytedanceimg-queue]], [[q.bytedancetts-queue]], [[q.bytedancevid-queue]], [[q.convsummary-queue]], [[q.echo-queue]], [[q.elevenlabs-queue]], [[q.ffmpeg-concat-queue]], [[q.ffmpeg-edit-audio-queue]], [[q.ffmpeg-extract-audio-queue]], [[q.ffmpeg-split-queue]], [[q.fileopt-queue]], [[q.fileparse-queue]], [[q.firefly-queue]], [[q.huaweiimg-queue]], [[q.huaweivid-queue]], [[q.imageopt-crop-queue]], [[q.imageopt-queue]], [[q.minimaxvid-queue]], [[q.podcast-queue]], [[q.python-markitdown-queue]], [[q.renderer-task-queue]], [[q.renderer-worker-queue]], [[q.resource-queue]], [[q.resourcename-queue]], [[q.vertexaiimg-queue]], [[q.vertexaimus-queue]], [[q.vertexaivid-queue]], [[q.vertexaivoic-queue]], [[q.videoextf-queue]], [[q.videoopt-queue]], [[q.zhipuimg-queue]], [[q.zhipuvid-queue]]
- READS [[tbl.dynamodb.relation-relation-generic]], [[tbl.dynamodb.resource-resources]]
- WRITES [[tbl.dynamodb.relation-relation-generic]], [[tbl.dynamodb.resource-resources]]
