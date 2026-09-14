# Morning Report — 2026-09-14

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Het rapport staat in `Output/Reports/Daily/2026-09-14_ads_report.md`, gecommit en gepusht (a7099958). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 14 september 2026

**Er draait niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september 11:50. Meta geeft voor de laatste 7 dagen nul rijen. PostHog bevestigt dat live: na 4 september nog 5 nalopers (6, 7 en 9 september), nul betaald verkeer op 10 t/m 13 september. Laatste inzending blijft 4 september.

**Goed nieuws:** Pipeboard werkte vandaag weer, de weeklimiet was gewoon gereset ondanks de resetdatum van 21 september in het antwoord van gisteren. Alle Meta-cijfers zijn vandaag vers opgehaald.

**Overzicht per campagne (last 30d)**

| Campagne | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | **€1.069,38** | 2,2% | €0,37 | €8,22 | | 19 | 23 (+12 zonder UTM-match) | €30,55 all-in |

ROAS niet van toepassing, het zijn lead-campagnes. Meta telt 19 leads tegenover 35 inzendingen in PostHog, dus kosten per inzending zijn op PostHog gebaseerd.

**Underperformers**

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, 0 inzendingen op 97 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar kortste sessies (52s), 0,8% conversie, €63,63 per inzending. Nieuwe hook testen.
- **Video 2 (LIT)** en **Statisch 1 (LIT)** krijgen een CPC- of CTR-vlag maar zijn de beste converteerders (4,1% en 3,8%). Behouden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38

**Funnel /become-a-distributor (30d):** 1.743 pageviews, 137 formulierstarts, 35 inzendingen.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. De herstart-voorstellen van 3 september wachten nog op jouw goedkeuring.

**Operationeel:** vier Pipeboard-calls gebruikt in deze run. Een campagne-lijst met status_filter hing 60 seconden, zonder filter kwam hij direct terug. Dat staat nu in het geheugen. Het voorstel om één gedeelde Meta-call per dag te cachen voor de drie rapporten blijft staan, anders valt de route later deze week opnieuw dicht.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.

---

Het rapport staat in `Output/Reports/Daily/2026-09-13_sybb_report.md`, gecommit en gepusht (c3cab522). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## SYBB rapport, 13 september 2026

**Meta Ads: niets loopt, maar de data is vandaag live.** Pipeboard werkte weer na de reset van de weeklimiet. Campagne `2026: SYBB` staat op PAUSED sinds 19 april (147 dagen), alle 7 campagnes in het account zijn gepauzeerd. Nul rijen voor 13 september en voor de 7 dagen ervoor. PostHog bevestigt dat: nul pageviews met `utm_source=meta` en de landing page startyourballoonbusiness.com staat voor de zestiende dag op 0 bezoekers.

**Event funnel op sempertexeurope.com: rustige, schone dag zonder inschrijfpoging.**

| Metric | 13 sep | 7d gemiddelde |
|---|---|---|
| SYBB sessies | 6 (alle echt, 0 bot) | 4,7 |
| Bounce rate | 0% | 27% |
| Sessieduur | 207s | 206s |
| Klik op Register | 0 | 5 in 7 dagen |
| Betaald | 0 | 1 (9 sep) |

**Drie observaties**

- **Drie vergelijkers, geen kiezers.** Twee bezoekers openden respectievelijk 2 en 5 verschillende SYBB registratiepagina's (professional 7, 8, 9, 47, 48) plus andere masterclasses, zonder op Register te klikken. Het events-overzicht laat datum, stad en taal niet in één blik zien.
- **Eerste aanwijzing voor de account-hypothese.** Een Nederlandse shopbezoeker opende de klantaccount-registratie 50 seconden vóór de SYBB pagina. Geen bewijs, wel de eerste keer dat iemand die volgorde laat zien.
- **Eerste SYBB bezoeker via ChatGPT.** Een sessie uit Australië kwam met `utm_source=chatgpt.com` op het events-overzicht en opende professional-9.

**Rode vlaggen:** session replay bevat van 6 t/m 13 september nul opnames, dus geen van de inschrijfpogingen van de afgelopen week is terug te kijken. De crawlergolf neemt af maar houdt aan (76% bot-achtige sessies site-breed, was 91%). De 70 rage clicks van gisteren zaten allemaal op shoppagina's, niet op SYBB.

**Top 3 acties**

1. Zelf de inschrijving doorlopen op iPhone Safari, uitgelogd, op professional-8 en screenshot van het deelnemersvenster maken. Staat voor de vierde dag op één.
2. Eén datum- en locatieoverzicht van alle SYBB data op /events en boven elke registratieknop zetten, zodat vergelijkers niet vijf pagina's hoeven te openen.
3. Replay-instellingen en retentie in PostHog controleren, en de testsessie uit actie 1 als controle gebruiken.

**Operationeel:** drie Pipeboard-calls gebruikt. In het PostHog-geheugen genoteerd dat een `arrayFilter` in de select-lijst van een sessions-query de timeout raakt, en dat chatgpt.com nu als entry source verschijnt.

---

Rapport staat in `Output/Reports/Daily/2026-09-14_auto_optimize.md`, gecommit en gepusht (356b500b). Alleen Pipeboard (directe JSON-RPC route, 2 calls) en PostHog (directe REST-route) gebruikt, beide MCP-servers zelf weigerden opnieuw. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Meta bevestigt live dat alle 7 campagnes op PAUSED staan, de twee Wholesaler campagnes sinds 4 september 11:50. De ad-level insights over 11 t/m 13 september geven nul rijen. De kill-regels hadden niets om op te draaien, geen `update_ad` calls gedaan.

**PostHog bevestigt de stilstand.** Nul sessies met een Meta-UTM sinds 11 september. De distributeurspagina kreeg alleen 10 organische pageviews op 11 en 12 september en nul inzendingen. Laatste betaalde inzending blijft 4 september, elfde dag zonder levering.

**Pipeboard werkte vandaag weer.** De weeklimiet was maandag gewoon gereset, ondanks de resetdatum van 21 september in het antwoord van gisteren. Dat staat al in het geheugen. Deze run gebruikte bewust maar 2 calls om de limiet te sparen.

**De zes voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:**

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE), twee op Video 2 (LIT), en een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE audience verbreden, Statisch 1 (LIT) naar 25-65 zonder desktop.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking fix vóór herstart, Meta telt 19 leads tegenover 35 in PostHog.
6. Eén gedeeld Meta-extract per dag cachen voor de drie rapporten, anders valt de gratis weeklimiet later deze week weer dicht.

Zolang niets herstart is, blijft elke run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
