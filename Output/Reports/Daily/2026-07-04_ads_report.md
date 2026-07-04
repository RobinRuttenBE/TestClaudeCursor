## Meta Ads Rapport — 4 juli 2026

**Er draaien geen actieve campagnes.** Alles op het Sempertex-account staat op PAUSED en de spend over de laatste 30 dagen is €0,00. Ik heb daarom de meest recente gepauzeerde campagnes gerapporteerd met hun **lifetime** data. Het tweede account (`act_607231713057715`) is niet toegankelijk met het huidige API-token.

### Overzicht per campagne (lifetime)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS* |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 0,18x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | — |

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 + CPM €16,34 (beide boven drempel) → dure test op klein volume, niet in deze vorm heropstarten.
- **Ad H11,B3,CTA5** — CPC €0,67, hoogste spend (€521,56), maar 2,0% CTR → pauzeren.
- **Ad H13,B3,CTA5 (2e set)** — CPC €0,63 → zwakke duplicaat van de winnaar, stopzetten.
- **Ad "SYBB w/ Semp (BLACK)"** — CTR 1,0% + CPC €0,61 → laagste engagement, retireren.
- Geen enkele ad boven de frequency-drempel (3,5) → geen creative fatigue.

### Top performers
- **Beste CTR:** H13,B3,CTA5 — **9,8%** (op 60k impressies, dus solide)
- **Laagste CPC:** H13,B3,CTA5 — **€0,07**
- **Beste campagne:** 2026: SYBB — ruim binnen alle KPI-targets

### Samenvatting
- **Totaal spend:** €2.609,46 lifetime · **laatste 30 dagen €0,00**
- **Beste performer:** hook **H13** — de bewezen winnaar (70%-bucket).
- **Slechtste:** ad H11 + de "- Kopie" campagne.
- **Kernbevinding:** de ads presteerden gezond op traffic (CTR/CPC/CPM binnen target), maar de funnel converteerde slecht: **6 aankopen op 297k impressies**. Het knelpunt zit ná de klik (landing page → checkout), niet in de ads.

**Aanbeveling (70-20-10):** herstart met H13 als kern-hook, zet de zwakke duplicaten uit, en fix eerst de landing page-conversie voordat je opschaalt — bij 12.067 clicks en 6 aankopen zit de winst in de funnel, niet in meer ad-spend.

⚠️ **Databetrouwbaarheid:** de pixel purchase-value is onbetrouwbaar geconfigureerd (tegenstrijdige bedragen per event), dus ROAS 0,18x is indicatief. Valideer de pixel-tracking voor je op ROAS stuurt.

Rapport opgeslagen: `Output/Reports/Daily/2026-07-04_ads_report.md` (Google Sheet-write overgeslagen zoals gevraagd).

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4.
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` en voeg de volledige funnel-analyse toe aan dit rapport.
