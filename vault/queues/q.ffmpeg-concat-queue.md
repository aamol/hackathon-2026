---
id: q.ffmpeg-concat-queue
type: queue
name: ffmpeg-concat-queue
fifo: true
physical_name: ffmpeg-${STAGE}-concat-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.ffmpeg-concat-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-concat-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-concat-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-concat-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-concat-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-concat-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-concat-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-concat-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# ffmpeg-concat-queue

## Links
- HAS_FIELD [[fld.ffmpeg-concat-queue.budget]], [[fld.ffmpeg-concat-queue.context]], [[fld.ffmpeg-concat-queue.global-usage-event]], [[fld.ffmpeg-concat-queue.input]], [[fld.ffmpeg-concat-queue.resource-group-id]], [[fld.ffmpeg-concat-queue.resource-id]], [[fld.ffmpeg-concat-queue.resource-type]], [[fld.ffmpeg-concat-queue.version]]
