# Morning Report — 2026-07-17

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 17 juli 2026

> **Geen actieve campagnes** op de toegankelijke accounts. Hieronder de meest recente **gepauzeerde** campagnes met lifetime performance.
>
> Het in het command genoemde account `act_607231713057715` is niet toegankelijk met deze token. Het tweede gekoppelde account is `act_1489853856181844` (AmbitionAvenue) en heeft geen campagnes. Alle spend zit in het **Sempertex Ad Account** (`act_567892422940728`).

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Aankopen | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|----------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | — |

**Totaal spend:** €4.867,46

### Underperformers

- **2026: SYBB - Kopie** — CPC €0,64 (drempel €0,50) → testkopie met €124 spend, 0 aankopen (wel 6 initiate_checkouts). Klein volume vertekent CPC. Niet heractiveren zonder de winnende hooks.
- **2026: SYBB - Kopie** — CPM €16,34 (drempel €15,00) → dure reach op klein publiek. Breder publiek of bewezen SYBB-creatives gebruiken.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (drempel 1%) → laagste engagement, maar wel laagste CPC (€0,17) en CPM (€1,64) door 369k reach. Prima voor awareness, zwak voor directe respons.

_Geen campagnes boven frequency-drempel 3,5 (hoogste: 2,9)._

### Top performers

- **Beste CTR:** 2026: SYBB — 4,1%
- **Laagste CPC:** Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS:** 2026: SYBB — 17,8x

### Samenvatting

- **Beste performer:** **2026: SYBB** — enige campagne die schaal én rendement combineert (4,1% CTR, €0,21 CPC, 17,8x ROAS, meeste volume). Bewezen winnaar.
- **Slechtste performer:** **Last push Nozzle Up** — ROAS 0,8x (verlies): €800 spend, 3 aankopen voor €623.
- **Aanbeveling (70-20-10):** Heractiveer en schaal **2026: SYBB** (70% op deze bewezen hooks), 20% op creative-varianten, 10% experimenten. Laat de "Kopie" gepauzeerd tot er een concrete hypothese is. Nozzle Up-campagnes zijn seizoensgebonden (2025) en niet langer eerste keuze.

### Google Sheet
Overgeslagen op verzoek. Rapport opgeslagen in `Output/Reports/Daily/2026-07-17_ads_report.md`.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Twee opmerkingen: (1) ik heb géén Google-tools gebruikt en niet naar de Sheet geschreven, conform je regels. (2) De ROAS-cijfers zijn Meta's toegewezen purchase values (7-day click / 1-day view); de SYBB purchase value van €44.247 op 6 aankopen impliceert grote B2B-wholesaleorders — plausibel, maar verifieer tegen je werkelijke omzet voordat je hierop stuurt.

---

Klaar. Het rapport staat opgeslagen op `Output/Reports/Daily/2026-07-16_sybb_report.md` en is gecommit + gepusht.

## Wat het rapport laat zien

Twee harde bevindingen, en ik heb bewust **geen cijfers verzonnen**:

1. **Meta Ads (wel opgehaald, wel gelukt):** Campagne "2026: SYBB" (`120239435987290239`, account `act_567892422940728`) staat op **PAUSED**. Nul delivery gisteren, afgelopen 7 dagen én afgelopen 30 dagen: 0 spend, 0 impressions, 0 clicks. Er valt dus geen ad performance of variant analyse te maken.

2. **PostHog (niet gelukt):** De **PostHog MCP is niet verbonden** in deze sessie, dus er is geen landing page data voor startyourballoonbusiness.com opgehaald. Sectie 3 en de funnel zijn daarom gemarkeerd als "geen data".

## Belangrijk voor jou

- Zonder actieve ads en zonder PostHog is er geen funnel om te analyseren. De top acties in het rapport zijn: (1) beslis of SYBB bewust op pauze staat of per ongeluk, (2) herstel de PostHog connectie, (3) draai het rapport opnieuw op een dag met echte delivery.
- **PostHog moet geautoriseerd worden** om dit rapport in de toekomst volledig te maken. Dat kan alleen in een interactieve sessie via je claude.ai connector settings (of `/mcp`). Ik kan die OAuth-flow hier niet uitvoeren.

## Regel-naleving voor deze run
Alleen Meta Ads MCP en (poging tot) PostHog MCP gebruikt. **Geen** Google MCPs aangeroepen (Gmail, Calendar, Drive, Sheets, Docs, Slides). **Niet** naar de Google Sheet tracker geschreven. Output uitsluitend lokaal opgeslagen.

Wil je dat ik de campagne heractiveer, of laat je hem bewust op pauze staan?

---

Klaar. Rapport opgeslagen op `Output/Reports/Daily/2026-07-17_auto_optimize.md` en gepusht.

## Kort samengevat

**Er is niets geoptimaliseerd en niets gepauzeerd, want er zijn geen actieve ads.**

- **Primair account** (`act_567892422940728`): alle campagnes staan op **PAUSED**, inclusief de hoofdcampagne `2026: SYBB`. Last_3d insights op campagne- en accountniveau zijn leeg (0 spend, 0 impressions).
- **Tweede account** (`act_1489853856181844`): geen actieve campagnes.
- **`act_607231713057715`**: dit token heeft **geen toegang** tot dit account (toegestaan zijn alleen `act_1489853856181844` en `act_567892422940728`). Overgeslagen. Als dit account nog relevant is, moeten de token-permissies hersteld worden.

De kill-regels (Link CTR / CPC link) en de 70-20-10 classificatie zijn niet toegepast: er is geen live performance data. PostHog was niet nodig omdat er geen ad-traffic is om tegen af te zetten.

**De enige echte actie voor jou:** de `2026: SYBB` campagne staat sinds 19 april op PAUSED. Zolang die uit staat levert deze dagelijkse run niks op. Wil je SYBB heractiveren zodat de optimalisatie weer kan draaien? Zo niet, dan kunnen we de auto-optimize run tijdelijk stilzetten tot er weer een campagne live is.

Alleen de Meta Ads MCP is gebruikt, geen Google MCPs, en er is niet naar de Google Sheet tracker geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
