# Morning Report — 2026-05-03

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

## Meta Ads Rapport — 2026-05-03

**Periode**: last 30 days (2026-04-03 t/m 2026-05-02) | **Account**: Sempertex Ad Account
**Status**: Geen ACTIVE campagnes. Onderstaande data is van PAUSED SYBB campagnes met activiteit in last_30d.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Init. Checkout | ROAS* |
|----------|--------|-------|-------------|--------|-----|-----|-----|----------------|-------|
| 2026: SYBB | PAUSED | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 33 (6 purch.) | n.v.t. (pixel datafout) ⚠ |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 6 (0 purch.) | n.v.t. |

*Pixel rapporteert €44.? purchases (verifieer Wix) value op campagne-niveau (€7.374/purchase) — duidt op een tracking-anomalie. Validatie nodig vóór beslissingen op ROAS.

### Underperformers
- **2026: SYBB - Kopie** (campagne) — CPC €0,64, CPM €16,34, ? purchases (verifieer Wix) → pauzeer of refresh.
- **H13,B3,CTA5 (Kopie 3, SYBB-Kopie)** — CPC €0,93, CPM €19,14 → uit-zetten.
- **H11, B3, CTA5 (SYBB hoofd)** — €521 spend, CPC €0,67 → grootste budget-vreter, verlaag of test nieuwe hook.

### Top performers
- **Beste CTR (met volume)**: H12,B3,CTA5 (Expertise & POC) — 4,7% bij 1.058 impr.
- **Laagste CPC (met volume)**: H12,B3,CTA5 (Kopie 2, SYBB) — €0,40 op 13.955 impr.
- **Hoogste conversievolume**: H11,B3,CTA5 (Kopie 1, SYBB) — ? purchases (verifieer Wix).

### Aanbeveling (Hormozi 70-20-10)
1. **70% schaal winnaars**: H12 en H14 hooks behouden bij herstart.
2. **20% variaties** op H12/H14 (andere body, CTA).
3. **10% experiment**: H15 (kleine sample, 6,4% CTR) verder testen.
4. **Eerst tracking-audit doen** — pixel attribution errors (€42.773 op één ad) verstoren ROAS-leesbaarheid.

### Google Sheet
Niet geschreven — strikte run-regels (Meta + PostHog MCP only). Stap 6 overgeslagen.

### Output bestand
`/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-03_ads_report.md`

---

> **Wil je funnel data toevoegen?** Geef de landing page metrics uit Wix Analytics of GA4.
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-02_sybb_report.md`.

**Twee belangrijke vaststellingen:**

1. **Geen Meta Ads activiteit op 2026-05-02.** Campagne "2026: SYBB" (`120239435987290239`) staat PAUSED sinds 2026-04-19 — laatste activiteitsdag bevestigd via `last_30d` met daily breakdown. Spend, impressions, clicks zijn allemaal nul voor gisteren én voor het rolling 7-daags venster.

2. **PostHog MCP niet aanwezig in deze sessie.** De skill verwacht hem (`mcp__posthog__*`) maar hij staat niet in de beschikbare tools. Ik heb de Landing Page Health en Funnel Drop-off secties leeg gelaten met expliciete `⚪ data ontbreekt` markering in plaats van te raden of te improviseren.

Het rapport bevat als referentie de laatste actieve 7-daagse periode (2026-04-13 → 2026-04-19: €594 spend, 941 clicks, CTR 2,2%, CPC €0,63). De drie acties die voorrang hebben: relaunch-beslissing, pixel/attributie audit (de €44k purchase value anomalie uit het 2026-05-03 rapport is nog onopgelost), en PostHog MCP herstellen zodat dit dagelijkse rapport weer compleet kan draaien.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-03_auto_optimize.md`.

**Korte samenvatting:**
- **Geen Niveau 1 acties uitgevoerd** — alle campagnes in beide toegankelijke accounts (`act_567892422940728`, `act_1489853856181844`) zijn PAUSED. Geen impressions, geen spend in afgelopen 3 dagen.
- **Geen 70-20-10 classificatie** mogelijk zonder actieve ads.
- **Geen Niveau 2 voorstellen** mogelijk zonder live data — het rapport stelt alleen een strategische keuze voor: hervat `2026: SYBB`, lanceer iets nieuws, of bewust off-air laten.
- `act_607231713057715` is **niet toegankelijk** met huidige token (alleen `act_1489853856181844` en `act_567892422940728` zijn toegestaan) — overweeg dit uit de skill-defaults te halen.
- PostHog niet geraadpleegd — zonder ad-traffic is er niks om te kruisen.

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
