---
id: svc.creative
type: service
name: creative
packages:
- access-layer
- access-layer-security
- ai-hub-constants
- api-response-builder
- app-events
- asset
- asset-types
- auth
- aws-singleton
- base-utils
- brand-check-policy
- brand-identity-copy
- brand-intelligence
- creative-core
- creative-types
- error-resolver
- eventbridge
- feature-preview
- global-usage
- google-auth
- lambda-eventbridge
- lambda-results
- mediagen
- observability-node
- oss-search
- powertools-middy
- project-types
- rasterizer-types
- rbac-actions
- rbac-wss
- rel-asset-creative
- rel-user-project
- relation
- resource-types
- user-types
- validator
- wss
- wss-app-events
- wssbrandx-types
path: Unite/services/creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: CALLS
  to: fn.wssbrandx.list-report-assets-for-creative-internal
  evidence: Unite/services/creative/src/utils/wssbrandx-report-client.ts:47
  confidence: 0.9
  via: service-code
- type: CONSUMES
  to: evt.asset.asset-created
  evidence: Unite/services/creative/serverless.yml:1798
  confidence: 1.0
  via: serverless.yml
  filter:
    assetPublic.sourceType:
    - CREATIVE_EXPORT
    - CREATIVE_PREVIEW
    assetPublic.assetType:
    - VIDEO
    - IMAGE
- type: CONSUMES
  to: evt.asset.asset-created
  evidence: Unite/services/creative/serverless.yml:1874
  confidence: 0.6
  via: serverless.yml
  filter:
    assetPublic.sourceType:
    - CREATIVE_EXPORT
    - exists: false
    record.assetType:
    - VIDEO
    - exists: false
- type: CONSUMES
  to: evt.asset.asset-deleted
  evidence: Unite/services/creative/serverless.yml:1828
  confidence: 1.0
  via: serverless.yml
  filter:
    assetPublic.sourceType:
    - anything-but:
      - CREATIVE_EXPORT
      - CREATIVE_PREVIEW
- type: CONSUMES
  to: evt.asset.asset-hard-deleted
  evidence: Unite/services/creative/serverless.yml:1828
  confidence: 1.0
  via: serverless.yml
  filter:
    assetPublic.sourceType:
    - anything-but:
      - CREATIVE_EXPORT
      - CREATIVE_PREVIEW
- type: CONSUMES
  to: evt.asset.asset-updated
  evidence: Unite/services/creative/serverless.yml:1828
  confidence: 1.0
  via: serverless.yml
  filter:
    assetPublic.sourceType:
    - anything-but:
      - CREATIVE_EXPORT
      - CREATIVE_PREVIEW
- type: CONSUMES
  to: evt.asset.creative-version-pmh-sync-completed
  evidence: Unite/services/creative/serverless.yml:262
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: evt.asset.creative-version-pmh-sync-started
  evidence: Unite/services/creative/serverless.yml:263
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: evt.creative-share.creative-version-share-expire
  evidence: Unite/services/creative/serverless.yml:236
  confidence: 0.6
  via: serverless.yml
- type: CONSUMES
  to: evt.creative-status.rasterization-status-update
  evidence: Unite/services/creative/serverless.yml:237
  confidence: 0.6
  via: serverless.yml
- type: CONSUMES
  to: evt.creative.app-event-format-event-created
  evidence: Unite/services/creative/serverless.yml:1906
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: evt.creative.creative-preview-asset-updated
  evidence: Unite/services/creative/serverless.yml:1950
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: evt.creative.html-export-requested
  evidence: Unite/services/creative/serverless.yml:1928
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: evt.rasterizer-service.motion-rasterized-failure
  evidence: Unite/services/creative/serverless.yml:1874
  confidence: 0.6
  via: serverless.yml
  filter:
    assetPublic.sourceType:
    - CREATIVE_EXPORT
    - exists: false
    record.assetType:
    - VIDEO
    - exists: false
