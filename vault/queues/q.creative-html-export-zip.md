---
id: q.creative-html-export-zip
type: queue
name: creative-html-export-zip
fifo: true
owner_service: creative
physical_name: creative-${self:custom.T.STAGE}-html-export-zip.fifo
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative-html-export-zip.correlation-id
  evidence: Unite/packages/creative-types/src/types/html-export.types.ts:80
  confidence: 0.8
  via: package:creative-types
- type: HAS_FIELD
  to: fld.creative-html-export-zip.creative-id
  evidence: Unite/packages/creative-types/src/types/html-export.types.ts:82
  confidence: 0.8
  via: package:creative-types
- type: HAS_FIELD
  to: fld.creative-html-export-zip.creative-version-id
  evidence: Unite/packages/creative-types/src/types/html-export.types.ts:83
  confidence: 0.8
  via: package:creative-types
- type: HAS_FIELD
  to: fld.creative-html-export-zip.project-id
  evidence: Unite/packages/creative-types/src/types/html-export.types.ts:81
  confidence: 0.8
  via: package:creative-types
---
# creative-html-export-zip

## Links
- HAS_FIELD [[fld.creative-html-export-zip.correlation-id]], [[fld.creative-html-export-zip.creative-id]], [[fld.creative-html-export-zip.creative-version-id]], [[fld.creative-html-export-zip.project-id]]
