## Meta Ads Rapport — 2026-05-02

**Periode:** last_30d (2026-04-02 t/m 2026-05-01)
**Account:** Sempertex Ad Account (`act_567892422940728`)
**Status:** Geen ACTIEVE campagnes. De 2 meest recente SYBB campagnes zijn PAUSED — hun laatste 30d performance staat hieronder.

### Overzicht per campagne

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Conv. | ROAS* |
|----------|--------|-------|-------|--------|------|------|------|------|-------|
| 2026: SYBB | Paused | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 6 | 41,8x* |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |
| **Totaal** | — | **€1.183,89** | **99.454** | **2.130** | **2,1%** | **€0,56** | **€11,90** | **6** | **37,4x*** |

\* **Data-waarschuwing:** ad H13,B3,CTA5 (Kopie 3) rapporteert 2 purchases met value €42.773,50 (= €21.386/aankoop). Pixel value is fout gemapt. Werkelijke ROAS (zonder outlier): ~1,4x.

### Underperformers
- **H11,B3,CTA5 (Kopie 1)** — CPC €0,67, hoogste spender (€521,56) → inefficiënt op schaal
- **H13,B3,CTA5 (Kopie 3, SYBB)** — CPC €0,63 + Pixel value-bug → fix tracking voor relaunch
- **H13,B3,CTA5 (Kopie 3, SYBB-Kopie)** — CPC €0,93, CPM €19,14 → 3 drempels overschreden
- **H12,B3,CTA5 (Kopie 2, SYBB-Kopie)** — CPM €18,92 → dure reach
- Geen creative fatigue (max freq 2,19) en geen CTR<1%

### Top performers
- **Beste CTR (volume):** H12,B3,CTA5 (BATCH 2) — **4,7%** bij 1.058 impressies, CPC €0,29
- **Laagste CPC:** H15,B3,CTA5 (BATCH 2) — €0,23 (lage volume)
- **Enige geloofwaardige converteerder:** H11,B3,CTA5 (Kopie 1) — 4 purchases, ROAS ~2,8x
- **Beste CPM:** H14,B3,CTA5 (BATCH 2) — €7,43

### Samenvatting & aanbeveling (Hormozi 70-20-10)
- 62% van spend zit in 2 ads (H11/H13 in adsets Kopie 1/3) — beide met CPC boven drempel
- **Winnaar voor relaunch:** H12,B3,CTA5 (BATCH 2) als hoofdcreative; H11,B3,CTA5 voor conversie
- **70% schalen:** H12 + H11 hooks behouden
- **20% variaties:** test H12,B[2,4],CTA5 en H11+CTA5 op LAL
- **10% experimenteel:** nieuw hooktype (credibility/transformation) + 1 nieuw format
- **Eerst doen:** Pixel value-mapping fixen vóór relaunch, anders is ROAS-data nutteloos

### Google Sheet
Overgeslagen per instructie. Rapport opgeslagen op:
`/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-02_ads_report.md`

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Als je deze data aanlevert, draai ik automatisch een `/funnel-diagnose` analyse en voeg die als sectie toe.
