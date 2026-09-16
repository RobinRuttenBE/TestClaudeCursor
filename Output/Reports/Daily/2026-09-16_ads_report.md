Het rapport staat in `Output/Reports/Daily/2026-09-16_ads_report.md`, gecommit en gepusht (31399fbf). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 16 september 2026

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september 11:50. Meta geeft voor 9 t/m 15 september nul rijen. PostHog bevestigt dat: na 4 september nog 5 nalopers, nul betaald verkeer op 10 t/m 15 september. Laatste wholesaler-inzending blijft 4 september. Op 15 september kwamen 2 organische bezoekers op de distributeurspagina.

Pipeboard werkte direct, geen weeklimiet. Alle Meta-cijfers zijn vandaag vers opgehaald.

**Overzicht per campagne (last 30d, 17 aug t/m 15 sep)**

| Campagne | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 |
| **Totaal** | **€1.069,38** | 2,2% | €0,37 | €8,22 | | 19 | 24 (+11 zonder UTM = 35) | €30,55 all-in |

ROAS is niet van toepassing, het zijn lead-campagnes. Kosten per inzending zijn op PostHog gebaseerd, omdat de Meta pixel structureel te weinig telt.

**Underperformers**

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar kortste sessies en 0,7% conversie, €63,63 per inzending. Nieuwe hook testen.
- **Video 2 (LIT)** en **Statisch 1 (LIT)** raken een CPC- of CTR-drempel maar zijn de beste converteerders (3,5% en 3,0%). Behouden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 2 (SWE) €32,03

**Funnel /become-a-distributor (30d):** 1.746 pageviews, 137 formulierstarts, 21 formulierfouten, 35 inzendingen. Van start naar inzending komt maar 24,8% door. Dat lek eerst fixen vóór er weer budget op gaat.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. De herstart-voorstellen van 3 september wachten nog op jouw goedkeuring.

**Wijzigingen t.o.v. gisteren:** geen. Zelfde status, zelfde cijfers, zelfde 35 inzendingen. Alleen 2 organische pageviews erbij.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.
