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

> 🚨 **OVERRIDE — VERIFIED FUNNEL CONFLICT**
> De budget aanbevelingen in de Ads Report / SYBB / Auto-Optimize secties hieronder zijn gebaseerd op Meta pixel data en conflicteren met de verified Wix order funnel. Volg ALLEEN de 'BUDGET AANBEVELINGEN (VERIFIED)' sectie verderop in dit rapport.
>
> ❌ **H12** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 155,80 spend. Negeer dat advies.
> ❌ **H14** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 122,96 spend. Negeer dat advies.
> ❌ **H15** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 52,15 spend. Negeer dat advies.
>
> **Top verified performer:** H13 · ROAS 2.05x · 1 order(s) · EUR 423,50 revenue.


## Meta Ads Rapport — 2026-04-22

**Periode:** last_30d (2026-03-23 t/m 2026-04-21) · **Status:** geen actieve campagnes, data is van twee recent gepauzeerde SYBB campagnes.

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|------:|------------:|-------:|----:|----:|----:|------:|-----:|
| 2026: SYBB | PAUSED | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 6 | n.v.t. (pixel datafout) ⚠︎ |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |

⚠︎ROAS n.v.t. (pixel datafout) komt uit €44.247 conversion value op ? purchases (verifieer Wix) (gem. €7.374/order). Zeer waarschijnlijk een tracking-artefact (duplicate pixel fires of verkeerde Shopify price mapping). Verifieer in Shopify vóór beslissingen.

### Underperformers

- **2026: SYBB** — CPC €0,55 (drempel €0,50) → lichte overschrijding. Sterkere hook testen bij relaunch.
- **2026: SYBB - Kopie** — CPC €0,64 en CPM €16,34 (beide boven drempel) → te klein voor harde conclusies, vermoedelijk audience-overlap met hoofdcampagne.
- **2026: SYBB funnel** — LPV → view_content 10,4%. Pixel-events firen niet betrouwbaar; eerst fixen voor relaunch.

### Top performers

- **Beste CTR**: 2026: SYBB - Kopie — 2,6%
- **Laagste CPC**: 2026: SYBB — €0,55
- **Beste ROAS**: 2026: SYBB — n.v.t. (pixel datafout) (onder voorbehoud van verificatie)

### Samenvatting

- **Totaal spend (30d)**: €1.183,89
- **Beste**: 2026: SYBB — volume, engagement en (mits geverifieerd) ROAS.
- **Slechtste**: 2026: SYBB - Kopie — duur, geen purchases, waarschijnlijk audience-overlap.
- **Aanbeveling (70-20-10)**: eerst tracking fixen (pixel events + purchase value), dan 2026: SYBB reactiveren met +25%/3d budget, 2-3 hook-variaties erbij als 20%, en 10% naar één nieuwe angle. Niet opnieuw de hele campagne kopiëren.

### Google Sheet

Overgeslagen — Google MCPs uitgeschakeld in deze run conform instructie. Rapport lokaal opgeslagen naar `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-04-22_ads_report.md`.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-21_sybb_report.md`.

**Kernbevindingen:**
- Campagne "2026: SYBB" (id `120239435987290239`) staat PAUSED sinds 19 april. Gisteren dus €0 spend, 0 clicks, 0 impressions.
- PostHog bevestigt 0 pageviews op www.startyourballoonbusiness.com op 21 april (confirmatie dat zonder ads geen traffic komt).
- 7d baseline (14-20 apr): CPC €0,62 (+24% boven target), bounce rate 84,1% (ver boven <55% target), ? purchases (verifieer Wix) (€1.473,50 revenue), CTR 2,23% gezond.
- Scroll depth tracking ontbreekt volledig in PostHog, blinde vlek voor engagement-diagnose.

**Top 3 acties:** 1) Beslis over campagne-status (heropen of documenteer pauze), 2) Diagnose bounce rate 84% met hero/ad-mismatch review in Wix, 3) Scroll depth tracking installeren in PostHog.

Geen Google MCPs gebruikt, alleen Pipeboard Meta Ads en PostHog.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-22_auto_optimize.md`.

**Kernbevindingen:**
- **0 ads gepauzeerd** (Niveau 1). Alle 5 campagnes op act_567892422940728 staan al op PAUSED, account act_1489853856181844 heeft geen campagnes, en act_607231713057715 is niet bereikbaar met deze token.
- Twee SYBB campagnes draaiden in de last_3d window (recent gepauzeerd). Beide ruim boven kill-drempels:
  - **2026: SYBB - Kopie**: Link CTR 1,6%, CPC link €1,00, 6 ICs (€2.100) op €124 spend.
  - **2026: SYBB**: Link CTR 1,3%, CPC link €1,22, 2 ICs op €44 spend.
- Waarschuwing: CPM ~€16 op beide → audience iets verbreden bij re-launch.

**4 voorstellen wachten op goedkeuring:** (1) re-launch SYBB - Kopie €40-€60/dag, (2) SYBB original heractiveren €15-€20/dag, (3) audience verbreden tegen hoog CPM, (4) hook-variatie test. Geef aan welke nummers je wilt uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 1 | 1 (EUR 350,00) | EUR 350,00 | 0.67x | EUR 521,56 |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 1 (EUR 423,50) | EUR 423,50 | 2.05x | EUR 207,00 |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.059,47** | **1036** | **1** | **2** | **EUR 773,50** | **0.73x** | **EUR 529,74** |

> **CROSS-REFERENCE: Meta Pixel vs Wix Orders**
> - Meta pixel: 18 purchases (EUR 132.741,00)
> - Wix orders: 2 orders (EUR 773,50)
> - Verschil: +16 pixel purchases, +EUR 131.967,50 pixel waarde
> - **Verdict: PIXEL OVERSTELT.** Gebruik Wix orders als bron van waarheid.
> - Mogelijke oorzaken: Conversions API duplicaten, test purchases, cross-domain pixel fires

> **ONGEMATCHTE /thank-you SESSIES:**
> - Sessie op 2026-04-18, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

**Ranking op Verified ROAS:**

| Rank | Ad | Verified ROAS | Wix Orders | Revenue | Spend | Advies |
|---|---|---|---|---|---|---|
| 🥇 | H13,B3,CTA5 | 2.05x | 1 | EUR 423,50 | EUR 207,00 | **70% budget** — hoogste verified ROAS · NIET pauzeren |
| 🥈 | H11, B3, CTA5 | 0.67x | 1 | EUR 350,00 | EUR 521,56 | 20% budget — tweede verified winner · houd actief |
| — | H12,B3,CTA5 | 0 orders | 0 | — | EUR 155,80 | NIET als best performer labelen · 0 Wix orders ondanks EUR 155,80 spend · heroverweeg |
| — | H14,B3,CTA5 | 0 orders | 0 | — | EUR 122,96 | NIET als best performer labelen · 0 Wix orders ondanks EUR 122,96 spend · heroverweeg |
| — | H15,B3,CTA5 | 0 orders | 0 | — | EUR 52,15 | NIET als best performer labelen · 0 Wix orders ondanks EUR 52,15 spend · heroverweeg |

**Verified funnel regels (hard):**
- Top verified performer: **H13** (verified ROAS 2.05x, 1 Wix order(s), EUR 423,50 revenue).
- H13 mag NIET gepauzeerd worden en krijgt 70% van het budget.
- Ads zonder verified orders (H12, H14, H15) mogen NIET als 'beste performer' of 'winner' gelabeld worden, ongeacht Meta pixel CTR/IC/purchase cijfers.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
