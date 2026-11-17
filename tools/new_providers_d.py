"""Providers found by diffing community indexes against the catalogue (part D).

Sources compared on 2026-11-17:
  - github.com/mnfst/awesome-free-llm-apis
  - github.com/jtig37/free-llm-api-resources
  - github.com/amardeeplakshkar/awesome-free-llm-apis
  - github.com/open-free-llm-api/awesome-freellm-apis
  - github.com/peter123023/awesome-free-llm-api
  - github.com/mvalentsev/awesome-free-ai-coding
  - freeinferencing.com

Everything else those lists carry was already in the catalogue or has retired.
"""

# fmt: off
PART_D = [
    ("amd-radeon-cloud", "AMD Radeon Cloud", "https://www.amd.com/en/developer.html", "rs",
     "Free public model API", "pp", "Two-day content retention, no training", False,
     "AMD's free public model API for development, evaluation and hackathons.",
     "AMD Radeon Cloud exposes a free model API for development, evaluation, demos, hackathons and open-source work: DeepSeek V4 Flash and V4.1 Flash, Qwen3.8 Flash/27B, GLM-5.3 Flash, MiMo-V2.6 Flash, MiniCPM5 and MinerU. Prompts and outputs roll off after two days and are never used for training, but content is logged in ordinary operation, and a rolling 24-hour spend ceiling (unpublished) gates heavy use.",
     ["Free route for development, evaluation and open-source work",
      "9 models including DeepSeek V4.1 Flash, Qwen3.8 and GLM-5.3 Flash",
      "30 RPM per key, 120 RPM per IP, 8 concurrent requests",
      "No card required; automatic API key on registration"],
     ["deepseek-v4-1-flash", "deepseek-v4-flash", "qwen3-8-flash", "qwen3-8-27b",
      "glm-5-3-flash", "mimo-v2-6-flash"],
     "A rolling 24-hour spend cap (value unpublished) limits heavy usage; prompts are kept for two days."),
    ("huggingface", "Hugging Face Inference Providers", "https://huggingface.co/docs/inference-providers", "mc",
     "Free monthly credits", "pp", "Provider-dependent routing", False,
     "One key that routes to many serverless inference providers, with free monthly credits.",
     "Hugging Face's Inference Providers unify dozens of serverless backends behind one router and one HF token, with an OpenAI-compatible endpoint. Free accounts get a small monthly credit (about $0.10, larger on PRO) that is shared across every provider the router can reach, so the practical allowance depends on which routes you pick.",
     ["Small free monthly credit on every HF account", "One token routes to dozens of providers",
      "OpenAI-compatible router endpoint", "No card required"],
     ["gpt-oss-120b", "qwen3-8-27b", "llama-3-3-70b", "deepseek-v4-1-flash"],
     "The free credit is tiny — good for testing a model, not for sustained use."),
    ("longcat", "LongCat API Platform", "https://longcat.chat", "tr",
     "Free trial credits", "pp", "Check provider policy", False,
     "Meituan's LongCat models with an OpenAI-compatible platform API.",
     "Meituan's LongCat family (including LongCat 2.0, a 1M-context MoE) is served through an OpenAI-compatible platform API. New accounts receive a trial credit on registration; after that the platform is pay-per-token.",
     ["Free trial credits on signup", "LongCat 2.0 with 1M context", "OpenAI-compatible API",
      "No card required to register"],
     [{"id": "longcat-2-0", "name": "LongCat 2.0", "family": "LongCat", "context_window": 1048576,
       "metrics": {"tps": 90}},
      {"id": "longcat-flash", "name": "LongCat Flash", "family": "LongCat", "context_window": 262144,
       "metrics": {"tps": 160}}],
     "Community-index sourcing — confirm the trial is still active before relying on it."),
]
# fmt: on
