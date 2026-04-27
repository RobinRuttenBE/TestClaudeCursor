# Morning Report — 2026-04-26

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

Ik kan het rapport nu niet genereren met live data. Hier is wat er aan de hand is:

**Blokkers:**
- **Meta Ads MCP (Pipeboard)** — niet geauthenticeerd. Tools zoals `get_ad_accounts`, `get_campaigns`, `get_insights`, `get_ads` zijn niet beschikbaar tot je de OAuth flow afrondt.
- **PostHog MCP** — niet geladen in deze sessie. Geen tools voor pageviews, bounce rate, CTA clicks etc.

De strikte regel voor deze run sluit Google MCPs (Sheets/Drive/GA4) en alle andere bronnen uit, dus ik heb geen alternatieve databron.

**Actie nodig van jou:**

1. Open deze URL in je browser om Pipeboard Meta Ads te autoriseren:

   https://pipeboard.co/oauth/authorize?response_type=code&client_id=f02ce0c1ed6d5c6e8b6b52ebb1c2c101&code_challenge=1UUuwNVTZBbkIn44iJuZbhiqPkF26_LbIdzxrO7uVNk&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A55426%2Fcallback&state=bP87qLjhruG5uLJ2rG8hpGpq-aLc0Tbi27CJFlD6QWU&scope=mcp%3Aread+mcp%3Awrite+mcp%3Aadmin+claudeai&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

2. Als de redirect-pagina een connection error toont, plak de volledige URL uit je adresbalk hier — dan rond ik de auth af.

3. Voor PostHog: laat weten of de MCP geconfigureerd moet worden, of dat ik dit rapport mag draaien zonder PostHog cross-reference (alleen Meta Ads data).

Zodra Pipeboard geautoriseerd is, draai ik het rapport en sla op naar `Output/Reports/Daily/2026-04-26_ads_report.md`.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-25_sybb_report.md`.

**Kernpunten:**
- Vijfde pauzedag op rij voor beide SYBB campagnes. "2026: SYBB - Kopie" PAUSED sinds 2026-04-20 17:09, "2026: SYBB" PAUSED sinds 2026-04-19 14:29. Nul spend, nul impressies, nul clicks op 2026-04-25.
- 7d run-dagen aggregaat gekrompen van 4 naar 3 run-dagen (04-17 valt uit het venster); morgen valt 04-18 ook weg.
- PostHog MCP zeven rapportdagen op rij offline, geen landing page health beschikbaar.
- Top actie: vandaag definitieve beslissing vastleggen (heractiveren / rebuild + datum / kill) voordat het 7d-venster volledig leeg loopt op 2026-04-28.

Geen Google MCPs aangeroepen. Alle Meta-cijfers direct uit `get_insights` met dag-breakdown.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-26_auto_optimize.md`.

**Samenvatting:**
- **0 automatische acties uitgevoerd** — er zijn geen actieve campagnes om te optimaliseren
- **act_567892422940728**: alle 5 campagnes staan PAUSED. De hoofd-campagne `2026: SYBB` is sinds 2026-04-19 gepauzeerd; een duplicaat `2026: SYBB - Kopie` is op 2026-04-20 aangemaakt (ook PAUSED)
- **act_1489853856181844**: geen campagnes aanwezig
- **act_607231713057715**: token heeft geen toegang tot dit account

Geen Google MCPs aangeroepen, geen Sheets writes uitgevoerd. Voorstellen in het rapport vragen om beslissing over relaunch-planning en eventuele tijdelijke skip van auto-optimize in het morning report.

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
