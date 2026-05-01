# Morning Report — 2026-05-01

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 6 purchases (totaal EUR 44247,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,13%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,02** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 88,29** over 12 actieve dagen (niet totaal/30)
> - Bron: spend EUR 1059,47 · impressions 91.839 · link_clicks 1.036
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H12,B3,CTA5 | EUR 14,37 | 1.058 | 20 | 1,89% | EUR 0,72 |
> | H13,B3,CTA5 | EUR 0,01 | 1 | 0 | 0,00% | EUR 0,00 |
> | H14,B3,CTA5 | EUR 122,96 | 16.551 | 158 | 0,95% | EUR 0,78 |
> | H15,B3,CTA5 | EUR 2,32 | 157 | 4 | 2,55% | EUR 0,58 |
> | H15,B3,CTA5 | EUR 49,83 | 4.737 | 57 | 1,20% | EUR 0,87 |
> | H11, B3, CTA5 | EUR 521,56 | 38.614 | 428 | 1,11% | EUR 1,22 |
> | H13,B3,CTA5 | EUR 206,99 | 16.766 | 195 | 1,16% | EUR 1,06 |
> | H12,B3,CTA5 | EUR 141,43 | 13.955 | 174 | 1,25% | EUR 0,81 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 1 mei 2026

**Geen actieve campagnes.** Beide SYBB-campagnes zijn op 19 april 2026 gepauzeerd. Rapport toont last_30d performance van de meest recente PAUSED campagnes.

### Overzicht per campagne

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. | ROAS* |
|----------|--------|-------|-------|--------|-----|-----|-----|--------|-------|
| 2026: SYBB | Paused | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 6 | n.v.t. (pixel datafout) |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n/a |

*Pixel revenue komt door als hoge integer (44.247). Geïnterpreteerd als cents → €442,47 →ROAS n.v.t. (pixel datafout). Indien EUR:ROAS n.v.t. (pixel datafout). **Verifieer pixel-config.**

### Underperformers
- **2026: SYBB** — CPC €0,55 (boven €0,50 drempel)
- **2026: SYBB - Kopie** — CPC €0,64 + CPM €16,34 (beide boven drempel) → archiveren of mergen
- **Ad H14, B3, CTA5** — €122,96 spend, 0 ATC, 0 IC, ? purchases (verifieer Wix) → niet heractiveren

### Top performers
- **Beste CTR (significant spend):** H12, B3, CTA5 (Kopie 2) — 2,6%
- **Laagste CPC:** H12, B3, CTA5 (Kopie 2) — €0,40
- **Meeste purchases:** **H11, B3, CTA5** — 4 van de ? purchases (verifieer Wix)

### Funnel bottleneck
Click → Landing page view: 57,7% drop (1.935 → 818). Tracking-gap of trage pagina. Tweede leak: LPV → ATC slechts 5,4%.

### Samenvatting
- **Totaal spend:** €1.183,89 (last_30d)
- **Aanbeveling (70-20-10):** H11 + H13 als hero heractiveren, H12 testen met andere body/CTA, H14 droppen, kopie-campagne archiveren. Eerst click → LPV gap fixen + pixel-waardes verifiëren vóór heractivatie.

### Output
- Rapport opgeslagen: `Output/Reports/Daily/2026-05-01_ads_report.md`
- Google Sheet write: **overgeslagen** (per run-instructie)

> **Wil je funnel data toevoegen?** Geef dan landing page visitors, opt-in/booking clicks, add to cart, en completed purchases uit Wix Analytics of GA4 — dan draai ik er een `/funnel-diagnose` overheen.

---

Rapport opgeslagen op `Output/Reports/Daily/2026-04-30_sybb_report.md`.

**Kern bevindingen:**
- Campagne `2026: SYBB` (id `120239435987290239`) staat **dag 11 op PAUSED** sinds 2026-04-19 — €0 spend, 0 impressies, 0 clicks op 2026-04-30. Cumulatief €1.100 niet-besteed budget.
- Filter op ACTIVE in account `act_567892422940728` retourneert een lege lijst — geen enkele draaiende campagne in het hele account.
- Duplicaat `2026: SYBB - Kopie` (id `120243293329420239`) ook nog steeds PAUSED, geen activiteit.
- **PostHog MCP niet beschikbaar** in deze sessie (tweede dag op rij) — sectie 3 en 4 zonder data, cross-referencing niet mogelijk.
- Top actie blijft: beslissing over reactiveren / vervangen / definitief stoppen, plus PostHog-verbinding herstellen.

---

## Auto-Optimize Rapport — 2026-05-01

**Geen acties uitgevoerd** — er zijn op dit moment geen actieve campagnes in de toegankelijke accounts.

**Belangrijkste bevindingen:**
- `act_567892422940728`: 5 campagnes, allemaal PAUSED (incl. `2026: SYBB` met €100 daily budget, gepauzeerd sinds 2026-04-19)
- `act_1489853856181844`: leeg
- `act_607231713057715`: geen API-toegang met huidig token
- Geen spend in `last_3d` of `last_7d` op enig account

Rapport opgeslagen op `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-01_auto_optimize.md`.

**Vraag aan jou:** is het bedoeling dat `2026: SYBB` nog gepauzeerd staat? Als die weer actief moet, kan ik 'm voor je heractiveren — daarna kan deze command weer functioneel draaien zodra er ≥24u performance-data is.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 0 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.059,47** | **1036** | **0** | **0** | **EUR 0,00** | **-** | **-** |

> Wix orders: 0 orders in periode. Update `data/wix-orders.json` met orders uit Wix admin.

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

> Geen van de ads heeft verified Wix orders in de periode. GEEN budget herverdeling op basis van verified funnel mogelijk. Wacht op meer data — negeer Meta pixel 'best performer' claims tot die tijd.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
