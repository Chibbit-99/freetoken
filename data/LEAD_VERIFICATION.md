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

## Iteration 17 — 2026-11-17

Added 100milionseek and ten additional services. All findings below are based on provider statements, not authenticated signup, paid-billing or live inference tests. Provider uptime, model identity and privacy claims are not independently verified.

| Lead | Decision and evidence |
| --- | --- |
| 100milionseek | [Docs](https://100milionseek.top/docs): normal 100M tokens/day; 400M/day promotion until Nov 20 19:14 UTC. Banner reports overload, failed requests and paused signups. New, unstable: monitor. No-storage statement is operator claim. |
| devseek | [Home](https://devseek.space/) and [docs](https://devseek.space/docs): separate key and data pool associated with 100milionseek, not an independent organization. No daily cap, no card; raw data stored 30 days and de-identified data sold. Homepage currently reports outage and labels upstream a mock test double. |
| Runcrate | [Free inference](https://www.runcrate.ai/inference/free): weekly workspace allowance, eligible GitHub account no card; Google requires card and auto top-up, and paid balance may be spent on overage or during free capacity overload. Third-party providers handle data. |
| KIE AI | [Model page](https://kie.ai/gpt-6-1-terra): 80 new-user credits for testing, calls consume credits. Finite trial, expiry and card status unknown. |
| Bee by HEOSSI | [Pricing](https://bee.heossi.com/pricing) says free no-card Cell workspace has five-hour refilling window and 2M monthly ceiling, one API key; separately priced API track. [SDK](https://bee.heossi.com/docs/sdks) provides model ID and endpoint. |
| EvolveX | [Pricing](https://www.evolvex.gg/pricing): 5 RPM, GitHub, no card. [Docs](https://www.evolvex.gg/docs) list models but do not identify specific Free models; homepage and pricing disagree on key requirement. |
| HelixMind | [Pricing](https://helixmind.online/pricing): Seed 50 requests/rolling day, 3 RPM, 10K input, 4 models, no card. [Catalog](https://helixmind.online/models) marks auto-model free but Seed eligibility not established. |
| kenari | [Homepage](https://kenari.id/) and [free model docs](https://kenari.id/docs/free-models): zero-balance new accounts get free-model access; homepage lists 50/day and 5 RPM, subject to model overrides. Higher limits require top-up but basic tier does not. |
| VoidAI | [Pricing](https://voidai.app/pricing) and [catalog](https://voidai.app/models): 125K daily credits, different per-model credit rates, listed model access is not live availability; [home](https://voidai.app/) says no card. |
| Zylo API | [Pricing](https://zyloai.net/) and [model page](https://zyloai.net/models/gpt-oss.html): no-card Basic, 200K tokens/day, 7,200 requests/day, 10 RPM, selected models including gpt-oss. Catalog prices apply to paid usage, not Basic allowance. |
| APIShare | [Marketplace homepage](https://apishare.cc/) lists zero-cost promotional routes and one signup credit; promotion term and daily cap unpublished, Qwen RPM claim conflicts. Card status unknown. |
| Zydit | Not added: [operator notice](https://zydit.in/) says service is permanently over, contrary to stale directories. |
| APInex | Excluded: mandatory initial top-up, per user instruction. |

## Iteration 18 — 2026-11-17

Target: 20 new providers; eight supported additions, all limited or trial access. Public pages were reviewed; no account creation, authenticated inference, identity, billing, credit delivery or reliability was independently tested. Do not mistake model names in marketing for verified upstream identity.

| Lead | Decision and evidence |
| --- | --- |
| ZeroLimitAI | Include: [developers](https://www.zerolimitai.com/developers) and [API docs](https://www.zerolimitai.com/docs/api) state 25 calls/day for seven days, no card; routing may substitute the requested model. Evaluation only. |
| YepAPI | Include as trial: [homepage](https://www.yepapi.com/) advertises $5, no card; [Nemotron page](https://www.yepapi.com/ai-api/nvidia/nemotron-3-super) says $0 per token but also mentions per-request billing. Zero-balance operation and charges are unverified. |
| SmarToken | Include: [$1 campaign](https://thesmartoken.com/campaign) is for approved eligible accounts, expires in 30 days; [homepage](https://thesmartoken.com/) documents text routes. Card requirement unconfirmed. |
| TokenMix | Include: [homepage](https://tokenmix.ai/) advertises signup credits and no card, but amount/expiry unconfirmed; [model page](https://tokenmix.ai/models/qwen/qwen3.8-flash) gives chat API example. |
| ToAPIs | Include: [homepage](https://toapis.com/) advertises no-card trial credits; [model guide](https://toapis.com/model-guide/deepseek-v4-flash) documents chat. Credit amount and expiry unconfirmed. |
| AnyRouter | Include only its five-call trial per [homepage](https://anyrouter.dev/) and [pricing](https://anyrouter.dev/pricing). Ongoing models require paid Go or donating an upstream key. Distinct from AgentRouter. |
| Helyx AI | Include cautiously: [$10 signup](https://helyxai.space/signup) advertised, but 50+ model claim conflicts with [eight-model catalog](https://helyxai.space/models-list), which mentions unclear daily claims. Actual operation, identity and credit delivery unknown. |
| TokenLab | Include: [homepage](https://tokenlab.sh/) advertises $0.25 for up to ten calls in seven days. lemondata.cc redirects here; card and eligible trial models unconfirmed. |
| AIHubMix | Correct existing entry: [free models](https://aihubmix.com/models/free) says only ten trial calls without payment; recurring daily quotas require a $1 top-up. Replace old recurring claim and unsupported model IDs. |
| InferAll, ApiFreeLLM | Already indexed; not new. InferAll's [homepage](https://inferall.ai/) distinguishes 25 no-payment calls/day from a paid higher cap. |
| AgentRouter | Excluded at user's explicit direction: user reports purported Claude Opus is not genuine and service is unstable. This is a user report, not an independently verified finding. |
| APInex | Excluded at user's direction: initial top-up required. |
| AkashML | [Documentation](https://akashml.com/docs/getting-started/introduction) and homepage conflict over payment verification / API access; no no-purchase API eligibility established. |
| Grokified | [Pricing](https://grokified.com/pricing) conditions bonus on top-up or plan. |
| OfoxAI | Its formerly free [GLM route](https://ofox.ai/models/z-ai/glm-4.7-flash%3Afree) is marked deprecated and no longer accepts requests. |
| InferRoute | Live site could not be fetched; archived marketing alone is insufficient. |
| deAPI, Articul8 Bivia | Media/embedding and decision APIs respectively; no general text generation established, so outside catalogue scope. |
| Anakin | [Pricing](https://anakin.ai/pricing) says model usage is BYOK, not a free hosted model allowance. |
| Runtime, OpenScale | Runtime now redirects to a paid model site with no confirmed free offer; OpenScale domain is for sale. |

## Iteration 19 — 2026-11-17

Research focused on no-top-up recurring access. Three rate-limited free-model offers were added; none is a verified daily/weekly/monthly credit grant. Public terms were reviewed, but no signup, authenticated inference, model identity, billing or reliability was tested.

| Lead | Decision and evidence |
| --- | --- |
| BeatAPI | Include as limited-time free models: [official documentation](https://docs.beatapi.io/free-models) says zero balance and no top-up required, 1 successful request/minute before top-up. Contrary to a [third-party directory](https://github.com/peter123023/awesome-free-llm-api)'s 2,000/day claim, official docs explicitly promise no daily allowance. Card requirement not confirmed. |
| CrowLLM | Include: [pricing](https://crowllm.com/pricing) says no card or top-up for its free lane, limited to a handful of calls/minute; [Solar Mini4 page](https://crowllm.com/models/solar-mini4:free) lists zero input and output pricing. Do not assume every :free suffix is zero-priced; a [catalogue contribution](https://github.com/mnfst/awesome-free-llm-apis/pull/172) identifies earned-credit exceptions. |
| Numes | Include: [models docs](https://numes.ai/docs/models) explicitly describe zero-cost :free routes, verified email and rate limits; selected IDs shown in live catalog. No numerical cap or card requirement established. |
| Router9 | Defer: [pricing](https://www.router9.com/pricing) offers 10,000 monthly credits restricted to free-tier models and [quickstart](https://www.router9.com/docs/quickstart) requires admin approval; [catalog](https://www.router9.com/models) currently marks no text models as free-tier eligible. Card requirements unknown. |
| DX Network | Defer: [homepage](https://www.dxnt.com/) still advertises 100+ free calls/day, but current [FAQ](https://www.dxnt.com/faq) says free route no longer consumes daily quota and instead spends finite bonus credit, then paid balance; daily quotas are for paid members. The old freerouter page now returns 404. |
| Free.ai | Defer: [API page](https://free.ai/api/) advertises 30K tokens/day and 1,000 requests/month, but its setup says to purchase tokens before creating a key; no-top-up API access is unresolved. |
| Rewind.ai | Defer: [free offer](https://rewind.ai/free-ai-unlimited/) mentions 5K tokens/day and shared API balance, while [API setup](https://rewind.ai/api/) says add tokens before minting a key. |
| FreeAIapikey | Exclude recurring all-model plan: [pricing](https://freeaiapikey.com/pricing) requires a one-time $5 payment. [Docs](https://freeaiapikey.com/docs) separately mention free :free models, but no current eligible model IDs were identified. |
| BlazeAPI | Exclude: [docs](https://blazeapi.org/docs.html) show zero daily tokens and an empty free model list, contrary to third-party 200K/day claims. |
| ACLIDE | Exclude: [pricing](https://aclide.com/en/pricing) says the project ended and signups are closed, despite the stale recurring plan table. |
| Hanzo | Defer: [pricing](https://hanzo.ai/pricing) describes its no-card free daily pool for web/desktop chat, while Dev/CLI access is paid; API eligibility not established. |
| APInex, AgentRouter | Remain excluded per user instruction: APInex requires a top-up; the user reports AgentRouter's claimed Claude Opus is not genuine and the service is unstable (not independently verified). |

## Iteration 20 — deeper free-lane checks, daily rewards and trials (2026-11-17)

All amounts below are provider statements checked on public pages; no account, inference, model authenticity, balance or billing was tested. Search snippets can be stale. Credits are not assumed to be tokens or USD.

- **BeatAPI**: https://docs.beatapi.io/free-models explicitly promises no daily allowance, despite homepage language about changing daily allowances and unsupported third-party 2,000/day claims. One successful free request/minute before first top-up; exact free IDs, no paid-sibling fallback.
- **CrowLLM**: https://crowllm.com/pricing and https://crowllm.com/models/hy4-flash:free advertise a no-card zero-price lane; HY4 added alongside Solar. Discord-earned credit is mentioned but older operator Reddit claims of $1/day are not corroborated by current terms. Some :free IDs have nonzero prices; check each model.
- **Numes**: https://numes.ai/docs/api-reference/limits confirms separate free-route limits and zero-balance requests have lower priority under load. A search result attributed to its social account claims no card, but an accessible dated primary post was not verified, so the card field remains unknown. No daily numerical allowance confirmed.
- **ireze**: https://ireze.site/ and https://ireze.site/changelog advertise 4M credits per 24h only after a manual Work.ink task and Discord login, plus 2M welcome credits. Identity of the claimed Claude models is unverified; unknown IDs route to the default model. Do not treat credits as actual tokens or USD or model labels as proof.
- **1min.AI**: https://1minai.tawk.help/article/daily-free-credits-15000-credits-per-day-approximately-450000-credits-per-month and https://1min.ai/free-ai-api-for-developers document 15,000 credits for daily web visits and signup credit usable on the chat API respectively. The sources do not explicitly connect daily-earned credit to API usage; qualify accordingly.
- **Trials**: earthruntime (100K starting tokens, no card); GetAiApiKey ($0.50/7 days, manually claim, no card); NoTrack ($0.50/7 days on first key, card unknown); RouterPlex ($1 once on eligible guided setup, no card, non-expiring); Wallaby ($0.50, no card, non-expiring); Abliteration (one credit, unit value unclear, no card); Mixedbread ($5, no card, Toast 1 chat); APIVALE ($0.20, no card, but docs also mention subscribing to a plan, so free API eligibility uncertain). Respective public sources in records.
- **Deferred The Grid**: https://thegrid.ai/llms.txt advertises a $25 signup grant but current https://thegrid.ai/docs/start-here/quickstart says to check balance and add credits if needed, without confirming a signup grant; its 100 requests/day is a limit, not free funding. Do not confuse a daily cap with an allowance.
- **qwenapi.top** uses strikingly similar copy, prices, trial, model ID and terms to GetAiApiKey; operator relationship and separate eligibility are unknown. Avoid counting potentially duplicated grants as separate until established. **APInex** remains excluded (initial top-up), and **AgentRouter** remains excluded per user's report that its Claude claim was not real and service was unstable; neither finding was independently tested.

### Iteration 21 — recurring allowances and new trials

- **Nutrient AI Gateway:** [gateway](https://www.nutrient.io/api/ai-gateway-api/) and [pricing](https://www.nutrient.io/api/pricing/) say the $5/month no-card allowance is shared with document APIs. Optional wallet reloads automatically; test keys have separate controls.
- **Speka:** [pricing](https://speka.me/pricing) advertises $1/month, no card and 10 RPM; [docs](https://speka.me/docs) say 402 when allowance exhausted, while pricing describes overage billing. [Live catalog](https://speka.me/models) differs from marketing counts; use actual model rows and verify billing.
- **Opper:** [guide](https://opper.ai/blog/openai-compatible-api) identifies `gemini/gemma-4-31b` as free before adding a card; [quickstart](https://docs.opper.ai/overview/quickstart) makes clear its GPT example is paid. Numeric quota unpublished.
- **Liquid Inference:** [site](https://liquidinference.ai/) says no-card starting credit, amount and expiry unspecified; distinct from Liquid AI. Auctioned usage incurs fees.
- **Corti:** [pricing](https://corti.ai/pricing) states starting credits without card but no amount or expiry; older indexed copy advertised $50/year, not confirmed by current page. [Models](https://corti.ai/models) documents text APIs.
- **Deferred Braintrust:** [plans](https://docs.braintrust.dev/plans-and-limits) offer $10/month but direct gateway use of built-in models requires paid Pro or Enterprise; no qualifying free direct inference API established. **SeekAPI.ai** currently describes supplier sourcing, not the claimed LLM gateway. **Ofox** marks its advertised free GLM route deprecated. **Grokified** [says](https://grokified.com/blog/free-llm-api) spending credit requires a first payment; exclude under the no-top-up rule. Existing FreeTheAI is not counted twice.
- All offers are operator claims; no signup, payment, inference, or model identity independently verified.

### Iteration 22 — larger allowances (2026-11-17)

- **Vikasit AI:** [inference page](https://vikasit.ai/inference) explicitly offers 2M tokens/day on `vikasit-nova`, no card, GitHub sign-in, subject to fair use and change; the rest of the catalog is priced. [Privacy policy](https://vikasit.ai/privacy) says it is a template pending legal review. No authenticated signup, inference, billing, or model identity tested.
- **100milionseek:** [homepage](https://100milionseek.top/) advertises 100M/day normally, 400M/day until 20 November 19:14 UTC, but reports paused signups and failing requests from overload. This existing entry already flags the outage. Treat operator claims and model identity as unverified.
- **IteraCompute:** [terms](https://iteracompute.com/free/) confirm 30M/month before its no-recharge promotion ends at 00:00 Pacific Time on 24 November; thereafter only eligible pre-cutoff recharge users or subscribers retain Auto access. No top-up should be recommended to satisfy this directory's eligibility rule.
- **Packet.ai:** [product page](https://packet.ai/token-factory) says free at launch for one month, then paid, with no quota stated; [August blog](https://packet.ai/blog/ai-token-cost) claims 1M/day without a card, while [another blog](https://packet.ai/blog/packet-ai-vs-groq-vs-together-ai-pricing) says no free tier. Defer the numeric quota pending current consistent terms and clarify trial dates and card requirements.
- **UnfilteredAPI:** indexed 50M/month page is now 404 and homepage is a placeholder; not added. **Flexlora:** the current homepage is a design-reference waitlist rather than an LLM inference gateway, so old 7M/day third-party claims are not current evidence. **OpenAI data-sharing:** requires positive balance; exclude under the no-top-up rule. **APInex** and **AgentRouter** remain excluded for the previously recorded reasons.

### Iteration 23 — recurring quotas and starting grants (2026-11-17)

- **EdgeOne Makers Models:** [limits](https://pages.edgeone.ai/document/limits-and-quotas) give 500K tokens/month for built-in models in its free edition, subject to commercial changes; [models](https://pages.edgeone.ai/document/models) documents the OpenAI endpoint and `@makers/deepseek-v4-flash`; [integration](https://pages.edgeone.ai/document/makers-models-integration) separates included `@makers/` models from BYOK. Card requirement unconfirmed.
- **PEKPIK:** [free credit](https://aiapiv2.pekpik.com/free-credit) says $1 after email verification and $0.50 manually claimable each day thereafter; claims reset rather than accumulate and continue after the first $20. Its 1.85M DeepSeek figure is an input-only price conversion, not a fixed token grant. Unofficial gateway; no model identity testing.
- **nabh.cloud:** [pricing](https://nabh.cloud/pricing/) offers 50 INR credits on signup and monthly thereafter, no card, GPT OSS 20B only, 5 RPM and 500/day. Developer access requires recharge; excluded from the free offer. Free-credit rollover unclear.
- **Aevon:** [homepage](https://aevon.sh/) and [docs](https://aevon.sh/docs) claim $100 one-time signup credit and no card; free model lists disagree. The operator itself recommends prototype use. Grant, model identities and routing remain untested. **MixRoute** [homepage](https://mixroute.ai/) advertises $5 starting credit, no card, on popular models; eligibility and expiry unspecified. **TrustedRouter** [homepage](https://trustedrouter.com/) advertises 1M starting tokens, no card; expiry and eligible routes unspecified. **GW BUS** [homepage](https://gwbus.com/) and [docs](https://gwbus.com/docs) advertise $5 starting credit and a 1M/day ceiling, not an established recurrent token grant; card status unknown.
- **Mango Inference:** current [product page](https://www.mangoboost.io/platform/mango-inference) discusses promotion terms but does not state $10 signup credit; defer pending current first-party grant evidence. **LLM Gateway:** free catalog filter returned no model rows; defer until a usable free model and conditions are verified. APInex and AgentRouter remain excluded per user instructions.
- All entries are based on public operator statements; no authenticated signup, inference, billing or model identity was tested. Avoid sensitive content with unverified relays.

### Iteration 24 — final research pass (2026-11-17)

- **Flux Router:** [pricing](https://fluxrouter.ai/pricing) specifies up to $1 or 100K tokens/month, whichever is reached first, Fast lane only, 60 RPM and a hard cap. [FAQ](https://fluxrouter.ai/faq) documents OpenAI-compatible routing; card requirements unconfirmed. This is both monetary and token capped, not 100K unconditional free tokens.
- **Infercom:** [plans](https://cloud.infercom.ai/plans) offer €5 signup credit, no card, expires after 90 days. [Free-tier table](https://docs.infercom.ai/en/models/rate-limits) lists GPT OSS 120B and Gemma 4 at 20 RPM and 20 RPD. Separate account/endpoint from SambaNova; no suggestion of multiple grants on one account.
- **Flonno:** [docs](https://www.flonno.com/docs) state $1 once after email verification, no card, one Qwen model and 402 if insufficient credit. **Boundless API:** [FAQ](https://www.boundlessapi.com/en/faq.html) says $5 signup, no card, 10 RPM on Starter models; optional automatic recharge, and the exact trial-eligible model set remains unconfirmed.
- **LLM EU** [terms](https://llmeu.com/en/free-llm-api/) now say 1M one-time tokens only after attaching a Stripe payment method; the older third-party $5 no-card claim is stale. Defer, do not assert no-card access. **OpenPaths** free LLM URL currently returns an invalid-fiddle error. **Teapot Router** claims signup credits but [homepage](https://teapotrouter.com/en) also says add balance before API requests and recommends Model Lab; API use before payment is unconfirmed. **LLMCloud** signup advertises $1 no card, but first-party API endpoint and eligible text models were not established in this pass; defer.
- All newly added claims are provider statements, not authenticated inference, signup, billing or model identity verification. APInex and AgentRouter remain excluded per user instructions.

### Existing provider token quota audit — 17 November 2026

- [Experiential Labs](https://www.experientiallabs.ai/pricing): 1M/day shared by the free core models, temporary refunded $1 card verification. Count the shared pool once; overflow can bill credits.
- [Synap](https://synap402.com/account.html): 100K/day for the first seven days, then 50K/day. Count the ongoing 50K/day; the same page still contains an unqualified 100K statement.
- [ModelBridge](https://aibridge-api.com/pricing.html): 500K/month plus 500K welcome bonus; count each once in the first month, no card, overage may bill.
- [Codiv](https://codiv.ai/): 10M one-time text-generation tokens; exclude the separate 100M System One decision-model tokens from this text-generation directory.
- [SlashAI](https://slashai.my.id/): search-indexed provider pricing advertises 2M tokens for a single one-hour trial. Site returned HTTP 500 during this recheck; retain the prior recorded offer as provisional.
- [Bee](https://bee.heossi.com/pricing): Cell describes a 2M/month ceiling and a five-hour refill window; the API pricing track is separately metered. Treat this as an upper bound pending account verification.
- [Flux Router](https://fluxrouter.ai/pricing): 100K/month OR $1/month, whichever runs out first; the count is an upper bound, not guaranteed tokens.
- [100milionseek](https://100milionseek.top/): normal 100M/day, but signup paused and requests failing due to overload. Omitted from numeric aggregation until availability is restored; temporary 400M/day promotion is not extrapolated.
- [Tencent TokenHub](https://www.tencentcloud.com/act/pro/tokenhub): trial quota scope is inconsistent across Tencent's own pages and other evidence indicates a $10 balance freeze. No token pool added without resolving the initial-funding requirement and scope. GW BUS's 1M/day is bounded by finite $5 credit, not an additional recurring grant.

All are advertised allowances or ceilings, not independently tested inference, billing, or model identity.
