---
id: svc.resource
type: service
name: resource
packages:
- resource-manager
path: Unite/services/resource
generated_at: '2026-09-28T12:00:00Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: EXPOSES
  to: api.resource.post-v1-resources
  evidence: Unite/services/resource/serverless.yml:40
  confidence: 1.0
  via: serverless.yml
- type: PUBLISHES
  to: evt.resource.resource-failed
  evidence: Unite/packages/resource-manager/src/callbacks/process-event-bridge.ts:9
  confidence: 0.8
  via: package:resource-manager
---
# resource

## Summary
Tracks long-running resource jobs and announces their outcome on EventBridge.

## Links
- EXPOSES [[api.resource.post-v1-resources]]
- PUBLISHES [[evt.resource.resource-failed]]
