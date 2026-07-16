## Meta Ads Rapport — 16 juli 2026

⚠️ **Geen actieve campagnes.** Alles in het Sempertex account (`act_567892422940728`) staat op PAUSED. `last_30d` gaf geen data, dus hieronder de **lifetime** performance van de twee meest recente campagnes. Het tweede account (`act_607231713057715`) is niet toegankelijk met dit token.

### Overzicht per campagne (lifetime, gepauzeerd)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Aankopen | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|------|------|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 0,18x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,00x |

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 (>€0,50) én CPM €16,34 (>€15), nul aankopen → duplicatie voegde niets toe, niet heractiveren.
- **Ad H11, B3, CTA5** — CPC €0,67, duurste ad (€521 spend), zwakste efficiency van de top-spenders.
- **SYBB w/ Semp (BLACK)** — CPC €0,61 + CTR 1,03% → zwakste hook.
- **Beide campagnes ROAS <0,2x** — de lek zit ná de klik (12.067 clicks → 6.992 LP views → 53 ATC → 6 aankopen).

### Top performers
- **Beste CTR**: `H13, B3, CTA5` — **9,8%**
- **Laagste CPC**: `H13, B3, CTA5` — **€0,07**
- **Beste ROAS**: hoofdcampagne `2026: SYBB` — 0,18x (enige met aankopen)

### Samenvatting
- **Totaal spend**: €2.609,46 (lifetime; geen spend laatste 30 dagen)
- **Beste**: Hook 13 — bewezen winnaar, schaal deze (70%).
- **Slechtste**: SYBB - Kopie — hoger op alle kostenmetrics, geen resultaat.
- **Aanbeveling**: bouw de volgende flight rond H13/H15, laat H11 en "BLACK" vallen. Maar de échte prioriteit is de **funnel ná de klik** — de ads leveren goedkope clicks, de landing page converteert niet. Fix eerst de LP-conversie (PostHog) vóór nieuw budget.

Rapport opgeslagen in `Output/Reports/Daily/2026-07-16_ads_report.md` en gecommit + gepusht. Google Sheet-write is overgeslagen zoals gevraagd.

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` op de gecombineerde data.

Wil je in plaats daarvan dat ik de **PostHog** landing page data er direct bij pak (die MCP is wél toegestaan in deze run)? Dan kan ik de post-klik bottleneck meteen kwantificeren.
