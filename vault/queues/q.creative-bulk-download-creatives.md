---
id: q.creative-bulk-download-creatives
type: queue
name: creative-bulk-download-creatives
dlq: q.creative-bulk-download-creatives-dlq
owner_service: creative
physical_name: creative-${self:custom.T.STAGE}-bulk-download-creatives
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative-bulk-download-creatives.creative-ids
  evidence: Unite/packages/creative-core/src/db/creative/bulk-download-creatives.ts:22
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.creative-bulk-download-creatives.exclude-brand-check-reports
  evidence: Unite/packages/creative-core/src/db/creative/bulk-download-creatives.ts:27
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.creative-bulk-download-creatives.project-id
  evidence: Unite/packages/creative-core/src/db/creative/bulk-download-creatives.ts:20
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.creative-bulk-download-creatives.user-id
  evidence: Unite/packages/creative-core/src/db/creative/bulk-download-creatives.ts:21
  confidence: 0.8
  via: package:creative-core
---
# creative-bulk-download-creatives

## Links
- HAS_FIELD [[fld.creative-bulk-download-creatives.creative-ids]], [[fld.creative-bulk-download-creatives.exclude-brand-check-reports]], [[fld.creative-bulk-download-creatives.project-id]], [[fld.creative-bulk-download-creatives.user-id]]
