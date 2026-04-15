# Morning Report — 2026-04-15

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 21386,75** bij 2 purchases (totaal EUR 42773,50).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (15% marge): EUR 297-488 (1 ticket), EUR 595-977 (2 tickets), EUR 892-1465 (3 tickets), etc.
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,07%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 0,99** (spend ÷ link_clicks)
> - Bron: spend EUR 701,77 · impressions 66.263 · link_clicks 711
> Dit zijn de ENIGE betrouwbare CTR/CPC cijfers in dit rapport. Kale `CTR`/`CPC` in campagne-summary tabellen zijn overschreven met de link-based waarden. Per-ad tabellen bevatten mogelijk nog all-clicks cijfers — controleer dubbel.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport -- 15 april 2026

### Campagne: 2026: SYBB (30 dagen)

| Metric | Waarde |
|--------|--------|
| Spend | EUR 701,77 |
| Impressions | 66.263 |
| Link CTR | 1,07% |
| CPC (link) | EUR 0,99 |
| Purchases | ? (verifieer Wix) |
|ROAS n.v.t. (pixel datafout) |

### 3 actieve ads

| Ad | Spend | CPC | Purch. | Flag |
|----|-------|-----|--------|------|
| H11, B3, CTA5 | EUR 266,81 | EUR 0,66 | 0 | CPC te hoog, 0 conversies ondanks 13 IC |
| H13, B3, CTA5 | EUR 142,66 | EUR 0,61 | 2 | CPC hoog maar ENIGE met purchases (ROAS n.v.t. (pixel datafout)) |
| H12, B3, CTA5 | EUR 102,81 | EUR 0,40 | 0 | Beste CPC/CTR, nog geen conversies |

### Kritieke bevindingen

1. **H11 eet 38% van het budget** maar converteert niet, ondanks 13 add-to-carts en 13 initiate checkouts. Er zit een blokkade in de checkout flow.
2. **LP bounce is het #1 probleem.** Van 545 landing page views vuren er maar 49 een view content event (9%). 91% verdwijnt direct.
3. **PostHog bevestigt:** 882 meta pageviews vs. 545 Meta LP views, 65% van al het SYBB traffic komt van Meta.
4. **Frequency 1,92** is prima, geen creative fatigue.

### Top 3 acties
1. **Verschuif budget van H11 naar H13** (enige converterende ad, ROAS n.v.t. (pixel datafout))
2. **Fix de landing page bounce** (91% verlaat zonder engagement, dit is de funnel bottleneck)
3. **Geef H12 meer ruimte** als secondary winner (laagste CPC EUR 0,40, hoogste CTR 2,3%)

Rapport opgeslagen in `Output/Reports/Daily/2026-04-15_ads_report.md` en gepusht naar GitHub.

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4.
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

SYBB rapport voor 2026-04-14 is gegenereerd, opgeslagen en gepushed.

**Belangrijkste bevindingen:**
- CPC €0.62 (boven €0.50 target), impressions -23% vs 7d gemiddelde
- Bounce rate 82.7% (structureel probleem, target is <55%)
- 40% zero-scroll rate, mediaan sessieduur slechts 7s
- H12 is de beste variant (CTR 3.02%, CPC €0.49, 75% bounce) maar krijgt slechts 9% budget
- H13 is de slechtste (88.5% bounce), H11 is het grootste geldlek (66% budget, 84% bounce)
- 10 unieke bezoekers bereikten /booking (9.6% conversie)

**Top acties:** budget verschuiven van H13 naar H12, hero sectie optimaliseren, LP variant testen voor H11 verkeer.

---

## Auto-Optimize Rapport 2026-04-15 klaar

**0 ads gepauzeerd** -- alle 3 actieve ads presteren boven de kill-drempels.

### Key metrics (3d)
| Ad | Link CTR | CPC (link) | Spend | Purchases |
|----|----------|------------|-------|-----------|
| H11 | 0,98% | €1,40 | €220,61 | 0 |
| H12 | 1,19% | €1,16 | €42,96 | 0 |
| H13 | 1,17% | €1,10 | €90,03 | 0 |

### Grootste probleem: budget mismatch wordt erger
- H11 (? purchases (verifieer Wix) lifetime, €313 spend) krijgt nu **62,4%** van budget (was 45% gisteren)
- H13 (enige ad met purchases,ROAS n.v.t. (pixel datafout)) krijgt slechts **25,5%**
- Na pauzering van H14 gisteren stuurt Meta nog meer budget naar H11
- CPC (link) campagne-gemiddeld stijgt: €1,14 naar €1,29

### 5 voorstellen wachten op goedkeuring:
1. **Pauzeer ad set Kopie 1 (H11)** om budget naar H13/H12 te forceren
2. **Checkout flow diagnose** -- H11 heeft 13 IC maar ? purchases (verifieer Wix), er zit een blokkade
3. **Hook variaties** op H13 (enige ad met purchases)
4. **ROAS verificatie** -- zijn H13's ? purchases (verifieer Wix) (€42.773) echte orders?
5. **Audience** -- geen actie nodig, frequency <2.0

Rapport opgeslagen in `Output/Reports/Daily/2026-04-15_auto_optimize.md`. Welke voorstellen wil je uitvoeren?

---

Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
