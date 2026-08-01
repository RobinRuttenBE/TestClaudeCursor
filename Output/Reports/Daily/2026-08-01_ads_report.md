## Meta Ads Rapport, 1 augustus 2026

**Het account staat volledig stil.** Nul spend in de laatste 30 dagen, en ook nul in de laatste 90. Laatste dag met spend was **20 april 2026**, dat is 103 dagen geleden. Alle vijf campagnes staan op PAUSED. Onderstaand dus de laatst bekende performance.

### Overzicht per campagne (13 jan tot 20 apr 2026)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |
| 3x Nozzle Up (2025) | PAUSED | geen data in periode | | | | | | | |

Totaal €2.609,46 spend, 12.262 clicks, 6 conversies.

### Twee dingen die belangrijker zijn dan de tabel

**1. De conversiewaarde is corrupt.** Die 17,8x klopt niet. Adset Kopie 1 rapporteert 4 aankopen à €368, prima. Adset Kopie 3 rapporteert 2 aankopen à **€21.386**. De pixel stuurt daar een verkeerde value mee. Reken je met realistische ticketwaarde, dan is de echte ROAS ongeveer **0,85x**, dus licht verlieslatend. Dit fixen voordat er budget in gaat, anders optimaliseert Meta op ruis.

**2. Het lek zat niet in de ads.** 12.262 clicks leverden 6 aankopen op. Dat is 0,05% click-to-purchase en circa **€435 kosten per aankoop** op een ticket van circa €368. Je kocht klikken voor €0,07. De ads deden hun werk, wat erna gebeurde niet.

### Underperformers

Alle zwakke plekken zijn duplicaat-adsets met identieke creatives:

- **H13 (SYBB - Kopie)**, CPC €0,93 en CPM €19,14. Duurste van het account.
- **H11 (BATCH 2 Kopie 1)**, CPC €0,67 tegen €0,25 voor dezelfde creative in de originele adset.
- **H13 (BATCH 2 Kopie 3)**, CPC €0,63 tegen €0,07 in het origineel.
- **SYBB w/ Semp (BLACK)**, statisch, CTR 1,0% en CPC €0,61. Enige statische creative, veruit de zwakste.
- **Campagne SYBB - Kopie** in zijn geheel, €124,42 op nul conversies.

Geen frequency-problemen, hoogste was 2,2. Creative fatigue was dus niet de reden om te pauzeren.

### Top performers

- **Beste CTR:** H13 in BATCH 2 origineel, 9,8%
- **Laagste CPC:** H13 in BATCH 2 origineel, €0,07
- **Beste ROAS:** H11 in Kopie 1, 2,83x, de enige die betrouwbaar oogt
- **Beste adset:** BATCH 2: Expertise & POC origineel, CPC €0,14, CTR 4,99%. Alle vijf duplicaten presteerden slechter op elke metric.

### Aanbeveling

1. Fix de pixelwaarde eerst.
2. Diagnose de landing page, niet de ads. Daar zit het lek.
3. Herstart met consolidatie, niet duplicatie. Eén campagne, één adset, geen kopieën.
4. 70-20-10: 70% op H13 en H15 in de originele setup, 20% varianten met nieuwe CTA, 10% één nieuwe hook uit een ongeteste SYBB-pilaar. Statisch laten vallen.

### Google Sheet
Overgeslagen op instructie. Geen Google MCPs aangeroepen. Rapport lokaal opgeslagen in `Output/Reports/Daily/2026-08-01_ads_report.md`, gecommit en gepusht.

**Twee beperkingen:** ad-level insights op campagneniveau liepen herhaaldelijk op API-timeouts, ik heb per adset opgehaald en samengevoegd. CTR, CPC en CPM per ad zijn afgeleid uit spend, impressions en clicks. Lifetime insights, inclusief de Nozzle Up campagnes uit 2025, kwamen door timeouts niet binnen.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Gezien die 0,05% click-to-purchase is dat hier de meest waardevolle vervolgstap. Ik kan ook direct de PostHog data voor startyourballoonbusiness.com ophalen als je dat liever hebt, dat mag binnen de regels van deze run.
