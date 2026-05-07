# SYBB Daily Report, 6 mei 2026

## 1. Samenvatting
Campagne **2026: SYBB** stond gisteren PAUSED (sinds 19 april), dus geen Meta Ads spend en geen paid traffic. Landing page kreeg 4 pageviews van 2 organic visitors (Instagram bio + Facebook bio), waarvan **1 sessie tot /checkout doorklikte**. Volume in lijn met 7d gemiddelde (~4 PV/dag), maar alle data dit weekend is organic only.

## 2. Meta Ads Performance

| Metric | Gisteren (5/6) | 7d gem. (4/29 t/m 5/5) | Trend |
|--------|----------------|------------------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

> Campagne **2026: SYBB** (id `120239435987290239`) en **2026: SYBB - Kopie** (id `120243293329420239`) staan beide PAUSED. Laatste spend op 2026-04-19 (€43,81). Geen actieve ads, geen Meta-getriggerde traffic vanaf eind april.

### Ad Variant Performance
Geen actieve ads gisteren. Voor referentie het laatste actieve venster (8 t/m 19 april) op campagneniveau:
- Totaal **€1.059,47** spend / 91.839 impressions / 1.935 clicks / CTR 2,11% / CPC €0,55 / freq 1,45.
- Beste day: 11 april (€138 spend, 2 purchases, CPC €0,48, CTR 1,96%).
- Best performance per ad-variant zit in `Output/Reports/Daily/2026-05-07_ads_report.md` (H11 en H13 als enige conversion-driving variants, H15 als laagste CPC validator).

## 3. Landing Page Health (www.startyourballoonbusiness.com)

| Metric | Gisteren | 7d gem. | Target | Status |
|--------|----------|---------|--------|--------|
| Pageviews | 4 | 4,1/dag | meten | meten |
| Unique visitors | 2 | 3,0/dag | meten | meten |
| Sessions | 2 | 3,0/dag | meten | meten |
| Bounce rate (single-PV sessions) | 0% (0/2) | n.v.t.* | <55% | groen (klein sample) |
| Avg session duration | 75s | n.v.t.* | >90s | geel |
| Scroll depth 25/50/75/100% | geen data | geen data | meten | rood: niet getrackt |
| CTA click rate | n.v.t. | n.v.t. | >4% | meten |
| /checkout reach | 1 sessie (50%) | n.v.t. | meten | groen |

*7d gemiddelde voor session-niveau metrics niet apart berekend, sample is te klein om betrouwbaar te middelen.

### Sessies van 6 mei (detail)
| Sessie | Bron | UTM | Path | Pageviews | Duration |
|--------|------|-----|------|-----------|----------|
| 13:32 | instagram | sybb / bio_link | / | 2 | 73s |
| 18:38 | facebook | sybb / bio_link | / | 2 | 77s |

Eén van deze 2 sessies kwam tot **/checkout**. Andere bleef op `/`.

### 7d traffic mix (4/29 t/m 5/5)
| Bron | UTM | Pageviews |
|------|-----|-----------|
| instagram organic | sybb / bio_link | 13 |
| direct (geen UTM) | n.v.t. | 13 |
| facebook organic | sybb / bio_link | 5 |
| meta cpc | sybb / h13_b3_cta5 | 2 |

> Die 2 paid PVs op `h13_b3_cta5` zijn waarschijnlijk delayed/late attribution clicks van vóór de pauze.

## 4. Funnel Drop-off
Met n=2 sessies is dit indicatief, geen statistiek.

```
Pageview op /            (100% — 2 sessies)
        ↓ 50% drop
Tweede pageview          ( 50% — 1 sessie naar /checkout)
        ↓ onbekend
CTA click / form submit  ( 1 autocapture event, niet gelabeld)
        ↓ onbekend
/booking pageview        ( 0 — komt niet voor)
```

**Grootste lek:** niet zinvol vast te stellen op 2 sessies. Grootste structurele lek is dat de **traffic-bron zelf droog staat** (campagne PAUSED).

## 5. Rode Vlaggen
- **Campagne PAUSED sinds 19 april.** Gisteren = dag 17 zonder paid traffic. Organic Insta/FB bio levert ~3 visitors/dag, te weinig om iets data-driven te valideren.
- **Scroll depth wordt niet getrackt** in PostHog voor deze site. Geen `$pageleave` met scroll-percentage en geen custom scroll events. Hierdoor kunnen we Hero/Sectie performance niet meten zodra je weer gaat schalen.
- **CTA tracking ontbreekt of is incompleet.** 1 `$autocapture` event op de hele dag, niet gelabeld als specifieke CTA. Zonder benoemde events kun je CTA click rate niet rapporteren.
- **`/checkout` pageview zonder vervolg.** Iemand bereikte checkout maar er is geen `purchase`/`booking_complete` event. Of de funnel breekt op checkout, of het event wordt niet gefired.

## 6. Top 3 Acties voor Vandaag
1. **Beslis: campagne reactiveren of pauze verlengen.** De ads-rapportage van 7 mei adviseerde H11 en H13 te reactiveren met +50% budget en H15 een €100 validatie-test te geven (zie `2026-05-07_ads_report.md`). Zonder paid traffic levert deze daily report geen meetbare signaal. **Wat:** ga/no-go besluit. **Hoe:** Meta Ads Manager, H11 en H13 unpause, H15 nieuwe ad set met €100 cap. **Verwachte impact:** terug naar ~€100/dag spend en ~150 LPVs/dag waarmee de funnel weer testbaar wordt. **Escalatie:** Geel (Robin goedkeuring).
2. **Fix tracking: scroll depth + CTA click events op startyourballoonbusiness.com.** Voeg PostHog autocapture rules toe of fire custom events op CTA-knoppen (`cta_click_book_now`, `cta_click_pricing`) en op scroll thresholds (25/50/75/100%). **Waarom:** zonder dit kun je ad-page mismatch niet diagnoseren wanneer je weer schaalt. **Hoe:** Wix custom code injectie of PostHog dashboard event-rule. **Verwachte impact:** vanaf eerste re-launch dag valide LP-health metrics in dit rapport. **Escalatie:** Oranje (Wix Editor + dev werk).
3. **Onderzoek de ene `/checkout`-sessie van gisteren.** Eén Instagram bio-visitor klikte door naar /checkout zonder dat er een purchase event volgde. **Wat:** session recording bekijken (als beschikbaar) en checken of pixel/booking complete event fired. **Hoe:** PostHog session replays voor session_id `019dfe95-6e19-72b3-8d18-a1f7e62523f9` of `019dfd7c-f574-729f-91cf-f2d401b01a6e`. **Verwachte impact:** ofwel een gemiste conversie (technisch lek) ofwel een micro-signaal dat de organic bio-flow nog werkt. **Escalatie:** Groen (auto onderzoek).

---

### Data bronnen
- Meta Ads via Pipeboard MCP, account `act_567892422940728` (Sempertex Ad Account), campaign `2026: SYBB` (`120239435987290239`).
- PostHog via MCP, project "Default project" (id 149694), host `www.startyourballoonbusiness.com`.
- Window: 2026-05-06 00:00 t/m 2026-05-07 00:00 UTC voor "gisteren"; 2026-04-29 t/m 2026-05-05 voor 7d gemiddelde.
- Geen Google MCPs gebruikt (geen Sheet write).
