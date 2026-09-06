# Morning Report — 2026-09-06

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport staat in `Output/Reports/Daily/2026-09-06_ads_report.md`, gecommit en gepusht (fd6f789a). Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 6 september 2026

**Meta Ads data was vandaag op geen enkele route bereikbaar.** De Pipeboard MCP vraagt om authenticatie, de directe JSON-RPC route geeft "weekly limit reached on your Free plan", en het opgeslagen Facebook-token is verlopen. De Meta-cijfers in het rapport zijn daarom de laatst bekende stand van 4 september, duidelijk zo gelabeld.

**PostHog werkt wel en bevestigt de pauze.** Betaalde sessies op de distributeurspagina gingen van rond 200 per dag naar 0 op 5 september. Sinds de pauze zijn er 0 inzendingen. Eindstand 27 augustus t/m 4 september blijft 1.406 betaalde sessies en 33 inzendingen.

**Eén ding om te checken.** Vandaag kwamen om 04:53 en 06:31 UTC twee betaalde sessies binnen met `utm_campaign=wholesaler_se` en `utm_content=video_01`. Dat is Video 1 (SWE), de ad die op 4 september is gepauzeerd en die volgens gisteren niet terug zou komen. Twee dagen nalevering is ongebruikelijk. Kijk in Ads Manager of die ad per ongeluk weer aanstaat.

**Laatst bekende stand (27 aug t/m 4 sep)**

| Campagne | Status | Spend | Link CTR | Link CPC | CPM | Freq. | Inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Paused | €562,13 | 1,0% | €0,64 | €6,18 | 3,97 | 16 | €35,13 |
| Wholesaler (SWE) | Paused | €507,24 | 1,8% | €0,73 | €12,92 | 3,29 | 8 | €63,41 |
| 2026: SYBB | Paused sinds 19 apr | €0,00 | n.v.t. | n.v.t. | n.v.t. | n.v.t. | 0 | n.v.t. |

Underperformers, top performers en de 70-20-10 aanbeveling zijn ongewijzigd ten opzichte van gisteren en staan volledig in het rapport. De vijf herstart-voorstellen wachten nog op je goedkeuring.

**Om morgen weer Meta-data te hebben**, kies één van deze:
1. Pipeboard upgraden naar Pro, of wachten tot de weekteller reset. Dit raakt ook het morning report en auto-optimize.
2. In een interactieve sessie `/mcp` draaien en de Pipeboard connector opnieuw autoriseren.
3. Een Meta System User token met `ads_read` in de config zetten als fallback naar de Marketing API.

Deze bevinding staat ook in mijn memory, zodat volgende runs direct de laatst bekende stand rapporteren in plaats van vast te lopen.

**Wil je funnel data toevoegen?** Gesprekken gepland, distributeurs actief en eerste orders zitten niet in Meta of PostHog. Lever die aan en ik draai de volledige funnel-diagnose.

---

Rapport staat in `Output/Reports/Daily/2026-09-05_sybb_report.md`, gecommit en gepusht (ed194ecc). Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Meta Ads was op geen enkele route bereikbaar.** De Pipeboard MCP vraagt autorisatie in deze niet-interactieve sessie en de directe route meldt de weeklimiet van het gratis plan. Het rapport gebruikt de laatst bekende stand: campagne PAUSED sinds 19 april, nul spend in de 30d extract van 5 september. PostHog bevestigt dat onafhankelijk: gisteren geen enkele pageview met `utm_source=meta` op de hele site.

**SYBB gisteren, uit PostHog.** Landing page opnieuw 0 bezoekers, al 8 dagen. De event registratiepagina's op sempertexeurope.com hadden 5 bezoekers, gelijk aan het 7d gemiddelde. Drie daarvan waren directe 0s hits zonder pageleave of autocapture, uit Duitsland, Japan en Zweden op Franse en Engelse registratie-URL's. Dat patroon wijst op link-preview bots op gedeelde links zonder UTM. De twee echte bezoekers bekeken de registratiepagina 4 tot 15 seconden en klikten terug naar de eventlijst. Conversie blijft onmeetbaar.

**Nieuwe bevinding over session replay.** Het rapport van 4 september meldde nul opnames voor de hele week, maar die opnames blijken er nu wel te zijn: honderden tot duizenden per dag van 29 augustus t/m 2 september, 92 op 3 september, daarna nul. Replay is dus gestopt of loopt achter. Dit staat als correctie in het rapport en ik heb de memory-notitie over PostHog aangepast.

**Top 3 acties in het rapport:**
1. Meta toegang herstellen: Pipeboard Pro, `/mcp` opnieuw autoriseren, of een System User token als fallback.
2. Session replay instellingen en activity log rond 3 september nakijken.
3. Registratie-voltooid event laten bouwen na `/event/*/register`.

Twee PostHog-calls vielen weg door socket-fouten en zijn met succes opnieuw gedraaid. De werkboom bevat nog ongecommitte wijzigingen van andere processen (ads-rapport van 6 september, logs, submodule). Die heb ik niet aangeraakt.

---

Rapport staat in `Output/Reports/Daily/2026-09-06_auto_optimize.md`, gecommit en gepusht (bde52e95). Alleen Pipeboard (geprobeerd) en PostHog (claude.ai connector) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Meta Ads was voor de tweede dag op rij op geen enkele route bereikbaar. De Pipeboard MCP vraagt authenticatie, de directe JSON-RPC route zit nog op de weeklimiet van het Free plan, en er staat geen ander Meta-token in de config. Zonder impressions en link clicks kunnen de kill-regels niet draaien. Volgens de laatst bekende stand staan alle 8 Wholesaler-ads sowieso op PAUSED sinds 4 september.

**PostHog bevestigt de stilstand.** Betaalde sessies per dag gingen van 186 op 3 september naar 50 op 4 september, 4 op 5 september en 1 vandaag. De vier sessies van 5 september waren organisch Facebook-verkeer via een Britse retailer, geen ads. Sinds de pauze zijn er 0 form starts en 0 inzendingen.

**Eén ding om zelf te checken.** Vanochtend om 04:53 UTC kwam een echte Zweedse bezoeker via Instagram binnen op de Video 1 (SWE) UTM, 11 seconden op de pagina. Eén bezoeker in 48 uur tegenover 10 sessies per dag toen de ad live was, wijst op een opgeslagen of gedeelde ad-post en niet op actieve levering. Omdat ik dit niet in Meta kan verifiëren: open Ads Manager en bevestig dat Video 1 (SWE) op PAUSED staat.

**Voorstellen die op goedkeuring wachten** staan ongewijzigd in het rapport, met één nieuwe randvoorwaarde:

0. Meta-data herstellen: Pipeboard Pro, connector opnieuw autoriseren via `/mcp`, of een System User token als fallback. Zonder dit kan auto-optimize morgen weer niets doen.
1. Tracking fixen voor de herstart (Meta 19 leads, PostHog 33).
2. Budget herverdeling bij herstart op €140 per dag, Core op Statisch 2 (SWE) en de twee LIT-video's.
3. Drie hook-varianten per land plus CTA-test.
4. Beslissing over Video 2 (LIT): conversie-guard of strikt pauzeren.
5. LIT ad sets samenvoegen, SWE audience verbreden.

Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
