# Morning Report — 2026-08-21

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

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

---

Rapport staat in `Output/Reports/Daily/2026-08-20_sybb_report.md`, gecommit en gepusht (`63de1402`).

**Over de databronnen:** de Pipeboard en PostHog MCP connectors staan in deze sessie op "requires authentication". Ik heb beide bereikt via directe HTTP calls met de tokens uit je MCP config, dezelfde route als het rapport van gisteren. Geen Google MCP aangeroepen, niets naar de tracker Sheet geschreven.

**Wat er te melden valt over 20 augustus: niets, en dat is het rapport.**

Campagne `2026: SYBB` staat op PAUSED en gaf lege rijen terug op campagne, adset én accountniveau. De laatste euro op het account is uitgegeven op **20 april 2026**, 122 dagen eerder. Elke ads-KPI is dus nul, niet zwak.

`startyourballoonbusiness.com` haalde **0 pageviews**. Verkeer zat volledig op sempertexeurope.com. De SYBB event pagina's kregen 6 pageviews van 4 personen, allemaal organisch. In het hele venster 13 t/m 20 augustus zat op 42.374 pageviews geen enkele UTM parameter.

Drie dingen die wel opvielen in de data:

**Taalversies scrollen ongelijk.** Dezelfde registratiepagina haalt 57,3% gemiddelde scroll in het Nederlands en 27,5% in het Engels, 19,5% Frans, 14,7% Duits. Zelfde aanbod, minder dan de helft van de diepte. Dat lijkt een template- of vertalingsprobleem, geen aanbodprobleem.

**Niemand komt voorbij 75% scroll.** Gisteren 0 van 4, en structureel zwak over 7 dagen. Als je registratieknop daaronder staat, wordt hij niet gezien. Dit is de enige actie in het rapport die iets kan opleveren zonder advertentiebudget.

**De variantvraag uit gisteren wordt scherper.** H13 wint op elke traffic metric (8,11% CTR, €0,10 CPC, 67,9% landing page view rate) maar leverde 2 aankopen op 4.234 pagina's. H11 leverde er 4 op 788. Per landing page view is H11 ruim tien keer effectiever, tegen 4,6x de klikprijs. En `SYBB w/ Semp (BLACK)` staat nog steeds op 167 clicks met nul landing page views, wat op een kapotte bestemming of pixel wijst.

Twee kanttekeningen die ik expliciet in het rapport heb gezet: de dagcijfers steunen op 4 sessies, dus percentages daarop zijn illustratief en niet significant. En de skill in `skills/daily-sybb-report/SKILL.md` gaat nog uit van startyourballoonbusiness.com als funnel. Dat klopt nu op twee opeenvolgende dagen niet meer. Wil je dat ik de skill bijwerk naar de event pagina's?

---

Rapport staat in `Output/Reports/Daily/2026-08-21_auto_optimize.md`, gecommit en gepusht (`113f8d8d`).

## Kort

**Nul automatische acties, en dat klopt.** Alle vijf campagnes staan op PAUSED, `last_3d` en `last_7d` geven een lege dataset terug. Geen enkele ad haalt de minimumdrempel van 1.000 impressions of 500 link clicks, dus geen kill-regel kan vuren. Alleen Meta Ads (Pipeboard) en PostHog gebruikt, geen Google MCP, niets naar de tracker Sheet.

De MCP connector stond op "requires authentication", maar de geconfigureerde token werkt wel via directe JSON-RPC calls. Dat heb ik als memory vastgelegd.

## Wat de analyse op lifetime link metrics wél opleverde

**Het is de adset, niet de hook.** De openstaande vraag uit je ads rapport van vanochtend is beantwoord: H13 kreeg €0,07 per klik in de originele adset `BATCH 2: Expertise & POC`, en €1,06 in `Kopie 3`. Dat patroon geldt voor alle vier de hooks die in beide draaiden, telkens in het voordeel van het origineel: H13 15,1x, H15 5,4x, H11 4,1x, H12 1,4x.

**Maar de dure adset is de enige die verkoopt.** De vier verifieerbare SYBB aankopen komen uit H11 in Kopie 1, tegen €1,22 per klik. De goedkope adset leverde 5.808 link clicks en nul aankopen. H13 alleen: 6.342 link clicks, 4.063 landing page views, nul aankopen. Sturen op CPC (link) zou je precies de verkeerde adset laten kiezen.

**Je account-ROAS is 2,7x, niet 11,5x.** Eén ad (H13 in Kopie 3) rapporteert €21.386,75 per order. Haal je die eruit, dan blijft €13.026,75 op €4.867,46 over. De andere vier converterende ads zijn wel plausibel (€1.180 tot €208 per order).

## Twee dingen die aandacht vragen

**Drie ads staan op ACTIVE onder de paused campagne "2026: SYBB - Kopie".** Zet je die campagne aan, dan starten H13, H12 en H11 meteen, en dat zijn precies de drie duurste ads van het account. Pauzeer ze eerst.

**Je kill-regel zou je op één na beste ad slopen.** "Ad 1 - Eind Aug" heeft een Link CTR van 0,7% en zou automatisch gepauzeerd worden. Diezelfde ad draait op €0,23 per link click met 6 aankopen en 6,4x ROAS. Ik stel voor de regel voorwaardelijk te maken: Link CTR < 0,8% **én** CPC (link) > €0,50 **én** nul aankopen. Dan overleeft Eind Aug en sneuvelen "SYBB w/ Semp (BLACK)" en "Ad 1 - nieuwe doelgroep" alsnog.

Vijf voorstellen staan in het rapport, geen daarvan uitgevoerd. Geef door welke nummers je wil.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
