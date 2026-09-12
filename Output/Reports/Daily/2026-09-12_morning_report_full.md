# Morning Report — 2026-09-12

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Het rapport staat in `Output/Reports/Daily/2026-09-12_ads_report.md` en is gecommit en gepusht (bce7f800). Alleen Pipeboard en PostHog gebruikt, beide via de directe HTTP-route omdat de MCP-servers niet verbonden. Geen Google-bronnen aangeroepen, geen Sheet geschreven.

## Meta Ads Rapport, 12 september 2026

**Er draait niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. PostHog bevestigt dat: 58 betaalde sessies op 4 september, daarna 0 tot 2 nalopers per dag. Laatste inzending blijft 4 september. Negende dag zonder levering.

**Beperking:** Pipeboard viel na drie calls op de weeklimiet van het Free plan. Campagne-cijfers zijn live van vandaag. Ad-level Meta-cijfers komen uit het rapport van 7 september over dezelfde periode en zijn ongewijzigd omdat er sindsdien geen levering was. Ad-level PostHog cijfers zijn wel live.

**Overzicht per campagne (last 30d)**

| Campagne | Spend | Impr. | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 90.888 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 39.267 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 7 | €72,46 |
| **Totaal** | **€1.069,38** | 130.155 | 2,2% | €0,37 | €8,22 | | 19 | 23 (+9 zonder UTM) | €46,49 |

ROAS niet van toepassing, het zijn lead-campagnes. Meta telt 277 landing page views tegenover 1.412 PostHog-sessies, dus kosten per inzending zijn op PostHog gebaseerd.

**Underperformers**

- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, 0 inzendingen op 113 sessies. Niet herstarten.
- **Video 2 (SWE)**: CPC €0,69, CPM €17,07, duurste ad van het account. Niet herstarten in deze vorm.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: laagste CPC (€0,20) maar 0,7% conversie en kortste sessies. Nieuwe hook testen.
- **Statisch 1 (LIT)**: link CTR 0,6%, maar 3,0% conversie. Behouden, lage CTR is hier geen kill-reden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38

**Funnel /become-a-distributor (30d):** 1.587 pageviews, 137 form starts, 35 inzendingen. Ruim 91% begint niet aan het formulier. Sinds de pauze 1 tot 8 sessies per dag, vrijwel allemaal organisch.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de LIT-winnaars (Video 1, Video 2, Statisch 1) plus Statisch 2 (SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). De vijf herstart-voorstellen van 3 september wachten nog op goedkeuring.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.

---

Het rapport staat in `Output/Reports/Daily/2026-09-11_sybb_report.md` en is gecommit en gepusht (831d75a9). Alleen Pipeboard en PostHog gebruikt, geen Google MCPs aangeroepen, geen Sheet geschreven.

**Belangrijkste bevindingen over 11 september**

- **Nul echte SYBB bezoekers.** PostHog telt drie sessies, maar twee zijn link-preview bots (Italië en Duitsland, 0 seconden, één event ooit) op de nieuwe Engelse eventpagina professional-48. De derde is het sluiten van de tab van de afbreker van 10 september, om 09:33 lokale tijd, zonder betaling en zonder tweede poging.
- **Meta campagne blijft PAUSED** (145 dagen). PostHog bevestigt: geen enkele Meta-pageview van 4 t/m 11 september. Landing page startyourballoonbusiness.com staat voor de veertiende dag op 0.
- **7-daags beeld (4 t/m 10 september):** 20 echte SYBB sessies, 4 inschrijfpogingen, 1 betaling. Het lek zit onveranderd in de stap na "Registreer".
- **Session replay staat acht dagen op nul.** Site-breed was gisteren opnieuw een crawlergolf: 89% van de 6.970 sessies is direct, 0 seconden, één pageview.
- **Warme pool:** 128 personen zagen in 30 dagen een SYBB pagina, 10 kwamen op meerdere dagen terug.

**Beperking Meta-data**

Pipeboard zat bij de eerste call al op de weeklimiet van het gratis plan (100 van 30 executies, reset maandag 14 september). De campagnestatus komt uit het live ads-rapport van vanochtend en het 30d-extract van gisteren, beide leeg qua levering. De Pipeboard MCP-servers vragen bovendien om autorisatie, dat kan alleen in een interactieve sessie via /mcp of de claude.ai connector-instellingen.

**Top 3 acties in het rapport**

1. Zelf de deelnemerstap van het registratieformulier doorlopen op mobiel Safari, uitgelogd en ingelogd (stond gisteren al op één, nog niet gedaan).
2. Session replay herstellen in de PostHog project settings en direct testen met die doorloop.
3. Pipeboard-verbruik terugbrengen: één gedeelde Meta-call per dag cachen voor de drie rapporten, of Pro-upgrade zodra de campagnes herstarten.

Memory bijgewerkt met de limietmelding-structuur van Pipeboard en twee HogQL-lessen (gereserveerde aliassen, pageleave-sessies van de vorige dag).

---

Rapport staat in `Output/Reports/Daily/2026-09-12_auto_optimize.md`, gecommit en gepusht (62124ca0). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt, beide MCP-servers zelf weigerden. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de Wholesaler campagnes sinds 4 september. Er is geen levering om de kill-regels op te draaien. Geen ads gepauzeerd, geen `update_ad` calls.

**Beperking:** de allereerste Pipeboard call kreeg al de weeklimiet-melding (100 van 30 calls gebruikt, reset maandag 14 september). Live Meta-cijfers over 9 t/m 12 september ontbreken dus. De campagnestatus komt uit het ads-rapport van vanochtend, de ad-level cijfers uit het rapport van 7 september.

**PostHog bevestigt de stilstand live.** Nul sessies met een Meta-UTM sinds 8 september, ook op ad-niveau. De paar Facebook- en Instagram-verwijzingen zijn organisch zonder UTM. Distributeurspagina kreeg 1 tot 8 organische bezoekers per dag. Laatste inzending blijft 4 september.

**Tiende dag op rij zonder levering.** De voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT), plus een nieuwe hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, SWE audience verbreden.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking fix vóór herstart, Meta telt 19 leads tegenover 33 in PostHog.
6. Nieuw: één gedeelde Meta-call per dag cachen voor de drie rapporten, anders valt Pipeboard na maandag opnieuw binnen 2 dagen droog.

Zolang er niets herstart is, blijft elke dagelijkse run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
