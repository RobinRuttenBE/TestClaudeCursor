# Meta Ads Rapport, 12 september 2026

Bronnen: Pipeboard Meta Ads via directe JSON-RPC call (MCP meldde "requires authentication") en PostHog project STX EU via directe REST call (MCP gaf HTTP 405). Geen Google MCPs aangeroepen, niets naar de Google Sheet "Meta Ads Tracker" geschreven. Periode: 13 augustus t/m 12 september 2026 (last 30d).

**Beperking van deze run:** Pipeboard viel na drie calls terug op de weeklimiet van het Free plan ("You've used all your trial commands and reached the weekly limit"). Campagne-lijst en campagne-level insights zijn vandaag live opgehaald. Ad-level Meta cijfers komen uit het rapport van 7 september over dezelfde leveringsperiode; omdat er sinds 4 september geen levering is, zijn die ongewijzigd. Ad-level PostHog cijfers (sessies, inzendingen) zijn wel live van vandaag.

## Status

**Er draait niets.** Alle 7 campagnes in act_567892422940728 staan op PAUSED. De twee Wholesaler Campagnes (SWE en LIT) zijn op 4 september gepauzeerd. PostHog bevestigt de stilstand: 58 betaalde sessies op 4 september, daarna 0 tot 2 per dag (2 op 6 september, 1 op 7 september, 2 op 9 september, nalopers op oude ad-URL's). Laatste form-inzending: 4 september. Negende dag op rij zonder levering.

Account act_607231713057715 uit de command bestaat niet in Pipeboard. Het tweede account act_1489853856181844 (AmbitionAvenue) is leeg.

## Overzicht per campagne (last 30d)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending (PostHog) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused sinds 4 sep | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler Campagne (SWE) | Paused sinds 4 sep | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | 3,77 | 19 | 23 (+9 zonder UTM) | €46,49 |

ROAS is niet van toepassing, het zijn lead-campagnes (OUTCOME_LEADS). Meta telt 277 landing page views en 19 leads, PostHog 1.412 betaalde sessies en 32 inzendingssessies (23 met ad-UTM, 9 organisch of zonder UTM). De pixel ondertelt structureel, dus kosten per inzending zijn op PostHog gebaseerd.

De vijf oudere campagnes (2026: SYBB, 2026: SYBB - Kopie, drie Nozzle Up campagnes uit 2025) hebben in de laatste 30 dagen 0 spend en 0 impressions.

## Ad-level (PostHog live, Meta ad-cijfers per 7 sep)

| Ad | Sessies | Bounces | Gem. duur | Inzendingen | Conversie | Bekende Meta-cijfers |
|---|---|---|---|---|---|---|
| Statisch 2 (LIT) | 292 | 82 | 52s | 2 | 0,7% | CPC €0,20 (laagste) |
| Statisch 2 (SWE) | 256 | 57 | 114s | 3 | 1,2% | CTR 4,0% (hoogste) |
| Video 1 (LIT) | 248 | 76 | 69s | 5 | 2,0% | €29,38 per inzending |
| Video 2 (LIT) | 141 | 42 | 96s | 5 | 3,5% | CPC €0,58, €28,75 per inzending (beste) |
| Statisch 1 (LIT) | 134 | 39 | 103s | 4 | 3,0% | link CTR 0,6%, €36,06 per inzending |
| Statisch 1 (SWE) | 131 | 26 | 210s | 2 | 1,5% | langste sessies |
| Video 1 (SWE) | 113 | 23 | 75s | 0 | 0,0% | CPC €0,53, CPM €15,27 |
| Video 2 (SWE) | 97 | 23 | 74s | 2 | 2,1% | CPC €0,69, CPM €17,07, €63,50 per inzending |

## Underperformers

- **Video 1 (SWE)**: CPC €0,53 (drempel €0,50) en CPM €15,27 (drempel €15,00), 0 inzendingen op 113 sessies. Aanbeveling: niet herstarten.
- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, duurste klik en duurste reach van alle acht ads. Aanbeveling: niet herstarten in deze vorm, wel de LIT Video 2 hook naar het Zweeds vertalen.
- **Wholesaler (LIT)**: frequency 3,97 (drempel 3,5). Klein Litouws publiek was na twee weken verzadigd. Aanbeveling: verse creatives voordat de campagne herstart.
- **Statisch 2 (LIT)**: goedkoopste klik (€0,20) maar 0,7% conversie en de kortste sessies (52s). Klikt goedkoop, converteert niet. Aanbeveling: nieuwe hook testen in het 10%-budget.
- **Statisch 1 (LIT)**: link CTR 0,6% (drempel 1%), maar 3,0% conversie en €36,06 per inzending. Aanbeveling: behouden, lage CTR is hier geen kill-reden.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar de beste kosten per inzending (€28,75) en hoogste conversie (3,5%). Aanbeveling: behouden.

## Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Beste kosten per inzending**: Video 2 (LIT) €28,75, daarna Video 1 (LIT) €29,38
- **Beste ROAS**: niet van toepassing (lead-campagnes)

## Funnel op /become-a-distributor (30d, alle verkeer)

| Stap | Aantal | Ratio |
|---|---|---|
| Pageviews | 1.587 | |
| Form starts | 137 | 8,6% van pageviews |
| Form submits | 35 | 25,5% van starts |
| Form errors | 21 (11 sessies) | |

Het grote lek zit vóór het formulier: ruim 91% van de bezoekers begint niet aan het formulier. Sinds de pauze krijgt de pagina 1 tot 8 sessies per dag, vrijwel allemaal organisch.

## Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days), alles vóór 5 september
- **Beste performer**: Wholesaler (LIT), €35,13 per inzending, 16 inzendingen, CPM €6,18
- **Slechtste performer**: Wholesaler (SWE), €72,46 per inzending; de twee SWE-video's zijn de duurste ads van het account
- **Aanbeveling (70-20-10)**: bij herstart 70% naar de bewezen LIT-set (Video 1, Video 2, Statisch 1) plus Statisch 2 (SWE), met verse creatives tegen de frequentie. 20% naar een Zweedse variant van Video 2 (LIT). 10% naar een nieuwe hook voor Statisch 2 (LIT). De vijf herstart-voorstellen van 3 september wachten nog op goedkeuring.

## Google Sheet

Overgeslagen op verzoek. Niet geschreven naar "Meta Ads Tracker".
