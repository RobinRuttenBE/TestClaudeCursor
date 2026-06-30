# Morning Report — 2026-06-29

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Request timed out

---

Ik kan dit rapport op dit moment **niet** genereren, omdat allebei de vereiste databronnen onbereikbaar zijn. Ik heb de MCP-serverstatus gecheckt en dit is wat er aan de hand is:

## 🔴 Blokkade: beide databronnen liggen plat

| Databron | Status | Probleem |
|----------|--------|----------|
| **Pipeboard Meta Ads** (`pipeboard-meta-ads`, token) | ⚠️ Connected · **tools fetch failed** | Server verbindt wel, maar levert geen tools/data |
| **Pipeboard Meta Ads** (`claude.ai` variant) | ⚠️ **Needs authentication** | Niet ingelogd |
| **PostHog** (`posthog`, SSE) | ✘ **Failed to connect** | Verbinding mislukt volledig |

Ik heb meermaals gezocht naar de Meta Ads- en PostHog-tools; ze zijn niet beschikbaar omdat de servers geen tools teruggeven.

## Waarom ik nu stop in plaats van doorga
- Ik heb **geen Meta Ads cijfers** (spend, impressions, clicks, CTR, CPC, frequency) en **geen PostHog data** (pageviews, bounce, scroll depth, funnel).
- Jouw strikte regel verbiedt de Google MCPs als alternatieve bron — terecht, want die bevatten deze data sowieso niet.
- Het alternatief zou zijn cijfers verzinnen, en dat doe ik niet. Een SYBB-rapport met gefabriceerde data is erger dan geen rapport.

## Wat er moet gebeuren om dit te fixen
1. **PostHog reconnecten** — de SSE-verbinding (`https://mcp.posthog.com/sse`) faalt. Meestal opgelost door opnieuw te authenticeren / de MCP-auth te vernieuwen.
2. **Pipeboard Meta Ads opnieuw authenticeren** — de token-server geeft "tools fetch failed", de claude.ai-variant "needs authentication". Pipeboard moet opnieuw ingelogd worden (token mogelijk verlopen).

Zodra één of beide weer "Connected" zijn met werkende tools, zeg je het maar en draai ik het rapport voor 2026-06-28 direct.

Wil je dat ik:
- **(a)** wacht en het over een paar minuten opnieuw probeer (soms herstellen de MCP-servers vanzelf), of
- **(b)** je begeleid bij het opnieuw verbinden van PostHog en Pipeboard?

---

Klaar. Hier is de samenvatting:

## Auto-Optimize Rapport — 29 June 2026

**Belangrijkste bevinding: er zijn geen actieve campagnes om te optimaliseren.**

| Account | Status |
|---------|--------|
| `act_567892422940728` (primair) | ✅ Toegankelijk — maar **0 actieve campagnes**, alle 5 staan op PAUSED |
| `act_607231713057715` (secundair) | ❌ Token heeft geen toegang |

**Acties:**
- ⚡ **0 ads gepauzeerd** — geen actieve ads om tegen de kill-regels (Link CTR < 0.8%, CPC link > €1.50) te toetsen
- ⚠️ Geen waarschuwingen, geen 70-20-10 classificatie, geen budgetvoorstellen — allemaal niet van toepassing zonder live ads

**Twee operationele aandachtspunten:**
1. De `2026: SYBB` campagne (dagbudget €100,00) is de meest recente live SYBB-campagne en staat nu op PAUSED. Zodra die weer actief is (en ≥24u loopt), draait deze run automatisch de volledige analyse.
2. Het Pipeboard-token mist toegang tot `act_607231713057715`. Het heeft wél toegang tot `act_1489853856181844` — dat account staat niet in dit command. Laat weten of dat relevant is, of herauthoriseer de Meta-connectie als het secundaire account meegenomen moet worden.

Rapport opgeslagen in `Output/Reports/Daily/2026-06-29_auto_optimize.md` en gepusht naar GitHub. Conform de strikte regel zijn alleen de Meta Ads MCP gebruikt, geen Google MCPs en niets naar de Google Sheet geschreven.

Wil je dat ik de `2026: SYBB` campagne weer activeer zodat de optimalisatie iets te doen heeft?

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
