# FreeToken Provider Data Schema

Every provider in the FreeToken catalogue is described by one JSON file in this
directory (`data/`). The app (`app/index.html`) discovers providers at runtime
from the manifest `data/providers.json`, so **adding a provider never requires
changes to the app**: a catalogue row and its detail view are both rendered from
the fields below.

## Scope

The catalogue lists **hosted text-LLM providers with verified free access**:
services you call over the internet with an API key to generate text.

Speech (TTS/STT), image, video and embedding-only services are **out of scope**,
even when they are free and hosted — the catalogue previously carried ElevenLabs,
Cartesia, Deepgram, AssemblyAI, Speechmatics, Palabra, Async Voice, Paxa Labs,
Lelapa, Viggle, Stability AI, WaveSpeed, Inferon, Clarifai, Voyage AI, Jina AI,
Qdrant and MongoDB Atlas, and all of them were pruned on 2026-11-17. A provider
stays in scope only if it serves at least one text-generation model. Self-hosted and local runtimes (Ollama,
LM Studio, llama.cpp, Jan, KoboldCpp, GPT4All, TextGen WebUI, vLLM, BentoML,
llamafile, …) are **out of scope** and must not be added — the catalogue answers
"who will run a model for me for free", not "what can I run on my own GPU".
Hosted providers that happen to be crowdsourced (AI Horde) or built on open
weights are fine, because the inference happens on someone else's hardware.

Every entry is checked against the sources recorded in its `verified` block, and
providers whose free tier has ended are removed rather than left in. Notable
exclusions as of 2026-11-17: **Cerebras** (the no-card free tier ended in August
2026; the replacement $5 credit needs a card and expires after 30 days), Chutes.ai,
Glhf.chat, Nebius, SambaNova, Venice, OpenAI, Anthropic, DeepSeek, Moonshot,
xAI, Together, Hugging Face Inference and GitHub Models.

## Adding a provider

1. Create `data/<id>.json` following this schema (see the examples below).
   `id` must be a slug and must match the filename.
2. Append `"<id>.json"` to the `providers` array in `data/providers.json`.
3. Record where the free offer was checked in `verified.sources`, and set
   `verified.checked` / `last_updated` to the date of the check.

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
| `id` | string | yes | Stable slug; must match the filename, e.g. `groq`. |
| `name` | string | yes | Display name shown in the catalogue, leaderboards and detail view. |
| `website` | string | yes | Public site URL; the detail view links here for sign-up. |
| `docs` | string | yes | API documentation or rate-limit page. |
| `signup` | string | yes | Direct URL to create a key / enter the console. |
| `description` | string | yes | One-line summary (catalogue row subtitle and link tooltip). |
| `overview` | string | yes | 2–4 sentence description of what the provider is, what its free offer covers and what limits apply. Rendered in the detail view. |
| `offer` | object | yes | Free-access classification (see below). |
| `privacy` | object | yes | Prompt-privacy classification (see below). |
| `requires_payment_card` | boolean | yes | `true` if sign-up requires a payment card. Drives the "No card" filter. |
| `last_updated` | string | yes | `YYYY-MM-DD` of the last data update. |
| `verified` | object | yes | Where and when free access was checked (see below). |
| `free_access` | array of strings | yes | Exactly four bullets summarising the free offer and its conditions, shown in the detail view. Keep each under ~80 characters. |
| `api_endpoint` | string | no | Base URL of the OpenAI-compatible API, where one exists. Omit for speech-only, embeddings-only or non-OpenAI APIs. |
| `notes` | string | no | Caveats that do not fit the bullets: phone verification, rotating free models, expiry, one-time-credit traps. |
| `models` | array | yes | Model objects (see below). Order defines display order. |

### `offer`

| Field | Type | Description |
| ----- | ---- | ----------- |
| `type` | string | One of `always-free`, `free-models`, `monthly-credits`, `research`, `trials`. Drives the catalogue filter tabs and dashboard grouping. |
| `label` | string | Badge text shown in the catalogue row and detail view, e.g. `"Always-free tier"`. |
| `tone` | string | Badge colour: `emerald`, `blue`, `amber`, `violet`, `sky`, `rose`, or `slate`. |

Guidance for picking `type`:

