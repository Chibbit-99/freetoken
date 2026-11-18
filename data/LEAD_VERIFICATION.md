# Lead verification — iteration 12 (2026-11-17)

Nineteen leads raised this pass. Sources were shifted away from English
"free LLM API" round-ups: Chinese, Russian, Japanese, Korean, Portuguese and
German queries, plus three directories (`free-llm.com`, `freellm.net`,
`awesome-free-llm-apis`) whose changelogs name providers nobody writes listicles
about. Every verdict below was taken from the provider's own page.

| Lead | Verdict | Provider id | Evidence |
| --- | --- | --- | --- |
| AxForge (axforge.ai) | added | axforge | Pricing page: "Every new account includes 3M free serverless tokens every 30 days. No card required." Renews, so not trial credit. |
| GigaChat (Sber) | added | gigachat | Product page states 365,000,000 tokens "with annual renewal" for individuals; split 250M Lite / 50M Ultra / 40M Pro / 25M Max. |
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
