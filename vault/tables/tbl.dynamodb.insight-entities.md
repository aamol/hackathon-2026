---
id: tbl.dynamodb.insight-entities
type: table
name: insight-entities
db: dynamodb
defined_in: Unite/services/insight/serverless.yml:572
physical_name: insight-${self:custom.T.STAGE}-Entities
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.canvas-id
  evidence: Unite/packages/insight-types/src/types.ts:163
  confidence: 0.8
  via: package:insight-types
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.created-by
  evidence: Unite/packages/insight-types/src/types.ts:176
  confidence: 0.8
  via: package:insight-types
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.insight-id
  evidence: Unite/packages/insight-types/src/types.ts:162
  confidence: 0.8
  via: package:insight-types
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.project-id
  evidence: Unite/packages/insight-types/src/types.ts:164
  confidence: 0.8
  via: package:insight-types
---
# insight-entities

## Links
- HAS_FIELD [[fld.dynamodb.insight-entities.canvas-id]], [[fld.dynamodb.insight-entities.created-by]], [[fld.dynamodb.insight-entities.insight-id]], [[fld.dynamodb.insight-entities.project-id]]
