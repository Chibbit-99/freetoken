"""Canonical model catalogue for the FreeToken data files.

One entry per model, shared by every provider that serves it, so a model's
name, family, context window and scores can never drift between providers.

`intelligence` is the Artificial Analysis Intelligence Index (v5.0.1, read from
https://artificialanalysis.ai/leaderboards/models on 2026-11-17). Models that
Artificial Analysis has not scored get `intelligence=None`, which drops the
field from the JSON instead of inventing a number.

`tps` is a curated throughput estimate in tokens/second for ranking only.
"""

MODELS = {}


def C(mid, name, family, ctx=None, aa=None, tps=None):
    MODELS[mid] = {
        "id": mid,
        "name": name,
        "family": family,
        "context_window": ctx,
        "intelligence": aa,
        "tps": tps,
    }


# ---------------------------------------------------------------- Google
C("gemini-4-carbon", "Gemini 4 Carbon", "Gemini 4", 1048576, 60, 180)
C("gemini-4-hydrogen", "Gemini 4 Hydrogen", "Gemini 4", 1048576, 54, 260)
C("gemini-4-argon", "Gemini 4 Argon", "Gemini 4", 1048576, 50, 200)
C("gemini-3-5-flash", "Gemini 3.5 Flash", "Gemini 3.5", 1048576, None, 300)
C("gemini-3-5-flash-lite", "Gemini 3.5 Flash-Lite", "Gemini 3.5", 1048576, 12, 420)
C("gemini-3-1-pro", "Gemini 3.1 Pro", "Gemini 3", 1048576, None, 120)
C("gemma-4-31b", "Gemma 4 31B", "Gemma 4", 262144, 4, 130)
C("gemma-4-26b-a4b", "Gemma 4 26B A4B", "Gemma 4", 262144, None, 240)
C("gemma-4-12b", "Gemma 4 12B", "Gemma 4", 262144, None, 260)
C("gemma-4-e4b", "Gemma 4 E4B", "Gemma 4", 131072, 5, 320)
C("gemma-3-27b", "Gemma 3 27B", "Gemma 3", 131072, None, 120)
C("gemma-3-12b", "Gemma 3 12B", "Gemma 3", 131072, None, 180)
C("gemma-3-4b", "Gemma 3 4B", "Gemma 3", 131072, None, 260)

# ---------------------------------------------------------------- Alibaba
C("qwen4-max", "Qwen4 Max", "Qwen 4", 1000000, 43, 90)
C("qwen3-8-max", "Qwen3.8 Max", "Qwen 3.8", 262144, None, 90)
C("qwen3-8-plus", "Qwen3.8 Plus", "Qwen 3.8", 262144, None, 140)
C("qwen3-8-flash", "Qwen3.8 Flash", "Qwen 3.8", 262144, 29, 220)
C("qwen3-8-27b", "Qwen3.8 27B", "Qwen 3.8", 262144, 20, 170)
C("qwen3-5-397b-a17b", "Qwen3.5 397B A17B", "Qwen 3.5", 262144, None, 80)
C("qwen3-5-122b-a10b", "Qwen3.5 122B A10B", "Qwen 3.5", 262144, None, 110)
C("qwen3-5-35b-a3b", "Qwen3.5 35B A3B", "Qwen 3.5", 262144, None, 230)
C("qwen3-5-9b", "Qwen3.5 9B", "Qwen 3.5", 262144, None, 200)
C("qwen3-5-4b", "Qwen3.5 4B", "Qwen 3.5", 262144, None, 250)
C("qwen3-next-80b", "Qwen3 Next 80B A3B", "Qwen 3", 262144, None, 160)
C("qwen3-32b", "Qwen3 32B", "Qwen 3", 131072, None, 120)
C("qwen3-8b", "Qwen3 8B", "Qwen 3", 131072, None, 200)
C("qwen3-4b", "Qwen3 4B", "Qwen 3", 131072, None, 240)

# ---------------------------------------------------------------- DeepSeek
C("deepseek-v4-1-flash", "DeepSeek V4.1 Flash", "DeepSeek V4", 1048576, 33, 100)
C("deepseek-v4-pro", "DeepSeek V4 Pro", "DeepSeek V4", 1048576, 23, 70)
C("deepseek-v4-flash", "DeepSeek V4 Flash", "DeepSeek V4", 262144, None, 95)
C("deepseek-r1-0528", "DeepSeek R1 0528", "DeepSeek R1", 131072, None, 45)