- type: CONSUMES
  to: evt.rasterizer-service.preview-rasterization-status-update
  evidence: Unite/services/creative/serverless.yml:248
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: evt.wssbrandx.creative-brand-check-status-updated
  evidence: Unite/services/creative/serverless.yml:255
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.creative-asset-events-creative
  evidence: Unite/services/creative/serverless.yml:969
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.creative-asset-relation-events
  evidence: Unite/services/creative/serverless.yml:984
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.creative-bulk-download-creatives
  evidence: Unite/services/creative/serverless.yml:430
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.creative-copy-events-creatives
  evidence: Unite/services/creative/serverless.yml:1031
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.creative-copy-selection-events
  evidence: Unite/services/creative/serverless.yml:1047
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.creative-format-events
  evidence: Unite/services/creative/serverless.yml:1013
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.creative-html-export-events
  evidence: Unite/services/creative/serverless.yml:1071
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.creative-html-export-preview-asset
  evidence: Unite/services/creative/serverless.yml:1094
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.creative-html-export-zip
  evidence: Unite/services/creative/serverless.yml:1111
  confidence: 1.0
  via: serverless.yml
- type: CONSUMES
  to: q.creative-rasterizer-events
  evidence: Unite/services/creative/serverless.yml:999
  confidence: 1.0
  via: serverless.yml
- type: DEPENDS_ON
  to: ext.google-genai
  evidence: Unite/services/creative/src/utils/validate-image-prompt.ts:1
  confidence: 0.9
  via: service-code
