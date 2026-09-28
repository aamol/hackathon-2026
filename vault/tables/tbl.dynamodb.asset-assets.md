---
id: tbl.dynamodb.asset-assets
type: table
name: asset-assets
db: dynamodb
defined_in: Unite/services/asset/serverless.yml:511
keys:
  partition: pk
  sort: sk
physical_name: asset-${self:custom.T.STAGE}-Assets
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- asset
- creative
- insight
edges:
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.asset-id
  evidence: Unite/packages/asset-types/src/index.ts:737
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.asset-type
  evidence: Unite/packages/asset-types/src/index.ts:739
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.auto-tags
  evidence: Unite/packages/asset-types/src/index.ts:760
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.brand-check-summaries
  evidence: Unite/packages/asset-types/src/index.ts:777
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.content
  evidence: Unite/packages/asset-types/src/index.ts:761
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.created-at
  evidence: Unite/packages/asset-types/src/index.ts:741
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.created-by
  evidence: Unite/packages/asset-types/src/index.ts:740
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.et
  evidence: Unite/packages/asset-types/src/index.ts:738
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.expiry-date
  evidence: Unite/packages/asset-types/src/index.ts:776
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.favourite
  evidence: Unite/packages/asset-types/src/index.ts:758
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.format-id
  evidence: Unite/packages/asset-types/src/index.ts:756
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.gsi1pk
  evidence: Unite/packages/asset-types/src/index.ts:734
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.gsi1sk
  evidence: Unite/packages/asset-types/src/index.ts:735
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.hidden
  evidence: Unite/packages/asset-types/src/index.ts:771
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.last-used-at
  evidence: Unite/packages/asset-types/src/index.ts:746
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.metadata
  evidence: Unite/packages/asset-types/src/index.ts:770
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.motion-preview-content
  evidence: Unite/packages/asset-types/src/index.ts:769
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.pk
  evidence: Unite/packages/asset-types/src/index.ts:732
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.pmh-sync
  evidence: Unite/packages/asset-types/src/index.ts:787
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.pmh-sync-history
  evidence: Unite/packages/asset-types/src/index.ts:782
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.preview-content
  evidence: Unite/packages/asset-types/src/index.ts:765
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.project-id
  evidence: Unite/packages/asset-types/src/index.ts:736
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.sk
  evidence: Unite/packages/asset-types/src/index.ts:733
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.source-group-id
  evidence: Unite/packages/asset-types/src/index.ts:750
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.source-id
  evidence: Unite/packages/asset-types/src/index.ts:751
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.source-sub-type
  evidence: Unite/packages/asset-types/src/index.ts:749
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.source-type
  evidence: Unite/packages/asset-types/src/index.ts:748
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.status
  evidence: Unite/packages/asset-types/src/index.ts:757
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.title
  evidence: Unite/packages/asset-types/src/index.ts:747
  confidence: 0.9
  via: package:asset-types
- type: HAS_FIELD
  to: fld.dynamodb.asset-assets.user-tags
  evidence: Unite/packages/asset-types/src/index.ts:759
  confidence: 0.9
  via: package:asset-types
---
# asset-assets

## Links
- HAS_FIELD [[fld.dynamodb.asset-assets.asset-id]], [[fld.dynamodb.asset-assets.asset-type]], [[fld.dynamodb.asset-assets.auto-tags]], [[fld.dynamodb.asset-assets.brand-check-summaries]], [[fld.dynamodb.asset-assets.content]], [[fld.dynamodb.asset-assets.created-at]], [[fld.dynamodb.asset-assets.created-by]], [[fld.dynamodb.asset-assets.et]], [[fld.dynamodb.asset-assets.expiry-date]], [[fld.dynamodb.asset-assets.favourite]], [[fld.dynamodb.asset-assets.format-id]], [[fld.dynamodb.asset-assets.gsi1pk]], [[fld.dynamodb.asset-assets.gsi1sk]], [[fld.dynamodb.asset-assets.hidden]], [[fld.dynamodb.asset-assets.last-used-at]], [[fld.dynamodb.asset-assets.metadata]], [[fld.dynamodb.asset-assets.motion-preview-content]], [[fld.dynamodb.asset-assets.pk]], [[fld.dynamodb.asset-assets.pmh-sync]], [[fld.dynamodb.asset-assets.pmh-sync-history]], [[fld.dynamodb.asset-assets.preview-content]], [[fld.dynamodb.asset-assets.project-id]], [[fld.dynamodb.asset-assets.sk]], [[fld.dynamodb.asset-assets.source-group-id]], [[fld.dynamodb.asset-assets.source-id]], [[fld.dynamodb.asset-assets.source-sub-type]], [[fld.dynamodb.asset-assets.source-type]], [[fld.dynamodb.asset-assets.status]], [[fld.dynamodb.asset-assets.title]], [[fld.dynamodb.asset-assets.user-tags]]
