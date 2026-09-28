# Where edges live in Unite

Unite = TypeScript on AWS Serverless. Each service = `services/<svc>/` with `serverless.yml`; shared config in `services/t.yml`; most logic lives in workspace packages (`packages/<name>/`, imported by bare name, e.g. `from "asset"`). Use `python -m sync.workspace` for the package list.

## Resolving serverless.yml variables
| expression | resolve to |
|---|---|
| `${self:custom.T.X.Y}` | key path `X.Y` in `services/t.yml` (resolve recursively) |
| `${self:service}` | the `service:` value at the top of this serverless.yml |
| `${self:custom.T.STAGE}`, `${sls:stage}`, `${process.env.STAGE}` | stage: keep raw in physical names; the id helpers strip it |
| `${self:provider.region}`, `${aws:accountId}`, `${cf:…}`, `${cachedSsm:…}`, `!Sub`, `!GetAtt`, `!Ref` | keep raw; resolve only if the literal part names the resource |
| `!GetAtt <Logical>.Arn` | the `resources.Resources.<Logical>.Properties` of this serverless.yml (e.g. `QueueName`, `TableName`) |

## Declarative (serverless.yml) → edges, confidence 1.0, via serverless.yml
| look for | emit |
|---|---|
| `functions.<fn>.events[].http: {method, path}` | api node (`handler` = the function's `handler:` → file `src/…` + line of the exported name) + EXPOSES |
| `events[].eventBridge.pattern: {source, detail-type, detail}` | one event node per (source × detail-type) + CONSUMES; `detail` → `filter`. No detail-type → event id with detail-type `any` and note it in the reply |
| `events[].sqs: {arn}` | queue node (name from the arn literal or `!GetAtt` resource) + CONSUMES |
| `functions.<fn>.environment` / `provider.environment` | env map only (no edge): `TABLE_NAME: ${self:custom.T.INSIGHT_ENTITY.TABLE_NAME}` → `insight-${self:custom.T.STAGE}-Entities` |
| `events[].schedule` / `stream` / `s3` / `websocket` | no trigger edge (not in contract v0.2); the function still gets an fn node + EXPOSES per Normalization rule 1 (unless it also has an http event) |
| `AWS::SNS::Subscription` with `FilterPolicy` feeding an SQS queue | queue node + CONSUMES, **and** event node(s) for the event(s) the filter selects + CONSUMES (`filter` = the `FilterPolicy`, flattened) — same treatment as an eventBridge pattern (see facts-schema.md's Normalization rules #9) |

## Code → edges (grep over the scope, then open each hit)
| edge | grep (regex) | resolve |
|---|---|---|
| PUBLISHES event | `sendEventBridge\(\|PutEventsCommand\|putEvents\(` | `source` (template `service.<x>.${STAGE}` → `service.<x>`), `detailType` / `DetailType` (follow enum/const imports; runtime maps → one edge per value) |
| PUBLISHES queue | `SendMessageCommand\|SendMessageBatchCommand\|sendMessage\(` | `QueueUrl` → env var → env map → queue name; queue owned by another service → still PUBLISHES to that queue node |
| READS table | `GetCommand\|GetItemCommand\|QueryCommand\|ScanCommand\|BatchGetCommand\|BatchGetItemCommand\|TransactGetCommand` | `TableName` → env var → env map → t.yml value |
| WRITES table | `PutCommand\|PutItemCommand\|UpdateCommand\|UpdateItemCommand\|DeleteCommand\|DeleteItemCommand\|BatchWriteCommand\|BatchWriteItemCommand\|TransactWriteCommand` | same as READS |
| READS/WRITES via wrapper | repository/helper functions taking a table name (e.g. `getItem(tableName, …)`) | follow one level into the wrapper to classify read vs write |
| CALLS function | `InvokeCommand\|invokeLambda\(` | `FunctionName` → env var → t.yml (e.g. `REGIONAL_FUNCTION_ARNS.<region>.AGENT_LAMBDA_FUNCTION` = `function:agentexec-${STAGE}-useAgent` → `function agentexec useAgent`) |
| DEPENDS_ON external | imports of 3rd-party SDKs: `@google/genai`, `openai`, `@anthropic-ai/sdk`, `stripe`, `@azure/`, `launchdarkly` | one external node per SDK |
| CALLS api | `fetch\(\|axios` | URL resolves to a Unite API path → CALLS api; else the target system is identifiable (base-URL env var or client name) → `external` node + CALLS; else target system itself is unknown → `unresolved`; a runtime/user-supplied URL is not an edge at all — skip it (see facts-schema.md's Normalization rules #4) |

## Real examples
- Consumer: `services/insight/serverless.yml` ~L200-235: `assetCreated` listens to `source: service.asset.${STAGE}`, `detail-type: AssetCreated`, `detail.record.sourceType: RESOURCE_MANAGER`; `resourceFailedListener` listens to `service.resource.${STAGE}` / `resource.failed`
- Producer via wrapper: `packages/asset/src/services/pmh/sync-assets-to-pmh.ts:638` `sendEventBridge({ source: \`service.asset.${process.env.STAGE}\`, detailType: PmhSyncEventDetailTypes.CREATIVE_VERSION_PMH_SYNC_STARTED, … })`
- Producer, runtime detail-type: `packages/resource-manager/src/callbacks/process-event-bridge.ts` (`getSource()` → `service.resource.${STAGE}`, `resourceStatusToDetailType[status]`)
- Table name: `services/t.yml:1741` `INSIGHT_ENTITY.TABLE_NAME: insight-${self:custom.T.STAGE}-Entities`
- Lambda ARN map: `services/t.yml:746` `REGIONAL_FUNCTION_ARNS`

## Scale tips
- Grep first, open only hits; never read a whole package
- creative is large (≈208 TS files, 65 functions): do the declarative pass for all functions, then the code pass per grep pattern
- If a package is huge and unrelated to the service's handlers (e.g. logging/observability), it rarely holds edges; grep it anyway, don't read it
