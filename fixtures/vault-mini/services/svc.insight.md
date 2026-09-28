---
id: svc.insight
type: service
name: insight
packages:
- asset
- insight-core
path: Unite/services/insight
generated_at: '2026-09-28T12:00:00Z'
contract_version: '0.2'
sources:
- insight
edges:
- type: CONSUMES
  to: evt.asset.asset-created
  evidence: Unite/services/insight/serverless.yml:213
  confidence: 1.0
  via: serverless.yml
  filter:
    record.sourceType:
    - RESOURCE_MANAGER
- type: CONSUMES
  to: evt.resource.resource-failed
  evidence: Unite/services/insight/serverless.yml:229
  confidence: 1.0
  via: serverless.yml
  filter:
    resourceCallbackSource:
    - update_resource
- type: CONSUMES
  to: q.insight-generation
  evidence: Unite/services/insight/serverless.yml:244
  confidence: 1.0
  via: serverless.yml
- type: PUBLISHES
  to: q.insight-generation
  evidence: Unite/packages/insight-core/src/queue/send-generation.ts:18
  confidence: 0.8
  via: package:insight-core
- type: READS
  to: tbl.dynamodb.insight-entities
  evidence: Unite/packages/insight-core/src/eventbridge/asset-created.ts:120
  confidence: 0.8
  via: package:insight-core
- type: WRITES
  to: tbl.dynamodb.insight-entities
  evidence: Unite/packages/insight-core/src/repository.ts:44
  confidence: 0.8
  via: package:insight-core
---
# insight

## Summary
Generates insights for assets; reacts to asset-created and resource-failed events.

## Links
- CONSUMES [[evt.asset.asset-created]], [[evt.resource.resource-failed]], [[q.insight-generation]]
- PUBLISHES [[q.insight-generation]]
- READS [[tbl.dynamodb.insight-entities]]
- WRITES [[tbl.dynamodb.insight-entities]]