- type: EXPOSES
  to: api.creative.delete-v1-brand-components-component-id
  evidence: Unite/services/creative/serverless.yml:826
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.delete-v1-creatives-proxy
  evidence: Unite/services/creative/serverless.yml:192
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-auth-creative-proxy
  evidence: Unite/services/creative/serverless.yml:89
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-brand-components
  evidence: Unite/services/creative/serverless.yml:796
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-brand-components-component-id
  evidence: Unite/services/creative/serverless.yml:811
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creative-creative-id
  evidence: Unite/services/creative/serverless.yml:329
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creative-creative-id-version-version-id-html-export
  evidence: Unite/services/creative/serverless.yml:140
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creative-creative-id-version-version-id-share
  evidence: Unite/services/creative/serverless.yml:116
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creative-creative-id-version-version-id-share-proxy
  evidence: Unite/services/creative/serverless.yml:122
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creative-creative-id-version-version-id-status
  evidence: Unite/services/creative/serverless.yml:110
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creative-formats
  evidence: Unite/services/creative/serverless.yml:104
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creative-share-audit-project-project-id
  evidence: Unite/services/creative/serverless.yml:134
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creative-share-audit-share-id
  evidence: Unite/services/creative/serverless.yml:128
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creative-tag
  evidence: Unite/services/creative/serverless.yml:311
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creative-version-version-id
  evidence: Unite/services/creative/serverless.yml:920
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creatives
  evidence: Unite/services/creative/serverless.yml:347
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creatives-bulk-copy-jobs-active
  evidence: Unite/services/creative/serverless.yml:544
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creatives-bulk-copy-jobs-source-source-project-id
  evidence: Unite/services/creative/serverless.yml:530
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creatives-bulk-copy-jobs-source-source-project-id-target-target-project-id
  evidence: Unite/services/creative/serverless.yml:571
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-creatives-bulk-copy-jobs-target-target-project-id
  evidence: Unite/services/creative/serverless.yml:743
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v1-latest-creative-version-creative-id
  evidence: Unite/services/creative/serverless.yml:867
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.get-v2-creatives-versions-shares-proxy
  evidence: Unite/services/creative/serverless.yml:210
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.patch-v1-creative-creative-id
  evidence: Unite/services/creative/serverless.yml:365
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.patch-v1-creatives-bulk-delete
  evidence: Unite/services/creative/serverless.yml:445
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.patch-v1-creatives-bulk-update
  evidence: Unite/services/creative/serverless.yml:462
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-auth-creative-proxy
  evidence: Unite/services/creative/serverless.yml:86
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-brand-components
  evidence: Unite/services/creative/serverless.yml:781
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative
  evidence: Unite/services/creative/serverless.yml:279
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-asset-replicate-check
  evidence: Unite/services/creative/serverless.yml:693
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-asset-replicate-create
  evidence: Unite/services/creative/serverless.yml:711
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-asset-replicate-override
  evidence: Unite/services/creative/serverless.yml:729
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-bulk-download
  evidence: Unite/services/creative/serverless.yml:405
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-copy
  evidence: Unite/services/creative/serverless.yml:296
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-creative-id-version-version-id-share
  evidence: Unite/services/creative/serverless.yml:171
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-creative-id-version-version-id-share-proxy
  evidence: Unite/services/creative/serverless.yml:177
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-download-creative-id
  evidence: Unite/services/creative/serverless.yml:387
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-generate-image
  evidence: Unite/services/creative/serverless.yml:763
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-replicate-check
  evidence: Unite/services/creative/serverless.yml:589
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-replicate-create
  evidence: Unite/services/creative/serverless.yml:607
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-replicate-override
  evidence: Unite/services/creative/serverless.yml:625
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creative-version
  evidence: Unite/services/creative/serverless.yml:851
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creatives-bulk-copy
  evidence: Unite/services/creative/serverless.yml:482
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creatives-bulk-copy-jobs-active
  evidence: Unite/services/creative/serverless.yml:558
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creatives-bulk-copy-precheck
  evidence: Unite/services/creative/serverless.yml:517
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creatives-bulk-copy-selection
  evidence: Unite/services/creative/serverless.yml:500
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-creatives-proxy
  evidence: Unite/services/creative/serverless.yml:165
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-template-replicate-check
  evidence: Unite/services/creative/serverless.yml:642
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-template-replicate-create
  evidence: Unite/services/creative/serverless.yml:659
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: api.creative.post-v1-template-replicate-override
  evidence: Unite/services/creative/serverless.yml:676
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.activate-share-handler
  evidence: Unite/services/creative/serverless.yml:927
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.asset-events-creative-handler
  evidence: Unite/services/creative/serverless.yml:961
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.asset-relation-events-handler
  evidence: Unite/services/creative/serverless.yml:976
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.async-event-handler
  evidence: Unite/services/creative/serverless.yml:218
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.backfill-asset-creative-relations
  evidence: Unite/services/creative/serverless.yml:1125
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.backfill-asset-format-id
  evidence: Unite/services/creative/serverless.yml:1135
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.backfill-latest-version-formats
  evidence: Unite/services/creative/serverless.yml:1117
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.bulk-download-creatives-worker
  evidence: Unite/services/creative/serverless.yml:413
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.copy-events-creative-handler
  evidence: Unite/services/creative/serverless.yml:1020
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.copy-selection-events-handler
  evidence: Unite/services/creative/serverless.yml:1037
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.create-html-export-zip
  evidence: Unite/services/creative/serverless.yml:1100
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.creative-custom-auth
  evidence: Unite/services/creative/serverless.yml:63
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.get-creative-formats-internal
  evidence: Unite/services/creative/serverless.yml:888
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.get-creative-internal
  evidence: Unite/services/creative/serverless.yml:874
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.get-creative-rasterization-status-internal
  evidence: Unite/services/creative/serverless.yml:895
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.get-latest-creative-version-internal
  evidence: Unite/services/creative/serverless.yml:881
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.process-format-events
  evidence: Unite/services/creative/serverless.yml:1006
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.process-html-export
  evidence: Unite/services/creative/serverless.yml:1052
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.process-html-export-preview-asset
  evidence: Unite/services/creative/serverless.yml:1077
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.process-rasterizer-events
  evidence: Unite/services/creative/serverless.yml:991
  confidence: 1.0
  via: serverless.yml
- type: EXPOSES
  to: fn.creative.trigger-creative-rasterization-internal
  evidence: Unite/services/creative/serverless.yml:902
  confidence: 1.0
  via: serverless.yml
- type: PUBLISHES
  to: evt.creative.app-event-commercial-open-action-performed
  evidence: Unite/services/creative/src/handlers/event-bridge/process-creative-version-pmh-sync.ts:228
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.creative.app-event-creative-bulk-download-failed
  evidence: Unite/services/creative/src/handlers/creative/bulk-download-creatives.sqs.ts:56
  confidence: 0.6
  via: service-code
- type: PUBLISHES
  to: evt.creative.app-event-creative-bulk-download-prepared
  evidence: Unite/services/creative/src/handlers/creative/bulk-download-creatives.sqs.ts:44
  confidence: 0.6
  via: service-code
