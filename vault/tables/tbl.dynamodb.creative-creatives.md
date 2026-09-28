---
id: tbl.dynamodb.creative-creatives
type: table
name: creative-creatives
db: dynamodb
defined_in: Unite/services/creative/serverless.yml:1316
keys:
  pk: HASH
  sk: RANGE
physical_name: creative-${self:custom.T.STAGE}-Creatives
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.created-by
  evidence: Unite/packages/creative-core/src/db/creative-entity/entity.ts:23
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.name
  evidence: Unite/packages/creative-core/src/db/creative-entity/entity.ts:17
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.pk
  evidence: Unite/packages/creative-core/src/db/creative-entity/entity.ts:15
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.sk
  evidence: Unite/packages/creative-core/src/db/creative-entity/entity.ts:16
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.status
  evidence: Unite/packages/creative-core/src/db/creative-entity/entity.ts:19
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.dynamodb.creative-creatives.type
  evidence: Unite/packages/creative-core/src/db/creative-entity/entity.ts:22
  confidence: 0.8
  via: package:creative-core
---
# creative-creatives

## Links
- HAS_FIELD [[fld.dynamodb.creative-creatives.created-by]], [[fld.dynamodb.creative-creatives.name]], [[fld.dynamodb.creative-creatives.pk]], [[fld.dynamodb.creative-creatives.sk]], [[fld.dynamodb.creative-creatives.status]], [[fld.dynamodb.creative-creatives.type]]
