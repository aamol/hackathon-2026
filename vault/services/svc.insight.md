---
id: svc.insight
type: service
name: insight
packages:
- agentexec
- agentexec-types
- ai-chat-types
- ai-hub
- api-response-builder
- asset
- asset-types
- auth
- aws-singleton
- error-resolver
- global-usage-types
- insight-core
- insight-types
- lambda-handlers
- mediagen
- observability-node
- powertools-middy
- project-types
- rel-user-project
- relation
- resource-types
- user
- user-types
- vertexai-img
- wss
path: Unite/services/insight
generated_at: '2026-09-28T09:36:16Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: CALLS
  to: ext.wss-agents-api
  evidence: Unite/packages/insight-core/src/insights/wss-agents-resolver.ts:3
  confidence: 0.8
  via: package:insight-core
- type: CONSUMES
  to: evt.asset.asset-created
  evidence: Unite/services/insight/serverless.yml:215
  confidence: 1.0
  via: serverless.yml
  filter:
    record.sourceType:
    - RESOURCE_MANAGER
- type: CONSUMES
  to: evt.insight.canvas-created
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:14
  confidence: 0.9
  via: service-code
- type: CONSUMES
  to: evt.insight.canvas-deleted
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:16
  confidence: 0.9
  via: service-code
- type: CONSUMES
  to: evt.insight.canvas-updated
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:15
  confidence: 0.9
  via: service-code
- type: CONSUMES
  to: evt.insight.insight-created
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:11
  confidence: 0.9
  via: service-code
- type: CONSUMES
  to: evt.insight.insight-deleted
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:13
  confidence: 0.9
  via: service-code
- type: CONSUMES
  to: evt.insight.insight-updated
  evidence: Unite/services/insight/src/application/handlers/events/eb/eventbridge.ts:12
  confidence: 0.9
  via: service-code
- type: CONSUMES
  to: evt.resource.resource-failed
  evidence: Unite/services/insight/serverless.yml:231
  confidence: 1.0
  via: serverless.yml
  filter:
    resourceCallbackSource:
    - update_resource
- type: CONSUMES
  to: q.canvas-suggestions-queue
  evidence: Unite/services/insight/serverless.yml:307
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.insight-brand-colours-extract-queue
  evidence: Unite/services/insight/serverless.yml:333
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.insight-bulk-operation-queue
  evidence: Unite/services/insight/serverless.yml:324
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.insight-conversation-queue
  evidence: Unite/services/insight/serverless.yml:315
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.insight-editing-dlq
  evidence: Unite/services/insight/serverless.yml:447
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.insight-editing-queue
  evidence: Unite/services/insight/serverless.yml:251
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.insight-generation-dlq
  evidence: Unite/services/insight/serverless.yml:444
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.insight-generation-queue
  evidence: Unite/services/insight/serverless.yml:241
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.insight-image-prompt-build
  evidence: Unite/services/insight/serverless.yml:271
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.insight-image-prompt-generation-queue
  evidence: Unite/services/insight/serverless.yml:262
  confidence: 1.0
  via: serverless.yml
- type: DEPENDS_ON
  to: ext.anthropic-ai-sdk
  evidence: Unite/packages/agentexec/src/claude/claude-options.ts:1
  confidence: 0.8
  via: package:agentexec
- type: DEPENDS_ON
  to: ext.google-genai
  evidence: Unite/packages/agentexec/src/gemini/client.ts:1
  confidence: 0.8
  via: package:agentexec