# ---------------------------------------------------------------- Z.AI / GLM
C("glm-5-3", "GLM-5.3", "GLM 5.3", 1048576, 32, 180)
C("glm-5-3-flash", "GLM-5.3 Flash", "GLM 5.3", 1048576, 28, 220)
C("glm-5-2", "GLM-5.2", "GLM 5.2", 1048576, None, 170)
C("glm-4-7-flash", "GLM-4.7 Flash", "GLM 4.7", 200000, None, 200)
C("glm-4-6", "GLM-4.6", "GLM 4.6", 200000, None, 130)

# ---------------------------------------------------------------- Moonshot
C("kimi-k3-1-pro", "Kimi K3.1 Pro", "Kimi", 1048576, 46, 80)
C("kimi-k3", "Kimi K3", "Kimi", 262144, None, 90)
C("kimi-linear-48b", "Kimi Linear 48B A3B", "Kimi", 1048576, None, 220)

# ---------------------------------------------------------------- MiniMax / Xiaomi
C("minimax-m3-1-flash", "MiniMax M3.1 Flash", "MiniMax", 1048576, 29, 150)
C("minimax-m3", "MiniMax M3", "MiniMax", 1048576, 19, 80)
C("minimax-m2-7", "MiniMax M2.7", "MiniMax", 262144, None, 90)
C("mimo-v2-6-pro", "MiMo V2.6 Pro", "MiMo", 1048576, 30, 90)
C("mimo-v2-6-flash", "MiMo V2.6 Flash", "MiMo", 1048576, 27, 160)

# ---------------------------------------------------------------- Meta
C("llama-4-maverick", "Llama 4 Maverick", "Llama 4", 1048576, None, 130)
C("llama-4-scout", "Llama 4 Scout", "Llama 4", 10000000, None, 150)
C("llama-3-3-70b", "Llama 3.3 70B", "Llama 3", 131072, None, 80)
C("llama-3-1-405b", "Llama 3.1 405B", "Llama 3", 131072, None, 40)
C("llama-3-1-8b", "Llama 3.1 8B", "Llama 3", 131072, None, 220)
C("muse-glimmer", "Muse Glimmer 30B", "Muse", 131072, 6, 160)
C("muse-spark-open", "Muse Spark Open", "Muse", 1048576, 25, 170)

# ---------------------------------------------------------------- Mistral
C("mistral-large-4", "Mistral Large 4", "Mistral", 1048576, 26, 90)
C("mistral-medium-3-5", "Mistral Medium 3.5", "Mistral", 262144, 5, 110)
C("mistral-small-4", "Mistral Small 4", "Mistral", 262144, 4, 180)
C("mistral-small-3-2", "Mistral Small 3.2 24B", "Mistral", 131072, None, 120)
C("mistral-nemo", "Mistral Nemo 12B", "Mistral", 131072, None, 110)
C("magistral-medium", "Magistral Medium", "Magistral", 131072, None, 90)
C("codestral", "Codestral", "Codestral", 262144, None, 160)

# ---------------------------------------------------------------- NVIDIA
C("nemotron-3-ultra-550b", "Nemotron 3 Ultra 550B A55B", "Nemotron", 262144, 12, 110)
C("nemotron-3-5-super-vl", "Nemotron 3.5 Super VL", "Nemotron", 1048576, 14, 150)
C("nemotron-3-5-lightning", "Nemotron 3.5 Lightning", "Nemotron", 1048576, 6, 400)
C("nemotron-3-nano-30b", "Nemotron 3 Nano 30B A3B", "Nemotron", 1048576, None, 300)
C("nemotron-nano-9b-v2", "Nemotron Nano 9B V2", "Nemotron", 131072, None, 380)

# ---------------------------------------------------------------- OpenAI open weights
C("gpt-oss-120b", "GPT-OSS 120B", "GPT-OSS", 131072, 4, 520)
C("gpt-oss-20b", "GPT-OSS 20B", "GPT-OSS", 131072, None, 780)
C("gpt-oss-safeguard-20b", "GPT-OSS Safeguard 20B", "GPT-OSS", 131072, None, 700)

# ---------------------------------------------------------------- Cohere / IBM / Upstage
C("command-a-plus", "Command A+", "Command", 192000, 6, 90)
C("command-a", "Command A", "Command", 256000, None, 85)
C("command-r-plus", "Command R+", "Command", 128000, None, 60)
C("north-mini-code", "North Mini Code", "North", 256000, 3, 200)
C("granite-4-2-8b", "Granite 4.2 8B", "Granite", 131072, 5, 200)
C("granite-4-2-30b", "Granite 4.2 30B", "Granite", 131072, None, 110)
C("solar-pro-4", "Solar Pro 4", "Solar", 524288, 14, 110)
C("solar-mini-4", "Solar Mini 4", "Solar", 524288, None, 200)

