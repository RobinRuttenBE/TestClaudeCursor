## Meta Ads Rapport, 21 augustus 2026

**Pipeboard werkt weer.** Voor het eerst in twaalf dagen is er live data. De MCP connector zelf staat nog steeds op "requires authentication" in deze sessie, maar de Pipeboard endpoint accepteert je project token wel via directe HTTP calls. Alle cijfers hieronder komen daar vandaan. PostHog idem, via de API met je persoonlijke key. Geen enkele Google MCP aangeroepen, stap 6 overgeslagen zoals gevraagd.

Eén correctie op het commando: `act_607231713057715` (Robin Rutten) bestaat niet. Het tweede account is `act_1489853856181844` (AmbitionAvenue), nul campagnes, nul spend, nul historie.

### Overzicht per campagne

Geen enkele actieve campagne in beide accounts. Alle vijf campagnes staan op PAUSED. Cijfers zijn lifetime, want de laatste 30 dagen leverden nul rijen op.

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

Totaal lifetime: **€4.867,46**. Dat is exact het accountsaldo, dus de vijf campagnes dekken je volledige Meta historie.

**Laatste 30 dagen: €0,00.** De laatste euro die je op Meta uitgaf was in **april 2026**. Vier maanden donker.

| Maand 2026 | Campagne | Spend | Impressions | CTR | CPC |
|---|---|---|---|---|---|
| Januari | 2026: SYBB | €101,74 | 16.268 | 1,0% | €0,61 |
| Maart | 2026: SYBB | €1.323,83 | 189.067 | 5,3% | €0,13 |
| April | 2026: SYBB | €1.059,47 | 91.839 | 2,1% | €0,55 |
| April | 2026: SYBB - Kopie | €124,42 | 7.615 | 2,6% | €0,64 |
| Mei t/m augustus | geen | €0,00 | 0 | n.v.t. | n.v.t. |

### Ad-niveau, 2026: SYBB

Tien ads, gesorteerd op spend. Dit is je bibliotheek voor het moment dat je herstart.

| Ad | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq | LPV | Aankopen | Leads |
|---|---|---|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | €521,56 | 38.614 | 784 | 2,0% | €0,67 | €13,51 | 1,85 | 343 | **4** | 0 |
| H13, B3, CTA5 | €421,29 | 60.074 | 5.902 | **9,8%** | **€0,07** | €7,01 | 1,57 | **4.063** | 0 | 3 |
| H12, B3, CTA5 | €388,40 | 48.166 | 1.248 | 2,6% | €0,31 | €8,06 | 1,78 | 485 | 0 | 5 |
| H14, B3, CTA5 | €232,36 | 33.235 | 911 | 2,7% | €0,26 | €6,99 | 1,46 | 465 | 0 | 1 |
| H15, B3, CTA5 | €218,96 | 34.299 | 1.465 | 4,3% | €0,15 | €6,38 | 1,50 | 845 | 0 | 0 |
| H13, B3, CTA5 | €206,99 | 16.766 | 331 | 2,0% | €0,63 | €12,35 | 1,64 | 171 | **2** | 0 |
| H11, B3, CTA5 | €202,48 | 31.060 | 796 | 2,6% | €0,25 | €6,52 | 1,63 | 445 | 0 | **6** |
| H12, B3, CTA5 | €141,43 | 13.955 | 356 | 2,6% | €0,40 | €10,13 | 1,95 | 139 | 0 | 0 |
| SYBB w/ Semp (BLACK) | €101,74 | 16.268 | 167 | **1,0%** | €0,61 | €6,25 | 1,81 | 0 | 0 | 0 |
| H15, B3, CTA5 | €49,83 | 4.737 | 107 | 2,3% | €0,47 | €10,52 | 1,45 | 36 | 0 | 0 |

De drie ads in 2026: SYBB - Kopie (H11, H12, H13) draaiden samen €124,42 met CPM's van €13,57 tot €19,14 en nul conversies. Dat was een mislukte hertest, geen campagne.

