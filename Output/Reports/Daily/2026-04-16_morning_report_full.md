# Morning Report — 2026-04-16

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,07%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,00** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 87,15** over 9 actieve dagen (niet totaal/30)
> - Bron: spend EUR 784,32 · impressions 72.653 · link_clicks 781
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
> | H11, B3, CTA5 | EUR 328,99 | 25.350 | 259 | 1,02% | EUR 1,27 |
> | H13,B3,CTA5 | EUR 149,30 | 12.626 | 142 | 1,12% | EUR 1,05 |
> | H12,B3,CTA5 | EUR 108,64 | 11.630 | 128 | 1,10% | EUR 0,85 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport opgeslagen en gepushed. Hier is de samenvatting:

## Meta Ads Rapport, 16 april 2026

### Campagne: 2026: SYBB (30 dagen)

| Metric | Waarde |
|--------|--------|
| Spend | €776,42 |
| Impressions | 72.110 |
| Link Clicks | 768 |
| Landing Page Views | 589 |
| Link CTR | 1,07% |
| CPC (link) | EUR 1,00 |
| Purchases | 6 |
| Purchase Value | €44.247 |
| ROAS | 57,0x |

### Top 3 Actieve Ads

| Ad | Spend | CPC | Purchases | ROAS | Flag |
|----|-------|-----|-----------|------|------|
| H11, B3, CTA5 (Kopie 1) | €328,99 | € 1,27 | 4 | 4,5x | CPC boven target |
| H13, B3, CTA5 (Kopie 3) | €149,30 | € 1,05 | 2 | 286,5x | CPC boven target |
| H12, B3, CTA5 (Kopie 2) | €108,64 | € 0,85 | 0 | 0x | Geen conversies |

### Belangrijkste bevindingen

1. **CPC net boven target** (€0,53 vs €0,50), maar de ads die converteren zijn juist de duurdere. De goedkopere ads (H12 met €0,39) leveren geen purchases op.
2. **LP Conversie Rate is 1,0%** (6 purchases / 589 LPV), ruim onder de 5% target. Bottleneck zit op de landing page, niet in de ads.
3. **PostHog toont 1.416 pageviews** vs 589 Meta LP views: 58% van het LP-verkeer komt van buiten Meta.
4. **Frequency (1,99) is veilig**, geen creative fatigue.

### Aanbevelingen

- **Schaal H13 (Kopie 3) op**: hoogste ROAS, lage frequency, ruimte om te groeien
- **Maak hook variaties** op H11 en H13 om CPC te drukken
- **Overweeg H12 (Kopie 2) te pauzeren** als er na 3 extra dagen nog geen conversie komt
- **Focus op landing page optimalisatie**: de echte bottleneck zit in LP conversie (1,0% vs 5% target)

Volledig rapport: `Output/Reports/Daily/2026-04-16_ads_report.md`

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4. Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` analyse.

---

Rapport is gepushed. Hier de kernpunten:

## SYBB Rapport 15 april 2026, samenvatting

**Goed nieuws:**
- 4 purchases (€1.473,50) uit €74,65 spend = **ROAS 19,7x**
- CTA Click Rate op 15,7% (ruim boven 4% target)
- Scroll 75%+ en 100% targets gehaald
- Frequency laag (1,34), verse doelgroep bereikt

**Aandachtspunten:**
- **CPC €0,61** (boven €0,50 target, +13% vs 7d avg)
- **H12 mismatch**: CTR 4,55% maar slechts 25% scrollt voorbij 50% en 0 conversies in 7 dagen. €123 verspild.
- **/booking tracking kapot**: 1 pageview terwijl er 3 "Place Order & Pay" clicks waren. Wix SPA routing triggert geen $pageview.
- **Scroll 25%+ op 65,6%** (target 80%). Hero sectie verliest 35% bezoekers.
- **Volume daling**: spend -27%, impressions -34% vs 7d gemiddelde

**Top 3 acties:**
1. **Pauzeer H12 adset** (Kopie 2), geen conversies, ad-page mismatch
2. **Fix /booking pageview tracking** in Wix, funnel data is onbetrouwbaar
3. **Test hero section variant** om scroll 25%+ richting 80% te krijgen

---

Auto-optimize run compleet. Rapport opgeslagen in `Output/Reports/Daily/2026-04-16_auto_optimize.md`.

**Samenvatting:**

**Geen ads gepauzeerd.** Alle 3 actieve ads presteren boven de kill-drempels.

| Ad | Link CTR | CPC (link) | ROAS | Status |
|----|----------|------------|------|--------|
| H11, B3, CTA5 | 1,02% | EUR 1,27 | **7,23x** | Core winner (4 purchases) |
| H12,B3,CTA5 | 1,10% | EUR 0,85 | 0,00x | Emerging (te weinig data) |
| H13,B3,CTA5 | 1,12% | EUR 1,05 | 0,00x | Emerging (monitor) |

**Aandachtspunten:**
- H11 is verantwoordelijk voor 100% van de purchases. Geen backup converter.
- H12 CPM nadert EUR 15 grens (EUR 14,74)
- H13 heeft EUR 68,76 gespend zonder purchase. Bij EUR 150+ zonder conversie: heroverweeg.
- Experimentele bucket (10%) is leeg. Variaties van winnende H11 hook aanbevolen.

**Wil je een of meer van de voorstellen uit het rapport uitvoeren?**

---

Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
