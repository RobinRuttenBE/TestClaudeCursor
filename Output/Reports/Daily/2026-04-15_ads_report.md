## Meta Ads Rapport -- 15 april 2026

### Campagne: 2026: SYBB (30 dagen)

| Metric | Waarde |
|--------|--------|
| Spend | EUR 701,77 |
| Impressions | 66.263 |
| CTR | 2,0% |
| CPC | EUR 0,52 |
| Purchases | 2 (EUR 42.773,50) |
| ROAS | 60,9x |

### 3 actieve ads

| Ad | Spend | CPC | Purch. | Flag |
|----|-------|-----|--------|------|
| H11, B3, CTA5 | EUR 266,81 | EUR 0,66 | 0 | CPC te hoog, 0 conversies ondanks 13 IC |
| H13, B3, CTA5 | EUR 142,66 | EUR 0,61 | 2 | CPC hoog maar ENIGE met purchases (ROAS 299,8x) |
| H12, B3, CTA5 | EUR 102,81 | EUR 0,40 | 0 | Beste CPC/CTR, nog geen conversies |

### Kritieke bevindingen

1. **H11 eet 38% van het budget** maar converteert niet, ondanks 13 add-to-carts en 13 initiate checkouts. Er zit een blokkade in de checkout flow.
2. **LP bounce is het #1 probleem.** Van 545 landing page views vuren er maar 49 een view content event (9%). 91% verdwijnt direct.
3. **PostHog bevestigt:** 882 meta pageviews vs. 545 Meta LP views, 65% van al het SYBB traffic komt van Meta.
4. **Frequency 1,92** is prima, geen creative fatigue.

### Top 3 acties
1. **Verschuif budget van H11 naar H13** (enige converterende ad, 299,8x ROAS)
2. **Fix de landing page bounce** (91% verlaat zonder engagement, dit is de funnel bottleneck)
3. **Geef H12 meer ruimte** als secondary winner (laagste CPC EUR 0,40, hoogste CTR 2,3%)

Rapport opgeslagen in `Output/Reports/Daily/2026-04-15_ads_report.md` en gepusht naar GitHub.

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4.
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
