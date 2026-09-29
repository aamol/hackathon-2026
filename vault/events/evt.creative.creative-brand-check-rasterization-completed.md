---
id: evt.creative.creative-brand-check-rasterization-completed
type: event
name: CreativeBrandCheckRasterizationCompleted
detail_type: CreativeBrandCheckRasterizationCompleted
source: service.creative
generated_at: '2026-09-28T10:17:01Z'
contract_version: '0.2'
sources:
- creative
edges:
- type: HAS_FIELD
  to: fld.creative.creative-brand-check-rasterization-completed.creative-id
  evidence: Unite/packages/creative-core/src/services/creative-rasterization-status/add-creative-rasterization-event.ts:219
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.creative.creative-brand-check-rasterization-completed.creative-version-id
  evidence: Unite/packages/creative-core/src/services/creative-rasterization-status/add-creative-rasterization-event.ts:220
  confidence: 0.8
  via: package:creative-core
- type: HAS_FIELD
  to: fld.creative.creative-brand-check-rasterization-completed.project-id
  evidence: Unite/packages/creative-core/src/services/creative-rasterization-status/add-creative-rasterization-event.ts:218
  confidence: 0.8
  via: package:creative-core
---
# CreativeBrandCheckRasterizationCompleted

## Links
- HAS_FIELD [[fld.creative.creative-brand-check-rasterization-completed.creative-id]], [[fld.creative.creative-brand-check-rasterization-completed.creative-version-id]], [[fld.creative.creative-brand-check-rasterization-completed.project-id]]