- type: EXPOSES
  to: api.insight.delete-v1-insight-proxy
  evidence: Unite/services/insight/serverless.yml:101
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.insight.get-v1-insight-proxy
  evidence: Unite/services/insight/serverless.yml:112
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.insight.post-v1-insight-proxy
  evidence: Unite/services/insight/serverless.yml:128
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.insight.put-v1-insight-proxy
  evidence: Unite/services/insight/serverless.yml:90
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.asset-created-listener-handler
  evidence: Unite/services/insight/serverless.yml:200
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.brand-colours-extraction-queue-handler
  evidence: Unite/services/insight/serverless.yml:329
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.canvas-deleted-dynamo-listener
  evidence: Unite/services/insight/serverless.yml:277
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.canvas-suggestions-worker-handler
  evidence: Unite/services/insight/serverless.yml:303
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.ddb-event-notification-processor
  evidence: Unite/services/insight/serverless.yml:138
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.eventbridge-insight-listener-handler
  evidence: Unite/services/insight/serverless.yml:159
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.group-generation-publisher-handler
  evidence: Unite/services/insight/serverless.yml:175
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.group-membership-changed-mark-stale-listener
  evidence: Unite/services/insight/serverless.yml:403
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.image-generation-reaper-handler
  evidence: Unite/services/insight/serverless.yml:431
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.image-prompt-build-worker-handler
  evidence: Unite/services/insight/serverless.yml:267
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.image-prompt-generation-worker-handler
  evidence: Unite/services/insight/serverless.yml:258
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.insight-bulk-operation-worker-handler
  evidence: Unite/services/insight/serverless.yml:320
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.insight-changed-mark-stale-listener
  evidence: Unite/services/insight/serverless.yml:379
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.insight-conversation-worker-handler
  evidence: Unite/services/insight/serverless.yml:311
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.insight-dlq-consumer-handler
  evidence: Unite/services/insight/serverless.yml:440
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.insight-editing-worker-handler
  evidence: Unite/services/insight/serverless.yml:247
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.insight-generation-worker-handler
  evidence: Unite/services/insight/serverless.yml:237
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.resource-failed-listener-handler
  evidence: Unite/services/insight/serverless.yml:222
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.insight.search-index-listener
  evidence: Unite/services/insight/serverless.yml:338
  confidence: 1.0
  via: serverless.yml
- type: PUBLISHES
  to: evt.insight.canvas-created
  evidence: Unite/services/insight/src/infra/adapters/events/ddb.stream.adapter.ts:173
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.insight.canvas-deleted
  evidence: Unite/services/insight/src/infra/adapters/events/ddb.stream.adapter.ts:173
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.insight.canvas-updated
  evidence: Unite/services/insight/src/infra/adapters/events/ddb.stream.adapter.ts:173
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.insight.insight-created
  evidence: Unite/services/insight/src/infra/adapters/events/ddb.stream.adapter.ts:173
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.insight.insight-deleted
  evidence: Unite/services/insight/src/infra/adapters/events/ddb.stream.adapter.ts:173
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.insight.insight-updated
  evidence: Unite/services/insight/src/infra/adapters/events/ddb.stream.adapter.ts:173
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.canvas-suggestions-queue
  evidence: Unite/services/insight/src/application/handlers/http/v1/suggestions/canvas-form-suggest.ts:114
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.insight-brand-colours-extract-queue
  evidence: Unite/services/insight/src/application/handlers/events/eb/canvas.ts:24
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.insight-bulk-operation-queue
  evidence: Unite/services/insight/src/infra/adapters/queue/enqueue-insight-for-bulk-operations.ts:69
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.insight-conversation-queue
  evidence: Unite/packages/insight-core/src/queue/enqueue-insight-for-conversation.ts:28
  confidence: 0.8
  via: package:insight-core
- type: PUBLISHES
  to: q.insight-editing-queue
  evidence: Unite/services/insight/src/subscribers/insight-generation-worker.ts:292
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.insight-image-prompt-build
  evidence: Unite/services/insight/src/application/handlers/http/v1/image-prompts/build-image-prompt.ts:43
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.insight-image-prompt-generation-queue
  evidence: Unite/services/insight/src/application/handlers/events/eb/image-generation.ts:89
  confidence: 0.9
  via: service-code
- type: READS
  to: tbl.dynamodb.asset-assets
  evidence: Unite/packages/asset/src/db/get-assets-by-id.ts:38
  confidence: 0.8
  via: package:asset
