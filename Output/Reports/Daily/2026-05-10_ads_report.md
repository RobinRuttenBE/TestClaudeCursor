## Meta Ads Rapport — 10 mei 2026

**Status:** Geen ACTIVE campagnes. Rapport toont meest recent gepauzeerde campagnes (beide SYBB 2026), last 30d.

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS* |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | PAUSED | €940,63 | 76.542 | 1.620 | 2,1% | €0,58 | €12,29 | 6 | 47,04x* |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 (6 IC) | n.v.t. |

*ROAS-waarschuwing: de 47x wordt opgeblazen door één Wix-event van €42.773,50 op H13 (terwijl `web_app_in_store_purchase` voor diezelfde ad slechts €4,28 toont). Vermoedelijke value-tracking misconfig in de Wix → Meta Pixel pipeline. Niet vertrouwen tot dit gefixt is.*

### Underperformers

- **Campagne "2026: SYBB - Kopie"** — CPM €16,34 (>€15) én CPC €0,64 (>€0,50), 100 LPV en 0 purchases op €124. → Niet heractiveren.
- **Ad H11,B3,CTA5** — €521,56 (55% budget) tegen CPC €0,67. → Pauzeren; H12 doet dezelfde job 40% goedkoper.
- **Ad H13,B3,CTA5** — CPC €0,63 + value-tracking is corrupt. → Pauzeren tot Pixel-fix.

### Top performers

- **Beste CTR (ad)**: H12,B3,CTA5 — 2,55%
- **Laagste CPC**: H12,B3,CTA5 — €0,40
- **Beste ROAS (geverifieerd)**: H11,B3,CTA5 — 2,83x (€1.473,50 op €521,56)

### Samenvatting

- **Totaal spend:** €1.065,05 over 30 dagen
- **Beste performer:** H12,B3,CTA5 — laagste CPC + hoogste CTR, maar **0 purchases** ondanks 139 LPV → engagement werkt, conversie-pad lekt.
- **Slechtste performer:** H11,B3,CTA5 — slokt budget tegen 67% boven CPC-target.
- **Aanbeveling (70-20-10):** Fix Wix Pixel value-mapping eerst. Daarna H12 schalen als hoofdcreative, 2-3 hook-varianten op het H12-frame, H11 en H13 archiveren.

### Google Sheet
Stap 6 overgeslagen per instructie. Rapport opgeslagen in:
`/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-10_ads_report.md`

---

> **Wil je funnel data toevoegen?** Geef de landing page metrics uit Wix Analytics of GA4 (visitors, opt-in/booking clicks, add to cart, completed purchases) en ik draai automatisch een `/funnel-diagnose` met de gecombineerde data.
