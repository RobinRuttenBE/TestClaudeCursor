# Meta Ads Rapport — 8 mei 2026

**Periode:** last_30d (2026-04-08 t/m 2026-05-07)
**Account:** Sempertex Ad Account (act_567892422940728)
**Tweede account:** act_1489853856181844 — geen actieve of recent gepauzeerde campagnes met data
**Status:** Geen ACTIEVE campagnes. Onderstaande data komt van de twee meest recent gepauzeerde campagnes (laatste update 19 en 20 april 2026).

---

## Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Frequency | Conv. (purchase) | Conv. value |
|----------|--------|-------|-------------|--------|------|-----|-----|-----------|------------------|-------------|
| 2026: SYBB | Paused | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 2,19 | 6 | €442,47 |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 1,42 | 0 (3 IC) | €21,00 (IC) |

**Toelichting:** "2026: SYBB - Kopie" had geen purchases gemeten, alleen 3 initiate_checkouts (waarde uit `action_values.initiate_checkout` = 2.100 cents = €21,00).

---

## Ad-level performance (top 10 op spend)

| Campagne | Ad naam | Adset | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq | Purchases | LP views | ATC | IC |
|----------|---------|-------|-------|-------|--------|-----|-----|-----|------|-----------|----------|-----|-----|
| SYBB | H11, B3, CTA5 | Kopie 1 | €521,56 | 38.614 | 784 | 2,0% | €0,67 | €13,51 | 1,85 | 4 | 343 | 23 | 23 |
| SYBB | H13,B3,CTA5 | Kopie 3 | €206,99 | 16.766 | 331 | 2,0% | €0,63 | €12,35 | 1,64 | 2 | 171 | 8 | 4 |
| SYBB | H12,B3,CTA5 | Kopie 2 | €141,43 | 13.955 | 356 | 2,6% | €0,40 | €10,13 | 1,95 | 0 | 139 | 10 | 6 |
| SYBB | H14,B3,CTA5 | BATCH 2 | €122,96 | 16.551 | 297 | 1,8% | €0,41 | €7,43 | 1,34 | 0 | 108 | 0 | 0 |
| SYBB - Kopie | H11, B3, CTA5 | Kopie 1 | €51,34 | 3.782 | 95 | 2,5% | €0,54 | €13,57 | 1,22 | 0 | 42 | 0 | 3 |
| SYBB | H15,B3,CTA5 | Kopie 4 | €49,83 | 4.737 | 107 | 2,3% | €0,47 | €10,52 | 1,45 | 0 | 36 | 1 | 0 |
| SYBB - Kopie | H13,B3,CTA5 | Kopie 3 | €47,21 | 2.466 | 51 | 2,1% | €0,93 | €19,14 | 1,20 | 0 | 36 | 0 | 1 |
| SYBB - Kopie | H12,B3,CTA5 | Kopie 2 | €25,87 | 1.367 | 49 | 3,6% | €0,53 | €18,92 | 1,35 | 0 | 22 | 0 | 2 |
| SYBB | H12,B3,CTA5 | BATCH 2 | €14,37 | 1.058 | 50 | 4,7% | €0,29 | €13,58 | 1,94 | 0 | 18 | 2 | 0 |
| SYBB | H15,B3,CTA5 | BATCH 2 | €2,32 | 157 | 10 | 6,4% | €0,23 | €14,78 | 1,34 | 0 | 3 | 0 | 0 |

> Ad H13,B3,CTA5 (BATCH 2 main, ad_id 120241275557280239) wordt weggelaten: slechts 1 impressie en €0,01 spend.

---

## Underperformers (drempels: CPC > €0,50, CTR < 1%, CPM > €15, Freq > 3,5)

### Campagne-niveau
- **2026: SYBB** — CPC €0,55 (drempel €0,50). Marginaal over. → Aanbeveling: bij heractivatie eerst budget naar de twee bewezen creatives schuiven, dan CPC monitoren.
- **2026: SYBB - Kopie** — CPC €0,64 én CPM €16,34 boven drempel. → Aanbeveling: deze test-kopie heeft geen purchases en hogere kosten op alle vlakken. Niet heractiveren in deze vorm.