- type: READS
  to: tbl.dynamodb.insight-entities
  evidence: Unite/packages/insight-core/src/db/insight.ts:387
  confidence: 0.8
  via: package:insight-core
- type: READS
  to: tbl.dynamodb.relation-relation-generic
  evidence: Unite/packages/relation/src/get-relation.ts:33
  confidence: 0.8
  via: package:relation
- type: READS
  to: tbl.dynamodb.user-user-table
  evidence: Unite/packages/user/src/db/user-entity/repository.ts:152
  confidence: 0.8
  via: package:user
- type: WRITES
  to: tbl.dynamodb.insight-entities
  evidence: Unite/packages/insight-core/src/db/insight.ts:399
  confidence: 0.8
  via: package:insight-core
---
# insight

## Summary
Manages canvases, insights, groups and AI-generated summaries/images for the Insight product surface.

## Links
- CALLS [[ext.wss-agents-api]]
- CONSUMES [[evt.asset.asset-created]], [[evt.insight.canvas-created]], [[evt.insight.canvas-deleted]], [[evt.insight.canvas-updated]], [[evt.insight.insight-created]], [[evt.insight.insight-deleted]], [[evt.insight.insight-updated]], [[evt.resource.resource-failed]], [[q.canvas-suggestions-queue]], [[q.insight-brand-colours-extract-queue]], [[q.insight-bulk-operation-queue]], [[q.insight-conversation-queue]], [[q.insight-editing-dlq]], [[q.insight-editing-queue]], [[q.insight-generation-dlq]], [[q.insight-generation-queue]], [[q.insight-image-prompt-build]], [[q.insight-image-prompt-generation-queue]]
- DEPENDS_ON [[ext.anthropic-ai-sdk]], [[ext.google-genai]]
- EXPOSES [[api.insight.delete-v1-insight-proxy]], [[api.insight.get-v1-insight-proxy]], [[api.insight.post-v1-insight-proxy]], [[api.insight.put-v1-insight-proxy]], [[fn.insight.asset-created-listener-handler]], [[fn.insight.brand-colours-extraction-queue-handler]], [[fn.insight.canvas-deleted-dynamo-listener]], [[fn.insight.canvas-suggestions-worker-handler]], [[fn.insight.ddb-event-notification-processor]], [[fn.insight.eventbridge-insight-listener-handler]], [[fn.insight.group-generation-publisher-handler]], [[fn.insight.group-membership-changed-mark-stale-listener]], [[fn.insight.image-generation-reaper-handler]], [[fn.insight.image-prompt-build-worker-handler]], [[fn.insight.image-prompt-generation-worker-handler]], [[fn.insight.insight-bulk-operation-worker-handler]], [[fn.insight.insight-changed-mark-stale-listener]], [[fn.insight.insight-conversation-worker-handler]], [[fn.insight.insight-dlq-consumer-handler]], [[fn.insight.insight-editing-worker-handler]], [[fn.insight.insight-generation-worker-handler]], [[fn.insight.resource-failed-listener-handler]], [[fn.insight.search-index-listener]]
- PUBLISHES [[evt.insight.canvas-created]], [[evt.insight.canvas-deleted]], [[evt.insight.canvas-updated]], [[evt.insight.insight-created]], [[evt.insight.insight-deleted]], [[evt.insight.insight-updated]], [[q.canvas-suggestions-queue]], [[q.insight-brand-colours-extract-queue]], [[q.insight-bulk-operation-queue]], [[q.insight-conversation-queue]], [[q.insight-editing-queue]], [[q.insight-image-prompt-build]], [[q.insight-image-prompt-generation-queue]]
- READS [[tbl.dynamodb.asset-assets]], [[tbl.dynamodb.insight-entities]], [[tbl.dynamodb.relation-relation-generic]], [[tbl.dynamodb.user-user-table]]
- WRITES [[tbl.dynamodb.insight-entities]]
