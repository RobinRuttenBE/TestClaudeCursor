Het rapport staat in `Output/Reports/Daily/2026-09-20_ads_report.md`. Alleen Pipeboard (directe JSON-RPC route, 1 testcall) en PostHog (directe REST-route, 6 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 20 september 2026

**Meta was vandaag niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie en de directe route zat op de eerste call op de weeklimiet (30 van 30, reset maandag 21 september 00:00 UTC, dus vannacht). De Meta-cijfers komen uit het live extract van 16 september. PostHog bevestigde dat het 30d-venster van vandaag (21 augustus t/m 19 september) dezelfde levering bevat: de eerste betaalde sessie viel op 27 augustus en de laatste nalopers op 9 september, nul betaald verkeer sinds. De cijfers zijn dus ongewijzigd geldig.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Zeventiende dag zonder levering.

**Overzicht per campagne (last 30d, extract 16 september, PostHog-venster 21 aug t/m 20 sep)**

| Campagne | Status | Spend | Impr. | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,14 | 90.888 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 | Freq. > 3,5 |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 | geen |
| **Totaal** | | **€1.069,38** | 130.155 | 2,2% | €0,37 | €8,22 | | 19 | 35 (24 via ad-UTM, 11 organisch) | €30,55 all-in | |

ROAS niet van toepassing, het zijn lead-campagnes. Kosten per inzending zijn op PostHog gebaseerd omdat de Meta pixel structureel te weinig telt. De all-in kosten per inzending zakten van €32,41 (gisteren) terug naar €30,55 omdat er vandaag een organische inzending bijkwam; de campagnes zelf deden niets.

**Nieuw signaal: tweede organische inzending in drie dagen.** Vandaag 09:13 UTC kwam een inzending binnen uit Malta (mobiel, Chrome op iOS). Directe landing op de Engelse homepage, 10 pageviews in bijna 24 minuten, formulier gestart om 09:09, ingezonden om 09:13, en de sessie eindigde op de wachtwoord-reset pagina (waarschijnlijk direct een klantaccount aangemaakt). Geen UTM, geen Meta. Na de Letse inzending van 18 september is dit de tweede nieuwe markt zonder advertentiebudget. Op 17 september startte ook een Britse bezoeker via Google het formulier zonder af te ronden, en op 19 en 20 september een Nederlandse desktopbezoeker twee keer (tweede keer om 02:31 UTC, 15 seconden, geen inzending).

**Underperformers (uit extract 16 september, gelden bij herstart in huidige vorm)**

- **Video 2 (SWE)**: CPC €0,69 (drempel €0,50) en CPM €17,07 (drempel €15,00). Aanbeveling: niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53 en CPM €15,27, nul inzendingen op 113 sessies. Aanbeveling: definitief uit.
- **Campagne LIT**: frequency 3,97 (drempel 3,5), publiek verzadigd. Aanbeveling: verse creatives vóór herstart.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar 0,7% sessie-naar-inzending en €63,63 per inzending. Aanbeveling: nieuwe hook testen.
- **Video 2 (LIT)** en **Statisch 1 (LIT)** raken een CPC- of CTR-drempel maar converteren het best (3,5% en 3,0%). Aanbeveling: behouden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 2 (SWE) €32,03
- Beste ROAS: niet van toepassing (lead-campagnes)

**Funnel /become-a-distributor (30d, 21 aug t/m 20 sep, PostHog live):** 1.699 pageviews (1.429 sessies), 141 formulierstarts (134 sessies), 22 formulierfouten, 35 inzendingen (32 sessies), 35 booking views. Van start naar inzending komt 24,8% door. Dat lek eerst dichten vóór herstart. Verkeer op de pagina sinds 14 september: 1 tot 8 sessies per dag, allemaal organisch.

**Samenvatting**

- Totaal spend: €1.069,38 (periode: last 30 days, ongewijzigd sinds 4 september)
- Beste performer: Video 2 (LIT), laagste kosten per inzending en hoogste conversie
- Slechtste performer: Video 1 (SWE), nul inzendingen bij CPC en CPM boven drempel
- Aanbeveling (70-20-10) bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Letland en nu ook Malta zijn kandidaten voor de targeting: twee organische inzendingen uit markten die niet in de campagnes zaten.

**Operationeel:** de Pipeboard-limiet reset vannacht om 00:00 UTC. Morgen kan het rapport weer live draaien; doe dan eerst de campaign-level 30d call en de ad-level call, en sla de per-ad tabel als markdown op zodat de rest van de week erop kan terugvallen. Voorstel 6 (één gedeeld Meta-extract per dag voor de drie rapporten) blijft de enige structurele oplossing. De zes voorstellen van 3 en 16 september wachten nog op goedkeuring.

**Google Sheet:** overgeslagen op verzoek. Niets geschreven naar "Meta Ads Tracker".

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.

---
Databronnen: Pipeboard directe JSON-RPC (1 call, weekly_limit_exceeded 30/30, reset_date 2026-09-21T00:00:00Z), Meta-extract van 16 september 2026 09:03, PostHog REST project 149694 (sessions met $entry_utm_source = 'facebook' per dag sinds 20 augustus; wholesaler_* events per dag sinds 21 augustus; 30d funneltotalen; sessiedetails van de inzendingen sinds 17 september; distributeurspagina-sessies per dag sinds 14 september).
