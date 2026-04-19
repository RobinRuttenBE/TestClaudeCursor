# SYBB Daily Report 2026-04-18

## 1. Samenvatting
Stabiele dag met een doorbraak op de funnel-bottom: voor het eerst sinds dagen 7 initiate checkouts en 1 voltooide aankoop (`/thank-you-page` PV, ~€350 actiewaarde). Top-of-funnel zwakte blijft: spend €94,47 met CPC €0,62 (boven target), CPM €14,68 (18% boven 7d avg) en bounce rate 80,4%. Variant **H12** levert opnieuw de beste efficiency (CTR 4,21%, CPC €0,38) maar krijgt slechts 13% van het budget. **H13** heeft de slechtste landingpage performance (88,9% bounce, scroll 50% slechts 20%).

## 2. Meta Ads Performance

Campagne: `2026: SYBB` (ID 120239435987290239), account `act_567892422940728`, status ACTIVE.

| Metric | Gisteren (18-04) | 7d Gemiddelde (11-17 apr) | Trend |
|--------|------------------|---------------------------|-------|
| Spend | €94,47 | €104,83 | ↓ 10% |
| Impressions | 6.435 | 8.408 | ↓ 23% |
| Reach | 4.789 | 5.616/dag | ↓ 15% |
| Clicks (all) | 152 | 174 | ↓ 13% |
| Link clicks | 90 | n.v.t. | — |
| Landing page views | 78 | n.v.t. | — |
| CTR | 2,36% | 2,07% | ↑ 14% |
| CPC | €0,62 | €0,60 | → (+3%) |
| CPM | €14,68 | €12,47 | ↑ 18% (slechter) |
| Frequency (dag) | 1,34 | 1,50 (cum. 7d) | ↓ |
| Initiate Checkout | **7** | n.v.t. | nieuw signaal |
| Add to Cart | **6** | n.v.t. | nieuw signaal |
| Cost / IC | €13,50 | n.v.t. | — |

### Ad Variant Performance (gisteren)

| Ad (utm_content) | Spend | Impr | Clicks | CTR | CPC | LPV (Meta) | IC | PH Sessions | PH Bounce | PH Scroll 50%+ |
|------------------|-------|------|--------|-----|-----|-----------|----|-------------|-----------|----------------|
| h11_b3_cta5 | €67,43 | 4.585 | 93 | 2,03% | €0,73 | 51 | 2 | 63 | 82,5% | 31,8% (7/22) |
| h12_b3_cta5 | €12,46 | 784   | 33 | 4,21% | €0,38 | 12 | 3 | 17 | 82,4% | 28,6% (2/7)  |
| h13_b3_cta5 | €14,58 | 1.066 | 26 | 2,44% | €0,56 | 15 | 2 | 18 | 88,9% | 20,0% (1/5)  |

**Beste variant:** **H12** opnieuw de winnaar voor pre-click metrics (CTR 4,21% = 2x H11; CPC €0,38 = 48% lager dan H11) en levert 3 van de 7 IC's met slechts 13% van de spend. CPI €4,15 (33% van H11's €33,72).
**Slechtste variant:** **H13** combineert slechte CTR (2,44%) met de hoogste landing-bounce (88,9%) en laagste scroll diepte. Geen efficiente klik én geen engaged bezoeker.

## 3. Landing Page Health (startyourballoonbusiness.com)

| Metric | Gisteren | 7d Gemiddelde | Target 30d | Status |
|--------|----------|---------------|-----------|--------|
| Pageviews | 135 | 149/dag | — | — |
| Unieke bezoekers | 100 | 105/dag | — | — |
| Sessions | 102 | 110/dag | — | — |
| Bounce Rate | 80,4% | 81,1% | <55% | 🔴 |
| Avg Session Duration (uit pageleave) | 158s | 343s (volatiel) | >90s | 🟢 |
| Scroll 25% | 41,9% (18/43) | 44,0% | >80% | 🔴 |
| Scroll 50% | 37,2% (16/43) | 41,8% | >60% | 🔴 |
| Scroll 75% | 37,2% (16/43) | n.v.t. | >40% | 🟡 |
| Scroll 100% | 23,3% (10/43) | n.v.t. | >20% | 🟢 |
| Avg max scroll | 41,7% | 42,4% | >60% | 🔴 |
| CTA "Go to workshop" CTR | 9,8% (10/102) | — | >4% | 🟢 |
| Combined CTA clicks | 15 (Go+Book+Buy) | — | — | — |

Opm.: bounce rate gemeten als % sessies met exact 1 pageview (PostHog `$pageview` events). Scroll diepte over 43 `$pageleave` events; 59 sessies (58%) sturen geen leave-event (typisch harde bouncers).

### Pathname verdeling gisteren

| Path | Pageviews | Sessions |
|------|-----------|----------|
| `/` (landing) | 112 | 98 |
| `/product-page/start-your-balloon-business-professional` | 14 | 12 |
| `/checkout` | 7 | 7 |
| `/booking` | 1 | 1 |
| `/thank-you-page` | 1 | 1 |

### Top autocapture clicks gisteren

| Element | Clicks |
|---------|--------|
| "Go to workshop" (CTA) | 10 |
| "Where does the workshop take place?" (FAQ) | 7 |
| "Add to Cart" | 3 |
| "Book Your Spot" | 3 |
| "Buy Now" | 2 |
| FAQ varia (dates, parking, starttijd, ticket, food) | 10 |
| `/booking` link | 1 |

## 4. Funnel Drop-off

