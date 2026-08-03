## Meta Ads Rapport, 3 augustus 2026

**Het account ligt stil.** Nul spend in de laatste 30 dagen, en ook nul over de laatste 90 dagen. De laatste actieve dag was in april 2026, dus ruim 3 maanden geleden. Alle 5 campagnes staan op PAUSED.

Het tweede account uit het command (`act_607231713057715`) bestaat niet onder deze connectie. Wel gecheckt: **AmbitionAvenue** (`act_1489853856181844`), geen campagnes, geen spend.

### Overzicht per campagne (lifetime, gesorteerd op spend)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. | ROAS |
|---|---|---|---|---|---|---|---|---|---|
| 2026: SYBB | Paused | € 2.485,04 | 297.174 | 12.067 | 4,1% | € 0,21 | € 8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | Paused | € 853,19 | 129.558 | 3.291 | 2,5% | € 0,26 | € 6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | € 800,78 | 109.869 | 2.786 | 2,5% | € 0,29 | € 7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | € 604,03 | 369.136 | 3.638 | 1,0% | € 0,17 | € 1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | € 124,42 | 7.615 | 195 | 2,6% | € 0,64 | € 16,34 | 0 | n.v.t. |

\* Die 17,8x klopt niet. De pixel meldt 6 purchases met € 44.247,00 totaalwaarde, dus € 7.374,50 per SYBB-ticket, plus € 86.100,00 op complete_registration. Tracking-fix nodig.

### Underperformers
- **2026: SYBB - Kopie**, CPC € 0,64 en CPM € 16,34, beide boven drempel. Duurste campagne van het account, nul purchases.
- **Ad H13,B3,CTA5 (Kopie 3)**, CPC € 0,93. Dezelfde hook draaide in BATCH 2 op € 0,07. De hook is niet het probleem, de gedupliceerde ad set wel.
- **Ad H11, B3, CTA5 (Kopie 1)**, CPC € 0,67 over € 521,56, de grootste spender van 2026. Origineel in BATCH 2: € 0,25.
- **Ad SYBB w/ Semp (BLACK)**, CTR 1,0% en CPC € 0,61. Enige statische creative, zwakste van het account.
- **April als maand**, CPC € 0,55 en CPM € 11,54 tegen € 0,13 en € 7,00 in maart.

Frequency zit nergens boven 3,5 (max 2,89), dus de kostenstijging komt niet van herhaling maar van het dupliceren van ad sets.

### Top performers
- **Beste CTR:** H13,B3,CTA5 in BATCH 2, 9,8%
- **Laagste CPC:** dezelfde ad, € 0,07
- **Beste betrouwbare ROAS:** Campagne Nozzle Up 2025 1, 8,3x
- **Beste ad set:** BATCH 2: Expertise & POC, € 1.463,49 spend, 10.322 clicks, gemiddeld € 0,14 CPC

### Aanbeveling
1. Fix eerst de pixel-waardes. Zonder betrouwbare purchase value is elke ROAS-beslissing giswerk.
2. Herstart de **originele** 2026: SYBB met de bestaande BATCH 2 ad set, archiveer de kopie definitief.
3. 70% bewezen (H13, H15, H12 uit BATCH 2: samen 8.615 clicks op € 0,12), 20% nieuwe hooks op dezelfde B3 body en CTA5, 10% één nieuwe angle (pricing of quality proof). Geen statische creatives meer.
4. Elke week extra stilstand maakt de herstart duurder: pixel-signalen verouderen en de learning phase moet opnieuw.

Rapport opgeslagen in `output/reports/daily/2026-08-03_ads_report.md`, gecommit en gepusht. Google Sheet-stap overgeslagen, geen enkele Google MCP aangeroepen.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Let wel: met nul ad traffic sinds april zal die funnel data alleen organisch verkeer laten zien.
