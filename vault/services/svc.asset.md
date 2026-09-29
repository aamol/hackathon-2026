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
generated_at: '2026-09-28T10:17:00Z'
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
  evidence: Unite/packages/asset/src/services/pmh/pmh-auth.ts:25
  confidence: 0.8
  via: package:asset
- type: CALLS
  to: fn.asset.create-asset-from-resource-id
  evidence: Unite/packages/asset/src/utils/invoke-lambda.ts:8
  confidence: 0.8
  via: package:asset
- type: CALLS
  to: fn.thumbnailgen.thumbnail-generator
  evidence: Unite/packages/asset/src/utils/invoke-lambda.ts:8
  confidence: 0.6
  via: package:asset
- type: CONSUMES
  to: evt.rasterizer-service.motion-rasterized-success
  evidence: Unite/services/asset/serverless.yml:667
  confidence: 1.0
  via: serverless.yml
  filter:
    detail-type:
    - MotionRasterizedSuccess
    source:
    - rasterizer.service.${self:custom.T.STAGE}
- type: CONSUMES
  to: evt.resource.resource-available
  evidence: Unite/services/asset/serverless.yml:246
  confidence: 0.6
  via: serverless.yml
- type: CONSUMES
  to: evt.resource.resource-failed
  evidence: Unite/services/asset/serverless.yml:246
  confidence: 0.6
  via: serverless.yml
- type: CONSUMES
  to: evt.wssbrandx.asset-brand-check-status-updated
  evidence: Unite/services/asset/serverless.yml:270
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.asset-enrich-asset-queue
  evidence: Unite/services/asset/serverless.yml:208
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.asset-pmh-sync-queue
  evidence: Unite/services/asset/serverless.yml:230
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
  evidence: Unite/services/asset/serverless.yml:259
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.copy-asset-internal
  evidence: Unite/services/asset/serverless.yml:317
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.create-asset-from-resource-id
  evidence: Unite/services/asset/serverless.yml:56
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.create-asset-internal
  evidence: Unite/services/asset/serverless.yml:334
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.dynamo-router-handler
  evidence: Unite/services/asset/serverless.yml:410
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.get-asset-location-by-id-internal
  evidence: Unite/services/asset/serverless.yml:325
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.get-creative-export-assets-internal
  evidence: Unite/services/asset/serverless.yml:308
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.process-enrich-asset-queue
  evidence: Unite/services/asset/serverless.yml:189
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.process-pmh-sync-queue
  evidence: Unite/services/asset/serverless.yml:216
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.process-rasterizer-events
  evidence: Unite/services/asset/serverless.yml:440
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.asset.resource-finished-handler
  evidence: Unite/services/asset/serverless.yml:239
  confidence: 1.0
  via: serverless.yml
- type: PUBLISHES
  to: evt.asset.asset-created
  evidence: Unite/services/asset/src/handlers/dynamo-router.ts:53
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.asset.asset-deleted
  evidence: Unite/services/asset/src/handlers/dynamo-router.ts:53
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.asset.asset-hard-deleted
  evidence: Unite/services/asset/src/handlers/dynamo-router.ts:53
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.asset.asset-pmh-sync-completed
  evidence: Unite/services/asset/src/application/handlers/sqs/pmh-sync-worker.ts:74
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.asset.asset-pmh-sync-started
  evidence: Unite/packages/asset/src/services/pmh/sync-assets-to-pmh.ts:814
  confidence: 0.8
  via: package:asset
- type: PUBLISHES
  to: evt.asset.asset-updated
  evidence: Unite/services/asset/src/handlers/dynamo-router.ts:53
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.asset.creative-version-pmh-sync-completed
  evidence: Unite/services/asset/src/application/handlers/sqs/pmh-sync-worker.ts:74
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.asset.creative-version-pmh-sync-started
  evidence: Unite/packages/asset/src/services/pmh/sync-assets-to-pmh.ts:638
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
  evidence: Unite/packages/asset/src/db/get-asset-by-source-id.ts:77
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
Owns asset CRUD, tagging and usage lookups; syncs assets and creative versions to PMH and enriches assets via an agent worker.

## Links
- CALLS [[api.creative.get-v1-creative-creative-id]], [[api.creative.get-v1-creative-version-version-id]], [[ext.pmh-api]], [[fn.asset.create-asset-from-resource-id]], [[fn.thumbnailgen.thumbnail-generator]]
- CONSUMES [[evt.rasterizer-service.motion-rasterized-success]], [[evt.resource.resource-available]], [[evt.resource.resource-failed]], [[evt.wssbrandx.asset-brand-check-status-updated]], [[q.asset-enrich-asset-queue]], [[q.asset-pmh-sync-queue]], [[q.asset-rasterizer-events]]
- EXPOSES [[api.asset.delete-v1-asset-asset-id]], [[api.asset.delete-v1-asset-bulk-delete]], [[api.asset.get-v1-asset]], [[api.asset.get-v1-asset-asset-id]], [[api.asset.get-v1-asset-asset-id-file]], [[api.asset.get-v1-asset-asset-id-usage]], [[api.asset.get-v1-asset-source]], [[api.asset.get-v1-assets-proxy]], [[api.asset.get-v1-tag]], [[api.asset.post-v1-asset]], [[api.asset.post-v1-asset-bulk-download]], [[api.asset.post-v1-assets-proxy]], [[api.asset.put-v1-asset-asset-id]], [[api.asset.put-v1-asset-bulk-update]], [[fn.asset.asset-brand-check-status-updated-handler]], [[fn.asset.copy-asset-internal]], [[fn.asset.create-asset-from-resource-id]], [[fn.asset.create-asset-internal]], [[fn.asset.dynamo-router-handler]], [[fn.asset.get-asset-location-by-id-internal]], [[fn.asset.get-creative-export-assets-internal]], [[fn.asset.process-enrich-asset-queue]], [[fn.asset.process-pmh-sync-queue]], [[fn.asset.process-rasterizer-events]], [[fn.asset.resource-finished-handler]]
- PUBLISHES [[evt.asset.asset-created]], [[evt.asset.asset-deleted]], [[evt.asset.asset-hard-deleted]], [[evt.asset.asset-pmh-sync-completed]], [[evt.asset.asset-pmh-sync-started]], [[evt.asset.asset-updated]], [[evt.asset.creative-version-pmh-sync-completed]], [[evt.asset.creative-version-pmh-sync-started]], [[q.asset-enrich-asset-queue]], [[q.asset-pmh-sync-queue]]
- READS [[tbl.dynamodb.asset-assets]], [[tbl.dynamodb.relation-relation-generic]], [[tbl.dynamodb.resource-resources]]
- WRITES [[tbl.dynamodb.asset-assets]], [[tbl.dynamodb.resource-resources]]
