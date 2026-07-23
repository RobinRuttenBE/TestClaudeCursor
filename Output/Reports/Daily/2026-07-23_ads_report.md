## Meta Ads Rapport — 23 juli 2026

⚠️ **Er zijn geen actieve campagnes.** €0 spend in de laatste 30 dagen; alle campagnes staan op PAUSED. Conform de fallback-regel van `/ads-report` toon ik hieronder de meest recente gepauzeerde campagnes met hun **laatste bekende performance (lifetime data)**.

> *Accounts:* het in het command genoemde `act_607231713057715` is niet toegankelijk onder deze login. Beschikbaar zijn **Sempertex** (`act_567892422940728`) en **AmbitionAvenue** (`act_1489853856181844`, €0 spend, geen campagnes).

### Overzicht per campagne (gesorteerd op spend, lifetime)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Aankopen | ROAS* |
|----------|--------|-------|-------------|--------|-----|-----|-----|----------|-------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x* |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x* |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

*ROAS = purchase action_value ÷ spend. Frequency bij alle campagnes onder de drempel van 3,5 (hoogste: 2,89).

> **ROAS-waarschuwing:** de purchase-waarden ogen onbetrouwbaar. 2026: SYBB rapporteert €44.247 op 6 aankopen (~€7.374/order), Campagne Nozzle Up 2025 1 €7.081 op 6 aankopen (~€1.180/order). Dit wijst op een **verkeerd geconfigureerde pixel purchase-waarde**. Stuur op **aantal aankopen** en **CPA**, niet op ROAS, tot de pixel-waarde geverifieerd is.

### Underperformers

- **2026: SYBB - Kopie** — CPC €0,64 (drempel €0,50) én CPM €16,34 (drempel €15) → dure reach op mini-schaal (€124 spend), 0 aankopen. **Consolideer in de hoofdcampagne**, schrap de losse kopie (Hormozi 70-20-10).
- **Nozzle Up END OF AUGUST** — CTR 1,0% (drempel 1%) → grensgeval. Zeer lage CPM (€1,64) en CPC (€0,17) houden de campagne toch efficiënt; lage CTR duidt op brede reach-targeting. Creative refresh kan CTR tillen, economics zijn gezond.
- **Last push Nozzle Up** — geen drempel-flag, maar zwakste output: slechts 3 aankopen op €800 spend (CPA ~€267). Uitgeputte campagne.
- **2026: SYBB (hoofd)** — geen drempel-flags, maar **6 aankopen uit 12.067 clicks / 6.992 LP-views**: het echte knelpunt zit in de **funnel, niet de ads**.

### Top performers

- **Beste CTR:** 2026: SYBB — 4,1%
- **Laagste CPC:** Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS:** niet betrouwbaar te bepalen (zie waarschuwing); op aankoopvolume presteert 2026: SYBB het sterkst

### Samenvatting

- **Totaal spend (lifetime, alle campagnes):** €4.867,46 — 51% zit in de hoofdcampagne 2026: SYBB.
- **Beste performer:** **2026: SYBB** — goedkoop, hoog-engagement verkeer (4,1% CTR, €0,21 CPC, 68.615 video views, 80K post-engagements). De hooks en creatives werken.
- **Slechtste performer:** **2026: SYBB - Kopie** — duur, klein, 0 conversies.
- **Kern:** Het probleem zit in de **funnel, niet de ads**. Sterk en goedkoop verkeer converteert nauwelijks (6.992 LP-views → 6 aankopen op de hoofdcampagne).
- **Aanbeveling (Hormozi 70-20-10):** (1) bij heropstart **één bewezen campagne** — 2026: SYBB — met 70% budget, 20% op variaties van de winnende hooks, 10% experiment; geen losse kopie ernaast. (2) Fix de pixel purchase-waarde vóór heropstart. (3) Hoogste prioriteit = **landing page conversie**, niet meer ad-budget.

### Google Sheet
Overgeslagen conform run-instructie (stap 6). Rapport lokaal opgeslagen in `Output/Reports/Daily/2026-07-23_ads_report.md`.

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` — gezien 6.992 LP-views → 6 aankopen is dat hier de belangrijkste analyse.
