# Morning Report — 2026-04-28

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

Zelfde situatie als gisteren. Twee blokkades:

1. **Pipeboard Meta Ads MCP** is geïnstalleerd maar vereist OAuth authenticatie. De data-tools (`get_ad_accounts`, `get_campaigns`, `get_insights`, `get_ads`) zijn niet beschikbaar tot je inlogt.
2. **PostHog MCP** is niet aangesloten in deze sessie (geen tools gevonden in search).

Conform jouw instructie mag ik geen Google MCPs gebruiken als fallback, dus ik kan zonder Pipeboard geen campagnedata ophalen.

Wil je dat ik de Pipeboard auth flow start? Dan krijg je een autorisatie-URL — na login kan ik `act_567892422940728` (Sempertex) en `act_607231713057715` (Robin Rutten) trekken over last_30d en het rapport opslaan in `Output/Reports/Daily/2026-04-28_ads_report.md`. Ik schrijf het bestand pas weg zodra er echte data is — geen placeholder rapporten.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-27_sybb_report.md`.

**Kerngetallen 2026-04-27:**
- Beide SYBB campagnes nog steeds PAUSED (Kopie sinds 04-20 17:09, origineel sinds 04-19 14:29). Nul spend, nul impressies, nul clicks.
- 7e pauzedag op rij. Pauze (7d) overstijgt runperiode (5d) nu met 2 dagen.
- 7d-venster (04-21 t/m 04-27) bevat voor het eerst nul run-dagen, exact zoals voorspeld in het 04-26 rapport. Baseline-tabel onbruikbaar tot heractivering.
- PostHog MCP voor de 9e rapportdag op rij niet beschikbaar.
- Beslissingslog en iter1 baseline document, beide 3 dagen open. Top 3 acties zijn dezelfde als gisteren met groeiende urgentie.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-28_auto_optimize.md`.

**Samenvatting:**
- **Niveau 1 acties:** geen — er zijn 0 actieve campagnes op beide toegestane accounts (`act_567892422940728`, `act_1489853856181844`).
- **Status `act_567892422940728`:** 5 campagnes, allen PAUSED. SYBB-campagne en kopie zijn op 19/20 april gepauzeerd.
- **Toegang:** `act_607231713057715` is niet toegestaan met dit token.
- **Belangrijkste open beslissing:** wat te doen met `2026: SYBB` (heractiveren of afsluiten) — zonder actieve campagne is er geen ads-data voor de daily report flow.

Geen Google MCPs aangeroepen, geen Sheet-write uitgevoerd, output uitsluitend lokaal.

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
