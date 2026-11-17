"""Per-provider serving speed.

Throughput is a property of the *host*, not of the model: the same GPT-OSS 20B
runs at ~780 tok/s on Groq's LPUs, several hundred tok/s on a dedicated GPU
endpoint and far slower on a shared free queue. tools/models.py therefore holds a
baseline `tps` for each model (reference-class serving speed), and every provider
scales it with `SPEED_FACTOR`. Explicit `MODEL_OVERRIDES` win where a provider's
own numbers are known.

These remain curated estimates for ranking; no provider publishes comparable
figures for its free tier.
"""

# Multiplier applied to the model's baseline throughput on this provider.
SPEED_FACTOR = {
    # dedicated, latency-optimised hardware
    "groq": 1.00,
    "inception": 1.00,  # diffusion decoding: ~1,000 tok/s is the published figure
    "fireworks-ai": 0.95,
    "friendli-ai": 0.95,
    "hyperbolic": 0.90,
    "vertex-ai-express": 0.90,
    "google-ai-studio": 0.90,
    "aion-labs": 0.85,
    "agnes-ai": 0.85,
    "zhipu-bigmodel": 0.85,
    "z-ai": 0.85,
    "alibaba-model-studio": 0.85,
    "nous-portal": 0.80,
    "ollama-cloud": 0.80,
    "vercel-ai-gateway": 0.80,
    "token-harbor": 0.80,
    "novita-ai": 0.78,
    "sensenova": 0.75,
    "iflytek-spark": 0.75,
    "siliconflow": 0.75,
    "zro": 0.75,
    "upstage": 0.75,
    "llmtr": 0.75,
    "sarvam-ai": 0.75,
    "scaleway": 0.72,
    "inferbase": 0.72,
    "freeinference": 0.72,
    "orcarouter": 0.72,
    "requesty": 0.72,
    "deepseek-hosted": 0.72,
    # shared / routed capacity
    "openrouter": 0.68,
    "kilo-ai-gateway": 0.68,
    "routeway": 0.68,
    "bazaarlink": 0.65,
    "llm-kiwi": 0.65,
    "ibm-watsonx": 0.60,
    "mistral-ai": 0.60,
    "cohere": 0.60,
    "nvidia-nim": 0.60,
    "ovhcloud-ai-endpoints": 0.58,
    "regolo-ai": 0.58,
    "hetzner-inference": 0.58,
    "arli-ai": 0.58,
    "modelscope": 0.55,
    "mixlayer": 0.55,
    "vlm-run": 0.55,
    "llm7-io": 0.52,
    "meganova": 0.50,
    "novai": 0.50,
    "cloudflare-workers-ai": 0.45,
    "kiosapi": 0.40,
    "pollinations-ai": 0.40,
    "ai-horde": 0.20,
}

# Exact provider-specific figures where the host's behaviour is known.
MODEL_OVERRIDES = {
    "groq": {"gpt-oss-120b": 520, "gpt-oss-20b": 780, "llama-4-scout": 580},
    "nvidia-nim": {"nemotron-3-ultra-550b": 55, "nemotron-3-5-lightning": 520},
    "cloudflare-workers-ai": {"llama-3-1-8b": 120, "gpt-oss-20b": 240},
    "ai-horde": {"gemma-4-e4b": 25, "qwen3-4b": 40, "llama-3-1-8b": 60},
    "openrouter": {"gemma-4-31b": 95, "gpt-oss-20b": 480},
}

DEFAULT_FACTOR = 0.55


def tps_for(provider_id, model_id, base):
    """Provider-specific throughput for a model, or None when unknown."""
    if base is None:
        return None
    override = MODEL_OVERRIDES.get(provider_id, {}).get(model_id)
    if override is not None:
        return override
    factor = SPEED_FACTOR.get(provider_id, DEFAULT_FACTOR)
    value = base * factor
    return int(round(value / 5.0) * 5)
