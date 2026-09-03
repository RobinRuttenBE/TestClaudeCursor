# Morning Report — 2026-09-03

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

API Error: Can't reach the API server — check your internet or DNS (ENOTFOUND)

---

Het rapport staat in `Output/Reports/Daily/2026-09-02_sybb_report.md` en is gecommit en gepusht naar main (0f68a0d6).

**Databronnen.** De Pipeboard MCP meldde een auth-fout en de PostHog MCP verbond niet (DNS fout, daarna HTTP 405). Beide geconfigureerde tokens werkten wel via directe calls op dezelfde endpoints, dus de data komt uit Pipeboard en PostHog project STX EU. Geen Google MCPs aangeroepen, niets naar de Google Sheet geschreven.

**Belangrijkste bevindingen voor 2 september:**
- **Campagne 2026: SYBB staat nog op PAUSED** sinds 19 april. Nul spend en nul impressies over de hele week, ook voor de kopie-campagne.
- **Landing page startyourballoonbusiness.com kreeg 0 bezoekers.** Geen scroll-, CTA- of recording-data beschikbaar.
- **De event registratiepagina's op sempertexeurope.com kregen 5 bezoekers in 6 sessies**, tegen een 7-daags gemiddelde van 5,7. Alles via site navigatie, geen UTM's. Editie 7 trekt 4 van de 5 bezoekers.
- **Valse conversiepagina ontmaskerd.** De pagina `/registratie-voltooid` dook op in een SYBB sessie, maar is de B2B accountregistratie van de webshop, niet de workshopinschrijving. Conversie blijft dus onmeetbaar.
- **Nieuw kruisverband.** In 30 dagen eindigden 4 van 148 SYBB sessies in een voltooide accountregistratie. Mogelijk vereist de event-inschrijving een klantaccount. Dat is niet bevestigd en vraagt een handmatige check.

**Top 3 acties in het rapport:** een registratie-voltooid event op de event funnel toevoegen, als uitgelogde bezoeker testen of inschrijven een account vereist, en de skill herdefiniëren op de registratiepagina's in plaats van de dode landing page.

**Memory bijgewerkt.** Nieuwe referentie voor de directe PostHog API (host, project id, HogQL endpoint) en een aanvulling op de SYBB funnel notitie dat `/registratie` de accountflow is.

---

Rapport staat in `Output/Reports/Daily/2026-09-03_auto_optimize.md`, gecommit en gepusht (493bbaa5). Alleen Meta Ads via Pipeboard en PostHog gebruikt, geen Google MCPs, niets naar de Sheet geschreven.

## Auto-Optimize, 3 september 2026

**Geen ads gepauzeerd.** Twee actieve campagnes (Wholesaler SWE en LIT), 8 ads, elk €20,00/dag. Periode 31 augustus t/m 2 september, alles op link metrics. Het tweede account uit het command (act_607231713057715) bestaat niet in deze koppeling.

**Kill-regels**

- **CPC (link) > €1,50**: niet van toepassing, geen enkele ad heeft 500 link clicks.
- **Link CTR < 0,8%**: Statisch 1 (LIT) triggert voor de tweede dag op rij met 0,48% op 12.389 impressions. Opnieuw niet gepauzeerd, en nu met harder bewijs: PostHog laat zien dat deze ad 2 formulier-inzendingen leverde in 3 dagen (€30,52 per inzending) en lifetime de hoogste sessie-naar-inzending ratio van alle 8 ads heeft (4,0%). De lage CTR zit in Facebook en desktop, wie doorklikt converteert bovengemiddeld. Ik heb in het rapport een concrete regel voor de volgende run vastgelegd: pauzeren zodra de ad 3 dagen op rij 0 inzendingen heeft. Beslissing ligt bij jou (voorstel 5).

**Belangrijkste bevinding: de Meta pixel telt structureel te weinig.** Gisteren stond in het rapport dat maar 12 tot 17% van de link clicks een landing page view werd. Dat klopt niet. PostHog ziet 521 sessies op 635 link clicks (82%) en 9 form submits waar Meta er 5 als lead telt. Het lek zit in de meting, niet in de landing page. De ad sets optimaliseren daardoor op een half signaal. Dit is de belangrijkste actie van vandaag.

**Waarschuwingen**

- Video 1 (SWE): 0 leads en 0 inzendingen na €115,49 in 6 dagen, CPM €15,60.
- Video 2 (SWE): CPM €18,16, 1 inzending na €113,21, Instagram Link CTR 0,74%.
- Video 2 (LIT): 37% van de link clicks komt van Audience Network (nep-clicks), maar wel 5 inzendingen lifetime, dus behouden.
- Statisch 2 (LIT): goedkoopste clicks (€0,43) maar 0 inzendingen in 3 dagen. Niet opschalen op clicks alleen.

**70-20-10**: Core (Statisch 2 SWE, Video 1 LIT, Video 2 LIT) krijgt 37,5% in plaats van 70%. De twee SWE-video's krijgen 25% in plaats van 10%.

**Voorstellen (wachten op jouw goedkeuring)**

1. **Budget**, budget-neutraal op €160/dag: Video 1 (SWE) pauzeren, Video 2 (SWE) naar €10,00, Statisch 2 (SWE), Video 1 (LIT) en Video 2 (LIT) elk naar €30,00.
2. **Variaties**: alle 8 ads hebben identieke copy, de hook-test is nog niet gestart. Drie varianten per land op de winnende Statisch 2 visual (Statement, Label, Vraag), met andere CTA's.
3. **Audience**: Statisch 1 (LIT) naar 25-65 en desktop uitsluiten. Audience Network overal uitsluiten. Instagram uit voor Video 2 (SWE).
4. **Tracking check**: verifieer op de become-a-distributor pagina of het Meta Pixel PageView en Lead-event vuren bij formulierinzending (pixel of Conversions API).
5. **Statisch 1 (LIT)**: A laten draaien met audience-fix en de kill-regel voor lead-campagnes aanpassen naar "Link CTR < 0,8% én 0 inzendingen in 3 dagen" (aanbevolen), of B strikt pauzeren.

Geef aan welke nummers je wilt uitvoeren (1, 2, 3, 4, 5A of 5B).

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
