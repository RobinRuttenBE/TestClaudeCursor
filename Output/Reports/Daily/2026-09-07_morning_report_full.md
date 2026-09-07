# Morning Report — 2026-09-07

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport staat in `Output/Reports/Daily/2026-09-07_ads_report.md`, gecommit en gepusht (399a7c94). Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 7 september 2026

**Meta-data is weer bereikbaar.** De Pipeboard weeklimiet is gereset, dus dit rapport bevat echte 30-daagse cijfers in plaats van de laatst bekende stand. De PostHog MCP verbrak de verbinding, de directe REST-route werkte wel.

**Geen actieve campagnes.** Beide Wholesaler campagnes staan sinds 4 september op pauze en Meta registreert 0 spend van 5 t/m 7 september. De twee Video 1 (SWE) sessies van gisteren waren dus geen ad-levering. Geen actie nodig in Ads Manager.

**Overzicht per campagne (8 aug t/m 6 sep)**

| Campagne | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |

Totaal €1.069,38 spend, 1.409 betaalde sessies, 33 inzendingen. Meta telde 277 landing page views tegenover 1.409 PostHog sessies, dus funnel-conclusies blijven op PostHog gebaseerd.

**Underperformers**
- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27 en 0 inzendingen op 113 sessies. Definitief uit.
- **Wholesaler (LIT)**: frequency 3,97. Conversie zakte vanaf 1 september van 16 naar 6 inzendingen bij gelijk verkeer. Creative fatigue.
- **Statisch 1 (LIT)**: link CTR 0,6%, maar €36,06 per inzending. Lage CTR is hier geen kill-reden.

**Top performers**
- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38
- ROAS niet van toepassing, het zijn lead-campagnes

**Aanbeveling (70-20-10):** bij herstart 70% naar de bewezen LIT-set (Video 1, Video 2, Statisch 1), 20% naar Statisch 2 (SWE), 10% naar één nieuwe creative per markt om de frequentie te doorbreken. De vijf herstart-voorstellen van 3 september wachten nog op je goedkeuring; deze data bevestigt ze.

**Wil je funnel data toevoegen?** Gesprekken gepland, distributeurs actief en eerste orders zitten niet in Meta of PostHog. Lever die aan en ik draai de volledige funnel-diagnose.

---

Het rapport staat in `Output/Reports/Daily/2026-09-06_sybb_report.md` en is gecommit en gepusht (commit dcbc5c9f).

**Belangrijkste bevindingen voor 6 september**

- **Meta Ads was weer live bereikbaar.** De MCP-servers vroegen om autorisatie, maar de directe Pipeboard-route werkte na de maandagreset van de weeklimiet. Campagne "2026: SYBB" heeft nul spend, impressies en clicks over gisteren, 7 dagen en 30 dagen. Alle 7 campagnes in het ad account staan op PAUSED, SYBB nu 140 dagen.
- **Landing page startyourballoonbusiness.com** kreeg voor de negende dag op rij 0 bezoekers. Scroll- en CTA-metrics blijven onmeetbaar.
- **Echte SYBB funnel op sempertexeurope.com:** 8 sessies, boven het 7d-gemiddelde van 5,3. Vier zijn bots (directe 0-seconden hits uit Japan en de VS zonder vervolg-events), vier zijn echte bezoekers uit het VK, NL en BE. Drie van die vier eindigden hun sessie op een SYBB-registratiepagina, maar zonder registratie-voltooid event is niet te zien of ze zich inschreven.
- **Session replay staat nu drie dagen op nul** (4, 5 en 6 september), na duizenden opnames per dag tot 2 september. Vertraagde verwerking is als verklaring vrijwel afgevallen.
- **Opvallende lead:** een bezoeker uit het VK kwam via proballoonshop.co.uk, gebruikte de mengcalculator, bekeek de distributeurspagina en eindigde op de Engelse SYBB-registratie.

**Top 3 acties in het rapport:** replay-instellingen in PostHog controleren (Geel), een registratie-voltooid event laten bouwen (Oranje), en gedeelde registratie-links UTM-taggen zodat bots en mensen scheidbaar worden (Groen).

**Wat ik niet deed:** de PostHog MCP zelf (HTTP 405) en de Pipeboard MCP-tools waren onbruikbaar, dus beide bronnen zijn via hun directe API met de geconfigureerde tokens bevraagd. Geen Google MCPs aangeroepen, niets naar de Google Sheet geschreven. Het is maandag, maar er is geen SYBB-weekoverzicht gemaakt omdat de opdracht alleen het dagrapport betrof en de Weekly-map daar nog geen precedent voor heeft.

---

Rapport staat in `Output/Reports/Daily/2026-09-07_auto_optimize.md`, gecommit en gepusht (43f6b966). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Er zijn 0 actieve campagnes. Alle 8 Wholesaler-ads (4 LIT, 4 SWE) staan sinds 4 september 11:50 op PAUSED. Meta registreert €0,00 spend op 5, 6 en 7 september. De kill-regels hadden dus niets om op te draaien en er zijn geen `update_ad` calls gedaan.

**PostHog bevestigt de stilstand.** Betaalde sessies op de distributeurspagina gingen van 58 op 4 september naar 0 op 5 september, 2 op 6 september en 0 vandaag. Die twee sessies van gisteren kwamen via Instagram op de Video 1 (SWE) UTM binnen zonder Meta-impressions, dus het is een gedeelde of opgeslagen post en geen levering. Het handmatige check-punt van gisteren is daarmee afgehandeld. Sinds de pauze 0 form starts en 0 inzendingen.

**Eén observatie voor de herstart.** Op de laatste ochtend van 4 september triggerde Statisch 1 (LIT) mechanisch de Link CTR-regel (0,2% bij 1.830 impressions), terwijl het over 30 dagen een van de drie goedkoopste converters is. Zonder conversie-guard pauzeert auto-optimize deze ad op de eerste volle dag na herstart.

**Twee bijzonderheden in de setup**
- Het in het command genoemde tweede account act_607231713057715 bestaat niet in de Pipeboard-koppeling. Het staat al zo in het geheugen, maar het command verwijst er nog naar.
- De PostHog-token stond op een ander pad in de config dan verwacht. Ik heb dat pad in het geheugen genoteerd zodat de volgende run niet stokt.

**Voorstellen die op goedkeuring wachten** (uitgewerkt in het rapport):

1. Herstart Wholesaler (LIT) op €100,00 per dag, 70-20-10 verdeeld over Video 2, Video 1, Statisch 1, Statisch 2 en één nieuwe creative.
2. Herstart Wholesaler (SWE) beperkt op €40,00 per dag, alleen Statisch 2 plus één nieuwe creative.
3. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT).
4. Conversie-guard op de kill-regels: niet pauzeren bij minimaal 1 PostHog-inzending onder €40,00.
5. LIT ad sets samenvoegen, SWE audience verbreden.
6. Tracking fix vóór herstart, Meta telt 19 leads tegenover 33 in PostHog.

Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
