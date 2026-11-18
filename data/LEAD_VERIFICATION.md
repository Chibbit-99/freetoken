# Lead verification — second sweep (2026-11-17)

Every lead carried over from the previous pass, plus the new ones that surfaced while checking, with the verdict and the reason. "hold" means the free tier is real but the free model IDs are only visible inside an account, so the row cannot be written without guessing.

| Lead | Verdict | Provider id | Why |
| --- | --- | --- | --- |

| Nexusify | add | nexusify | $25 free credit renewed every Monday, 130 rpm, no card, 99 text models. Docs state the credit and the cap. |
| UnoRouter | add | unorouter | 294 models, 159 marked free with a `:free` suffix, one OpenAI-compatible key. |
| onomeo | add | onomeo | Free models cost nothing with per-window call quotas (account_quota 403, network_quota 429); paid models need a top-up. |
| StudioLM | add | studiolm | API chat route carries a free daily token allowance on gemma-3-12b-it-qat; images are paid. |
| DGrid | add | dgrid | Single router model dgridai/free at $0/M input and output, OpenAI-compatible, free key. |
| TokenReply | hold | — | Free tier is real (free-tagged models, 40 requests/day to Models of the week, daily rewards) but the 28 free model IDs only render in a logged-in session — model rows cannot be written honestly yet. |
| Coarena | hold | — | Free tier confirmed first-party: free models every day, 30 rpm, 2 concurrent, no card. Which of the 24 IDs are in the free set is only shown in the account. |
| ValorGPT | hold | — | Site shows 523 models and a '16 Free' count, but the free subset is not enumerable without an account. |
| AnyAPI (already added) | partial | anyapi | Free plan (100K ANY tokens/day) is published; the free model IDs are login-gated, so the two rows carry the models its public directory names. |
| A4F | reject | — | Models page returns only marketing copy — the catalogue renders client-side behind a login, so no free tier could be read. |
| AI Pooled (pool'edAI) | reject | — | Relay with no pricing or free-tier page; nothing documents a free allowance. |
| CoderPlan | reject | — | Pay-as-you-go credits only; signup credit is 'if awarded' and every tier is a top-up. |
| Subaxis | dead | — | Homepage is a shutdown notice: service discontinued, balances only recoverable via Discord ticket. |
| CoderPlan / AI Pooled / A4F | reject | — | See above — no first-party free tier. |
| ZeroLimitAI, Grokified, Router9, Septor Labs, APINex | unverified | — | No first-party page reached from the directories that list them; APINex gates its free quota behind a $5 payment, so it fails the no-pay rule anyway. |

## Tally

- **Added:** 5 (Nexusify, UnoRouter, onomeo, StudioLM, DGrid).
- **Held for account access:** 3 (TokenReply, Coarena, ValorGPT) — each needs one logged-in look to enumerate its free models.
- **Rejected:** 5 (A4F, pool'edAI, CoderPlan, plus ZeroLimitAI/Grokified/Router9/Septor Labs/APINex with no first-party page, and APINex which wants $5 first).
- **Dead:** 1 (Subaxis).
