"""Providers re-verified from the July 2026 research ledger (part F).

The ledger listed 138 platforms. Every row that was not already in the catalogue
was re-checked against the vendor's own pages on 2026-11-17; these three survived:

  - NaraRouter   — /api/plans exposes a "Start free, forever" plan: 7,000,000
                   tokens/day, 15 RPM, no card (router.bynara.id/api/plans).
  - PLaMo API    — PFN's Free plan exists for PLaMo API/Chat and plamo-3.0-fin-beta
                   carries no token charge on any plan, 50 requests/24h
                   (docs.plamo.preferredai.jp/en/api).
  - ApiFreeLLM   — Community Best-Effort sandbox: free key, 50 requests/day and
                   8K input tokens, best-effort capacity
                   (apifreellm.com/en/api-access).

Rejected in this pass, with the reason recorded so the ledger is not re-mined:
  - GitHub Models  — fully retired on 2026-07-30 (docs.github.com/github-models).
  - kluster.ai     — sunset 2026-06-09 after the MITO acquisition.
  - Chutes         — pay-per-token only, no free tier on its pricing page.
  - FreeTheAI      — "The free tier is closed for most users" on its homepage.
  - AIgateway.sh   — credit top-ups (3x bonus), no free allowance.
  - glhf.chat      — origin certificate broken, endpoint effectively dead.
  - OW Gateway     — owgateway.xyz no longer resolves (Cloudflare tunnel gone).
  - Infron, TeamoRouter, X-Hero, AnyAPI, UnoRouter, AINative, NavyAI, Reka,
    Codestral, Modals/Portkey/Helicone-style proxies — no first-party free tier.
"""

# fmt: off
PART_F = [
    ("nara-router", "NaraRouter", "https://router.bynara.id", "af", "7M tokens/day free plan", "pp",
     "Third-party upstream routing", False,
     "Indonesian router with a permanent free plan: 7M tokens a day, no card.",
     "NaraRouter is an OpenAI-compatible gateway run by PT. NARA PEMECUT DIGITAL that fronts 40-plus aliases from Anthropic, DeepSeek, GLM, OpenAI, Moonshot, MiniMax and Qwen. Its plan endpoint publishes a Free tier that is explicitly permanent — \"start free, forever\" — with a 7,000,000-token daily cap, 15 requests/minute and no payment method. The same base URL also speaks the Anthropic Messages and OpenAI Responses formats, and paid plans raise the daily cap rather than replacing the free one.",
     ["Free plan: 7,000,000 tokens/day, 15 RPM", "No card required", "Chat, Messages and Responses endpoints",
      "Paid tiers only raise the daily cap"],
     [{"id": "deepseek-v4-flash", "name": "DeepSeek V4 Flash", "family": "DeepSeek V4",
       "context_window": 262144, "rate_limits": "Free plan: 7M tokens/day, 15 RPM"},
      {"id": "glm-5-3-flash", "name": "GLM-5.3 Flash", "family": "GLM 5.3",
       "context_window": 1048576, "rate_limits": "Free plan: 7M tokens/day, 15 RPM"}],
     "The Free plan's model list is resolved per key from /v1/models; prices and limits are set in IDR."),

    ("plamo", "PLaMo API (Preferred Networks)", "https://plamo.preferredai.jp", "af", "Free plan with daily caps", "nn",
     "Free plan trains on your prompts", False,
     "Preferred Networks' Japanese flagship models with a free API plan.",
     "PLaMo is Preferred Networks' scratch-built Japanese foundation model family, served from api.platform.preferredai.jp with an OpenAI-compatible chat endpoint. PLaMo API has a Free plan that needs no card — PLaMo Chat runs on the same account — and plamo-3.0-fin-beta, the financial trial model, carries no token charge on any plan but is capped at 50 requests per 24 hours. The Free plan reserves prompts and completions for training; the paid Standard and Provider plans do not.",
     ["Free plan on PLaMo API and Chat", "plamo-3.0-fin-beta is untokenised on every plan",
      "262K context, 20,480 output tokens", "No card required"],
     [{"id": "plamo-3.1-prime", "name": "PLaMo 3.1 Prime", "family": "PLaMo", "context_window": 262144},
      {"id": "plamo-3.0-fin-beta", "name": "PLaMo 3.0 Fin Beta", "family": "PLaMo", "context_window": 256000,
       "rate_limits": "Free on every plan: 50 requests per 24 hours"}],
     "The Free plan's caps are unpublished and only visible in the console; it trains on what you send."),

    ("api-free-llm", "ApiFreeLLM", "https://apifreellm.com", "af", "50 free requests/day", "pp",
     "Check provider policy", False,
     "Community sandbox that hands out a free key for a single hosted model.",
     "ApiFreeLLM splits its service in two: a Community Best-Effort sandbox that is free and a credit-based Managed path that is not. The free tier needs only a Google sign-in, takes 50 requests a day with an 8,000-token input ceiling, and answers through a single model with no reliability guarantee — its own dashboard reported 74.5% success and roughly 25 tokens/second over a recent 24 hours. The endpoint takes `message` rather than `messages`, so the OpenAI SDKs cannot be pointed at it.",
     ["50 free requests/day", "8,000-token input ceiling", "Google sign-in, no card",
      "Best-effort sandbox; OpenAI-compatible endpoint is paid-only"],
     [{"id": "apifreellm", "name": "ApiFreeLLM Community", "family": "ApiFreeLLM",
       "rate_limits": "50 requests/day; 8K input tokens; best-effort capacity"}],
     "Custom request schema (message, not messages) and roughly 75% success in the vendor's own metrics."),
]
# fmt: on
