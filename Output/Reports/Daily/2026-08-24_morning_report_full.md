# Morning Report — 2026-08-24

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 24 augustus 2026

**Belangrijkste conclusie: er draait al 4 maanden niets.** Geen actieve campagnes, €0,00 spend in de laatste 30 dagen. Het account staat stil sinds 20 april 2026. Hieronder de laatste performance van de 5 gepauzeerde campagnes.

De Pipeboard MCP meldde "requires authentication", maar via de directe HTTP route (zoals eerder gedocumenteerd) was alle data gewoon bereikbaar. Het account act_607231713057715 uit de command bestaat niet; alle data komt uit het Sempertex Ad Account.

### Overzicht (lifetime, gesorteerd op spend)

| Campagne | Spend | Impr. | Clicks | CTR | CPC | CPM | Purchases | ROAS |
|----------|-------|-------|--------|-----|-----|-----|-----------|------|
| 2026: SYBB | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

*\*Die 17,8x is niet te vertrouwen: de pixel rapporteert €44.247 omzet op 6 purchases, ofwel €7.374 per purchase. Vrijwel zeker een value misconfiguratie op de eventpagina's.*

### Underperformers

- **2026: SYBB - Kopie**: CPC €0,64 én CPM €16,34, beide boven de drempel, met 0 conversies. Niet heractiveren in deze vorm.
- **Last push Nozzle Up**: ROAS 0,8x, verlieslatend.
- **SYBB w/ Semp (BLACK)** (ad): €101,74 spend, CTR 1,0%, nul landing page views, nul purchases. Definitief uitzetten.
- Frequency zit nergens boven 3,5, dus geen creative fatigue flags.

### Top performers

- **Beste CTR en laagste CPC**: ad H13, B3, CTA5 in SYBB met 9,8% CTR en €0,07 CPC (4.063 landing page views, maar opvallend: 0 purchases in de hoofdadset, terwijl dezelfde combo in de tweede adset wel 2 purchases haalde)
- **Beste betrouwbare ROAS**: Campagne Nozzle Up 2025 1 met 8,3x
- **Proven converter**: ad H11, B3, CTA5 met 4 purchases (wel dure clicks: €0,67)

### Aanbeveling (70-20-10)

Herstart SYBB met 70% budget op bewezen winnaars (H11 als converter, H13/H15 als goedkoop verkeer), 20% variaties op die hooks, 10% experiment. Maar fix eerst twee dingen: de purchase value in de pixel (anders blijft ROAS onbruikbaar) en uitzoeken waarom H13 duizenden landing page views maar nul purchases gaf in de hoofdadset.

Het rapport staat in `Output/Reports/Daily/2026-08-24_ads_report.md` en is gecommit en gepusht (`9227578d`). De Google Sheet stap is overgeslagen conform je instructie; er zijn geen Google MCPs aangeroepen.

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.** Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik er een /funnel-diagnose overheen.

---

Het rapport staat in `Output/Reports/Daily/2026-08-23_sybb_report.md` en is gecommit en gepusht (commit 6fed0950). Alleen de Meta Ads MCP (via de directe Pipeboard JSON-RPC route) en de PostHog MCP zijn gebruikt, geen Google tools en geen Sheet-writes.

**TLDR: er valt niets te rapporteren over performance, want de campagne "2026: SYBB" staat al sinds 19 april op PAUSED.**

De belangrijkste bevindingen:

- **Meta Ads:** €0 spend, 0 impressies, 0 clicks op 23 augustus én in de 7 dagen ervoor. Ook de kopie-campagne "2026: SYBB - Kopie" staat op PAUSED.
- **Landing page:** startyourballoonbusiness.com kreeg gisteren precies 2 bezoeken (100% bounce, 0s sessieduur), tegenover 0 bezoeken in de hele week ervoor. Opvallend: die bezoeken hadden `utm_content=h11_b3_cta5` in de URL maar referrer `$direct`, dus iemand heropende een oude getagde ad-link. De UTM-tracking op de pagina werkt in elk geval nog.
- **Funnel en variantenanalyse:** overgeslagen in het rapport, met 2 sessies is dat ruis.

De echte rode vlag is structureel: de daily report flow draait alsof de campagne live is, terwijl er al ruim 4 maanden geen data is. Bovendien verkoopt SYBB inmiddels via de event pagina's op sempertexeurope.com (waar alle recente PostHog events zitten), niet via deze landing page. De top-actie in het rapport is dan ook een keuze maken: campagne hervatten, de skill ombouwen naar de event pagina funnel, of dit dagelijkse rapport pauzeren tot de campagne weer live gaat.

Praktische noot: de Pipeboard MCP servers meldden "requires authentication", de data is opgehaald via de bekende directe HTTP-workaround. Wil je de MCP tools zelf weer werkend hebben, dan moet je die connector opnieuw autoriseren via je claude.ai connector-instellingen of `/mcp` in een interactieve sessie.

---

De auto-optimize run is klaar. TLDR: **er valt niets te optimaliseren, alle campagnes staan uit.**

## Auto-Optimize Rapport, 24 augustus 2026

**Bevindingen:**
- Alle 5 campagnes in het Sempertex Ad Account (act_567892422940728) staan op PAUSED. De laatste, "2026: SYBB", is al op 19 april 2026 gepauzeerd.
- Account insights over de laatste 3 dagen bevestigen €0,00 spend, 0 impressions, 0 link clicks.
- Het tweede account uit het command (act_607231713057715) is niet toegankelijk met de token; alleen Sempertex en AmbitionAvenue (leeg) zijn toegestaan. Dit bevestigt de eerdere memory dat dit ID niet klopt.

**Acties:**
- ⚡ Niveau 1: 0 ads gepauzeerd, er zijn geen actieve ads.
- ⚠️ Waarschuwingen: geen, zonder delivery valt er niets te meten.
- 📊 70-20-10: niet van toepassing.

**Voorstellen (wachten op jouw goedkeuring):**
1. **SYBB herstart beslissing.** De campagne staat 4+ maanden stil. Bij herstart richting najaar: creatives verversen, UTM's valideren, en klein beginnen conform de 10% experimental regel.
2. **Account opschonen.** De duplicaat "2026: SYBB - Kopie" (nooit substantieel gedraaid) archiveren of verwijderen.

Rapport opgeslagen in `Output/Reports/Daily/2026-08-24_auto_optimize.md` en gepusht naar GitHub (commit 3407eb00). Alleen Meta Ads via Pipeboard gebruikt (directe HTTP, want de MCP meldde weer "requires authentication"); geen Google MCPs aangeroepen en niets naar de Google Sheet geschreven, zoals gevraagd.

Wil je dat ik een van de twee voorstellen uitvoer? Geef het nummer aan.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
