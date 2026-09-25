# Morning Report — 2026-09-25

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Het rapport staat in `Output/Reports/Daily/2026-09-25_ads_report.md`, gecommit en gepusht (3278104f). Alleen Pipeboard (directe JSON-RPC route, 3 calls) en PostHog (directe REST-route, 8 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 25 september 2026

**Beide bronnen live bereikbaar.** De Pipeboard MCP meldt "requires authentication", maar de directe route werkte direct en zonder limietmelding. De PostHog events-tabel antwoordde normaal, dus de funnelcijfers zijn live.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Dit is de 21e dag zonder levering. PostHog bevestigt: nul betaalde sessies sinds 11 september.

**Overzicht per campagne (last 30d, 26 aug t/m 24 sep)**

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inz. | € / inz. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 19 | 23 (+9 organisch) | €46,49 |

Cijfers identiek aan 16, 21, 22 en 24 september. ROAS niet van toepassing, het zijn lead-campagnes. De volledige per-ad tabel (16 kolommen, met PostHog bounce, sessieduur en conversie per ad) staat in het bestand.

**Let op vanaf 27 september:** dan valt 27 augustus uit het 30d-venster en dalen de LIT-cijfers zonder dat er iets veranderde.

**Underperformers** (gelden bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste converteerder (3,5%). Behouden.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20), maar 0,7% conversie en kortste sessieduur (51s). Nieuwe hook testen.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06

**Funnel /become-a-distributor (live):** 30d staat op 141 formulierstarts, 22 fouten (15,6%), 35 inzendingen in 32 sessies. Organisch 2 tot 6 sessies per dag over de pagina. Geen nieuwe inzending sinds Malta op 20 september.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Eerst het formulierlek en het pixel-lead-event fixen (Meta telt 19 van de 32 inzendingen) vóór er weer budget op gaat. De zes voorstellen van 3 en 16 september wachten nog op jouw goedkeuring.

**Google Sheet:** overgeslagen op verzoek.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.

---

SYBB rapport niet beschikbaar.

---

Het rapport staat in `Output/Reports/Daily/2026-09-25_auto_optimize.md`, gecommit en gepusht (1e59cf9d). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. PostHog bevestigt live nul betaalde sessies van 18 t/m 25 september. Er zijn geen `update_ad` calls gedaan. Tweeëntwintigste dag zonder levering.

**Meta-weeklimiet zit vol.** De enige call kreeg `weekly_limit_exceeded` (30 van 30, reset maandag 28 september). Het ads-rapport van 08:17 vanochtend kon nog 3 calls doen, dus tussen woensdag en vrijdag ging het verbruik van circa 6 naar 30. De run draait daarom op de campagnestatus uit dat ads-rapport plus de per-ad link-tabel uit het live extract van 24 september. Dat is veilig: zonder levering veranderen de per-ad cijfers niet, en PostHog bevestigt dat.

**Archiefprobleem blijft.** Het bestand van 24 september bevat op schijf opnieuw alleen de chatsamenvatting. De volledige tabel stond wel in de commit, en daar heb ik hem vandaan gehaald. Het bestand van vandaag is met grep gecontroleerd en bevat de tabel.

**Funnel /become-a-distributor:** vijfde dag op rij zonder formulierstart. Geen inzending sinds Malta op 20 september. Organisch 3 tot 6 sessies per dag op de pagina.

**Zeven voorstellen wachten op je goedkeuring**, ongewijzigd sinds 22 september:

1. Herstart LIT op €100,00 en SWE op €40,00 per dag, met bedragen per ad en beide SWE-video's op €0,00.
2. Hook-varianten op Statisch 2 (SWE), Zweedse variant van Video 2 (LIT), nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE verbreden, Letland en Malta als testlanden.
4. Conversie-guard op de kill-regels.
5. Formulierfout (15,6%) en pixel-lead-event fixen vóór herstart.
6. Eén gedeeld Meta-extract per dag voor de drie rapporten. Dit is nu urgent: de limiet zat vrijdag al vol.
7. Nieuwe 70-20-10 drempels op link-metrics.

Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