- type: PUBLISHES
  to: evt.creative.app-event-creative-copy-completed
  evidence: Unite/packages/creative-core/src/db/creative/copy-creative.ts:511
  confidence: 0.6
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.app-event-creative-copy-failed
  evidence: Unite/packages/creative-core/src/db/creative/copy-creative.ts:529
  confidence: 0.6
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.app-event-creative-copy-started
  evidence: Unite/packages/creative-core/src/db/creative/copy-creative.ts:441
  confidence: 0.6
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.app-event-creative-created
  evidence: Unite/packages/creative-core/src/db/creative/create-creative.ts:80
  confidence: 0.6
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.app-event-creative-download-prepared
  evidence: Unite/packages/creative-core/src/db/creative/download-creative.ts:379
  confidence: 0.6
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.app-event-creative-preview-updated
  evidence: Unite/packages/creative-core/src/services/update-preview/update-preview-in-parent.ts:272
  confidence: 0.6
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.app-event-creative-rasterization-completed
  evidence: Unite/services/creative/src/handlers/event-bridge/event-bridge-handler.ts:159
  confidence: 0.6
  via: service-code
- type: PUBLISHES
  to: evt.creative.app-event-creative-rasterization-failed
  evidence: Unite/services/creative/src/handlers/rasterizer-events/rasterized-failure.ts:20
  confidence: 0.6
  via: service-code
- type: PUBLISHES
  to: evt.creative.app-event-creative-rasterization-started
  evidence: Unite/services/creative/src/handlers/event-bridge/event-bridge-handler.ts:149
  confidence: 0.6
  via: service-code
- type: PUBLISHES
  to: evt.creative.app-event-creative-removed
  evidence: Unite/packages/creative-core/src/db/creative/delete-creative.ts:33
  confidence: 0.6
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.app-event-creative-shared
  evidence: Unite/packages/creative-core/src/services/creative-version-share/create-share.ts:87
  confidence: 0.6
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.app-event-creative-updated
  evidence: Unite/packages/creative-core/src/db/creative/update-creative.ts:171
  confidence: 0.6
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.app-event-creative-version-created
  evidence: Unite/services/creative/src/handlers/creative-version/create-creative-version.ts:194
  confidence: 0.6
  via: service-code
- type: PUBLISHES
  to: evt.creative.app-event-format-event-created
  evidence: Unite/packages/creative-core/src/db/creative/download-creative.ts:406
  confidence: 0.8
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.creative-brand-check-rasterization-completed
  evidence: Unite/packages/creative-core/src/services/creative-rasterization-status/add-creative-rasterization-event.ts:214
  confidence: 0.8
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.creative-brand-check-rasterization-failed
  evidence: Unite/packages/creative-core/src/services/creative-rasterization-status/add-creative-rasterization-event.ts:214
  confidence: 0.8
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.creative-preview-asset-updated
  evidence: Unite/packages/creative-core/src/utils/creative-events-publisher.ts:108
  confidence: 0.8
  via: package:creative-core
- type: PUBLISHES
  to: evt.creative.html-export-requested
  evidence: Unite/services/creative/src/features/html-export/processHtmlExportRequest.ts:19
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: evt.email.email-event
  evidence: Unite/packages/creative-core/src/services/auth/auth-creative-initiate.ts:58
  confidence: 0.8
  via: package:creative-core
- type: PUBLISHES
  to: q.creative-bulk-download-creatives
  evidence: Unite/services/creative/src/handlers/creative/bulk-download-creatives.ts:63
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.creative-copy-events-creatives
  evidence: Unite/services/creative/src/handlers/creative/bulk-copy-creatives.ts:119
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.creative-copy-selection-events
  evidence: Unite/services/creative/src/handlers/creative/bulk-copy-selection.ts:97
  confidence: 0.9
  via: service-code
- type: PUBLISHES
  to: q.creative-html-export-zip
  evidence: Unite/packages/creative-core/src/utils/creative-events-publisher.ts:78
  confidence: 0.8
  via: package:creative-core
- type: PUBLISHES
  to: q.rasterizer-screenshot-request-queue
  evidence: Unite/services/creative/src/utils/generate-static-screenshots.ts:336
  confidence: 0.9
  via: service-code
