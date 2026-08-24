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
