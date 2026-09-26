# Morning Report — 2026-09-26

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Het rapport staat in `Output/Reports/Daily/2026-09-26_ads_report.md`, gecommit en gepusht (dd2c2f51). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 5 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 26 september 2026

**Pipeboard zit dicht tot maandag.** De eerste call kreeg `weekly_limit_exceeded` (30 van 30 wekelijkse executions op het gratis plan, reset 28 september 00:00 UTC). Geen tweede call gedaan. De Meta-cijfers komen uit het laatste live extract van 24 september. Dat is veilig: alle campagnes staan sinds 4 september op PAUSED en PostHog bevestigt live nul betaalde sessies sinds 9 september. Morgen valt 27 augustus uit het 30d-venster, dan dalen de LIT-cijfers zonder dat er iets veranderde.

**Er draait nog steeds niets.** Alle 7 campagnes PAUSED. Laatste betaalde sessies: 2 op 9 september.

**Overzicht per campagne (last 30d, 27 aug t/m 25 sep)**

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inz. | € / inz. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 19 | 23 (+12 organisch) | €46,49 |

ROAS niet van toepassing, lead-campagnes. De volledige per-ad tabel (8 ads, 11 kolommen) staat in het bestand en is met grep gecontroleerd.

**Underperformers** (bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste converteerder (3,5%). Behouden.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20), maar 0,7% conversie. Nieuwe hook testen.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06

**Funnel /become-a-distributor (live):** 30d staat op 142 formulierstarts, 22 fouten (15,5%), 35 inzendingen in 32 sessies. Laatste 7 dagen: 21 pageviews, 4 starts, 1 inzending. Geen nieuwe inzending sinds Malta op 20 september. Organisch 2 tot 6 sessies per dag op de pagina, geen enkele betaald.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Eerst het formulierlek en het pixel-lead-event fixen (Meta telt 19 van de 32 inzendingen). Voorstel 6 van 22 september (één gedeeld Meta-extract per dag voor de drie rapporten) is nu urgent: de 30 calls zijn op vrijdag al op. De zeven voorstellen wachten nog op jouw goedkeuring.

**Google Sheet:** overgeslagen op verzoek.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.

---

SYBB rapport niet beschikbaar.

---

Het rapport staat in `Output/Reports/Daily/2026-09-26_auto_optimize.md`, gecommit en gepusht (e430fc9a). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. PostHog bevestigt live nul betaalde sessies in het kill-venster van 23 t/m 25 september en ook vandaag tot 12:30. Er zijn geen `update_ad` calls gedaan. Drieëntwintigste dag zonder levering.

**Meta-weeklimiet zit nog vol.** De enige call kreeg `weekly_limit_exceeded` (30 van 30, reset maandag 28 september 00:00 UTC). De run draait daarom op de campagnestatus uit het ads-rapport van gisteren plus de per-ad link-tabel uit het live extract van 24 september. Dat is veilig zolang er geen levering is.

**Twee dingen om te weten:**

- **Archiefprobleem blijft.** De bestanden van 25 september bevatten op schijf alleen de chatsamenvatting. De volledige tabel stond wel in de commit, en daar heb ik hem vandaan gehaald. Het bestand van vandaag is met grep gecontroleerd en bevat de tabel.
- **30d-venster verschuift morgen.** Vanaf 27 september valt de eerste leveringsdag (27 augustus) uit het venster, dus de LIT-cijfers gaan dalen zonder dat er iets gebeurde. Maandag trek ik een extract met vast datumbereik 27 augustus t/m 4 september.

**Funnel /become-a-distributor:** geen inzending sinds Malta op 20 september. Eén formulierstart op 25 september zonder inzending. Organisch 2 tot 6 sessies per dag op de pagina.

**Zeven voorstellen wachten op je goedkeuring**, ongewijzigd sinds 22 september:

1. Herstart LIT op €100,00 en SWE op €40,00 per dag, met bedragen per ad en beide SWE-video's op €0,00.
2. Hook-varianten op Statisch 2 (SWE), Zweedse variant van Video 2 (LIT), nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE verbreden, Letland en Malta als testlanden.
4. Conversie-guard op de kill-regels.
5. Formulierfout (15,5%) en pixel-lead-event fixen vóór herstart.
6. Eén gedeeld Meta-extract per dag voor de drie rapporten. Dit blijft urgent: de limiet zat vrijdag al vol en houdt zaterdag en zondag alle Meta-data tegen.
7. Nieuwe 70-20-10 drempels op link-metrics.

Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
