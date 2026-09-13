# Morning Report — 2026-09-13

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Het rapport staat in `Output/Reports/Daily/2026-09-13_ads_report.md`, gecommit en gepusht (1d7ff4f6). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 13 september 2026

**Er draait niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. PostHog bevestigt dat live: na 4 september nog 3 nalopers in totaal, en nul betaald verkeer op 10, 11 en 12 september. Elfde dag zonder levering. Laatste inzending blijft 4 september.

**Beperking:** Pipeboard zat bij de eerste call al op de weeklimiet van het Free plan. De resetdatum in het antwoord is opgeschoven naar 21 september, niet 14 september. Meta-cijfers komen daarom uit het rapport van 7 september en zijn ongewijzigd omdat er sindsdien geen levering was. PostHog-cijfers zijn live van vandaag.

**Overzicht per campagne (last 30d)**

| Campagne | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 |
| **Totaal** | **€1.069,38** | 2,2% | €0,37 | €8,22 | | 19 | 24 (+11 zonder UTM) | €30,55 all-in |

ROAS niet van toepassing, het zijn lead-campagnes. Meta telt 19 leads tegenover 35 inzendingen in PostHog, dus kosten per inzending zijn op PostHog gebaseerd.

**Underperformers**

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, 0 inzendingen op 97 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: meeste sessies, kortste duur (56s), 0,8% conversie, circa €63,63 per inzending. Nieuwe hook testen.
- **Statisch 1 (LIT)**: link CTR 0,6%, maar 3,8% conversie. Behouden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38

**Funnel /become-a-distributor (30d):** 1.743 pageviews, 137 formulierstarts, 35 inzendingen. Sinds de pauze 1 tot 8 organische sessies per dag.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). De herstart-voorstellen van 3 september wachten nog op goedkeuring.

**Operationeel:** Pipeboard blijft tot 21 september dicht. Het voorstel om één gedeelde Meta-call per dag te cachen voor de drie rapporten wordt hiermee urgent, anders valt de route na de reset binnen 2 dagen opnieuw dicht.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.

---

Het SYBB rapport voor 12 september staat in `Output/Reports/Daily/2026-09-12_sybb_report.md`, gecommit en gepusht (88e214c2). Het rapport bestond al van de ochtendrun; ik heb alle data opnieuw opgehaald, de cijfers bevestigd en het bestand bijgewerkt in plaats van een duplicaat te maken.

**Samenvatting van het rapport**

- **Meta Ads niet live.** Pipeboard gaf bij de eerste call `weekly_limit_exceeded` (100 van 30 executies, Free plan). De resetdatum staat op 21 september 2026 00:00 UTC. Campagne `2026: SYBB` staat op PAUSED sinds 19 april. Spend, impressies en clicks gisteren: 0. PostHog bevestigt dit onafhankelijk: nul pageviews met `utm_source=meta` sinds 5 september.
- **Landing page startyourballoonbusiness.com** staat voor de vijftiende dag op 0 bezoekers. Bounce, scroll en CTA zijn daar niet te meten omdat die events niet bestaan.
- **Werkelijke funnel (eventpagina's op sempertexeurope.com):** 8 SYBB sessies gisteren, 6 van echte mensen, tegen een 7d gemiddelde van 2,7. Drukste dag van de week.
- **Vijfde inschrijfpoging van de week strandde op dezelfde plek.** Een nieuwe NL bezoeker op mobiel Safari klikte om 06:59 lokale tijd op Register, bevestigde het ticket en sloot het deelnemersvenster binnen 1 seconde. Vier van vijf pogingen in zeven dagen breken hier af. De enige betaler (9 september) was ingelogd.
- **Session replay is leeg.** De hele tabel bevat nog één opname uit maart. De opnames van eind augustus zijn verdwenen.
- **Nieuw kanaal gespot:** de webshop-productpagina voor de workshop van 5 en 6 oktober kreeg gisteren voor het eerst sinds 21 augustus een bezoeker. Het rapport telt dat kanaal nog niet als funnelstap.

**Top 3 acties in het rapport**

1. Zelf de deelnemerstap doorlopen op een iPhone in Safari, uitgelogd, op de Engelse pagina van professional-8, en vastleggen wat er na de ticketbevestiging verschijnt.
2. Replay-instellingen en bewaartermijn in PostHog controleren en een testopname maken.
3. Beslissen of eventpagina of webshop-product het canonieke SYBB verkoopkanaal is, en de skill daarop aanpassen.

**Wat ik bij de herverificatie aanpaste**

- Crawler-telling bijgewerkt van 5.319 naar 5.326 direct-nul sessies (91% blijft gelijk), bezoekers van 5.774 naar 5.784.
- Herverificatienotitie toegevoegd in de databronnen-voetnoot met alle bevestigde cijfers en de resetdatum van Pipeboard.

**Bronnen en beperkingen.** Pipeboard MCP vroeg om autorisatie en de directe JSON-RPC route zat op de weeklimiet. PostHog MCP gaf HTTP 405, de directe REST-route op project STX EU werkte volledig. Geen Google MCPs aangeroepen, niets naar de Google Sheet geschreven. Voor live Meta-data tot 21 september is een Pipeboard Pro-plan of een herautorisatie van de MCP via /mcp nodig.

---

Rapport staat in `Output/Reports/Daily/2026-09-13_auto_optimize.md`, gecommit en gepusht (734e40fa). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST route) gebruikt, beide MCP-servers zelf weigerden. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de Wholesaler campagnes sinds 4 september. Er is geen levering om de kill-regels op te draaien. Geen ads gepauzeerd, geen `update_ad` calls.

**Beperking:** de eerste Pipeboard call kreeg direct de weeklimiet-melding (100 van 30 calls gebruikt, reset 21 september 00:00 UTC). Live Meta-cijfers over 10 t/m 13 september ontbreken. Campagnestatus komt uit het ads-rapport van vanochtend, ad-level cijfers uit het extract van 7 september.

**PostHog bevestigt de stilstand live.** Nul sessies met een Meta-UTM op 10, 11, 12 en 13 september, ook per campagne en per ad. Nul inzendingen. Distributeurspagina kreeg 0 tot 8 organische bezoekers per dag. Twaalfde dag zonder levering.

**De zes voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:**

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT), plus een nieuwe hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, SWE audience verbreden.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking fix vóór herstart, Meta telt 19 leads tegenover 35 in PostHog.
6. Eén gedeelde Meta-call per dag cachen voor de drie rapporten, anders valt Pipeboard na 21 september binnen 2 dagen opnieuw dicht.

Zolang niets herstart is, blijft elke run op 0 acties uitkomen. Eerstvolgende run met live Meta-data is op of na 21 september, tenzij Pipeboard eerder naar Pro gaat of je de MCP opnieuw autoriseert via /mcp. Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