### Underperformers

- **2026: SYBB - Kopie** (campagne), CPC €0,64 en CPM €16,34, beide boven drempel, nul aankopen op 195 clicks. Aanbeveling: niet reactiveren, archiveren.
- **Nozzle Up END OF AUGUST**, CTR 1,0%, precies op de drempel bij 369.136 impressions. De CPM van €1,64 is uitzonderlijk laag, dus dit was brede goedkope reach zonder engagement. Aanbeveling: als reach-campagne prima geweest, niet als sales-template hergebruiken.
- **SYBB w/ Semp (BLACK)** (ad), CTR 1,0% en CPC €0,61 en **nul** landing page views op 167 clicks. Nul LPV bij 167 clicks betekent dat de pixel op de bestemming niet vuurde of de pagina niet laadde. Aanbeveling: dood laten, en vóór herstart de bestemming testen.
- **H13, B3, CTA5** (de €206,99 variant), CPC €0,63 tegenover €0,07 voor dezelfde hook in de andere adset. Aanbeveling: zie de opmerking hieronder, dit is het interessantste getal in het rapport.
- **Last push Nozzle Up**, ROAS 0,8x, de enige campagne die aantoonbaar geld verloor.

Frequency is nergens een probleem. Hoogste is 2,89 (Campagne Nozzle Up 2025 1), ruim onder de 3,5.

### Top performers

- **Beste CTR**: H13, B3, CTA5 (2026: SYBB), **9,8%**
- **Laagste CPC**: H13, B3, CTA5 (2026: SYBB), **€0,07**
- **Beste ROAS**: 2026: SYBB, **17,8x** (zie voorbehoud)
- **Meest efficiënte reach**: Nozzle Up END OF AUGUST, CPM €1,64

### Dezelfde hook, 8,8x prijsverschil

H13 draaide twee keer. De ene keer 9,8% CTR bij €0,07 per klik, de andere keer 2,0% CTR bij €0,63. Zelfde hook, zelfde body, zelfde CTA. Het verschil zit dus niet in de creative maar in de delivery: targeting, plaatsingen of het moment.

Dit betekent iets ongemakkelijks voor je 70-20-10 verdeling. Je "bewezen winnaars" zijn niet bewezen op hookniveau zolang je de adset-context niet meeneemt. Voordat je 70% van je budget op H13 zet, moet je weten welke van de twee setups die €0,07 opleverde.

En de tweede ongemakkelijkheid: **H13 leverde 4.063 landing page views op en nul aankopen.** H11 leverde 343 LPV op en alle vier de aankopen, tegen bijna tien keer de klikprijs. Goedkoop verkeer dat niets doet is duurder dan duur verkeer dat converteert. Je goedkoopste ad is op dit moment je slechtste ad.

### Voorbehoud bij de ROAS cijfers

De ROAS van 2026: SYBB is 17,8x op papier: €44.247 aan pixel-omzet op €2.485 spend. Maar dat is €7.374 gemiddeld per aankoop over zes aankopen, en de pixel registreert daarnaast €86.100 aan waarde op zes `complete_registration` events. Dat is €14.350 per registratie. Die waarde klopt niet.

De Nozzle Up campagnes zien er wel plausibel uit voor B2B groothandel: €1.180, €641 en €208 gemiddelde orderwaarde. Het probleem zit specifiek in de SYBB conversiewaarden.

**Behandel 17,8x niet als feit.** Verifieer eerst in Odoo wat die zes orders werkelijk waard waren, anders bouw je je hele herstart op een verkeerd getal.

### PostHog, wat gebeurt er zonder ads

Nul betaalde sessies in de laatste 30 dagen. Geen `utm_source=meta`, geen `utm_medium=cpc`. Consistent met €0,00 spend.

De oude landingspagina is dood: **www.startyourballoonbusiness.com haalde 4 pageviews in 30 dagen.**

Maar SYBB zelf leeft, op sempertexeurope.com:

