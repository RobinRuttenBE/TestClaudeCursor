# Morning Report — 2026-04-19

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,12%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,02** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 84,62** over 12 actieve dagen (niet totaal/30)
> - Bron: spend EUR 1015,48 · impressions 89.063 · link_clicks 1.000
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H11, B3, CTA5 | EUR 503,89 | 37.483 | 410 | 1,09% | EUR 1,23 |
> | H13,B3,CTA5 | EUR 184,72 | 15.357 | 179 | 1,17% | EUR 1,03 |
> | H12,B3,CTA5 | EUR 137,38 | 13.719 | 172 | 1,25% | EUR 0,80 |
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

## Meta Ads Rapport — 2026-04-19

### Overzicht per campagne

| Campagne   | Status | Spend    | Impressions | Clicks | CTR  | CPC   | CPM    | Conv. | ROAS   |
|------------|--------|----------|-------------|--------|------|-------|--------|-------|--------|
| 2026: SYBB | Active | €1015,48 | 89.063      | 1.873  | 2,1% | €0,54 | €11,40 | 6     | n.v.t. (pixel datafout) |

### Actieve ads

| Ad (adset)            | Spend   | CTR  | CPC   | CPM    | Purch. | ROAS    | Flag                |
|-----------------------|---------|------|-------|--------|--------|---------|---------------------|
| H11,B3,CTA5 (Kopie 1) | €503,89 | 1,09% | € 1,23 | €13,44 | 4      | n.v.t. (pixel datafout)   | CPC te hoog         |
| H13,B3,CTA5 (Kopie 3) | €184,72 | 1,17% | € 1,03 | €12,03 | 2      | n.v.t. (pixel datafout)  | CPC hoog, top ROAS  |
| H12,B3,CTA5 (Kopie 2) | €137,38 | 1,89% | € 0,72 | €10,01 | 0      | —       | Sterke CTR, 0 conv. |

### Underperformers

- **H11 (Kopie 1)** — CPC €0,67 (drempel €0,50), slokt 50% budget op met slechts ROAS n.v.t. (pixel datafout) → halveren of pauzeren.
- **H13 (Kopie 3)** — CPC €0,61 maar **niet pauzeren**: draagt 97% van revenue. Test nieuwe hooks om CPC te drukken.
- **Campagne-CPC €0,54** ligt 8% boven drempel, getrokken door H11 en H13.

### Top performers

- **Beste CTR:** H12 (Kopie 2) — 2,6%
- **Laagste CPC:** H12 (Kopie 2) — €0,39
- **Beste ROAS:** H13 (Kopie 3) — n.v.t. (pixel datafout) (€42.773 revenue op €184,72 spend)

### Samenvatting

- **Totaal spend:** €1.015,48 (30d, ≈€34/dag — daily budget van €100 niet vol benut)
- **Beste performer:** H13 genereert bijna alle purchase revenue — één duidelijke winner.
- **Slechtste performer:** H11 — hoog budget, lage ROAS, dure CPC.
- **Paradox:** H12 heeft beste front-end ratios maar ? purchases (verifieer Wix) → click-to-purchase lek.

**Aanbeveling (70-20-10):** 70% budget verhoging op H13 (winner), 20% varianten van H13 met nieuwe hooks om CPC onder €0,50 te krijgen, 10% experiment: H11 pauzeren en budget verschuiven naar nieuwe adset of LP-test om H12's conversiegat te diagnosticeren.

### Google Sheet

Niet geschreven — stap 6 overgeslagen conform regels (alleen Meta/PostHog MCP). Rapport lokaal opgeslagen: `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-04-19_ads_report.md`

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

The local branch has 49 commits while origin has 90 different commits - a significant divergence. This needs your decision, I'm not going to auto-resolve this. The report is committed locally but not yet pushed.

Status:
- ✅ Report saved to `Output/Reports/Daily/2026-04-18_sybb_report.md`
- ✅ Committed locally (commit `01d8b16`)
- ❌ Push blocked: branches have diverged (49 local vs 90 remote commits). Rebase hit conflicts in auto-sync log files.

**Report summary:**
- Meta Ads: €94,47 spend, CTR 2,36%, CPC €0,62, 152 clicks, 78 LPV, 7 Initiate Checkouts, **? purchases (verifieer Wix)**
- Top red flag: 7 IC → ? purchases (verifieer Wix) (7d baseline was 27% conversie) — likely checkout/payment issue
- H11 slokt 71% van het budget tegen CPC €0,73; H12 is efficiëntst (CPC €0,38, CTR 4,21%) maar krijgt slechts 13%
- PostHog MCP niet beschikbaar in deze sessie — LP health sectie leeg, cross-reference beperkt

**Aanbevolen:** los de git divergentie handmatig op (bijvoorbeeld `git merge origin/main` met conflict resolution op logs/), of geef akkoord om de merge te doen.

---

Rapport opgeslagen: `Output/Reports/Daily/2026-04-19_auto_optimize.md`.

**Samenvatting:**
- **0 ads gepauzeerd** — alle 3 actieve ads (H11, H12, H13) passen de kill-regels op Link CTR (>0,8%) en zijn nog onder de 500-link-click-drempel voor CPC-kill.
- **Budget mismatch:** H11 verbruikt 73,2% van de spend (€174,87) met zwakste economics (Link CTR 1,25%, CPC €1,16). H12 is de winner (Link CTR 2,11%, CPC €0,65, 6 IC / 44 clicks = 13,6% IC-rate) maar krijgt slechts 12,0% budget.
- **Waarschuwing:** H11 trekt richting CPC-kill-drempel; met huidige spend bereikt hij binnen 7–10 dagen de 500 link clicks — bij volgende run kan kill triggeren.
- **Voorstellen (wachten op jouw goedkeuring):** adset-budget cap op Kopie 1 (H11) + floor op Kopie 2 (H12), variaties op H12-hook, audience-uitbreiding voor Kopie 2 (reach slechts 1.071).

Laat weten welke voorstellen je wilt uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 503,89 | 410 | 0 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 151,75 | 192 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 184,73 | 179 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.015,48** | **1000** | **0** | **0** | **EUR 0,00** | **-** | **-** |

> Wix orders: 0 orders in periode. Update `data/wix-orders.json` met orders uit Wix admin.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
