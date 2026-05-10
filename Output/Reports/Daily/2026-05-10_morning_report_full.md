# Morning Report — 2026-05-10

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,14%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,08** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 94,06** over 10 actieve dagen (niet totaal/30)
> - Bron: spend EUR 940,63 · impressions 76.542 · link_clicks 874
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H14,B3,CTA5 | EUR 20,82 | 2.470 | 20 | 0,81% | EUR 1,04 |
> | H15,B3,CTA5 | EUR 49,83 | 4.737 | 57 | 1,20% | EUR 0,87 |
> | H11, B3, CTA5 | EUR 521,56 | 38.614 | 428 | 1,11% | EUR 1,22 |
> | H13,B3,CTA5 | EUR 206,99 | 16.766 | 195 | 1,16% | EUR 1,06 |
> | H12,B3,CTA5 | EUR 141,43 | 13.955 | 174 | 1,25% | EUR 0,81 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

> 🚨 **OVERRIDE — VERIFIED FUNNEL CONFLICT**
> De budget aanbevelingen in de Ads Report / SYBB / Auto-Optimize secties hieronder zijn gebaseerd op Meta pixel data en conflicteren met de verified Wix order funnel. Volg ALLEEN de 'BUDGET AANBEVELINGEN (VERIFIED)' sectie verderop in dit rapport.
>
> ❌ **H13** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 206,99 spend. Negeer dat advies.
> ❌ **H12** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 141,43 spend. Negeer dat advies.
> ❌ **H15** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 49,83 spend. Negeer dat advies.
> ❌ **H14** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 20,82 spend. Negeer dat advies.
>
> **Top verified performer:** H11 · ROAS 0.67x · 1 order(s) · EUR 350,00 revenue.


## Meta Ads Rapport — 10 mei 2026

**Status:** Geen ACTIVE campagnes. Rapport toont meest recent gepauzeerde campagnes (beide SYBB 2026), last 30d.

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS* |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | PAUSED | €940,63 | 76.542 | 1.620 | 2,1% | €0,58 | €12,29 | 6 | n.v.t. (pixel datafout)* |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 (6 IC) | n.v.t. |

*ROAS-waarschuwing: de 47x wordt opgeblazen door één Wix-event van €42.773,50 op H13 (terwijl `web_app_in_store_purchase` voor diezelfde ad slechts €4,28 toont). Vermoedelijke value-tracking misconfig in de Wix → Meta Pixel pipeline. Niet vertrouwen tot dit gefixt is.*

### Underperformers

- **Campagne "2026: SYBB - Kopie"** — CPM €16,34 (>€15) én CPC €0,64 (>€0,50), 100 LPV en ? purchases (verifieer Wix) op €124. → Niet heractiveren.
- **Ad H11,B3,CTA5** — €521,56 (55% budget) tegen CPC €0,67. → Pauzeren; H12 doet dezelfde job 40% goedkoper.
- **Ad H13,B3,CTA5** — CPC €0,63 + value-tracking is corrupt. → Pauzeren tot Pixel-fix.

### Top performers

- **Beste CTR (ad)**: H12,B3,CTA5 — 2,55%
- **Laagste CPC**: H12,B3,CTA5 — €0,40
- **Beste ROAS (geverifieerd)**: H11,B3,CTA5 — n.v.t. (pixel datafout) (€1.473,50 op €521,56)

### Samenvatting

- **Totaal spend:** €1.065,05 over 30 dagen
- **Beste performer:** H12,B3,CTA5 — laagste CPC + hoogste CTR, maar **? purchases (verifieer Wix)** ondanks 139 LPV → engagement werkt, conversie-pad lekt.
- **Slechtste performer:** H11,B3,CTA5 — slokt budget tegen 67% boven CPC-target.
- **Aanbeveling (70-20-10):** Fix Wix Pixel value-mapping eerst. Daarna H12 schalen als hoofdcreative, 2-3 hook-varianten op het H12-frame, H11 en H13 archiveren.

### Google Sheet
Stap 6 overgeslagen per instructie. Rapport opgeslagen in:
`/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-10_ads_report.md`

---

> **Wil je funnel data toevoegen?** Geef de landing page metrics uit Wix Analytics of GA4 (visitors, opt-in/booking clicks, add to cart, completed purchases) en ik draai automatisch een `/funnel-diagnose` met de gecombineerde data.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-09_sybb_report.md`.

**TL;DR:** Tweede stilstand-rapport op rij. `2026: SYBB` campagne staat ~20 dagen op PAUSED, €0 spend gisteren. Landing page kreeg 2 pageviews uit organisch verkeer (identiek aan 8 mei). Over 2-9 mei: 25 pageviews totaal, 60% via Instagram/Facebook bio links, 8% residueel uit `meta cpc / sybb / h13_b3_cta5`. Klein lichtpuntje: 3 `/checkout` views in de 8-daagse periode, dus organische instroom converteert nog mondjesmaat. Hoofdactie: relaunch-of-stop beslissing forceren deze week (uiterlijk 12 mei), anders blijft het dagrapport leeg.

---

## Auto-Optimize Rapport — 10 May 2026

**Geen automatische acties uitgevoerd.** Alle Sempertex campagnes staan op PAUSED en er was geen spend in de laatste 3 dagen.

### Belangrijkste bevindingen
- **Sempertex Ad Account**: 5 campagnes, allen PAUSED. SYBB campagne sinds 2026-04-19 op pauze (EUR 94,06/dag (10 actieve dagen) budget).
- **AmbitionAvenue**: leeg, geen campagnes.
- **act_607231713057715** (genoemd in command): Pipeboard token heeft geen toegang. Allowed accounts zijn alleen `act_1489853856181844` en `act_567892422940728`.
- Geen ads gepauzeerd, geen budget wijzigingen, geen schrijf-acties.

### Vragen voor jou
1. Is heractivering van `2026: SYBB` gepland? Zo ja, wanneer?
2. Moet `act_607231713057715` uit het `/ads-auto-optimize` command verwijderd worden, of moet de Pipeboard koppeling uitgebreid worden?

Rapport opgeslagen in `Output/Reports/Daily/2026-05-10_auto_optimize.md`.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 1 | 1 (EUR 350,00) | EUR 350,00 | 0.67x | EUR 521,56 |
| H12,B3,CTA5 | EUR 141,43 | 174 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 206,99 | 195 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 20,82 | 20 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 49,83 | 57 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 940,63** | **874** | **1** | **1** | **EUR 350,00** | **0.37x** | **EUR 940,63** |

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
| — | H13,B3,CTA5 | 0 orders | 0 | — | EUR 206,99 | NIET als best performer labelen · 0 Wix orders ondanks EUR 206,99 spend · heroverweeg |
| — | H12,B3,CTA5 | 0 orders | 0 | — | EUR 141,43 | NIET als best performer labelen · 0 Wix orders ondanks EUR 141,43 spend · heroverweeg |
| — | H15,B3,CTA5 | 0 orders | 0 | — | EUR 49,83 | NIET als best performer labelen · 0 Wix orders |
| — | H14,B3,CTA5 | 0 orders | 0 | — | EUR 20,82 | NIET als best performer labelen · 0 Wix orders |

**Verified funnel regels (hard):**
- Top verified performer: **H11** (verified ROAS 0.67x, 1 Wix order(s), EUR 350,00 revenue).
- H11 mag NIET gepauzeerd worden en krijgt 70% van het budget.
- Ads zonder verified orders (H13, H12, H15, H14) mogen NIET als 'beste performer' of 'winner' gelabeld worden, ongeacht Meta pixel CTR/IC/purchase cijfers.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
