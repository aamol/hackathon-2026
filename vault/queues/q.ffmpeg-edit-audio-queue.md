---
id: q.ffmpeg-edit-audio-queue
type: queue
name: ffmpeg-edit-audio-queue
fifo: true
physical_name: ffmpeg-${STAGE}-edit-audio-queue.fifo
generated_at: '2026-09-28T08:25:35Z'
contract_version: '0.2'
sources:
- resource
edges:
- type: HAS_FIELD
  to: fld.ffmpeg-edit-audio-queue.budget
  evidence: Unite/packages/resource-types/src/types.ts:281
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-edit-audio-queue.context
  evidence: Unite/packages/resource-types/src/types.ts:287
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-edit-audio-queue.global-usage-event
  evidence: Unite/packages/resource-types/src/types.ts:301
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-edit-audio-queue.input
  evidence: Unite/packages/resource-types/src/types.ts:271
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-edit-audio-queue.resource-group-id
  evidence: Unite/packages/resource-types/src/types.ts:268
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-edit-audio-queue.resource-id
  evidence: Unite/packages/resource-types/src/types.ts:300
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-edit-audio-queue.resource-type
  evidence: Unite/packages/resource-types/src/types.ts:269
  confidence: 0.8
  via: package:resource-manager
- type: HAS_FIELD
  to: fld.ffmpeg-edit-audio-queue.version
  evidence: Unite/packages/resource-types/src/types.ts:270
  confidence: 0.8
  via: package:resource-manager
---
# ffmpeg-edit-audio-queue

## Links
- HAS_FIELD [[fld.ffmpeg-edit-audio-queue.budget]], [[fld.ffmpeg-edit-audio-queue.context]], [[fld.ffmpeg-edit-audio-queue.global-usage-event]], [[fld.ffmpeg-edit-audio-queue.input]], [[fld.ffmpeg-edit-audio-queue.resource-group-id]], [[fld.ffmpeg-edit-audio-queue.resource-id]], [[fld.ffmpeg-edit-audio-queue.resource-type]], [[fld.ffmpeg-edit-audio-queue.version]]
