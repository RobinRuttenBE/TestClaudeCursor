# Morning Report — 2026-09-22

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Het rapport staat in `Output/Reports/Daily/2026-09-22_ads_report.md`, gecommit en gepusht (d0318806). Alleen Pipeboard (directe JSON-RPC route, 3 calls) en PostHog (directe REST-route, 2 sessions-queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 22 september 2026

**Meta was live bereikbaar.** Weekverbruik Pipeboard staat na deze run op 11 van 30 calls. Beide insights-calls hadden één retry nodig (eerste poging hing), daarna kwam alles binnen 20 seconden.

**PostHog events-queries hingen vandaag op beide routes.** Sessions-queries werkten wel. De funnelcijfers (formulierstarts, fouten, inzendingen) komen daarom uit het rapport van gisteren. Zonder levering veranderen die niet, behalve door organische inzendingen.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Negentiende dag zonder levering. PostHog bevestigt: nul betaalde sessies sinds 10 september.

**Overzicht per campagne (last 30d, 23 aug t/m 21 sep)**

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inz. | € / inz. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 19 | 35 all-in | €30,55 all-in |

Cijfers identiek aan 21 en 16 september. ROAS niet van toepassing, het zijn lead-campagnes. De volledige per-ad tabel met 17 kolommen staat in het bestand.

**Underperformers** (gelden bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste converteerder. Behouden.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20), maar 0,7% conversie. Nieuwe hook testen.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06

**Funnel /become-a-distributor:** organisch lopen er 1 tot 8 sessies per dag over de pagina (live, sinds 15 september), allemaal zonder betaald verkeer. Of daar op 21 september een nieuwe inzending bij zat kon ik niet bevestigen omdat de events-tabel niet antwoordde. Laatste bekende stand 30d: 141 formulierstarts, 22 fouten, 35 inzendingen.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Letland en Malta als targeting-kandidaten. Eerst het formulierlek dichten vóór er weer budget op gaat. De zes voorstellen van 3 en 16 september wachten nog op jouw goedkeuring.

**Google Sheet:** overgeslagen op verzoek.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.

---

Het rapport staat in `output/reports/daily/2026-09-21_sybb_report.md` (macOS behandelt `Output/Reports/Daily` als dezelfde map), gecommit en gepusht als 9a9b282b.

**Databronnen.** Beide Pipeboard MCP-servers vroegen om autorisatie en de PostHog MCP gaf HTTP 405, dus ik gebruikte de directe routes uit het geheugen: één JSON-RPC call naar Pipeboard en zeventien HogQL-queries op de PostHog REST API. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Meta Ads.** Campagne `2026: SYBB` staat 155 dagen op PAUSED. De insights-call over 15 t/m 21 september kwam leeg terug, dus nul spend en nul levering. PostHog bevestigt dit onafhankelijk: geen enkele sessie met Meta-UTM of SYBB-UTM.

**Landing page.** startyourballoonbusiness.com staat voor de vierentwintigste dag op nul bezoekers. Session replay staat voor de zestiende dag op nul opnames.

**Event funnel (de echte SYBB-funnel).** Negen externe sessies van acht personen op de registratiepagina's, 22 SYBB-pageviews, nul kliks op Registreer, nul betalingen. Voor de derde dag op rij geen enkele inschrijfpoging. Wel twee sterke twijfelaars:

- Een Belgische Android-bezoeker landde via Google op de Franse pagina, kwam drie uur later terug en klikte vijftien keer tussen professional-7, 8 en 9 zonder te kiezen.
- Een Belgische iPhone-bezoeker opende professional-9 nu voor de zesde keer sinds 29 augustus, altijd via de kalender, nooit een klik.

**Nieuwe bevindingen.** Professional-7 heeft in de kalender het uiterlijk van een gesloten event (grijze titel, lichte knop) maar staat bovenaan en kreeg 10 van de 22 SYBB-pageviews. Twee medewerkers ontsnapten aan het bestaande interne filter; ik herken ze nu via de Odoo-backend-referrer, waardoor het cohort op 12 ids staat. Google stuurt Belgen, een bezoeker uit Réunion en een Oostenrijkse klant naar de Franse en Duitse pagina's, die niet vermelden dat de workshop in Genk is.

**Top 3 acties in het rapport.** Een e-mail opt-in voor twijfelaars op de vier registratiepagina's, de status en volgorde van professional-7 in de kalender controleren, en een vergelijkingsblok met datum, taal, locatie, prijs en beschikbaarheid op elke SYBB-pagina.

De geheugennotities over PostHog en de SYBB-funnel zijn bijgewerkt met de nieuwe detectiemethode voor intern verkeer en de twee herhaalbezoekers.

---

Het rapport staat in `Output/Reports/Daily/2026-09-22_auto_optimize.md`, gecommit en gepusht (7234f4fd). Alleen Pipeboard (directe JSON-RPC route, 2 calls) en PostHog (directe REST-route, 3 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. De ad-level call over 19 t/m 21 september gaf nul rijen, dus de kill-regels hadden niets om op te draaien. Geen `update_ad` calls gedaan. Twintigste dag zonder levering.

**Meta was live bereikbaar.** Beide calls kwamen in de eerste poging binnen 3 seconden terug. Weekverbruik na deze run staat op 13 van 30. De per-ad tabel met Link CTR, CPC (link), Meta leads en PostHog inzendingen staat nu echt als markdown in het rapport. Het bestand van gisteren bevatte alleen de samenvatting, dus dit is de eerste bruikbare fallback-tabel voor als de limiet later deze week dichtgaat.

**PostHog bevestigt de stilstand live.** Nul betaalde sessies van 12 tot en met 22 september. De events-tabel antwoordde vanmiddag weer normaal. Op 21 september geen nieuwe inzending, wat vanochtend nog niet te bevestigen was. De organische inzendingen uit Letland (18 september) en Malta (20 september) blijven de enige sinds de pauze.

**Wat de link-metrics laten zien.** Alleen Statisch 2 (SWE) haalt beide Core-drempels (Link CTR 2,2%, CPC link €0,45), maar kreeg maar 12,0% van het budget. Statisch 1 (LIT) zit met 0,6% Link CTR onder de kill-drempel en zou bij herstart mechanisch gepauzeerd worden, terwijl het met €36,06 per inzending de derde beste converteerder is. Beide SWE-video's vallen af op CPM boven €15,00 en op conversie.

**Zeven voorstellen wachten op je goedkeuring**, dezelfde als gisteren, nu onderbouwd met de live 30d-cijfers:

1. Herstart LIT op €100,00 en SWE op €40,00 per dag, met concrete bedragen per ad en de twee SWE-video's op €0,00.
2. Hook-varianten op Statisch 2 (SWE), een Zweedse variant van Video 2 (LIT), nieuwe body voor Video 1 (SWE) en een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, Statisch 1 (LIT) verengen, SWE verbreden, Letland en Malta als testlanden.
4. Conversie-guard op de kill-regels.
5. Formulierfout en pixel-lead-event fixen vóór herstart.
6. Eén gedeeld Meta-extract per dag voor de drie rapporten.
7. Nieuwe 70-20-10 drempels op link-metrics, zodat de indeling overeenkomt met de conversie-ranking.

Geef aan welke nummers ik mag uitvoeren. Voorstel 2 wordt concreter als ik de huidige ad-copy mag ophalen; dat kost één extra Meta-call.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
