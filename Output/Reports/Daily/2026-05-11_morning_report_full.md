# Morning Report — 2026-05-11

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,14%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,13** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 96,92** over 9 actieve dagen (niet totaal/30)
> - Bron: spend EUR 872,28 · impressions 68.069 · link_clicks 774
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H14,B3,CTA5 | EUR 11,68 | 1.304 | 10 | 0,77% | EUR 1,17 |
> | H15,B3,CTA5 | EUR 42,06 | 3.732 | 40 | 1,07% | EUR 1,05 |
> | H11, B3, CTA5 | EUR 505,35 | 36.938 | 399 | 1,08% | EUR 1,27 |
> | H13,B3,CTA5 | EUR 192,24 | 15.093 | 179 | 1,19% | EUR 1,07 |
> | H12,B3,CTA5 | EUR 120,95 | 11.002 | 146 | 1,33% | EUR 0,83 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

> 🚨 **OVERRIDE — VERIFIED FUNNEL CONFLICT**
> De budget aanbevelingen in de Ads Report / SYBB / Auto-Optimize secties hieronder zijn gebaseerd op Meta pixel data en conflicteren met de verified Wix order funnel. Volg ALLEEN de 'BUDGET AANBEVELINGEN (VERIFIED)' sectie verderop in dit rapport.
>
> ❌ **H13** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 192,24 spend. Negeer dat advies.
> ❌ **H12** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 120,95 spend. Negeer dat advies.
> ❌ **H15** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 42,06 spend. Negeer dat advies.
> ❌ **H14** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 11,68 spend. Negeer dat advies.
>
> **Top verified performer:** H11 · ROAS 0.69x · 1 order(s) · EUR 350,00 revenue.


## Meta Ads Rapport — 2026-05-11

**Periode:** last_30d (2026-04-11 → 2026-05-10) · **Account:** Sempertex Ad Account · **Status:** geen actieve campagnes, twee meest recente PAUSED campagnes gerapporteerd.

### Overzicht per campagne

| Campagne | Status | Spend | Impr | Clicks | CTR | CPC | CPM | Purch | ROAS |
|---|---|---|---|---|---|---|---|---|---|
| 2026: SYBB | PAUSED | €872,28 | 68.069 | 1.433 | 2,1% | €0,61 | €12,81 | 6 | n.v.t. (pixel datafout) |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n/a |

**Totaal:** €996,70 spend · 75.684 impressions · 1.628 clicks · ? purchases (verifieer Wix) · 6 workshop registrations

### Underperformers
- **H14, B3, CTA5** (origineel adset) — CTR 1,4%, 0 conversies → pauzeer
- **H13, B3, CTA5** (Kopie-campagne) — CPC €0,93, CPM €19,14 → pauzeer per direct
- **H11, B3, CTA5** (Kopie 1 hoofd) — CPC €0,68 maar ? purchases (verifieer Wix) → laat draaien, refresh creative
- **H13/H15** (hoofdcampagne) — CPC boven €0,50 zonder purchases → refresh of pauzeer

### Top performers
- **Beste CTR**: H12, B3, CTA5 (Kopie-campagne) — 3,6%
- **Laagste CPC**: H12, B3, CTA5 (Kopie 2 hoofd) — €0,41
- **Meeste purchases**: H11, B3, CTA5 (Kopie 1) — ? purchases (verifieer Wix)

### Aanbeveling (70-20-10)
1. **70%**: H11 reactiveren als kernad (enige bewezen purchase-driver)
2. **20%**: H12 testen als TOF — hoge CTR moet nog converteren, vermoedelijk landing-page CTA mismatch
3. **10%**: Nieuwe hooks voor SYBB pillar 1 (Mindset) en pillar 7 (Pricing)
4. **Pauzeer**: H13 Kopie + H14 origineel
5. **Funnel-leak**: ? purchases (verifieer Wix) / 635 LPV = 0,9% → fix zit NA de klik, niet vóór

