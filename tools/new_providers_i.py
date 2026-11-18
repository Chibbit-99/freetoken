"""Providers found with multilingual and model-targeted searches, checked 2026-11-17 (part I).

ElectronHub publishes a 24-model `:free` list with context sizes on its models
page; AnyAPI publishes its Free plan ($0, 100K ANY tokens/day, no card) on the
pricing page but only reveals which models are free after login, so its rows
carry the models its directory names publicly.
"""

# fmt: off
PART_I = [
    ("electronhub", "Electron Hub", "https://www.electronhub.ai", "fm", "Free plan with 24 free models", "pp",
     "Free-model requests served by ad-supported upstreams", False,
     "Gateway with a permanent free plan: 200 free-model requests a day plus $0.25 weekly credit.",
     "Electron Hub routes 600+ models through an OpenAI- and Anthropic-compatible endpoint and keeps 24 of them on a `:free` suffix — GPT-OSS 20B and 120B, Gemma 4 26B/31B, DeepSeek V3.2 and V4.1 Flash, Qwen 3.6/3.8, MiniMax M2.7, GLM 4.6 through 5.1, Nemotron 3.5 Lightning and the Aion 3.0 pair. The Free plan needs no card and allows 200 free-model requests a day at 5 requests a minute, funded by ads on the dashboard; paying tiers switch the ads off and add weekly credit that refills every Sunday at 21:00 UTC.", 
     ["24 models with a :free suffix", "200 free-model requests/day, 5 per minute",
      "No card; $0.25 weekly credit on top", "OpenAI- and Anthropic-compatible endpoints"],
     ["gpt-oss-120b", "gpt-oss-20b", "gemma-4-31b",
      {"id": "deepseek-v3-2", "name": "DeepSeek V3.2", "family": "DeepSeek", "context_window": 40960,
       "rate_limits": "200 free-model requests/day on the Free plan"},
      "deepseek-v4-1-flash",
      {"id": "ministral-3-8b", "name": "Ministral 3 8B Instruct", "family": "Ministral", "context_window": 65536,
       "rate_limits": "200 free-model requests/day on the Free plan"},
      "mistral-small-3-2", "minimax-m2-7", "qwen3-8-27b", "glm-4-7-flash"],
     "Free requests are ad-supported and capped daily; heavy use belongs on a paid tier."),

    ("anyapi", "AnyAPI", "https://anyapi.ai", "af", "Free: 100K ANY tokens/day", "pp",
     "Aggregated upstreams, check per model", False,
     "400-model gateway whose free plan meters 100K ANY tokens a day with no card.",
     "AnyAPI puts 400+ models — OpenAI, Anthropic, Gemini, Grok, Qwen, DeepSeek, Mistral, Cohere — behind one OpenAI-compatible key. The Free plan costs $0 a month, needs no credit card and meters 100,000 ANY tokens per day against the models its catalogue marks free; paid plans start at $20 of usage-based credit. Which model IDs are free is only visible in the logged-in catalogue, so the rows here are the free models its directory names publicly.", 
     ["Free plan: 100K ANY tokens/day", "No credit card required", "400+ models behind one key",
      "Free model set is visible only after login"],
     ["qwen3-8-27b", "ling-3-1-flash"],
     "The ANY-token unit is not 1:1 with model tokens; the free model list rotates inside the dashboard."),
]
