# SYBB Daily Report -- 14 april 2026

## 1. Samenvatting

Matige dag voor SYBB. CPC gestegen naar €0.62 (boven €0.50 target), terwijl het volume daalde met 23% minder impressions dan het 7-daags gemiddelde. De landing page lekt zwaar: 82.7% bounce rate, gemiddelde scroll depth van slechts 49%, en sessieduur van 46.7 seconden. Positief: 10 unieke bezoekers bereikten /booking en de CTA click rate is sterk (~11%). Het probleem zit duidelijk in de eerste seconden op de pagina, niet in de CTA's zelf.

## 2. Meta Ads Performance

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €95.93 | €100.25 | → |
| Impressions | 7,292 | 9,466 | ↓ |
| Clicks (all) | 154 | 194 | ↓ |
| Link Clicks | 83 | 102 | ↓ |
| CTR | 2.11% | 2.05% | → |
| CPC (all) | €0.62 | €0.52 | ↑ |
| Frequency | 1.53 | 1.92 | → |
| LP Views | 63 | 78 | ↓ |
| Video Views | 1,568 | 1,866 | ↓ |
| View Content | 7 | 7.0 | → |
| Add to Cart | 2 | 3.7 | → |

Gisteren waren er 3 actieve ad sets (Kopie 1, 2, 3). De originele ad sets (met H14 en H15) draaiden niet meer op 14 april.

### Ad Variant Performance (14 april)

| Ad (utm_content) | Spend | Link Clicks | CTR | CPC (link) | LP Views | View Content | ATC |
|---|---|---|---|---|---|---|---|
| H11,B3,CTA5 | €63.51 | 55 | 2.04% | €1.15 | 40 | 4 | 0 |
| H13,B3,CTA5 | €23.57 | 19 | 2.01% | €1.24 | 14 | 2 | 0 |
| H12,B3,CTA5 | €8.85 | 9 | 3.02% | €0.98 | 9 | 1 | 2 |

**7d Ad Performance (8-14 april, alle ad sets gecombineerd):**

| Ad Variant | 7d Spend | 7d Link Clicks | 7d CPC (link) | 7d LP Views | 7d ATC |
|---|---|---|---|---|---|
| H11 (Kopie 1) | €266.80 | 213 | €1.25 | 165 | 13 |
| H13 (Kopie 3) | €142.66 | 138 | €1.03 | 117 | 6 |
| H12 (Kopie 2 + orig) | €117.18 | 141 | €0.83 | 107 | 6 |
| H14 (origineel) | €122.96 | 158 | €0.78 | 108 | 0 |
| H15 (Kopie 4 + orig) | €52.15 | 61 | €0.86 | 39 | 1 |

**Beste variant:** H12. Hoogste CTR gisteren (3.02%), laagste CPC (€0.98/link click), en 2 add-to-carts op slechts €8.85 spend. Over 7 dagen de efficiëntste actieve variant met €0.83/link click en €19.53/ATC.

**Slechtste variant:** H11. Krijgt het meeste budget (€63.51 = 66% van spend), maar heeft de op een na duurste CPC (€1.15) en 0 ATCs gisteren. Over 7 dagen: €1.25/link click en €20.52/ATC. Budget proportie is niet in lijn met prestatie.

## 3. Landing Page Health (PostHog)

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 134 | 183 | meten | ↓ |
| Unique Visitors | 100 | ~129 | meten | ↓ |
| Bounce Rate | 82.7% | 81.8% | <55% | 🔴 |
| Avg Session Duration | 46.7s | 44.7s | >90s | 🔴 |
| Scroll 25%+ | 46.2% | 56.8% | >80% | 🔴 |
| Scroll 50%+ | 46.2% | 50.5% | >60% | 🔴 |
| Scroll 75%+ | 42.3% | 45.5% | >40% | 🟢 |
| Scroll 100% | 34.6% | 35.9% | >20% | 🟢 |
| CTA Click Rate | ~11% | ~15% | >4% | 🟢 |
| /booking Visits | 10 UV | ~16 UV/dag | meten | ↓ |

*Note: Scroll data gebaseerd op 26 sessies (van 104 totaal) met pageleave tracking op 14 april. 7d scroll data gebaseerd op 220 sessies.*

### Landing Page per UTM (14 april, PostHog)

| UTM Content | LP Pageviews | Unique Visitors | Avg Scroll | Scroll 50%+ |
|---|---|---|---|---|
| h11_b3_cta5 | 76 | 61 | 48.7% | 40.0% |
| h13_b3_cta5 | 33 | 25 | 58.9% | 63.6% |
| h12_b3_cta5 | 11 | 7 | 57.8% | 40.0% |
| bio_link | 8 | 6 | 80.7% | 66.7% |

## 4. Funnel Drop-off

```
LP Pageview (100 UV) ──100%──> CTA Click (~12 UV) ──12%──> /booking (10 UV) ──10%──> Add to Cart (2)
                         ↓ 88% verliest              ↓ 17% verliest             ↓ 80% verliest
```

| Funnel Stap | Unieke Bezoekers | % van Start | Drop-off vs vorige stap |
|---|---|---|---|
| LP Pageview | 100 | 100% | -- |
| CTA Click | ~12 | ~12% | -88% |
| /booking Page | 10 | 10% | -17% |
| Add to Cart (Meta) | 2 | 2% | -80% |

