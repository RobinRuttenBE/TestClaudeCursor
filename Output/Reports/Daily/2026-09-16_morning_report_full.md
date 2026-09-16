# Morning Report — 2026-09-16

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Het rapport staat in `Output/Reports/Daily/2026-09-16_ads_report.md`, gecommit en gepusht (31399fbf). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 16 september 2026

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september 11:50. Meta geeft voor 9 t/m 15 september nul rijen. PostHog bevestigt dat: na 4 september nog 5 nalopers, nul betaald verkeer op 10 t/m 15 september. Laatste wholesaler-inzending blijft 4 september. Op 15 september kwamen 2 organische bezoekers op de distributeurspagina.

Pipeboard werkte direct, geen weeklimiet. Alle Meta-cijfers zijn vandaag vers opgehaald.

**Overzicht per campagne (last 30d, 17 aug t/m 15 sep)**

| Campagne | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 |
| **Totaal** | **€1.069,38** | 2,2% | €0,37 | €8,22 | | 19 | 24 (+11 zonder UTM = 35) | €30,55 all-in |

ROAS is niet van toepassing, het zijn lead-campagnes. Kosten per inzending zijn op PostHog gebaseerd, omdat de Meta pixel structureel te weinig telt.

**Underperformers**

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar kortste sessies en 0,7% conversie, €63,63 per inzending. Nieuwe hook testen.
- **Video 2 (LIT)** en **Statisch 1 (LIT)** raken een CPC- of CTR-drempel maar zijn de beste converteerders (3,5% en 3,0%). Behouden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 2 (SWE) €32,03

**Funnel /become-a-distributor (30d):** 1.746 pageviews, 137 formulierstarts, 21 formulierfouten, 35 inzendingen. Van start naar inzending komt maar 24,8% door. Dat lek eerst fixen vóór er weer budget op gaat.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. De herstart-voorstellen van 3 september wachten nog op jouw goedkeuring.

**Wijzigingen t.o.v. gisteren:** geen. Zelfde status, zelfde cijfers, zelfde 35 inzendingen. Alleen 2 organische pageviews erbij.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.

---

Het rapport staat in `Output/Reports/Daily/2026-09-15_sybb_report.md`, gecommit en gepusht (4b9481eb). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## SYBB Daily Report, 15 september 2026

**Stilste dag van de week, en de derde dag op rij zonder één klik op Register.** Van de 4 SYBB-sessies was er 1 echt: een terugkerende Nederlandse desktopbezoeker die via de workshopkalender de Falcone-tour, Content Day Winter Wonderland en SYBB professional-9 vergeleek. SYBB kreeg 17 seconden, de Falcone-tour bijna 3 minuten. De andere 3 sessies waren link-previews op professional-48 in het Engels, Duits en Frans binnen 3 uur, elk precies 1 event in de hele projecthistorie. Iemand heeft die link gisteravond gedeeld.

**Meta:** de 30d-call kwam live binnen en bevat geen enkele SYBB-rij, dus nul spend en nul levering. De tweede call liep op de Pipeboard-weeklimiet (30 van 30, resetdatum 21 september). Campagnestatus komt uit het ads-rapport van vanochtend: alle 7 campagnes PAUSED, SYBB al 149 dagen. PostHog bevestigt site-breed nul Meta-verkeer.

**7d-baseline nu schoon.** Interne sessies (10 distinct_ids met vertaal-editor of Odoo-login in 30 dagen) zijn eruit gefilterd. 8 t/m 14 september: 33 echte externe sessies, 4 klikken op Register (12%), 3 tickets bevestigd, 1 betaling op 9 september.

**Rode vlaggen:** derde dag zonder inschrijfpoging, SYBB-verkeer zakt naar 1 echte bezoeker per dag, previews vervuilen de bounce rate, session replay tiende dag op nul, landing page achttiende dag op nul, en Pipeboard al op woensdag dicht. Site-breed liep gisteren een nieuwe crawlergolf (3.335 sessies, 80% bot-achtig), maar de SYBB-pagina's bleven daar buiten.

**Top 3 acties:**
1. Zelf de inschrijving doorlopen op iPhone, uitgelogd, en meteen de replay-instellingen controleren. Zesde dag open.
2. SYBB een eigen blok bovenaan de workshopkalender geven, met voor wie, wat je meeneemt, data en één knop per datum. Vergelijkers geven SYBB nu de minste tijd van alle kaarten.
3. Uitzoeken waar de link naar professional-48 gisteravond is gedeeld, en tegelijk het interne cohort in de PostHog projectinstellingen uitfilteren.

Twee memory-notities bijgewerkt: de Pipeboard-limiet gaat nu al op woensdag dicht, dus bij een stilstaand account volstaat één 30d-call per SYBB-run; en de aanpak voor een schone 7d-baseline plus het preview-profiel op eventpagina's staan in de PostHog-notitie.

---

Rapport staat in `Output/Reports/Daily/2026-09-16_auto_optimize.md`, gecommit en gepusht (c9f23b93). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september 11:50. Meta gaf vanochtend nul rijen voor 9 t/m 15 september. De kill-regels hadden niets om op te draaien, geen `update_ad` calls gedaan. 0 van 0 actieve ads gepauzeerd.

**Meta was deze run niet vers bereikbaar.** De Pipeboard MCP vraagt autorisatie, en de directe route zat op de eerste call al op de weeklimiet (30 van 30, reset 21 september). Het ads-rapport van 09:03 had de Meta-data nog live, dus de campagnestatus komt daaruit. De SYBB-run daarna verbruikte de laatste calls.

**PostHog bevestigt de stilstand live.** Nul sessies met een Meta-UTM sinds 10 september, nul formulierstarts, nul inzendingen. Alleen 14 organische pageviews op de distributeurspagina in zeven dagen. Laatste betaalde inzending blijft 4 september, dertiende dag zonder levering.

**De zes voorstellen staan ongewijzigd en wachten op je goedkeuring:**

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE), twee op Video 2 (LIT), een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE audience verbreden, Statisch 1 (LIT) naar 25-65 zonder desktop.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking en funnel fix vóór herstart: Meta telt 19 leads tegenover 35 in PostHog, en 102 van 137 formulierstarters haken af.
6. Eén gedeeld Meta-extract per dag cachen voor de drie rapporten. Vandaag was de limiet op woensdag al vol, dus dit wordt urgent als er weer ads draaien.

Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
