---
id: tbl.dynamodb.insight-entities
type: table
name: insight-entities
db: dynamodb
defined_in: Unite/services/t.yml:1742
keys:
- PK
- SK
physical_name: insight-${self:custom.T.STAGE}-Entities
generated_at: '2026-09-28T12:00:00Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: HAS_FIELD
  to: fld.dynamodb.insight-entities.entity-id
  evidence: Unite/packages/insight-core/src/repository.ts:12
  confidence: 0.8
  via: package:insight-core
---
# insight-entities

## Links
- HAS_FIELD [[fld.dynamodb.insight-entities.entity-id]]
