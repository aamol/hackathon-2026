# Facts file format (contract v0.2)

One file per service: `vault/_facts/<service>.json`, where `<service>` = folder name under `Unite/services/`.

```json
{
  "facts_version": "0.2",
  "service": "insight",
  "source_commit": "<git -C Unite rev-parse --short=12 HEAD>",
  "extracted_at": "2026-09-28T16:00:00Z",
  "nodes": [ { "id": "...", "type": "...", "name": "...", "summary": "optional, services only, 1-2 lines", ...type props } ],
  "edges": [ { "from": "...", "type": "...", "to": "...", "evidence": "Unite/<path>:<line>",
               "snippet": "exact text from that line", "confidence": 1.0, "via": "serverless.yml",
               "filter": { "only": "on CONSUMES" } } ]
}
```
Never put `edges`, `sources`, `generated_at` or `contract_version` on a node (the builder adds them).

## Node types and required properties
| type | id: `python -m sync.ids …` | required props | optional |
|---|---|---|---|
| service | `service <svc>` | `path` = `Unite/services/<svc>` | `packages` (workspace deps), `description`, `summary` |
| api | `api <svc> <METHOD> <path>` | `service`, `method` (GET/POST/PUT/PATCH/DELETE/HEAD/OPTIONS/ANY), `path`, `handler` (`Unite/<file>:<line>`) | `proxy` (true for `{proxy+}`), `authorizer` |
| event | `event <source> <detail-type>` | `source` (stage removed, e.g. `service.asset`), `detail_type` (raw, e.g. `AssetCreated`) | `bus` |
| queue | `queue <physical-name>` | `physical_name` (raw, with `${…}`) | `fifo`, `owner_service`, `dlq` (queue id) |
| function | `function <svc> <function-key>` | `service`, `function_key` | `handler` |
| table | `table <physical-name>` | `db` = `dynamodb`, `physical_name` | `defined_in` (`Unite/<file>:<line>`), `keys` |
| field | `field <owner-id> <field.path>` | `owner` (id), `data_type` | `pii`, `pii_category` (email/phone/name/address/id/financial/none), `pii_confidence` |
| test | `test <svc> <file-path>` | `file` (`Unite/…`), `framework` (jest/vitest) | |
| external | `external <name>` | – | `url` |
| unresolved | `unresolved <svc> <raw>` | `raw` (literal expression), `reason` | `candidates` (ids) |

`name`: human label: service folder, `METHOD /path` for apis, raw detail-type for events, property name for fields, file name for tests.

## Edge types
| edge | from → to |
|---|---|
| EXPOSES | service → api, function |
| CALLS | service → api, function, external, unresolved |
| PUBLISHES | service → event, queue, unresolved |
| CONSUMES | service → event, queue (`filter` = the pattern's `detail` block, flattened: `{"record.sourceType": ["RESOURCE_MANAGER"]}`) |
| READS / WRITES | service → table, unresolved |
| HAS_FIELD | event, queue, api, table → field |
| TESTS | test → service, api, function |
| DEPENDS_ON | service → external |

## Ownership (enforced by `sync.facts`)
Edges may only start at nodes this file owns:
- `svc.<service>` itself
- ids starting `api.<service>.`, `fn.<service>.`, `test.<service>.`
- events/queues this service PUBLISHES (their HAS_FIELD), tables it WRITES (their HAS_FIELD)
Every node an edge references (both ends) must be declared in this file's `nodes`, shared ones too (repeat the event/table node with the same properties the producer uses).
Consumers never write HAS_FIELD for someone else's event.

## Evidence, snippet, confidence, via
- `evidence` = `Unite/<repo-relative path>:<line>`, 1-based line you opened
- `snippet` = ≥3 characters copied verbatim from that line (the distinctive part, e.g. `detail-type`, `AssetCreated`, `new PutCommand`)
- Which line: EXPOSES → `path:` line · CONSUMES event → the `detail-type` value line (else the `source` value line) · CONSUMES queue → the `arn:` line · PUBLISHES/READS/WRITES/CALLS → the call line (`sendEventBridge(`, `new PutCommand(`, …) · HAS_FIELD → the property line in the type · TESTS → the `describe(`/import line
- confidence: serverless.yml / t.yml 1.0 · service code 0.9 · workspace package code 0.8 · inferred ≤ 0.6 · unresolved edges 0.5
- via: `serverless.yml` | `t.yml` | `service-code` | `package:<package-name>`

## Worked example (consumer side)
```json
{"from": "svc.insight", "type": "CONSUMES", "to": "evt.asset.asset-created",
 "evidence": "Unite/services/insight/serverless.yml:215", "snippet": "- AssetCreated",
 "confidence": 1.0, "via": "serverless.yml", "filter": {"record.sourceType": ["RESOURCE_MANAGER"]}}
```

## Worked example (producer side, runtime-selected detail-type)
`packages/resource-manager/src/callbacks/process-event-bridge.ts` picks the detail-type from `resourceStatusToDetailType[status]`. Open the map and emit one PUBLISHES edge per value (same evidence line: the `detailType`/`DetailType` usage or the send call), each to its own `evt.resource.<detail-type>` node.
