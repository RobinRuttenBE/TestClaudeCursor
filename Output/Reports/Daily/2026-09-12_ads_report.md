Het rapport staat in `Output/Reports/Daily/2026-09-12_ads_report.md` en is gecommit en gepusht (bce7f800). Alleen Pipeboard en PostHog gebruikt, beide via de directe HTTP-route omdat de MCP-servers niet verbonden. Geen Google-bronnen aangeroepen, geen Sheet geschreven.

## Meta Ads Rapport, 12 september 2026

**Er draait niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. PostHog bevestigt dat: 58 betaalde sessies op 4 september, daarna 0 tot 2 nalopers per dag. Laatste inzending blijft 4 september. Negende dag zonder levering.

**Beperking:** Pipeboard viel na drie calls op de weeklimiet van het Free plan. Campagne-cijfers zijn live van vandaag. Ad-level Meta-cijfers komen uit het rapport van 7 september over dezelfde periode en zijn ongewijzigd omdat er sindsdien geen levering was. Ad-level PostHog cijfers zijn wel live.

**Overzicht per campagne (last 30d)**

| Campagne | Spend | Impr. | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 90.888 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 39.267 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | **€1.069,38** | 130.155 | 2,2% | €0,37 | €8,22 | | 19 | 23 (+9 zonder UTM) | €46,49 |

ROAS niet van toepassing, het zijn lead-campagnes. Meta telt 277 landing page views tegenover 1.412 PostHog-sessies, dus kosten per inzending zijn op PostHog gebaseerd.

**Underperformers**

- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, 0 inzendingen op 113 sessies. Niet herstarten.
- **Video 2 (SWE)**: CPC €0,69, CPM €17,07, duurste ad van het account. Niet herstarten in deze vorm.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: laagste CPC (€0,20) maar 0,7% conversie en kortste sessies. Nieuwe hook testen.
- **Statisch 1 (LIT)**: link CTR 0,6%, maar 3,0% conversie. Behouden, lage CTR is hier geen kill-reden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38

**Funnel /become-a-distributor (30d):** 1.587 pageviews, 137 form starts, 35 inzendingen. Ruim 91% begint niet aan het formulier. Sinds de pauze 1 tot 8 sessies per dag, vrijwel allemaal organisch.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de LIT-winnaars (Video 1, Video 2, Statisch 1) plus Statisch 2 (SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). De vijf herstart-voorstellen van 3 september wachten nog op goedkeuring.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.
