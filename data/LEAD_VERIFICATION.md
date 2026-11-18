# Lead verification — iteration 12 (2026-11-17)

Nineteen leads raised this pass. Sources were shifted away from English
"free LLM API" round-ups: Chinese, Russian, Japanese, Korean, Portuguese and
German queries, plus three directories (`free-llm.com`, `freellm.net`,
`awesome-free-llm-apis`) whose changelogs name providers nobody writes listicles
about. Every verdict below was taken from the provider's own page.

| Lead | Verdict | Provider id | Evidence |
| --- | --- | --- | --- |
| AxForge (axforge.ai) | added | axforge | Pricing page: "Every new account includes 3M free serverless tokens every 30 days. No card required." Renews, so not trial credit. |
| GigaChat (Sber) | added | gigachat | Product page states 365,000,000 tokens "with annual renewal" for individuals; split 250M Lite / 50M Ultra / 40M Pro / 25M Max. Divides to ~1M/day, so mid-table rather than the largest allowance. |
| DeepSeek | added | deepseek | 5M tokens on signup, no card until the grant is spent; grant is console-side, not on the pricing page. |
| GonkaRouter | added | gonkarouter | Homepage: "1M free tokens to start", email or Google sign-in, no card. Separate product from Gonka Broker. |
| Vectoree | added | vectoree | Pricing: "$5 welcome credit after CLI login + link", card only needed to top up afterwards. |
| NLP Cloud | added | nlp-cloud | Pricing table: Free plan $0, "Automatically get a $15 FREE credit", 2 parallel requests. |
| Liquid AI | added | liquid-ai | Pricing: "Every new organization starts with $2 in free credit". |
| Qiniu AI (七牛云) | added | qiniu | 3M free tokens on signup across 70+ models, OpenAI + Anthropic shapes, 5 rpm / 60 rph for individuals. |
| BlockRun | added | blockrun | Model list filtered to Free: nine open-weight models at Free/Free with no payment header — keyless. |
| ACLIDE | dead | — | Homepage banner: "The ACLIDE project has ended. Sign-ups and purchases are closed." |
| BlazeAPI | rejected | — | Docs table lists Free at 0 daily tokens; plans are crypto-only. The 200K/day figure comes from a third-party audit, not the vendor. |
| Chutes | rejected | — | Pricing is pay-as-you-go per token with no free allowance. |
| glhf.chat | dead | — | Cloudflare 526 invalid SSL certificate on the origin. |
| Berget AI | rejected | — | €5 trial credit, but the FAQ says "a card is required at signup to prevent abuse". |
| Infomaniak | rejected | — | 1M trial credits, card required. |
| MiniMax | rejected | — | No free tier on the pricing page; the ¥15 figure is third-party only. |
| Moonshot / Kimi | rejected | — | Official docs: no trial credits, $1 minimum top-up to unlock Kimi K3. |
| xAI Grok | rejected | — | $150/month needs $5 of prior spend, is region-gated and is no longer documented; $25 promo expires in 30 days. |
| Krutrim | rejected | — | Cloud platform with no published LLM free allowance; "free credits" claims are aggregator copy. |

**Tally:** added 9 · rejected 8 · dead 2. Two further leads were checked and
deliberately left out of the table: `free-llm.com` and `freellm.net` are
directories rather than providers, and `Voyage AI` / `Jina AI` sell embeddings
and rerankers, which the scope rule excludes.

Standing rule applied: a provider whose free path needs a card first (Berget,
Infomaniak, xAI) is not catalogued, even when the credit is real.

# Lead verification — iteration 13 (2026-11-18)

Eight net-new providers added, one entry refreshed. The sweep this pass
followed the Gonka broker ecosystem (six independent resellers of the same
open-weight capacity, each with its own free grant), the Shanghai AI Lab
InkStone trial, and two sovereign-model labs (Thailand's Typhoon, India's
Sarvam). Every verdict below was taken from the provider's own page.

