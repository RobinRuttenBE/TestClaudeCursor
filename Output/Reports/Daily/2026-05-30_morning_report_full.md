# Morning Report — 2026-05-30

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport klaar en opgeslagen in `Output/Reports/Daily/2026-05-30_ads_report.md` (lokaal, geen Google Sheet write zoals gevraagd).

## Meta Ads Rapport — 30 May 2026

**Twee zaken vooraf:**
1. **Geen actieve campagnes.** Alle 5 campagnes in het Sempertex account staan op PAUSED, en `last_30d` is daardoor overal leeg. Ik toon hieronder de **lifetime** cijfers van de gepauzeerde campagnes.
2. **`act_607231713057715` (Robin Rutten) is niet toegankelijk** met dit token. Alleen AmbitionAvenue (€0, geen campagnes) en het Sempertex account waren bereikbaar.

### Overzicht per campagne (lifetime, op spend)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Aankopen | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|------|------|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | PAUSED | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | PAUSED | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | PAUSED | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.b. |

\* SYBB purchase-waarde €44.247 op 6 aankopen (gem. €7.374/order) is vrijwel zeker testdata/vervuild. Behandel die 17,8x als onbetrouwbaar. **Totaal spend: €4.867,46** (klopt exact met het account amount_spent).

### Underperformers
- **2026: SYBB - Kopie** → CPC €0,64 (>€0,50) én CPM €16,34 (>€15), 0 aankopen. Niet zo heractiveren; herzien of archiveren.
- **Nozzle Up END OF AUGUST** → CTR 1,0% (net op de 1%-grens), maar compenseert met CPC €0,17 en CPM €1,64. Geen actie nodig.
- **Last push Nozzle Up** → geen drempeloverschrijding, maar ROAS 0,8x (onder break-even). Niet herhalen zonder aanpassing.
- Geen frequency-issue (max 2,89).

### Top performers
- **Beste CTR:** 2026: SYBB — 4,1%
- **Laagste CPC:** Nozzle Up END OF AUGUST — €0,17
- **Beste betrouwbare ROAS:** Campagne Nozzle Up 2025 1 — 8,3x

### Aanbeveling (70-20-10)
Bij heractivatie: 70% bewezen budget op de Nozzle Up winnaar (Campagne 2025 1, 8,3x) en op "2026: SYBB" voor goedkoop top-of-funnel verkeer. "SYBB - Kopie" alleen als bewuste variatie (20%), niet als kopie. **Fix eerst de SYBB purchase-tracking** — die €44k waarde maakt ROAS-sturing op die campagne blind.

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik er automatisch een `/funnel-diagnose` op (tabel, #1 bottleneck, 3 actiepunten, SYBB-vergelijking).

---

Klaar. Het SYBB rapport voor 29 mei 2026 staat in `Output/Reports/Daily/2026-05-29_sybb_report.md` en is gecommit + gepusht.

## Belangrijkste bevinding
**Er valt niets te optimaliseren, want de funnel staat stil.** Beide databronnen wijzen dezelfde kant op:

- **Meta Ads (Pipeboard):** Campagne `2026: SYBB` staat op **PAUSED sinds 19 april 2026**. Geen spend, impressies of clicks op 29 mei, en ook niet in de hele 7-daagse vergelijkingsperiode (22-28 mei). Laatste echte levering was de week van 19-25 april.
- **PostHog:** Landing page kreeg gisteren **0 pageviews**, en over de afgelopen 7 dagen samen slechts 9. Geen instroom betekent geen bounce-, scroll-, CTA- of funneldata.

## Twee zaken die ik tegenkwam en doorgaf in het rapport
1. **De campagne is bewust of per ongeluk uit** — dit is de hoofdoorzaak van alle nullen. Eerste actie: beslissen of hij weer aan gaat (🟡 vraagt jouw budget-akkoord).
2. **Tracking-gat:** de landing page tracket in PostHog alleen `$pageview`, er zijn **geen scroll-depth of CTA-click events**. Zelfs als het verkeer terugkomt, blijven die rijen van het rapport leeg tot dit is opgelost (🟠 Wix Editor).

## Wat ik gerespecteerd heb
- Alleen Meta Ads MCP en PostHog MCP gebruikt. Geen enkele Google MCP, geen schrijven naar de Tracker Google Sheet. Output uitsluitend lokaal opgeslagen.
- Geen em/en dashes in de content, conform je voorkeur.

Wil je dat ik help met het reactiveren van de campagne of het opzetten van de scroll/CTA-tracking?

---

Klaar. Hier is wat er gebeurde:

## Auto-Optimize — 30 mei 2026

**Er draaien geen actieve Meta Ads campagnes**, dus er is niets te optimaliseren. De run is correct gestopt na de data-check.

**Bevindingen:**
- **`act_567892422940728` (Sempertex, primair):** 0 actieve campagnes. Alles staat op PAUSED, inclusief `2026: SYBB` (dagbudget €100,00, gepauzeerd sinds 19 april). Dit klopt met het SYBB dagrapport van 29 mei ("campaign paused, no LP traffic").
- **`act_607231713057715` (secundair, uit het command):** **niet toegankelijk** met de huidige token. De token kent alleen `act_567892422940728` en `act_1489853856181844`. → Het account-ID in het command lijkt verouderd, het melden waard.
- **`act_1489853856181844` (extra toegankelijk):** ook 0 actieve campagnes.

**Acties:**
- ⚡ Niveau 1 (automatisch pauzeren): **0 ads** — geen actieve ads om tegen de kill-regels te toetsen.
- 💡 Niveau 2 (voorstellen): geen data-gedreven voorstellen mogelijk zonder live performance. Enig operationeel signaal: als SYBB weer moet draaien, moet jij de campagne reactiveren.

Alleen de Meta Ads MCP is gebruikt; geen Google MCPs, geen schrijfacties naar de tracker-sheet. Rapport opgeslagen op `Output/Reports/Daily/2026-05-30_auto_optimize.md` en gecommit + gepusht.

Twee dingen om over te beslissen:
1. Wil je `2026: SYBB` heractiveren? Draai dit command dan opnieuw zodra de campagne ≥24 uur live is.
2. Klopt het secundaire account-ID in het command nog? Mogelijk moet `act_607231713057715` vervangen worden door `act_1489853856181844`.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
