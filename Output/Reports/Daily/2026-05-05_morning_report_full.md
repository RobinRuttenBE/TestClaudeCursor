# Morning Report — 2026-05-05

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
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
> | H11, B3, CTA5 | EUR 521,56 | 38.614 | 428 | 1,11% | EUR 1,22 |
> | H13,B3,CTA5 | EUR 206,99 | 16.766 | 195 | 1,16% | EUR 1,06 |
> | H12,B3,CTA5 | EUR 141,43 | 13.955 | 174 | 1,25% | EUR 0,81 |
> | H14,B3,CTA5 | EUR 122,96 | 16.551 | 158 | 0,95% | EUR 0,78 |
> | H15,B3,CTA5 | EUR 49,83 | 4.737 | 57 | 1,20% | EUR 0,87 |
> | H12,B3,CTA5 | EUR 14,37 | 1.058 | 20 | 1,89% | EUR 0,72 |
> | H15,B3,CTA5 | EUR 2,32 | 157 | 4 | 2,55% | EUR 0,58 |
> | H13,B3,CTA5 | EUR 0,01 | 1 | 0 | 0,00% | EUR 0,00 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

> 🚨 **OVERRIDE — VERIFIED FUNNEL CONFLICT**
> De budget aanbevelingen in de Ads Report / SYBB / Auto-Optimize secties hieronder zijn gebaseerd op Meta pixel data en conflicteren met de verified Wix order funnel. Volg ALLEEN de 'BUDGET AANBEVELINGEN (VERIFIED)' sectie verderop in dit rapport.
>
> ❌ **H13** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 207,00 spend. Negeer dat advies.
> ❌ **H12** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 155,80 spend. Negeer dat advies.
> ❌ **H14** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 122,96 spend. Negeer dat advies.
> ❌ **H15** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 52,15 spend. Negeer dat advies.
>
> **Top verified performer:** H11 · ROAS 0.67x · 1 order(s) · EUR 350,00 revenue.


## Meta Ads Rapport — 5 mei 2026

**Periode:** last 30 days (2026-04-05 t/m 2026-05-04) · **Account:** Sempertex Ad Account (`act_567892422940728`)

> **Geen ACTIVE campagnes.** Account `act_607231713057715` niet toegankelijk. Rapport gaat over recente PAUSED SYBB campagnes met data binnen 30d.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | PAUSED | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 6 | n.v.t. (pixel datafout)* |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |
| **Totaal** | | **€1.183,89** | **99.454** | **2.130** | **2,1%** | **€0,56** | **€11,90** | **6** | **n.v.t. (pixel datafout)*** |

\*Pixel meldt €44.247 op ? purchases (verifieer Wix) (€7.374 gem.) — verifieer in Wix voor je extern deelt.

### Underperformers
- **2026: SYBB** — CPC €0,55 (>€0,50). Bij re-launch eerst top 3 ads filteren op CPC.
- **2026: SYBB - Kopie** — CPC €0,64 én CPM €16,34, ? purchases (verifieer Wix) bij €124 spend. Niet heractiveren in huidige vorm.
- **2026: SYBB - Kopie** — 6 initiate checkouts → ? purchases (verifieer Wix). Mogelijk checkout-flow probleem of pixel-mismatch.

### Top performers
- **Beste CTR**: 2026: SYBB - Kopie — 2,6%
- **Laagste CPC + CPM + beste ROAS**: 2026: SYBB

### Aanbeveling (Hormozi 70-20-10)
1. **70%**: Re-launch alleen hoofd-campagne, kill ads met CPC ≥€0,50.
2. **20%**: 2-3 nieuwe variaties op winning hook.
3. **10%**: Eén radicaal nieuwe hook (Kopie kwalificeert hier niet — was te dicht op origineel).
4. **Tracking-fix eerst**: Verifieer purchase value in Wix vóór nieuw budget gealloceerd wordt.

### Google Sheet
**Niet geschreven** — overgeslagen volgens strikte regel voor deze run.

Rapport opgeslagen: `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-05_ads_report.md`

