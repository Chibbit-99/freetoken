"""Lead verification pass, checked 2026-11-17 (part J).

Each row here started as an unverified lead from the previous sweep and was read
first-party before being written: Nexusify's docs state the weekly $25 credit and
the 130 rpm cap, UnoRouter's front page counts 159 `:free` routes out of 294,
onomeo's integration docs describe free-model call quotas, StudioLM's landing
page and quickstart describe a free daily chat allowance, and DGrid publishes a
$0/M router model. Leads that failed the check are recorded in
data/LEAD_VERIFICATION.md instead of being added.
"""

# fmt: off
PART_J = [
    ("nexusify", "Nexusify", "https://nexusify.co", "mc", "Weekly $25 credit", "pp",
     "Routed upstreams, check per model", False,
     "Router that credits $25 of usage every Monday with no card and a 130 rpm cap.",
     "Nexusify exposes 99 text models — Gemini, GPT, Llama, Mistral, Grok, DeepSeek and more — through one OpenAI-compatible endpoint at api.nexusify.co/v1. Every account gets $25 in free credits that renew every Monday, with no card to start and a 130 requests-per-minute ceiling; paid credits only draw after the free ones run out and never expire. Sign-in is by Google, Discord or CAPTCHA. Image models sit on the same key at a flat per-request price.",
     ["$25 free credit renewed every Monday", "130 requests/minute on the free credit",
      "No card to start; Google, Discord or CAPTCHA login", "99 text models on one OpenAI-compatible endpoint"],
     [{"id": "gemini-2.5-flash", "name": "Gemini 2.5 Flash", "family": "Gemini", "context_window": 1048576},
      {"id": "gpt-4o-mini", "name": "GPT-4o mini", "family": "GPT-4o", "context_window": 131072},
      {"id": "deepseek-v3.2", "name": "DeepSeek V3.2", "family": "DeepSeek", "context_window": 131072},
      {"id": "qwen3-235b-a22b", "name": "Qwen3 235B A22B", "family": "Qwen 3", "context_window": 262144},
      {"id": "kimi-k2.5", "name": "Kimi K2.5", "family": "Kimi", "context_window": 262144},
      {"id": "mistral-large-3", "name": "Mistral Large 3", "family": "Mistral", "context_window": 262144},
      {"id": "llama-3.1-405b-instruct", "name": "Llama 3.1 405B", "family": "Llama 3.1", "context_window": 131072},
      {"id": "grok-3", "name": "Grok 3", "family": "Grok", "context_window": 131072}],
     "Credits are denominated in dollars, not tokens; $25/week buys far more on a small model than on a frontier one."),

    ("unorouter", "UnoRouter", "https://unorouter.com", "fm", "159 free models", "pp",
     "Routed upstreams, check per model", False,
     "Router with 294 models behind one key, 159 of them marked free.",
     "UnoRouter fronts 294 models from 52+ upstreams through a single OpenAI-compatible key. Its own count marks 159 of them free — the `:free` suffix marks the route — including Gemini 3.5 Flash Lite, Gemma 4 12B, Codestral, Mistral Small, Cohere North Mini Code, Upstage Syn Pro and Nemotron 3 Nano Omni. It is aimed at coding agents and character-chat clients, with setup guides for Claude Code, Cline, Roo Code, SillyTavern and Open WebUI; paid routes share the same key.",
     ["294 models, 159 marked free", "One OpenAI-compatible key for every route",
      "Setup guides for coding agents and chat clients", "Free routes carry a `:free` suffix"],
     [{"id": "google/gemini-3.5-flash-lite:free", "name": "Gemini 3.5 Flash Lite", "family": "Gemini", "context_window": 1048576},
      {"id": "google/gemma-4-12b:free", "name": "Gemma 4 12B", "family": "Gemma 4", "context_window": 131072},
      {"id": "mistral/codestral-latest:free", "name": "Codestral", "family": "Codestral", "context_window": 262144},
      {"id": "mistral/mistral-small:free", "name": "Mistral Small", "family": "Mistral", "context_window": 131072},
      {"id": "cohere/north-mini-code:free", "name": "North Mini Code", "family": "Cohere", "context_window": 262144},
      {"id": "upstage/syn-pro:free", "name": "Syn Pro", "family": "Upstage", "context_window": 131072}],
     "Free routes rotate with upstream capacity; check the model page's own limit before depending on one."),

    ("onomeo", "onomeo", "https://onomeo.com", "fm", "Free-model calls from a shared pool", "pp",
     "Free calls logged upstream", False,
     "Chat front-end with an OpenAI-compatible endpoint and a site-wide free-call pool.",
     "onomeo runs a chat site and exposes the same models through https://onomeo.com/v1, OpenAI-compatible. Free usage is a site-wide pool of free-model calls refreshed every five hours and shared by every account, shown on the models page as a percentage left; the API returns account_quota (403) once your share is spent and network_quota or site_busy (429) when the shared pool is under load. The separately suffixed free model ids that older directories listed are gone — the 44-model catalogue now prices every named model — so the free pool is the only no-top-up route. Paid models such as Claude and GPT need a balance.",
     ["Site-wide free-model call pool, refreshed every 5 hours", "No top-up needed for the free pool",
      "OpenAI-compatible https://onomeo.com/v1", "Paid models only if you add balance"],
     [{"id": "gemma-4-31b", "name": "Gemma 4 31B", "family": "Gemma 4", "context_window": 262144,
       "rate_limits": "Site-wide free-call pool per 5 hours; 403 account_quota when spent"}],
     "The free pool is shared across all accounts, so the percentage shown is the whole service's remainder, not yours. Update: on 2026-11-18 the models page no longer carries the separately suffixed free ids, only the shared pool."),

    ("studiolm", "StudioLM", "https://studiolm.dev", "fm", "Free daily chat allowance", "pp",
     "Check provider policy", False,
     "Image-generation site whose API also serves chat with a free daily token allowance.",
     "StudioLM is a browser image generator with a developer API at api.studiolm.dev. Images cost a cent each from prepaid credit, but the API's chat completions route carries a free daily token allowance on the small open model it serves, gemma-3-12b-it-qat, so text generation works without adding funds. Routes follow the OpenAI layout and there is a Python SDK called studiolm.",
     ["Free daily token allowance on the chat route", "OpenAI-shaped /v1 routes and a Python SDK",
      "No card needed for chat", "Image generation is paid ($0.01 per image)"],
     [{"id": "gemma-3-12b-it-qat", "name": "Gemma 3 12B IT QAT", "family": "Gemma 3", "context_window": 131072,
       "rate_limits": "Free daily token allowance, amount not published"}],
     "The free allowance covers chat only; images always draw on prepaid credit."),

    ("dgrid", "DGrid", "https://dgrid.ai", "af", "Free Models Router at $0/M", "pp",
     "Aggregated free compute, check per model", False,
     "Free router model that schedules across free compute and bills $0 per token.",
     "DGrid publishes a single router model, dgridai/free, priced at $0 per million input and output tokens. It schedules across whatever free capacity it has — general chat, reasoning, coding help, multilingual writing — so you call one model ID through POST /v1/chat/completions at https://api.dgrid.ai/v1 and get whichever upstream is healthy, rather than choosing a model yourself. A free API key is all that is needed.",
     ["$0/M input and output tokens", "OpenAI-compatible /v1/chat/completions",
      "Free API key, no card", "Upstream model varies per request"],
     [{"id": "dgridai/free", "name": "Free Models Router", "family": "DGrid", "context_window": 131072,
       "rate_limits": "Free router; capacity shared across free upstreams"}],
     "The backing model is chosen at request time, so throughput and capability vary."),
]
