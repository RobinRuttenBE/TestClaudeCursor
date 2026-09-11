Het rapport staat in `Output/Reports/Daily/2026-09-11_ads_report.md` en is gecommit en gepusht. Alleen Pipeboard en PostHog zijn gebruikt, beide via de directe HTTP-route omdat de MCP-servers niet verbonden. Geen Google-bronnen aangeroepen, geen Sheet geschreven.

## Meta Ads Rapport, 11 september 2026

**Er draait op dit moment niets.** Alle 7 campagnes staan op PAUSED. De twee Wholesaler Campagnes (SWE en LIT) zijn op 4 september gepauzeerd. PostHog bevestigt dat: 58 betaalde sessies op 4 september, daarna 0 tot 2 per dag. Dit rapport is een terugblik op de laatste 30 dagen, geen live stand.

**Overzicht per campagne (last 30d)**

| Campagne | Spend | Impr. | Freq. | CTR | CPC | CPM | Meta leads | PostHog inzendingen | Kosten / inzending |
|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 90.888 | 3,97 | 1,8% | €0,35 | €6,18 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 39.267 | 3,29 | 3,2% | €0,41 | €12,92 | 8 | 7 | €72,46 |
| **Totaal** | **€1.069,38** | 130.155 | | 2,2% | €0,37 | €8,22 | 19 | 23 | €46,49 |

ROAS is niet van toepassing, het zijn lead-campagnes. Meta telt 277 landing page views, PostHog 1.412 sessies. De pixel ondertelt structureel, dus kosten per inzending zijn op PostHog gebaseerd.

**Underperformers**

- **Video 1 (SWE)**: CPC €0,53, CPM €15,27 en 0 inzendingen op 113 sessies. Uitschakelen.
- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, duurste klik van alle acht. Niet herstarten in deze vorm.
- **Video 2 (LIT)**: CPC €0,58 boven de drempel, maar goedkoopste inzending (€28,75) en hoogste conversie (3,5%). Behouden.
- **Campagne LIT**: frequency 3,97. Klein Litouws publiek was na twee weken verzadigd, verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: laagste CPC (€0,20) maar 0,7% conversie en kortste sessies. Klikt goedkoop, converteert niet.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Goedkoopste inzending: Video 2 (LIT), €28,75

**Aanbeveling (70-20-10)** bij herstart: 70% naar de LIT-winnaars (Video 1, Video 2, Statisch 1) plus Statisch 2 (SWE), met nieuwe creatives. 20% naar een Zweedse variant op Video 2 (LIT), want SWE heeft geen werkende video. 10% naar een nieuwe hook voor Statisch 2 (LIT).

**Funnel** op /become-a-distributor (30d, alle verkeer): 1.739 pageviews, 138 form starts, 35 inzendingen. Het grote lek zit vóór het formulier: 92% haakt af voordat ze beginnen.

**Let op:** account act_607231713057715 uit de command bestaat niet in Pipeboard. Als je later Wix of GA4 landing page data aanlevert, kan ik daar een volledige funnel-diagnose op draaien.
