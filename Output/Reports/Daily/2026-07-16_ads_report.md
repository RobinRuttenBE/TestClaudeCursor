# Meta Ads Rapport — 16 juli 2026

> **Let op:** Er zijn **geen actieve campagnes** in het Sempertex Ad Account (`act_567892422940728`). Alle campagnes staan op PAUSED. Hieronder de twee meest recente campagnes (SYBB 2026) met hun laatst bekende performance. Omdat de campagnes gepauzeerd zijn, gaven de `last_30d` metrics geen data terug — daarom is **lifetime** data gebruikt (periode per campagne aangegeven).
>
> Het tweede account uit de command (`act_607231713057715`, Robin Rutten) is **niet toegankelijk** met dit token. Beschikbare accounts: `act_567892422940728` (Sempertex) en `act_1489853856181844` (AmbitionAvenue, €0 spend, geen campagnes).

## Overzicht per campagne (lifetime, gepauzeerd)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. (aankopen) | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|------|------|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 0,18x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,00x |

- **2026: SYBB** — periode 13 jan – 16 jul 2026. Reach 132.674, frequency 2,24. Aankopen: 6 (waarde €442,47). Leads: 15. Add to cart: 53. Initiate checkout: 36. Landing page views: 6.992.
- **2026: SYBB - Kopie** — periode 19 apr – 16 jul 2026. Reach 5.377, frequency 1,42. Aankopen: 0. Initiate checkout: 6 (waarde €21,00).

## Underperformers

Op campagne-niveau (drempels: CPC €0,50 · CTR 1% · Frequency 3,5 · CPM €15):

- **2026: SYBB - Kopie** — CPC €0,64 (drempel €0,50) → **te duur**. Aanbeveling: deze kopie presteert op alle vlakken slechter dan het origineel (hogere CPC, lagere CTR, geen aankopen). Niet heractiveren; leer van het origineel.
- **2026: SYBB - Kopie** — CPM €16,34 (drempel €15) → **dure reach**. Aanbeveling: kleine reach (5.377) met dure CPM wijst op zwakke targeting/creative match. Laten vallen.
- **Beide campagnes** — ROAS 0,18x en 0,00x. De hoofd-SYBB campagne genereerde uitstekende engagement maar slechts 6 aankopen op €2.485 spend. **De bottleneck zit ná de klik** (landing page → checkout), niet in de ads zelf.

Op ad-niveau (hoofdcampagne 2026: SYBB), CPC boven €0,50:

- **H11, B3, CTA5** — CPC €0,67, hoogste spend (€521,56), CPM €13,51 → duurste ad, laagste efficiency van de top-spenders.
- **H13, B3, CTA5** (variant) — CPC €0,63, CPM €12,35 → dure variant naast een veel goedkopere naamgenoot.
- **SYBB w/ Semp (BLACK)** — CPC €0,61 én CTR 1,03% (net boven drempel) → zwakste hook van het lot, laagste engagement.

## Top performers

- **Beste CTR**: `H13, B3, CTA5` — **9,8%** (ad-niveau, hoofdcampagne). Absolute winnaar.
- **Laagste CPC**: `H13, B3, CTA5` — **€0,07** (zelfde ad). Bewezen hook + creative combinatie.
- **Beste ROAS**: `2026: SYBB` (hoofdcampagne) — 0,18x. Absoluut gezien zwak, maar de enige campagne met aankopen (6 × €442,47 totaal).

## Samenvatting

- **Totaal spend**: €2.609,46 (lifetime van beide SYBB-campagnes; geen actieve spend in de laatste 30 dagen)
- **Beste performer**: **Hook 13 (H13, B3, CTA5)** — CTR 9,8% en CPC €0,07. Dit is een 70-regel winnaar: het bewijst dat hook 13 de aandacht pakt tegen minimale kosten.
- **Slechtste performer**: **2026: SYBB - Kopie** — hogere CPC (€0,64), dure CPM (€16,34), lage CTR (2,6%) en nul aankopen. De duplicatie voegde niets toe.
- **Aanbeveling (Hormozi 70-20-10)**:
  1. **70% — schaal de winnaar**: bouw de volgende SYBB-flight rond **H13** (bewezen CTR/CPC). Zet hem als anker-hook in.
  2. **20% — variaties**: maak varianten op H13 en H15 (€0,15 CPC, 4,3% CTR — de tweede sterkste). Test nieuwe body/CTA-combinaties op deze twee bewezen hooks.
  3. **10% — experiment**: één nieuwe hook-richting. Laat H11 en de "BLACK"-creative vallen (te duur, zwakke engagement).
  4. **Prioriteit boven ads**: de echte lek zit in de funnel ná de klik — 12.067 clicks → 6.992 landing page views → 53 add to cart → 6 aankopen. Voordat je opnieuw budget inzet, eerst de landing page conversie fixen (PostHog-analyse). Ads leveren clicks; de pagina converteert niet.

## Google Sheet
Overgeslagen op verzoek (stap 6 niet uitgevoerd). Rapport lokaal opgeslagen in `Output/Reports/Daily/2026-07-16_ads_report.md`.