### Google Sheet
**OVERGESLAGEN** — conform instructie geen Google MCPs aangeroepen.

Rapport opgeslagen: `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-11_ads_report.md`

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-10_sybb_report.md`.

**Kernpunten:**
- Campagne `2026: SYBB` is 21 dagen PAUSED (sinds 19/20 april), €0 spend gisteren en de afgelopen 7 dagen.
- Landing page kreeg 3 pageviews op 10 mei, allemaal direct (geen UTM), 100% bounce, 0s avg duration. Alleen `/` bezocht; geen `/checkout`, `/booking` of `/review`.
- PostHog tracked alleen `$pageview` en `$web_vitals`, dus scroll-depth en CTA click rate KPI's zijn niet meetbaar.
- Derde rapport-dag op rij met identieke "stilstand"-output. Top actie: forceer vandaag relaunch-of-stop beslissing; tweede actie: scroll/CTA tracking events wiren vóór relaunch.

Bronnen: alleen Meta Ads MCP (Pipeboard) en PostHog MCP gebruikt, geen Google MCPs.

---

Rapport opgeslagen: `Output/Reports/Daily/2026-05-11_auto_optimize.md`.

**Uitkomst van deze run:**
- Beide toegankelijke accounts (`act_567892422940728`, `act_1489853856181844`) hebben **0 actieve campagnes**. Alle 5 campagnes in het primaire account zijn PAUSED, de SYBB campagne sinds 2026-04-19.
- **Niveau 1 (auto-pauze): 0 ads gepauzeerd** — er is geen levering om de kill-regels op toe te passen.
- **Niveau 2: geen budget/audience voorstellen op huidige data**, maar 4 richtingsvragen in het rapport voor de heropstart-discussie (sales vs lead-gen, funnel-onderzoek, creative-batch, account-toegang voor `act_607231713057715`).
- Historische context van last_30d SYBB toegevoegd ter referentie: Link CTR 1,14% en CPC (link) €1,13 — boven kill-drempels, maarROAS n.v.t. (pixel datafout) op directe attributie.

Geen Google MCPs aangeroepen, niets naar de Google Sheet tracker geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 505,35 | 399 | 1 | 1 (EUR 350,00) | EUR 350,00 | 0.69x | EUR 505,35 |
| H12,B3,CTA5 | EUR 120,95 | 146 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 192,24 | 179 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 11,68 | 10 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 42,06 | 40 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 872,28** | **774** | **1** | **1** | **EUR 350,00** | **0.40x** | **EUR 872,28** |

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
| 🥇 | H11, B3, CTA5 | 0.69x | 1 | EUR 350,00 | EUR 505,35 | **70% budget** — hoogste verified ROAS · NIET pauzeren |
| — | H13,B3,CTA5 | 0 orders | 0 | — | EUR 192,24 | NIET als best performer labelen · 0 Wix orders ondanks EUR 192,24 spend · heroverweeg |
| — | H12,B3,CTA5 | 0 orders | 0 | — | EUR 120,95 | NIET als best performer labelen · 0 Wix orders ondanks EUR 120,95 spend · heroverweeg |
| — | H15,B3,CTA5 | 0 orders | 0 | — | EUR 42,06 | NIET als best performer labelen · 0 Wix orders |
| — | H14,B3,CTA5 | 0 orders | 0 | — | EUR 11,68 | NIET als best performer labelen · 0 Wix orders |

**Verified funnel regels (hard):**
- Top verified performer: **H11** (verified ROAS 0.69x, 1 Wix order(s), EUR 350,00 revenue).
- H11 mag NIET gepauzeerd worden en krijgt 70% van het budget.
- Ads zonder verified orders (H13, H12, H15, H14) mogen NIET als 'beste performer' of 'winner' gelabeld worden, ongeacht Meta pixel CTR/IC/purchase cijfers.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