# ---------------------------------------------------------------- Reflection / Arcee / Ling / Step / etc.
C("beam-1-0", "Beam 1.0", "Reflection Beam", 1048576, 18, 60)
C("ling-3-1-flash", "Ling 3.1 Flash", "Ling", 1048576, 30, 220)
C("ling-3-0-flash-vl", "Ling 3.0 Flash VL", "Ling", 262144, None, 180)
C("step-5-preview", "Step 5 Preview", "Step", 1048576, 29, 90)
C("agnes-2-5-pro-theta", "Agnes 2.5 Pro Theta", "Agnes", 1048576, 24, 120)
C("inkling-2-small", "Inkling 2 Small", "Inkling", 1048576, 31, 150)
C("sarvam-105b", "Sarvam 105B", "Sarvam", 131072, None, 80)
C("sea-lion-27b", "SEA-LION 27B", "SEA-LION", 131072, None, 150)
C("sea-lion-guard", "SEA-LION Guard", "SEA-LION", 131072, None, 150)
C("apertus-70b", "Apertus 70B", "Apertus", 131072, None, 70)
C("olmo-3-1-32b", "OLMo 3.1 32B Think", "OLMo", 66000, None, 90)
C("phi-4-multimodal", "Phi-4 Multimodal", "Phi", 131072, None, 140)
C("hermes-4-70b", "Hermes 4 70B", "Hermes", 131072, None, 70)
C("mercury-2", "Mercury 2", "Mercury", 131072, None, 950)
C("mercury-2-5", "Mercury 2.5", "Mercury", 131072, None, 1050)
C("mercury-3", "Mercury 3", "Mercury", 131072, None, 1100)
C("k-exaone-2-0", "K-EXAONE 2.0", "EXAONE", 262144, 8, 90)
C("nanbeige-4-3-33b", "Nanbeige4.3 33B", "Nanbeige", 524288, 20, 100)
C("k2-horizon-375b", "K2 Horizon 375B A23B", "K2", 524288, 18, 120)
C("jt-4-1-flash", "JT-4.1 Flash 236B A21B", "JT", 262144, 19, 130)
C("tencent-hy4", "Tencent Hy4", "Hunyuan", 1048576, 35, 110)

# ---------------------------------------------------------------- Speech / embeddings / utility
C("whisper-large-v3", "Whisper Large v3", "Whisper", None, None, None)
C("whisper-large-v3-turbo", "Whisper Large v3 Turbo", "Whisper", None, None, None)
C("bge-m3", "BGE-M3 Embeddings", "BGE", 8192, None, None)
C("jina-embeddings-v5", "Jina Embeddings v5 Text Small", "Jina Embeddings", 8192, None, None)
C("jina-reranker-v3", "Jina Reranker v3", "Jina Reranker", 131072, None, None)
C("voyage-4-large", "Voyage 4 Large", "Voyage", 32768, None, None)
C("voyage-4-lite", "Voyage 4 Lite", "Voyage", 32768, None, None)
C("voyage-rerank-3", "Voyage Rerank 3", "Voyage Reranker", 32768, None, None)
C("qdrant-bm25", "Qdrant BM25 (sparse)", "Qdrant Embeddings", None, None, None)
C("qdrant-multilingual-e5", "Qdrant Multilingual E5 (dense)", "Qdrant Embeddings", 512, None, None)

# ---------------------------------------------------------------- Sber / Liquid / NLP Cloud
C("gigachat-2-lite", "GigaChat 2 Lite", "GigaChat", 32768, None, 90)
C("gigachat-2-pro", "GigaChat 2 Pro", "GigaChat", 131072, None, 65)
C("gigachat-2-max", "GigaChat 2 Max", "GigaChat", 131072, None, 45)
C("gigachat-3-ultra", "GigaChat 3 Ultra", "GigaChat", 131072, None, 38)
C("lfm3-1-7b", "LFM3 1.7B", "LFM3", 32768, None, 210)
C("lfm2-5-24b-a2b", "LFM2.5 24B A2B", "LFM2.5", 32768, None, 140)
C("d1-2", "Liquid d1.2", "Liquid d1", 131072, None, 150)
C("chatdolphin", "ChatDolphin", "Dolphin", 8192, None, 55)
C("yi-34b", "Yi 34B", "Yi", 4096, None, 40)
C("mixtral-8x7b", "Mixtral 8x7B", "Mixtral", 32768, None, 60)