---

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4.
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-04_sybb_report.md`.

**Kern:** Er is gisteren feitelijk niets gebeurd op SYBB. De campagne `2026: SYBB` staat sinds 19 april op PAUSED (laatste spend €43,81), de kopie campagne is ook PAUSED en nooit live gegaan. Gisteren: 0 spend, 0 paid clicks. De LP zag 2 organische bezoekers (beide bounce, geen scroll-events). 7d window: 23 sessies waarvan 14 pageviews via Instagram bio link, 0 via Meta paid.

**Belangrijkste actie:** Beslissen of de SYBB campagne her-activeert of formeel gearchiveerd wordt — tot dat moment is dit dagelijkse rapport leeg. Daarnaast de zwevende `2026: SYBB - Kopie` opruimen en LP tracking verifiëren vóór re-launch.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-05_auto_optimize.md`.

**Samenvatting:**
- **0 ads gepauzeerd** — er zijn geen ACTIVE campagnes in `act_567892422940728` (alle 5 zichtbare campagnes, inclusief 2026: SYBB, staan op PAUSED).
- `act_1489853856181844` is leeg.
- `act_607231713057715` (uit de command spec) is niet toegankelijk met de huidige Pipeboard-token — verzoek aan jou om óf permissies uit te breiden óf dat account uit de spec te halen.
- Geen 70-20-10 classificatie of budget-voorstellen mogelijk zonder actieve ads. Hoofdactiepunt: beslissen of **2026: SYBB** (€100/dag) hervat moet worden of vervangen via `/ads-deploy`.

Geen Google MCPs aangeroepen, geen schrijfacties naar de Google Sheet tracker.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 1 | 1 (EUR 350,00) | EUR 350,00 | 0.67x | EUR 521,56 |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.059,47** | **1036** | **1** | **1** | **EUR 350,00** | **0.33x** | **EUR 1.059,47** |

> **CROSS-REFERENCE: Meta Pixel vs Wix Orders**
> - Meta pixel: 18 purchases (EUR 132.741,00)
> - Wix orders: 1 orders (EUR 350,00)
> - Verschil: +17 pixel purchases, +EUR 132.391,00 pixel waarde
> - **Verdict: PIXEL OVERSTELT.** Gebruik Wix orders als bron van waarheid.
> - Mogelijke oorzaken: Conversions API duplicaten, test purchases, cross-domain pixel fires

> **ONGEMATCHTE /thank-you SESSIES:**
> - Sessie op 2026-04-26, utm_content=(geen utm_content)
> - Sessie op 2026-04-18, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

**Ranking op Verified ROAS:**

| Rank | Ad | Verified ROAS | Wix Orders | Revenue | Spend | Advies |
|---|---|---|---|---|---|---|
| 🥇 | H11, B3, CTA5 | 0.67x | 1 | EUR 350,00 | EUR 521,56 | **70% budget** — hoogste verified ROAS · NIET pauzeren |
| — | H13,B3,CTA5 | 0 orders | 0 | — | EUR 207,00 | NIET als best performer labelen · 0 Wix orders ondanks EUR 207,00 spend · heroverweeg |
| — | H12,B3,CTA5 | 0 orders | 0 | — | EUR 155,80 | NIET als best performer labelen · 0 Wix orders ondanks EUR 155,80 spend · heroverweeg |
| — | H14,B3,CTA5 | 0 orders | 0 | — | EUR 122,96 | NIET als best performer labelen · 0 Wix orders ondanks EUR 122,96 spend · heroverweeg |
| — | H15,B3,CTA5 | 0 orders | 0 | — | EUR 52,15 | NIET als best performer labelen · 0 Wix orders ondanks EUR 52,15 spend · heroverweeg |

**Verified funnel regels (hard):**
- Top verified performer: **H11** (verified ROAS 0.67x, 1 Wix order(s), EUR 350,00 revenue).
- H11 mag NIET gepauzeerd worden en krijgt 70% van het budget.
- Ads zonder verified orders (H13, H12, H14, H15) mogen NIET als 'beste performer' of 'winner' gelabeld worden, ongeacht Meta pixel CTR/IC/purchase cijfers.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
