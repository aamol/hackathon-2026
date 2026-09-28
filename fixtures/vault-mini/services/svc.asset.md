---
id: svc.asset
type: service
name: asset
packages:
- asset
- resource-manager
path: Unite/services/asset
generated_at: '2026-09-28T12:00:00Z'
contract_version: '0.2'
sources:
- asset
edges:
- type: CALLS
  to: unres.asset.a1b2c3
  evidence: Unite/packages/asset/src/services/pmh/client.ts:14
  confidence: 0.5
  via: package:asset
- type: CONSUMES
  to: evt.resource.resource-failed
  evidence: Unite/services/asset/serverless.yml:246
  confidence: 1.0
  via: serverless.yml
  filter:
    resourceCallbackSource:
    - update_resource
- type: EXPOSES
  to: api.asset.get-v1-assets-id
  evidence: Unite/services/asset/serverless.yml:55
  confidence: 1.0
  via: serverless.yml
- type: PUBLISHES
  to: evt.asset.asset-created
  evidence: Unite/packages/asset/src/events/asset-created.ts:30
  confidence: 0.8
  via: package:asset
---
# asset

## Summary
Stores creative assets and emits AssetCreated when a resource finishes.

## Links
- CALLS [[unres.asset.a1b2c3]]
- CONSUMES [[evt.resource.resource-failed]]
- EXPOSES [[api.asset.get-v1-assets-id]]
- PUBLISHES [[evt.asset.asset-created]]
