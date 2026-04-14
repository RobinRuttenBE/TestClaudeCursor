# SYBB Daily Report — 2026-04-13

## 1. Samenvatting
Spend schoot +62% omhoog naar €140,48 terwijl CPC steeg naar €0,68 (7d avg €0,50). Landing page bounce rate zakte wél van 81,9% (7d) naar 73,4% en avg scroll depth verbeterde naar 60%. Belangrijkste probleem: duurdere clicks + geen purchase op deze dag, met H15 en H12 variants die 80-100% bouncen op de LP.

## 2. Meta Ads Performance

### Campaign Totals
| Metric | Gisteren (13/04) | 7d Daily Avg | Trend |
|---|---|---|---|
| Spend | €140,48 | €86,53 | ↑ +62% |
| Impressions | 9.894 | 8.423 | ↑ +17% |
| Clicks (all) | 208 | 172 | ↑ +21% |
| Link clicks | 109 | 90 | ↑ +21% |
| CTR | 2,10% | 2,04% | → stabiel |
| CPC (all) | €0,68 | €0,50 | ↑ +36% 🚩 |
| Frequency | 1,47 | 1,85 (7d agg) | ↓ lager |
| Landing page views | 86 | 69 | ↑ +25% |
| Add to cart | 8 | 3,4 | ↑ |
| Initiate checkout | 5 | 2,1 | ↑ |
| Purchases | 0 | 0,3 (2 op 7d) | → |

### Ad Variant Performance (gisteren)
| Ad (utm_content) | Impr | Clicks | CTR | CPC | Spend | LP Sessions | LP Bounce |
|---|---|---|---|---|---|---|---|
| h11_b3_cta5 | 5.338 | 105 | 1,97% | €0,74 | €78,14 | 47 | 66,0% 🟡 |
| h13_b3_cta5 | 2.936 | 61 | 2,08% | €0,63 | €38,53 | 38 | 78,9% 🔴 |
| h12_b3_cta5 | 898 | 25 | 2,78% | €0,59 | €14,77 | 10 | 80,0% 🔴 |
| h15_b3_cta5 | 722 | 17 | 2,35% | €0,53 | €9,04 | 9 | 100% 🔴 |

**Beste variant op ad-niveau:** H12 (hoogste CTR 2,78%) en H15 (laagste CPC €0,53). Spend is nog laag dus signaal is zwak.
**Slechtste variant:** H11 vangt 56% van spend maar heeft de hoogste CPC (€0,74) en laagste CTR (1,97%) — slechte cost efficiency ondanks hoogste volume.
**Kritisch signaal:** H15 heeft 100% bounce rate op de LP (alle 9 sessies bouncen). Ad trekt goedkoop aan, LP faalt direct.

## 3. Landing Page Health (startyourballoonbusiness.com)
| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|---|---|---|---|---|
| Pageviews | 178 | ~151/dag | — | — |
| Unique visitors | 105 | — | — | — |
| Sessions | 109 | 116/dag | — | — |
| Bounce Rate | 73,4% | 81,9% | <55% | 🔴 (verbeterd vs 7d) |
| Avg Max Scroll | 60,1% | 44,0% | >60% | 🟢 (verbeterd) |
| Scroll 25% | 65,5% | — | >80% | 🟡 |
| Scroll 50% | 58,6% | — | >60% | 🟡 |
| Scroll 75% | 48,3% | — | >40% | 🟢 |
| Scroll 90% | 43,1% | — | >20% | 🟢 |

**Positieve trend:** avg scroll sprong van 44% (7d) naar 60,1%, beste single-day engagement deze week. Bounce zakte ook 8,5 punten.
**Probleem:** absolute bounce (73,4%) nog ruim boven target <55%.

### Path Distribution (gisteren)
| Path | Pageviews |
|---|---|
| / (LP) | 120 |
| /booking | 38 |
| /product-page (3 varianten) | 15 |
| /checkout | 4 |

**Waarneming:** 38 /booking pageviews vs 120 LP pageviews = ~31,7% van LP-bezoekers klikt door naar /booking. 4 /checkout visits duiden op actief aankoop-intent, maar 0 purchases via Meta Ads pixel op deze dag.

## 4. Funnel Drop-off
```
Meta link clicks (109) → LP session (109) → /booking view (38) → /checkout (4) → Purchase (0)
     100%                   100%              35%                  4%                0%
```

**Grootste lek 1:** LP → /booking = 65% drop. Tweederde van bezoekers klikt niet door naar booking.
**Grootste lek 2:** /booking → /checkout = 89% drop-off. Van 38 bookingpagina bezoeken starten er maar 4 een checkout.
**Kritisch:** /checkout → Purchase = 100% drop-off. Geen enkele checkout voltooid, terwijl de 7d gemiddelde 0,3/dag is (2 op 7 dagen).

