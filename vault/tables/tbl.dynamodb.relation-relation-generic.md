---
id: tbl.dynamodb.relation-relation-generic
type: table
name: relation-relation-generic
db: dynamodb
physical_name: relation-${self:custom.T.STAGE}-Relation-Generic
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- asset
- creative
- insight
- resource
edges:
- type: HAS_FIELD
  to: fld.dynamodb.relation-relation-generic.main-pk
  evidence: Unite/packages/relation/src/types.ts:12
  confidence: 0.8
  via: package:relation
- type: HAS_FIELD
  to: fld.dynamodb.relation-relation-generic.main-sk
  evidence: Unite/packages/relation/src/types.ts:18
  confidence: 0.8
  via: package:relation
- type: HAS_FIELD
  to: fld.dynamodb.relation-relation-generic.predicate-type
  evidence: Unite/packages/relation/src/types.ts:37
  confidence: 0.8
  via: package:relation
- type: HAS_FIELD
  to: fld.dynamodb.relation-relation-generic.relation-type
  evidence: Unite/packages/relation/src/types.ts:24
  confidence: 0.8
  via: package:relation
---
# relation-relation-generic

## Links
- HAS_FIELD [[fld.dynamodb.relation-relation-generic.main-pk]], [[fld.dynamodb.relation-relation-generic.main-sk]], [[fld.dynamodb.relation-relation-generic.predicate-type]], [[fld.dynamodb.relation-relation-generic.relation-type]]
