## Meta Ads Rapport, 21 augustus 2026

**Pipeboard werkt weer.** Voor het eerst in twaalf dagen live data. De MCP connector staat in deze sessie nog op "requires authentication", maar de Pipeboard endpoint accepteert je project token wel via directe HTTP calls. PostHog idem, via de API. Geen Google MCP aangeroepen, stap 6 overgeslagen.

Correctie op het commando: `act_607231713057715` bestaat niet. Het tweede account is `act_1489853856181844` (AmbitionAvenue), nul campagnes, nul spend.

### Overzicht per campagne

Geen actieve campagnes. Alle vijf staan op PAUSED. Cijfers zijn lifetime, want de laatste 30 dagen leverden nul rijen op.

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|---|---|---|---|---|---|---|---|---|---|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

**Laatste 30 dagen: €0,00.** Laatste euro uitgegeven in **april 2026**. Vier maanden donker. Lifetime totaal €4.867,46, exact het accountsaldo.

### Underperformers

- **2026: SYBB - Kopie**, CPC €0,64 én CPM €16,34, nul aankopen op 195 clicks → archiveren
- **SYBB w/ Semp (BLACK)** (ad), CTR 1,0%, en **nul landing page views op 167 clicks**. Dat betekent pixel of bestemming stuk → testen vóór herstart
- **Last push Nozzle Up**, ROAS 0,8x, de enige aantoonbare verliezer
- Frequency nergens een probleem, hoogste is 2,89

### Dezelfde hook, 8,8x prijsverschil

H13 draaide twee keer. Eén keer 9,8% CTR bij **€0,07** per klik, één keer 2,0% bij **€0,63**. Zelfde creative. Het verschil zit in de delivery, niet in de hook. Je "bewezen winnaar" is dus niet bewezen zolang je niet weet welke adset die €0,07 leverde.

En het ongemakkelijke deel: **H13 leverde 4.063 landing page views op en nul aankopen.** H11 leverde er 343 op en alle vier de aankopen, tegen tien keer de klikprijs. Je goedkoopste ad is op dit moment je slechtste ad.

### Voorbehoud bij die 17,8x

€44.247 pixel-omzet op zes aankopen is €7.374 per order. De pixel registreert daarnaast €86.100 waarde op zes registraties, dus €14.350 per registratie. Dat klopt niet. De Nozzle Up cijfers zijn wél plausibel (€1.180, €641, €208 gemiddelde order). Verifieer de zes SYBB orders in Odoo voor je hier iets op bouwt.

### PostHog

Nul betaalde sessies in 30 dagen. De oude landingspagina is dood: **startyourballoonbusiness.com haalde 4 pageviews.** Maar de SYBB event pagina's op sempertexeurope.com deden 270 pageviews en **93 unieke personen**, volledig organisch. SYBB verkoopt via de event pagina's, niet via de landing page.

Botverkeer onveranderd: Seychellen 279 bezoekers bij 1,00 pageview, Argentinië 189 bij 1,00, Brazilië 443 bij 1,04. Nieuw is het **VK op 2.153 bezoekers** bij 1,45, je grootste land nu, met een patroon dat meer op de botlanden lijkt dan op België of Nederland.

### Aanbeveling

De blokkade van elf rapporten is weg, maar zet nog geen budget aan. In deze volgorde: (1) verifieer de zes SYBB orders in Odoo, (2) filter de bots vóór je een nulmeting vastlegt, (3) richt op `/event/start-your-balloon-business-professional-*/register`, (4) ontrafel welke adset H13 op €0,07 kreeg, (5) herstart klein met 70% H11, 20% H15, 10% H13 in de winnende setup.

Rapport staat in `Output/Reports/Daily/2026-08-21_ads_report.md`, gecommit en gepusht (`0eb16e31`).

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
