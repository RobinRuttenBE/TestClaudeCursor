## Meta Ads Rapport, 19 september 2026

**Databronnen:** Pipeboard Meta Ads (directe JSON-RPC route) en PostHog (directe REST-route, project STX EU 149694). Geen Google MCPs aangeroepen, niets naar de Google Sheet geschreven. Het rapportbestand van 18 september bevat alleen een foutmelding over verbruikte usage credits, dus dit is het eerste volledige rapport sinds 17 september.

**Meta was vandaag niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie en de directe route kreeg op de eerste call `weekly_limit_exceeded` (30 van 30, plan free, reset 21 september 2026 00:00 UTC). Er zijn geen verdere Meta-calls gedaan. De Meta-cijfers komen uit het laatste live extract van 16 september 09:03. PostHog bevestigt dat het 30d-venster van vandaag (20 augustus t/m 19 september) exact dezelfde levering bevat: nul betaalde sessies (`utm_source=facebook`) tussen 14 en 26 augustus en nul sinds 10 september. Spend, impressies, CTR, CPC, CPM en leads zijn dus ongewijzigd geldig.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september 11:50. Zestiende dag zonder levering. SYBB (`2026: SYBB`) staat sinds 19 april op PAUSED; de drie sessies met SYBB-UTM op 23 en 28 augustus zijn link-preview hits op de oude ad-URL, geen levering.

### Overzicht per campagne (last 30d, 20 aug t/m 19 sep)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending | ROAS |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler Campagne (LIT) | Paused sinds 4 sep | €562,14 | 90.888 | 1.606 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 | n.v.t. |
| Wholesaler Campagne (SWE) | Paused sinds 4 sep | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 | n.v.t. |
| 2026: SYBB | Paused sinds 19 apr | €0,00 | 0 | 0 | 0,0% | n.v.t. | n.v.t. | n.v.t. | 0 | 0 | n.v.t. | n.v.t. |
| Overige 4 campagnes | Paused | €0,00 | 0 | 0 | | | | | 0 | 0 | | |
| **Totaal** | | **€1.069,38** | **130.155** | **2.843** | **2,2%** | **€0,37** | **€8,22** | | **19** | **33 tijdens levering (+1 organisch 18 sep)** | **€32,41 all-in** | n.v.t. |

ROAS is niet van toepassing, het zijn lead-campagnes. Kosten per inzending zijn op PostHog gebaseerd omdat de Meta pixel op deze pagina structureel te weinig telt. Clicks zijn afgeleid van spend en CPC uit het extract van 16 september.

De all-in kosten per inzending gaan van €30,55 (17 september) naar €32,41. Dat is geen prestatieverandering: twee organische inzendingen van vóór 20 augustus vielen uit het venster.

### Underperformers (per ad, uit het extract van 16 september)

- **Video 2 (SWE)**: CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15,00). Aanbeveling: niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53 (drempel €0,50), CPM €15,27 (drempel €15,00), nul inzendingen op 113 sessies. Aanbeveling: definitief uit.
- **Wholesaler Campagne (LIT)**: frequency 3,97 (drempel 3,5), publiek verzadigd. Aanbeveling: verse creatives bij herstart, geen herstart van dezelfde set.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar 0,7% sessie-naar-inzending en €63,63 per inzending. Aanbeveling: nieuwe hook testen, niet mechanisch pauzeren op CPC.
- **Video 2 (LIT)** en **Statisch 1 (LIT)**: raken een CPC- of CTR-drempel maar converteren het best (3,5% en 3,0%). Aanbeveling: behouden.

### Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,0%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Beste ROAS**: n.v.t. (lead-campagnes). Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 2 (SWE) €32,03

### Funnel /become-a-distributor (30d, 20 aug t/m 19 sep, PostHog)

| Stap | Aantal | Doorstroom |
|---|---|---|
| Pageviews (`wholesaler_page_view`) | 1.698 | |
| Formulierstarts | 138 | 8,1% van pageviews |
| Formulierfouten | 21 | 15,2% van starts |
| Inzendingen | 34 | 24,6% van starts |

Van start naar inzending komt nog steeds maar een kwart door. Dat lek eerst dichten vóór er weer budget op gaat.

**Nieuw sinds 17 september:** op 18 september om 10:56 UTC kwam één organische inzending binnen, een bezoeker uit Letland (LV) via Google of direct, zonder UTM. Het is de eerste inzending sinds 4 september en de eerste uit Letland. Geen betaald verkeer die dag. Dat is een signaal dat de Baltische markt ook zonder ads reageert; neem het mee in de herstart-afweging voor de LIT-campagne (Litouwen, Letland, Estland als één doelgroep). Verder op 16 t/m 18 september: 14 organische pageviews, 4 formulierstarts, 1 inzending.

### Samenvatting

- **Totaal spend**: €1.069,38 (periode: last 30 days, alle spend tussen 27 augustus en 4 september)
- **Beste performer**: Video 2 (LIT), laagste kosten per inzending (€28,75) en hoogste sessie-naar-inzending ratio (3,5%)
- **Slechtste performer**: Video 1 (SWE), CPC en CPM boven drempel en nul inzendingen op 113 sessies
- **Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives tegen de frequency van 3,97; 20% naar een Zweedse variant van Video 2 (LIT); 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Overweeg Letland toe te voegen aan de LIT-targeting op basis van de organische inzending van 18 september. De zes herstart-voorstellen van 3 en 16 september wachten nog op goedkeuring van Robin.

### Operationeel

- Meta blijft tot maandag 21 september onbereikbaar via Pipeboard (weeklimiet). Alle Meta-rapporten draaien tot dan op het extract van 16 september.
- Voorstel 6 (één gedeeld Meta-extract per dag cachen voor ads-report, SYBB-rapport en auto-optimize) blijft urgent. Zonder cache is de limiet van 30 calls elke week vanaf woensdag vol.
- Het rapport van 18 september is mislukt door verbruikte usage credits van Claude, niet door een databron.

### Google Sheet

Overgeslagen op verzoek. Niets naar "Meta Ads Tracker" geschreven; output alleen lokaal in dit bestand.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.
