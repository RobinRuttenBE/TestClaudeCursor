# Morning Report — 2026-04-20

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
> - Bron: spend EUR 1059,46 · impressions 91.838 · link_clicks 1.036
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
> | H11, B3, CTA5 | EUR 521,55 | 38.613 | 428 | 1,11% | EUR 1,22 |
> | H13,B3,CTA5 | EUR 206,99 | 16.766 | 195 | 1,16% | EUR 1,06 |
> | H12,B3,CTA5 | EUR 141,43 | 13.955 | 174 | 1,25% | EUR 0,81 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 2026-04-20

Periode: last_30d. Één actieve campagne gevonden: **2026: SYBB - Kopie** (live sinds 2026-04-19). Account `act_607231713057715` niet toegankelijk via token, overgeslagen.

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. (IC) | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|------------|------|
| 2026: SYBB - Kopie | Active | €45,65 | 3.320 | 75 | 2,3% | €0,61 | €13,75 | 4 | n.v.t. (pixel datafout) |

ROAS is op `initiate_checkout` action values (€1.400), niet op daadwerkelijke purchases.

### Underperformers

- **H13, B3, CTA5** — CPC €0,79 én CPM €15,79 boven drempel. Aanbeveling: pauzeer, ververs creative.
- **H11, B3, CTA5** — CPC €0,58 (net boven €0,50). Houd draaien, levert 53% van conversies.

### Top performers

- **Beste CTR**: H12, B3, CTA5 — 2,8%
- **Laagste CPC**: H12, B3, CTA5 — €0,48
- **Beste ROAS (IC)**: H12, B3, CTA5 — n.v.t. (pixel datafout)

Geen frequency fatigue (max 1,21).

### Samenvatting

- **Totaal spend**: €45,65 (campagne 1 dag live)
- **Beste performer**: H12 — winnaar op alle drie de kern-KPI's
- **Slechtste performer**: H13 — hoogste CPC/CPM, laagste CTR
- **Aanbeveling (70-20-10)**: budget naar H12 shiften, H11 laten draaien, H13 pauzeren. 13 PAUSED ads vormen de experiment-bucket — selectief activeren na leervenster.

### Google Sheet
Overgeslagen per instructie. Rapport opgeslagen in `Output/Reports/Daily/2026-04-20_ads_report.md`.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-19_sybb_report.md`.

**Samenvatting van de run:**
- Meta Ads data: ✅ opgehaald via Pipeboard MCP voor campagne "2026: SYBB - Kopie" (de originele "2026: SYBB" is PAUSED sinds 19-04 14:29, vervangen door de Kopie die om 14:25 live ging)
- PostHog data: ❌ PostHog MCP is niet beschikbaar in deze tool-omgeving. Sectie 3 en 4 zijn ingevuld met Meta pixel proxies (link click > LPV > IC) en PostHog-velden gemarkeerd als "geen data". Dit is expliciet geflagd in het rapport.
- Google MCPs: ❌ niet aangeroepen, niet geschreven naar Sheets, conform instructie.

**Kerncijfers 2026-04-19:** €45,65 spend, 3.320 impr, 2,26% CTR, €0,61 CPC, 37 LPV, 4 IC. H12 beste CTR/CPC, H13 zwakste.

---

Rapport opgeslagen. Samenvatting:

**Actieve ads:** 3 (alle in campagne `2026: SYBB - Kopie`, act_567892422940728)
**Gepauzeerd:** 0 — alle ads boven kill-drempels of nog onder minimum data (1.000 imp)
**Waarschuwing:** 1 — `H13,B3,CTA5` CPM €15.79 (>€15, dure reach)
**70-20-10:** geen Core winners, 2 Emerging (H11, H13), 1 Experimental (H12)
**Voorstellen:** budget laten staan tot 2026-04-22; variaties op H13 + H11 pas klaarzetten bij 2.000 imp/hook; audience-uitbreiding H13 als CPM >€15 blijft

Output: `Output/Reports/Daily/2026-04-20_auto_optimize.md`

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,55 | 428 | 0 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.059,46** | **1036** | **0** | **0** | **EUR 0,00** | **-** | **-** |

> Wix orders: 0 orders in periode. Update `data/wix-orders.json` met orders uit Wix admin.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
