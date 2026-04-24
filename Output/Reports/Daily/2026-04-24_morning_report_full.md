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
> | H11, B3, CTA5 | EUR 521,56 | 38.614 | 428 | 1,11% | EUR 1,22 |
> | H13,B3,CTA5 | EUR 206,99 | 16.766 | 195 | 1,16% | EUR 1,06 |
> | H12,B3,CTA5 | EUR 141,43 | 13.955 | 174 | 1,25% | EUR 0,81 |
> | H14,B3,CTA5 | EUR 122,96 | 16.551 | 158 | 0,95% | EUR 0,78 |
> | H15,B3,CTA5 | EUR 49,83 | 4.737 | 57 | 1,20% | EUR 0,87 |
> | H12,B3,CTA5 | EUR 14,37 | 1.058 | 20 | 1,89% | EUR 0,72 |
> | H15,B3,CTA5 | EUR 2,32 | 157 | 4 | 2,55% | EUR 0,58 |
> | H13,B3,CTA5 | EUR 0,01 | 1 | 0 | 0,00% | EUR 0,00 |
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


## Meta Ads Rapport — 2026-04-24

**Status check:** Geen ACTIVE campagnes op Sempertex Ad Account. Beide SYBB campagnes staan op PAUSED maar hadden activiteit binnen last_30d. Nozzle Up campagnes zonder data. Robin Rutten account (act_607231713057715) niet toegankelijk met huidige token.

### Overzicht per campagne (last_30d: 2026-03-25 → 2026-04-23)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | PAUSED | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 6 purch / 33 IC | n.v.t. (pixel datafout)* |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 purch / 6 IC | n.v.t. (pixel datafout) |

*ROAS vertekend door 1 groot wholesale order van €42.773 op H13,B3,CTA5 — Kopie 3.

### Underperformers
- **H13,B3,CTA5 — Kopie 3 (Kopie campagne)** — CPC €0,93 + CPM €19,14 → uitschakelen
- **H11, B3, CTA5 — Kopie 1 (main)** — CPC €0,67, hoogste spend → hook-refresh of duplicate naar nieuwe lookalike
- **H13,B3,CTA5 — Kopie 3 (main)** — CPC €0,63 → hook-refresh, maar signaalwaarde hoog (? purchases (verifieer Wix))
- **Kopie campagne overall** — CPM €16,34 (30% duurder dan main), ? purchases (verifieer Wix) bij €124,42 → heractiveer niet zonder audience-rebuild

### Top performers
- **Beste CTR**: H15,B3,CTA5 Base (main) — 6,4%
- **Laagste CPC**: H15,B3,CTA5 Base (main) — €0,23
- **Beste winner op schaal**: H12,B3,CTA5 Base (main) — CTR 4,7% / CPC €0,29 bij €14,37 spend → hero ad voor heractivatie
- **Beste ROAS**: H13,B3,CTA5 — Kopie 3 (main) — ? purchases (verifieer Wix), €42.773 value
- **Beste volume-winner**: H11, B3, CTA5 — Kopie 1 (main) — ? purchases (verifieer Wix), €521,56 spend

### Samenvatting
- **Totaal spend**: €1.183,89 (last 30d)
- **Totale purchases**: 6 (value €44.247, grotendeels 1 outlier wholesale order)
- **Beste performer**: H12,B3,CTA5 Base — scherpste CTR × CPC combo, dupliceer bij heractivatie
- **Slechtste performer**: H13,B3,CTA5 Kopie 3 (Kopie campagne) — duur, 1 checkout
- **70-20-10 aanbeveling**: 70% budget op H11/H12/H13 main (bewezen purchases), 20% varianten op H12 Base hero ad, 10% lookalike van 6 purchasers

### Output
**Google Sheet:** overgeslagen conform run-instructie.
**Rapport:** `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-04-24_ads_report.md`

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-23_sybb_report.md`.

**Kernbevindingen:**
- Campagne "2026: SYBB" (ID 120239435987290239) stond op **PAUSED** op 2026-04-23 → €0 spend, 0 impressions, 0 clicks.
- Landingspagina kreeg 4 pageviews / 3 sessies, allemaal via `utm_content=bio_link` (organisch).
- 7d baseline Meta (2026-04-16 t/m 2026-04-22): €283,02 spend, 19.726 impressions, CTR 2,32%, CPC €0,62, frequency 1,80, 14 initiate checkouts, 1 complete registration.
- **Datakwaliteit-issues gevonden:** scroll depth telemetrie vrijwel leeg, `$pageleave` ondergerapporteerd, QA-UTM `test123` lekte naar productie op 18-04.
- PostHog host blijkt `www.startyourballoonbusiness.com` (met `www.`), de SKILL.md noemt de variant zonder `www.` wat anders een lege query zou opleveren — waard om op te lossen in de skill.

**Top 3 acties:** campagne-restart bevestigen, PostHog scroll/pageleave tracking fixen in Wix, QA-UTM opschonen.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-24_auto_optimize.md`.

**Kort resultaat:**
- Beide toegankelijke ad accounts (`act_567892422940728` en `act_1489853856181844`) hebben **0 actieve campagnes**. De hoofdcampagne `2026: SYBB` staat op PAUSED sinds 2026-04-19, evenals een duplicaat `2026: SYBB - Kopie`.
- `last_3d` insights op beide SYBB-campagnes zijn leeg → geen spend/impressies/clicks in de periode.
- Geen automatische pauze-acties nodig (niets loopt), geen 70-20-10 classificatie mogelijk.
- Account `act_607231713057715` is niet toegankelijk met de huidige MCP token — in rapport gemeld.

**Open vraag in het rapport:** is de pauze op SYBB bewust (refresh/herstructurering) of moet één van de twee campagnes weer ACTIEF? Pas dan levert dit command optimalisatiewaarde.

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
