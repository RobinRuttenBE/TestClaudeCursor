Committed and pushed. Report saved to `Output/Reports/Daily/2026-07-31_auto_optimize.md`.

## Auto-Optimize 31 juli 2026: geen acties

**Er is niets gewijzigd in het ad account.** Nul actieve campagnes, nul impressions, nul spend over de afgelopen 3 dagen én over 90 dagen. Alle 5 campagnes in `act_567892422940728` staan op PAUSED, laatste delivery was april 2026. Kill-regels kunnen zonder delivery niet triggeren, dus **0 ads gepauzeerd**.

Dit is de tweede dag op rij met een identieke nul-uitkomst.

### Wat wel nieuw is

**De SYBB landingspagina wordt helemaal niet gemeten in PostHog.** De enige hostnames die events sturen zijn `www.sempertexeurope.com` en de Odoo backend. `startyourballoonbusiness.com` komt niet voor, en de organisatie heeft maar één project, dus de data staat ook niet elders.

Dat betekent dat de KPI-targets uit `CLAUDE.md` (LP bounce rate, scroll depth, CTA click rate, time on page) op dit moment niet meetbaar zijn, en dat de Meta/PostHog cross-reference in het morning report op een aanname draait die niet klopt. Ik zou dit als blokkerend behandelen voor heropstart.

### Baseline vastgelegd voor heropstart

Ik heb de laatste actieve periode (april 2026, 8 ads, €1.059,47) doorgerekend op link metrics, zodat er een vertrekpunt ligt:

| | All clicks | Link |
|---|---|---|
| CTR | 2,1% | **1,1%** |
| CPC | €0,55 | **€1,02** |

Precies de vertekening waarvoor de drempels in april zijn herzien. Onder de huidige regels zou geen enkele april-ad gepauzeerd zijn (laagste Link CTR 1,0%, geen ad haalde de 500 link clicks voor de CPC-regel). Januari zou dat wél zijn, met 0,7% Link CTR, wat suggereert dat de 0,8% drempel niet te streng staat.

Verder viel op dat maart 9.703 link clicks kocht voor €0,14 met 0 purchases, terwijl april 1.036 clicks kocht voor €1,02 met 6 purchases. De maart-cijfers zien er op CTR beter uit, maar zijn niet het voorbeeld om naar terug te keren.

### Twee openstaande blockers

De purchase-waardes in Meta zijn intern tegenstrijdig (dezelfde 6 purchases als 44247 en als 4.42), en de overige eventwaardes ogen als vaste placeholders. ROAS is daardoor onbruikbaar als stuurmetric, wat ook betekent dat het ROAS-criterium in de 70-20-10 classificatie nu wegvalt.

Daarnaast klopt het command-bestand op twee punten niet: `act_607231713057715` is niet toegankelijk met dit token (wel `act_1489853856181844`, dat leeg is), en de MCP heet `pipeboard-meta-ads`.

Zal ik het command uit de scheduled morning report halen tot de heropstart, of er een wekelijkse check van maken?
