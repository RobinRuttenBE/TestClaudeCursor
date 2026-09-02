Rapport is opgeslagen in `Output/Reports/Daily/2026-09-02_ads_report.md` en gecommit/gepusht (4702c793). Geen Google MCPs aangeroepen, geen Sheet geschreven.

## Meta Ads Rapport, 2 september 2026

**Periode:** last 30d, maar beide actieve campagnes draaien pas sinds 27/28 augustus, dus feitelijk 5 à 6 dagen data. De Pipeboard MCP meldde "requires authentication"; de data is via de directe JSON-RPC call opgehaald. Het account act_607231713057715 uit het command bestaat niet.

### Overzicht per campagne

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Leads | CPL |
|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Active | €390,33 | 57.230 | 1.149 | 2,0% | €0,34 | €6,82 | 3,58 | 11 | €35,48 |
| Wholesaler (SWE) | Active | €343,29 | 25.060 | 845 | 3,4% | €0,41 | €13,70 | 3,03 | 5 | €68,66 |
| **Totaal** | | **€733,62** | **82.290** | **1.994** | **2,4%** | **€0,37** | **€8,92** | | **16** | **€45,85** |

ROAS is niet van toepassing, het zijn lead-campagnes. Setup: 4 ad sets per campagne, elk €20/dag.

### Underperformers

- **Video 2 (SWE)**: CPC €0,72 en CPM €17,90, 0 leads na €81,76. Pauzeren.
- **Video 1 (SWE)**: CPM €15,88, 0 leads na €88,37. Tot 4 september geven, dan pauzeren als het zo blijft.
- **Video 2 (LIT)**: CPC €0,52, maar laagste CPL van LIT (€24,97). Laten draaien.
- **Campagne LIT**: frequency 3,58 na 6 dagen, kleine doelgroep (reach 15.995). Nieuwe creatives binnen een week.
- **Statisch 1 (LIT)**: CTR 1,2%, net boven de drempel. Monitoren.

### Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,2%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Laagste CPL**: Statisch 2 (SWE), €21,91 (4 van de 5 Zweedse leads)

### Grootste bevinding: funnel-lek

Slechts 22,7% (SWE) en 13,5% (LIT) van de link clicks wordt een landing page view. Meer dan driekwart van de betaalde klikken komt niet geregistreerd aan. Dat wijst op laadsnelheid, pixelplaatsing of onbedoelde tikken op mobiel. Dit weegt zwaarder dan elk verschil tussen ads.

### Aanbeveling (70-20-10)

1. **70% naar winnaars**: Statisch 2 (SWE) van €20 naar €35/dag, Statisch 2 (LIT) naar €30/dag.
2. **Pauzeer Video 2 (SWE)** vandaag; Video 1 (SWE) krijgt tot 4 september.
3. **20% variaties**: 2 nieuwe statische varianten op de Statisch 2 hook voor Litouwen, vóór de frequency de 4 passeert.
4. **Fix de LPV-lek**: mobiele laadsnelheid en pixel van de wholesaler-landingspagina checken.

SYBB en Nozzle Up staan gepauzeerd zonder spend in de afgelopen 30 dagen.

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik een `/funnel-diagnose` op de gecombineerde data.
