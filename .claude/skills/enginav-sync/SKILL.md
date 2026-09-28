---
name: enginav-sync
description: Extracts Unite monorepo services into the EngiNav Obsidian vault (services, APIs, EventBridge events, SQS queues, DynamoDB tables, Lambda functions, fields, tests; every link with file:line evidence). Use when asked to sync, extract, refresh or update the EngiNav vault or knowledge base for Unite services, or after Unite code changed, e.g. "/enginav-sync resource", "/enginav-sync asset insight", "/enginav-sync --changed".
---

# enginav-sync

You write `vault/_facts/<service>.json` (facts with evidence). Scripts turn facts into notes (`sync.build_vault`) and check them (`sync.validate`). Never edit `vault/**/*.md` by hand.

## Paths
- Run every command from the EngiNav repo root (the folder with `sync/` and `vault/`), with its `.venv` active
- `$UNITE` = the Unite checkout: `../Unite` unless the user named another path. If it does not exist, ask for it
- `$SKILL` = this skill's folder (`.claude/skills/enginav-sync`)

## Step 1: Pick services
- `/enginav-sync <svc> [<svc> ...]`: those folder names under `$UNITE/services/`
- `/enginav-sync --changed`: run `python -m sync.changed --unite $UNITE --vault vault`. It prints one service per line. Empty → tell the user the vault is up to date and stop
- Check each exists: `ls $UNITE/services/<svc>/serverless.yml`. Missing → tell the user and skip it
- Fields/PII + tests: include them unless the user asked for a quick sync

## Step 2: Extract (one subagent per service, all in one message so they run in parallel)
Dispatch a `general-purpose` subagent per service with this prompt (fill the `<...>`):

```
Extract ONE Unite service, `<svc>`, into an EngiNav facts file.

Unite checkout: <absolute $UNITE>. Evidence paths start with `Unite/` = that folder.
EngiNav repo root (run commands here, .venv active): <absolute repo root>
Output: vault/_facts/<svc>.json (overwrite if present)
Include fields/PII and tests: <yes|no>

Before starting, read fully: <$SKILL>/references/facts-schema.md and <$SKILL>/references/unite-patterns.md
(and <$SKILL>/references/pii-rules.md if fields = yes).

Steps:
1. source_commit = `git -C <UNITE> rev-parse --short=12 HEAD`; extracted_at = `date -u +%Y-%m-%dT%H:%M:%SZ`
2. Scope = `python -m sync.workspace --unite <UNITE> <svc>`: services/<svc>/ plus the listed package directories.
   Evidence in services/<svc>/src → via "service-code", confidence 0.9. In a package → via "package:<name>", 0.8
3. Declarative pass on services/<svc>/serverless.yml (resolve ${self:custom.T.…} in services/t.yml):
   service node, http → api + EXPOSES, eventBridge → event + CONSUMES (+ filter), sqs → queue + CONSUMES.
   Build an env map per function: env var → resolved value
4. Code pass: grep the patterns from unite-patterns.md over the scope (skip *.spec.ts, __mocks__, node_modules, dist).
   Open each hit and resolve names (enums, constants, template literals, lookup maps, env vars via the env map).
   Emit PUBLISHES / READS / WRITES / CALLS / DEPENDS_ON. One call site may publish several events.
   Cannot resolve → unresolved node with raw + reason. Never guess a target
5. If fields = yes: payload types / zod schemas of events+queues you PUBLISH, and items of tables you WRITE → field
   nodes + HAS_FIELD, tagged per pii-rules.md. *.spec.ts / *.test.ts that exercise this service's handlers → TESTS
6. Build every id with `python -m sync.ids <kind> <args…>`. Never type ids by hand
7. Write the JSON. For each edge, open the evidence file at that line and copy `snippet` (≥3 chars) verbatim from it
8. Run `python -m sync.facts vault/_facts/<svc>.json --unite <UNITE>` and fix every problem it prints
   (correct the line/snippet, or delete an edge you cannot prove). Repeat until it exits 0

Reply with: node and edge counts by type, the unresolved references (raw + reason), and anything uncertain.
Do not paste the JSON.
```

## Step 3: Build and validate
```bash
python -m sync.build_vault --vault vault --unite $UNITE
python -m sync.validate vault --unite $UNITE
```
- Both exit 0 → Step 4
- Build exit 1 → stderr lines look like `ERROR <svc>: …`. Send each service its own lines in a new subagent: "Fix these problems in vault/_facts/<svc>.json. Re-read the evidence lines in <UNITE>; fix line numbers/snippets or remove edges you cannot prove. Do not add new edges. Finish with `python -m sync.facts … --unite …` exiting 0." Rebuild. At most 2 rounds
- Still failing after 2 rounds → rebuild with `--allow-drops` and tell the user which edges were dropped (listed in `vault/_meta/run-report.md`)
- Build exit 2 → a facts file is unusable; the message names the file and JSON path. Fix it (subagent), rebuild
- Validate errors after a clean build are a bug in the scripts: stop and report them

## Step 4: Report to the user
- For each extracted service: `python -m sync.eval diff vault/_facts/<svc>.json`
- Summarize: notes/edges/warnings from `vault/_meta/run-report.md`, added/removed edges per service, unresolved refs, conflict and stale warnings, and the subagents' uncertainties
- Ask the user to review, then commit `vault/_facts/` and `vault/`. Do not commit unless asked

## Rules
- No edge without an evidence line you actually opened; `snippet` copied exactly from that line
- Unresolvable target → `unresolved` node, never a guessed one
- Ids only from `python -m sync.ids`
- Facts files follow the ownership rules in facts-schema.md; `sync.facts` enforces them
