# Morning Report — 2026-07-16

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

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

---

Klaar. Rapport opgeslagen op `Output/Reports/Daily/2026-07-15_sybb_report.md`, gecommit en gepusht.

**Belangrijkste uitkomst: er valt voor 15 juli geen performance te rapporteren.**

- **Meta Ads (wél verbonden):** de campagne `2026: SYBB` (`120239435987290239`) staat op **PAUSED**. Nul spend/impressies/clicks voor gisteren, de 7-daagse baseline én de afgelopen 30 dagen. Er is ook een gepauzeerde kopie `2026: SYBB - Kopie`. Geen data = geen ad-variant analyse.
- **PostHog (niet beschikbaar):** er is in deze sessie **geen PostHog MCP verbonden**. Landing page health (bounce, scroll depth, CTA, funnel) kon dus niet worden opgehaald. Ik heb hier niets verzonnen; de betreffende secties staan gemarkeerd als "geen data".

Ik heb me strikt aan je run-regel gehouden: alleen Meta Ads MCP en PostHog MCP geprobeerd, geen enkele Google MCP aangeroepen en niet naar de Google Sheet tracker geschreven.

**Twee dingen die je aandacht vragen:**
1. Wil je dat SYBB weer live gaat? Dan moet `2026: SYBB` geactiveerd worden — zeg het en ik doe het (of doe het in Ads Manager).
2. De PostHog-connectie moet hersteld/geautoriseerd worden, anders blijft de landing-page-helft van dit dagelijkse rapport leeg.

---

Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-16_auto_optimize.md` en gepusht.

## Samenvatting

**Er is niets te optimaliseren — geen enkele campagne staat aan.**

- **Databronnen:** alleen Meta Ads MCP (Pipeboard). Geen Google MCPs, niet naar de tracker-Sheet geschreven. PostHog niet nodig (geen actieve ads om te kruisen).
- **Primair account `act_567892422940728`:** 5 campagnes, allemaal **PAUSED** — inclusief `2026: SYBB` (dagbudget €100,00, gepauzeerd sinds 19 april 2026).
- **Tweede account `act_1489853856181844`:** geen actieve campagnes.
- **Configureerde `act_607231713057715`:** niet toegankelijk met dit API-token (toegestaan: alleen `act_567892422940728` en `act_1489853856181844`). Dit wil je mogelijk in het command bijwerken.

**Acties:** 0 ads gepauzeerd (niks actief), geen waarschuwingen, geen 70-20-10 classificatie mogelijk.

**Openstaande vraag:** de `2026: SYBB` campagne staat al maanden op pauze — sluit aan bij het SYBB dagrapport van 15 juli ("campaign paused"). Wil je dat ik hem activeer, of blijft alles bewust uit? Zolang alles gepauzeerd blijft, produceert dit command elke dag een leeg rapport.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