| Lead | Verdict | Provider id | Evidence |
| --- | --- | --- | --- |
| Dahl Inference (inference.dahl.global) | added | dahl | Homepage: "First 100 million tokens free", OpenAI-compatible at /v1, no card. Operator FROMZERO OÜ (Estonia) reselling Gonka capacity. |
| Intern InkStone (书生·端砚) | added | intern-inkstone | discovery.intern-ai.org.cn: monthly 10 ink dots in trial; Shusheng-S2, Atria-Dawn-Preview and Agents-A1 priced at 0 dots; API at discovery-api.intern-ai.org.cn/v1, OpenAI + Anthropic shapes, WeChat QR sign-in. |
| OpenThai (openthai.aieat.or.th) | added | openthai | Free hosted API at api.aieat.or.th needing only a dummy bearer token; OpenThaiGPT 1.5 7B (Qwen 2.5 derivative, 131K context). Community/non-profit, rate-limited, no SLA. |
| JoinGonka Gateway (gate.joingonka.ai) | added | joingonka | "3M tokens for free upon registration"; GLM-5.3-Flash at $0.0058/1M; 10% usage fee; OpenAI + Anthropic compatible. |
| Gonka24 (gonka24.com) | added | gonka24 | "$1 in free credits after email and human verification", no card, base https://api.gonka24.com/v1, dashboard usage tracking. |
| Mingles Router (router.mingles.ai) | added | mingles | Open-source Gonka router (github.com/MinglesAI/gonka-proxy), free key in 30 s, no card/KYC, "up to 4M tokens/week". |
| Typhoon (SCB 10X) | added | typhoon | opentyphoon.ai: OpenAI-compatible research API, all Typhoon text models at $0, ~5 req/s and 200 req/min; Typhoon 2.5 30B A3B at 131K context. Usage data collected for research. |
| Sarvam AI | added | sarvam | docs.sarvam.ai: "Rs 100 worth of free credits for every verified user on signup", usable on any API, never expire; Sarvam 105B plus GLM-5.3, DeepSeek V4.1 Flash, Gemma 4 31B and Kimi K3.1 Pro on OpenAI-compatible /v2. |
| Onomeo | refreshed | onomeo | First-party check 2026-11-18: the separately suffixed free model ids are gone; free usage is now a site-wide call pool refreshed every 5 h. Entry rewritten to match. |
| ZRO (zro.moonmath.ai) | already catalogued | zro | Free plan with included daily usage resetting daily; was added in an earlier iteration. |
| Pollinations, LLM7, Cohere, SenseNova, MoArk, Routeway, Token Harbor, Tencent TokenHub, TokenReply, Bytez, AnyAPI, API.Airforce, BazaarLink, Vercel AI Gateway, MixLayer, SimpleLLM, KiosAPI, LLMTR, Aion Labs, Zhipu BigModel, iFlytek Spark, Hetzner Inference, FreeInference, ALCF Inference | already catalogued | — | Each was found in the sweep but already present in data/providers.json; no action taken. |
| Gonka-API.org | rejected | — | Page is mostly partner logos (CertiK, Bitfury, Gcore, Hyperfusion, 6block); the bonus figure is not stated on the provider's own page. |
| Hyperfusion (hyperfusion.io) | rejected | — | GCC GPU/AI cloud; own site says "book a demo", no free tier. The $10 console-credit claim comes only from Gonka's third-party broker list. |
| Bhashini | rejected | — | ASR/NMT/TTS speech and translation only, not an LLM text-chat API; out of scope. |
| Nineteen (sn19.ai) | open | — | Lead not yet verified against the provider's own page. |
| Yandex AI Studio | open | — | "Grant for new users: 4000 ₽" claimed by third parties; not yet verified first-party. |

**Tally:** added 8 · refreshed 1 · already catalogued 25 · rejected 3 ·
open 2.

Standing rule applied: a provider whose free path needs a card first is not
catalogued, and a grant figure that appears only in a third-party list is
not treated as evidence.