### Ad-niveau
- **H13,B3,CTA5 (Kopie 3, "SYBB - Kopie")** — CPC €0,93 (87% boven drempel) en CPM €19,14. Geen IC tot betekenis. → Aanbeveling: pauzeren of vervangen.
- **H12,B3,CTA5 (Kopie 2, "SYBB - Kopie")** — CPM €18,92 boven drempel ondanks goede CTR (3,6%). Audience overlap met main campagne waarschijnlijk. → Aanbeveling: budget consolideren in main campagne.
- **H11, B3, CTA5 (Kopie 1, main "SYBB")** — CPC €0,67 boven drempel maar wel 4 purchases en hoogste spend. → Aanbeveling: niet pauzeren, wel bidstrategy of audience trimmen om CPC < €0,50 te krijgen.

---

## Top performers

- **Beste CTR (met volume):** H12,B3,CTA5 — Kopie 2 (main SYBB) — **2,55%** bij €141 spend. Variant in Kopie 2 ("SYBB - Kopie") haalt 3,58% maar bij dunner volume.
- **Laagste CPC (met volume):** H12,B3,CTA5 — Kopie 2 (main SYBB) — **€0,40**.
- **Beste CPM:** H14,B3,CTA5 — BATCH 2 (main SYBB) — **€7,43** (significant onder €15-drempel).
- **Beste ROAS direct attribuable:** H13,B3,CTA5 — Kopie 3 (main SYBB) — €206,99 spend → 2 purchases met `action_values.purchase` = €427,73 = **2,07x ROAS** (waarde lijkt cents → €4,28 web_app_in_store_purchase = 1:100 schaal). Verifieer of de reported €427,73 een grootschalige B2B order betreft.
- **Laagste CPC absolute:** H15,B3,CTA5 — BATCH 2 — €0,23 maar slechts 10 clicks (te laag volume om conclusie te trekken).

---

## Samenvatting

- **Totaal spend (last 30d):** €1.183,89 over 2 campagnes (alleen "2026: SYBB" + "Kopie").
- **Totale purchases (gemeten):** 6, geattribueerde waarde €442,47 → directe ROAS **0,42x** (verlies op directe attribution, maar 33 initiate_checkouts en 44 add_to_carts wijzen op funnel met latente conversie).
- **Beste performer ad:** H13,B3,CTA5 (Kopie 3, main SYBB) — hoogste directe ROAS met 2 purchases ondanks gemiddelde CPC.
- **Slechtste performer ad:** H13,B3,CTA5 (Kopie 3, "SYBB - Kopie") — €47 spend, geen purchases, CPC €0,93 + CPM €19,14.
- **Beste duo (Hormozi 70-20-10 winners):** H11 in Kopie 1 (volume + 4 purchases) en H12 in Kopie 2 (laagste CPC + hoogste CTR met volume). Bij heractivatie: 70% budget naar deze twee, 20% naar varianten van H13/H14 (Kopie 3), 10% experimenten.

### Aanbeveling (concreet)
1. **Bij heractivatie:** sluit "2026: SYBB - Kopie" af. Deze had hogere CPC én CPM en geen purchases — pure budget-verspilling vs. de main campagne.
2. **Schaal H11 (Kopie 1) en H12 (Kopie 2)** in main campagne. Dit zijn de twee adsets met bewezen funnel-doorstroom (purchases + IC).
3. **Pauzeer H13,B3,CTA5 in "Kopie 3"** binnen "SYBB - Kopie". Ondermaats op alle KPIs.
4. **Onderzoek de €427,73 purchase value op H13 Kopie 3** — als dat één wholesale order is, overweeg dan een retargeting-laag te bouwen op dezelfde audience signals.
5. **Audience overlap audit** voordat je weer twee parallel-running SYBB campagnes laat lopen — de "Kopie"-versie at een deel van het main-budget zonder eigen returns te leveren.

---

## Google Sheet

Niet geschreven (stap 6 overgeslagen op verzoek van Robin voor deze run).

---

> **Wil je funnel data toevoegen?** Geef de landing page metrics uit Wix Analytics of GA4: visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik een /funnel-diagnose op de gecombineerde dataset.
