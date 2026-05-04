# Morning Report — 2026-05-04

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

## Meta Ads Rapport — 4 mei 2026

**Periode:** last 30 days (2026-04-04 t/m 2026-05-03)
**Account:** Sempertex Ad Account (`act_567892422940728`) — geen ACTIVE campagnes; toon meest recente PAUSED.

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. (Purch.) | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|----------------|------|
| 2026: SYBB | Paused | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 6 | n.v.t. (pixel datafout) |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 (6 IC) | n.v.t. (pixel datafout)* |
| Last push Nozzle Up | Paused | — | — | — | — | — | — | — | — |

*ROAS Kopie op `initiate_checkout` waarde, geen voltooide purchases.

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 + CPM €16,34 → niet heractiveren in huidige vorm
- **H13,B3,CTA5 (Kopie campagne, adset Kopie 3)** — CPC €0,93, CPM €19,14, 1 IC → pauseren
- **H12,B3,CTA5 (Kopie campagne, adset Kopie 2)** — CPM €18,92 → pauseren
- **H11, B3, CTA5 (hoofdcampagne, Kopie 1)** — CPC €0,67, maar ? purchases (verifieer Wix) + 5 leads → optimaliseer creative i.p.v. pauzeren

### Top performers
- **Beste CTR**: H15,B3,CTA5 (BATCH 2 origineel) — 6,37%, CPC €0,23 (lage spend)
- **Beste volume + efficiency**: H12,B3,CTA5 (BATCH 2 origineel) — CTR 4,73%, CPC €0,29
- **Beste ROAS (volume)**: H13,B3,CTA5 (hoofdcampagne, Kopie 3) — €207 → €42.773,50 = n.v.t. (pixel datafout) (outlier — verifieer)
- **Beste ROAS (consistent)**: H11, B3, CTA5 (hoofdcampagne, Kopie 1) — €521,56 → ? purchases (verifieer Wix) €1.473,50 = n.v.t. (pixel datafout)

### Samenvatting
- **Totaal spend (last 30d):** €1.183,89
- **Beste performer:** H12,B3,CTA5 (BATCH 2 origineel) — combinatie hoogste CTR + laagste CPC
- **Slechtste performer:** H13,B3,CTA5 (Kopie campagne, adset Kopie 3) — CPC €0,93, geen conversies
- **Frequency:** alle <3,5 (geen fatigue)
- **Aanbeveling (Hormozi 70-20-10):** Heractiveer hoofdcampagne, concentreer budget op H12 + H11. Pauseer Kopie-campagne ads zonder conversies. Verifieer eerst de €44.? purchases (verifieer Wix) value op 6 orders in Wix — als correct (B2B), is heractivatie urgent.

### Output
- **Lokaal opgeslagen:** `Output/Reports/Daily/2026-05-04_ads_report.md`
- **Google Sheet write:** overgeslagen conform run-instructie

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4.
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Als je de funnel data aanlevert, draai ik automatisch een `/funnel-diagnose` over Meta Ads + landing page samen, met bottleneck-analyse en 3 actiepunten.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-03_sybb_report.md`.

**Kernbevindingen:**
- Campagne **2026: SYBB** is dag 14 in pauze (sinds 2026-04-19), nul spend/impressions/clicks op 2026-05-03 en over de hele 7d window.
- **PostHog MCP niet beschikbaar** in deze sessie, dus secties 3 (LP Health) en 4 (Funnel) blijven leeg, twee dagen op rij.
- Drie acties: relaunch-beslissing, pixel-audit (€43.750 op 5 registraties is niet realistisch), en PostHog MCP-integratie fixen.

Conform run-regel: alleen Pipeboard Meta Ads MCP gebruikt, geen Google MCPs aangeroepen, niets naar Google Sheet geschreven.

---

Klaar. Belangrijkste bevinding van de run:

**Geen acties uitgevoerd — beide accounts hebben 0 actieve campagnes en 0 spend in `last_3d`.** De hoofdcampagne `2026: SYBB` (`act_567892422940728`) staat sinds 19 april 2026 paused, dus al ~15 dagen stil. Dat is het signaal dat aandacht vraagt; alle dagelijkse rapporten (morning report, ads-report, deze auto-optimize) zullen tot heractivering leeg blijven.

Rapport opgeslagen in `Output/Reports/Daily/2026-05-04_auto_optimize.md`. Niets naar Sheets of Google MCPs geschreven (per run-instructie).

Wil je dat ik `2026: SYBB` heractiveer, of laten we die bewust paused?

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
