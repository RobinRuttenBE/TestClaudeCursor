# SYBB Daily Report -- 6 april 2026

## 1. Samenvatting

De SYBB campagne staat sinds 8 maart op PAUZE (dag 30). Er is geen Meta Ads spend of traffic. Het organische verkeer naar startyourballoonbusiness.com is stabiel laag: 4 pageviews van 3 unieke bezoekers, voornamelijk via bio_link (3 van 4). Positief: 1 van de 3 bezoekers klikte op een CTA en bereikte /booking (33% conversie). De sessieduur is verdubbeld t.o.v. gisteren (31s vs 15s), maar blijft ver onder target.

## 2. Meta Ads Performance

**CAMPAGNE STATUS: GEPAUZEERD sinds 8 maart 2026 (dag 30)**

Er is geen actieve Meta Ads data voor gisteren of de afgelopen 7 dagen. Hieronder de laatst bekende performance (1-8 maart 2026) ter referentie:

| Metric | Laatste actieve week (1-8 mrt) | Daggemiddelde |
|--------|-------------------------------|---------------|
| Spend | EUR 1.323,83 | EUR 165,48 |
| Impressions | 189.067 | 23.633 |
| Clicks | 9.965 | 1.246 |
| CTR | 5,27% | - |
| CPC | EUR 0,13 | - |
| Link Clicks | 9.703 | 1.213 |
| Landing Page Views | 6.174 | 772 |
| Frequency | 2,07 | - |
| Leads | 15 | 1,9 |

### All-time Campagne Totalen (13 jan - 8 mrt 2026)

| Metric | Totaal |
|--------|--------|
| Spend | EUR 1.425,57 |
| Impressions | 205.335 |
| Reach | 99.103 |
| Link Clicks | 9.815 |
| Landing Page Views | 6.174 |
| Leads | 15 |
| Video Views | 50.032 |
| Cost per Lead | EUR 95,04 |

### Ad Variant Performance (all-time, gesorteerd op link clicks)

| Ad (utm_content) | Link Clicks | CTR | CPC | LP Views | Leads | Cost/Lead |
|-------------------|-------------|------|-------|----------|-------|-----------|
| h13_b3_cta5 | 6.342 | 9,82% | EUR 0,07 | 4.063 | 3 | EUR 140,43 |
| h15_b3_cta5 | 1.399 | 4,26% | EUR 0,15 | 842 | 0 | - |
| h11_b3_cta5 | 684 | 2,56% | EUR 0,25 | 445 | 6 | EUR 33,75 |
| h12_b3_cta5 | 676 | 2,54% | EUR 0,31 | 467 | 5 | EUR 74,81 |
| h14_b3_cta5 | 602 | 3,68% | EUR 0,18 | 357 | 1 | EUR 109,40 |
| SYBB BLACK (statisch) | 112 | 1,03% | EUR 0,61 | - | 0 | - |

**Beste variant (clicks):** h13_b3_cta5 -- 65% van alle link clicks, laagste CPC (EUR 0,07).
**Beste variant (leads):** h11_b3_cta5 -- 6 leads voor EUR 33,75 per lead. Hoogste lead conversie.
**Slechtste variant:** SYBB BLACK (statisch) -- laagste CTR (1,03%), hoogste CPC (EUR 0,61), 0 leads.

## 3. Landing Page Health (PostHog)

| Metric | Gisteren (6 apr) | 7d Gemiddelde | Target | Status |
|--------|-----------------|---------------|--------|--------|
| Pageviews | 4 | 6,4/dag | - | - |
| Unique Visitors | 3 | 4,6/dag | - | - |
| Bounce Rate | 66,7%* | ~55% | <55% | 🔴 |
| Avg Session Duration | 31s | ~30s** | >90s | 🔴 |
| CTA Click Rate | 33,3% | ~16% | >4% | 🟢 |
| /booking Visits | 1 | ~0,6/dag | - | 🟡 |

*Bounce rate berekend als 2/3 bezoekers zonder interactie.
**7d gemiddelde session duration vertekend door extreem lage volumes. Niet statistisch significant.

### UTM Segmentatie (gisteren)

| utm_content | Pageviews | % van totaal |
|-------------|-----------|-------------|
| bio_link | 3 | 75% |
| Geen UTM (direct/organic) | 1 | 25% |

Geen Meta Ads UTM traffic (campagne staat uit). Bio_link domineert: Instagram bio is de primaire traffic bron.

### 7-Daagse Trend (31 mrt - 6 apr)

| Datum | Pageviews | Unique Visitors |
|-------|-----------|-----------------|
| 31 mrt | 5 | 2 |
| 1 apr | 2 | 1 |
| 2 apr | 22 | 15 |
| 3 apr | 0 | 0 |
| 4 apr | 4 | 4 |
| 5 apr | 8 | 7 |
| 6 apr | 4 | 3 |
| **Totaal** | **45** | **~32** |

