# Morning Report — 2026-05-06

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
> ❌ **H13** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 207,00 spend. Negeer dat advies.
> ❌ **H12** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 155,80 spend. Negeer dat advies.
> ❌ **H14** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 122,96 spend. Negeer dat advies.
> ❌ **H15** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 52,15 spend. Negeer dat advies.
>
> **Top verified performer:** H11 · ROAS 0.67x · 1 order(s) · EUR 350,00 revenue.


## Meta Ads Rapport — 6 May 2026

> Status: **GEEN actieve campagnes** op `act_567892422940728` (Sempertex Ad Account). `act_607231713057715` is niet toegankelijk met deze token. `act_1489853856181844` is leeg. Onderstaand de **5 meest recente gepauzeerde campagnes**.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Periode | Spend | Impr. | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026: SYBB | PAUSED | last_30d | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 6 | n.v.t. (pixel datafout) |
| Campagne Nozzle Up 2025 1 | PAUSED | lifetime | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | n.v.t. (pixel datafout) |
| Nozzle Up END OF AUGUST | PAUSED | lifetime | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | n.v.t. (pixel datafout) |
| 2026: SYBB - Kopie | PAUSED | last_30d | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |
| Last push Nozzle Up | PAUSED | last_90d | — | — | — | — | — | — | — | — |

### Underperformers

- **2026: SYBB - Kopie** — CPC €0,64 (>€0,50), CPM €16,34 (>€15). ? purchases (verifieer Wix) op €124 spend. Niet relaunchen as-is.
- **2026: SYBB** — CPC €0,55 (>€0,50). CTR gezond (2,1%). Bidstrategie aanscherpen bij relaunch.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (op de grens). CPM extreem laag (€1,64). Hooks aanscherpen voor volgende run.
- Geen frequency-fatigue: alles <3,5.

### Top performers

- **Beste CTR**: 2026: SYBB - Kopie — 2,6% (kleine sample)
- **Laagste CPC**: Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS**: 2026: SYBB — n.v.t. (pixel datafout) (mogelijk vertekend door uitschieter, slechts ? purchases (verifieer Wix))
- **Sterkste totaalbalans**: Campagne Nozzle Up 2025 1 — CTR 2,5% + CPC €0,26 +ROAS n.v.t. (pixel datafout)

### Samenvatting

- **Totaal spend**: €2.641,11 over alle gerapporteerde campagnes
- **Totaal purchases gerapporteerd**: 18, totaal action_values €55.177,25
- **Beste performer**: Campagne Nozzle Up 2025 1 — meest realistische balans, grootste click-volume
- **Slechtste performer**: 2026: SYBB - Kopie — duurste CPC en CPM, ? purchases (verifieer Wix)
- **Aanbeveling (Hormozi 70-20-10)**:
  1. **70%**: relaunch creatives en hooks uit "Campagne Nozzle Up 2025 1"
  2. **20%**: hookvariaties op 2026: SYBB origineel
  3. **10%**: nieuwe hook op een nog ongeteste SYBB pillar
- **Kritisch**: er draait nu niets. Prioriteit deze week is 1 live campagne op basis van de Nozzle Up winning formula.

### Google Sheet

[Status: overgeslagen volgens runtime-instructie — opgeslagen in `Output/Reports/Daily/2026-05-06_ads_report.md`]

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen op `Output/Reports/Daily/2026-05-05_sybb_report.md` en gepusht naar GitHub.

**Korte samenvatting:**
- **Meta Ads:** Campagne `2026: SYBB` (ID 120239435987290239) staat al minstens 7 dagen PAUSED → €0 spend, geen impressies, geen klikken op 2026-05-05.
- **PostHog:** 8 pageviews uit 6 sessies (vs 7d gemiddelde van 3,86 pv). Bounce rate 66,7%, avg sessieduur 113s. Eén complete CTA flow: homepage → "Book Your Spot" → /checkout → "Continue" klik. Scroll depth blijft zwak (16,7% bereikt 25%+).
- **Anomalie:** UTM `h13_b3_cta5` gaf 1 sessie op een dag dat de campagne paused was, dus controleer of er ergens nog ads/retargeting actief zijn.
- **Top actie:** beslis of campagne herstart wordt, of nieuwe strategie/creatives nodig zijn. Onderzoek de /checkout sessie van gisteren via recording (sessie ID `019df75b-9edf-7cf1-8cdd-d14bd71a9839`).

---

Klaar. Rapport opgeslagen op `Output/Reports/Daily/2026-05-06_auto_optimize.md` en gepushed.

**Bevindingen:**
- Alle 5 campagnes in `act_567892422940728` staan op `PAUSED` (waaronder `2026: SYBB` sinds 2026-04-19, ~17 dagen).
- `act_1489853856181844` is leeg.
- `act_607231713057715` is genoemd in het command maar het Pipeboard-token heeft er geen toegang toe.
- Geen spend/impressies/clicks in `last_3d` → 0 kill-regel evaluaties, 0 voorstellen, 0 acties.

**Open beslissingen voor jou:**
1. SYBB relaunch-timing of expliciet open-eindig laten (en dat ergens noteren zodat dagelijkse rapporten niet leeg blijven).
2. `act_607231713057715` toegang regelen, of die referentie uit `.claude/commands/ads-auto-optimize.md` halen.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 1 | 1 (EUR 350,00) | EUR 350,00 | 0.67x | EUR 521,56 |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.059,47** | **1036** | **1** | **1** | **EUR 350,00** | **0.33x** | **EUR 1.059,47** |

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
| — | H14,B3,CTA5 | 0 orders | 0 | — | EUR 122,96 | NIET als best performer labelen · 0 Wix orders ondanks EUR 122,96 spend · heroverweeg |
| — | H15,B3,CTA5 | 0 orders | 0 | — | EUR 52,15 | NIET als best performer labelen · 0 Wix orders ondanks EUR 52,15 spend · heroverweeg |

**Verified funnel regels (hard):**
- Top verified performer: **H11** (verified ROAS 0.67x, 1 Wix order(s), EUR 350,00 revenue).
- H11 mag NIET gepauzeerd worden en krijgt 70% van het budget.
- Ads zonder verified orders (H13, H12, H14, H15) mogen NIET als 'beste performer' of 'winner' gelabeld worden, ongeacht Meta pixel CTR/IC/purchase cijfers.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