- `always-free` — a standing free tier that does not expire and is not a
  time-limited grant (e.g. Groq Developer, Cloudflare Workers AI, or the free
  plans of gateways such as Token Harbor and Inferbase).
- `free-models` — only a subset of models is free, or the free plan is
  rate-limited per model (e.g. OpenRouter `:free`, Z.AI Flash models, Routeway
  `:free` routes, Mixlayer).
- `monthly-credits` — a recurring allowance that resets (e.g. Vercel AI
  Gateway's $5/month, IBM watsonx Lite, Gonka Broker's monthly grant).
- `research` — free access granted for research, education or open-source use
  (e.g. SEA-LION, FreeInference).
- `trials` — a one-time credit, a time-limited trial, or a phone-verified grant
  (e.g. Scaleway's 1M tokens, Vertex AI Express' 90 days, Hyperbolic, Upstage,
  FriendliAI). **Never** use `always-free` for these.

### `privacy`

| Field | Type | Description |
| ----- | ---- | ----------- |
| `type` | string | One of `private`, `partial`, `none`. `private` satisfies the "Private prompts" filter. |
| `label` | string | Badge text shown in the catalogue row, e.g. `"No training on prompts"`. |

Use `private` only when the provider states it does not train on free-tier
prompts; `partial` for provider-dependent, opt-out or unpublished terms; `none`
when prompts may be used for training, research or review. The label should say
which.

### `verified`

| Field | Type | Description |
| ----- | ---- | ----------- |
| `checked` | string | `YYYY-MM-DD` the free offer was last confirmed. Must equal `last_updated`. |
| `sources` | array of strings | URLs used for the check: the provider's own pricing, rate-limit or docs page first, then any directory used for cross-checking. |

This is the provenance record for the row. A provider must not be added without
at least one source that shows the free offer. When a source is superseded,
re-check the provider, update `verified`/`last_updated`, and remove the entry if
the free offer no longer exists.

## Model object

| Field | Type | Required | Description |
| ----- | ---- | -------- | ----------- |
| `id` | string | yes | Stable slug, unique within the provider, e.g. `gemini-3-8-flash`. |
| `name` | string | yes | Display name. |
| `family` | string | yes | Model family; drives the family chips and the family filter dropdown. |
| `context_window` | integer | no | Context window in tokens. |
| `metrics` | object | no | Ranking metrics (see below). |
| `token_allowance` | integer | no | Free **tokens per day** granted for this model. **Leave blank (omit or `null`) to mean unlimited.** |
| `rate_limits` | string | no | Free-form statement of the real limit, e.g. `"30 RPM, 1K RPD, 200K TPD"`, `"10K neurons/day"` or `"1M free tokens (90 days)"`. Can be used alone or together with `token_allowance`. |

### `metrics`

| Field | Type | Description |
| ---- | ---- | ----------- |
| `tps` | number | Generation speed in tokens per second **on this provider** (curated estimate). |
| `intelligence` | number | Artificial Analysis Intelligence Index score (0-100). |

`intelligence` is the **Artificial Analysis Intelligence Index v5.0.1**, read
from <https://artificialanalysis.ai/leaderboards/models>. It is copied as
published — never estimated and never rescaled — so the catalogue's quality
column is comparable with everyone else's. Artificial Analysis has not scored
every model (most small and audio models are blank there); when there is no
published score, **omit the field** rather than inventing a number. If a model's
score changes upstream, update it; the index is versioned (v5.0.1 at the time of
writing), so re-read the leaderboard when bumping the version.

`tps` is a curated throughput estimate used only to rank speed; providers do not
publish comparable figures. It is **per provider**: `tools/models.py` stores a
reference throughput and `tools/speed.py` scales it by the host (`SPEED_FACTOR`,
with `MODEL_OVERRIDES` for known cases), so GPT-OSS 20B is 780 tok/s on Groq and
240 tok/s on Cloudflare Workers AI. Do not copy one host's number onto another.
Leave `metrics` out entirely for models where neither value exists (embeddings,
rerankers, speech). Token *allowance* is always `token_allowance` (tokens per
day), never a metric.

## Token allowance semantics

- `token_allowance: 200000` — a hard quota of 200,000 free tokens per day.
- `token_allowance` left blank (omitted or `null`) — **unlimited** free tokens
  per day. Rate limits may still apply via `rate_limits` (e.g. unlimited tokens
  but a capped request rate). This is the normal shape for request-capped free
  tiers such as OpenRouter (50 RPD) and Cohere (1,000 calls/month).