- type: READS
  to: tbl.dynamodb.asset-assets
  evidence: Unite/packages/asset/src/db/get-asset-by-source-id.ts:75
  confidence: 0.8
  via: package:asset
- type: READS
  to: tbl.dynamodb.creative-creatives
  evidence: Unite/packages/creative-core/src/db/creative-entity/repository.ts:87
  confidence: 0.8
  via: package:creative-core
- type: READS
  to: tbl.dynamodb.relation-relation-generic
  evidence: Unite/packages/relation/src/get-relations.ts:39
  confidence: 0.8
  via: package:relation
- type: WRITES
  to: tbl.dynamodb.asset-assets
  evidence: Unite/packages/creative-core/src/services/migration/backfill-asset-format-id.ts:354
  confidence: 0.8
  via: package:creative-core
- type: WRITES
  to: tbl.dynamodb.creative-creatives
  evidence: Unite/packages/creative-core/src/db/creative-entity/repository.ts:40
  confidence: 0.8
  via: package:creative-core
- type: WRITES
  to: tbl.dynamodb.relation-relation-generic
  evidence: Unite/packages/relation/src/bulk-action-in-transaction.ts:2
  confidence: 0.8
  via: package:relation
---
# creative

## Summary
Creative-authoring backend: creatives/templates CRUD, versions, sharing, bulk copy/download, HTML export, brand components, AI image generation.

