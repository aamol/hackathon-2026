# Vault build report

- Facts files: asset, creative, insight, resource
- Newest extraction: 2026-09-28T09:40:26Z
- Notes: 588 · Edges: 641 · Errors: 0 · Warnings: 2

## Nodes by type

| type | count |
|---|---|
| api | 75 |
| event | 29 |
| external | 5 |
| field | 216 |
| function | 56 |
| queue | 73 |
| service | 4 |
| table | 6 |
| test | 110 |
| unresolved | 14 |

## Edges by type

| type | count |
|---|---|
| CALLS | 9 |
| CONSUMES | 50 |
| DEPENDS_ON | 3 |
| EXPOSES | 129 |
| HAS_FIELD | 217 |
| PUBLISHES | 92 |
| READS | 17 |
| TESTS | 112 |
| WRITES | 12 |

## Package attribution

| package | edges | services |
|---|---|---|
| agentexec | 2 | insight |
| asset | 18 | asset, creative, insight |
| asset-core | 1 | asset, resource |
| asset-types | 90 | asset, creative, insight |
| creative-core | 32 | creative |
| creative-types | 15 | creative |
| insight-core | 21 | insight |
| relation | 8 | asset, creative, insight, resource |
| resource-manager | 25 | asset, insight, resource |
| resource-types | 21 | asset, resource |
| user | 2 | asset, insight |
| wss-app-events | 7 | creative |

## Problems
- WARNING node fld.dynamodb.asset-assets.source-type: 'data_type': keeping 'SourceType (enum)' from asset, ignoring 'SourceType' from creative
- WARNING node fld.dynamodb.asset-assets.status: 'data_type': keeping 'AssetStatus (enum)' from asset, ignoring 'AssetStatus' from creative
