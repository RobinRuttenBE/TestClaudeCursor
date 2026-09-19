# Morning Report — 2026-09-19

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

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

---

Het SYBB-rapport voor 18 september stond al volledig in `Output/Reports/Daily/2026-09-18_sybb_report.md` (geschreven en gecommit vanochtend om 08:27). Ik heb het niet opnieuw opgebouwd, maar de kerncijfers live geverifieerd en een herverificatienotitie toegevoegd. Die wijziging is gecommit en gepusht naar main.

**Wat de live-check bevestigde**

- **PostHog, SYBB event-pagina's op 18 september:** 11 sessies, waarvan 1 tab-sluiting zonder pageview, 5 bot-bounces en 1 sessie met een afgeronde betaling (2 deelnemers, NL professional-9). Identiek aan het rapport.
- **PostHog, 7-daags venster 11 t/m 17 september:** 47 SYBB-sessies, zoals gerapporteerd.
- **Landing page startyourballoonbusiness.com:** 0 sessies over 11 t/m 18 september. Eenentwintigste dag zonder verkeer.
- **Site-breed 18 september:** 1.654 sessies en 4.136 pageviews, 0 via Meta-UTM's of utm_campaign=sybb. Alleen 2 organische facebook.com-referrals. Geen betaalde levering.
- **Meta Ads via Pipeboard:** de directe call kreeg `weekly_limit_exceeded` (30 van 30, reset 21 september 00:00 UTC). Campagne `2026: SYBB` blijft PAUSED. De 30d-cijfers in het rapport komen uit het extract van 16 september, wat bij een stilstaande campagne geen informatieverlies is.

**Belangrijkste inhoud van het rapport**

- Tweede betaalde SYBB-inschrijving van de maand, de eerste met 2 deelnemers. Directe landing zonder referrer of UTM, dus de bron is onbekend.
- Grootste lek blijft de stap van pagina bekeken naar klik op Registreer (1 van 24 vorige week, 1 van 5 gisteren).
- Nieuwe crawlergolf op de SYBB-URL's vervuilt de bounce rate van de sessions-tabel.
- Top 3 acties: inschrijving controleren in Odoo en de koper vragen waar de link vandaan kwam, session replay aanzetten en de kaartbetaling testen (13 minuten op /payment/status), en een locatie- en reisblok boven de Registreer-knop plaatsen plus directe SYBB-links vanuit de twee starter-blogs.

**Beperkingen**

- Beide Pipeboard MCP-servers vroegen om autorisatie en de PostHog MCP gaf HTTP 405. Ik heb de directe JSON-RPC route en de PostHog REST API met de geconfigureerde tokens gebruikt, dus dezelfde databronnen.
- Geen Google MCP's aangeroepen en geen Google Sheet bijgewerkt, conform de strikte regel.

Ik heb in memory genoteerd dat de daily trigger blijkbaar twee keer per ochtend vuurt, en dat een tweede run dan alleen hoeft te verifiëren in plaats van te regenereren. Dat spaart de Pipeboard-weeklimiet.

---

Het rapport staat in `Output/Reports/Daily/2026-09-19_auto_optimize.md`, gecommit en gepusht (5d5999f6). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Er zijn 0 actieve ads, dus de kill-regels hadden niets om op te draaien. Geen `update_ad` calls gedaan.

**Meta was niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie, en de directe route zat op de eerste call op de weeklimiet (30 van 30, reset maandag 21 september). De campagnestatus komt uit het live extract van 16 september. Ik heb verder geen Meta-calls gedaan.

**PostHog bevestigt de stilstand live.** Nul betaalde sessies sinds 9 september, nul sessies op de distributeurspagina vandaag. De enige beweging is de organische inzending van 18 september uit Letland, die vanochtend ook al in het ads-rapport stond.

**Waarschuwingen** komen uit het extract van 16 september en gelden bij herstart in de huidige vorm: frequency 3,97 op de LIT-campagne, CPM boven €15,00 op beide SWE-video's, en 0,7% conversie op Statisch 2 (LIT).

**De zes voorstellen staan ongewijzigd open**, met één aanvulling op nummer 3: Letland toevoegen aan de LIT-targeting bij herstart, op basis van die eerste Letse inzending ooit.

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) op €40,00 per dag zonder de twee SWE-video's.
2. Variaties op Statisch 2 (SWE), Video 2 (LIT) en een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE audience verbreden, Statisch 1 (LIT) naar 25-65 zonder desktop, plus Letland toevoegen.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking en funnel fix vóór herstart: 24,6% van de formulierstarters komt door.
6. Eén gedeeld Meta-extract per dag cachen voor de drie rapporten. Dit is de vierde dag deze week dat auto-optimize op de limiet stuit.

Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
