# Morning Report — 2026-05-09

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,17%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,04** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 90,62** over 11 actieve dagen (niet totaal/30)
> - Bron: spend EUR 996,81 · impressions 81.409 · link_clicks 956
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H12,B3,CTA5 | EUR 14,37 | 1.058 | 20 | 1,89% | EUR 0,72 |
> | H13,B3,CTA5 | EUR 0,01 | 1 | 0 | 0,00% | EUR 0,00 |
> | H14,B3,CTA5 | EUR 60,30 | 6.121 | 78 | 1,27% | EUR 0,77 |
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
> ❌ **H13** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 207,00 spend. Negeer dat advies.
> ❌ **H12** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 155,80 spend. Negeer dat advies.
> ❌ **H14** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 60,30 spend. Negeer dat advies.
> ❌ **H15** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 52,15 spend. Negeer dat advies.
>
> **Top verified performer:** H11 · ROAS 0.67x · 1 order(s) · EUR 350,00 revenue.


## Meta Ads Rapport — 9 mei 2026

**Status: GEEN ACTIEVE CAMPAGNES**
Geen actieve campagnes in `act_567892422940728` (Sempertex) of `act_1489853856181844`. Account `act_607231713057715` is niet toegankelijk met huidige API token. Hieronder de meest recente gepauzeerde campagnes met hun laatste performance data.

### Overzicht per campagne

| Campagne | Status | Periode | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|---------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | PAUSED | last_30d | €996,81 | 81.409 | 1.782 | 2,2% | €0,56 | €12,24 | 6 | n.v.t. (pixel datafout)* |
| Campagne Nozzle Up 2025 1 | PAUSED | lifetime | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | n.v.t. (pixel datafout) |
| Last push Nozzle Up | PAUSED | lifetime | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | n.v.t. (pixel datafout) |
| Nozzle Up END OF AUGUST | PAUSED | lifetime | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | n.v.t. (pixel datafout) |
| 2026: SYBB - Kopie | PAUSED | last_30d | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |

*Pixel value voor 2026: SYBB lijkt inflated (€7.374 per purchase). Behandel als directioneel signaal.

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 + CPM €16,34 + ? purchases (verifieer Wix) bij 6 checkouts → niet apart reactiveren, mergen met hoofdvariant.
- **2026: SYBB** — CPC €0,56 marginaal boven €0,50 drempel → test sterkere openers.
- **Last push Nozzle Up** —ROAS n.v.t. (pixel datafout) (3/236 checkout-completion = 1,3%) → bottleneck zit op checkout, niet op ad.
- **Nozzle Up END OF AUGUST** — CTR 0,99% (marginaal onder 1%) → brede targeting, niet repeteren voor SYBB-audiences.

### Top performers
- **Beste CTR (volume)**: Nozzle Up 2025 1 / Last push Nozzle Up — 2,5%
- **Laagste CPC**: Nozzle Up END OF AUGUST — €0,17
- **Beste full-funnel performer**: Campagne Nozzle Up 2025 1 — €0,26 CPC + ROAS n.v.t. (pixel datafout) + 329 checkouts.

### Samenvatting
- **Totaal spend last_30d (2026 SYBB)**: €1.121,23
- **Beste performer historisch**: Campagne Nozzle Up 2025 1 — schaalbare creatives.
- **Slechtste performer historisch**: Last push Nozzle Up — ad metrics goed, downstream probleem.
- **Aanbeveling (70-20-10)**:
  1. **70%**: Heractiveer Nozzle Up 2025 1 met dezelfde creatives.
  2. **20%**: Hook-variaties op de top-3 ads uit die campagne.
  3. **10%**: Test SYBB-hooks tegen de Nozzle Up audience.
  4. **Eerst diagnoseren**: Checkout drop-off (SYBB hoofd 18%, Last push 1,3%) is grootste leverage — run `/funnel-diagnose` zodra LP data beschikbaar is.

### Google Sheet
Niet weggeschreven (per instructie overgeslagen). Rapport opgeslagen op `Output/Reports/Daily/2026-05-09_ads_report.md`.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen in `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-08_sybb_report.md`.

