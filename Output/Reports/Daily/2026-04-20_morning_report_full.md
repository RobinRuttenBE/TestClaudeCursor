# Morning Report — 2026-04-20

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
> - Bron: spend EUR 1059,46 · impressions 91.838 · link_clicks 1.036
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
> | H11, B3, CTA5 | EUR 521,55 | 38.613 | 428 | 1,11% | EUR 1,22 |
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
> ❌ **Pauzeer H13** advies in dit rapport conflicteert met verified ROAS 2.05x. H13 is de top performer — NIET pauzeren.
> ❌ **H12** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 155,80 spend. Negeer dat advies.
> ❌ **H14** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 122,96 spend. Negeer dat advies.
> ❌ **H15** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 52,15 spend. Negeer dat advies.
>
> **Top verified performer:** H13 · ROAS 2.05x · 1 order(s) · EUR 423,50 revenue.


## Meta Ads Rapport — 2026-04-20

**Periode:** last_30d (2026-03-21 t/m 2026-04-19) · **Account:** Sempertex Ad Account

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. (IC) | ROAS (IC) |
|----------|--------|-------|-------------|--------|-----|-----|-----|------------|-----------|
| 2026: SYBB - Kopie | Active | €45,77 | 3.323 | 75 | 2,3% | €0,61 | €13,77 | 4 | n.v.t. (pixel datafout) |

*IC = initiate_checkout (geen purchase pixel fire gemeten; ROAS gebaseerd op checkout waarde €1.400)*

### Ad-level performance (actieve ads)

| Ad | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq | IC |
|----|-------|-------|--------|-----|-----|-----|------|-----|
| H11, B3, CTA5 | €23,10 | 1.807 | 40 | 1,11% | € 1,22 | €12,78 | 1,12 | 2 |
| H13, B3, CTA5 | €14,95 | 947 | 19 | 1,16% | € 1,06 | €15,79 | 1,07 | 1 |
| H12, B3, CTA5 | € 0,81 | 569 | 16 | 1,25% | € 0,81 | €13,57 | 1,21 | 1 |

### Underperformers
- **Campagne SYBB** — CPC €0,61 (drempel €0,50) → H13 trekt gemiddelde omhoog, herverdelen
- **H13** — CPC €0,79 én CPM €15,79 boven drempel → pauzeer, laagste CTR
- **H11** — CPC €0,58 net boven drempel, maar sterke CTR (2,2%) en 2 IC → laten draaien

### Top performers
- **Beste CTR:** H12 — 2,8%
- **Laagste CPC:** H12 — €0,48 (enige ad binnen alle drempels)
- **Beste ROAS (op IC):** H11 — n.v.t. (pixel datafout)

### Samenvatting
- **Totaal spend:** €45,77 (campagne live sinds 2026-04-19, dus feitelijk 1 dag data)
- **Beste performer:** H12 — laagste CPC, hoogste CTR, alles binnen drempels
- **Slechtste performer:** H13 — CPC 58% boven drempel, CPM boven drempel
- **Aanbeveling (70-20-10):** pauzeer H13, schuif budget naar H12, bouw 2-3 variaties op H12-concept, één nieuwe hook als experiment. Data set nog klein → wacht 3-4 dagen + €150-200 spend voor definitieve calls.

### Google Sheet
Overgeslagen conform strikte regel. Rapport opgeslagen in `Output/Reports/Daily/2026-04-20_ads_report.md`.

---

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4.
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen op `Output/Reports/Daily/2026-04-19_sybb_report.md`.

**Kerncijfers 19/04:**
- Meta SYBB combined (oude + Kopie): €89,58 spend, 6.079 impr, 136 clicks, 2,24% CTR, €0,66 CPC, 6 IC. Volume in lijn met 7d avg, IC's +71%.
- Landing page: 140 pageviews, 119 sessies, **bounce 85,7%** (vs 80% 7d, target <55%), avg session 33s (target >90s).
- Ads doen het werk, de pagina vangt het verkeer niet op. h11 = volume + instant exits (7s), h13 = duurste klikker (€0,81) + 89% bounce, h12 = beste fit (60% bounce, kleinste volume).

**Top acties:** (1) onderzoek h11 ad-page mismatch via session recordings, (2) pauzeer h13 en lanceer een vervanger, (3) fix scroll-tracking (slechts 12% van pageviews triggert pageleave).

---

## Samenvatting

**Rapport opgeslagen:** `Output/Reports/Daily/2026-04-20_auto_optimize.md`

**Niveau 1 (automatisch):** **0 ads gepauzeerd.** Geen ad voldoet aan de kill-criteria (Link CTR < 0,8% bij ≥1.000 imp, of CPC link > €1,50 bij ≥500 link clicks). Bovendien draait de campagne pas ~18u — nog onder de 24-uur drempel uit de skill.

**Snapshot 3 actieve ads (van 16 totaal in `2026: SYBB - Kopie`):**
- H11 (...410239): 1.807 imp, **Link CTR 1,38%**, **CPC link €0,92** — meeste volume
- H13 (...660239): 947 imp, **Link CTR 1,69%**, **CPC link €0,93** — beste hook, CPM €15,79 ⚠️
- H12 (...700239): 569 imp, **Link CTR 1,41%**, **CPC link €0,97** — minst data

Alle 3 vallen in **20% Emerging** (geen Core: CPC link nergens < €0,50). 100% van het budget zit in Emerging, normaal voor dag-1.

**Voorstellen (wachten op jouw OK):** budget shift naar H13 na 48-72u, 2-3 nieuwe variaties op H13, en activeer 1 dormant hook per adset (13 PAUSED ads zijn al gebouwd).

**Notes:** Tweede account `act_607231713057715` geen toegang met huidig token. Geen Google MCPs gebruikt, niets naar Google Sheet geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,55 | 428 | 1 | 1 (EUR 350,00) | EUR 350,00 | 0.67x | EUR 521,55 |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 1 (EUR 423,50) | EUR 423,50 | 2.05x | EUR 207,00 |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.059,46** | **1036** | **1** | **2** | **EUR 773,50** | **0.73x** | **EUR 529,73** |

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
| 🥈 | H11, B3, CTA5 | 0.67x | 1 | EUR 350,00 | EUR 521,55 | 20% budget — tweede verified winner · houd actief |
| — | H12,B3,CTA5 | 0 orders | 0 | — | EUR 155,80 | NIET als best performer labelen · 0 Wix orders ondanks EUR 155,80 spend · heroverweeg |
| — | H14,B3,CTA5 | 0 orders | 0 | — | EUR 122,96 | NIET als best performer labelen · 0 Wix orders ondanks EUR 122,96 spend · heroverweeg |
| — | H15,B3,CTA5 | 0 orders | 0 | — | EUR 52,15 | NIET als best performer labelen · 0 Wix orders ondanks EUR 52,15 spend · heroverweeg |

**Verified funnel regels (hard):**
- Top verified performer: **H13** (verified ROAS 2.05x, 1 Wix order(s), EUR 423,50 revenue).
- H13 mag NIET gepauzeerd worden en krijgt 70% van het budget.
- Ads zonder verified orders (H12, H14, H15) mogen NIET als 'beste performer' of 'winner' gelabeld worden, ongeacht Meta pixel CTR/IC/purchase cijfers.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
