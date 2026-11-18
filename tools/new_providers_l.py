"""Sibling domains of the Clean APIs product, added as their own providers (part L).

They share a dashboard and a 33-model catalogue, but each needs its own signup
and each grants its own 0.5M-token monthly allowance, so they are separate
entries in the catalogue rather than one card with three domains in the notes.
"""

# fmt: off
PART_L = [
    ("radoxai", "Radox AI", "https://radoxai.com", "mc", "0.5M free tokens/month", "pp",
     "Routed upstreams, check per model", False,
     "33 models with a 0.5M-token monthly free allowance and no card.",
     "Radox AI runs the same catalogue as Clean APIs on its own domain: Claude Fable 5, GPT-5.6 Luna, DeepSeek V4 Flash and Pro, Qwen3.8 27B, Seed 2.1 Turbo and 27 more behind one OpenAI-compatible endpoint at radoxai.com/v1. A separate account grants its own 500,000 free tokens a month with no card, and the free plan reaches every model, so the allowance can go on a frontier model. Paid plans start at $4.50 for 100M tokens, with balance-based overage at list rates.",
     ["500K free tokens every month, per account", "No card; all 33 models on the free plan",
      "OpenAI-compatible with streaming, tools and vision", "Overage bills at list rates, HTTP 402 when empty"],
     [{"id": "deepseek-v4-flash-0731", "name": "DeepSeek V4 Flash 0731", "family": "DeepSeek", "context_window": 1048576},
      {"id": "deepseek-v4-pro-0813", "name": "DeepSeek V4 Pro 0813", "family": "DeepSeek", "context_window": 1048576},
      {"id": "gpt-5.6-luna", "name": "GPT-5.6 Luna", "family": "GPT-5.6", "context_window": 1050624},
      {"id": "qwen3.8-27b", "name": "Qwen3.8 27B", "family": "Qwen 3.8", "context_window": 262144},
      {"id": "seed-2.1-turbo", "name": "Seed 2.1 Turbo", "family": "Seed", "context_window": 262144},
      {"id": "gemma-2-2b", "name": "Gemma 2 2B", "family": "Gemma 2", "context_window": 8192}],
     "Same catalogue and dashboard as cleanapis.com and oxionai.com, but a separate account and a separate monthly allowance. Pricing differs slightly: 100M tokens is $4.50 here, $3.50 on Clean APIs."),

    ("oxionai", "Oxion AI", "https://oxionai.com", "mc", "0.5M free tokens/month", "pp",
     "Routed upstreams, check per model", False,
     "33 models with a 0.5M-token monthly free allowance and no card.",
     "Oxion AI serves the same 33-model catalogue as its sibling domains through an OpenAI-compatible endpoint at oxionai.com/v1 — Claude, GPT, Gemini, Kimi, DeepSeek, Qwen, GLM and Seed among them. Signing up here means a third independent 500,000-token monthly free allowance with no card, and every model in the catalogue is reachable on the free plan. Paid plans start at $3.50 for 50M tokens, with overage billed against the balance at each model's list rate.",
     ["500K free tokens every month, per account", "No card; all 33 models on the free plan",
      "OpenAI-compatible with streaming, tools and vision", "Overage bills at list rates, HTTP 402 when empty"],
     [{"id": "deepseek-v4-flash-0731", "name": "DeepSeek V4 Flash 0731", "family": "DeepSeek", "context_window": 1048576},
      {"id": "deepseek-v4-pro-0813", "name": "DeepSeek V4 Pro 0813", "family": "DeepSeek", "context_window": 1048576},
      {"id": "gpt-5.6-luna", "name": "GPT-5.6 Luna", "family": "GPT-5.6", "context_window": 1050624},
      {"id": "qwen3.8-27b", "name": "Qwen3.8 27B", "family": "Qwen 3.8", "context_window": 262144},
      {"id": "seed-2.1-turbo", "name": "Seed 2.1 Turbo", "family": "Seed", "context_window": 262144},
      {"id": "gemma-2-2b", "name": "Gemma 2 2B", "family": "Gemma 2", "context_window": 8192}],
     "Same catalogue and dashboard as cleanapis.com and radoxai.com, but a separate account and a separate monthly allowance."),
]
