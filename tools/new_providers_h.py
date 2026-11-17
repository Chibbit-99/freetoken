"""Providers found after the LEDGER_AUDIT pass, verified 2026-11-17 (part H).

xKiro surfaced from a direct report, cheapllm.shop from the awesome-free-ai-api
list. Both were read first-party: xkiro.com/models marks each zero-priced model
and the free-tier copy states the daily token cap, while cheapllm.shop/docs
publishes the permanent free-tier floor in its Limits section.
"""

# fmt: off
PART_H = [
    ("xkiro", "xKiro", "https://xkiro.com", "af", "Always-free tier", "pp",
     "Routed model catalog; each provider keeps its own policy", False,
     "Router reselling 69 models, 26 of them permanently free with a daily token cap.",
     "xKiro puts OpenAI, Anthropic, Google and open-model vendors behind one OpenAI- and Anthropic-compatible endpoint at api.xkiro.com/v1. Twenty-six catalogue entries are priced at zero rather than metered: the whole Cohere list, eight Mistral models including Large 3, Medium 3.5 and Codestral, SenseNova 6.8 Flash-Lite and one anonymous stealth model. Free keys need no card and cover 500,000 tokens a day, doubled to 1,000,000 once a Telegram account is linked. Paid routes are metered per token at list price.", 
     ["26 models priced at zero, no card", "500K tokens/day, 1M after Telegram verification",
      "OpenAI- and Anthropic-compatible endpoints", "69-model catalogue behind one key"],
     [{"id": "cohere/command-a-plus", "name": "Command A+", "family": "Cohere",
       "context_window": 446464, "rate_limits": "500K tokens/day on the free tier"},
      {"id": "cohere/command-a", "name": "Command A", "family": "Cohere",
       "context_window": 294912, "rate_limits": "500K tokens/day on the free tier"},
      {"id": "cohere/command-r-plus-08-2024", "name": "Command R+ (08-2024)", "family": "Cohere",
       "context_window": 131072, "rate_limits": "500K tokens/day on the free tier"},
      {"id": "cohere/aya-expanse-32b", "name": "Aya Expanse 32B", "family": "Aya",
       "context_window": 131072, "rate_limits": "500K tokens/day on the free tier"},
      {"id": "mistralai/mistral-large-2512", "name": "Mistral Large 3", "family": "Mistral",
       "context_window": 262144, "rate_limits": "500K tokens/day on the free tier"},
      {"id": "mistralai/mistral-medium-3.5", "name": "Mistral Medium 3.5", "family": "Mistral",
       "context_window": 262144, "rate_limits": "500K tokens/day on the free tier"},
      {"id": "mistralai/mistral-small-2603", "name": "Mistral Small 4", "family": "Mistral",
       "context_window": 262144, "rate_limits": "500K tokens/day on the free tier"},
      {"id": "mistralai/codestral-2508", "name": "Codestral 2508", "family": "Codestral",
       "context_window": 262144, "rate_limits": "500K tokens/day on the free tier"},
      {"id": "mistralai/ministral-8b", "name": "Ministral 3 8B", "family": "Ministral",
       "context_window": 262144, "rate_limits": "500K tokens/day on the free tier"},
      {"id": "sensenova/sensenova-6.8-flash-lite", "name": "SenseNova 6.8 Flash-Lite",
       "family": "SenseNova", "context_window": 268288,
       "rate_limits": "500K tokens/day on the free tier"}],
     "A router in front of upstream providers, so the free list can rotate; the daily cap is per account, not per model."),

    ("cheapllm-shop", "cheapllm.shop", "https://cheapllm.shop", "af", "Permanent free tier", "pp",
     "Beta service, no published retention policy", False,
     "Single-model API with a permanent hourly free allowance and no card.",
     "cheapllm.shop serves one model, DeepSeek V4.1 Flash 1017, through OpenAI, Anthropic Messages and Responses formats so existing SDKs work by changing the base URL. During its beta every account is unmetered; when the beta closes the vendor promises a permanent free tier of at least 5,000 input and 1,000 output tokens per hour per account with no card, with usage beyond that billed at $0.005 per million input tokens. One request runs at a time per account.", 
     ["Permanent free tier: at least 5K input + 1K output tokens/hour",
      "No card; key from the dashboard", "OpenAI, Anthropic and Responses formats",
      "One concurrent request per account"],
     [{"id": "deepseek-v4.1-flash-1017", "name": "DeepSeek V4.1 Flash 1017", "family": "DeepSeek",
       "context_window": 1048576,
       "rate_limits": "5K input + 1K output tokens/hour free; one request at a time"}],
     "Free tier is currently unmetered during beta; the published floor is 6K tokens/hour afterwards."),
]
