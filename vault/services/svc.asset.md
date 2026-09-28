---
id: svc.asset
type: service
name: asset
packages:
- access-layer-security
- agentexec
- agentexec-types
- api-response-builder
- asset
- asset-core
- asset-types
- audit-helper
- auth
- aws-singleton
- brand-check-policy
- brand-intelligence
- error-resolver
- eventbridge
- filesign
- lambda-handlers
- observability-node
- powertools-middy
- project-types
- rbac
- rbac-actions
- rbac-wss
- rel-asset-creative
- rel-user-project
- relation
- resource-manager
- resource-types
- storage
- storage-types
- user
- user-types
- validator
- wss
- wssbrandx-types
path: Unite/services/asset
generated_at: '2026-09-28T09:36:30Z'
contract_version: '0.2'
sources:
- asset
edges:
- type: CALLS
  to: api.creative.get-v1-creative-creative-id
  evidence: Unite/packages/asset/src/services/creative/get-creative.ts:37
  confidence: 0.8
  via: package:asset
- type: CALLS
  to: api.creative.get-v1-creative-version-version-id
  evidence: Unite/packages/asset/src/services/creative/get-creative-version.ts:38
  confidence: 0.8
  via: package:asset
- type: CALLS
  to: ext.pmh-api
  evidence: Unite/packages/asset/src/services/pmh/create-upload-url.ts:19
  confidence: 0.8
  via: package:asset
- type: CALLS
  to: ext.pmh-api
  evidence: Unite/packages/asset/src/services/pmh/get-pmh-submissions.ts:44
  confidence: 0.8
  via: package:asset
- type: CALLS
  to: ext.pmh-api
  evidence: Unite/packages/asset/src/services/pmh/pmh-auth.ts:25
  confidence: 0.8
  via: package:asset
- type: CALLS
  to: fn.thumbnailgen.thumbnail-generator
  evidence: Unite/packages/asset/src/previews/create-thumbnail-for-image.ts:21
  confidence: 0.8
  via: package:asset
- type: CONSUMES
  to: evt.resource.resource-available
  evidence: Unite/packages/resource-types/src/types.ts:414
  confidence: 0.6
  via: package:resource-types
- type: CONSUMES
  to: evt.resource.resource-failed
  evidence: Unite/packages/resource-types/src/types.ts:415
  confidence: 0.6
  via: package:resource-types
- type: CONSUMES
  to: evt.wssbrandx.asset-brand-check-status-updated
  evidence: Unite/services/asset/serverless.yml:270
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.asset-enrich-asset-queue
  evidence: Unite/services/asset/serverless.yml:210
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.asset-pmh-sync-queue
  evidence: Unite/services/asset/serverless.yml:232
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.asset-rasterizer-events
  evidence: Unite/services/asset/serverless.yml:450
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.delete-v1-asset-asset-id
  evidence: Unite/services/asset/serverless.yml:154
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.delete-v1-asset-bulk-delete
  evidence: Unite/services/asset/serverless.yml:301
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.get-v1-asset
  evidence: Unite/services/asset/serverless.yml:169
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.get-v1-asset-asset-id
  evidence: Unite/services/asset/serverless.yml:80
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.get-v1-asset-asset-id-file
  evidence: Unite/services/asset/serverless.yml:94
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.get-v1-asset-asset-id-usage
  evidence: Unite/services/asset/serverless.yml:108
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.get-v1-asset-source
  evidence: Unite/services/asset/serverless.yml:122
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.get-v1-assets-proxy
  evidence: Unite/services/asset/serverless.yml:402
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.get-v1-tag
  evidence: Unite/services/asset/serverless.yml:183
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.post-v1-asset
  evidence: Unite/services/asset/serverless.yml:51
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.post-v1-asset-bulk-download
  evidence: Unite/services/asset/serverless.yml:360
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.post-v1-assets-proxy
  evidence: Unite/services/asset/serverless.yml:382
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.put-v1-asset-asset-id
  evidence: Unite/services/asset/serverless.yml:139
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.asset.put-v1-asset-bulk-update
  evidence: Unite/services/asset/serverless.yml:284
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.asset-brand-check-status-updated-handler
  evidence: Unite/services/asset/serverless.yml:258
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.copy-asset-internal
  evidence: Unite/services/asset/serverless.yml:316
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.create-asset-from-resource-id
  evidence: Unite/services/asset/serverless.yml:55
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.create-asset-internal
  evidence: Unite/services/asset/serverless.yml:333
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.dynamo-router-handler
  evidence: Unite/services/asset/serverless.yml:409
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.get-asset-location-by-id-internal
  evidence: Unite/services/asset/serverless.yml:324
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.get-creative-export-assets-internal
  evidence: Unite/services/asset/serverless.yml:307
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.process-enrich-asset-queue
  evidence: Unite/services/asset/serverless.yml:188
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.process-pmh-sync-queue
  evidence: Unite/services/asset/serverless.yml:215
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.process-rasterizer-events
  evidence: Unite/services/asset/serverless.yml:439
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.resource-finished-handler
  evidence: Unite/services/asset/serverless.yml:238
  confidence: 1.0
  via: serverless.yml
