---
id: q.asset-enrich-asset-queue
type: queue
name: asset-enrich-asset-queue
fifo: true
owner_service: asset
physical_name: asset-${self:custom.T.STAGE}-EnrichAsset-queue.fifo
generated_at: '2026-09-28T10:17:00Z'
contract_version: '0.2'
sources:
- asset
edges:
- type: HAS_FIELD
  to: fld.asset-enrich-asset-queue.pk
  evidence: Unite/packages/asset/src/utils/queue.ts:29
  confidence: 0.8
  via: package:asset
- type: HAS_FIELD
  to: fld.asset-enrich-asset-queue.sk
  evidence: Unite/packages/asset/src/utils/queue.ts:29
  confidence: 0.8
  via: package:asset
---
# asset-enrich-asset-queue

## Links
- HAS_FIELD [[fld.asset-enrich-asset-queue.pk]], [[fld.asset-enrich-asset-queue.sk]]
