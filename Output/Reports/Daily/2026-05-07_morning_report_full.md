# Morning Report — 2026-05-07

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


## Meta Ads Rapport — 7 mei 2026

**Account:** Sempertex Ad Account · **Periode:** last_30d (2026-04-07 → 2026-05-06) · **Totaal spend:** €1.183,89

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq | Pur | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|------|-----|------|
| 2026: SYBB | PAUSED | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 2,19 | 6 | n.v.t. (pixel datafout) |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 1,42 | 0 | n.v.t. (pixel datafout) (op IC) |

> Geen actieve campagnes. Beide getoonde campagnes staan PAUSED maar hebben spend in de last 30d.

### Underperformers
- **H13, B3, CTA5 (SYBB - Kopie · Kopie 3)** — CPC €0,93 + CPM €19,14 → **pauzeer**
- **H11, B3, CTA5 (SYBB · Kopie 1)** — CPC €0,67 maar ? purchases (verifieer Wix) (ROAS ~57x) → **niet pauzeren**, dupliceren naar nieuw publiek
- **H12, B3, CTA5 (SYBB · Kopie 2)** — €141 spend, ? purchases (verifieer Wix) → targeting aanscherpen of pauzeren
- **H14, B3, CTA5 (SYBB · BATCH 2)** — beste CPM (€7,43) maar 0 conversies bij 108 LPVs → landing page mismatch onderzoeken

### Top performers
- **Beste CTR**: H15 (BATCH 2) — 6,4% (kleine sample)
- **Laagste CPC**: H15 (BATCH 2) — €0,23
- **Beste ROAS**: H13 (Kopie 3) — ~71x · **Hoogste volume**: H11 (Kopie 1) — ? purchases (verifieer Wix)
- **Laagste CPM**: H14 (BATCH 2) — €7,43

### Aanbeveling (70-20-10)
- **70%** — Reactiveer en scale H11 (Kopie 1) en H13 (Kopie 3) met +50% budget. Enige 2 ads met purchases.
- **20%** — Bouw 2 hook-variaties op H11.
- **10%** — Geef H15 €100 budget om te valideren of CTR 6,4% vasthoudt.
- **Verificatie eerst**: pixel purchase value (€7.374 gem.) lijkt hoog voor SYBB workshop — check of pixel correct getriggerd is voordat je opschaalt.

### Output
- Rapport opgeslagen: `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-07_ads_report.md`
- Google Sheet write **geskipt** per instructie (geen Google MCPs aangeroepen).

> **Wil je funnel data toevoegen?** Geef dan landing page metrics uit Wix Analytics of GA4: visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik er een `/funnel-diagnose` overheen.

---

Rapport opgeslagen op `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-06_sybb_report.md`.

Kerncijfers 6 mei 2026:
- **Meta Ads SYBB:** PAUSED sinds 19 april — €0 spend, 0 impressions/clicks gisteren én de 7d ervoor.
- **Landing page:** 4 PVs / 2 visitors / 2 sessies, beide via bio-link (Instagram 13:32, Facebook 18:38), gem. 75s op pagina.
- **Funnel signaal:** 1 van de 2 sessies klikte door naar `/checkout` (geen `purchase` event gevolgd).
- **Top 3 acties:** (1) ga/no-go besluit op campagne reactiveren (H11+H13 +50% per ads-rapport van 7 mei), (2) fix scroll-depth en CTA-event tracking op de LP, (3) onderzoek de `/checkout`-sessie op pixel-fire.

Twee data-gaten waar ik tegenaan liep en die deze rapportage permanent zwakker maken zolang ze er zijn: scroll depth wordt niet getrackt op de LP, en CTA clicks zijn niet als named events gedefinieerd.

---

Klaar.

**Resultaat:** Geen actieve campagnes op `act_567892422940728` of `act_1489853856181844`. `act_607231713057715` is niet toegankelijk voor de huidige token. Spend en impressions over last_3d zijn nul, dus geen kill-regels getriggerd, geen 70-20-10 classificatie en geen budget-voorstellen mogelijk.

**Output:** `Output/Reports/Daily/2026-05-07_auto_optimize.md` (gecommit en gepusht).

**Open beslissingen voor jou:**
1. SYBB campagne `120239435987290239` herstarten met de nieuwe link-metrics drempels, of archiveren?
2. Token-toegang voor `act_607231713057715` regelen, of dat account uit het command halen?

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
