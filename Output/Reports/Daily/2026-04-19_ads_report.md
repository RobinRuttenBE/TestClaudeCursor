Rapport hieronder en opgeslagen op `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-04-19_ads_report.md`.

## Meta Ads Rapport — 2026-04-19

**Periode:** last_30d (2026-03-20 t/m 2026-04-18) · **Account:** Sempertex Ad Account

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Active | €1.015,48 | 89.063 | 1.873 | 2,1% | €0,54 | €11,40 | 6 | 43,57x* |

*ROAS wordt vertekend door 1 outlier purchase van €42.773,50 op H13 (Kopie 3). Realistic ROAS exclusief outlier: ~1,4x.

### Ad-level (gesorteerd op spend)

| Ad | Adset | Status | Spend | CTR | CPC | Freq | LPV | ATC | Purch. | ROAS |
|----|-------|--------|-------|-----|-----|------|-----|-----|--------|------|
| H11,B3,CTA5 | Kopie 1 | ACTIVE | €503,89 | 2,0% | €0,67 | 1,84 | 325 | 23 | 4 | 2,92x |
| H13,B3,CTA5 | Kopie 3 | ACTIVE | €184,72 | 2,0% | €0,61 | 1,58 | 155 | 8 | 2 | 231x* |
| H12,B3,CTA5 | Kopie 2 | ACTIVE | €137,38 | 2,6% | €0,39 | 1,92 | 139 | 10 | 0 | 0x |
| H14,B3,CTA5 | Batch 2 | PAUSED | €122,96 | 1,8% | €0,41 | 1,34 | 108 | 0 | 0 | 0x |
| H15,B3,CTA5 | Kopie 4 | ACTIVE | €49,83 | 2,3% | €0,47 | 1,45 | 36 | 1 | 0 | 0x |

### Underperformers

- **H11,B3,CTA5 (Kopie 1, ACTIVE)** — CPC €0,67 (drempel: €0,50) → pauzeer of verlaag bid; slokt 50% budget tegen te hoge CPC.
- **H13,B3,CTA5 (Kopie 3, ACTIVE)** — CPC €0,61 (drempel: €0,50) → laat aan zolang ROAS data accuraat is; valideer purchase value handmatig.
- **Campagne avg CPC €0,54** boven 30d-target. Geen CTR <1%, geen freq >3,5, geen CPM >€15 in active set.

### Top performers

- **Beste CTR:** H12 (Kopie 2) — 2,6%
- **Laagste CPC:** H12 (Kopie 2) — €0,39
- **Beste ROAS:** H13 (Kopie 3) 231x outlier; realistisch winnaar = H11 (Kopie 1) 2,92x

### Samenvatting

- **Totaal spend:** €1.015,48 · **Purchases:** 6 (€44.247 incl. outlier)
- **Beste performer:** H12 (Kopie 2) — beste front-of-funnel, maar 0 purchases (conversie nog te bewijzen)
- **Slechtste performer (active):** H11 (Kopie 1) — 50% budget tegen CPC 34% boven drempel
- **Aanbeveling (70-20-10):**
  1. **70%:** Schuif €100-150/dag van H11 → H12 (Kopie 2). Beste front-of-funnel; verdient kans op purchases.
  2. **20%:** Houd H13 (Kopie 3) actief, maar valideer €42k purchase in Meta. Als echt → schaal. Als artefact → heroverweeg.
  3. **10%:** Test 1-2 nieuwe hooks als variant op H12 voordat freq omhoog gaat.

### Google Sheet

Overgeslagen op verzoek (geen Google MCP gebruikt deze run).

---

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4. Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
