---
id: tbl.dynamodb.creative-creatives
type: table
name: creative-creatives
db: dynamodb
defined_in: Unite/services/creative/serverless.yml:1310
keys:
  pk: pk
  sk: sk
physical_name: creative-${self:custom.T.STAGE}-Creatives
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.created
  evidence: Unite/packages/creative-core/src/types.ts:180
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.created-by
  evidence: Unite/packages/creative-core/src/types.ts:178
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.favorite
  evidence: Unite/packages/creative-core/src/types.ts:184
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.modified
  evidence: Unite/packages/creative-core/src/types.ts:182
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.name
  evidence: Unite/packages/creative-core/src/types.ts:174
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.pk
  evidence: Unite/packages/creative-core/src/types.ts:172
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.preview-asset-id
  evidence: Unite/packages/creative-core/src/types.ts:183
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.sk
  evidence: Unite/packages/creative-core/src/types.ts:173
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.status
  evidence: Unite/packages/creative-core/src/types.ts:175
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.type
  evidence: Unite/packages/creative-core/src/types.ts:176
  confidence: 0.8
  via: package:creative-core
---
# creative-creatives

## Links
- HAS_FIELD [[fld.dynamodb.creative-creatives.created]], [[fld.dynamodb.creative-creatives.created-by]], [[fld.dynamodb.creative-creatives.favorite]], [[fld.dynamodb.creative-creatives.modified]], [[fld.dynamodb.creative-creatives.name]], [[fld.dynamodb.creative-creatives.pk]], [[fld.dynamodb.creative-creatives.preview-asset-id]], [[fld.dynamodb.creative-creatives.sk]], [[fld.dynamodb.creative-creatives.status]], [[fld.dynamodb.creative-creatives.type]]
