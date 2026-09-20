Het rapport staat in `Output/Reports/Daily/2026-09-20_ads_report.md`, gecommit en gepusht (ec34a249). Alleen Pipeboard (directe JSON-RPC route, 1 testcall) en PostHog (directe REST-route, 6 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 20 september 2026

**Meta was vandaag niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie en de directe route zat op de eerste call op de weeklimiet (30 van 30, reset vannacht 21 september 00:00 UTC). De Meta-cijfers komen uit het live extract van 16 september. PostHog bevestigde dat het 30d-venster van vandaag dezelfde levering bevat: eerste betaalde sessie 27 augustus, laatste nalopers 9 september, nul sinds. De cijfers zijn dus ongewijzigd geldig.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Zeventiende dag zonder levering.

**Overzicht per campagne (last 30d)**

| Campagne | Spend | Impr. | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 90.888 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 39.267 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 |
| **Totaal** | **€1.069,38** | 130.155 | 2,2% | €0,37 | €8,22 | | 19 | 35 (24 via ad, 11 organisch) | €30,55 all-in |

ROAS niet van toepassing, het zijn lead-campagnes. De all-in kosten per inzending zakten van €32,41 naar €30,55 puur door een organische inzending vandaag, niet door de campagnes.

**Nieuw signaal: tweede organische inzending in drie dagen.** Vanochtend 09:13 UTC kwam een inzending binnen uit Malta. Directe landing op de Engelse homepage, 10 pageviews in 24 minuten, en de sessie eindigde op de wachtwoord-reset pagina, dus vermoedelijk direct een klantaccount aangemaakt. Geen UTM, geen Meta. Na Letland op 18 september is dit de tweede nieuwe markt zonder advertentiebudget.

**Underperformers** (extract 16 september, gelden bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar 0,7% conversie en €63,63 per inzending. Nieuwe hook testen.
- **Video 2 (LIT)** en **Statisch 1 (LIT)** raken een drempel maar converteren het best (3,5% en 3,0%). Behouden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 2 (SWE) €32,03

**Funnel /become-a-distributor (30d, live):** 1.699 pageviews, 141 formulierstarts, 22 fouten, 35 inzendingen. Van start naar inzending komt 24,8% door. Dat lek eerst dichten vóór herstart.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Letland en Malta zijn nu allebei targeting-kandidaten. De zes voorstellen van 3 en 16 september wachten nog op jouw goedkeuring.

**Operationeel:** de limiet reset vannacht. Morgen draait het rapport weer live, met campaign-level plus ad-level in één run en de per-ad tabel opgeslagen als markdown. Voorstel 6 (één gedeeld Meta-extract per dag) blijft de structurele oplossing.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.
