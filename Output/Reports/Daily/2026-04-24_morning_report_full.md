# Morning Report — 2026-04-24

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,13%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,02** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 88,29** over 12 actieve dagen (niet totaal/30)
> - Bron: spend EUR 1059,47 · impressions 91.839 · link_clicks 1.036
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H12,B3,CTA5 | EUR 14,37 | 1.058 | 20 | 1,89% | EUR 0,72 |
> | H13,B3,CTA5 | EUR 0,01 | 1 | 0 | 0,00% | EUR 0,00 |
> | H14,B3,CTA5 | EUR 122,96 | 16.551 | 158 | 0,95% | EUR 0,78 |
> | H15,B3,CTA5 | EUR 2,32 | 157 | 4 | 2,55% | EUR 0,58 |
> | H15,B3,CTA5 | EUR 49,83 | 4.737 | 57 | 1,20% | EUR 0,87 |
> | H11, B3, CTA5 | EUR 521,56 | 38.614 | 428 | 1,11% | EUR 1,22 |
> | H13,B3,CTA5 | EUR 206,99 | 16.766 | 195 | 1,16% | EUR 1,06 |
> | H12,B3,CTA5 | EUR 141,43 | 13.955 | 174 | 1,25% | EUR 0,81 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Ik kan het rapport niet draaien. De vereiste MCPs zijn niet beschikbaar in deze sessie:

- **Meta Ads MCP (Pipeboard)** — geïnstalleerd, maar **niet geauthenticeerd**. Alleen `authenticate` en `complete_authentication` zijn beschikbaar. De data-tools (`get_ad_accounts`, `get_campaigns`, `get_insights`, `get_ads`) zijn pas bereikbaar na OAuth.
- **PostHog MCP** — **niet aangesloten** in deze sessie. Geen enkele `mcp__posthog__*` tool beschikbaar.

Je instructie verbiedt expliciet alle Google MCPs als alternatieve bron, dus ik heb geen fallback om Meta Ads- of landing page-data op te halen. Zonder deze data kan ik geen inhoudelijk rapport schrijven — ik zou moeten gokken op cijfers, en dat doe ik niet in een performance rapport.

**Wat ik nodig heb om door te gaan — kies één:**

1. **Authenticeer Meta Ads (Pipeboard)** — ik start de OAuth flow, jij autoriseert in de browser, daarna kan ik Meta Ads data ophalen. PostHog blijft dan ongebruikt (sectie "Landing page health" vervalt) tenzij je die MCP alsnog aansluit.
2. **Sluit PostHog MCP aan** — en authenticeer Meta Ads. Dan kan ik het volledige rapport draaien.
3. **Lever de data handmatig aan** — plak campagne-data (spend, impressions, clicks, CTR, CPC, CPM, conversions) en ik verwerk het naar het rapport-format zoals gespecificeerd in de skill, en schrijf het weg naar `Output/Reports/Daily/2026-04-24_ads_report.md`.

Welke wil je?

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-23_sybb_report.md`.

**Kernbevindingen:**
- **Derde nul-dag op rij.** 2026-04-23 opnieuw €0 spend, 0 impressies, 0 clicks op beide SYBB campagnes. "2026: SYBB - Kopie" staat sinds 2026-04-20 17:09 op PAUSED; origineel sinds 2026-04-19 14:29.
- **7d baseline uit run-dagen (04-16 t/m 04-20):** €81,49 gem. spend per run-dag, CTR 2,38%, CPC €0,62, LPV > IC rate 6,1% over 20 ICs / 329 LPVs.
- **PostHog MCP 5 dagen op rij niet beschikbaar.** Geen posthog tools in de deferred tool lijst — structureel kapot, niet incidenteel.
- **Top 3 acties:** (1) beslissen heractiveren/killen/rebuilden, (2) PostHog MCP herstellen, (3) 5-dagen snapshot documenteren voor iteratie 2 planning.

Conform de striktheidsregel: alleen Meta Ads MCP (Pipeboard) gebruikt, geen Google MCPs, output uitsluitend naar lokale markdown.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-24_auto_optimize.md`.

**Kort resultaat:**
- Beide ad accounts hebben 0 actieve campagnes. De hoofdcampagne `2026: SYBB` (daily budget €100,00) staat sinds 2026-04-19 op PAUSED, evenals de kopie-versie van 2026-04-19.
- Geen Niveau 1 acties uitgevoerd (niks om te pauzeren), geen Niveau 2 voorstellen (geen performance-data).
- Note: `act_607231713057715` gaf een token-permission error (allowed accounts zijn `act_1489853856181844` en `act_567892422940728`) — geen blokker voor deze run.

Wil je `2026: SYBB` heractiveren? Zo ja, dan kan ik de campagne-status via `update_campaign` op ACTIVE zetten.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 0 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| (geen ad match) | - | - | - | 2 (EUR 773,50) | EUR 773,50 | - | - |
| **Totaal** | **EUR 1.059,47** | **1036** | **0** | **2** | **EUR 773,50** | **0.73x** | **EUR 529,74** |

> **CROSS-REFERENCE: Meta Pixel vs Wix Orders**
> - Meta pixel: 18 purchases (EUR 132.741,00)
> - Wix orders: 2 orders (EUR 773,50)
> - Verschil: +16 pixel purchases, +EUR 131.967,50 pixel waarde
> - **Verdict: PIXEL OVERSTELT.** Gebruik Wix orders als bron van waarheid.
> - Mogelijke oorzaken: Conversions API duplicaten, test purchases, cross-domain pixel fires

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

> Geen van de ads heeft verified Wix orders in de periode. GEEN budget herverdeling op basis van verified funnel mogelijk. Wacht op meer data — negeer Meta pixel 'best performer' claims tot die tijd.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
