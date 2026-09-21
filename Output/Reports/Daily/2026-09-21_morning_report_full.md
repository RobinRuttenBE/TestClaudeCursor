# Morning Report — 2026-09-21

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Het rapport staat in `Output/Reports/Daily/2026-09-21_ads_report.md`, gecommit en gepusht (5c5047b5). Alleen Pipeboard (directe JSON-RPC route, 3 calls) en PostHog (directe REST-route, 4 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 21 september 2026

**Meta was vandaag weer live bereikbaar.** De Pipeboard-weeklimiet is vannacht gereset. Alle Meta-cijfers zijn vers opgehaald en identiek aan het extract van 16 september. De per-ad tabel staat nu als markdown in het rapportbestand, zodat latere runs erop kunnen terugvallen als de limiet weer dichtgaat.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Achttiende dag zonder levering. PostHog bevestigt: laatste betaalde sessies op 9 september, nul sinds.

**Overzicht per campagne (last 30d, 22 aug t/m 20 sep)**

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Meta leads | PostHog inz. | € / inz. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,14 | 90.888 | 1.617 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | Paused | €507,24 | 39.267 | 1.237 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | | **€1.069,38** | 130.155 | 2.854 | 2,2% | €0,37 | €8,22 | | 19 | 35 (23 via ad, 9 zonder UTM) | €30,55 all-in |

ROAS niet van toepassing, het zijn lead-campagnes. SWE staat op 7 inzendingen via ad in plaats van 8: de sessie-join telt unieke sessies, eerdere rapporten telden submit-events. Het all-in totaal van 35 is ongewijzigd.

**Per ad** (volledige tabel met 15 kolommen in het bestand)

| Ad | Spend | CTR | CPC | CPM | Sessies | Inz. | Conv. | € / inz. | Flag |
|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | €146,91 | 2,4% | €0,32 | €7,72 | 248 | 5 | 2,0% | €29,38 | |
| Video 2 (LIT) | €143,74 | 1,4% | €0,58 | €8,32 | 141 | 5 | 3,5% | €28,75 | CPC |
| Statisch 1 (LIT) | €144,24 | 1,0% | €0,49 | €5,07 | 134 | 4 | 3,0% | €36,06 | |
| Statisch 2 (LIT) | €127,25 | 2,4% | €0,20 | €4,87 | 292 | 2 | 0,7% | €63,63 | |
| Video 1 (SWE) | €126,75 | 2,9% | €0,53 | €15,27 | 113 | 0 | 0,0% | n.v.t. | CPC, CPM |
| Video 2 (SWE) | €127,00 | 2,5% | €0,69 | €17,07 | 97 | 2 | 2,1% | €63,50 | CPC, CPM |
| Statisch 1 (SWE) | €125,36 | 2,7% | €0,45 | €12,22 | 131 | 2 | 1,5% | €62,68 | |
| Statisch 2 (SWE) | €128,13 | 4,0% | €0,24 | €9,66 | 256 | 3 | 1,2% | €42,71 | |

**Underperformers** (gelden bij herstart in huidige vorm)

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig.
- **Video 2 (LIT)**: CPC boven drempel, maar beste converteerder. Behouden, niet mechanisch pauzeren.
- **Statisch 2 (LIT)**: goedkoopste clicks, maar 0,7% conversie. Nieuwe hook testen.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 1 (LIT) €36,06

**Funnel /become-a-distributor (30d, live):** 1.699 pageviews, 141 formulierstarts, 22 fouten, 35 inzendingen. Van start naar inzending komt 24,8% door. Sinds de pauze twee organische inzendingen (Letland 18 september, Malta 20 september) en op 20 september nog een formulierfout. Het formulier hapert dus ook zonder betaald verkeer.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. Letland en Malta als targeting-kandidaten. Eerst het formulierlek dichten vóór er weer budget op gaat. De zes voorstellen van 3 en 16 september wachten nog op jouw goedkeuring.

**Google Sheet:** overgeslagen op verzoek.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.

---

Het SYBB rapport voor 20 september stond al volledig in `Output/Reports/Daily/2026-09-20_sybb_report.md`, aangemaakt en gecommit eerder vandaag om 13:15. Ik heb het niet opnieuw opgebouwd maar de kerncijfers herverifieerd, een notitie toegevoegd en gecommit en gepusht (commit ebc88ae9).

**Databronnen:** beide MCP-servers waren ook nu niet bruikbaar. Pipeboard vroeg om autorisatie en de PostHog MCP gaf HTTP 405. Ik heb daarom de directe routes gebruikt die in het geheugen staan: de Pipeboard JSON-RPC endpoint met de geconfigureerde token en de PostHog REST API op project STX EU. Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.

**Herverificatie, alles identiek aan het rapport:**

| Cijfer | Waarde |
|---|---|
| Meta `2026: SYBB`, 20 sep, campaign-level insights | leeg, geen levering (campagne PAUSED sinds 19 april) |
| SYBB sessies op sempertexeurope.com, 20 sep | 10, waarvan 2 tab-sluitingen, 8 externe personen |
| Landing page startyourballoonbusiness.com, 13 t/m 20 sep | 0 sessies |
| Site-breed 20 sep | 1.457 sessies, 3.903 pageviews, 0 Meta-UTM, 0 social referrals, 12 via ChatGPT |

**Kern van het rapport:** drukste SYBB-dag van de week met hoogwaardige bezoekers, maar nul inschrijfpogingen. De Malta wholesaler-lead bekeek na de inzending ook professional-9, de koper van 18 september kwam drie keer terug en navigeerde handmatig naar zijn geboekte datum, en twee starters kwamen via de kostprijscalculator en de starter-blog. De drie acties voor vandaag: Malta-lead opvolgen met SYBB in het aanbod, de bevestigingsmail en praktische info op de eventpagina controleren, en een SYBB-blok in de tools en de blog plaatsen.

Wil je de MCP-connecties zelf herstellen, dan moet Pipeboard geautoriseerd worden via de claude.ai connector-instellingen en de PostHog MCP via `/mcp` in een interactieve sessie. De rapporten draaien intussen door via de directe routes.

---

Het rapport staat in `Output/Reports/Daily/2026-09-21_auto_optimize.md`, gecommit en gepusht (3938a57c). Alleen Pipeboard (directe JSON-RPC route, 2 calls) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. De ad-level call over de laatste 3 dagen gaf nul rijen, dus de kill-regels hadden niets om op te draaien. Geen `update_ad` calls gedaan. Achttiende dag zonder levering.

**Meta was live bereikbaar.** De weeklimiet is vannacht gereset. Ik heb de kans gebruikt om de per-ad Link CTR en CPC (link) over 30 dagen vers op te halen en als markdown-tabel op te slaan, zoals gisteren afgesproken. Verbruik vandaag over de drie rapporten: 6 van 30 calls.

**PostHog bevestigt de stilstand live.** Nul betaalde sessies van 14 tot en met 21 september. Op de distributeurspagina alleen organisch verkeer: 2 inzendingen (Letland 18 september, Malta 20 september) en opnieuw een formulierfout op 20 september.

**Wat de echte link-metrics laten zien.** Link CTR ligt gemiddeld op 55% van de all-clicks CTR en CPC (link) is 1,8 keer hoger dan CPC (all). Op link-metrics haalt alleen Statisch 2 (SWE) de Core-drempel (Link CTR 2,2%, CPC link €0,45). Statisch 1 (LIT) zou met 0,6% Link CTR mechanisch gepauzeerd worden, terwijl het op kosten per inzending (€36,06) een van de drie beste ads is. Beide SWE-video's vallen op link-metrics én conversie af.

**Waarschuwingen** gelden bij herstart: frequency 3,97 op LIT, CPM boven €15,00 op beide SWE-video's, en Statisch 2 (LIT) met goedkope clicks maar €63,63 per inzending.

**Zeven voorstellen wachten op je goedkeuring.** De eerste zes zijn bekend, nu opnieuw uitgewerkt op link-metrics. Nummer 7 is nieuw:

1. Herstart LIT op €100,00 en SWE op €40,00 per dag, met concrete bedragen per ad en de drie zwakste ads naar €0,00.
2. Drie hook-varianten (Statement, Label, Vraag) op de Statisch 2 (SWE) visual, Zweedse variant van Video 2 (LIT), nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, Statisch 1 (LIT) naar 25-65 zonder desktop, SWE verbreden, Letland en Malta als testlanden.
4. Conversie-guard op de kill-regels.
5. Funnel en pixel fix vóór herstart.
6. Eén gedeeld Meta-extract per dag.
7. Nieuwe 70-20-10 drempels gekalibreerd op de echte link-cijfers, zodat de indeling overeenkomt met de conversie-ranking. Dit sluit de TODO in het command.

Geef aan welke nummers ik mag uitvoeren. Als ik morgen de huidige ad-copy mag ophalen voor voorstel 2, kost dat één extra Meta-call.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
