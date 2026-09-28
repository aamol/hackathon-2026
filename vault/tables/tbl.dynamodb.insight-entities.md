---
id: tbl.dynamodb.insight-entities
type: table
name: insight-entities
db: dynamodb
defined_in: Unite/services/insight/serverless.yml:578
keys:
- PK
- SK
physical_name: insight-${self:custom.T.STAGE}-Entities
generated_at: '2026-09-28T09:36:16Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.asset-id
  evidence: Unite/packages/insight-core/src/db/insight.ts:79
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.canvas-id
  evidence: Unite/packages/insight-core/src/db/insight.ts:72
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.category
  evidence: Unite/packages/insight-core/src/db/insight.ts:76
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.conversation
  evidence: Unite/packages/insight-core/src/db/insight.ts:81
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.created-by
  evidence: Unite/packages/insight-core/src/db/insight.ts:83
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.description
  evidence: Unite/packages/insight-core/src/db/insight.ts:77
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.header-image
  evidence: Unite/packages/insight-core/src/db/insight.ts:88
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.image-errors
  evidence: Unite/packages/insight-core/src/db/insight.ts:97
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.insight-id
  evidence: Unite/packages/insight-core/src/db/insight.ts:71
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.media
  evidence: Unite/packages/insight-core/src/db/insight.ts:87
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.processing-state
  evidence: Unite/packages/insight-core/src/db/insight.ts:86
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.project-id
  evidence: Unite/packages/insight-core/src/db/insight.ts:73
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.review-status
  evidence: Unite/packages/insight-core/src/db/insight.ts:85
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.sources
  evidence: Unite/packages/insight-core/src/db/insight.ts:90
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.status
  evidence: Unite/packages/insight-core/src/db/insight.ts:84
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.title
  evidence: Unite/packages/insight-core/src/db/insight.ts:75
  confidence: 0.8
  via: package:insight-core
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.wpp-internal-data-flag
  evidence: Unite/packages/insight-core/src/db/insight.ts:80
  confidence: 0.8
  via: package:insight-core
---
# insight-entities

## Links
- HAS_FIELD [[fld.dynamodb.insight-entities.asset-id]], [[fld.dynamodb.insight-entities.canvas-id]], [[fld.dynamodb.insight-entities.category]], [[fld.dynamodb.insight-entities.conversation]], [[fld.dynamodb.insight-entities.created-by]], [[fld.dynamodb.insight-entities.description]], [[fld.dynamodb.insight-entities.header-image]], [[fld.dynamodb.insight-entities.image-errors]], [[fld.dynamodb.insight-entities.insight-id]], [[fld.dynamodb.insight-entities.media]], [[fld.dynamodb.insight-entities.processing-state]], [[fld.dynamodb.insight-entities.project-id]], [[fld.dynamodb.insight-entities.review-status]], [[fld.dynamodb.insight-entities.sources]], [[fld.dynamodb.insight-entities.status]], [[fld.dynamodb.insight-entities.title]], [[fld.dynamodb.insight-entities.wpp-internal-data-flag]]
