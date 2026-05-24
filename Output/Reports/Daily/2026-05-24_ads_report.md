# Meta Ads Rapport, 2026-05-24

**Periode:** last_30d (geen data), aangevuld met laatste actieve periode per campagne
**Account:** Sempertex Ad Account (act_567892422940728)
**Status:** Geen actieve campagnes. Rapport toont 5 meest recente gepauzeerde campagnes.

> AmbitionAvenue (act_1489853856181844) bevat 0 campagnes en €0 lifetime spend. Niet meegenomen in analyse.

## Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. (purchase) | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|------------------|------|
| 2026: SYBB | Paused | €2.383,30 | 280.906 | 11.900 | 4,2% | €0,20 | €8,48 | 6 | 18,6x* |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0x |

*\* 2026: SYBB ROAS is opgeblazen door verkeerd geconfigureerde pixel value. Zie waarschuwing onderaan.*

### Aanvullende campagne details

| Campagne | Frequency | Reach | Landing Page Views | ATC | IC | Leads |
|----------|-----------|-------|--------------------|-----|----|----|
| 2026: SYBB | 2,2 | 125.654 | 6.992 | 53 | 36 | 15 |
| Campagne Nozzle Up 2025 1 | 2,9 | 44.774 | 1.733 | 65 | 329 | 0 |
| Last push Nozzle Up | 2,4 | 45.985 | 1.920 | 36 | 236 | 0 |
| Nozzle Up END OF AUGUST | 2,2 | 165.122 | 2.104 | 18 | 141 | 0 |
| 2026: SYBB - Kopie | 1,4 | 5.377 | 100 | 0 | 6 | 0 |

## Underperformers

- **2026: SYBB - Kopie**, CPC €0,64 (drempel €0,50). Aanbeveling: deze test draaide kort en is gestopt. Voor toekomstige relaunch eerst hook-test op bestaande winnaars uit de hoofdcampagne in plaats van nieuwe creatives.
- **2026: SYBB - Kopie**, CPM €16,34 (drempel €15). Aanbeveling: audience was te smal of creative te zwak. Bij hervatten: bredere prospecting audience en gevalideerde hook.
- **Nozzle Up END OF AUGUST**, CTR 1,0% (drempel 1%). Aanbeveling: ondergrens, ondanks zeer lage CPM (€1,64). Reach was groot maar engagement marginaal. Hook upgrade nodig voor relaunch.
- **Last push Nozzle Up**, ROAS 0,8x. Aanbeveling: laatste push leverde geen winst op, gebruik dit niet als basis voor herhaling. Kijk naar de eerdere Nozzle Up campagnes (8,3x en 6,4x ROAS) als template.

## Top performers

- **Beste CTR:** 2026: SYBB, 4,2%. Sterk boven Sempertex-target van >2%. Hooks en creatives zijn gevalideerd.
- **Laagste CPC:** Nozzle Up END OF AUGUST, €0,17. Maar gecombineerd met lage CTR (1,0%), dus dit was vooral goedkoop omdat de audience groot en koud was.
- **Beste betrouwbare ROAS:** Campagne Nozzle Up 2025 1, 8,3x (€7.081 op €853 spend, 6 purchases, AOV €1.180). Dit is de Nozzle Up campagne die als template gebruikt moet worden.

## Samenvatting

- **Totaal spend** (5 gepauzeerde campagnes): €4.765,72
- **Lifetime account spend:** €4.867,46
- **Beste performer:** Campagne Nozzle Up 2025 1, 8,3x ROAS met €7.081 omzet uit €853 spend. Hoogste AOV (€1.180), sterke ATC en checkout funnel.
- **Slechtste performer:** Last push Nozzle Up, 0,8x ROAS. Drie purchases voor €623 omzet, ondanks 1.920 landing page views. Funnel knelt aan de checkout-kant.
- **2026: SYBB campagne:** sterke front-of-funnel cijfers (4,2% CTR, €0,20 CPC, 6.992 LPVs, 36 IC, 15 leads) maar slechts 6 purchases. Conversie van LPV naar purchase is 0,09%. De ROAS van 18,6x is misleidend vanwege pixel value misconfiguratie (zie waarschuwing).

## Aanbeveling (Hormozi 70-20-10)

**70% (bewezen winnaars):** Bouw nieuwe campagne op het template van Campagne Nozzle Up 2025 1 (8,3x ROAS) en Nozzle Up END OF AUGUST (6,4x ROAS). Combineer de hoge engagement van SYBB-hooks met de Nozzle Up funnel-flow die wel converteert.

**20% (variaties):** Test SYBB-creatives met nieuwe checkout-flow. De LPV-to-purchase rate is te laag, het lek zit op de landing page of in de checkout, niet in de ads.

**10% (experimenten):** Eerst pixel value tracking fixen voordat nieuwe SYBB-campagnes live gaan, anders blijft ROAS-data onbetrouwbaar.

## Waarschuwing: pixel value tracking 2026: SYBB

De campagne 2026: SYBB rapporteert €44.247 purchase value voor 6 purchases, oftewel €7.374 per purchase. Complete_registration value is €86.100 voor 6 events (€14.350 per registratie). Dit zijn onrealistische waarden voor een SYBB workshop sale van max enkele honderden euro per ticket.

**Vermoedelijke oorzaak:** verkeerde value parameter in de Meta Pixel of conversie API. Dit moet gefixed worden voordat we ROAS-gebaseerde beslissingen nemen op SYBB campagnes.

**Actie:** check pixel implementatie op startyourballoonbusiness.com, met name de `value` parameter op Purchase en CompleteRegistration events.

## Output

- Rapport opgeslagen: `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-24_ads_report.md`
- Google Sheet update: **overgeslagen** (per command argument, geen Google MCP-aanroepen)

---

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit PostHog (kan ik nu ophalen via PostHog MCP) of GA4.

Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Of zeg "pak de PostHog data" en ik haal het direct op voor de SYBB landing page.
