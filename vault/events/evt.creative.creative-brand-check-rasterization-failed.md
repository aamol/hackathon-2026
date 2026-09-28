---
id: evt.creative.creative-brand-check-rasterization-failed
type: event
name: CreativeBrandCheckRasterizationFailed
detail_type: CreativeBrandCheckRasterizationFailed
source: service.creative
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.creative-brand-check-rasterization-failed.creative-id
  evidence: Unite/packages/creative-core/src/services/creative-rasterization-status/add-creative-rasterization-event.ts:219
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.creative.creative-brand-check-rasterization-failed.creative-version-id
  evidence: Unite/packages/creative-core/src/services/creative-rasterization-status/add-creative-rasterization-event.ts:220
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.creative.creative-brand-check-rasterization-failed.project-id
  evidence: Unite/packages/creative-core/src/services/creative-rasterization-status/add-creative-rasterization-event.ts:218
  confidence: 0.8
  via: package:creative-core
---
# CreativeBrandCheckRasterizationFailed

## Links
- HAS_FIELD [[fld.creative.creative-brand-check-rasterization-failed.creative-id]], [[fld.creative.creative-brand-check-rasterization-failed.creative-version-id]], [[fld.creative.creative-brand-check-rasterization-failed.project-id]]
