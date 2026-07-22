# Morning Report — 2026-07-22

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 22 juli 2026

> **Geen actieve campagnes.** Alle campagnes in de toegankelijke accounts staan op **PAUSED**. Cijfers hieronder zijn de laatst bekende **lifetime**-performance (in de laatste 30 dagen was er geen spend). Account `act_607231713057715` was niet toegankelijk met deze token; `act_1489853856181844` bevat geen campagnes.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

### Underperformers

- **2026: SYBB - Kopie** — CPC €0,64 (>€0,50) én CPM €16,34 (>€15) → test-kopie presteert op elk vlak slechter dan het origineel, nul purchases. Definitief intrekken.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (grens) → reach-opzet met goedkope CPM maar zwakke engagement; strakkere hook nodig voor conversie.
- **Last push Nozzle Up** — ROAS 0,8x (onder break-even) → uitgeputte end-of-cycle campagne, niet heractiveren.
- Geen campagne boven frequency-drempel 3,5 (hoogste: 2,89).

### Top performers

- **Beste CTR**: 2026: SYBB — 4,1%
- **Laagste CPC**: Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS**: 2026: SYBB — 17,8x (6 B2B-purchases, €44.247 purchase value)

### Samenvatting

- **Totaal spend**: €4.867,46 (lifetime, 5 gepauzeerde campagnes)
- **Beste performer**: **2026: SYBB** — bewezen winnaar op CTR, CPC, ROAS en engagementvolume.
- **Slechtste performer**: **2026: SYBB - Kopie** — dure CPC/CPM, nul purchases.
- **Aanbeveling (70-20-10)**: heractiveer 2026: SYBB als hoofdcampagne (70%), trek de kopie in, bouw 20% variaties op de winnende SYBB-creatives, 10% nieuwe experimenten. Nozzle Up is afgesloten cyclus — gebruik de learnings, bouw voort op SYBB.

**Rapport opgeslagen:** `Output/Reports/Daily/2026-07-22_ads_report.md`
**Google Sheet:** overgeslagen conform run-instructie (geen Google MCP-calls).

---

Een belangrijke kanttekening over de ROAS-cijfers: die van 2026: SYBB (17,8x) leunt op **6 purchases met een totale waarde van €44.247** — dat zijn enkele hoogwaardige B2B wholesale-orders. Bij zulke lage aantallen is één order het verschil tussen top en flop, dus behandel ROAS hier als richting, niet als hard getal.

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4. Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` over de gecombineerde data (Meta + landing page).

Wil je daarnaast dat ik de **actuele SYBB landing page health** uit PostHog haal (bounce rate, scroll depth, CTA clicks) om de heractivatie-beslissing te onderbouwen? Dat mag binnen de run-regels (PostHog MCP is toegestaan).

---

Klaar. Rapport gegenereerd, opgeslagen en gepusht: `Output/Reports/Daily/2026-07-21_sybb_report.md`.

## Belangrijkste bevindingen

De SYBB funnel stond gisteren stil, en de oorzaak is niet performance maar activatie:

**Meta Ads (Pipeboard MCP)**
- Campagne `2026: SYBB` (Sempertex Ad Account) staat op **PAUSED**. Nul spend, nul impressies, nul clicks, gisteren én de hele maand juli. Daardoor geen ad-variant data per `utm_content`.

**PostHog (`www.startyourballoonbusiness.com`)**
- Gisteren: **1 pageview, 1 bezoeker, 1 sessie**, 0s duur, directe bounce. 7d totaal: 17 pageviews (~2,4/dag). Cijfers zijn statistisch betekenisloos door het minieme volume.
- **Tracking gap:** de LP vuurt alleen `$pageview` en `$web_vitals`. Geen scroll-depth, CTA-click of booking events, dus scroll depth, CTA click rate en de funnel zijn niet meetbaar.

**Top 3 acties** in het rapport: (1) SYBB campagne activeren of bewust on-hold vastleggen, (2) basis-tracking (scroll + CTA events) live zetten op de LP, (3) de UTM-meetketen verifiëren vóór heractivatie.

## Twee dingen om te weten

1. **Strikte-regel nageleefd:** alleen Meta Ads MCP en PostHog MCP gebruikt. Geen enkele Google MCP aangeroepen, en niets naar de Google Sheet tracker geschreven. Output uitsluitend als lokale markdown.
2. **Meta-token** is beperkt tot twee accounts (`AmbitionAvenue` en `Sempertex Ad Account`); ik moest expliciet `account_ids` meegeven. De SYBB campagne zit in de Sempertex-account. Goed om te weten: verreweg het meeste PostHog-verkeer in dit project gaat naar `www.sempertexeurope.com` (23.100 pageviews/30d), niet naar de SYBB LP (61/30d).

---

## Auto-Optimize Rapport — 22 juli 2026

Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-22_auto_optimize.md` (gecommit + gepusht). Alleen Meta Ads MCP (Pipeboard) gebruikt, geen Google MCPs, niets naar de tracker sheet geschreven.

**Kernconclusie: er viel niets te optimaliseren.**

- **Geen actieve campagnes** op beide toegankelijke accounts. In `act_567892422940728` staan alle 5 campagnes op PAUSED — inclusief `2026: SYBB` (sinds 19 apr 2026, €100/dag budget). Account `act_1489853856181844` is leeg.
- **Geen spend** in de laatste 3 dagen → kill-regels (Link CTR < 0,8% / CPC link > €1,50) niet van toepassing, 70-20-10 classificatie niet mogelijk.
- **0 ads gepauzeerd.**

**Twee punten die je aandacht vragen:**

1. **`act_607231713057715`** (het "secundaire" account uit het command) is **niet toegankelijk** met de huidige API-token. Toegestane accounts zijn `act_1489853856181844` en `act_567892422940728`. Fix de token-permissies of haal dit account uit de command-config.
2. **SYBB staat op pauze.** Zolang er geen campagne actief is, levert deze command geen bruikbare output. Zeg het als SYBB weer live moet — dat activeren is een Niveau 2 actie die ik niet zonder jouw akkoord uitvoer.

Zodra er weer verkeer draait, geeft de volgende run een volledige performance-analyse.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
