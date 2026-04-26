# Morning Report — 2026-04-26

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
> ❌ **Pauzeer H13** advies in dit rapport conflicteert met verified ROAS 2.05x. H13 is de top performer — NIET pauzeren.
> ❌ **H12** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 155,80 spend. Negeer dat advies.
> ❌ **H14** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 122,96 spend. Negeer dat advies.
> ❌ **H15** wordt elders in dit rapport als winnaar/best performer gelabeld of krijgt extra budget, maar heeft **0 Wix orders** op EUR 52,15 spend. Negeer dat advies.
>
> **Top verified performer:** H13 · ROAS 2.05x · 1 order(s) · EUR 423,50 revenue.


Rapport opgeslagen. Hier het Meta Ads rapport voor 2026-04-26:

## Meta Ads Rapport — 2026-04-26

**Status:** Geen ACTIVE campagnes. Alle 5 campagnes op `act_567892422940728` staan PAUSED. Het tweede toegestane account `act_1489853856181844` heeft geen campagnes. `act_607231713057715` is niet toegankelijk via deze API token.

### Overzicht per campagne (last 30d)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. | Init. CO |
|----------|--------|-------|-------|--------|------|------|------|--------|------|
| 2026: SYBB | PAUSED | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 6 | 33 |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 6 |
| Last push Nozzle Up | PAUSED | geen data | — | — | — | — | — | — | — |

### Underperformers
- **2026: SYBB - Kopie (campagne)** — CPC €0,64 + CPM €16,34, ? purchases (verifieer Wix) → consolideren met hoofdcampagne
- **H13,B3,CTA5 (Kopie campagne)** — CPC €0,93 → pauzeren
- **H11,B3,CTA5 (Kopie 1)** — CPC €0,67 maar hoogste spend → CPC-optimalisatie ipv afschalen
- Geen frequency-issues (max 2,19 campagne, 1,95 ad)

### Top performers
- **Beste CTR**: H15,B3,CTA5 — 6,4% (klein sample) | met volume: H12,B3,CTA5 — 4,7%
- **Laagste CPC**: H15 — €0,23 | met volume: H12,B3,CTA5 (Kopie 2) — €0,40
- **Beste CPM**: H14,B3,CTA5 — €7,43
- **Meeste purchases**: H11,B3,CTA5 (Kopie 1) — ? purchases (verifieer Wix)

### Tracking-waarschuwing
Meta `purchase` action_values zijn afwijkend hoog (€42.773 voor ? purchases (verifieer Wix)) terwijl `web_app_in_store_purchase` waarden in centen staan. Pixel value-mapping in Wix → Meta integratie checken; ROAS uit Meta is nu niet betrouwbaar.

### Samenvatting & aanbeveling (Hormozi 70-20-10)
- **Totaal spend:** €1.183,89 / ? purchases (verifieer Wix) (te valideren via Wix)
- **70% bewezen winnaars:** H12 en H14 (BATCH 2 origineel) — bouw nieuwe ACTIVE campagne hierop
- **20% variaties:** H11 thumbnail/openingsframe varianten testen voor CPC <€0,50
- **10% experimenten:** H15 budget verhogen voor signifcant volume
- **Direct:** "2026: SYBB - Kopie" campagne pauzeren; H13 in beide kopie-adsets pauzeren
- **Beslismoment:** geen enkele campagne ACTIVE — bewust besluit nodig om aan te zetten of nieuwe campagne op winnende creatives te bouwen

### Google Sheet
Niet geschreven (stap 6 overgeslagen per instructie).

Rapport opgeslagen naar `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-04-26_ads_report.md`.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Lokaal gecommit. Push overgeslagen omdat `main` 57 commits ahead én 195 commits behind `origin/main` is. Een gewone push wordt geweigerd, en force push zou 195 remote commits overschrijven, dat is niet veilig zonder jouw bevestiging.

**Rapport:** `Output/Reports/Daily/2026-04-25_sybb_report.md`

**Kern:** Beide SYBB campagnes paused sinds 19/20 april. Gisteren 0 Meta spend, 3 organische LP-sessies (100% bounce). 7d-data laat de "Kopie"-variant winnen (CTR 2.56% vs 2.21%, CPC €0.64 vs €0.72, 6 IC vs 2). Top-actie: vóór heractivering eerst de landingpage hero fixen (96% van sessies komt niet voorbij 25% scroll).

Wil je dat ik de divergentie met origin/main onderzoek (pull/merge of reset) zodat de push alsnog kan?

---

## Samenvatting

**Geen automatische acties uitgevoerd** — er zijn geen actieve campagnes in het Sempertex Ad Account. Beide SYBB-campagnes (2026: SYBB en 2026: SYBB - Kopie) staan op PAUSED sinds 19/20 april. Ad-niveau insights voor `last_3d` zijn leeg, wat bevestigt dat er geen recente spend is.

Alleen Pipeboard Meta Ads MCP gebruikt, geen Google MCPs aangeroepen, niets naar de tracker Google Sheet geschreven.

**Rapport opgeslagen:** `Output/Reports/Daily/2026-04-26_auto_optimize.md`

Het rapport bevat ook context uit de laatste run-periode (last_7d en last_30d) met link-metrics als referentie voor heractivatie, plus drie voorgestelde vervolgstappen die op jouw goedkeuring wachten.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 1 | 1 (EUR 350,00) | EUR 350,00 | 0.67x | EUR 521,56 |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 1 (EUR 423,50) | EUR 423,50 | 2.05x | EUR 207,00 |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.059,47** | **1036** | **1** | **2** | **EUR 773,50** | **0.73x** | **EUR 529,74** |

> **CROSS-REFERENCE: Meta Pixel vs Wix Orders**
> - Meta pixel: 18 purchases (EUR 132.741,00)
> - Wix orders: 2 orders (EUR 773,50)
> - Verschil: +16 pixel purchases, +EUR 131.967,50 pixel waarde
> - **Verdict: PIXEL OVERSTELT.** Gebruik Wix orders als bron van waarheid.
> - Mogelijke oorzaken: Conversions API duplicaten, test purchases, cross-domain pixel fires

> **ONGEMATCHTE /thank-you SESSIES:**
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
| 🥇 | H13,B3,CTA5 | 2.05x | 1 | EUR 423,50 | EUR 207,00 | **70% budget** — hoogste verified ROAS · NIET pauzeren |
| 🥈 | H11, B3, CTA5 | 0.67x | 1 | EUR 350,00 | EUR 521,56 | 20% budget — tweede verified winner · houd actief |
| — | H12,B3,CTA5 | 0 orders | 0 | — | EUR 155,80 | NIET als best performer labelen · 0 Wix orders ondanks EUR 155,80 spend · heroverweeg |
| — | H14,B3,CTA5 | 0 orders | 0 | — | EUR 122,96 | NIET als best performer labelen · 0 Wix orders ondanks EUR 122,96 spend · heroverweeg |
| — | H15,B3,CTA5 | 0 orders | 0 | — | EUR 52,15 | NIET als best performer labelen · 0 Wix orders ondanks EUR 52,15 spend · heroverweeg |

**Verified funnel regels (hard):**
- Top verified performer: **H13** (verified ROAS 2.05x, 1 Wix order(s), EUR 423,50 revenue).
- H13 mag NIET gepauzeerd worden en krijgt 70% van het budget.
- Ads zonder verified orders (H12, H14, H15) mogen NIET als 'beste performer' of 'winner' gelabeld worden, ongeacht Meta pixel CTR/IC/purchase cijfers.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
