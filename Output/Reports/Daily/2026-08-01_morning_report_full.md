# Morning Report — 2026-08-01

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

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

---

Rapport staat in `Output/Reports/Daily/2026-07-31_sybb_report.md`, gecommit en gepusht.

**De kern: er viel gisteren niets te meten.**

**Meta Ads.** Campagne `2026: SYBB` (120239435987290239) staat op PAUSED, net als alle 6 ad sets eronder. Nul impressies, nul clicks, nul spend op 31 juli. Laatste dag met delivery was 19 april 2026, dat is 103 dagen geleden. Op accountniveau draaide in heel juli geen enkele campagne.

**PostHog.** startyourballoonbusiness.com kreeg gisteren precies 1 pageview, 1 sessie, direct verkeer, geen UTM, 15 seconden, 0 CTA clicks, 0 `/booking` bezoeken. In de hele week 25 tot 31 juli: 3 pageviews.

Drie dingen die wel de moeite waard zijn:

1. **Tracking werkt, budget ontbreekt.** April had 1.976 pageviews op de landing page, exact gelijklopend met de ad delivery. Sinds mei zit de site op een organische bodem van circa 50 pageviews per maand.

2. **Er is wel een meetgat voor de herstart.** Op de sessie van gisteren ontbreken `$pageleave` en `$autocapture`. Zonder die twee zijn scroll depth en CTA click rate niet meetbaar, dus vier van de zeven KPI's uit dit rapport blijven leeg zodra de campagne weer aan gaat.

3. **Het historische lek zit tussen `/` en `/booking`.** Lifetime: 1.839 landingen, 165 booking bezoeken (9,0%), 54 checkouts, 10 thank-you pageviews. Dat bevestigt het beeld uit het ads rapport van 1 augustus.

Ik heb de KPI-statuslampjes bewust leeg gelaten (⚪ in plaats van 🟢/🟡/🔴). Bij n=1 sessie is "100% bounce rate" geen signaal maar ruis, en groen of rood zetten zou suggereren dat er iets te sturen valt.

Alleen Meta Ads MCP en PostHog MCP gebruikt. Geen Google MCPs aangeroepen, niets naar de Tracker Sheet geschreven.

---

Rapport staat in `Output/Reports/Daily/2026-08-01_auto_optimize.md`, gecommit en gepusht.

## Auto-Optimize, 1 augustus 2026

**Nul automatische acties.** Alle 5 campagnes in `act_567892422940728` staan PAUSED. Insights over `last_3d`, `last_30d` en `last_90d` geven allemaal een lege dataset. Laatste spend was 20 april, 103 dagen geleden. Er is geen ad om te pauzeren en geen data om tegen de drempels te toetsen.

**Twee dingen die je moet weten:**

**1. Het tweede account is niet bereikbaar.** De command noemt `act_607231713057715`, maar de Pipeboard token geeft alleen toegang tot `act_567892422940728` en `act_1489853856181844` (dat laatste is leeg). Als dat account echt mee moet, moet de token-scope uitgebreid worden.

**2. De link-metrics herberekening levert wél iets op.** Ik heb de laatst bekende periode opnieuw doorgerekend op link clicks in plaats van all-clicks, per adset. Dat verandert het beeld:

| Ad set | Link CTR | CPC (link) | Spend |
|--------|---------:|-----------:|------:|
| BATCH 2: Expertise & POC (origineel) | 4,8% | €0,15 | €1.463,49 |
| 4x Kopie | 1,1 tot 1,3% | €0,81 tot €1,22 | €919,81 |
| SYBB test set STATISCH | 0,7% | €0,91 | €101,74 |

Identieke creatives, 4x betere Link CTR en 8x lagere CPC in het origineel. De duplicatie kostte grofweg 5.800 link clicks aan gemiste volume.

De STATISCH adset (Link CTR 0,7%) zou de nieuwe kill-regel hebben getriggerd. Op all-clicks CTR (1,03%) was hij er doorheen geglipt. De drempelherziening van 13 april doet dus wat hij moet doen.

**Gat in de regelset:** Kopie 1 verbrandde €521,56 op een CPC (link) van €1,22 zonder ooit gepauzeerd te worden, omdat hij de 500 link clicks nooit haalde. Ik stel een tweede regel voor: CPC (link) > €0,80 na 150 link clicks. Dat had €340 bespaard op die ene adset.

**Zes voorstellen staan in het rapport, wachtend op goedkeuring.** Nummer 1 blokkeert de rest: de corrupte pixelwaarde (€21.386 per aankoop in Kopie 3) moet gefixt voordat er budget in gaat. Ik heb bewust geen nieuwe creative-varianten uitgeschreven, want die test je nu tegen een funnel die 12.262 clicks omzette in 6 aankopen. Zeg het als je ze toch wilt.

Alleen Meta Ads MCP gebruikt. Geen Google MCPs, niet naar de Tracker Sheet geschreven. PostHog heb ik niet bevraagd omdat er geen ad-data was om tegen te cross-referencen, maar dat is wel de meest waardevolle vervolgstap gezien die 0,05% click-to-purchase.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
