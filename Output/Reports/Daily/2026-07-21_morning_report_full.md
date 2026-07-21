# Morning Report — 2026-07-21

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 21 juli 2026

> **Geen actieve campagnes.** Beide accounts (Sempertex `act_567892422940728` en AmbitionAvenue `act_1489853856181844`) hebben niks op ACTIVE staan. Hieronder de **meest recente gepauzeerde campagnes** met hun laatste lifetime-data. AmbitionAvenue is een leeg account.

### Overzicht per campagne (gepauzeerd — gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Aankopen | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

\* **Datakwaliteit-flag:** SYBB rapporteert €44.247 aankoopwaarde op 6 orders (≈€7.374/order) — onwaarschijnlijk hoog, wijst op een verkeerd geconfigureerde pixel-waarde. Behandel die 17,8x als onbetrouwbaar.

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 (drempel €0,50) → mislukte kopie-test, €124 spend, 0 aankopen. Niet heropstarten; het origineel presteert overal beter.
- **2026: SYBB - Kopie** — CPM €16,34 (drempel €15) → dure reach op koude test.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (op de grens) → lage engagement, maar spotgoedkope reach (CPM €1,64). Puur awareness-opzet, zwakke hook voor conversie.

Geen enkele campagne >3,5 frequency (max 2,89) → geen fatigue-risico.

### Top performers
- **Beste CTR**: 2026: SYBB — 4,1%
- **Laagste CPC**: Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS (betrouwbaar)**: Campagne Nozzle Up 2025 1 — 8,3x

### Samenvatting
- **Totaal spend**: €4.867,46 (volledige historie van het account)
- **Beste performer**: **Campagne Nozzle Up 2025 1** — 8,3x ROAS met betrouwbare data, gezonde CTR/CPC.
- **Sterkste top-of-funnel**: **2026: SYBB** — 4,1% CTR, €0,21 CPC, 6.992 landing page views, 15 leads. Hook werkt; alleen de purchase-tracking is stuk.
- **Slechtste**: **2026: SYBB - Kopie** — 0 aankopen, hoogste CPC en CPM.
- **Aanbeveling (70-20-10)**: er draait nu niks. Zet de bewezen winnaar (70%) weer aan — de originele SYBB-set. **Repareer eerst de purchase-pixel**, anders is ROAS betekenisloos. 20% naar SYBB-hookvariaties, 10% experiment. Laat "- Kopie" los.

Rapport opgeslagen in `Output/Reports/Daily/2026-07-21_ads_report.md`. Google Sheet-write overgeslagen conform je instructie.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Ik kan die desgewenst ook uit de **PostHog MCP** halen (site startyourballoonbusiness.com) — zeg het maar, dan draai ik meteen een `/funnel-diagnose` over de SYBB-funnel.

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-07-20_sybb_report.md` en is gecommit + gepusht.

## Belangrijkste bevinding: de funnel staat stil

De data (uitsluitend via Meta Ads MCP en PostHog MCP, geen Google-bronnen) laat één duidelijk verhaal zien:

**Meta Ads "2026: SYBB" is PAUSED.** €0 besteed gisteren én de hele week (14 t/m 20 juli). Er komt geen betaald verkeer binnen. Dit is de oorzaak van alle nullen verderop.

**Landingspagina (www.startyourballoonbusiness.com), gisteren:**
- 6 pageviews / 6 sessies / 6 bezoekers, allemaal single-page → **100% bounce**
- 0 CTA clicks, 0 scroll-events, 0 conversies
- 100% direct verkeer, 0% UTM-getagd, waarvan **2 van de 6 bots** (Edge/CN); de andere 4 waren directe Chrome-bezoekers uit de US
- 7-daags totaal: slechts 17 pageviews (~2,4/dag), dus ruisniveau

## Top 3 acties
1. **Besluit over de campagne** (Rood/strategie): heractiveren in Meta Ads Manager (dagbudget €100 staat klaar) óf bewust vastleggen dat SYBB gepauzeerd blijft, zodat dit rapport niet elke ochtend leeg draait.
2. **UTM-tagging controleren** vóór heractivatie (nu 0% getagd).
3. **LP-tracking verifiëren**: er komen geen scroll-/CTA-events binnen in PostHog, en bot-verkeer vertekent bij dit lage volume.

Twee opmerkingen bij de betrouwbaarheid: scroll-depth en CTA-click events lijken momenteel niet te vuren op de pagina (staat als 🔴 "geen data" in het rapport), en door het minieme volume + bots zijn alle ratio's statistisch nietszeggend tot de campagne weer live is.

---

Klaar. Rapport opgeslagen op `Output/Reports/Daily/2026-07-21_auto_optimize.md` en gepusht naar GitHub.

## Uitkomst van deze run

**Geen automatische acties uitgevoerd — er zijn geen actieve Meta Ads campagnes.**

Wat ik vond (alleen via Meta Ads MCP / Pipeboard, geen Google MCPs, niets naar de Tracker Sheet):

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (primair) | ✅ | 0 — alle 5 campagnes PAUSED |
| `act_1489853856181844` | ✅ | 0 — geen campagnes |
| `act_607231713057715` | ❌ | Token heeft **geen toegang** tot dit account |

Twee dingen om te weten:

1. **De SYBB-campagne staat op PAUSED** (`120239435987290239`, daily budget €100,00). Zonder live ads zijn er geen kill-regel-checks (Link CTR < 0.8%, CPC link > €1.50), geen fatigue-signalen en geen 70-20-10 classificatie mogelijk. Zodra SYBB weer ≥24 uur draait, levert een volgende run de volledige analyse.
2. **`act_607231713057715` is niet bereikbaar** met de huidige Pipeboard-token. Toegestane accounts zijn `act_1489853856181844` en `act_567892422940728`. Als dat account echt gemonitord moet worden, moet de juiste Facebook-connection gekoppeld worden in Pipeboard.

Er zijn geen voorstellen die op goedkeuring wachten — laat weten wanneer SYBB weer live staat, dan draai ik de complete optimalisatie.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
