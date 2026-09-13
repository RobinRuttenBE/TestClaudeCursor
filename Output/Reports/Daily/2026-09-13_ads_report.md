Het rapport staat in `Output/Reports/Daily/2026-09-13_ads_report.md`, gecommit en gepusht (1d7ff4f6). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 13 september 2026

**Er draait niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. PostHog bevestigt dat live: na 4 september nog 3 nalopers in totaal, en nul betaald verkeer op 10, 11 en 12 september. Elfde dag zonder levering. Laatste inzending blijft 4 september.

**Beperking:** Pipeboard zat bij de eerste call al op de weeklimiet van het Free plan. De resetdatum in het antwoord is opgeschoven naar 21 september, niet 14 september. Meta-cijfers komen daarom uit het rapport van 7 september en zijn ongewijzigd omdat er sindsdien geen levering was. PostHog-cijfers zijn live van vandaag.

**Overzicht per campagne (last 30d)**

| Campagne | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 |
| **Totaal** | **€1.069,38** | 2,2% | €0,37 | €8,22 | | 19 | 24 (+11 zonder UTM) | €30,55 all-in |

ROAS niet van toepassing, het zijn lead-campagnes. Meta telt 19 leads tegenover 35 inzendingen in PostHog, dus kosten per inzending zijn op PostHog gebaseerd.

**Underperformers**

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, 0 inzendingen op 97 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: meeste sessies, kortste duur (56s), 0,8% conversie, circa €63,63 per inzending. Nieuwe hook testen.
- **Statisch 1 (LIT)**: link CTR 0,6%, maar 3,8% conversie. Behouden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38

**Funnel /become-a-distributor (30d):** 1.743 pageviews, 137 formulierstarts, 35 inzendingen. Sinds de pauze 1 tot 8 organische sessies per dag.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). De herstart-voorstellen van 3 september wachten nog op goedkeuring.

**Operationeel:** Pipeboard blijft tot 21 september dicht. Het voorstel om één gedeelde Meta-call per dag te cachen voor de drie rapporten wordt hiermee urgent, anders valt de route na de reset binnen 2 dagen opnieuw dicht.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.