**Belangrijkste bevinding:** Campagne `2026: SYBB` staat sinds ~19 april op PAUSED (19 dagen). Op 8 mei dus €0 spend en 0 impressies. Landing page kreeg 2 pageviews uit residueel organisch verkeer, voornamelijk via Instagram/Facebook bio links. Alle landing-page ratio's (bounce, scroll, CTA) zijn niet betekenisvol meetbaar door te laag volume.

**Top 3 acties** (in rapport): (1) beslissing relaunchen of definitief afbouwen, (2) creative refresh klaarzetten voor relaunch (vorige CPC zat 24% boven target), (3) bio-link posts intensiveren om organische instroom te repareren.

Geen Google MCPs aangeroepen, geen schrijfacties naar de Tracker Sheet — alleen Meta Ads MCP en PostHog MCP gebruikt.

---

Auto-optimize uitgevoerd. Status: er zijn op `act_567892422940728` geen ACTIVE campagnes (alle 5 staan op PAUSED, de SYBB-campagne is ergens vóór 2026-04-25 stopgezet) en op `act_1489853856181844` bestaan geen campagnes. Dus geen kill-regels getriggerd, geen 70-20-10-classificatie en geen budget-voorstellen vandaag.

Het rapport bevat wel context over de laatste actieve campagne (SYBB lifetime: ROAS 0,44× / CPC (link) €1,04 / Link CTR 1,2%) en drie pre-launch voorstellen voor wanneer je SYBB weer aanzet. Opgeslagen in `Output/Reports/Daily/2026-05-09_auto_optimize.md`.

Wil je dat ik het bestand commit en push? (Auto-commit feedback staat in memory, maar dit is een nieuw rapport in een tracked map — kort vragen voor de zekerheid.)

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 1 | 1 (EUR 350,00) | EUR 350,00 | 0.67x | EUR 521,56 |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 60,30 | 78 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 996,81** | **956** | **1** | **1** | **EUR 350,00** | **0.35x** | **EUR 996,81** |

> **CROSS-REFERENCE: Meta Pixel vs Wix Orders**
> - Meta pixel: 18 purchases (EUR 132.741,00)
> - Wix orders: 1 orders (EUR 350,00)
> - Verschil: +17 pixel purchases, +EUR 132.391,00 pixel waarde
> - **Verdict: PIXEL OVERSTELT.** Gebruik Wix orders als bron van waarheid.
> - Mogelijke oorzaken: Conversions API duplicaten, test purchases, cross-domain pixel fires

> **ONGEMATCHTE /thank-you SESSIES:**
> - Sessie op 2026-04-26, utm_content=(geen utm_content)
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
| 🥇 | H11, B3, CTA5 | 0.67x | 1 | EUR 350,00 | EUR 521,56 | **70% budget** — hoogste verified ROAS · NIET pauzeren |
| — | H13,B3,CTA5 | 0 orders | 0 | — | EUR 207,00 | NIET als best performer labelen · 0 Wix orders ondanks EUR 207,00 spend · heroverweeg |
| — | H12,B3,CTA5 | 0 orders | 0 | — | EUR 155,80 | NIET als best performer labelen · 0 Wix orders ondanks EUR 155,80 spend · heroverweeg |
| — | H14,B3,CTA5 | 0 orders | 0 | — | EUR 60,30 | NIET als best performer labelen · 0 Wix orders ondanks EUR 60,30 spend · heroverweeg |
| — | H15,B3,CTA5 | 0 orders | 0 | — | EUR 52,15 | NIET als best performer labelen · 0 Wix orders ondanks EUR 52,15 spend · heroverweeg |

**Verified funnel regels (hard):**
- Top verified performer: **H11** (verified ROAS 0.67x, 1 Wix order(s), EUR 350,00 revenue).
- H11 mag NIET gepauzeerd worden en krijgt 70% van het budget.
- Ads zonder verified orders (H13, H12, H14, H15) mogen NIET als 'beste performer' of 'winner' gelabeld worden, ongeacht Meta pixel CTR/IC/purchase cijfers.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
