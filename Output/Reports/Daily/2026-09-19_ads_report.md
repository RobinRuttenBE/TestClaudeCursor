Het rapport staat in `Output/Reports/Daily/2026-09-19_ads_report.md`, gecommit en gepusht (f3ec6ab8). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 19 september 2026

**Meta was vandaag niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie en de directe route zat op de eerste call op de weeklimiet (30 van 30, reset maandag 21 september). De Meta-cijfers komen uit het live extract van 16 september. PostHog bevestigde dat het 30d-venster van vandaag exact dezelfde levering bevat: nul betaalde sessies tussen 14 en 26 augustus en nul sinds 10 september. De cijfers zijn dus ongewijzigd geldig. Het rapportbestand van gisteren bevat alleen een foutmelding over verbruikte Claude usage credits, dus dit is het eerste volledige rapport sinds 17 september.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Zestiende dag zonder levering.

**Overzicht per campagne (last 30d, 20 aug t/m 19 sep)**

| Campagne | Spend | Impr. | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 90.888 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 39.267 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 |
| **Totaal** | **€1.069,38** | 130.155 | 2,2% | €0,37 | €8,22 | | 19 | 33 (+1 organisch) | €32,41 all-in |

ROAS niet van toepassing, het zijn lead-campagnes. De all-in kosten per inzending stegen van €30,55 naar €32,41 puur omdat twee oudere organische inzendingen uit het venster vielen, niet door een prestatieverandering.

**Nieuw signaal:** op 18 september kwam de eerste inzending sinds 4 september binnen, organisch, van een bezoeker uit Letland via Google of direct. Geen betaald verkeer die dag. Dit is de eerste inzending ooit uit Letland en een argument om Letland bij herstart aan de LIT-targeting toe te voegen.

**Underperformers**

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar 0,7% conversie en €63,63 per inzending. Nieuwe hook testen.
- **Video 2 (LIT)** en **Statisch 1 (LIT)** raken een drempel maar converteren het best (3,5% en 3,0%). Behouden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 2 (SWE) €32,03

**Funnel /become-a-distributor (30d):** 1.698 pageviews, 138 formulierstarts, 21 fouten, 34 inzendingen. Van start naar inzending komt maar 24,6% door. Dat lek eerst dichten vóór herstart.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. De zes voorstellen van 3 en 16 september wachten nog op jouw goedkeuring.

**Operationeel:** tot maandag 21 september draaien alle Meta-rapporten op het extract van 16 september. Voorstel 6 (één gedeeld Meta-extract per dag cachen voor de drie rapporten) blijft urgent, anders is de limiet elke week vanaf woensdag vol.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.
