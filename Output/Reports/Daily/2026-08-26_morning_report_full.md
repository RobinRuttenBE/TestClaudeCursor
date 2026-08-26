# Morning Report — 2026-08-26

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 26 augustus 2026

**TLDR: er draait momenteel niets.** Alle 5 campagnes in het Sempertex Ad Account staan op PAUSED en de spend van de laatste 30 dagen is €0,00. De laatste activiteit was de SYBB campagne, gepauzeerd rond 19-20 april. Hieronder de lifetime performance van de gepauzeerde campagnes. Het rapport staat in `Output/Reports/Daily/2026-08-26_ads_report.md` en is gecommit en gepusht.

Vooraf twee praktische punten. De Pipeboard MCP meldde "requires authentication", dus ik heb de data via de directe HTTP route opgehaald (werkt prima). En het account act_607231713057715 uit de command bestaat niet in deze connectie; er zijn alleen het Sempertex account en het lege AmbitionAvenue account.

### Overzicht per campagne (lifetime, op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0x |

\* **Belangrijke datavondst:** de pixel rapporteert €44.247 omzet op 6 SYBB purchases, dus €7.374 per ticket. De initiate checkout waarde is consistent €350 per stuk, wat klopt met de workshopprijs. De purchase value in de pixel lijkt dus verkeerd geconfigureerd. Op basis van €350 per ticket is de reële SYBB ROAS eerder 0,8x dan 17,8x. Dit eerst fixen voordat je op ROAS stuurt.

### Underperformers

- **2026: SYBB - Kopie** heeft CPC €0,64 en CPM €16,34, beide boven drempel, met 0 purchases. Niet heractiveren, het origineel presteert overal beter.
- **SYBB w/ Semp (BLACK)** verbrandde €101,74 zonder één LP view of conversie, met CTR op de 1% drempel. Zwakste ad in het account, killen.
- **H13 in de Kopie campagne** zat op CPC €0,93 en CPM €19,14.
- Frequency was nergens een probleem, alles onder 3,5.

### Top performers

- **Beste CTR**: H13, B3, CTA5 (batch 1) met 9,8% en CPC €0,07, goed voor 4.063 landing page views maar 0 purchases. Een click magnet, geen koper-ad.
- **Beste converter**: H11, B3, CTA5 (batch 2) met 4 van de 6 SYBB purchases en 23 initiate checkouts, ondanks CPC €0,67.
- **Beste betrouwbare ROAS**: Campagne Nozzle Up 2025 1 met 8,3x.

### Aanbeveling (70-20-10)

Het account staat al ruim 4 maanden stil. Bij een SYBB herstart: 70% budget op de bewezen winnaar H11/B3/CTA5, 20% op varianten daarvan plus H13 batch 2 (de enige andere ad met purchases), 10% op nieuwe hooks. H13 batch 1 alleen bovenin de funnel inzetten voor goedkoop bereik. En omdat SYBB inmiddels via de event pagina's op sempertexeurope.com verkoopt: eerst pixel value en UTM's daarop aansluiten, anders blijft de meting kapot.

De Google Sheet stap heb ik volledig overgeslagen zoals gevraagd, en PostHog heb ik niet aangeroepen omdat er geen ad traffic in de periode was.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik er een /funnel-diagnose overheen.

---

Het rapport staat in `Output/Reports/Daily/2026-08-25_sybb_report.md` en is gecommit en gepusht (commit 78598f08). De kern: **er was gisteren geen SYBB-activiteit aan beide kanten van de funnel.**

**Meta Ads:** de campagne "2026: SYBB" staat sinds 19 april op PAUSED. Een insights-call op de campagne én op accountniveau voor 25 augustus gaf een lege dataset terug, dus nul spend, nul impressies, nul clicks. De Pipeboard MCP zelf was niet geauthenticeerd in deze sessie; ik heb de bekende workaround met directe JSON-RPC calls gebruikt, die werkte gewoon.

**PostHog:** startyourballoonbusiness.com had gisteren 0 bezoekers en over de hele afgelopen week slechts 2 (beiden 100% bounce, 0s sessieduur). Het enige domein dat nog pageviews stuurt is www.sempertexeurope.com. Er bestaan bovendien geen scroll depth- of CTA click-events in het project, en geen utm_campaign property met recente waarden.

Daardoor zijn de secties Ad Variant Performance en Funnel Drop-off in het rapport leeg gelaten (geen data om te rapporteren). In plaats van performance-vlaggen heb ik twee structurele rode vlaggen opgenomen:

1. De skill meet het verkeerde domein: SYBB verkoopt via de event-pagina's op sempertexeurope.com, terwijl het rapport naar de oude, dode landing page kijkt.
2. Er is geen on-page tracking (scroll/CTA events) klaar voor als de ads weer live gaan.

De top 3 acties in het rapport sluiten daarop aan: beslissen over herstart van de campagne (en de bestemming), de daily-sybb-report skill updaten naar de werkelijke funnel, en tracking op de event-pagina's inrichten. Zoals gevraagd zijn er geen Google MCPs aangeraakt en is er niets naar de tracker-sheet geschreven.

---

De auto-optimize run is klaar: **geen acties uitgevoerd, want er draait momenteel niets in het ad account.**

Wat ik heb gecontroleerd via Pipeboard (directe HTTP calls, de MCP zelf meldt onterecht "requires authentication"):

- **0 actieve campagnes** op act_567892422940728. Alle 5 campagnes staan op PAUSED, inclusief "2026: SYBB" (sinds 19 april, dagbudget €100,00) en de drie Nozzle Up campagnes uit 2025.
- **€0,00 spend en 0 impressions** in de afgelopen 3 dagen op account-niveau, dus geen data voor kill-regels, waarschuwingen of 70-20-10 classificatie.
- Het tweede account uit het command (act_607231713057715) bestaat niet binnen deze token, dat bevestigt wat al in memory stond. Alleen het Sempertex account bevat data.

Er waren dus geen Niveau 1 acties (niets om te pauzeren). Als Niveau 2 punten om later over te beslissen: de SYBB campagne heractiveren vraagt om een verse creative-batch (creatives zijn ruim 4 maanden oud), en de afgeronde Nozzle Up campagnes zouden gearchiveerd kunnen worden voor schonere rapportages.

Rapport opgeslagen in `Output/Reports/Daily/2026-08-26_auto_optimize.md` en gepusht naar GitHub (commit `f57bbc41`). Geen Google services aangeroepen, niets naar de Tracker Sheet geschreven, conform de run-regels.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