- type: PUBLISHES
  to: evt.asset.asset-created
  evidence: Unite/services/asset/src/handlers/dynamo-router.ts:88
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.asset.asset-deleted
  evidence: Unite/services/asset/src/handlers/dynamo-router.ts:87
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.asset.asset-hard-deleted
  evidence: Unite/services/asset/src/handlers/dynamo-router.ts:94
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.asset.asset-pmh-sync-completed
  evidence: Unite/services/asset/src/application/handlers/sqs/pmh-sync-worker.ts:59
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.asset.asset-pmh-sync-started
  evidence: Unite/packages/asset/src/services/pmh/sync-assets-to-pmh.ts:816
  confidence: 0.8
  via: package:asset
- type: PUBLISHES
  to: evt.asset.asset-updated
  evidence: Unite/services/asset/src/handlers/dynamo-router.ts:92
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.asset.creative-version-pmh-sync-completed
  evidence: Unite/services/asset/src/application/handlers/sqs/pmh-sync-worker.ts:60
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.asset.creative-version-pmh-sync-started
  evidence: Unite/packages/asset/src/services/pmh/sync-assets-to-pmh.ts:640
  confidence: 0.8
  via: package:asset
- type: PUBLISHES
  to: q.asset-enrich-asset-queue
  evidence: Unite/packages/asset/src/utils/queue.ts:32
  confidence: 0.8
  via: package:asset
- type: PUBLISHES
  to: q.asset-pmh-sync-queue
  evidence: Unite/packages/asset/src/utils/queue.ts:44
  confidence: 0.8
  via: package:asset
- type: READS
  to: tbl.dynamodb.asset-assets
  evidence: Unite/packages/asset/src/db/get-asset-by-id.ts:12
  confidence: 0.8
  via: package:asset
- type: READS
  to: tbl.dynamodb.relation-relation-generic
  evidence: Unite/packages/relation/src/get-relations-by-subject-id.ts:71
  confidence: 0.8
  via: package:relation
- type: READS
  to: tbl.dynamodb.resource-resources
  evidence: Unite/packages/resource-manager/src/resource/index.ts:33
  confidence: 0.8
  via: package:resource-manager
- type: READS
  to: tbl.dynamodb.user-user-table
  evidence: Unite/packages/user/src/db/user-entity/repository.ts:152
  confidence: 0.8
  via: package:user
- type: WRITES
  to: tbl.dynamodb.asset-assets
  evidence: Unite/packages/asset/src/db/create-asset.ts:301
  confidence: 0.8
  via: package:asset
- type: WRITES
  to: tbl.dynamodb.resource-resources
  evidence: Unite/packages/resource-manager/src/resource/update-resource.ts:266
  confidence: 0.8
  via: package:resource-manager
---
# asset

## Summary
Digital asset management service: CRUD/listing/tagging/bulk APIs for assets, ingests resource-manager and rasterizer outputs into persistent asset records via EventBridge/SQS, and syncs assets and creative versions to the WSS-only PMH integration.

## Links
- CALLS [[api.creative.get-v1-creative-creative-id]], [[api.creative.get-v1-creative-version-version-id]], [[ext.pmh-api]], [[fn.thumbnailgen.thumbnail-generator]]
- CONSUMES [[evt.resource.resource-available]], [[evt.resource.resource-failed]], [[evt.wssbrandx.asset-brand-check-status-updated]], [[q.asset-enrich-asset-queue]], [[q.asset-pmh-sync-queue]], [[q.asset-rasterizer-events]]
- EXPOSES [[api.asset.delete-v1-asset-asset-id]], [[api.asset.delete-v1-asset-bulk-delete]], [[api.asset.get-v1-asset]], [[api.asset.get-v1-asset-asset-id]], [[api.asset.get-v1-asset-asset-id-file]], [[api.asset.get-v1-asset-asset-id-usage]], [[api.asset.get-v1-asset-source]], [[api.asset.get-v1-assets-proxy]], [[api.asset.get-v1-tag]], [[api.asset.post-v1-asset]], [[api.asset.post-v1-asset-bulk-download]], [[api.asset.post-v1-assets-proxy]], [[api.asset.put-v1-asset-asset-id]], [[api.asset.put-v1-asset-bulk-update]], [[fn.asset.asset-brand-check-status-updated-handler]], [[fn.asset.copy-asset-internal]], [[fn.asset.create-asset-from-resource-id]], [[fn.asset.create-asset-internal]], [[fn.asset.dynamo-router-handler]], [[fn.asset.get-asset-location-by-id-internal]], [[fn.asset.get-creative-export-assets-internal]], [[fn.asset.process-enrich-asset-queue]], [[fn.asset.process-pmh-sync-queue]], [[fn.asset.process-rasterizer-events]], [[fn.asset.resource-finished-handler]]
- PUBLISHES [[evt.asset.asset-created]], [[evt.asset.asset-deleted]], [[evt.asset.asset-hard-deleted]], [[evt.asset.asset-pmh-sync-completed]], [[evt.asset.asset-pmh-sync-started]], [[evt.asset.asset-updated]], [[evt.asset.creative-version-pmh-sync-completed]], [[evt.asset.creative-version-pmh-sync-started]], [[q.asset-enrich-asset-queue]], [[q.asset-pmh-sync-queue]]
- READS [[tbl.dynamodb.asset-assets]], [[tbl.dynamodb.relation-relation-generic]], [[tbl.dynamodb.resource-resources]], [[tbl.dynamodb.user-user-table]]
- WRITES [[tbl.dynamodb.asset-assets]], [[tbl.dynamodb.resource-resources]]
