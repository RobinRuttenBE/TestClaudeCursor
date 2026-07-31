# Morning Report — 2026-07-31

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Gecommit en gepusht (`186b41c2`).

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**

Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Twee kanttekeningen daarbij: omdat er nul spend was in de laatste 30 dagen, is een funnel diagnose alleen zinvol over de periode dat SYBB wél liep (januari tot april 2026). En als je liever de PostHog data gebruikt in plaats van Wix of GA4, kan ik die zelf ophalen. De PostHog MCP staat binnen de regels van deze run.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-07-30_sybb_report.md`, gecommit en gepusht.

**Kort de uitkomst:**

**Meta Ads** — campagne `2026: SYBB` (`120239435987290239`) staat op PAUSED en had op 30 juli nul delivery. Ook het hele venster 24 t/m 30 juli en het volledige account over juli: nul spend. Laatste delivery was april 2026 (€1.059,47 / 91.839 impressies / CTR 2,11% / CPC €0,55). Lifetime staat de campagne op CTR 4,06% en CPC €0,21, dus april was een duidelijke verslechtering vlak vóór de pauze. Klassieke creative fatigue. Ik heb de ad-level aprildata meegenomen als referentie voor een eventuele herstart: H11 slokte 49% van het budget op tegen de op een na slechtste CPC (€0,67), H12 presteerde het best.

**PostHog** — landing page had gisteren 0 pageviews en 0 sessies. De trend over drie weken: 18 → 14 → 2 pageviews. Bounce 100% in het 7d venster, 95,7% over heel juli.

**Twee dingen die je moet weten:**

1. De `read-data-schema` taxonomie gaf aanvankelijk alleen `www.sempertexeurope.com` terug als host, wat suggereerde dat de SYBB landing page helemaal niet getrackt werd. Dat klopte niet. Een directe SQL-query over de events tabel liet zien dat `www.startyourballoonbusiness.com` wel degelijk data heeft. Alle landing page cijfers in het rapport komen uit die directe query.

2. De landing page tracking is onvolledig. Er bestaan geen scroll depth events en geen CTA click event op die host, alleen `$pageview`, `$web_vitals`, `$autocapture` en `$pageleave` (die laatste vuurt bijna nooit: 3 events in een maand). Vier van de zeven KPI-rijen uit de skill zijn daardoor structureel niet berekenbaar, ook niet als de campagne morgen weer aan gaat. Ik heb ze als "niet gemeten" gemarkeerd in plaats van ze te schatten. Ook: de conversiestap heet `/checkout`, niet `/booking` zoals de skill aanneemt, en de UTM tags staan als `META` / `SYBB` / `H14,B3,CTA5` in plaats van lowercase met underscores, wat de koppeling met de Ads Tracker breekt.

Alleen Meta Ads MCP en PostHog MCP gebruikt, geen Google diensten, niets naar de Google Sheet geschreven.

---

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

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
