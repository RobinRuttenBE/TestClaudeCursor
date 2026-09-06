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
