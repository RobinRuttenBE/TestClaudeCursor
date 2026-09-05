# Meta Ads Rapport, 5 september 2026

**Periode:** last 30 days (6 augustus t/m 5 september 2026)
**Account:** Sempertex Ad Account (`act_567892422940728`), saldo €94,03
**Bronnen:** Meta Ads via Pipeboard (directe JSON-RPC, MCP meldt "requires authentication") en PostHog project STX EU (claude.ai connector). Geen Google MCPs gebruikt, niets naar de Google Sheet geschreven.

## Status: geen enkele campagne actief

Op 4 september tussen 11:50 en 11:52 zijn beide Wholesaler campagnes en alle 8 ads op PAUSED gezet. Dat is 25 minuten na de auto-optimize run, die om 11:25 alleen Statisch 1 (LIT) pauzeerde. Van de volledige pauze staat niets in de logs, dus dit is een handmatige actie. Sinds die tijd is er geen spend en geen verkeer meer: PostHog telt op 5 september 1 sessie op de wholesaler pagina.

De oudere campagnes (2026: SYBB, SYBB Kopie, drie Nozzle Up campagnes uit 2025) staan al maanden op PAUSED en hebben geen spend in de laatste 30 dagen. Het rapport hieronder is dus de eindafrekening van de Wholesaler campagnes over 27 augustus t/m 4 september.

## Overzicht per campagne (lifetime = last 30d)

| Campagne | Status | Spend | Impr. | Link clicks | Link CTR | Link CPC | CPM | Freq. | Leads Meta | Inzendingen PostHog | € / inzending |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,13 | 90.887 | 881 | 1,0% | €0,64 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | 696 | 1,8% | €0,73 | €12,92 | 3,29 | 8 | 8 | €63,41 |
| **Totaal** | | **€1.069,37** | **130.154** | **1.577** | **1,2%** | **€0,68** | **€8,22** | **3,73** | **19** | **33** | **€32,41** |

ROAS is niet van toepassing: dit zijn lead-campagnes zonder aankoopwaarde. Kostprijs per inzending is gebaseerd op PostHog `wholesaler_form_submit`, omdat de Meta pixel structureel te weinig telt (19 versus 33). Negen inzendingen hebben geen ad-UTM en zijn niet aan een campagne toe te wijzen; het totaal van €32,41 rekent alle 33 mee.

## Overzicht per ad

| Ad | Spend | Impr. | Link CTR | Link CPC | CPM | Freq. | Sessies PH | Inzendingen PH | € / inzending | Flag |
|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €146,91 | 19.041 | 1,3% | €0,61 | €7,72 | 1,90 | 241 | 5 | €29,38 | CPC |
| Statisch 1 (LIT) | €144,24 | 28.434 | 0,6% | €0,88 | €5,07 | 2,91 | 126 | 4 | €36,06 | CTR, CPC |
| Video 2 (LIT) | €143,74 | 17.267 | 1,0% | €0,80 | €8,32 | 2,52 | 127 | 5 | €28,75 | CPC |
| Statisch 2 (SWE) | €128,13 | 13.265 | 2,2% | €0,45 | €9,66 | 1,97 | 238 | 4 | €32,03 | |
| Statisch 2 (LIT) | €127,24 | 26.145 | 1,1% | €0,43 | €4,87 | 2,37 | 280 | 2 | €63,62 | |
| Video 2 (SWE) | €127,00 | 7.441 | 1,5% | €1,11 | €17,07 | 2,02 | 86 | 2 | €63,50 | CPC, CPM |
| Video 1 (SWE) | €126,75 | 8.299 | 1,7% | €0,91 | €15,27 | 2,05 | 99 | 0 | geen | CPC, CPM, 0 conv. |
| Statisch 1 (SWE) | €125,36 | 10.262 | 1,5% | €0,80 | €12,22 | 2,15 | 122 | 2 | €62,68 | CPC |

Link CTR en Link CPC zijn berekend op link clicks (niet op alle clicks, die ook likes en video plays meetellen). Op alle clicks zit iedere ad onder €0,60 CPC en boven 1% CTR.

## Verloop per dag (PostHog wholesaler pagina)

| Dag | Sessies | Form starts | Inzendingen | Meta spend |
|---|---|---|---|---|
| 27 aug | 35 | 27 | 6 | start LIT |
| 28 aug | 250 | 46 | 6 | start SWE |
| 29 aug | 208 | 12 | 4 | |
| 30 aug | 118 | 10 | 6 | |
| 31 aug | 158 | 10 | 5 | |
| 1 sep | 202 | 13 | 1 | |
| 2 sep | 159 | 5 | 3 | €125,88 |
| 3 sep | 209 | 5 | 1 | €153,91 |
| 4 sep | 57 | 4 | 1 | €55,70 (tot 11:50) |
| 5 sep | 1 | 0 | 0 | €0,00 |

