# Morning Report — 2026-07-18

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Klaar. Hier het rapport.

## Meta Ads Rapport — 18 juli 2026

> **Er zijn momenteel GEEN actieve campagnes.** Alles in het Sempertex Ad Account (`act_567892422940728`) staat op PAUSED. Het tweede command-account (`act_607231713057715`) is niet toegankelijk met deze token; het extra toegankelijke account (`act_1489853856181844`) heeft geen actieve campagnes. Onderstaande cijfers zijn **laatst bekende lifetime-performance** van de recentste gepauzeerde campagnes (elk over eigen looptijd, niet 1-op-1 vergelijkbaar).

### Overzicht per campagne (gepauzeerd, lifetime)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x ⚠️ |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

⚠️ **ROAS SYBB is pixel-vertekend:** €44.247 op 6 aankopen = €7.374/aankoop → verkeerd geconfigureerde pixel-waarde, geen echte omzet. Behandel 17,8x als onbetrouwbaar.

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 (>€0,50) én CPM €16,34 (>€15), 0 aankopen op €124. Te dunne test → niet los heropstarten.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (op de drempel) ondanks spotgoedkope CPM (€1,64). Hook herzien.
- Geen enkele campagne over de frequency-drempel (max 2,39).

### Top performers
- **Beste CTR**: 2026: SYBB — 4,1%
- **Laagste CPC**: Nozzle Up END OF AUGUST — €0,17
- **Beste (betrouwbare) ROAS**: Nozzle Up END OF AUGUST — 6,4x

### Samenvatting
- **Totaal spend** (4 campagnes, lifetime, niet-overlappend): **€4.014,27**
- **Sterkste fundament**: 2026: SYBB (hoogste CTR + laagste CPC-tier) → 70-20-10 op deze bewezen hooks bij heropstart.
- **Zwakste**: 2026: SYBB - Kopie (dure test, 0 conversies).
- **Eerste actie**: fix de tracking — de SYBB purchase/registration-waarden kloppen niet, dus op ROAS sturen kan nog niet. Draai `/tracking-check`.

### Google Sheet
Overgeslagen conform instructie (stap 6). Alleen lokaal opgeslagen: `Output/Reports/Daily/2026-07-18_ads_report.md`. Gecommit en gepusht. Geen Google MCPs gebruikt.

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` erover.

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-07-17_sybb_report.md` en is gecommit + gepusht.

## Wat er uit de data kwam

**Meta Ads (via Pipeboard MCP)**
- Campagne **"2026: SYBB"** (`120239435987290239`) stond gisteren de hele dag op **PAUSED**.
- **Nul** impressies, clicks en spend op 17 juli — én over het hele 7-daagse venster (11–17 juli).
- Laatste echte delivery was **19–30 april 2026** (2.756 impressies, 61 clicks, €43,81, CTR 2,21%, CPC €0,72). Puur historisch.

**PostHog**
- ⚠️ De **PostHog MCP is niet verbonden** in deze sessie. De beschikbare servers zijn Canva, Gmail, Calendar, Drive, Granola, Wix, ga4, google, imessage, instagram, lottiefiles en pipeboard-meta-ads — geen PostHog. De landing page kant (bounce, scroll, CTA, funnel) kon dus **niet** worden opgehaald. Dit heb ik expliciet als rode vlag in het rapport gezet, niet als nul verzonnen.

Ik heb me strikt aan je regel gehouden: alleen Meta Ads MCP gebruikt, geen enkele Google MCP, en niets naar de Google Sheet tracker geschreven.

## Twee dingen die je aandacht vragen
1. **De SYBB campagne draait niet meer** sinds ~1 mei. Er staat €100/dag gereserveerd dat niets doet — beslissing nodig of je reactiveert of de focus verlegt.
2. **PostHog moet gekoppeld worden** wil dit dagrapport zijn kernfunctie (de cross-reference tussen ads en landingspagina) kunnen doen. Dat kun je in een interactieve sessie via `/mcp` of `claude mcp` regelen.

Zolang de campagne bewust uit staat, kan het overwegen waard zijn dit dagrapport op een "wake on activity"-trigger te zetten in plaats van elke ochtend, om lege rapporten te voorkomen.

---

Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-18_auto_optimize.md`, gecommit en gepusht.

## Samenvatting

**Geen optimalisaties uitgevoerd — er zijn geen actieve campagnes.**

Wat ik gecheckt heb (alleen Meta Ads MCP, geen Google MCPs, niets naar de Google Sheet geschreven):

- **`act_567892422940728`** (primair) → 0 actieve campagnes. Alle 5 campagnes staan PAUSED, inclusief `2026: SYBB` (dagbudget €100,00, laatst gewijzigd 19 April 2026) en de kopie ervan.
- **`act_1489853856181844`** (token-toegestaan) → geen campagnes.
- **`act_607231713057715`** (in command genoemd) → **niet toegankelijk** met deze API-token. Toegestane accounts zijn alleen `act_1489853856181844` en `act_567892422940728`.

**Resultaat:** 0 ads gepauzeerd, geen waarschuwingen, geen 70-20-10 classificatie mogelijk, 0 voorstellen. De kill-regels en budget-logica hebben geen delivery om op te werken.

**Enige relevante actie voor jou:** de SYBB-campagne staat gepauzeerd. Wil je die opnieuw activeren? Zodra er ≥ 24 uur delivery is, draait dit command automatisch de kill-regels en classificatie.

Eén ding om te weten: het account `act_607231713057715` uit het command is niet bereikbaar met de huidige token — als daar wél live campagnes draaien, moet de token-toegang eerst geregeld worden voordat ik dat kan meenemen.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
