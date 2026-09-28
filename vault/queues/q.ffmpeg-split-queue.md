---
id: q.ffmpeg-split-queue
type: queue
name: ffmpeg-split-queue
fifo: true
physical_name: ffmpeg-${STAGE}-split-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.ffmpeg-split-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-split-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-split-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-split-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-split-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-split-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-split-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-split-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# ffmpeg-split-queue

## Links
- HAS_FIELD [[fld.ffmpeg-split-queue.budget]], [[fld.ffmpeg-split-queue.context]], [[fld.ffmpeg-split-queue.global-usage-event]], [[fld.ffmpeg-split-queue.input]], [[fld.ffmpeg-split-queue.resource-group-id]], [[fld.ffmpeg-split-queue.resource-id]], [[fld.ffmpeg-split-queue.resource-type]], [[fld.ffmpeg-split-queue.version]]
