#!/usr/bin/env python3
"""Write the freeinferencing.com additions into data/ and update the manifest.

Usage: python3 tools/add_new_providers.py [--dry-run]
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from models import MODELS  # noqa: E402
from speed import tps_for  # noqa: E402
from new_providers_a import PART_A  # noqa: E402
from new_providers_b import PART_B  # noqa: E402
from new_providers_c import PART_C  # noqa: E402
from new_providers_d import PART_D  # noqa: E402
from new_providers_e import PART_E  # noqa: E402
from new_providers_f import PART_F  # noqa: E402
from new_providers_g import PART_G  # noqa: E402
from new_providers_h import PART_H  # noqa: E402
from new_providers_i import PART_I  # noqa: E402
from new_providers_j import PART_J  # noqa: E402
from new_providers_k import PART_K  # noqa: E402
from new_providers_l import PART_L  # noqa: E402
from new_providers_m import PART_M  # noqa: E402
from new_providers_n import PART_N  # noqa: E402
from new_providers_o import PART_O  # noqa: E402
from new_providers_p import PART_P  # noqa: E402
from new_providers_r import PART_R  # noqa: E402
from new_providers_s import PART_S  # noqa: E402
from new_providers_t import PART_T  # noqa: E402
from new_providers_u import PART_U  # noqa: E402
from new_providers_v import PART_V  # noqa: E402
from new_providers_w import PART_W  # noqa: E402
from new_providers_q import PART_Q  # noqa: E402

DATA = os.path.join(os.path.dirname(HERE), "data")
CHECKED = "2026-11-17"
SOURCE_SNAPSHOT = "https://freeinferencing.com/"

OFFER = {
    "af": ("always-free", "emerald"),
    "fm": ("free-models", "blue"),
    "mc": ("monthly-credits", "amber"),
    "rs": ("research", "sky"),
    "tr": ("trials", "amber"),
}
PRIVACY = {"pv": "private", "pp": "partial", "nn": "none", None: "none"}

# Providers whose free offer is not text-model specific still need a model row.
# Providers removed from the catalogue because they are not text-LLM APIs
# (speech, image/video, embeddings) or because the free offer did not hold up.
SKIP = {
    "elevenlabs", "cartesia", "deepgram", "assemblyai", "speechmatics", "palabra",
    "async-voice", "paxa-labs", "lelapa", "viggle", "stability-ai", "wavespeed",
    "inferon", "clarifai", "voyage-ai", "jina-ai", "qdrant-cloud", "mongodb-atlas",
    "vlm-run",
    # ":free" routes need a retained $5 prepaid balance, so the tier is not free in practice.
    "infron",
}

# First-party pages read for each added provider, used for verified.sources.
SOURCES = {
    "flux-router": ["https://fluxrouter.ai/pricing", "https://fluxrouter.ai/faq"],
    "infercom": ["https://cloud.infercom.ai/plans", "https://docs.infercom.ai/en/models/rate-limits"],
    "flonno": ["https://www.flonno.com/", "https://www.flonno.com/docs"],
    "boundless-api": ["https://www.boundlessapi.com/en/", "https://www.boundlessapi.com/en/faq.html"],
    "pekpik": ["https://aiapiv2.pekpik.com/free-credit", "https://aiapiv2.pekpik.com/docs/quickstart/"],
    "nabh-cloud": ["https://nabh.cloud/pricing/", "https://nabh.cloud/docs/"],
    "aevon": ["https://aevon.sh/", "https://aevon.sh/docs"],
    "mixroute": ["https://mixroute.ai/", "https://mixroute.ai/docs/introduction"],
    "trustedrouter": ["https://trustedrouter.com/"],
    "gwbus": ["https://gwbus.com/", "https://gwbus.com/docs"],
    "edgeone-makers": ["https://pages.edgeone.ai/document/limits-and-quotas", "https://pages.edgeone.ai/document/models", "https://pages.edgeone.ai/document/makers-models-integration"],
    "vikasit-ai": ["https://vikasit.ai/inference", "https://vikasit.ai/privacy"],
    "nutrient": ["https://www.nutrient.io/api/ai-gateway-api/", "https://www.nutrient.io/api/pricing/"],
    "speka": ["https://speka.me/pricing", "https://speka.me/docs", "https://speka.me/models"],
    "opper": ["https://docs.opper.ai/overview/quickstart", "https://opper.ai/blog/openai-compatible-api"],
    "liquid-inference": ["https://liquidinference.ai/", "https://liquidinference.ai/docs"],
    "corti": ["https://corti.ai/pricing", "https://corti.ai/models"],
    "ireze": ["https://ireze.site/", "https://ireze.site/changelog"],
    "1min-ai": ["https://1min.ai/free-ai-api-for-developers", "https://1minai.tawk.help/article/daily-free-credits-15000-credits-per-day-approximately-450000-credits-per-month"],
    "earthruntime": ["https://earthruntime.com/"],
    "getaiapikey": ["https://getaiapikey.com/", "https://getaiapikey.com/terms/"],
    "notrack-api": ["https://notrack.ai/api"],
    "routerplex": ["https://routerplex.com/", "https://docs.routerplex.com/quickstart"],
    "wallaby": ["https://wallabytoken.com/", "https://wallabytoken.com/blog/p/kimi-k3-free-trial"],
    "abliteration": ["https://abliteration.ai/pricing", "https://docs.abliteration.ai/api/rate-limits"],
    "mixedbread": ["https://www.mixedbread.com/pricing", "https://www.mixedbread.com/docs/agent/chat-completions"],
    "apivale": ["https://apivale.com/", "https://apivale.com/docs"],
    "beatapi": ["https://docs.beatapi.io/free-models", "https://beatapi.io/"],
    "crowllm": ["https://crowllm.com/pricing", "https://crowllm.com/models/solar-mini4:free", "https://crowllm.com/models/hy4-flash:free"],
    "numes": ["https://numes.ai/docs/models", "https://numes.ai/docs/api-reference/overview", "https://numes.ai/docs/api-reference/limits"],
    "aihubmix": ["https://aihubmix.com/models/free"],
    "zerolimitai": ["https://www.zerolimitai.com/developers", "https://www.zerolimitai.com/docs/api"],
    "yepapi": ["https://www.yepapi.com/", "https://www.yepapi.com/ai-api/nvidia/nemotron-3-super"],
    "smartoken": ["https://thesmartoken.com/campaign", "https://thesmartoken.com/"],
    "tokenmix": ["https://tokenmix.ai/", "https://tokenmix.ai/models/qwen/qwen3.8-flash"],
    "toapis": ["https://toapis.com/", "https://toapis.com/model-guide/deepseek-v4-flash"],
    "anyrouter-dev": ["https://anyrouter.dev/", "https://anyrouter.dev/pricing"],
    "helyx-ai": ["https://helyxai.space/signup", "https://helyxai.space/models-list"],
    "tokenlab": ["https://tokenlab.sh/", "https://tokenlab.sh/en/pricing"],
    "100milionseek": ["https://100milionseek.top/docs", "https://100milionseek.top/"],
    "devseek": ["https://devseek.space/", "https://devseek.space/docs"],
    "runcrate": ["https://www.runcrate.ai/inference/free", "https://www.runcrate.ai/privacy"],
    "kie-ai": ["https://kie.ai/gpt-6-1-terra", "https://kie.ai/"],
    "bee-heossi": ["https://bee.heossi.com/pricing", "https://bee.heossi.com/docs/sdks"],
    "evolvex": ["https://www.evolvex.gg/pricing", "https://www.evolvex.gg/docs"],
    "helixmind": ["https://helixmind.online/pricing", "https://helixmind.online/models"],
    "kenari": ["https://kenari.id/", "https://kenari.id/docs/free-models"],
    "void-ai": ["https://voidai.app/pricing", "https://voidai.app/models"],
    "zylo-api": ["https://zyloai.net/", "https://zyloai.net/models/gpt-oss.html"],
    "apishare": ["https://apishare.cc/", "https://apishare.cc/market"],
    "synap": ["https://synap402.com/ai/account.html", "https://synap402.com/ai/docs.html"],
    "chatanywhere": ["https://github.com/chatanywhere/GPT_API_free", "https://chatanywhere.tech/"],
    "modelbridge": ["https://aibridge-api.com/pricing.html", "https://aibridge-api.com/docs.html"],
    "mindshub": ["https://mindshub.ai/unified-inference", "https://mindshub.ai/"],
    "y-api": ["https://y-api.bestvirtualgoods.com/", "https://y-api.bestvirtualgoods.com/models"],
    "eden-ai": ["https://www.edenai.co/post/top-free-text-generation-tools-apis-and-open-source-models", "https://www.edenai.co/post/top-free-llm-tools-apis-and-open-source-models"],
    "maritaca": ["https://docs.maritaca.ai/en/overview", "https://docs.maritaca.ai/en/s5-quick-start"],
    "krafton-raon": ["https://raon-mini.krafton.ai/en", "https://raon-mini.krafton.ai/en/terms"],
    "codiv": ["https://codiv.ai/", "https://codiv.ai/docs/models"],
    "callmissed": ["https://www.callmissed.com/pricing", "https://www.callmissed.com/blog/how-to-get-a-free-api-key-for-llm-models-from-callmissed-features-models-and-usa"],
    "plugsky": ["https://plugsky.com/docs", "https://plugsky.com/articles/ai-api-for-law-firms-use-cases-security-and-deployment-options"],
    "septor-labs": ["https://septorlabs.com/", "https://septorlabs.com/models/hermes-3-llama-3.1-405b-free"],
    "clod": ["https://clod.io/free-cheap-ai", "https://app.clod.io/auth/models", "https://clod.io/docs"],
    "dreamprompting": ["https://dreamprompting.com/pricing", "https://dreamprompting.com/models"],
    "gizmo": ["https://gizmoplatforms.com/developers", "https://gizmoplatforms.com/models/nvidia/nemotron-3-ultra-550b-a55b:free"],
    "exaone": ["https://www.lgresearch.ai/news/view?seq=755", "https://docs.exaone.ai/en/docs/rate-limits"],
    "lxd-api": ["https://api.lxds.org/", "https://api.lxds.org/instructions"],
    "naga-ai": ["https://naga.ac/models/nvidia/nemotron-3-ultra-550b-a55b:free", "https://docs.naga.ac/api-reference/overview"],
    "poixe-ai": ["https://poixe.com/products/free", "https://poixe.com/"],
    "literouter": ["https://literouter.com/", "https://docs.literouter.com/quickstart"],
    "merkium": ["https://www.merkium.nl", "https://mvalentsev.github.io/awesome-free-ai-coding/providers/merkium/"],
    "iteracompute": ["https://iteracompute.com/free/", "https://mvalentsev.github.io/awesome-free-ai-coding/providers/iteracompute/"],
    "miapi": ["https://miapi.uk", "https://mvalentsev.github.io/awesome-free-ai-coding/providers/miapi/"],
    "sambanova": ["https://docs.sambanova.ai/docs/en/models/rate-limits", "https://cloud.sambanova.ai"],
    "freeinference": ["https://doc.freeinference.org/models", "https://freeinference.org/terms"],
    "sea-lion": ["https://sea-lion.ai/try-sea-lion/", "https://docs.sea-lion.ai/guides/inferencing/api"],
    "opentyphoon": ["https://docs.opentyphoon.ai/en/rate-limits/", "https://docs.opentyphoon.ai/en/faq/"],
    "agnes-ai": ["https://wiki.agnes-ai.com/en/docs/pricing", "https://wiki.agnes-ai.com/en/docs/faqs"],
    "nara-router": ["https://router.bynara.id/api/plans", "https://router.bynara.id/docs"],
    "plamo": ["https://docs.plamo.preferredai.jp/en/api", "https://plamo.preferredai.jp/"],
    "api-free-llm": ["https://apifreellm.com/en/api-access", "https://apifreellm.com/en"],
    "navy-ai": ["https://api.navy", "https://nejib1.github.io/Free-LLM/"],
    "ant-ling": ["https://ling.tbox.cn", "https://api.tbox.cn/api/llm/v1"],
    "sakura-ai-engine": ["https://cloud.sakura.ad.jp/aipf/ai-engine/", "https://manual.sakura.ad.jp/cloud/ai-engine/"],
    "mlvoca": ["https://mlvoca.com", "https://github.com/mlvoca/free-llm-api"],
    "gmi-cloud": ["https://www.gmicloud.ai/en/blog/best-free-gpu-cloud-options-for-ai-startups-and-researchers", "https://www.gmicloud.ai"],
    "nscale": ["https://www.nscale.com", "https://docs.nscale.com"],
    "volcengine-ark": ["https://www.volcengine.com/product/ark", "https://www.volcengine.com/docs/82379"],
    "xiaomi-mimo": ["https://platform.xiaomimimo.com", "https://api.xiaomimimo.com/v1"],
    "stepfun": ["https://platform.stepfun.com", "https://api.stepfun.com/v1"],
    "baichuan": ["https://platform.baichuan-ai.com", "https://www.baichuan-ai.com"],
    "ppio": ["https://ppio.com", "https://docs.ppio.com"],
    "slashai": ["https://slashai.my.id", "https://slashai.my.id/docs"],
    "xkiro": ["https://xkiro.com/models", "https://docs.xkiro.com/guides/sdk-openai/"],
    "cheapllm-shop": ["https://cheapllm.shop/docs", "https://cheapllm.shop"],
    "electronhub": ["https://www.electronhub.ai/pricing", "https://www.electronhub.ai/models.html#access=free"],
    "anyapi": ["https://anyapi.ai/pricing", "https://anyapi.ai/ai-models"],
    "nexusify": ["https://docs.nexusify.co/", "https://nexusify.co"],
    "unorouter": ["https://unorouter.com/en", "https://unorouter.com/en/models"],
    "onomeo": ["https://onomeo.com/integrations", "https://onomeo.com/models"],
    "studiolm": ["https://studiolm.dev/", "https://docs.studiolm.dev/getting-started/quickstart/"],
    "dgrid": ["https://dgrid.ai/models/dgridai/free/", "https://dgrid.ai"],
    "tokenreply": ["https://www.tokenreply.com/docs/plans", "https://www.tokenreply.com/models"],
    "coarena": ["https://coarena.ai/docs", "https://coarena.ai/account/api"],
    "valorgpt": ["https://www.valorgpt.com/models", "https://www.valorgpt.com"],
    "freemodel": ["https://freemodel.in/", "https://freemodel.in/pricing"],
    "cleanapis": ["https://cleanapis.com/", "https://cleanapis.com/pricing"],
    "radoxai": ["https://radoxai.com/", "https://radoxai.com/pricing"],
    "oxionai": ["https://oxionai.com/", "https://oxionai.com/pricing"],
    "axforge": ["https://axforge.ai/pricing/", "https://axforge.ai/serverless-models/"],
    "gigachat": ["https://developers.sber.ru/portal/products/gigachat-api", "https://developers.sber.ru/docs/ru/gigachat/tariffs/individual-tariffs"],
    "deepseek": ["https://platform.deepseek.com/", "https://api-docs.deepseek.com/quick_start/pricing"],
    "gonkarouter": ["https://gonkarouter.io/", "https://gonkarouter.io/docs"],
    "vectoree": ["https://vectoree.ai/pricing", "https://vectoree.ai/product/model-plaza"],
    "nlp-cloud": ["https://nlpcloud.com/pricing.html", "https://docs.nlpcloud.com/"],
    "liquid-ai": ["https://www.liquid.ai/pricing", "https://console.liquid.ai/docs/getting-started"],
    "qiniu": ["https://www.qiniu.com/ai", "https://developer.qiniu.com/ai"],
    "blockrun": ["https://blockrun.ai/models?filter=free", "https://blockrun.ai/docs"],
    "dahl": ["https://inference.dahl.global/", "https://gonka.ai/docs/developer/quickstart/"],
    "zro": ["https://zro.moonmath.ai/pricing", "https://zro.moonmath.ai/"],
    "mingles": ["https://router.mingles.ai/", "https://github.com/MinglesAI/gonka-proxy"],
    "intern-inkstone": ["https://discovery.intern-ai.org.cn/token-plan/home", "https://www.shlab.org.cn/"],
    "openthai": ["https://openthai.aieat.or.th/", "https://openthai.ai/en/previous-versions-and-resources/openthaigpt-1.5"],
    "joingonka": ["https://gate.joingonka.ai/", "https://joingonka.ai/"],
    "gonka24": ["https://gonka24.com/", "https://gonka24.com/docs"],
    "typhoon": ["https://opentyphoon.ai/", "https://docs.opentyphoon.ai/en/"],
    "sarvam": ["https://www.sarvam.ai/api-pricing", "https://docs.sarvam.ai/api/getting-started/models"],
}

# Account-wide pools and published catalogue sizes, written onto the provider.
PROVIDER_EXTRA = {
    "flux-router": {"api_endpoint": "https://api.fluxrouter.ai/v1", "docs": "https://fluxrouter.ai/faq", "signup": "https://fluxrouter.ai/auth/sign-up"},
    "infercom": {"api_endpoint": "https://api.infercom.ai/v1", "docs": "https://docs.infercom.ai/en/models/rate-limits", "signup": "https://cloud.infercom.ai/"},
    "flonno": {"api_endpoint": "https://www.flonno.com/v1", "docs": "https://www.flonno.com/docs", "signup": "https://www.flonno.com/sign-up"},
    "boundless-api": {"api_endpoint": "https://api.boundlessapi.com/v1", "docs": "https://www.boundlessapi.com/en/faq.html"},
    "pekpik": {"api_endpoint": "https://aiapiv2.pekpik.com/v1", "docs": "https://aiapiv2.pekpik.com/docs/quickstart/", "signup": "https://aiapiv2.pekpik.com/register"},
    "nabh-cloud": {"api_endpoint": "https://api.nabh.cloud/v1", "docs": "https://nabh.cloud/docs/", "signup": "https://app.nabh.cloud/signup"},
    "aevon": {"api_endpoint": "https://aevon.sh/v1", "docs": "https://aevon.sh/docs", "signup": "https://aevon.sh/auth"},
    "mixroute": {"api_endpoint": "https://api.mixroute.ai/v1", "docs": "https://mixroute.ai/docs/introduction", "signup": "https://console.mixroute.ai/"},
    "trustedrouter": {"api_endpoint": "https://api.trustedrouter.com/v1", "free_token_allowance": 1000000, "allowance_period": "one-time"},
    "gwbus": {"api_endpoint": "https://api.gwbus.com/v1", "docs": "https://gwbus.com/docs"},
    "edgeone-makers": {"api_endpoint": "https://ai-gateway.edgeone.link/v1", "free_token_allowance": 500000, "allowance_period": "month", "docs": "https://pages.edgeone.ai/document/models"},
    "vikasit-ai": {"api_endpoint": "https://api.vikasit.ai/v1", "free_token_allowance": 2000000, "allowance_period": "day", "docs": "https://vikasit.ai/inference", "signup": "https://vikasit.ai/auth"},
    "ireze": {"docs": "https://ireze.site/#docs", "api_endpoint": "https://ireze.site/v1"},
    "1min-ai": {"docs": "https://docs.1min.ai/docs/api/chat-with-ai-api", "signup": "https://app.1min.ai/"},
    "earthruntime": {"docs": "https://earthruntime.com/docs", "api_endpoint": "https://api.earthruntime.com/v1", "free_token_allowance": 100000, "allowance_period": "one-time"},
    "getaiapikey": {"docs": "https://getaiapikey.com/docs/", "signup": "https://getaiapikey.com/get-api-key/", "api_endpoint": "https://api.getaiapikey.com/v1"},
    "notrack-api": {"docs": "https://notrack.ai/api/docs", "signup": "https://notrack.ai/api-keys", "api_endpoint": "https://api.notrack.ai/v1"},
    "routerplex": {"docs": "https://docs.routerplex.com/quickstart", "signup": "https://routerplex.com/sign-up", "api_endpoint": "https://api.routerplex.com/v1"},
    "wallaby": {"docs": "https://wallabytoken.com/docs", "signup": "https://api.wallabytoken.com/register", "api_endpoint": "https://api.wallabytoken.com/v1"},
    "abliteration": {"docs": "https://docs.abliteration.ai/", "signup": "https://abliteration.ai/sign-up", "api_endpoint": "https://api.abliteration.ai/v1"},
    "mixedbread": {"docs": "https://www.mixedbread.com/docs/agent/chat-completions", "signup": "https://www.platform.mixedbread.com/", "api_endpoint": "https://api.mixedbread.com/v1"},
    "apivale": {"docs": "https://apivale.com/docs", "signup": "https://apivale.com/sign-up", "api_endpoint": "https://apivale.com/v1"},
    "beatapi": {"docs": "https://docs.beatapi.io/free-models", "signup": "https://beatapi.io/dashboard/apikeys", "api_endpoint": "https://api.beatapi.io/v1"},
    "crowllm": {"docs": "https://crowllm.com/docs", "signup": "https://crowllm.com/sign-up", "api_endpoint": "https://crowllm.com/v1"},
    "numes": {"docs": "https://numes.ai/docs/models", "signup": "https://numes.ai/", "api_endpoint": "https://api.numes.ai/api/v1"},
    "plugsky": {"free_token_allowance": 250000, "allowance_period": "day"},
    "septor-labs": {"free_token_allowance": 250000, "allowance_period": "day"},
    "dreamprompting": {"free_token_allowance": 500000, "allowance_period": "day"},
    "iteracompute": {"free_token_allowance": 30000000, "allowance_period": "month"},
    "nara-router": {"free_token_allowance": 7000000, "allowance_period": "day"},
    "xkiro": {"free_token_allowance": 500000, "allowance_period": "day", "catalog_size": 69},
    "cheapllm-shop": {"free_token_allowance": 144000, "allowance_period": "day", "catalog_size": 1},
    "anyapi": {"free_token_allowance": 100000, "allowance_period": "day", "catalog_size": 400},
    "electronhub": {"catalog_size": 600},
    "nexusify": {"catalog_size": 99},
    "unorouter": {"catalog_size": 294},
    "onomeo": {"catalog_size": 40},
    "dgrid": {"catalog_size": 1},
    "tokenreply": {"catalog_size": 175},
    "valorgpt": {"catalog_size": 523},
    "freemodel": {"free_token_allowance": 1000000, "allowance_period": "month", "catalog_size": 29},
    "cleanapis": {"free_token_allowance": 500000, "allowance_period": "month", "catalog_size": 33},
    "radoxai": {"free_token_allowance": 500000, "allowance_period": "month", "catalog_size": 33},
    "oxionai": {"free_token_allowance": 500000, "allowance_period": "month", "catalog_size": 33},
    "axforge": {"free_token_allowance": 3000000, "allowance_period": "month", "catalog_size": 4},
    "gigachat": {"free_token_allowance": 365000000, "allowance_period": "year", "catalog_size": 4},
    "deepseek": {"free_token_allowance": 5000000, "allowance_period": "one-time"},
    "gonkarouter": {"free_token_allowance": 1000000, "allowance_period": "one-time"},
    "vectoree": {"catalog_size": 36},
    "qiniu": {"free_token_allowance": 3000000, "allowance_period": "one-time", "catalog_size": 70},
    "blockrun": {"catalog_size": 124},
    "dahl": {"free_token_allowance": 100000000, "allowance_period": "one-time", "catalog_size": 4},
    "zro": {"catalog_size": 2},
    "mingles": {"free_token_allowance": 4000000, "allowance_period": "week"},
    "intern-inkstone": {"catalog_size": 10},
    "joingonka": {"free_token_allowance": 3000000, "allowance_period": "one-time", "catalog_size": 3},
    "gonka24": {"catalog_size": 4},
    "typhoon": {"catalog_size": 12},
    "sarvam": {"catalog_size": 14},
    "navy-ai": {"free_token_allowance": 150000, "allowance_period": "day"},
    "ant-ling": {"free_token_allowance": 500000, "allowance_period": "day"},
    "baichuan": {"free_token_allowance": 5000000, "allowance_period": "one-time"},
    "inception": {"free_token_allowance": 100000000, "allowance_period": "one-time"},
    "amd-radeon-cloud": {"catalog_size": 9},
    "logfare": {"catalog_size": 22},
    "ndif": {"catalog_size": 113},
    "swiss-ai": {"catalog_size": 34},
    "gwdg-saia": {"catalog_size": 15},
    "helmholtz-blablador": {"catalog_size": 15},
    "nsf-nrp": {"catalog_size": 10},
    "virginia-tech-arc": {"catalog_size": 10},
    "tu-wien-aqueduct": {"catalog_size": 8},
    "goethe-ai-toollab": {"catalog_size": 17},
    "eth-sph": {"catalog_size": 8},
    "alcf-inference": {"catalog_size": 7},
    "westai": {"catalog_size": 7},
    "fastrouter": {"catalog_size": 20},
    "waterfall": {"catalog_size": 21},
    "api-airforce": {"catalog_size": 28},
    "lightning-ai": {"catalog_size": 37},
    "opencode-zen": {"catalog_size": 10},
    "taiwan-adi": {"catalog_size": 48},
    "airawat": {"catalog_size": 16},
    "moark": {"catalog_size": 200},
}

SB_LIMITS = "Free tier: 20 requests/minute, 20 requests/day, 200K tokens/day (no card)"
MERCURY_LIMITS = "100M one-time signup balance shared across Mercury 2/2.5/3; 100 RPM, 100K input TPM, 10K output TPM"

MODEL_EXTRA = {
    "inception": {
        "mercury-2": {"token_allowance": 100000000},
    },
    # SambaNova's Free tier is metered per model, not per account.
    "sambanova": {
        "deepseek-v3-1": {"token_allowance": 200000, "rate_limits": SB_LIMITS},
        "llama-3-3-70b": {"token_allowance": 200000, "rate_limits": SB_LIMITS},
        "gpt-oss-120b": {"token_allowance": 200000, "rate_limits": SB_LIMITS},
        "deepseek-v3-2": {"token_allowance": 200000, "rate_limits": SB_LIMITS},
        "gemma-4-31b": {"token_allowance": 200000, "rate_limits": SB_LIMITS},
    },
}
MODEL_FIX = {
    "oracle-oci": ["command-r-plus", "llama-4-maverick"],
    "aws-bedrock": ["llama-4-maverick", "mistral-large-4", "command-r-plus"],
    "azure-ai-foundry": ["gpt-oss-120b", "llama-4-maverick", "mistral-small-4"],
    "ramp-router": ["gpt-oss-120b", "qwen3-8-27b", "glm-5-3-flash"],
}


def build_models(ids, provider_id=None):
    out = []
    for mid in ids:
        if isinstance(mid, dict):
            out.append(mid)
            continue
        if mid == "cohere-embed":
            out.append({"id": "cohere-embed-v4", "name": "Embed v4", "family": "Cohere Embed"})
            continue
        if mid not in MODELS:
            raise SystemExit("unknown model id: " + mid)
        src = MODELS[mid]
        m = {"id": src["id"], "name": src["name"], "family": src["family"]}
        if src.get("context_window"):
            m["context_window"] = src["context_window"]
        metrics = {}
        tps = tps_for(provider_id, mid, src.get("tps"))
        if tps is not None:
            metrics["tps"] = tps
        if src.get("intelligence") is not None:
            metrics["intelligence"] = src["intelligence"]
        if metrics:
            m["metrics"] = metrics
        out.append(m)
    return out


def main():
    dry = "--dry-run" in sys.argv
    manifest_path = os.path.join(DATA, "providers.json")
    manifest = json.load(open(manifest_path, encoding="utf-8"))
    listed = set(manifest["providers"])
    added = []
    for row in PART_A + PART_B + PART_C + PART_D + PART_E + PART_F + PART_G + PART_H + PART_I + PART_J + PART_K + PART_L + PART_M + PART_N + PART_O + PART_P + PART_Q + PART_R + PART_S + PART_T + PART_U + PART_V + PART_W:
        (pid, name, site, offer_code, offer_label, priv_code, priv_label, card,
         desc, overview, bullets, mids, notes) = row[:13]
        if pid in SKIP:
            continue
        models = build_models(MODEL_FIX.get(pid, mids), pid)
        if pid == "inception":
            for m in models:
                m["rate_limits"] = MERCURY_LIMITS
        for m in models:
            m.update(MODEL_EXTRA.get(pid, {}).get(m["id"], {}))
        if not models:
            raise SystemExit("no models for " + pid)
        offer_type, tone = OFFER[offer_code]
        entry = {
            "id": pid,
            "name": name,
            "website": site,
            "docs": site,
            "signup": site,
            "description": desc,
            "overview": overview,
            "offer": {"type": offer_type, "label": offer_label, "tone": tone},
            "privacy": {"type": PRIVACY[priv_code]},
            "requires_payment_card": card,
            "last_updated": CHECKED,
            "verified": {"checked": CHECKED, "sources": SOURCES.get(pid, [site, SOURCE_SNAPSHOT])},
            "free_access": bullets,
        }
        if priv_label:
            entry["privacy"]["label"] = priv_label
        else:
            entry["privacy"]["label"] = "Privacy not documented"
        if notes:
            entry["notes"] = notes
        entry.update(PROVIDER_EXTRA.get(pid, {}))
        entry["models"] = models
        if dry:
            print("would write", pid, len(models), "models")
        else:
            with open(os.path.join(DATA, pid + ".json"), "w", encoding="utf-8") as fh:
                json.dump(entry, fh, indent=2, ensure_ascii=False)
                fh.write("\n")
        if pid + ".json" not in listed:
            manifest["providers"].append(pid + ".json")
            added.append(pid)
    if not dry:
        with open(manifest_path, "w", encoding="utf-8") as fh:
            json.dump(manifest, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
    print("new providers:", len(added), "manifest size:", len(manifest["providers"]))


if __name__ == "__main__":
    main()
