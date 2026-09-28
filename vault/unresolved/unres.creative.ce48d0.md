---
id: unres.creative.ce48d0
type: unresolved
name: publishEvent(app-event::creative.rasterization.completed) - no explicit source (AWS_LAMBDA_FUNCTION_NAME fallback)
candidates:
- evt.creative.app-event-creative-rasterization-completed
raw: publishEvent(app-event::creative.rasterization.completed) - no explicit source (AWS_LAMBDA_FUNCTION_NAME fallback)
reason: SERVICE_SOURCE env var is not set for the calling handler; app-events' getDefaultSource() falls back to process.env.AWS_LAMBDA_FUNCTION_NAME, which is not a stable declared event source
generated_at: '2026-09-28T09:40:26Z'
contract_version: '0.2'
sources:
- creative
edges: []
---
# publishEvent(app-event::creative.rasterization.completed) - no explicit source (AWS_LAMBDA_FUNCTION_NAME fallback)

## Links
_No outgoing links._
