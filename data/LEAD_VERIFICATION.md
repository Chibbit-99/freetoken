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

# Lead verification — iteration 14 (2026-11-17)

Five providers added with recurring free usage, rather than one-time grants.
All five free offers are documented by the provider. Signup card requirements
were not explicitly confirmed, so they are marked unknown, not no-card.

| Lead | Verdict | Evidence |
| --- | --- | --- |
| EXAONE | added | [LG](https://www.lgresearch.ai/news/view?seq=755) offers K-EXAONE 2.5 free; [rate limits](https://docs.exaone.ai/en/docs/rate-limits) include a daily window, increased with optional data consent. Example figures are not a promised quota. |
| LXD API | added | [Pricing](https://api.lxds.org/) lists $0 plan, 5 Xen daily, all text models and 5 images/day. Xen-to-token conversion and signup card requirement unconfirmed. |
| NagaAI | added | [Model page](https://naga.ac/models/nvidia/nemotron-3-ultra-550b-a55b:free): no top-up needed, 10/min and 100/day shared across free models. |
| Poixe AI | added | [Free-model page](https://poixe.com/products/free): unpaid tier has separate 5/day high-performance and 50/day lightweight groups, with separate CLI2API limits. |
| LiteRouter | added | [Basic plan](https://literouter.com/) is $0, unlimited daily requests on some free models, up to 50 premium requests/day, one concurrent and seven-second cooldown. [Quickstart](https://docs.literouter.com/quickstart) gives a free model ID. |
| KiosAPI, Aion Labs, xKiro, ElectronHub, Agnes AI, UnoRouter, Token Harbor | already catalogued | Manifest entries exist; do not duplicate. |
| GitHub Models | rejected | [Retired July 30, 2026](https://docs.github.com/en/github-models). |
| Cerebras | rejected | [Free trial requires a verified payment method](https://inference-docs.cerebras.ai/support/rate-limits). |
| You.com, Fanar, Nineteen, EVREN, Pooled AI, OrcaRouter | open | Recurring allowance, eligibility, or public terms not sufficiently verified for addition. |

The no-card filter excludes unknown card requirements; a $0 tier or lack of
required top-up does not by itself prove card-free signup.

# Lead verification — iteration 15 (2026-11-17)

Five net-new providers added after checking the linked directories against
provider pages. Quotas refer to free accounts and can change; no live inference
requests were made.

| Lead | Verdict | Evidence |
| --- | --- | --- |
| Plugsky | added | [Docs](https://plugsky.com/docs): Micro/Lite on permanent no-card Free plan, 500 requests and 250K tokens per day (100/50K first 24 hours), 30 RPM. |
| Septor Labs | added | [Homepage](https://septorlabs.com/) and [free model](https://septorlabs.com/models/hermes-3-llama-3.1-405b-free): 50 requests and 250K tokens/day, no card; free inference uses independent aggregators. $1 signup balance is separate and one-time. |
| CLōD | added | [Free page](https://clod.io/free-cheap-ai) and [catalogue](https://app.clod.io/auth/models): 100 daily free requests, no card; selected model badges say Free alongside token prices, so verify actual route before use. |
| DreamPrompting | added | [Pricing](https://dreamprompting.com/pricing): 500K tokens and 5,000 requests per rolling day, no card, shared upstream pool; model fallback can be disabled. |
| Gizmo | added | [API docs](https://gizmoplatforms.com/developers) and [Nemotron free model](https://gizmoplatforms.com/models/nvidia/nemotron-3-ultra-550b-a55b:free): 1,000 zero-cost-model API requests/calendar month and no-card signup. Separate paid-model usage may require a payment method. |
| Router9 | unresolved, not added | [Pricing](https://www.router9.com/pricing) promises 10K credits/month; [model access docs](https://www.router9.com/docs/api-reference/models) say Free is restricted to explicitly flagged routes, but [public catalogue](https://www.router9.com/models) shows a dash in the Free Tier column for every text model. No free-account inference test was possible. Rate-limit docs mention rollover while [credits docs](https://www.router9.com/docs/token-plan/credits) say credits no longer roll over for new accounts. |
| APInex | excluded | [Homepage](https://apinex.bond/) requires a $5 top-up to unlock 25M daily free-category tokens; user excludes payment-gated recurring offers. |
| FreeAIapikey | excluded | [Pricing](https://freeaiapikey.com/pricing) says the daily free plan requires a one-time $5 payment, despite stale no-card directory claims. |
| Free.ai | unresolved, not added | [Developer page](https://free.ai/developer/) claims free API key and 30K/day, but [API reference](https://free.ai/api/) says purchase tokens before generating a key. Purchase requirement needs clarification or an authenticated test. |

All sources checked 2026-11-17. Router9 and Free.ai remain leads rather than
confirmed usable no-payment text APIs.

## Iteration 16 — 2026-11-17

Discovery included the [freetokens tracker](https://github.com/luongnv89/freetokens), the [free inference index](https://freeinference.dev/), [GitHub community lists and discussions](https://github.com/mnfst/awesome-free-llm-apis), and a [YouTube video](https://www.youtube.com/watch?v=QADqE9mlOdo). These were leads, not proof of current eligibility. No authenticated API calls or billing tests were performed.

| Lead | Decision and first-party evidence |
| --- | --- |
| Synap | Added recurring: [account](https://synap402.com/ai/account.html) and [docs](https://synap402.com/ai/docs.html) specify 100K/50 daily first 7 days, then 50K/10; no card. A second account-page section still has the old limit. |
| ChatAnywhere | Added recurring: [README](https://github.com/chatanywhere/GPT_API_free) says 50K points/week, 100 requests/day/key, GitHub binding, non-commercial only; [homepage](https://chatanywhere.tech/) confirms free key. Card status unknown. |
| ModelBridge | Added recurring: [pricing](https://aibridge-api.com/pricing.html) says 500K tokens/month and no card; 500K bonus is one-time. |
| MindsHub | Added recurring: [inference](https://mindshub.ai/unified-inference) and [home](https://mindshub.ai/) offer Air within daily fair use, no card, for non-coding work; published absolute allowance absent. |
| Y-API | Added free models: [homepage](https://y-api.bestvirtualgoods.com/) and [catalog](https://y-api.bestvirtualgoods.com/models) say no card, 100 requests/day and selected models deduct no credit; free flag can be withdrawn and calls automatically become paid. |
| Eden AI | Added free models: [vendor article](https://www.edenai.co/post/top-free-text-generation-tools-apis-and-open-source-models) lists tested $0 routes; [another](https://www.edenai.co/post/top-free-llm-tools-apis-and-open-source-models) conflicts on region. Quota, billing activation and residency require checking. |
| Maritaca | Added temporary preview, not recurring: [docs](https://docs.maritaca.ai/en/s5-quick-start) state S5-free is limited-time and text-only. |
| KRAFTON Raon | Added temporary preview, not recurring: [launch](https://raon-mini.krafton.ai/en) and [hosted terms](https://raon-mini.krafton.ai/en/terms) specify evaluation/development beta, limits and application. |
| Codiv | Added finite trial: [site](https://codiv.ai/) and [model docs](https://codiv.ai/docs/models) identify 10M text-generation tokens per account, separate from System One; no card, no renewal stated. |
| CallMissed | Added finite trial: [pricing](https://www.callmissed.com/pricing) specifies 1,000 signup credits, 100 LLM calls/month and no monthly credit grant; calls spend credits. [Vendor blog](https://www.callmissed.com/blog/how-to-get-a-free-api-key-for-llm-models-from-callmissed-features-models-and-usa) says signup needs no card. |
| Reka | Not added: [old index claim](https://freellmapi.co/state-of-free-llm-apis-2026) of $10/month lacks current vendor corroboration; [maintainer report](https://github.com/tashfeenahmed/freellmapi/issues/1559) says prepaid credits required. No current first-party free tier verified. |
| FreeTheAI | Not added: [operator](https://freetheai.org/blog/free-tier-closing) closed free tier for most accounts on Nov 10, despite old indexes/search results. |
| APInex | Excluded: [operator](https://apinex.bond/) requires initial top-up for free aliases. |
| Unisound | Not added: [U2-Decision](https://maas.unisound.com/model-hub/u2-decision) is a temporary decision API, not text generation; [U2-Flash](https://maas.unisound.com/model-hub/u2-flash) is priced. |
| VModel | Not added: [pricing](https://vmodel.ai/docs/api/pricing.html) claims $10 credits valid for text but no specific available text-generation model verified. |
