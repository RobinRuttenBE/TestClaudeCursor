# SYBB Daily Report -- 14 april 2026

## 1. Samenvatting

Matige dag voor SYBB. Het volume is flink gedaald: impressions -23% en clicks -21% vs het 7-daags gemiddelde. De CPC is gestegen naar EUR 0.62 (boven het target van EUR 0.50). Grootste zorgpunt blijft de extreem hoge bounce rate van 82.7%, ver boven het target van 55%. Positief: de CTA click rate op de landing page was sterk (16.3%), en H12 presteert uitstekend met de laagste CPC en hoogste CTR. De /booking bezoeken zijn echter met 38% gedaald vs het 7d gemiddelde.

## 2. Meta Ads Performance

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | EUR 95.93 | EUR 100.25 | -> |
| Impressions | 7,292 | 9,466 | v |
| Clicks (all) | 154 | 193.7 | v |
| Link Clicks | 83 | 101.6 | v |
| CTR | 2.11% | 2.05% | -> |
| CPC | EUR 0.62 | EUR 0.52 | ^ |
| LP Views | 63 | 77.9 | v |
| Frequency | 1.53 | 1.92 (7d totaal) | OK |
| Add to Cart | 2 | 3.7 | v |
| View Content | 7 | 7.0 | -> |

### Ad Variant Performance (Gisteren)

| Ad (utm_content) | Spend | Imp | Link Clicks | CTR | CPC | LP Views | View Content | ATC |
|-------------------|-------|-----|-------------|-----|-----|----------|-------------|-----|
| H11, B3, CTA5 | EUR 63.51 | 4,903 | 55 | 2.04% | EUR 0.64 | 40 | 4 | 0 |
| H13, B3, CTA5 | EUR 23.57 | 1,792 | 19 | 2.01% | EUR 0.65 | 14 | 2 | 0 |
| H12, B3, CTA5 | EUR 8.85 | 597 | 9 | 3.02% | EUR 0.49 | 9 | 1 | 2 |

### Ad Variant Performance (7d Totaal)

| Ad (utm_content) | Spend | Link Clicks | LP Views | Cost/LP View | View Content | ATC | Purchases |
|-------------------|-------|-------------|----------|-------------|-------------|-----|-----------|
| H11, B3, CTA5 | EUR 266.80 | 213 | 165 | EUR 1.62 | 22 | 13 | 0 |
| H13, B3, CTA5 | EUR 142.66 | 138 | 117 | EUR 1.22 | 13 | 6 | 2 |
| H12, B3, CTA5 (Kopie 2) | EUR 102.81 | 121 | 98 | EUR 1.05 | 8 | 4 | 0 |
| H14, B3, CTA5 | EUR 122.96 | 158 | 108 | EUR 1.14 | 3 | 0 | 0 |
| H15, B3, CTA5 (Kopie 4) | EUR 49.83 | 57 | 36 | EUR 1.38 | 2 | 1 | 0 |
| H12, B3, CTA5 (origineel) | EUR 14.37 | 20 | 18 | EUR 0.80 | 1 | 2 | 0 |
| H15, B3, CTA5 (origineel) | EUR 2.32 | 4 | 3 | EUR 0.77 | 0 | 0 | 0 |

**Beste variant gisteren:** H12, B3, CTA5. Hoogste CTR (3.02%), laagste CPC (EUR 0.49), en als enige 2 add-to-carts. Krijgt echter slechts 9% van het budget.

**Slechtste variant gisteren:** H13, B3, CTA5. Laagste CTR (2.01%), hoogste CPC (EUR 0.65), geen conversies.

**7d winnaar op conversie:** H13 heeft 2 purchases (enige variant met purchases), maar H11 leidt in add-to-carts (13) en initiate checkouts (13).

## 3. Landing Page Health (PostHog)

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 134 | 175.7/dag | n.v.t. | v |
| Unique Visitors | 100 | 119.1/dag | n.v.t. | v |
| Sessions | 104 | 130.4/dag | n.v.t. | v |
| Bounce Rate | 82.7% | 81.9% | <55% | ROOD |
| CTA Click Rate | 16.3% | 11.1% | >4% | GROEN |
| /booking Bezoeken | 13 | 20.9/dag | n.v.t. | v |
| Avg Session Duration | n.b. | n.b. | >90s | ? |
| Scroll Depth | n.b. | n.b. | >60% | ? |

### UTM Segmentatie (Gisteren, PostHog)

| UTM Content | Pageviews | Sessions | Unieke Bezoekers | Pag/Sessie |
|-------------|-----------|----------|-------------------|------------|
| h11_b3_cta5 | 76 | 62 | 61 | 1.23 |
| h13_b3_cta5 | 33 | 26 | 25 | 1.27 |
| h12_b3_cta5 | 11 | 8 | 7 | 1.38 |
| bio_link | 8 | 6 | 6 | 1.33 |
| (direct/geen UTM) | 6 | 4 | 4 | 1.50 |

### CTA Click Breakdown (Gisteren)

