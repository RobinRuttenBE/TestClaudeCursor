Rapport staat in `Output/Reports/Daily/2026-09-08_ads_report.md`, gecommit en gepusht (25618073). Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 8 september 2026

**Databronnen.** De Pipeboard MCP vroeg om authenticatie en de PostHog MCP gaf HTTP 405. Beide werkten via de directe route met de geconfigureerde tokens, dus dit rapport bevat echte 30-daagse cijfers (9 augustus t/m 7 september).

**Geen actieve campagnes.** Alle zeven campagnes staan op pauze. De Wholesaler campagnes (SWE en LIT) zijn sinds 4 september uit en Meta registreert 0 spend van 5 t/m 8 september. De laatste PostHog-inzending kwam op 4 september. Ten opzichte van gisteren is er niets veranderd behalve het venster dat één dag opschoof.

**Overzicht per campagne**

| Campagne | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |

Totaal €1.069,38 spend, 1.410 betaalde sessies, 23 geattribueerde inzendingen plus 9 zonder UTM. Meta telde 277 landing page views tegenover 1.410 PostHog-sessies, dus funnel-conclusies blijven op PostHog gebaseerd. ROAS is niet van toepassing bij lead-campagnes.

**Underperformers**
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27 en 0 inzendingen op 113 sessies. Definitief uit.
- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, €63,50 per inzending. Niet herstarten.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar de beste kosten per inzending (€28,75). Behouden.
- **Wholesaler (LIT)**: frequency 3,97. Inzendingen zakten vanaf 1 september van 16 naar 6 bij gelijk verkeer. Creative fatigue.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20), maar 290 sessies leveren maar 2 inzendingen op. Budget verlagen.

**Top performers**
- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38

**Aanbeveling (70-20-10):** bij herstart 70% naar de bewezen LIT-set (Video 1, Video 2, Statisch 1), 20% naar Statisch 2 (SWE), 10% naar één nieuwe creative per markt om de frequentie te doorbreken. Beide SWE-video's niet herstarten. De vijf herstart-voorstellen van 3 september wachten nog op je goedkeuring.

**Wil je funnel data toevoegen?** Gesprekken gepland, distributeurs actief en eerste orders zitten niet in Meta of PostHog. Lever die aan en ik draai de volledige funnel-diagnose.
