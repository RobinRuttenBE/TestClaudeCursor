Het rapport staat in `Output/Reports/Daily/2026-09-14_ads_report.md`, gecommit en gepusht (a7099958). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 14 september 2026

**Er draait niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september 11:50. Meta geeft voor de laatste 7 dagen nul rijen. PostHog bevestigt dat live: na 4 september nog 5 nalopers (6, 7 en 9 september), nul betaald verkeer op 10 t/m 13 september. Laatste inzending blijft 4 september.

**Goed nieuws:** Pipeboard werkte vandaag weer, de weeklimiet was gewoon gereset ondanks de resetdatum van 21 september in het antwoord van gisteren. Alle Meta-cijfers zijn vandaag vers opgehaald.

**Overzicht per campagne (last 30d)**

| Campagne | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | **€1.069,38** | 2,2% | €0,37 | €8,22 | | 19 | 23 (+12 zonder UTM-match) | €30,55 all-in |

ROAS niet van toepassing, het zijn lead-campagnes. Meta telt 19 leads tegenover 35 inzendingen in PostHog, dus kosten per inzending zijn op PostHog gebaseerd.

**Underperformers**

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, 0 inzendingen op 97 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar kortste sessies (52s), 0,8% conversie, €63,63 per inzending. Nieuwe hook testen.
- **Video 2 (LIT)** en **Statisch 1 (LIT)** krijgen een CPC- of CTR-vlag maar zijn de beste converteerders (4,1% en 3,8%). Behouden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38

**Funnel /become-a-distributor (30d):** 1.743 pageviews, 137 formulierstarts, 35 inzendingen.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. De herstart-voorstellen van 3 september wachten nog op jouw goedkeuring.

**Operationeel:** vier Pipeboard-calls gebruikt in deze run. Een campagne-lijst met status_filter hing 60 seconden, zonder filter kwam hij direct terug. Dat staat nu in het geheugen. Het voorstel om één gedeelde Meta-call per dag te cachen voor de drie rapporten blijft staan, anders valt de route later deze week opnieuw dicht.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.
