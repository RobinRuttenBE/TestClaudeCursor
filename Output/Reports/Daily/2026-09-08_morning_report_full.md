# Morning Report — 2026-09-08

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport staat in `Output/Reports/Daily/2026-09-08_ads_report.md`, gecommit en gepusht (25618073). Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 8 september 2026

**Databronnen.** De Pipeboard MCP vroeg om authenticatie en de PostHog MCP gaf HTTP 405. Beide werkten via de directe route met de geconfigureerde tokens, dus dit rapport bevat echte 30-daagse cijfers (9 augustus t/m 7 september).

**Geen actieve campagnes.** Alle zeven campagnes staan op pauze. De Wholesaler campagnes (SWE en LIT) zijn sinds 4 september uit en Meta registreert 0 spend van 5 t/m 8 september. De laatste PostHog-inzending kwam op 4 september. Ten opzichte van gisteren is er niets veranderd behalve het venster dat één dag opschoof.

**Overzicht per campagne**

| Campagne | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |

Totaal €1.069,38 spend, 1.410 betaalde sessies, 23 geattribueerde inzendingen plus 9 zonder UTM. Meta telde 277 landing page views tegenover 1.410 PostHog-sessies, dus funnel-conclusies blijven op PostHog gebaseerd. ROAS is niet van toepassing bij lead-campagnes.

**Underperformers**
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27 en 0 inzendingen op 113 sessies. Definitief uit.
- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, €63,50 per inzending. Niet herstarten.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar de beste kosten per inzending (€28,75). Behouden.
- **Wholesaler (LIT)**: frequency 3,97. Inzendingen zakten vanaf 1 september van 16 naar 6 bij gelijk verkeer. Creative fatigue.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20), maar 290 sessies leveren maar 2 inzendingen op. Budget verlagen.

**Top performers**
- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38

**Aanbeveling (70-20-10):** bij herstart 70% naar de bewezen LIT-set (Video 1, Video 2, Statisch 1), 20% naar Statisch 2 (SWE), 10% naar één nieuwe creative per markt om de frequentie te doorbreken. Beide SWE-video's niet herstarten. De vijf herstart-voorstellen van 3 september wachten nog op je goedkeuring.

**Wil je funnel data toevoegen?** Gesprekken gepland, distributeurs actief en eerste orders zitten niet in Meta of PostHog. Lever die aan en ik draai de volledige funnel-diagnose.

---

Het rapport staat in `Output/Reports/Daily/2026-09-07_sybb_report.md` en is gecommit en gepusht (commit 7bba0e37).

**Hoe de data is opgehaald.** Beide MCP-servers waren in deze sessie niet bereikbaar: Pipeboard vroeg om autorisatie en de PostHog MCP gaf HTTP 405. Beide werkten wel via de directe HTTP-routes uit mijn memory, met de bestaande tokens. Geen enkele Google MCP is aangeroepen en de Google Sheet is niet bijgewerkt.

**Belangrijkste bevindingen voor 7 september:**

- **Meta Ads:** campagne `2026: SYBB` staat nog steeds op PAUSED sinds 19 april, nu 141 dagen. Nul spend, impressies en clicks, gisteren en in de 7 dagen ervoor. Alle 7 campagnes in het account zijn gepauzeerd. PostHog bevestigt onafhankelijk dat er 8 dagen geen enkele pageview met utm_source=meta binnenkwam.
- **Landing page:** startyourballoonbusiness.com had voor de tiende dag op rij 0 bezoekers.
- **Echte SYBB funnel op sempertexeurope.com:** 3 sessies, alle drie uit België en alle drie echte mensen. Voor het eerst sinds 3 september geen bot-hits. Volume ligt wel onder het 7-daags gemiddelde van 7,3 sessies.
- **Sterkste signaal:** één bezoeker klikte op het telefoonnummer op de registratiepagina. Een tweede bezoeker klikte tweemaal op "Registreer" en sloot het formulier binnen 22 seconden met "Afsluiten". Dat is de duidelijkste afgebroken inschrijving tot nu toe. Beide sessies kwamen 5 minuten na elkaar uit België, mogelijk dezelfde persoon op telefoon en daarna desktop.
- **Rode vlaggen:** session replay staat nu vier dagen op nul, dus die afgebroken inschrijving is niet terug te kijken. Er is nog steeds geen registratie-voltooid event.

**Top 3 acties in het rapport:** session replay herstellen in de PostHog-instellingen, zelf het registratieformulier van professional-8 op desktop doorlopen met alleen essentiële cookies om een technisch lek uit te sluiten, en een start- en voltooid-event voor de inschrijving toevoegen. Als kleine opvolging: check intern of er gisteren rond 11:53 lokale tijd een telefoontje over SYBB is binnengekomen.

---

Rapport staat in `Output/Reports/Daily/2026-09-08_auto_optimize.md`, gecommit en gepusht (2245f9fa). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST route) gebruikt, beide MCPs zelf weigerden. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes en alle 57 ads staan op PAUSED. Meta registreert 0 impressions en 0 spend over 5 t/m 8 september. De kill-regels hadden geen data om op te draaien, er zijn geen `update_ad` calls gedaan.

**PostHog bevestigt de stilstand.** Sinds 6 september 0 sessies met cpc als medium. De distributeurspagina kreeg alleen een handvol organische bezoekers. Laatste inzending was op 4 september, daarna 0.

**Niets veranderd ten opzichte van gisteren.** De zes voorstellen uit de run van 7 september staan ongewijzigd in het rapport en wachten op je goedkeuring:

1. Herstart Wholesaler (LIT) op €100,00 per dag, 70-20-10 verdeeld.
2. Herstart Wholesaler (SWE) beperkt op €40,00 per dag, alleen Statisch 2 plus één nieuwe creative.
3. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT).
4. Conversie-guard op de kill-regels, zodat Statisch 1 (LIT) niet op dag 1 na herstart wordt gepauzeerd.
5. LIT ad sets samenvoegen, SWE audience verbreden.
6. Tracking fix vóór herstart, Meta telt 19 leads tegenover 33 in PostHog.

Zolang er niets herstart is, blijft elke dagelijkse run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
