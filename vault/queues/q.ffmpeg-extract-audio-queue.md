---
id: q.ffmpeg-extract-audio-queue
type: queue
name: ffmpeg-extract-audio-queue
fifo: true
physical_name: ffmpeg-${STAGE}-extract-audio-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.ffmpeg-extract-audio-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-extract-audio-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-extract-audio-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-extract-audio-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-extract-audio-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-extract-audio-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-extract-audio-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-extract-audio-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# ffmpeg-extract-audio-queue

## Links
- HAS_FIELD [[fld.ffmpeg-extract-audio-queue.budget]], [[fld.ffmpeg-extract-audio-queue.context]], [[fld.ffmpeg-extract-audio-queue.global-usage-event]], [[fld.ffmpeg-extract-audio-queue.input]], [[fld.ffmpeg-extract-audio-queue.resource-group-id]], [[fld.ffmpeg-extract-audio-queue.resource-id]], [[fld.ffmpeg-extract-audio-queue.resource-type]], [[fld.ffmpeg-extract-audio-queue.version]]