- For grants stated over a longer window (a one-time credit, a 90-day quota, a
  monthly allowance) `token_allowance` is the **per-day equivalent** and
  `rate_limits` states the real grant. Examples in the current data:
  - Scaleway: `1M free tokens` → `33333` tokens/day.
  - Alibaba Cloud Model Studio: `1M free tokens per model, 90 days` → `11111`.
  - Voyage AI: `200M free tokens per model` → `6666667`.
  - IBM watsonx.ai Lite: `300K tokens/month` → `10000`.
- Purely request-, neuron- or credit-denominated free tiers leave
  `token_allowance` blank and describe the real quota in `rate_limits`.
- The Token Allowance leaderboard ranks **providers**, not models: the free
  tokens/day are summed across every model in the file that carries a numeric
  `token_allowance`, and the row shows how many models contributed. Providers
  that are only request-capped (no token quota anywhere) do not appear on that
  board — they are still listed in the catalogue. One-time signup balances (for
  example Inception's 100M tokens) **do count**, but the row is labelled
  "One-time" so a credit is never mistaken for recurring capacity.
- Values are shortened for display: `1000000` → `1M`, `5400` → `5.4K`.
- When a provider gives one shared account-wide balance rather than a per-model
  quota, put the number on the single model the balance is priced against (see
  Inception) instead of copying it onto every model, so the provider total is
  not multiplied.

## Model catalogue (`tools/`)

Model rows are not hand-written per provider. `tools/models.py` holds one entry
per model — name, family, context window, Artificial Analysis score, curated TPS
— and `tools/provider_models.py` maps each provider to the model ids its free
offer reaches. `tools/rebuild_models.py` then rewrites the `models` arrays, so a
model served by ten providers has identical numbers everywhere.

To add a model: add it to `tools/models.py` with
`C("id", "Name", "Family", ctx, aa_score, tps)`, reference the id in the
provider map, and run `python3 tools/rebuild_models.py`. Providers whose free
line-up is not in the map keep whatever is in their JSON file.

`tools/new_providers_a.py` / `_b.py` hold the providers appended from
<https://freeinferencing.com/> (snapshot 2026-10-06), and
`tools/add_new_providers.py` writes them out and updates the manifest.

## Detail view

Clicking a catalogue row opens `/#/providers/<id>` — a standalone page: the
hero, the three leaderboards and the catalogue filters are hidden, the document
title becomes the provider name, and browser back returns to the index. The
older `#provider/<id>` form is still accepted.

The panel is rendered entirely from the provider file:

- `name`, `offer.label` and `privacy.label` as badges;
- `overview`;
- the four `free_access` bullets;
- `api_endpoint` (copyable), `website`, `docs`, `signup` links;
- `requires_payment_card`, `notes` and `verified` (checked date + sources);
- the full `models` table with context window, metrics, allowance and limits.

Nothing in that panel is hardcoded per provider, so a new file automatically gets
a complete detail page.

## Examples

An always-free tier with a hard daily token quota:

```json
{
  "id": "groq",
  "name": "Groq",
  "website": "https://groq.com",
  "docs": "https://console.groq.com/docs/rate-limits",
  "signup": "https://console.groq.com/keys",
  "description": "Very fast LPU inference with a standing free Developer plan and published daily caps.",
  "overview": "GroqCloud runs open models on Groq's LPU hardware and is among the fastest inference providers available. The free Developer plan needs no card and publishes per-model limits for GPT-OSS and Qwen3.x, plus Whisper for speech-to-text. Older Llama 3.x and Compound models were retired during 2026.",
  "offer": { "type": "always-free", "label": "Always-free tier", "tone": "emerald" },
  "privacy": { "type": "private", "label": "No training on prompts" },
  "requires_payment_card": false,
  "last_updated": "2026-11-17",
  "verified": {
    "checked": "2026-11-17",
    "sources": [
      "https://console.groq.com/docs/rate-limits",
      "https://free-llm.com/provider/groq-cloud"
    ]
  },
  "free_access": [
    "30 requests/minute and 1,000 requests/day per model",
    "200,000 tokens/day per model",
    "No credit card required",
    "No training on customer prompts"
  ],
  "api_endpoint": "https://api.groq.com/openai/v1",
  "notes": "Limits apply at the organisation level; cached tokens do not count towards them.",
  "models": [
    {
      "id": "gpt-oss-120b",
      "name": "GPT-OSS 120B",
      "family": "GPT-OSS",
      "context_window": 131072,
      "metrics": { "tps": 520, "intelligence": 63 },
      "token_allowance": 200000,
      "rate_limits": "30 RPM, 1K RPD, 8K TPM, 200K TPD"
    }
  ]
}
```

A free-model tier with no daily token cap, only request limits:

```json
{
  "id": "openrouter",
  "name": "OpenRouter",
  "website": "https://openrouter.ai",
  "docs": "https://openrouter.ai/docs/api-reference/limits",
  "signup": "https://openrouter.ai/keys",
  "description": "One OpenAI-compatible key for hundreds of models, including a rotating roster of :free models.",
  "overview": "OpenRouter is a single OpenAI-compatible API in front of hundreds of models from many providers. Its :free variants cost nothing but are capped at 20 requests/minute and 50 requests/day, rising to 1,000/day once $10 of credit has been purchased.",
  "offer": { "type": "free-models", "label": "Free models (:free)", "tone": "blue" },
  "privacy": { "type": "partial", "label": "Provider-dependent" },
  "requires_payment_card": false,
  "last_updated": "2026-11-17",
  "verified": {
    "checked": "2026-11-17",
    "sources": ["https://openrouter.ai/docs/api-reference/limits"]
  },
  "free_access": [
    ":free model variants cost nothing",
    "20 requests/minute",
    "50 requests/day (1,000/day after a one-time $10 credit)",
    "No credit card required"
  ],
  "api_endpoint": "https://openrouter.ai/api/v1",
  "models": [
    {
      "id": "gemma-4-31b-it-free",
      "name": "Gemma 4 31B IT (free)",
      "family": "Gemma 4",
      "context_window": 131072,
      "metrics": { "tps": 130, "intelligence": 62 },
      "rate_limits": "20 RPM, 50 RPD (1,000 after $10 credit)"
    }
  ]
}
```

A free-model-only provider with no token-denominated quota:

```json
{
  "id": "mixlayer",
  "name": "Mixlayer",
  "website": "https://mixlayer.com",
  "docs": "https://docs.mixlayer.com/credits-and-limits",
  "signup": "https://console.mixlayer.com/app/api-keys",
  "description": "Serverless open-model API with one permanently free Qwen route and no prepaid credit.",
  "overview": "Mixlayer is a serverless open-model API priced per token. Its documents state that free models do not require prepaid credit, while paid models return 402 on an empty balance. One zero-priced route, Qwen3.5 4B, is currently listed for lightweight tests and CI.",
  "offer": { "type": "free-models", "label": "Free model route", "tone": "blue" },
  "privacy": { "type": "private", "label": "No training on customer content" },
  "requires_payment_card": false,
  "last_updated": "2026-11-17",
  "verified": {
    "checked": "2026-11-17",
    "sources": [
      "https://docs.mixlayer.com/credits-and-limits",
      "https://free-llm.com/provider/mixlayer"
    ]
  },
  "free_access": [
    "Free models need no prepaid credit",
    "Qwen3.5 4B is $0 at 131K context",
    "No credit card required",
    "No training on customer content by default"
  ],
  "api_endpoint": "https://models.mixlayer.ai/v1",
  "notes": "Only one small free model; rate limits are shown in the console rather than published.",
  "models": [
    {
      "id": "qwen3-5-4b-free",
      "name": "Qwen3.5 4B (free)",
      "family": "Qwen 3.5",
      "context_window": 131072,
      "metrics": { "tps": 250, "intelligence": 45 },
      "rate_limits": "Per-org limits in console"
    }
  ]
}
```

## Maintenance rules

- Free tiers change without notice. Re-check `verified.checked` and drop any
  provider whose free offer has ended; do not keep it "for reference".
- Keep `providers.json` and the files in `data/` in sync: every listed file
  must exist, and no unlisted provider file may be left behind.
- A model should only be listed if it is reachable on that provider's free offer
  at the time of the check.
- Never present a card-gated one-time credit as a free tier: use `trials`,
  set `requires_payment_card`, and say so in `notes`.
