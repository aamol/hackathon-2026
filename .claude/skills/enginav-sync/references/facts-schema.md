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

`name`: human label: service folder, `METHOD /path` for apis, raw detail-type for events (see Normalization rules #7), id suffix for tables and queues (see Normalization rules #6), property name for fields, file name for tests.

`test` id: `test.<svc>.<origin>-<path after the last /src/>`, extension stripped, slugged. `<origin>` = the package directory for files under `Unite/packages/<dir>/`, `svc` for files under `Unite/services/<svc>/`; a path with no `/src/` (or outside services/packages) uses the whole path instead. This keeps same-named specs apart across directories and packages, e.g. `Unite/services/asset/src/handlers/create-asset.spec.ts` → `test.asset.svc-handlers-create-asset-spec`, `Unite/packages/insight-core/src/eventbridge/asset-created.spec.ts` → `test.insight.insight-core-eventbridge-asset-created-spec`, `Unite/packages/filesign/src/utils.spec.ts` → `test.resource.filesign-utils-spec` vs. `Unite/packages/validator/src/utils.spec.ts` → `test.resource.validator-utils-spec`, `Unite/services/resource/test/sqs.integration.test.ts` → `test.resource.unite-services-resource-test-sqs-integration-test`. Always build it with `python -m sync.ids test <svc> <file>`.

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
- events whose `source` is this service, queues it owns (its own queue resource) — their HAS_FIELD; tables it WRITES (their HAS_FIELD)
Every node an edge references (both ends) must be declared in this file's `nodes`, shared ones too (repeat the event/table node with the same properties the producer uses).
Consumers never write HAS_FIELD for someone else's event or queue; publishing to another service's queue or event gives PUBLISHES only, no field nodes for it (see Normalization rules #2).

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

## Normalization rules (from CP1/CP2 runs)
1. **Function nodes:** create `fn.<svc>.<key>` + EXPOSES only for functions with **no `http` event** (queue/stream/eventBridge/schedule handlers, direct-invoke targets). An http function is represented by its api node(s) only. `fn` nodes for *other* services are created only as CALLS targets.
2. **HAS_FIELD ownership:** emit HAS_FIELD on a queue or event only if **this service owns it** (its own queue resource / events whose `source` is this service). Publishing a payload to another service's queue gives PUBLISHES only — no field nodes for that queue.
3. **Field coverage:** at most the top-level properties of the payload/item type; include every PII-tagged property and the identifier properties; do not expand nested objects (tag the parent per pii-rules.md instead).
4. **External vs unresolved:** a third-party or non-Unite HTTP API whose system is identifiable (base-URL env var or client name, e.g. WPP Open project API, PMH API) → `external` node (`ext.<system-name>`) + CALLS. Use `unresolved` only when the target system itself is unknown (runtime/user-supplied URL is not an edge at all — skip it).
5. **TESTS target:** a spec that exercises an http handler → TESTS the api node(s) of that handler; a non-http handler → its `fn` node; otherwise → the service node.
6. **Table `name`:** always the id suffix, i.e. the physical name with stage removed, slugged (`insight-${self:custom.T.STAGE}-Entities` → `insight-entities`). Same for queue `name`.
7. **Event `name`:** always the raw detail-type string (e.g. `AssetCreated`, `resource.failed`).
8. **EventBridge pattern expansion:** one event per (source × detail-type) pair **unless** the pattern mixes sources and detail-types that belong to different producers (a serverless.yml comment or the handler code shows which pairs are real) — then emit only the real pairs, and mention the skipped pairs in the reply.
9. **SNS subscription FilterPolicy** (`AWS::SNS::Subscription` with `FilterPolicy` feeding an SQS queue) is treated like an eventBridge pattern: CONSUMES the event(s) (with `filter`) in addition to CONSUMES the queue. See unite-patterns.md's declarative table.
10. **Direct-scope gaps:** if a call leaves the direct workspace scope (package not in `sync.workspace` output) and the target is a table/queue named in this service's env map, emit the edge with confidence 0.6 and evidence at the in-scope call line; otherwise mention it in the reply, no edge.