## Links
- CALLS [[fn.wssbrandx.list-report-assets-for-creative-internal]]
- CONSUMES [[evt.asset.asset-created]], [[evt.asset.asset-deleted]], [[evt.asset.asset-hard-deleted]], [[evt.asset.asset-updated]], [[evt.asset.creative-version-pmh-sync-completed]], [[evt.asset.creative-version-pmh-sync-started]], [[evt.creative-share.creative-version-share-expire]], [[evt.creative-status.rasterization-status-update]], [[evt.creative.app-event-format-event-created]], [[evt.creative.creative-preview-asset-updated]], [[evt.creative.html-export-requested]], [[evt.rasterizer-service.motion-rasterized-failure]], [[evt.rasterizer-service.preview-rasterization-status-update]], [[evt.wssbrandx.creative-brand-check-status-updated]], [[q.creative-asset-events-creative]], [[q.creative-asset-relation-events]], [[q.creative-bulk-download-creatives]], [[q.creative-copy-events-creatives]], [[q.creative-copy-selection-events]], [[q.creative-format-events]], [[q.creative-html-export-events]], [[q.creative-html-export-preview-asset]], [[q.creative-html-export-zip]], [[q.creative-rasterizer-events]]
- DEPENDS_ON [[ext.google-genai]]
- EXPOSES [[api.creative.delete-v1-brand-components-component-id]], [[api.creative.delete-v1-creatives-proxy]], [[api.creative.get-v1-auth-creative-proxy]], [[api.creative.get-v1-brand-components]], [[api.creative.get-v1-brand-components-component-id]], [[api.creative.get-v1-creative-creative-id]], [[api.creative.get-v1-creative-creative-id-version-version-id-html-export]], [[api.creative.get-v1-creative-creative-id-version-version-id-share]], [[api.creative.get-v1-creative-creative-id-version-version-id-share-proxy]], [[api.creative.get-v1-creative-creative-id-version-version-id-status]], [[api.creative.get-v1-creative-formats]], [[api.creative.get-v1-creative-share-audit-project-project-id]], [[api.creative.get-v1-creative-share-audit-share-id]], [[api.creative.get-v1-creative-tag]], [[api.creative.get-v1-creative-version-version-id]], [[api.creative.get-v1-creatives]], [[api.creative.get-v1-creatives-bulk-copy-jobs-active]], [[api.creative.get-v1-creatives-bulk-copy-jobs-source-source-project-id]], [[api.creative.get-v1-creatives-bulk-copy-jobs-source-source-project-id-target-target-project-id]], [[api.creative.get-v1-creatives-bulk-copy-jobs-target-target-project-id]], [[api.creative.get-v1-latest-creative-version-creative-id]], [[api.creative.get-v2-creatives-versions-shares-proxy]], [[api.creative.patch-v1-creative-creative-id]], [[api.creative.patch-v1-creatives-bulk-delete]], [[api.creative.patch-v1-creatives-bulk-update]], [[api.creative.post-v1-auth-creative-proxy]], [[api.creative.post-v1-brand-components]], [[api.creative.post-v1-creative]], [[api.creative.post-v1-creative-asset-replicate-check]], [[api.creative.post-v1-creative-asset-replicate-create]], [[api.creative.post-v1-creative-asset-replicate-override]], [[api.creative.post-v1-creative-bulk-download]], [[api.creative.post-v1-creative-copy]], [[api.creative.post-v1-creative-creative-id-version-version-id-share]], [[api.creative.post-v1-creative-creative-id-version-version-id-share-proxy]], [[api.creative.post-v1-creative-download-creative-id]], [[api.creative.post-v1-creative-generate-image]], [[api.creative.post-v1-creative-replicate-check]], [[api.creative.post-v1-creative-replicate-create]], [[api.creative.post-v1-creative-replicate-override]], [[api.creative.post-v1-creative-version]], [[api.creative.post-v1-creatives-bulk-copy]], [[api.creative.post-v1-creatives-bulk-copy-jobs-active]], [[api.creative.post-v1-creatives-bulk-copy-precheck]], [[api.creative.post-v1-creatives-bulk-copy-selection]], [[api.creative.post-v1-creatives-proxy]], [[api.creative.post-v1-template-replicate-check]], [[api.creative.post-v1-template-replicate-create]], [[api.creative.post-v1-template-replicate-override]], [[fn.creative.activate-share-handler]], [[fn.creative.asset-events-creative-handler]], [[fn.creative.asset-relation-events-handler]], [[fn.creative.async-event-handler]], [[fn.creative.backfill-asset-creative-relations]], [[fn.creative.backfill-asset-format-id]], [[fn.creative.backfill-latest-version-formats]], [[fn.creative.bulk-download-creatives-worker]], [[fn.creative.copy-events-creative-handler]], [[fn.creative.copy-selection-events-handler]], [[fn.creative.create-html-export-zip]], [[fn.creative.creative-custom-auth]], [[fn.creative.get-creative-formats-internal]], [[fn.creative.get-creative-internal]], [[fn.creative.get-creative-rasterization-status-internal]], [[fn.creative.get-latest-creative-version-internal]], [[fn.creative.process-format-events]], [[fn.creative.process-html-export]], [[fn.creative.process-html-export-preview-asset]], [[fn.creative.process-rasterizer-events]], [[fn.creative.trigger-creative-rasterization-internal]]
- PUBLISHES [[evt.creative.app-event-commercial-open-action-performed]], [[evt.creative.app-event-creative-bulk-download-failed]], [[evt.creative.app-event-creative-bulk-download-prepared]], [[evt.creative.app-event-creative-copy-completed]], [[evt.creative.app-event-creative-copy-failed]], [[evt.creative.app-event-creative-copy-started]], [[evt.creative.app-event-creative-created]], [[evt.creative.app-event-creative-download-prepared]], [[evt.creative.app-event-creative-preview-updated]], [[evt.creative.app-event-creative-rasterization-completed]], [[evt.creative.app-event-creative-rasterization-failed]], [[evt.creative.app-event-creative-rasterization-started]], [[evt.creative.app-event-creative-removed]], [[evt.creative.app-event-creative-shared]], [[evt.creative.app-event-creative-updated]], [[evt.creative.app-event-creative-version-created]], [[evt.creative.app-event-format-event-created]], [[evt.creative.creative-brand-check-rasterization-completed]], [[evt.creative.creative-brand-check-rasterization-failed]], [[evt.creative.creative-preview-asset-updated]], [[evt.creative.html-export-requested]], [[evt.email.email-event]], [[q.creative-bulk-download-creatives]], [[q.creative-copy-events-creatives]], [[q.creative-copy-selection-events]], [[q.creative-html-export-zip]], [[q.rasterizer-screenshot-request-queue]]
- READS [[tbl.dynamodb.asset-assets]], [[tbl.dynamodb.creative-creatives]], [[tbl.dynamodb.relation-relation-generic]]
- WRITES [[tbl.dynamodb.asset-assets]], [[tbl.dynamodb.creative-creatives]], [[tbl.dynamodb.relation-relation-generic]]
