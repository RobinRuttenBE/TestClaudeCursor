# SYBB Daily Report, 16 april 2026

## 1. Samenvatting
Spend halveerde t.o.v. 7d gemiddelde (€57,79 vs €101,97/dag) met sterk lagere levering (impressions, 49%). CTR bleef gezond (2,31%) maar CPC (€0,56) zit boven target en er waren 0 purchases ondanks 5 initiated checkouts, wat wijst op een lek bij het betaalmoment.

## 2. Meta Ads Performance

| Metric | Gisteren (16 apr) | 7d Gemiddelde (9,15 apr) | Trend |
|--------|-------------------|--------------------------|-------|
| Spend | €57,79 | €101,97 | ↓ |
| Impressions | 4.498 | 8.812 | ↓ |
| Clicks (all) | 104 | 189 | ↓ |
| Link clicks | 64 | 98 | ↓ |
| Landing page views | 54 | 76 | ↓ |
| CTR | 2,31% | 2,15% | → |
| CPC | €0,56 | €0,54 | → |
| Frequency | 1,45 | 2,10 (7d cum.) | → |
| Initiated checkouts | 5 | 2,7 | ↑ |
| Purchases | 0 | 0,86 | ↓ |
| Complete registration | 1 | 0,7 | → |

**Opmerking:** 7d gemiddelde berekend uit 9,15 april totalen (€713,79 spend, 61.683 impressions, 1.325 clicks, 6 purchases).

### Ad Variant Performance (16 april)

| Ad (utm_content) | Spend | Impressions | Clicks | CTR | CPC | LP Views | ATC | Checkouts | Purchases |
|------------------|-------|-------------|--------|-----|-----|----------|-----|-----------|-----------|
| h11_b3_cta5 | €41,43 | 3.154 | 74 | 2,35% | €0,56 | 35 | 5 | 2 | 0 |
| h13_b3_cta5 | €8,98 | 708 | 17 | 2,40% | €0,53 | 9 | 2 | 0 | 0 |
| h12_b3_cta5 | €7,38 | 636 | 13 | 2,04% | €0,57 | 10 | 3 | 3 | 0 |

**Beste variant:** H13 heeft hoogste CTR (2,40%) en laagste CPC (€0,53), nog net onder target. H12 is efficient in checkout push (3 initiated checkouts op 13 clicks = 23% checkout rate).
**Slechtste variant:** H11 nam 72% van budget op maar leverde geen purchases en had hoogste drop off bij checkout (2 initiated checkouts op 5 ATCs). H11 blijft de workhorse qua volume, maar conversion efficiency zakt.

## 3. Landing Page Health

> **PostHog MCP niet beschikbaar in deze sessie.** Landing page metrics konden niet worden opgehaald. Meta reporteert wel `landing_page_view` events (54 totaal, Meta's definitie = pixel fired na volledige laadtijd), maar zonder PostHog kunnen we geen bounce rate, scroll depth, session duur of CTA click rate vergelijken met targets.

Proxy observaties vanuit Meta data:
- Link clicks, LP views ratio: 64 link clicks, 54 LP views (84%). 16% van de clicks bereikt de pagina niet fully, normaal voor mobile drop off.
- LP view, ATC ratio: 54 LP views, 10 add to carts (18,5%). Dit is een engagement signaal, niet een bounce vervanging.

**Action:** PostHog MCP verbinding herstellen vóór volgende run voor complete LP health check.

## 4. Funnel Drop-off (Meta pixel data)

| Stap | Events | % vs vorige stap |
|------|--------|------------------|
| Link click | 64 | 100% |
| Landing page view | 54 | 84% |
| View content | 9 | 17% |
| Add to cart | 10 | 111% |
| Initiated checkout | 5 | 50% |
| Complete registration | 1 | 20% |
| Purchase | 0 | 0% |

**Grootste lek:** Initiated checkout, purchase (5, 0 = 100% drop off). Dit is het kritieke punt. Ook de stap LP view, view content (54, 9 = 83% drop off) suggereert dat de pagina content niet de juiste trigger biedt om dieper te gaan.

> **Data caveat:** pixel waarden blijven vertekend (€44.247 complete_registration value in 7d = niet realistisch). Negeer alle euro waarden vanuit actions, focus op event counts.

## 5. Rode Vlaggen

- **Spend daling 43%** t.o.v. 7d gemiddelde. Check of budget of delivery issue: daily budget staat op €100 (10000 cents), normale delivery zou dit moeten uitputten.
- **0 purchases ondanks 5 initiated checkouts.** 100% drop off bij betaalstap, mogelijk checkout issue op startyourballoonbusiness.com/booking.
- **CPC €0,56 boven target €0,50** (+12%). H11 en H12 beide boven, H13 net eronder.
- **H11 funnel mismatch:** 44 link clicks, 1 complete registration, 0 purchase terwijl het 72% van het budget krijgt.
- **PostHog data ontbreekt:** blinde vlek op LP kwaliteit, herstel vóór volgende run.

## 6. Top 3 Acties voor Vandaag

1. **Test de booking checkout flow persoonlijk.** 5 mensen kwamen bij initiated checkout, 0 voltooid. Open startyourballoonbusiness.com, klik een CTA, doorloop checkout met test card. Check voor fouten, trage load, verplichte velden, payment provider issues. **Escalatie:** Oranje (Wix Editor).
2. **Onderzoek waarom spend 43% daalde.** Meta Ads Manager, 2026: SYBB, check delivery status, audience size, bid cap, en budget pacing. Mogelijk ad fatigue of audience saturation op BATCH 2 adsets. **Escalatie:** Geel (Robin goedkeuring).
3. **PostHog MCP verbinding herstellen.** Zonder LP analytics is cross reference analyse onmogelijk. Fix de MCP configuratie in .mcp.json of het relevante config bestand. **Escalatie:** Groen (auto).

---

**Data bronnen:** Meta Ads MCP (Pipeboard), account act_567892422940728, campagne 2026: SYBB (ID 120239435987290239).
**Datum:** 16 april 2026 (gisteren).
**PostHog:** niet beschikbaar.
