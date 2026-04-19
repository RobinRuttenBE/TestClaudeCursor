# Morning Report — 2026-04-19

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,12%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,02** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 84,62** over 12 actieve dagen (niet totaal/30)
> - Bron: spend EUR 1015,48 · impressions 89.063 · link_clicks 1.000
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
> | H11, B3, CTA5 | EUR 503,89 | 37.483 | 410 | 1,09% | EUR 1,23 |
> | H13,B3,CTA5 | EUR 184,72 | 15.357 | 179 | 1,17% | EUR 1,03 |
> | H12,B3,CTA5 | EUR 137,38 | 13.719 | 172 | 1,25% | EUR 0,80 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport hieronder en opgeslagen op `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-04-19_ads_report.md`.

## Meta Ads Rapport — 2026-04-19

**Periode:** last_30d (2026-03-20 t/m 2026-04-18) · **Account:** Sempertex Ad Account

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Active | €1.015,48 | 89.063 | 1.873 | 2,1% | €0,54 | €11,40 | 6 | n.v.t. (pixel datafout)* |

*ROAS wordt vertekend door 1 outlier purchase van €42.773,50 op H13 (Kopie 3). Realistic ROAS exclusief outlier: ~n.v.t. (pixel datafout).

### Ad-level (gesorteerd op spend)

| Ad | Adset | Status | Spend | CTR | CPC | Freq | LPV | ATC | Purch. | ROAS |
|----|-------|--------|-------|-----|-----|------|-----|-----|--------|------|
| H11,B3,CTA5 | Kopie 1 | ACTIVE | €503,89 | 1,09% | € 1,23 | 1,84 | 325 | 23 | 4 | n.v.t. (pixel datafout) |
| H13,B3,CTA5 | Kopie 3 | ACTIVE | €184,72 | 1,17% | € 1,03 | 1,58 | 155 | 8 | 2 | 231x* |
| H12,B3,CTA5 | Kopie 2 | ACTIVE | €137,38 | 1,25% | € 0,80 | 1,92 | 139 | 10 | 0 | 0x |
| H14,B3,CTA5 | Batch 2 | PAUSED | €122,96 | 0,95% | € 0,78 | 1,34 | 108 | 0 | 0 | 0x |
| H15,B3,CTA5 | Kopie 4 | ACTIVE | €49,83 | 1,20% | € 0,87 | 1,45 | 36 | 1 | 0 | 0x |

### Underperformers

- **H11,B3,CTA5 (Kopie 1, ACTIVE)** — CPC €0,67 (drempel: €0,50) → pauzeer of verlaag bid; slokt 50% budget tegen te hoge CPC.
- **H13,B3,CTA5 (Kopie 3, ACTIVE)** — CPC €0,61 (drempel: €0,50) → laat aan zolang ROAS data accuraat is; valideer purchase value handmatig.
- **Campagne avg CPC €0,54** boven 30d-target. Geen CTR <1%, geen freq >3,5, geen CPM >€15 in active set.

### Top performers

- **Beste CTR:** H12 (Kopie 2) — 2,6%
- **Laagste CPC:** H12 (Kopie 2) — €0,39
- **Beste ROAS:** H13 (Kopie 3) 231x outlier; realistisch winnaar = H11 (Kopie 1) n.v.t. (pixel datafout)

### Samenvatting

- **Totaal spend:** €1.015,48 · **Purchases:** 6 (€44.247 incl. outlier)
- **Beste performer:** H12 (Kopie 2) — beste front-of-funnel, maar ? purchases (verifieer Wix) (conversie nog te bewijzen)
- **Slechtste performer (active):** H11 (Kopie 1) — 50% budget tegen CPC 34% boven drempel
- **Aanbeveling (70-20-10):**
  1. **70%:** Schuif €100-150/dag van H11 → H12 (Kopie 2). Beste front-of-funnel; verdient kans op purchases.
  2. **20%:** Houd H13 (Kopie 3) actief, maar valideer €42k purchase in Meta. Als echt → schaal. Als artefact → heroverweeg.
  3. **10%:** Test 1-2 nieuwe hooks als variant op H12 voordat freq omhoog gaat.

### Google Sheet

Overgeslagen op verzoek (geen Google MCP gebruikt deze run).

---

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4. Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen op `Output/Reports/Daily/2026-04-18_sybb_report.md`.

**Highlights 2026-04-18:**
- Spend €94,47 (-10% vs 7d), CPC €0,62 (boven target), CPM €14,68 (+18% vs 7d, slechter)
- **Doorbraak op funnel-bottom:** 7 initiate checkouts en 1 voltooide aankoop (`/thank-you-page`) — eerste echte conversie in dagen
- **H12 wint** (CTR 4,21%, CPC €0,38, 3/7 IC's met 13% van de spend), maar krijgt nog steeds te weinig budget
- **H13 onderpresteert**: 88,9% bounce, scroll 50% slechts 20% — kandidaat om te pauzeren
- Bounce 80,4% en scroll 25% van 41,9% bevestigen dat hero-sectie het grootste lek blijft
- CTA → `/booking` tracking gap nog steeds open (10 clicks → 1 PV)

Top acties: schaal H12 / pauzeer H13, fix CTA tracking, plan hero-test.

---

Rapport opgeslagen: `Output/Reports/Daily/2026-04-19_auto_optimize.md`.

**Niveau 1 (automatisch):** 0 ads gepauzeerd — alle 3 actieve ads in `2026: SYBB` passeren Link CTR > 0,8% (laagste is H11 op 1,2%). CPC kill-rule kan niet triggeren want geen ad heeft 500+ link clicks in 3d.

**Belangrijkste bevinding:** budget mismatch. H11 absorbeert 73% van de spend (€175 van €239) maar heeft de zwakste conv rate (2,6%) en hoogste cost per IC (€43,72). H12 — beste op vrijwel elke metric (Link CTR 2,1%, conv rate 13,6%, cost per IC €4,79) — krijgt slechts 12%.

**Niveau 2 voorstellen** (wachten op goedkeuring): (1) budget herverdeling H12 +300% / H11 -40%, (2) nieuwe variaties op winnende H12 hook, (3) audience-uitbreiding bij opschaling H12. Geef de nummers door om uit te voeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 503,89 | 410 | 1 | 1 (EUR 350,00) | EUR 350,00 | 0.69x | EUR 503,89 |
| H12,B3,CTA5 | EUR 151,75 | 192 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 184,73 | 179 | 0 | 1 (EUR 423,50) | EUR 423,50 | 2.29x | EUR 184,73 |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.015,48** | **1000** | **1** | **2** | **EUR 773,50** | **0.76x** | **EUR 507,74** |

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



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
