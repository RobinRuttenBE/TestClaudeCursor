## Meta Ads Rapport — 14 July 2026

> **Geen actieve campagnes** op beide accounts. Hieronder de meest recente **gepauzeerde** campagnes met **lifetime** performance (paused sinds april 2025, dus `last_30d` was leeg → `maximum` gebruikt).

**Accounts:** `act_567892422940728` Sempertex (5 paused campagnes) · `act_1489853856181844` AmbitionAvenue (leeg).

### Overzicht per campagne (spend hoog → laag)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,80x |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,30x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,78x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,37x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,00x |

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 (>€0,50) én CPM €16,34 (>€15) → korte test, 0 aankopen. Niet heractiveren zonder nieuwe creative/audience.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (grensgeval) → laagste engagement, maar goedkoopste reach (CPM €1,64). Hook aanscherpen.
- **Last push Nozzle Up** — ROAS 0,78x (onder break-even) → traffic prima, conversie niet. Lek zat in landing page/aanbod.
- Frequency: geen enkele campagne >3,5 → geen creative fatigue.

### Top performers
- **Beste CTR:** 2026: SYBB — 4,1%
- **Laagste CPC:** Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS:** 2026: SYBB — 17,80x

### Samenvatting
- **Totaal spend:** €4.867,46 (lifetime; matcht exact het account-totaal → alle campagnes gedekt)
- **Beste performer:** 2026: SYBB — hoogste CTR, lage CPC, grootste reach, beste ROAS. Sterkste concept in het account.
- **Slechtste performer:** Last push Nozzle Up — enige campagne onder break-even.
- **Aanbeveling (70-20-10):** 70% budget op de bewezen winnaar → heractiveer **2026: SYBB** als hoofdcampagne. 20% op variaties van de SYBB-hook. 10% experimenten. Laat de Kopie en Last push met rust tot landing page/aanbod verbeterd is.

⚠️ **Datakwaliteit:** SYBB's ROAS 17,80x berust op 6 purchases à ~€7.374 (gerapporteerde waarde €44.247). Hoog voor B2B, mogelijk één grote order of attributie-artefact, verifieer in de shop voor je dit als benchmark neemt.

### Google Sheet
Overgeslagen (strikte run-regel). Rapport opgeslagen in `Output/Reports/Daily/2026-07-14_ads_report.md`.

---

Twee opmerkingen bij de run-regels:
- **Geen Google MCP aangeroepen** en niet naar de Meta Ads Tracker geschreven, zoals gevraagd.
- De `claude.ai Pipeboard Meta Ads` connector vereist auth, maar de losse **pipeboard-meta-ads** server werkte wel, dus alle data is live opgehaald.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of PostHog (visitors, opt-in/booking clicks, add to cart, completed purchases), dan draai ik automatisch een `/funnel-diagnose` en voeg de volledige funnel-analyse toe.