Spike op 2 april (22 PV, 15 UV) is opvallend. Mogelijke oorzaak: Instagram post/story die naar LP linkte?

## 4. Funnel Drop-off (gisteren, 6 april)

```
Landing Page View (3 personen, 100%)
        |
        | -66,7% drop-off
        v
CTA Click (1 persoon, 33,3%)
        |
        | 0% drop-off
        v
/booking Page (1 persoon, 33,3%)
```

**Gemiddelde tijd tot CTA click:** 15 seconden
**Gemiddelde tijd CTA naar /booking:** 3 seconden

**Grootste lek:** Tussen Landing Page en CTA Click (67% drop-off). Maar: wie WEL klikt, gaat 100% door naar /booking. De funnel na CTA werkt perfect. Het probleem zit in de eerste indruk/scroll.

**Vergelijking met gisteren (5 apr):** Gisteren 0 CTA clicks bij 7 bezoekers (0%). Vandaag 1 CTA click bij 3 bezoekers (33%). Grote verbetering, maar volume is te laag voor conclusies.

## 5. Rode Vlaggen

- **CAMPAGNE GEPAUZEERD -- DAG 30** -- Geen Meta Ads traffic sinds 8 maart. Elke dag zonder campagne is gemiste exposure en leads. 15 leads in 54 dagen actief = 0,28 leads/dag.
- **Volume te laag voor analyse** -- Met 3-7 bezoekers per dag zijn alle metrics statistisch onbetrouwbaar. Minimaal 30+ bezoekers/dag nodig voor betrouwbare LP optimalisatie.
- **Session duration 31s** -- Beter dan gisteren (15s) maar nog steeds ver onder target van 90s.
- **Bounce rate 67%** -- Boven target van 55%. Twee van drie bezoekers vertrekken zonder interactie.
- **Geen betaald verkeer al 30 dagen** -- De LP kan niet geoptimaliseerd worden zonder volume. Elke dag vertraging kost potentiele leads.

## 6. Cross-referencing Analyse

Geen verse ad-to-page data beschikbaar (campagne paused). De huidige bezoekers (bio_link/direct) zijn een ander publiek dan Meta Ads verkeer.

**Historische inzichten ter herinnering:**
- **h13 paradox:** Hoogste CTR (9,82%) maar laagste lead conversie (0,07%). De ad trekt kijkers, niet kopers. Ad-page mismatch.
- **h11 is de lead machine:** Laagste CTR (2,56%) maar hoogste lead rate (1,35%). Filtert het publiek beter, serieuze klikkers.
- **Bij heractivering:** Focus budget op h11 (beste cost/lead) en h15 (goede CTR + CPC combo). Pauzeer h12 (duurste CPC) en de statische ad (geen ROI).

## 7. Top 3 Acties voor Vandaag

### 1. Beslissing: SYBB campagne heractiveren
- **Wat:** De campagne staat nu 30 dagen op pauze. Bepaal of en wanneer heractivering plaatsvindt.
- **Waarom:** Zonder betaald verkeer: te weinig volume voor LP optimalisatie, 0 ad-gegenereerde leads in 30 dagen, LP metrics onbetrouwbaar door klein sample.
- **Hoe:** Meta Ads Manager, campagne "2026: SYBB" van PAUSED naar ACTIVE. Start met EUR 15/dag budget op h11 en h15 only.
- **Verwachte impact:** ~150-200 LP views/dag, ~1-2 leads/week.
- **Escalatie:** Rood (strategie) -- Robin moet beslissen.

### 2. Onderzoek traffic spike 2 april
- **Wat:** Uitzoeken wat de 22 pageviews / 15 unique visitors op 2 april veroorzaakte.
- **Waarom:** Dit was 5x het normale volume. Als dit herhaalbaar is (bijv. een Instagram post), kan het een gratis traffic bron zijn.
- **Hoe:** Check Instagram posts/stories van 2 april, check email campagnes, check /social-report.
- **Verwachte impact:** Identificeer herhaalbare organische traffic drivers.
- **Escalatie:** Groen (onderzoek, zelf uitvoerbaar).

### 3. Landing page hero sectie verbeteren
- **Wat:** De meerderheid van bezoekers bounced binnen 31 seconden. De hero sectie moet sterker.
- **Waarom:** Bounce rate 67%, session duration 31s. De pagina overtuigt niet snel genoeg.
- **Hoe:** Wix Editor: sterkere headline met urgentie, social proof boven de fold (testimonials, aantallen), duidelijkere value proposition.
- **Verwachte impact:** Bounce rate richting 50%, session duration richting 60s.
- **Escalatie:** Oranje (Wix Editor nodig).

---

*Rapport gegenereerd op 7 april 2026 | Data: PostHog (startyourballoonbusiness.com) + Meta Ads MCP (Pipeboard) | Campagne: 2026: SYBB (GEPAUZEERD -- dag 30)*
