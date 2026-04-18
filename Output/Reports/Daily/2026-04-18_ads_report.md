## Meta Ads Rapport — 2026-04-18

**Periode:** last 30d (2026-03-19 t/m 2026-04-17) · **Account:** Sempertex (act_567892422940728)
Robin Rutten account: geen toegang met dit token. act_1489853856181844: geen actieve campagnes.

### Overzicht per campagne

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. | ROAS* |
|---|---|---|---|---|---|---|---|---|---|
| 2026: SYBB | Active | €920,88 | 82.616 | 1.721 | 2,1% | €0,54 | €11,15 | 6 | 48,05x |

*Meta-rapporteerde purchase action_value van €44.247 is verdacht hoog (web_app_in_store_purchase waarde = €4,42). Behandel ROAS als indicatief.

### Overzicht per ad (top 6 op spend)

| Ad | Adset | Status | Spend | CTR | CPC | Freq. | Purch. |
|---|---|---|---|---|---|---|---|
| H11,B3,CTA5 | Kopie 1 | ACTIVE | €436,37 | 2,0% | €0,66 | 1,79 | 4 |
| H13,B3,CTA5 | Kopie 3 | ACTIVE | €170,14 | 1,9% | €0,61 | 1,55 | 2 |
| H12,B3,CTA5 | Kopie 2 | ACTIVE | €124,88 | 2,5% | €0,39 | 1,87 | 0 |
| H14,B3,CTA5 | Batch 2 | PAUSED | €122,96 | 1,8% | €0,41 | 1,34 | 0 |
| H15,B3,CTA5 | Kopie 4 | PAUSED | €49,83 | 2,3% | €0,47 | 1,45 | 0 |
| H12,B3,CTA5 | Batch 2 | PAUSED | €14,37 | 4,7% | €0,29 | 1,94 | 0 |

### Underperformers (actief)

- **H11 Kopie 1** — CPC €0,66 (>€0,50). Drager van 47% spend en 67% purchases → behouden, maar test nieuwe hook-variant om CPC te drukken.
- **H13 Kopie 3** — CPC €0,61 (>€0,50). ROAS-signaal onstabiel (n=2). Laat staan, niet opschalen.
- Geen CTR <1%, geen frequency >3,5, geen CPM >€15 onder actieve set.

### Top performers

- **Beste CTR (actief):** H12 Kopie 2 — 2,5%
- **Laagste CPC (actief):** H12 Kopie 2 — €0,39
- **Meeste purchases:** H11 Kopie 1 — 4 van 6
- **Beste CTR overall:** H12 Batch 2 (paused) — 4,7% (n=1.058, ruis)

### Samenvatting + aanbeveling (70-20-10)

- **70% bewezen:** schuif budget naar H11 Kopie 1 tot CPC <€0,55 zakt of frequency 3,0 nadert.
- **20% variatie:** H12 Kopie 2 heeft sterke klik-metrics, 0 purchases op 319 clicks en 127 LP views. Bottleneck zit op de landing page, niet in de creative — draai `/funnel-diagnose` op utm_content `h12_b3_cta5` (Kopie 2).
- **10% experiment:** reactiveer H12 Batch 2 in kleine adset (€5/dag) om te zien of 4,7% CTR op schaal houdt.

### Google Sheet
Overgeslagen op verzoek. Geen Google MCP calls gedaan.

Rapport opgeslagen: `Output/Reports/Daily/2026-04-18_ads_report.md`

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