**Grootste lek:** De landing page zelf. 82.7% bounced direct. Van de ~18 mensen die doorlezen, converteert 55-67% naar een CTA click. Die conversie is gezond. Het probleem is dat de hero section en eerste 5 seconden niet overtuigen.

## 5. Cross-referencing: Meta Ads x PostHog

### Patroon 1: Hoge CTR + Hoge Bounce = Ad-pagina Mismatch
H11 heeft de meeste link clicks (55) maar de laagste scroll depth (48.7% gemiddeld, slechts 40% voorbij 50%). De ad hook trekt klikkers, maar de landing page levert niet wat de ad belooft.

### Patroon 2: H13 Beste Engagement Ondanks Lager Volume
H13 genereert minder clicks (19) maar de bezoekers scrollen significant verder (58.9% avg, 63.6% voorbij 50%). De audience quality is beter, maar het volume is te laag.

### Patroon 3: H12 Meest Complete Funnel
H12 is de enige variant met add-to-carts gisteren (2 ATCs op 9 link clicks). Combinatie van hoge CTR (3.02%), lage CPC (€0.98), en daadwerkelijke conversies. Budget is slechts €8.85 (9% van totaal).

### Patroon 4: Volume vs Quality Mismatch
H11 krijgt 66% van het dagbudget maar levert 0% van de ATCs. H12 krijgt 9% van het budget maar levert 100% van de ATCs. Budget verdeling is niet geoptimaliseerd voor conversie.

### Patroon 5: Bio Link = Beste Engagement
Organisch verkeer via bio_link (8 pageviews) toont de beste scroll depth (80.7%). Dit zijn bewust geinteresseerde bezoekers. Optimaliseer de landing page voor het gedrag dat deze groep al vertoont.

## 6. Rode Vlaggen 🚩

1. **CPC €0.62 > €0.50 target** -- Boven target. H11 (€1.15/link click) en H13 (€1.24) drijven de kosten omhoog. CPC stijging van +19.2% vs 7d gemiddelde, bijna op de 20% alert drempel.

2. **Bounce rate 82.7% > 70%** -- Structureel probleem, consistent over 7 dagen (81.8% gemiddeld). De ads trekken klikkers maar de pagina overtuigt niet in de eerste seconden.

3. **Scroll depth < 50% bij >54% van bezoekers** -- De hero en eerste sectie slagen er niet in bezoekers vast te houden. Vooral H11 traffic scrollt nauwelijks (48.7% avg).

4. **Session duration 46.7s ver onder 90s target** -- Bezoekers besteden minder dan een minuut op de pagina. Niet genoeg tijd om de value proposition te absorberen.

5. **11 rageclicks in 7 dagen** -- Frustratie-signaal in PostHog. Wijst op UX problemen: klikbare elementen die niet werken, of verwachtingen die niet matchen.

6. **Impressions daling -23%** -- Minder bereik dan gemiddeld. Mogelijk door minder actieve ad sets (3 vs 5 eerder in de week) of auction dynamics.

## 7. Top 3 Acties voor Vandaag

### 1. H12 Budget Opschalen, H11 Budget Verlagen
**Wat:** Verschuif 40-50% van H11 budget naar H12 ad set
**Waarom:** H12 = 3.02% CTR, €0.98/link click, 2 ATCs op €8.85. H11 = 2.04% CTR, €1.15/link click, 0 ATCs op €63.51. Budget verdeling is omgekeerd aan prestatie.
**Hoe:** Meta Ads Manager: verlaag Kopie 1 (H11) budget, verhoog Kopie 2 (H12) budget
**Verwachte impact:** CPC daling naar €0.50-0.55, meer ATCs per euro
**Escalatie:** Geel (Robin goedkeuring)

### 2. Landing Page Hero Sectie Herschrijven
**Wat:** Test een nieuwe hero met directere value proposition en social proof
**Waarom:** 82.7% bounce rate, 46.7s sessieduur, scroll depth gemiddeld 49%. De hero verliest het merendeel van bezoekers.
**Hoe:** A/B test in Wix: versie met "What you'll learn" bullets + testimonial vs huidige versie. Gebruik de bio_link audience (80.7% scroll) als benchmark voor gewenst gedrag.
**Verwachte impact:** Bounce rate dalen naar <70% = +50% meer engaged bezoekers
**Escalatie:** Oranje (Wix Editor)

### 3. Session Recordings Analyseren op Rageclicks
**Wat:** Bekijk de 11 rageclicks en 5-10 bounce sessies in PostHog
**Waarom:** 11 rageclicks = concrete frustratie, gecombineerd met 82.7% bounce wijst op een specifiek UX probleem dat te fixen is
**Hoe:** PostHog > Session Recordings > Filter: startyourballoonbusiness.com + rageclicks. Let op: welk element wordt herhaaldelijk geklikt? Welke sectie zien ze laatst?
**Verwachte impact:** Identificeer exact waar bezoekers afhaken of vastlopen, input voor actie #2
**Escalatie:** Groen (auto)

---

*Rapport gegenereerd op 15 april 2026. Data: Meta Ads via Pipeboard MCP, PostHog via PostHog MCP. Alle tijden in UTC.*
