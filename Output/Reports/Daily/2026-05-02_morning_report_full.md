# Morning Report — 2026-05-02

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

## Meta Ads Rapport — 2026-05-02

**Periode:** last_30d (2026-04-02 t/m 2026-05-01)
**Account:** Sempertex Ad Account (`act_567892422940728`)
**Status:** Geen ACTIEVE campagnes. De 2 meest recente SYBB campagnes zijn PAUSED — hun laatste 30d performance staat hieronder.

### Overzicht per campagne

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Conv. | ROAS* |
|----------|--------|-------|-------|--------|------|------|------|------|-------|
| 2026: SYBB | Paused | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 6 | n.v.t. (pixel datafout)* |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |
| **Totaal** | — | **€1.183,89** | **99.454** | **2.130** | **2,1%** | **€0,56** | **€11,90** | **6** | **n.v.t. (pixel datafout)*** |

\* **Data-waarschuwing:** ad H13,B3,CTA5 (Kopie 3) rapporteert ? purchases (verifieer Wix) met value €42.773,50 (= €21.386/aankoop). Pixel value is fout gemapt. Werkelijke ROAS (zonder outlier): ~n.v.t. (pixel datafout).

### Underperformers
- **H11,B3,CTA5 (Kopie 1)** — CPC €0,67, hoogste spender (€521,56) → inefficiënt op schaal
- **H13,B3,CTA5 (Kopie 3, SYBB)** — CPC €0,63 + Pixel value-bug → fix tracking voor relaunch
- **H13,B3,CTA5 (Kopie 3, SYBB-Kopie)** — CPC €0,93, CPM €19,14 → 3 drempels overschreden
- **H12,B3,CTA5 (Kopie 2, SYBB-Kopie)** — CPM €18,92 → dure reach
- Geen creative fatigue (max freq 2,19) en geen CTR<1%

### Top performers
- **Beste CTR (volume):** H12,B3,CTA5 (BATCH 2) — **4,7%** bij 1.058 impressies, CPC €0,29
- **Laagste CPC:** H15,B3,CTA5 (BATCH 2) — €0,23 (lage volume)
- **Enige geloofwaardige converteerder:** H11,B3,CTA5 (Kopie 1) — ? purchases (verifieer Wix), ROAS ~n.v.t. (pixel datafout)
- **Beste CPM:** H14,B3,CTA5 (BATCH 2) — €7,43

### Samenvatting & aanbeveling (Hormozi 70-20-10)
- 62% van spend zit in 2 ads (H11/H13 in adsets Kopie 1/3) — beide met CPC boven drempel
- **Winnaar voor relaunch:** H12,B3,CTA5 (BATCH 2) als hoofdcreative; H11,B3,CTA5 voor conversie
- **70% schalen:** H12 + H11 hooks behouden
- **20% variaties:** test H12,B[2,4],CTA5 en H11+CTA5 op LAL
- **10% experimenteel:** nieuw hooktype (credibility/transformation) + 1 nieuw format
- **Eerst doen:** Pixel value-mapping fixen vóór relaunch, anders is ROAS-data nutteloos

### Google Sheet
Overgeslagen per instructie. Rapport opgeslagen op:
`/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-02_ads_report.md`

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Als je deze data aanlevert, draai ik automatisch een `/funnel-diagnose` analyse en voeg die als sectie toe.

---

Rapport opgeslagen op `Output/Reports/Daily/2026-05-01_sybb_report.md`.

**Belangrijkste bevindingen:**
- Campagne `2026: SYBB` (id 120239435987290239) is **PAUSED sinds 2026-04-19** — geen spend/impressies/clicks op 2026-05-01. Ook de variant `2026: SYBB - Kopie` staat paused.
- **PostHog MCP gaf "Failed to connect"** bij health check, dus geen LP/scroll/bounce data beschikbaar. Cross-references waren vandaag onmogelijk.
- 30d historische context (2026-04-02 → 04-19 actief): €1.059,47 spend, CTR 2,11%, CPC €0,55 (boven target), frequency 2,19, ? purchases (verifieer Wix).
- Top acties: (1) beslis heractiveren of bewust on hold, (2) fix PostHog MCP connectie, (3) bereid nieuwe creative-batch voor (CPC + freq waren al op fatigue-niveau bij pauze).

Conform de strikte regel zijn er geen Google MCPs aangeroepen en is alleen lokaal weggeschreven.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-02_auto_optimize.md`.

**Samenvatting:**
- Alle campagnes op Sempertex account `act_567892422940728` staan PAUSED. Laatste actieve campagne (`2026: SYBB`) is gepauzeerd op 2026-04-19.
- Account `act_1489853856181844` is leeg; `act_607231713057715` is niet toegankelijk met dit token.
- Geen spend in last_3d of last_7d → geen kill-regels triggers, geen 70-20-10 classificatie, geen voorstellen.
- 0 ads gepauzeerd, 0 waarschuwingen.

Belangrijkste actie-item buiten dit command: beslissen wanneer SYBB weer live gaat — de funnel ligt al 13 dagen stil.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 0 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| (geen ad match) | - | - | - | 2 (EUR 773,50) | EUR 773,50 | - | - |
| **Totaal** | **EUR 1.059,47** | **1036** | **0** | **2** | **EUR 773,50** | **0.73x** | **EUR 529,74** |

> **CROSS-REFERENCE: Meta Pixel vs Wix Orders**
> - Meta pixel: 18 purchases (EUR 132.741,00)
> - Wix orders: 2 orders (EUR 773,50)
> - Verschil: +16 pixel purchases, +EUR 131.967,50 pixel waarde
> - **Verdict: PIXEL OVERSTELT.** Gebruik Wix orders als bron van waarheid.
> - Mogelijke oorzaken: Conversions API duplicaten, test purchases, cross-domain pixel fires

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

> Geen van de ads heeft verified Wix orders in de periode. GEEN budget herverdeling op basis van verified funnel mogelijk. Wacht op meer data — negeer Meta pixel 'best performer' claims tot die tijd.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
