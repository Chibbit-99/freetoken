"""Providers found on 2026-11-17 (part E).

Two hunting passes fed this file:

  - the provider pages of github.com/mvalentsev/awesome-free-ai-coding, whose
    rows are probe-verified twice a week and link their first-party evidence;
  - free-tier write-ups surfaced by searching YouTube coverage of "free LLM API"
    for the vendors the videos name, then checking each vendor's own docs.

Rows were kept only when the vendor's own page states the offer and the limits.
Infron was dropped: its ":free" routes need a retained $5 prepaid balance, so the
free tier does not exist without spending. TeamoRouter and X-Hero could not be
verified against a first-party page. Coding agents, OCR and speech routes were
ignored, and "provisional" rows were left for a later pass.

Vendor sources (read 2026-11-17):
  - https://www.merkium.nl
  - https://iteracompute.com/free/
  - https://miapi.uk
  - https://docs.sambanova.ai/docs/en/models/rate-limits
  - https://doc.freeinference.org/models
  - https://sea-lion.ai/try-sea-lion/
  - https://docs.opentyphoon.ai/en/rate-limits/
  - https://wiki.agnes-ai.com/en/docs/pricing
"""

# fmt: off
PART_E = [
    ("merkium", "Merkium", "https://www.merkium.nl", "af", "Permanently free models", "pv",
     "Never used for training", False,
     "Dutch model lab serving its own Ceres, Ganymede and Pluto models free of charge.",
     "Merkium is an independent Dutch model developer whose current API models carry no per-token or per-request charge: Ceres 1.0, Ganymede 1.1 and the Pluto 1.2 family, served through an OpenAI-compatible endpoint. The catalogue calls the models \"free to use through the API, permanently\" with no card or billing account, at 30 requests/minute per key, and states that conversations are never used to train, fine-tune or evaluate Merkium models.",
     ["Current models are permanently free", "30 requests/minute per key", "No card or billing account",
      "Prompts are never used for training"],
     [{"id": "ceres_1_0", "name": "Ceres 1.0", "family": "Ceres", "context_window": 131072},
      {"id": "ceres_1_0_pro", "name": "Ceres 1.0 Pro", "family": "Ceres", "context_window": 131072},
      {"id": "ganymede_1_1", "name": "Ganymede 1.1", "family": "Ganymede", "context_window": 131072},
      {"id": "pluto_1_2_flash", "name": "Pluto 1.2 Flash", "family": "Pluto", "context_window": 131072},
      {"id": "pluto_1_2_pro", "name": "Pluto 1.2 Pro", "family": "Pluto", "context_window": 131072}],
     "Small independent lab: space requests at least two seconds apart and honour Retry-After."),

    ("iteracompute", "IteraCompute", "https://iteracompute.com/free/", "tr", "30M free tokens/month", "pv",
     "No training without consent", False,
     "Open-model host with a large monthly free token allowance and an Auto router.",
     "IteraCompute serves self-hosted open models through an OpenAI-compatible API and gives every verified account 30,000,000 free tokens per month, shared across qwen/qwen3.8-27b and the Auto routing pool. There is no card, RPM or daily cap — but only one request at a time on the free slot, an 8,192-token output ceiling and no rollover. Prompts are not used to train foundation models without explicit authorisation; the no-recharge promotion currently runs to 2026-11-24.",
     ["30,000,000 free tokens per month, reset on the 1st", "No card and no recharge required",
      "One concurrent free request, 8,192 output tokens", "Prompts are not used for training without consent"],
     ["qwen3-8-27b",
      {"id": "itera-automatic", "name": "Itera Auto", "family": "Itera", "context_window": 131072,
       "rate_limits": "Router picks the model; shares the monthly allowance"}],
     "Free window currently ends 2026-11-24; optional $10/$50 top-ups raise the allowance."),

    ("miapi", "MIAPI", "https://miapi.uk", "af", "100 free queries/month", "pp",
     "Usage logs kept up to 90 days", False,
     "Grounded-answer API that returns citations, with a monthly free query allowance.",
     "MIAPI answers questions with web grounding and inline citations through a single `miapi-grounded` model. The Free plan covers every endpoint with 100 queries per month per account and 60 requests/minute; questions are capped at 2,000 characters and answers at 50–2,000 output tokens. Usage logs are retained for up to 90 days, and no card is required.",
     ["100 free queries per month", "60 requests/minute", "Answers include citations",
      "No card required"],
     [{"id": "miapi-grounded", "name": "MIAPI Grounded", "family": "MIAPI",
       "rate_limits": "100 queries/month; 60 RPM; max 2,000 output tokens"}],
     "Grounded search answers only — not a general chat endpoint."),

    ("sambanova", "SambaNova Cloud", "https://cloud.sambanova.ai", "af", "Forever-free tier", "pv",
     "Not used for training", False,
     "Open models on SambaNova's own RDU silicon, with a card-free rate-limited tier.",
     "SambaNova Cloud runs open weights on SambaNova's RDU chips behind an OpenAI-compatible API. The Free tier applies whenever no payment method is linked: every model gets 20 requests/minute, 20 requests/day and 200,000 tokens/day of its own, and no card is needed. Production models are DeepSeek V3.1, Llama 3.3 70B and gpt-oss-120b; DeepSeek V3.2 and Gemma 4 31B are evaluation-only previews. Linking a card moves the account to the metered Developer tier instead.",
     ["20 requests/minute, 20 requests/day per model", "200,000 tokens/day per model",
      "No card required for the Free tier", "Production and preview models both included"],
     [{"id": "deepseek-v3-1", "name": "DeepSeek V3.1", "family": "DeepSeek V3", "context_window": 131072},
      "llama-3-3-70b", "gpt-oss-120b",
      {"id": "deepseek-v3-2", "name": "DeepSeek V3.2", "family": "DeepSeek V3", "context_window": 131072},
      "gemma-4-31b"],
     "The binding limit is 20 requests/day per model; preview models can be withdrawn at short notice."),

    ("freeinference", "FreeInference (Harvard SEAS)", "https://freeinference.org", "rs",
     "Free research endpoint", "nn", "Prompts logged for research", False,
     "Harvard SEAS's MadSys Lab serving frontier open models free to every account.",
     "FreeInference is run by the MadSys Lab at Harvard SEAS as an experimental research service: every registered account gets free access to frontier open models behind both OpenAI-shaped (`/v1`) and Anthropic-shaped (`/anthropic`) endpoints, with a documented Claude Code setup. Only models marked Free accept a Free key. Capacity-dependent limits are not published, and prompts and responses may be logged and sanitised excerpts published for research.",
     ["Free keys reach models marked Free", "OpenAI- and Anthropic-shaped endpoints",
      "No card required", "Claude Code setup documented"],
     ["glm-5-3-flash", "minimax-m3", "deepseek-v4-flash",
      {"id": "qwen3-6-35b", "name": "Qwen3.6 35B", "family": "Qwen 3.6", "context_window": 262144}],
     "Research service: allowances vary with capacity and prompts may be published in sanitised form."),

    ("sea-lion", "SEA-LION (AI Singapore)", "https://sea-lion.ai", "af", "Free prototype API", "pp",
     "Check provider policy", False,
     "AI Singapore's own Southeast Asian language models behind a free API.",
     "SEA-LION is AI Singapore's open model family for Southeast Asian languages, served first-party through an OpenAI-compatible API. The free trial key is explicitly meant for prototyping and testing, capped at 10 calls per minute per account, with no published token budget or expiry; production use is directed to AI Singapore's cloud partners. Keys come from the playground key manager after signup, and the model list needs a key to read.",
     ["Free trial key for prototyping", "10 calls/minute per account",
      "OpenAI-compatible endpoint", "No card required"],
     [{"id": "aisingapore/Llama-SEA-LION-v3.5-70B-R", "name": "Llama SEA-LION v3.5 70B",
       "family": "SEA-LION", "context_window": 131072},
      {"id": "aisingapore/Qwen-SEA-LION-v4.5-27B-IT", "name": "Qwen SEA-LION v4.5 27B",
       "family": "SEA-LION", "context_window": 131072}],
     "Prototyping only per AI Singapore's terms; no published token budget."),

    ("opentyphoon", "OpenTyphoon", "https://opentyphoon.ai", "rs", "Free research showcase", "nn",
     "Usage data used to improve the model", False,
     "SCB 10X's Thai-tuned open models, free as a research showcase.",
     "OpenTyphoon is the Thai-tuned open-model family from SCB 10X, the venture arm of Siam Commercial Bank. Its FAQ calls the API a research showcase that is free to use: typhoon-v2.5-30b-a3b-instruct (a Thai fine-tune of Qwen3-30B-A3B) allows 5 requests/second and 200 requests/minute per account per model, and higher limits are available by email. Usage data is collected to improve the model and API, and production traffic is directed to Together AI.",
     ["Free to use as a research showcase", "5 requests/second, 200 requests/minute",
      "Thai-tuned 30B model with 128K context", "No card required"],
     [{"id": "typhoon-v2.5-30b-a3b-instruct", "name": "Typhoon v2.5 30B A3B",
       "family": "Typhoon", "context_window": 131072,
       "rate_limits": "5 requests/second; 200 requests/minute per account per model"}],
     "Trains on what you send; Thai-language focus. OCR and speech routes are excluded from this catalogue."),

    ("agnes-ai", "Agnes AI", "https://agnes-ai.com", "fm", "Free Flash models (promo)", "pp",
     "Opt out of training available", False,
     "Agnes AI's own Flash models, currently priced at zero, behind a standard API.",
     "Agnes AI serves its own models through an OpenAI-compatible endpoint at apihub.agnes-ai.com, and the two Flash text models — agnes-2.5-flash and agnes-3.0-flash — have input, cached-input and output all currently priced at zero. Pro models stay metered and the zero pricing is promotional, ending on a date the platform announces. Per-minute request allowances for the default user class are dynamic, so limit values only appear in the console; image generation is billable on separate rates.",
     ["agnes-2.5-flash and agnes-3.0-flash at zero price", "OpenAI-compatible endpoint",
      "Prompt opt-out available", "No card required"],
     [{"id": "agnes-2.5-flash", "name": "Agnes 2.5 Flash", "family": "Agnes", "context_window": 262144},
      {"id": "agnes-3.0-flash", "name": "Agnes 3.0 Flash", "family": "Agnes", "context_window": 262144}],
     "Zero pricing is promotional and can end without notice; the China station bills in CNY."),
]
# fmt: on