De eerste vijf dagen leverden 27 inzendingen op, de laatste vier dagen 6. Het verkeer bleef tot de pauze stabiel rond 200 sessies per dag. In de laatste drie draaidagen kostte een inzending €67,10 tegenover ongeveer €25 in de eerste week. De vermoeidheid die gisteren werd gesignaleerd is dus bevestigd, en de pauze was daarmee verdedigbaar.

## Underperformers (drempels uit het command)

- **Video 1 (SWE)**: €126,75 uitgegeven, 0 inzendingen, CPM €15,27 (drempel €15,00), Link CPC €0,91. Aanbeveling: niet opnieuw activeren.
- **Video 2 (SWE)**: CPM €17,07, duurste link click van het account (€1,11), €63,50 per inzending. Aanbeveling: alleen terug met een nieuwe hook, niet met dit visual.
- **Statisch 1 (LIT)**: Link CTR 0,6% (drempel 1%), Link CPC €0,88. Al gepauzeerd door auto-optimize op 4 sep 11:25. Kanttekening: 3,2% sessie-naar-inzending, de hoogste van LIT. Het visual stopt mensen niet, maar wie klikt converteert wel.
- **Wholesaler (LIT) campagne**: frequency 3,97 (drempel 3,5) door vier ad sets op dezelfde audience. Bij een herstart: ad sets samenvoegen zodat Meta de frequency zelf verdeelt.
- **Link CPC boven €0,50**: alle ads behalve Statisch 2 (SWE) en Statisch 2 (LIT). Op alle clicks zit alles onder de drempel; het verschil tussen die twee getallen is groot bij de video's, wat wijst op veel engagement-clicks zonder doorklik.

## Top performers

- **Beste Link CTR**: Statisch 2 (SWE), 2,2% (4,0% op alle clicks).
- **Laagste Link CPC**: Statisch 2 (LIT), €0,43 (€0,20 op alle clicks).
- **Laagste kostprijs per inzending**: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 2 (SWE) €32,03.
- **Beste ROAS**: niet van toepassing (lead-campagnes).

## Samenvatting

- **Totaal spend**: €1.069,37 (last 30 days, volledig toewijsbaar aan de twee Wholesaler campagnes).
- **Resultaat**: 33 inzendingen via PostHog, 19 leads via Meta, €32,41 per inzending over de hele looptijd.
- **Beste performer**: Video 2 (LIT) en Video 1 (LIT). Samen €290,65 voor 10 inzendingen, goedkoopste leadbron van het account. Statisch 2 (SWE) is de Zweedse winnaar.
- **Slechtste performer**: Video 1 (SWE). €126,75 zonder één inzending, en de dure Zweedse reach maakt het niet goed.
- **Litouwen versus Zweden**: LIT levert per euro bijna twee keer zoveel inzendingen (€35,13 tegenover €63,41). Zweedse reach kost twee keer zoveel per 1.000 impressies.

## Aanbeveling (Hormozi 70-20-10)

Nu alles stilstaat is dit het moment om de herstart goed te doen in plaats van dezelfde ads opnieuw aan te zetten.

1. **Eerst tracking fixen, dan pas budget.** Meta telt 19 leads, PostHog 33, en 9 inzendingen hebben geen UTM. Zolang het Lead-event niet betrouwbaar vuurt, optimaliseert Meta op de helft van het signaal. Check of het formulier op `/en_GB/become-a-distributor` het pixel Lead-event triggert bij succesvolle verzending.
2. **70% op bewezen winnaars**: Video 1 (LIT), Video 2 (LIT) en Statisch 2 (SWE) opnieuw activeren. Richtbudget: LIT €60/dag, SWE €40/dag.
3. **20% op variaties**: dezelfde drie visuals met twee nieuwe hooks per land (alle 8 ads gebruikten tot nu toe exact dezelfde tekst). De vijf copy-varianten uit het auto-optimize rapport van 4 september liggen klaar.
4. **10% experiment**: Statisch 1 (LIT) met een nieuwe eerste zin, omdat de landing conversie van dat visual de beste is.
5. **Niet terugbrengen**: Video 1 (SWE). Video 2 (SWE) alleen als hook-test binnen de 20%.
6. **Structuur**: LIT ad sets samenvoegen naar één ad set met meerdere ads, zodat de frequency onder 3,5 blijft.

## Google Sheet

Overgeslagen op verzoek. Dit rapport is alleen lokaal opgeslagen.

## Opmerkingen

- Het account `act_607231713057715` uit het command bestaat niet in de koppeling. Het tweede account is AmbitionAvenue (`act_1489853856181844`), zonder campagnes of spend.
- Wil je funnel data toevoegen? Geef dan de stappen na de inzending: gesprek gepland, distributeur geactiveerd, eerste order. Die zitten niet in Meta of PostHog. Met die cijfers kan ik een volledige funnel-diagnose draaien.
