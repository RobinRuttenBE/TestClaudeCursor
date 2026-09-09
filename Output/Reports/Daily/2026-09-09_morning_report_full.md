# Morning Report — 2026-09-09

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport staat in `Output/Reports/Daily/2026-09-09_ads_report.md`, gecommit en gepusht (ee88aa6f). Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 9 september 2026

**Databronnen.** De Pipeboard MCP vroeg om authenticatie en de PostHog MCP gaf HTTP 405. Beide werkten via de directe route met de geconfigureerde tokens, dus dit rapport bevat echte 30-daagse cijfers (10 augustus t/m 8 september).

**Geen actieve campagnes.** Alle zeven campagnes staan op pauze. De Wholesaler campagnes (SWE en LIT) zijn sinds 4 september uit. Meta registreert €0,00 spend op 8 september en PostHog ziet nog maar 1 tot 4 restsessies per dag op de distributeurpagina. Laatste inzending: 4 september. Ten opzichte van gisteren is er niets veranderd behalve het venster dat één dag opschoof.

**Overzicht per campagne (last 30d)**

| Campagne | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |

Totaal €1.069,38 spend, 1.407 betaalde sessies, 23 geattribueerde inzendingen plus 4 zonder UTM. Meta telde 277 landing page views tegenover 1.407 PostHog-sessies, dus funnel-conclusies zijn op PostHog gebaseerd. ROAS is niet van toepassing bij lead-campagnes.

**Underperformers**
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27 en 0 inzendingen op 113 sessies. Niet herstarten.
- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, €63,50 per inzending. Niet herstarten.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste kosten per inzending (€28,75). Behouden.
- **Wholesaler (LIT)**: frequency 3,97. Inzendingen zakten vanaf 1 september van 16 naar 6 bij gelijk verkeer. Creative fatigue.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20), maar 290 sessies leveren maar 2 inzendingen op. Budget verlagen.

**Top performers**
- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38

**Aanbeveling (70-20-10):** bij herstart 70% naar de bewezen LIT-set (Video 1, Video 2, Statisch 1), 20% naar Statisch 2 (SWE), 10% naar één nieuwe creative per markt om de frequency te doorbreken. Beide SWE-video's niet herstarten. De vijf herstart-voorstellen van 3 september wachten nog op je goedkeuring.

**Wil je funnel data toevoegen?** Gesprekken gepland, distributeurs actief en eerste orders zitten niet in Meta of PostHog. Lever die aan en ik draai de volledige funnel-diagnose.

---

Het rapport staat in `Output/Reports/Daily/2026-09-08_sybb_report.md` en is gecommit en gepusht naar main (commit a7e79d95).

**Belangrijkste bevindingen voor 8 september**

- **Meta Ads: nul levering.** Campagne `2026: SYBB` staat 142 dagen op PAUSED, net als alle 7 campagnes in het account. Gisteren en de 7 dagen ervoor: €0 spend, 0 impressies, 0 clicks. PostHog bevestigt dit onafhankelijk, geen enkele pageview met utm_source=meta deze week.
- **Landing page startyourballoonbusiness.com: elfde dag op rij 0 bezoekers.** Scroll- en CTA-metrics zijn daar structureel niet te berekenen.
- **Werkelijke SYBB funnel op sempertexeurope.com: 2 bezoekers in 3 sessies**, de laagste dag van de week, allebei echte mensen op mobiel Safari.
- **Tweede afgebroken inschrijving in twee dagen, hetzelfde patroon.** Een Belgische bezoeker klikte op "Registreer" op professional-9 en 10 seconden later op "Afsluiten". Op 7 september gebeurde exact hetzelfde op desktop op professional-8. Twee personen, twee devices, twee pagina's, hetzelfde resultaat. Dit wijst op een formulier- of prijsprobleem, niet op toeval.
- **De Nederlandse bezoeker liet de registratiepagina 46 minuten open** en ging daarna ballonnen bekijken in de webshop in plaats van in te schrijven.
- **Session replay staat vijf dagen op nul**, dus van geen van beide afgebroken inschrijvingen bestaat een opname.
- Organisch social verkeer naar de site (Facebook en Instagram referrals) zakte van 188 pageviews op 3 september naar 0 op 7 en 8 september.

**Top 3 acties in het rapport**

1. Zelf het registratieformulier doorlopen op een iPhone in Safari op professional-7, 8 en 9, en noteren wat er na "Registreer" verschijnt. 10 minuten, Groen.
2. In PostHog twee actions aanmaken op de bestaande autocapture-clicks, "Registreer" en "Afsluiten", zodat het rapport vanaf morgen een start- en afbreek-KPI heeft zonder code. 15 minuten, Groen.
3. Session replay herstellen via de project settings en met een testsessie bevestigen. 10 minuten, Geel.

**Databronnen en beperkingen**

Beide MCP servers waren niet direct bruikbaar: Pipeboard vroeg om autorisatie en de PostHog MCP gaf HTTP 405. Ik heb daarom de directe routes gebruikt die in de memory-notities staan, met dezelfde Pipeboard token en dezelfde PostHog project (STX EU, 149694). Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt. Eén batch PostHog-queries liep vast op een trage subquery-vorm; ik heb dat opgelost met losse queries en de snelle query-vorm toegevoegd aan de memory-notitie over PostHog.

Als je de Pipeboard en PostHog MCP servers in een interactieve sessie opnieuw autoriseert via /mcp, dan hoeft de volgende run niet meer om te rijden via de directe HTTP-routes.

---

Rapport staat in `Output/Reports/Daily/2026-09-09_auto_optimize.md`, gecommit en gepusht (0f2db115). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST route) gebruikt, beide MCPs zelf weigerden. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED. Meta geeft over 6 t/m 8 september 0 rijen op ad-niveau, dus 0 impressions, 0 link clicks en €0,00 spend. Er zijn geen ads gepauzeerd en geen `update_ad` calls gedaan.

**PostHog bevestigt de stilstand.** 0 sessies met cpc als medium sinds 6 september. De distributeurspagina kreeg 1 tot 5 organische bezoekers per dag. Laatste inzending blijft 4 september.

**Niets veranderd ten opzichte van gisteren.** Dit is de zesde dag op rij zonder levering. De vijf voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, en Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT).
3. LIT ad sets samenvoegen, SWE audience verbreden.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking fix vóór herstart, Meta telt 19 leads tegenover 33 in PostHog.

Zolang er niets herstart is, blijft elke dagelijkse run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
