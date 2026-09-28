---
id: evt.creative.creative-preview-asset-updated
type: event
name: CreativePreviewAssetUpdated
detail_type: CreativePreviewAssetUpdated
source: service.creative
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.creative-preview-asset-updated.correlation-id
  evidence: Unite/packages/creative-types/src/types/html-export.types.ts:89
  confidence: 0.8
  via: package:creative-types
- type: HAS_FIELD
  to: fld.creative.creative-preview-asset-updated.creative-id
  evidence: Unite/packages/creative-types/src/types/html-export.types.ts:91
  confidence: 0.8
  via: package:creative-types
- type: HAS_FIELD
  to: fld.creative.creative-preview-asset-updated.creative-version-id
  evidence: Unite/packages/creative-types/src/types/html-export.types.ts:92
  confidence: 0.8
  via: package:creative-types
- type: HAS_FIELD
  to: fld.creative.creative-preview-asset-updated.preview-asset-id
  evidence: Unite/packages/creative-types/src/types/html-export.types.ts:93
  confidence: 0.8
  via: package:creative-types
- type: HAS_FIELD
  to: fld.creative.creative-preview-asset-updated.project-id
  evidence: Unite/packages/creative-types/src/types/html-export.types.ts:90
  confidence: 0.8
  via: package:creative-types
---
# CreativePreviewAssetUpdated

## Links
- HAS_FIELD [[fld.creative.creative-preview-asset-updated.correlation-id]], [[fld.creative.creative-preview-asset-updated.creative-id]], [[fld.creative.creative-preview-asset-updated.creative-version-id]], [[fld.creative.creative-preview-asset-updated.preview-asset-id]], [[fld.creative.creative-preview-asset-updated.project-id]]