| Knooptekst | Clicks |
|------------|--------|
| Explore Options | 5 |
| booking link | 5 |
| Go to workshop | 4 |
| Book This Date! | 2 |
| Add to Cart | 1 |
| FAQ items | 6 |
| Overig/null | 31 |

## 4. Funnel Drop-off

```
LP Pageview (104 sessions, 100%)
    |
    v  83.7% verliest
CTA Click (17 clicks, 16.3%)
    |
    v  23.5% verliest
/booking Pageview (13 bezoeken, 12.5%)
    |
    v  76.9% verliest
Booking Action (3 acties, 2.9%)
```

**Grootste lek:** LP Pageview naar CTA Click. 83.7% van de bezoekers verlaat de pagina zonder interactie. Dit komt overeen met de 82.7% bounce rate. De hero sectie en eerste zichtbare content slagen er niet in om bezoekers vast te houden.

## 5. Cross-Reference Analyse

### Ad CTR vs LP Bounce
- H11: CTR 2.04% + hoge LP traffic (62 sessions) maar bounce rate structureel hoog (82.7% gemiddeld)
- Conclusie: de ads trekken klikkers, maar de landing page matcht niet met de verwachting die de ad wekt

### Ad CPC vs LP Conversie
- H12 heeft de laagste CPC (EUR 0.49) EN de hoogste pagina's/sessie (1.38). Dit wijst op betere audience-match.
- H11 heeft de hoogste CPC (EUR 0.64) maar domineert 66% van het budget, waardoor het totale CPC omhoog wordt getrokken.

### Volume vs Engagement
- Ondanks dalend volume (impressions -23%) is de CTA click rate gestegen naar 16.3% (vs 11.1% 7d avg). Minder, maar kwalitatief betere bezoekers? Of toeval door lage aantallen.

### Frequency vs Bounce
- Frequency gisteren (1.53) is lager dan 7d totaal (1.92). Geen direct ad fatigue signaal.

## 6. Rode Vlaggen

1. **KRITIEK: Bounce Rate 82.7%** (target <55%, al 7 dagen boven 80%). De landing page verliest meer dan 4 op 5 bezoekers direct. Dit is het grootste probleem in de hele funnel.

2. **CPC EUR 0.62 > EUR 0.50 target.** Stijging van 19.2% vs 7d gemiddelde. Bijna op het 20% alarm-niveau. H11 en H13 zijn de duurste varianten.

3. **Volume daalt:** Impressions -23%, clicks -21% vs 7d gemiddelde. Minder bereik = minder kansen.

4. **/booking bezoeken -38%:** Van 20.9/dag gemiddeld naar 13 gisteren. Minder mensen bereiken de boekingspagina.

5. **H11 domineert budget onnodig:** 66% van de spend gaat naar H11, terwijl H12 betere metrics heeft op CTR, CPC en conversie per euro.

## 7. Top 3 Acties voor Vandaag

### 1. Landing page hero sectie herzien (URGENT)
- **Wat:** Herwerk de above-the-fold content op startyourballoonbusiness.com. Meer specifieke waardepropositie, sterkere visuele hook, directe problem-identification.
- **Waarom:** 82.7% bounce rate. Bezoekers beslissen binnen 3 seconden dat de pagina niet relevant is.
- **Hoe:** Wix Editor. Test een variant met: specifiekere headline (niet generiek "start your balloon business" maar een concreet resultaat/probleem), social proof boven de vouw, en een duidelijke "wat krijg je" sectie.
- **Verwachte impact:** Bounce rate naar <70% zou /booking bezoeken verdubbelen.
- **Escalatie:** Oranje (Wix Editor)

### 2. Budget herverdelen: meer naar H12, minder naar H11
- **Wat:** Verschuif minimaal 30% van H11's budget naar H12. H12 heeft de beste CTR (3.02%), laagste CPC (EUR 0.49), en meeste add-to-carts relatief aan spend.
- **Waarom:** H11 pakt 66% van het budget met de hoogste CPC. H12 is 23% goedkoper per klik en converteert beter.
- **Hoe:** Meta Ads Manager, ad set budgets aanpassen.
- **Verwachte impact:** Gemiddelde CPC daling naar <EUR 0.55, meer conversies per euro.
- **Escalatie:** Geel (Robin goedkeuring)

### 3. PostHog scroll depth en session recording tracking verbeteren
- **Wat:** Zorg dat scroll depth events en session duration correct worden gelogd in PostHog.
- **Waarom:** Scroll depth en session duration data is niet beschikbaar, waardoor we niet kunnen diagnosticeren WAAR op de pagina bezoekers afhaken.
- **Hoe:** PostHog snippet configuratie checken, custom events voor scroll milestones toevoegen.
- **Verwachte impact:** Betere diagnose, gerichtere LP optimalisaties.
- **Escalatie:** Groen (technisch, zelfstandig uit te voeren)

---

*Rapport gegenereerd: 15 april 2026*
*Databronnen: Meta Ads MCP (Pipeboard), PostHog MCP*
*Periode: 14 april 2026 (met 7d vergelijking 8-14 april)*
