---
id: tbl.dynamodb.resource-resources
type: table
name: resource-resources
db: dynamodb
defined_in: Unite/services/resource/serverless.yml:314
keys:
  partition: resourceGroupId
  sort: resourceId
physical_name: resource-${self:custom.T.STAGE}-Resources
generated_at: '2026-09-28T10:17:00Z'
contract_version: '0.2'
sources:
- asset
- resource
edges:
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.budget
  evidence: Unite/packages/resource-types/src/types.ts:235
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.callbacks
  evidence: Unite/packages/resource-types/src/types.ts:207
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.context
  evidence: Unite/packages/resource-types/src/types.ts:234
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.created
  evidence: Unite/packages/resource-types/src/types.ts:152
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.global-passes
  evidence: Unite/packages/resource-types/src/types.ts:222
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:216
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.history-group
  evidence: Unite/packages/resource-types/src/types.ts:227
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.history-index
  evidence: Unite/packages/resource-types/src/types.ts:229
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.history-timestamp
  evidence: Unite/packages/resource-types/src/types.ts:228
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.input
  evidence: Unite/packages/resource-types/src/types.ts:160
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.last-updated
  evidence: Unite/packages/resource-types/src/types.ts:153
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.last-updated-region
  evidence: Unite/packages/resource-types/src/types.ts:162
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.output
  evidence: Unite/packages/resource-manager/src/resource/update-resource.ts:21
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.output
  evidence: Unite/packages/resource-types/src/types.ts:161
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.percentage
  evidence: Unite/packages/resource-types/src/types.ts:159
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.queue-position
  evidence: Unite/packages/resource-types/src/types.ts:205
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:154
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:156
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:157
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.timeout-at
  evidence: Unite/packages/resource-types/src/types.ts:212
  confidence: 0.8
  via: package:resource-types
- type: HAS_FIELD
  to: fld.dynamodb.resource-resources.version
  evidence: Unite/packages/resource-types/src/types.ts:158
  confidence: 0.8
  via: package:resource-types
---
# resource-resources

## Links
- HAS_FIELD [[fld.dynamodb.resource-resources.budget]], [[fld.dynamodb.resource-resources.callbacks]], [[fld.dynamodb.resource-resources.context]], [[fld.dynamodb.resource-resources.created]], [[fld.dynamodb.resource-resources.global-passes]], [[fld.dynamodb.resource-resources.global-usage-event]], [[fld.dynamodb.resource-resources.history-group]], [[fld.dynamodb.resource-resources.history-index]], [[fld.dynamodb.resource-resources.history-timestamp]], [[fld.dynamodb.resource-resources.input]], [[fld.dynamodb.resource-resources.last-updated]], [[fld.dynamodb.resource-resources.last-updated-region]], [[fld.dynamodb.resource-resources.output]], [[fld.dynamodb.resource-resources.percentage]], [[fld.dynamodb.resource-resources.queue-position]], [[fld.dynamodb.resource-resources.resource-group-id]], [[fld.dynamodb.resource-resources.resource-id]], [[fld.dynamodb.resource-resources.resource-type]], [[fld.dynamodb.resource-resources.timeout-at]], [[fld.dynamodb.resource-resources.version]]
