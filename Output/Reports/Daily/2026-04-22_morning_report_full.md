# Morning Report — 2026-04-22

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

De Pipeboard Meta Ads MCP server is niet geauthenticeerd, ik zie alleen `mcp__pipeboard-meta-ads__authenticate` en `mcp__pipeboard-meta-ads__complete_authentication`. De data tools (`get_ad_accounts`, `get_campaigns`, `get_insights`, `get_ads`) zijn pas beschikbaar nadat de OAuth flow is doorlopen.

Volgens jouw strikte regel mag ik geen Google MCPs gebruiken en geen andere data bronnen aanroepen. Zonder Meta Ads authenticatie kan ik geen echte campagne data ophalen.

Twee opties:

1. **Authenticeer Pipeboard nu** — ik start de OAuth flow, jij autoriseert in de browser, en ik haal dan live data op voor het rapport.
2. **Skip Meta Ads voor nu** — ik genereer een leeg/placeholder rapport met alleen het format en sla het op naar het opgegeven pad. Niet bruikbaar voor beslissingen.

Wil je dat ik de Pipeboard OAuth flow start (optie 1)?

---

Report saved. Key findings:

**Data status:**
- Meta Ads MCP (Pipeboard): werkend
- PostHog MCP: niet beschikbaar in deze sessie (geen posthog tools in deferred tool lijst)
- Geen Google MCPs aangeroepen

**Belangrijkste bevinding:** "2026: SYBB - Kopie" is op 2026-04-20 17:09 gepauzeerd en heeft op 2026-04-21 nul activiteit gedraaid. Het rapport bevat daarom geen fresh metrics voor gisteren, maar wel de cumulatieve 2-dagen variant ranking (H12 wint op CTR/CPC, H13 is pauzeer-kandidaat) en drie concrete acties: pauze-status bevestigen, PostHog MCP herstellen, na herstart 3+ dagen laten draaien.

Opgeslagen in: `Output/Reports/Daily/2026-04-21_sybb_report.md`

---

The local commit succeeded, but the push failed because `main` has diverged (40 local vs 34 remote) — that's a pre-existing state from the auto-sync cron, not something I should force-resolve. I'll leave it for the next auto-sync run.

## Samenvatting

Rapport opgeslagen in `Output/Reports/Daily/2026-04-22_auto_optimize.md`.

**Status: geblokkeerd** — tweede dag op rij.
- Pipeboard Meta Ads MCP niet geauthenticeerd (alleen `authenticate` / `complete_authentication` zichtbaar, geen data-tools).
- PostHog MCP tools niet geladen in deze sessie.
- Geen Google MCPs aangeroepen, geen writes naar Google Sheet — conform run-regel.
- **0 ads gepauzeerd, geen 70-20-10 classificatie, geen voorstellen** — alle oordelen zouden zonder verse Link CTR / CPC (link) / ROAS neerkomen op gokken.

**Commit:** lokaal gemaakt (`848ec60`), push geblokkeerd door pre-existing 40↔34 divergentie op `main`. De auto-sync cron pakt 'm bij de volgende run.

**Actie van jou nodig:** autoriseer Pipeboard via `/mcp` of open de OAuth-URL in het rapport, en herhaal dan `/ads-auto-optimize`. Check ook de €7.374,50-per-purchase pixel fout uit eerdere rapporten voordat ROAS-voorstellen weer meetellen.

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
