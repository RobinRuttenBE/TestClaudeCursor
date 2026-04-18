# Morning Report — 2026-04-18

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,10%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,01** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 83,72** over 11 actieve dagen (niet totaal/30)
> - Bron: spend EUR 920,88 · impressions 82.616 · link_clicks 910
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
> | H11, B3, CTA5 | EUR 436,37 | 32.892 | 355 | 1,08% | EUR 1,23 |
> | H13,B3,CTA5 | EUR 170,14 | 14.291 | 162 | 1,13% | EUR 1,05 |
> | H12,B3,CTA5 | EUR 124,88 | 12.929 | 154 | 1,19% | EUR 0,81 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 2026-04-18

**Periode:** last_30d (2026-03-19 t/m 2026-04-17). Alleen `act_567892422940728` had spend. Account `act_607231713057715` is niet toegankelijk via de API token.

### Overzicht per campagne

| Campagne | Status | Spend | Imp. | Clicks | CTR | CPC | CPM | Purch. | ROAS* |
|----------|--------|-------|------|--------|-----|-----|-----|--------|-------|
| 2026: SYBB | Active | €920,88 | 82.616 | 1.721 | 2,1% | €0,54 | €11,15 | 6 | n.v.t. (pixel datafout) |

*Action_value purchase €44.247, verifieer bij Shopify/Stripe.

### Top performers

- **Meeste purchases:** H11, B3, CTA5 (POC Kop), ? purchases (verifieer Wix), €436 spend
- **Beste CTR op volume:** H12, B3, CTA5 (POC Kop), 2,5%
- **Laagste CPC op volume:** H12, B3, CTA5 (POC Kop), €0,39

### Underperformers

- **H11 (POC Kop)** CPC €0,66, boven drempel, maar enige volumedriver met purchases. Houd lopen, test een variant.
- **H13 (POC Kop)** CPC €0,61, ? purchases (verifieer Wix). Verschuif budget naar H12 als geen 3e purchase in 7 dagen.
- **H14 (POC)** ? purchases (verifieer Wix) op €122, CTR 1,8%. Niet heractiveren zonder creative refresh.

### Samenvatting

- **Totaal spend:** €920,88
- **Aanbeveling (70-20-10):** 70% naar H11 Kop, 20% naar H12/H13 Kop variaties, 10% nieuwe hooktest Batch 3. Pauseer H14 permanent. Verhoog budget op POC Kop adset met 25% zolang CPC <€0,70 en frequency <2,5.
- **#1 actie:** grootste funnel lek is LPV naar ATC (706 → 38 = 5,4%). Ads werken, landing page converteert te weinig.

**Google Sheet:** overgeslagen per instructie. Rapport opgeslagen op `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-04-18_ads_report.md`.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen: `Output/Reports/Daily/2026-04-17_sybb_report.md`.

**Kernpunten 2026-04-17:**
- **Meta Ads:** €86,54 spend, CTR 2,32%, CPC €0,62 (24% boven target). Volume ↓32% vs 7d avg.
- **H12 is duidelijke winnaar** (CTR 4,24%, CPC €0,32) maar krijgt slechts 10% van de spend; H11 eet 76% met middelmatige prestaties.
- **Landing page alarm:** bounce 84,6%, sessieduur 16,9s, 68% scrollt niet voorbij 25%. Grootste lek zit tussen landing en 50% scroll.
- **Funnel gap:** 5 "Go to workshop" clicks, maar slechts 1 `/booking` pageview — mogelijk tracking issue.
- **Top 3 acties:** budget naar H12, hero-sectie diagnose via session recordings, CTA→/booking tracking valideren.

---

Rapport opgeslagen. Samenvatting:

**Geen ads gepauzeerd** — alle 3 actieve ads in campagne "2026: SYBB" zitten boven de kill-drempels (Link CTR >0,8%; CPC (link) kill-regel niet van toepassing, want geen ad heeft nog ≥500 link clicks in 3 dagen).

**Campagne 3-daagse performance:** €219,11 spend, Link CTR 1,2%, CPC (link) €1.10,ROAS n.v.t. (pixel datafout) op €1.473,50 revenue.

**Top performer:** H11,B3,CTA5 levertROAS n.v.t. (pixel datafout) (€169.56 → €1.473,50). Krijgt 77% van budget — Meta optimaliseert correct.

**Beste Link CTR:** H12,B3,CTA5 op 1,8% met CPC (link) €0.67, maar nog geen purchases.

**Voorstellen (wacht op goedkeuring):** variaties op H11-winner, variaties op H12 voor conversie-push. Geen budget-shifts uitgevoerd.

Rapport: `Output/Reports/Daily/2026-04-18_auto_optimize.md`

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 436,37 | 355 | 1 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 139,25 | 174 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 170,15 | 162 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 920,88** | **910** | **1** | **0** | **EUR 0,00** | **-** | **-** |

> Wix orders: 0 orders in periode. Update `data/wix-orders.json` met orders uit Wix admin.

> **ONGEMATCHTE /thank-you SESSIES:**
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