```
Meta impressions (6.435)
  → Link clicks (90, 1,40%)
    → Meta LPV (78, 87% van link clicks)
      → PH sessies op landing / (98, ~retargeting/repeat verschil ~25%)
        → Scroll 50%+ (16 van 43 leave-events, 37%)
          → CTA-clicks (Go to workshop 10 + Book Your Spot 3 = 13, ~13% sessies)
            → /product-page (14 PV / 12 sessies)
              → /checkout (7 sessies)
                → /thank-you-page (1, ~14% van checkouts, ~1% sessies)
```

**Grootste lek:** **landing → 50% scroll** (37% komt door). Hetzelfde patroon als 17-04. De hero/eerste sectie sluit niet aan bij ad-belofte.

**Tweede lek:** **CTA-click → /booking pageview** (10 "Go to workshop" clicks, slechts 1 `/booking` PV). Tracking probleem blijft bestaan — dezelfde issue als gisteren.

**Positief signaal:** **/checkout → /thank-you-page**: 7 → 1 (14% conversie). Eerste daadwerkelijke aankoop in dagen. Meta IC pixel + PH /checkout match perfect (7 = 7), wat tracking valideert op deze stap.

## 5. Rode Vlaggen

- **Bounce rate 80,4%** — 25 punten boven target (🚨 kritiek, in lijn met 7d avg).
- **CPM €14,68** — 18% hoger dan 7d avg (€12,47); auction druk neemt toe of creatives vermoeien (frequency stabiel = waarschijnlijk audience-niveau).
- **CPC €0,62** — 24% boven target €0,50; H11 trekt blended CPC omhoog met €0,73.
- **H11 budget-dominantie** — 71% van spend (€67,43) naar slechtst presterende klik-variant. Levert wel 51 LPV's (volume).
- **H12 onderbenut** — 13% van spend, top CTR + top efficiency op IC (3 IC's = 43% van totaal). Learning wordt nog steeds niet uitgenut.
- **H13 LP-mismatch** — 88,9% bounce (4pp hoger dan campagne-gemiddelde) en avg scroll 32%. Klikken kosten €0,56 maar mensen verlaten direct.
- **CTA → /booking gap** — 10 "Go to workshop" + 3 "Book Your Spot" clicks, slechts 1 `/booking` PV. Probleem nog niet gefixt sinds gisteren.
- **Scroll data sparse** — 43 van 102 sessies (42%) leveren leave-event. 59 sessies vertrekken zonder enige interactie — bevestigt 80% bounce.

## 6. Top 3 Acties voor Vandaag

1. **Schaal H12 op, pauzeer H13.** H12 verdient minimaal 35% van het budget (nu 13%). H13 heeft de hoogste bounce (88,9%) en de slechtste scroll — en is nog steeds tweede in spend (€14,58). Verschuif H13's budget naar H12. Dit is bewezen, geen experiment: H12 scoort op CTR, CPC én IC.
   - **Waarom:** H12 CTR 4,21% (2x H11), CPI €4,15 (12% van H11's €33,72), 3 van de 7 IC's met 13% van de spend.
   - **Hoe:** Meta Ads Manager → adset Kopie 2 (H12) verhoog naar €35-40/dag, adset Kopie 3 (H13) pauzeer of verlaag naar €5/dag.
   - **Verwachte impact:** blended CPC -15-20% binnen 5 dagen, +30-50% IC volume bij stabiele LP performance.
   - **Escalatie:** 🟡 Geel (Robin goedkeuring).

2. **Fix CTA tracking — definitief.** 10 "Go to workshop" clicks, 1 `/booking` PV. Open dev tools, klik vanuit de ad op de CTA en check (a) of href naar `/booking` gaat, (b) of de PostHog snippet daar ook geladen is. Als de CTA naar een externe ticket-url leidt: voeg PostHog snippet toe of stuur eerst naar interne `/booking` met redirect.
   - **Waarom:** Zonder betrouwbare booking tracking weten we niet welke variant écht converteert. We hebben nu 1 voltooide aankoop maar geen attributie.
   - **Hoe:** Robin handmatig in browser → check `Network` tab + PostHog session recording reproduceren.
   - **Verwachte impact:** directe toewijzing van conversies aan utm_content; H12 ROI wordt hard meetbaar.
   - **Escalatie:** 🟢 Groen (Robin zelf, ~10 min).

3. **Hero-sectie hypothese-test plannen.** Scroll 25% blijft 41,9% — dwz 58% van de bezoekers ziet de fold maar scrollt niet eens een halve schermhoogte. Patroon herhaalt zich nu 2 dagen op rij. Open 3 session recordings van H11 mobile traffic en check: (a) laadtijd boven de fold, (b) hero copy match met H11 ad hook, (c) of er irriterende elementen zijn (popup/cookie banner).
   - **Waarom:** Grootste funnel-lek; alle downstream optimalisaties (CTA, checkout) beïnvloeden slechts 42% van het verkeer dat überhaupt scrollt.
   - **Hoe:** PostHog → Session recordings → filter op `utm_content = h11_b3_cta5` + `Mobile`, kies 3 met scroll < 25%. Schrijf binnen de week 1 hero-variant ter test.
   - **Verwachte impact:** +10pp scroll 50% verdubbelt effectieve lead flow naar de CTA en daarmee de absolute IC-volumes.
   - **Escalatie:** 🟠 Oranje (Wix Editor + copy review).

---

## Bronnen
- **Meta Ads:** Pipeboard MCP, campaign ID `120239435987290239`, account `act_567892422940728`. Tijdsvenster: dag = 2026-04-18, baseline = 2026-04-11 t/m 2026-04-17 (7d).
- **PostHog:** project `Default project` (id 149694), host `www.startyourballoonbusiness.com`. HogQL queries op `events` tabel.
- Rapport gegenereerd op 2026-04-19.