| SYBB Professional registratiepagina's, 30d | |
|---|---|
| Pageviews | 270 |
| Sessies | 107 |
| Unieke personen | **93** |

Herkomst: 231 pageviews vanaf sempertexeurope.com zelf, 33 direct, 2 via Google. Volledig organisch en intern verkeer, nul euro advertentiebudget.

Dat bevestigt opnieuw wat er in het geheugen staat: **SYBB verkoopt via de event pagina's, niet via de landing page.** Elke euro die je straks naar startyourballoonbusiness.com stuurt, stuur je naar een pagina die je eigen bezoekers al hebben verlaten.

### Botverkeer, nog steeds niet opgelost

De 1,00-pageview-per-bezoeker signatuur uit het rapport van 18 augustus staat er onveranderd:

| Land (7d) | Bezoekers | Pageviews | Views per bezoeker |
|---|---|---|---|
| België | 354 | 10.139 | 28,6 |
| Nederland | 376 | 8.135 | 21,6 |
| Duitsland | 700 | 5.100 | 7,3 |
| Frankrijk | 609 | 2.613 | 4,3 |
| Brazilië | 443 | 461 | **1,04** |
| **Seychellen** | **279** | **279** | **1,00** |
| Argentinië | 189 | 189 | **1,00** |

Nieuw sinds vorige week: het **Verenigd Koninkrijk staat nu op 2.153 bezoekers**, veruit je grootste land, bij 1,45 pageviews per bezoeker. Dat patroon lijkt meer op de botlanden dan op België of Nederland. Het kan echte groei zijn, het kan hetzelfde verkeer via een andere exit node zijn. Uitzoeken vóór je een nulmeting vastlegt.

### Samenvatting

- **Totaal spend**: €0,00 (periode: laatste 30 dagen). Lifetime €4.867,46.
- **Beste performer**: 2026: SYBB. 4,1% CTR bij €0,21 CPC over 297.174 impressions is sterk boven je target van €0,50. De ROAS van 17,8x moet je eerst verifiëren.
- **Slechtste performer**: Last push Nozzle Up. €800,78 spend, drie aankopen, €623 omzet. ROAS 0,8x, het enige aantoonbare verlies.
- **Grootste blinde vlek**: je hebt vier maanden aan gedragsdata gemist terwijl SYBB organisch 93 mensen per maand naar de registratiepagina's trekt.

### Aanbeveling

Pipeboard werkt weer. Dat was elf rapporten lang de blokkade, en die is nu weg. Maar zet nog geen budget aan, in deze volgorde:

1. **Verifieer de zes SYBB aankopen in Odoo.** Als de werkelijke orderwaarde ver onder €7.374 ligt, is je beste campagne niet je beste campagne, en bouw je je 70-20-10 verdeling op een pixelfout.
2. **Filter de bots in PostHog.** Seychellen, Argentinië en Brazilië eruit, en bepaal wat het VK werkelijk is. Zonder dit vergelijk je straks je advertentieverkeer met een vervuilde nulmeting en trekt je elke conclusie de verkeerde kant op.
3. **Zet de bestemming op de event pagina's**, `/event/start-your-balloon-business-professional-*/register`, niet op startyourballoonbusiness.com. Die pagina haalt 4 pageviews per maand.
4. **Ontrafel eerst het H13 raadsel** voordat je 70% van je budget verdeelt. Zoek uit welke adset €0,07 per klik leverde. Die adset is je echte bewezen winnaar, niet de hook.
5. **Herstart klein.** 70% op H11 (de enige ad met aankopen, ondanks €0,67 CPC), 20% op H15 (4,3% CTR bij €0,15, het beste compromis tussen prijs en engagement), 10% op H13 in de winnende setup als test of dat goedkope verkeer met een betere bestemming wél converteert.

Archiveer 2026: SYBB - Kopie en Last push Nozzle Up. Die hoeven niet terug.

### Google Sheet
Overgeslagen op verzoek. Rapport opgeslagen in `Output/Reports/Daily/2026-08-21_ads_report.md`.
