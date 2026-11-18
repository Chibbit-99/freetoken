# Ledger audit — July 2026 research file, re-checked 2026-11-17

The supplied ledger claims a 500-platform target but contains **128 records**, numbered 1–137 with nine gaps (60, 91, 113, 117–119, 125–126, 131). Every record is listed below with the verdict reached on 2026-11-17 by checking the vendor's own page (or, where none exists, the only source the ledger cites).

Verdicts: **covered** = already in the catalogue · **added** = new this pass · **rejected** = checked and not free / not an API · **dead** = shut down · **proxy** / **out-of-scope** = not an inference supplier or not a text LLM.

| # | Ledger entry | Verdict | Detail |
| ---: | --- | --- | --- |
| 1 | Google Gemini API / AI Studio | covered | google-ai-studio |
| 2 | GroqCloud | covered | groq |
| 3 | Cerebras Inference | rejected | Free tier is card-gated and the recurring allowance ended — dropped in an earlier pass. |
| 4 | OpenRouter | covered | openrouter |
| 5 | GitHub Models | dead | GitHub Models was fully retired on 2026-07-30 (docs.github.com/github-models). |
| 6 | Cloudflare Workers AI | covered | cloudflare-workers-ai |
| 7 | Hugging Face Inference Providers | covered | huggingface |
| 8 | NVIDIA NIM API Catalog | covered | nvidia-nim |
| 9 | Cohere | covered | cohere |
| 10 | Mistral AI La Plateforme | covered | mistral-ai |
| 11 | Z.ai / Zhipu AI (BigModel) | covered | z-ai |
| 12 | Pollinations AI | covered | pollinations-ai |
| 13 | OVHcloud AI Endpoints | covered | ovhcloud-ai-endpoints |
| 14 | AI Horde | covered | ai-horde |
| 15 | Ollama Cloud | covered | ollama-cloud |
| 16 | Kilo Gateway / Kilo Code | covered | kilo-ai-gateway |
| 17 | NaraRouter (byNara / Naraya) | **added** | nara-router — /api/plans publishes a permanent Free plan: 7M tokens/day, 15 RPM. |
| 18 | Aion Labs | covered | aion-labs |
| 19 | Requesty | covered | requesty |
| 20 | NavyAI | **added** | navy-ai — Free plan: 150K tokens/day, 20 RPM, OpenAI-compatible at api.navy/v1. |
| 21 | Agnes AI | covered | agnes-ai |
| 22 | Reka | rejected | No free text tier: only Reka Vision video indexing (180 minutes), which is out of scope. |
| 23 | SiliconFlow | covered | siliconflow |
| 24 | Routeway | covered | routeway |
| 25 | BazaarLink | covered | bazaarlink |
| 26 | AINative Studio | rejected | No first-party free tier found on AINative's own material. |
| 27 | SEA-LION | covered | sea-lion |
| 28 | LLM7.io | covered | llm7-io |
| 29 | OpenCode Zen | covered | opencode-zen |
| 30 | AnyAPI | rejected | AnyAPI: no first-party page with a published free allowance. |
| 31 | UnoRouter | rejected | UnoRouter: no first-party page with a published free allowance. |
| 32 | Kluster AI | dead | kluster.ai sunset on 2026-06-09 after the MITO acquisition. |
| 33 | Vercel AI Gateway | covered | vercel-ai-gateway |
| 34 | RiftAI | rejected | RiftAI advertises a "free tier forever" but publishes no quota and no model ids that can be checked. |
| 35 | LyClaude Free API | rejected | LyClaude: API surface only, no published allowance. |
| 36 | ModelScope API Inference | covered | modelscope |
| 37 | Alibaba Cloud Model Studio / DashScope | covered | alibaba-model-studio |
| 38 | Chutes | rejected | Chutes is per-token only; the free tier ended in March 2026. |
| 39 | Glhf.chat | dead | glhf.chat: origin certificate broken, endpoint unusable. |
| 40 | Nscale Inference | **added** | nscale — $5 starter credit, no card, OpenAI-compatible serverless endpoint. |
| 41 | Nebius AI Studio | covered | nebius |
| 42 | SambaNova Cloud | covered | sambanova |
| 43 | xAI / Grok API | rejected | xAI: no free API tier. |
| 44 | DeepSeek API | rejected | DeepSeek: no free API tier, paid per token. |
| 45 | AI21 Studio | dead | AI21 Studio shut down its API. |
| 46 | Modal | covered | modal |
| 47 | Baseten | rejected | Baseten: deployment platform, no free inference allowance. |
| 48 | Replicate | covered | replicate |
| 49 | FastRouter.ai | covered | fastrouter |
| 50 | Cloudflare AI Gateway | proxy | Cloudflare AI Gateway is a proxy in front of other providers, not an inference supplier. |
| 51 | Portkey | proxy | Portkey is a gateway; inference comes from a connected provider. |
| 52 | Helicone | proxy | Helicone is observability/proxy only. |
| 53 | Novita AI | covered | novita-ai |
| 54 | Codestral API | covered | Mistral — Codestral is a Mistral endpoint, already represented by mistral-ai. |
| 55 | FrogAPI | rejected | FrogAPI: no reachable first-party site or docs. |
| 56 | Xiaomi MiMo API | **added** | xiaomi-mimo — ¥10 signup credit (~1M tokens) plus a creator programme. |
| 57 | ForgeCode | rejected | ForgeCode is a coding product, not an externally callable API. |
| 58 | Free LLM API Keys / PekPik gateway | rejected | PekPik relay: anonymous key giveaway, no verifiable operator or terms. |
| 59 | Plugsky | rejected | Plugsky: marketing page claims 100K tokens/day with no docs or console to confirm. |
| 61 | Lyceum | rejected | Lyceum is pay-per-use only; no free tier on its inference page. |
| 62 | AKI.IO | rejected | AKI.IO: €10 one-time credit, no first-party page located. |
| 63 | ARK Labs | rejected | ARK Labs: nothing beyond an infrabase listing; no docs or quota. |
| 64 | AiQu | rejected | AiQu: infrabase listing only, no published free allowance. |
| 65 | Beam | rejected | Beam/Cerebrium/Genesis/Lambda-style platforms sell GPU compute, not a free model route. |
| 66 | Berget AI | rejected | Berget AI is paid (EU-hosted open models); no free tier published. |
| 67 | Cerebrium | rejected | Cerebrium is a serverless compute platform, not a free LLM API. |
| 68 | CodingPlanX | rejected | CodingPlanX: no first-party documentation of a free allowance. |
| 69 | Cortecs AI | rejected | Cortecs AI: infrabase listing only. |
| 70 | EUrouter | rejected | EUrouter's "Free" plan still bills token cost with a 15% markup — requests are free, inference is not. |
| 71 | Genesis Cloud | rejected | Genesis Cloud: GPU credits, no hosted free LLM route. |
| 72 | Infercom | rejected | Infercom: infrabase listing only, no docs. |
| 73 | IonRouter | rejected | IonRouter: no current first-party evidence of a free tier. |
| 74 | Jina AI | out of scope | Jina AI's free allowance covers embeddings/rerankers, which this text-LLM catalogue excludes. |
| 75 | LLMWise | rejected | LLMWise's free tier is 20 credits — a demo, not an allowance. |
| 76 | Lambda | rejected | Lambda sells GPU hours; no free LLM endpoint. |
| 77 | Miapi | covered | miapi |
| 78 | Monster API | rejected | Monster API advertises a free tier but publishes no quota; nothing to record honestly. |
| 79 | GMI Cloud | **added** | gmi-cloud — two permanently free endpoints (Llama 3.3 70B Turbo, DeepSeek R1 Distill 70B). |
| 80 | DeepInfra | rejected | DeepInfra requires a card on file before the free allowance. |
| 81 | Baidu Qianfan / ERNIE | covered | baidu-qianfan |
| 82 | Ant Group Ling Studio | **added** | ant-ling — Ling Studio: 500K tokens/day on an OpenAI-compatible endpoint after Alipay binding. |
| 83 | Tencent Hunyuan / TokenHub | covered | tencent-hunyuan |
| 84 | Volcengine Ark (ByteDance) | **added** | volcengine-ark — 500K free tokens per model for 30 days, real-name verification required. |
| 85 | iFlytek Spark / Xinghuo | covered | iflytek-spark |
| 86 | Meituan LongCat | covered | longcat |
| 87 | Moonshot / Kimi Platform | rejected | Moonshot/Kimi is paid; the 3 RPM note is a rate limit, not a free allowance. |
| 88 | Infini-AI / 无问芯穹 | rejected | Infini-AI GenStudio explicitly grants no trial quota for API inference — embeddings/rerank only. |
| 89 | Baishan AI / 白山智算 | rejected | Baishan AI offers promotional credits (¥450) rather than a recurring tier. |
| 90 | PPIO | **added** | ppio — ¥5 starter credit (~5M DeepSeek tokens) on an OpenAI-compatible API. |
| 92 | China Mobile MoMA | rejected | China Mobile MoMA: new-user package only, no first-party free API documentation. |
| 93 | China Telecom Tianyi AI / TeleAI | rejected | TeleAI: entitlement unpublished outside the console. |
| 94 | China Unicom Yuanjing MaaS | rejected | China Unicom Yuanjing: no published free allowance. |
| 95 | NoneLinear / 非线智能 | rejected | NoneLinear: enterprise aggregator, no public free tier. |
| 96 | DMXAPI | rejected | DMXAPI: Chinese relay, no first-party free terms. |
| 97 | NetEase Youdao ThinkFlow | rejected | Youdao ThinkFlow: routing service, no published free allowance. |
| 98 | CatRouter | rejected | CatRouter: relay named only in a guide, no first-party docs. |
| 99 | Shiyun API / 诗云 API | rejected | Shiyun API: relay named only in a guide. |
| 100 | Lumi | rejected | Lumi: relay named only in a guide. |
| 101 | FreeModel.dev | rejected | FreeModel.dev: relay named only in a guide. |
| 102 | RightCode | rejected | RightCode: relay named only in a guide. |
| 103 | Upstage | covered | upstage |
| 104 | NLP Cloud | rejected | NLP Cloud: $15 one-time credit plus phone verification — a trial, not a tier. |
| 105 | Inference.net | rejected | Inference.net: $1 credit plus survey bonus — a trial. |
| 106 | Hyperbolic | covered | hyperbolic |
| 107 | Scaleway Generative APIs | covered | scaleway |
| 108 | AIMLAPI | rejected | AIMLAPI's free plan exists but its quota is unpublished and the catalogue is mostly paid. |
| 109 | Sakura AI Engine | **added** | sakura-ai-engine — 3,000 free Chat Completions requests/month, OpenAI- and Anthropic-compatible. |
| 110 | MLVoca Free LLM API | **added** | mlvoca — keyless Ollama-shaped endpoint serving TinyLlama and DeepSeek R1 1.5B. |
| 111 | PublicAI | covered | public-ai |
| 112 | api.airforce | covered | api-airforce |
| 114 | Eden AI | rejected | Eden AI is a gateway; inference runs on connected providers. |
| 115 | Sarvam AI | covered | sarvam-ai |
| 116 | SlashAI | **added** | slashai — one-hour 2M-token trial across its catalogue, no card. |
| 120 | Tav-AI | rejected | Tav-AI: a Disboard listing, no API page or terms. |
| 121 | LemonData | rejected | LemonData: a dev.to article, no product docs for the 50 requests/day claim. |
| 122 | Tera | rejected | Tera: API exists but no free allocation is published. |
| 123 | UncloseAI | rejected | UncloseAI: claimed "unlimited", but no first-party site to verify against. |
| 124 | routing.run | rejected | routing.run: the 400 requests/day Lite plan could not be confirmed on any current page. |
| 127 | Meta Llama API | rejected | Meta Llama API's free preview has ended; no public self-serve free tier. |
| 128 | StepFun / 阶跃星辰 | **added** | stepfun — ~¥10 credit (about 1M tokens) at 5 RPM plus 15-day Step Plan promotions. |
| 129 | Baichuan AI | **added** | baichuan — 5M free tokens at 5 RPM on signup. |
| 130 | 01.AI / Yi | rejected | 01.AI/Yi: ¥10 promotional credit, no recurring free tier. |
| 132 | ChatAnywhere | rejected | ChatAnywhere: Chinese relay, no verifiable operator or terms. |
| 133 | GemAI | rejected | GemAI: ¥100 promo credit from a directory listing, no first-party terms. |
| 134 | API520 | rejected | API520: ¥100 promo credit from a directory listing. |
| 135 | 算力云 / Suali Cloud | rejected | Suali Cloud: P2P relay claim with no API documentation. |
| 136 | InternAI / 书生 (InternLM/InternVL) | rejected | InternAI: no first-party free API terms outside Chinese blog posts. |
| 137 | ClawBrain | rejected | ClawBrain: directory listing only, no reachable service. |

## Tally

- covered: 44
- added: 13
- rejected: 63
- dead: 4
- proxy: 3
- out-of-scope: 1

Numbers absent from the file: 60, 91, 113, 117, 118, 119, 125, 126, 131 — the ledger skips them.
