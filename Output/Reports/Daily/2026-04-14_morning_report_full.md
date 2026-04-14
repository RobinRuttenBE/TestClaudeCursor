# Morning Report — 2026-04-14

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 2026-04-14

### Overzicht per campagne

| Campagne   | Status | Spend   | Impressions | Clicks | CTR  | CPC   | CPM    | Conv. | ROAS  |
|------------|--------|---------|-------------|--------|------|-------|--------|-------|-------|
| 2026: SYBB | ACTIVE | €605,71 | 58.963      | 1.202  | 2,0% | €0,50 | €10,27 | 2     | 70,6x |

*Enige actieve campagne. act_1489853856181844 heeft geen actieve campagnes. act_607231713057715 niet toegankelijk met huidige token.*

### Ad-level (top 5 op spend)

| Ad                   | Spend   | CTR  | CPC   | Purch. | ROAS |
|----------------------|---------|------|-------|--------|------|
| H11,B3,CTA5 (Kopie 1)| €203,24 | 1,9% | €0,67 | 0      | —    |
| H14,B3,CTA5 (BATCH 2)| €122,96 | 1,8% | €0,41 | 0      | —    |
| H13,B3,CTA5 (Kopie 3)| €119,07 | 1,9% | €0,60 | **2**  | **359x** |
| H12,B3,CTA5 (Kopie 2)| €93,91  | 2,3% | €0,40 | 0      | —    |
| H15,B3,CTA5 (Kopie 4)| €49,83  | 2,3% | €0,47 | 0      | —    |

### Underperformers
- **H11,B3,CTA5 (Kopie 1)** — CPC €0,67 boven drempel, hoogste spend, 0 purchases → **pauzeren**
- **H13,B3,CTA5 (Kopie 3)** — CPC €0,60 technisch te duur, maar 2 purchases en ROAS 359x → **NIET pauzeren, budget verhogen**
- Geen ads met CTR <1%, frequency >3,5, of CPM >€15

### Top performers
- **Beste ROAS:** H13 (Kopie 3) — 359x (levert 100% van de revenue)
- **Beste CTR + volume:** H12 (Kopie 2) — 2,3% op 10.526 impr
- **Laagste CPC + volume:** H12 (Kopie 2) — €0,40

### Samenvatting
- **Totaal spend:** €605,71 | **Revenue:** €42.773,50 | **ROAS:** 70,6x (2 wholesale purchases à ~€21.387)
- **Beste:** H13 Kopie 3 — enige ad met conversies
- **Slechtste:** H11 Kopie 1 — €203 spend, 0 purchases
- **Aanbeveling (70-20-10):** 70% budget naar H13, 20% naar H12 variatie, 10% nieuw experiment. Pauzeer H11 onmiddellijk.

### Google Sheet
**Skipped** — stap 6 overgeslagen per instructie. Geen write naar Meta Ads Tracker.

### Opslag
Rapport opgeslagen: `Output/Reports/Daily/2026-04-14_ads_report.md`

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Report saved to `Output/Reports/Daily/2026-04-13_sybb_report.md`.

**Kerninzichten gisteren (2026-04-13):**
- Spend +62% naar €140,48, CPC gesprongen naar €0,68 (7d €0,50) 🚩
- LP bounce 73,4% (verbeterd vs 7d 81,9%), avg scroll 60% (vs 7d 44%) — engagement beter, volume-efficiency slechter
- **H11** vangt 56% van spend met slechtste CPC én CTR → budget herverdelen
- **H15** 100% LP bounce op 9 sessies, **H13** 78,9% bounce op 38 sessies → ad-page mismatch onderzoeken
- Funnel: 109 link clicks → 38 /booking (35%) → 4 /checkout (11%) → 0 purchases. Checkout-stap is het diepste lek.

---

## Auto-Optimize samenvatting — 2026-04-14

**⚡ Niveau 1 (uitgevoerd):** 1 ad gepauzeerd
- **H14, B3, CTA5** (120241275621450239) — Link CTR 0,8% met 1.304 imp, onder drempel 0,8%. Status: ACTIVE → PAUSED.

**📊 Campagne status 3d:** €418,52 spend, 35.193 imp, 366 link clicks, **Link CTR 1,0%**, **CPC (link) €1,14**. Campagne zelf is gezond.

**⚠️ Monitoring:** H11 (Kopie 1) zit borderline op beide kill-drempels (Link CTR 0,9%, CPC link €1,45) en slokt tegelijk 45% van het spend op. Grootste risico de komende 48u.

**💡 Niveau 2 voorstellen (wachten op goedkeuring):**
1. Budget herverdeling: Kopie 1 omlaag (-30/40%), Kopie 3 omhoog (+50%), Kopie 2 constant
2. Nieuwe variaties op winnende H13 hook (3 concrete varianten)
3. Funnel-diagnose op H12 — lage CPC maar nul conversies, waarschijnlijk LP-mismatch

**⚠️ Let op ROAS-anomalie:** H13 heeft 2 purchases met waarde €42.773,50 — waarschijnlijk één grote B2B wholesale order. Verifieer voordat budget echt wordt opgeschaald.

Rapport opgeslagen in `Output/Reports/Daily/2026-04-14_auto_optimize.md`. Geef aan welke voorstellen (1A/1B/1C/2A/2B/2C/3) je wil uitvoeren.

---

Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
