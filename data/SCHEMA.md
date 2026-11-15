# FreeToken Provider Data Schema

Every provider in the FreeToken catalogue is described by one JSON file in this
directory (`data/`). The app (`app/index.html`) discovers providers at runtime
from the manifest `data/providers.json`, so **adding a provider never requires
changes to the app**.

## Adding a provider

1. Create `data/<id>.json` following this schema (see the examples below).
2. Append `"<id>.json"` to the `providers` array in `data/providers.json`.

The order of the `providers` array is the display order in the catalogue.

## Files

| File | Purpose |
| ---- | ------- |
| `data/providers.json` | Manifest: metadata plus the ordered list of provider filenames |
| `data/<id>.json` | One file per provider |
| `data/SCHEMA.md` | This document |

## Provider object

| Field | Type | Required | Description |
| ----- | ---- | -------- | ----------- |
| `id` | string | yes | Stable slug, e.g. `provider-1`. Should match the filename. |
| `name` | string | yes | Display name shown in the catalogue and leaderboards. |
| `website` | string | yes | Public site URL; the catalogue name links here. |
| `docs` | string | yes | API documentation URL. |
| `description` | string | yes | One-line summary (shown as the catalogue link tooltip). |
| `offer` | object | yes | Free-access classification (see below). |
| `privacy` | object | yes | Prompt-privacy classification (see below). |
| `requires_payment_card` | boolean | yes | `true` if signup requires a payment card. |
| `last_updated` | string | yes | `YYYY-MM-DD` of the last data update. |
| `models` | array | yes | Model objects (see below). Order defines display order. |

### `offer`

| Field | Type | Description |
| ----- | ---- | ----------- |
| `type` | string | One of `always-free`, `free-models`, `monthly-credits`, `research`, `trials`, `community`. Drives the catalogue filter tabs. |
| `label` | string | Badge text shown in the catalogue row, e.g. `"Always-free quota"`. |
| `tone` | string | Badge colour: `emerald`, `blue`, `amber`, `violet`, `sky`, `rose`, or `slate`. |

### `privacy`

| Field | Type | Description |
| ----- | ---- | ----------- |
| `type` | string | One of `private`, `partial`, `none`. `private` satisfies the "Private prompts" filter. |
| `label` | string | Badge text shown in the catalogue row, e.g. `"Private prompts"`. |

## Model object

| Field | Type | Required | Description |
| ----- | ---- | -------- | ----------- |
| `id` | string | yes | Stable slug, e.g. `model-1`. |
| `name` | string | yes | Display name. |
| `family` | string | yes | Model family; drives the family chips and the family filter dropdown. |
| `context_window` | integer | no | Context window in tokens. |
| `metrics` | object | no | Benchmark metrics (see below). |
| `token_allowance` | integer | no | Free **tokens per day** granted for this model. **Leave blank (omit or `null`) to mean unlimited.** |
| `rate_limits` | string | no | Optional free-form rate limits for allowances not expressible as tokens/day, e.g. `"40 RPM, 1000 RPD"` (requests per minute / requests per day). Can be used alone or together with `token_allowance`. |

### `metrics`

| Field | Type | Description |
| ----- | ---- | ----------- |
| `tps` | number | Generation speed in tokens per second. |
| `intelligence` | number | Standardized 0-100 quality score. |

Note: `metrics` describes speed and quality only. Token *allowance* is always
`token_allowance` (tokens per day), never a metric.

## Token allowance semantics

- `token_allowance: 1000000` — a hard quota of 1,000,000 free tokens per day.
- `token_allowance` left blank (omitted or `null`) — **unlimited** free tokens
  per day. Rate limits may still apply via `rate_limits`
  (e.g. unlimited tokens but a capped request rate).
- The Token Allowance leaderboard ranks models by `token_allowance` with
  unlimited first, and shortens values: `1000000` → `1M`, `5000` → `5K`,
  `1200000` → `1.2M`, `5400` → `5.4K`. Models whose provider has no better
  model for the metric occupy one leaderboard slot per provider.

## Examples

A model with a hard daily quota:

```json
{
  "id": "model-1",
  "name": "Model 1",
  "family": "Family 1",
  "context_window": 131072,
  "metrics": { "tps": 240, "intelligence": 58 },
  "token_allowance": 1000000
}
```

A model with a daily quota *and* request-rate limits:

```json
{
  "id": "model-7",
  "name": "Model 7",
  "family": "Family 3",
  "metrics": { "tps": 95, "intelligence": 64 },
  "token_allowance": 1200000,
  "rate_limits": "30 RPM, 500 RPD"
}
```

An unlimited model (blank allowance) that is only request-rate limited:

```json
{
  "id": "model-26",
  "name": "Model 26",
  "family": "Family 12",
  "rate_limits": "40 RPM, 1000 RPD"
}
```

A fully unlimited model (no rate limits either):

```json
{
  "id": "model-8",
  "name": "Model 8",
  "family": "Family 3",
  "metrics": { "tps": 88, "intelligence": 60 }
}
```
