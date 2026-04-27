# Morning Report — 2026-04-27

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

Ik kan het rapport niet draaien zonder de data. Twee blokkades:

1. **Pipeboard Meta Ads MCP** is geïnstalleerd maar vereist OAuth authenticatie. De echte tools (`get_ad_accounts`, `get_campaigns`, `get_insights`, `get_ads`) zijn niet beschikbaar tot je inlogt.
2. **PostHog MCP** lijkt niet aangesloten in deze sessie. Hij komt niet terug in de tool search.

Wil je dat ik de Pipeboard auth flow start? Dan krijg je een autorisatie-URL die je in de browser opent, en daarna kan ik direct de data ophalen voor `act_567892422940728` en `act_607231713057715` over de afgelopen 30 dagen.

Voor PostHog: check even of die MCP actief is in je config, anders kan ik wel het Meta Ads gedeelte draaien zonder de PostHog cross-reference.

---

Rapport is klaar en gecommit/gepusht naar `Output/Reports/Daily/2026-04-26_sybb_report.md`.

**Korte samenvatting van wat erin staat:**
- Beide SYBB campagnes (`2026: SYBB` 120239435987290239 en `2026: SYBB - Kopie` 120243293329420239) staan op PAUSED, zesde volle pauzedag op rij. Op 2026-04-26 nul impressies, clicks en spend op beide.
- 7d window (04-19 t/m 04-25) heeft nog 2 run-dagen aan data: totaal €168,23 spend, 10.371 imp, 256 clicks, 161 link clicks, 8 IC, CTR 2,47%, CPC €0,66 over beide campagnes gecombineerd. Vanaf overmorgen is het 7d-aggregaat leeg.
- PostHog MCP is voor de achtste rapportdag op rij niet beschikbaar (geen `posthog_*` tools in de deferred tool lijst), dus geen landing page health en geen cross-reference.
- 3 acties: (1) beslissingslog vandaag aanmaken (heractiveren / rebuild / kill), (2) PostHog MCP herstellen, (3) iter-1 baseline vastleggen voor het 7d-venster leeg loopt.
- Geen Google MCPs aangeroepen, geen schrijfactie naar de Meta Ads Tracker Google Sheet.

Wil je dat ik /schedule een herinnering aanzet voor over 3 dagen om de SYBB beslissing op te volgen als die vandaag niet wordt vastgelegd?

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-27_auto_optimize.md`.

**Samenvatting:**
- **0 ads gepauzeerd** — er zijn geen actieve campagnes/adsets/ads op de toegankelijke accounts. Kill-regels niet van toepassing.
- Hoofdcampagne **2026: SYBB** (act_567892422940728) staat sinds **2026-04-19 PAUSED** met €100/dag budget nog ingesteld; alle 6 adsets en 26 ads PAUSED.
- Tweede toegestane account `act_1489853856181844` heeft 0 actieve campagnes.
- `act_607231713057715` (genoemd in commando) is **niet toegankelijk** met de huidige Pipeboard token.
- 70-20-10 classificatie niet uitvoerbaar bij nul actieve ads.
- Drie open strategische beslissingen geformuleerd: (1) heractiveer of sluit SYBB, (2) refresh creatives vóór heractivatie, (3) los token-scope op voor het ontbrekende account.

Geen Google MCPs aangeroepen, geen schrijfacties naar de tracker Google Sheet — uitsluitend Meta Ads MCP gebruikt en lokaal markdown weggeschreven.

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
