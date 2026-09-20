# Morning Report — 2026-09-20

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

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

---

Het rapport staat in `Output/Reports/Daily/2026-09-19_sybb_report.md`, gecommit en gepusht (667efa4d). Alleen Pipeboard (directe JSON-RPC route, 1 testcall) en PostHog (directe REST-route, 12 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## SYBB Daily Report, 19 september 2026

**Meta was niet live bereikbaar.** Beide Pipeboard MCP-servers vragen autorisatie en de PostHog MCP gaf HTTP 405. De directe Pipeboard-call kreeg op de eerste poging de weeklimiet (30 van 30, reset 21 september 00:00 UTC). Campagnestatus en cijfers komen uit het extract van 16 september. PostHog bevestigde live dat er geen betaald verkeer was: nul sessies via meta, facebook of instagram, ook geen organische social referrals.

**Stille dag zonder inschrijfpoging.** De campagne staat 153 dagen op PAUSED, de landing page staat voor de 22e dag op nul bezoekers, session replay voor de 14e dag op nul opnames.

| Metric | Gisteren | 7d gemiddelde |
|---|---|---|
| Echte externe SYBB-sessies | 3 | 4,0 |
| Bot of link-preview | 2 | 2,9 |
| Klik op Registreer | 0 | 2 in 7 dagen |
| Betaald ticket | 0 | 1 (18 sep, 2 deelnemers) |
| Bounce rate echte bezoekers | 0% | 0% |

**Warmste signaal van de dag:** een nieuwe Nederlandse desktopbezoeker kwam via Google op de kalender, opende drie SYBB-data en bleef vijf minuten op professional-9. Vierenhalf uur later kwam dezelfde persoon terug, zette de site op Nederlands en klikte op de kalender op "Genk" om opnieuw naar professional-9 te gaan. Geen klik op Registreer, en geen enkel vangnet: geen retargeting, geen e-mail, geen replay. Locatie was daarmee twee dagen op rij het enige klikdoel van SYBB-bezoekers.

**Nieuw:** de URL /en_GB/start-your-balloon-business-3 dook voor het eerst op, via een link-preview uit Japan. Dat is een Odoo websitepagina, geen event. Onduidelijk of die gepubliceerd hoort te zijn.

**Top 3 acties**

1. Blok "Locatie en reizen" boven de Registreer-knop op de vier taalversies. Twee dagen op rij is het adres het enige waarop geklikt wordt.
2. E-mail opt-in voor twijfelaars onder de Registreer-knop, met een korte follow-up van drie mails. Zonder ads is dit de enige manier om de warme pool van circa 120 personen vast te houden.
3. Check wat pagina start-your-balloon-business-3 is en zet session replay aan in de PostHog projectinstellingen.

Uit eerdere rapporten staat nog open: de inschrijving van 18 september in Odoo controleren en de koper vragen waar de link vandaan kwam, en de betaalstap testen op de wachttijd van 13 minuten.

**Operationeel:** maandag 21 september reset de Pipeboard-limiet. Dan eerst live testen en campaign-level plus ad-level in één run ophalen.

---

Het rapport staat in `Output/Reports/Daily/2026-09-20_auto_optimize.md`, gecommit en gepusht (c16889ff). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Er zijn 0 actieve ads, dus de kill-regels hadden niets om op te draaien. Geen `update_ad` calls gedaan.

**Meta was niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie, en de directe route zat op de eerste call op de weeklimiet (30 van 30). De reset is vannacht, 21 september 00:00 UTC. Campagnestatus en per-ad cijfers komen uit het extract van 16 september.

**PostHog bevestigt de stilstand live.** Nul betaalde sessies sinds 9 september. De enige beweging is organisch: na Letland op 18 september kwam vanochtend een inzending uit Malta binnen, vermoedelijk direct met aangemaakt klantaccount.

**Waarschuwingen** zijn ongewijzigd en gelden bij herstart: frequency 3,97 op LIT, CPM boven €15,00 op beide SWE-video's, en 0,7% conversie op Statisch 2 (LIT).

**De zes voorstellen staan open**, met één nieuwe aanvulling op nummer 3: Malta als testland in de Experimental-laag, naast Letland.

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) op €40,00 per dag zonder de twee SWE-video's.
2. Variaties op Statisch 2 (SWE), Video 2 (LIT) en een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE audience verbreden, Statisch 1 (LIT) naar 25-65 zonder desktop, plus Letland en Malta toevoegen.
4. Conversie-guard op de kill-regels zodat de beste converteerders niet op dag 1 na herstart sneuvelen.
5. Funnel fix vóór herstart: 24,8% van de formulierstarters komt door.
6. Eén gedeeld Meta-extract per dag cachen. Auto-optimize stuitte deze week vijf keer op de limiet.

Morgen draait auto-optimize weer live en slaat de per-ad Link CTR en CPC (link) tabel op als markdown. Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
