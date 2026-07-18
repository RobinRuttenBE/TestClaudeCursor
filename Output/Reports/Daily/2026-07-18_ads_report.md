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