## 5. Rode Vlaggen 🚩
- 🚩 **CPC +36% vs 7d avg:** €0,68 vs €0,50. Kostenefficiëntie verslechtert, boven target €0,50 op 30d.
- 🚩 **H11 dominant maar inefficiënt:** pakt 56% van het budget met de slechtste CPC (€0,74) en laagste CTR (1,97%) van de 4 varianten.
- 🚩 **H15 100% bounce:** alle 9 sessies bounceden. Kleine sample, maar pure traffic-to-nowhere.
- 🚩 **H13 + H12 bounce 79-80%:** ook ver boven LP-target <55%.
- 🚩 **0 purchases gisteren** terwijl 4 /checkout visits zijn geregistreerd. Mogelijke checkout-blokkade of pixel drop.
- 🚩 **Spend +62%** zonder conversie-winst: kosten stijgen, attributed revenue staat op 0 voor deze dag.

## 6. Top 3 Acties voor Vandaag

### 1. Budget herverdelen weg van H11 (Escalatie: Geel, Robin goedkeuring)
**Wat:** Verlaag budget op adset "BATCH 2: Expertise & POC - Kopie 1" (H11) met 40-50%, verhoog "Kopie 2" (H12) en "Kopie 4" (H15) adset budgets met het vrijgekomen bedrag.
**Waarom:** H11 pakt 56% van de spend met de slechtste CPC (€0,74) en laagste CTR (1,97%). H12 heeft de hoogste CTR (2,78%) en H15 de laagste CPC (€0,53), maar beide krijgen nu <12% van het budget. Onder-exploited winners, over-spended loser.
**Hoe:** Meta Ads Manager, adset budgets aanpassen. Laat Kopie 3 (H13) voorlopig lopen.
**Verwachte impact:** CPC daling van €0,68 richting €0,55, CTR stijging richting 2,3%.

### 2. H15 + H13 landing page mismatch onderzoeken (Escalatie: Oranje, Wix Editor)
**Wat:** Zoek uit waarom 79-100% van H15, H12 en H13 sessies bounct op de LP. Check welke hook/creative deze varianten gebruiken en of de LP boven-de-vouw dezelfde belofte inlost.
**Waarom:** CTR en CPC zijn gezond op ad-level, maar 0 van 9 H15 sessies scrollt door. Bij H13 78,9% bounce op 38 sessies (grootste signaal). Dit wijst op ad-page mismatch, niet op ad-kwaliteit.
**Hoe:** 1) Check ad creative tegen hero sectie LP per variant. 2) Bekijk session recordings in PostHog van bouncende sessies. 3) Als mismatch bevestigd: hero sectie aanpassen of aparte LP-variant per hook maken.
**Verwachte impact:** bounce rate H13/H15 van 79-100% richting 60%, daarmee LP bounce totaal richting 60%.

### 3. Checkout blokkade diagnosticeren (Escalatie: Rood, Strategie)
**Wat:** Onderzoek waarom 4 /checkout pageviews 0 purchases opleveren, en waarom /booking (38) naar /checkout (4) een 89% drop heeft.
**Waarom:** Dit is de diepste funnel stap en levert de grootste ROI op bij een fix. 0 conversies gisteren terwijl 7d gemiddelde 0,3/dag is. De drop /booking→/checkout van 89% is buitengewoon hoog voor een flow die specifiek voor conversie is gebouwd.
**Hoe:** 1) Bekijk /booking en /checkout session recordings in PostHog. 2) Test zelf de booking flow end-to-end (desktop + mobiel). 3) Check Meta Pixel events voor InitiateCheckout en Purchase firing op /booking en /checkout. 4) Wix booking widget config review.
**Verwachte impact:** elke 1% conversie-verbetering op /booking→/checkout geeft 0,4 extra checkouts/dag = substantieel bij €350 workshop prijs.

---

## Bijlage: Data Notes

- **Data bronnen:** Meta Ads MCP (Pipeboard), campagne ID `120239435987290239` (`2026: SYBB`). PostHog MCP, host `www.startyourballoonbusiness.com`.
- **Scroll metrics:** gebaseerd op 58 `$pageleave` events gisteren. Niet elke sessie vuurt `$pageleave` betrouwbaar, dus sample is kleiner dan session count (109).
- **7d window:** 2026-04-07 t/m 2026-04-13 inclusief.
- **Meta → PostHog mapping:** 109 Meta link_clicks matchen 1:1 met 109 PostHog sessies. Totale clicks (208) omvatten ook post engagement. Gebruik link_clicks als juiste funnel-instap.
- **Ad-niveau LP bounce cross-reference:** gebaseerd op PostHog sessies per `utm_content` gematcht op Meta ad namen (h11/h12/h13/h15_b3_cta5). 1 sessie had verkeerd gecapitaliseerde utm (`H12,B3,CTA5`) — ad-team UTM convention check aanbevolen.
