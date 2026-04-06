# SYBB Daily Report -- 5 april 2026

## 1. Samenvatting

De SYBB campagne staat sinds 8 maart op PAUZE. Er is geen Meta Ads spend of traffic geweest gisteren. Het organische verkeer naar startyourballoonbusiness.com is minimaal: 8 pageviews van 7 unieke bezoekers, voornamelijk via bio_link (4) en direct/onbekend (4). De bounce rate is hoog (57%) en de gemiddelde scroll depth is alarmerend laag (19%). Geen enkele CTA click gisteren.

## 2. Meta Ads Performance

**CAMPAGNE STATUS: GEPAUZEERD sinds 8 maart 2026**

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

### Ad Variant Performance (1-8 maart, laatste actieve data)

| Ad (utm_content) | Link Clicks | CTR | CPC | LP Views | Leads | Cost/Lead |
|-------------------|-------------|------|-------|----------|-------|-----------|
| h13_b3_cta5 | 6.342 | 9,82% | EUR 0,07 | 4.063 | 3 | EUR 140,43 |
| h15_b3_cta5 | 1.399 | 4,26% | EUR 0,15 | 842 | 0 | - |
| h11_b3_cta5 | 684 | 2,56% | EUR 0,25 | 445 | 6 | EUR 33,75 |
| h12_b3_cta5 | 676 | 2,54% | EUR 0,31 | 467 | 5 | EUR 74,81 |
| h14_b3_cta5 | 602 | 3,68% | EUR 0,18 | 357 | 1 | EUR 109,40 |

**Beste variant (clicks):** h13_b3_cta5 -- verreweg de meeste clicks en laagste CPC (EUR 0,07). Maakt 65% van alle link clicks uit.
**Beste variant (leads):** h11_b3_cta5 -- hoogste lead conversie rate met 6 leads voor EUR 33,75 per lead.
**Slechtste variant:** h12_b3_cta5 -- hoogste CPC (EUR 0,31) met vergelijkbare CTR als h11.

## 3. Landing Page Health (PostHog)

| Metric | Gisteren (5 apr) | 7d Gemiddelde | Target | Status |
|--------|-----------------|---------------|--------|--------|
| Pageviews | 8 | 8,7/dag | - | - |
| Unique Visitors | 7 | 4,4/dag | - | - |
| Bounce Rate | 57,1% | 53,1% | <55% | 🔴 |
| Avg Session Duration | 15s | 187s* | >90s | 🔴 |
| Avg Scroll Depth | 18,9% | 25,4% | >60% | 🔴 |
| CTA Click Rate | 0% | 15,6%** | >4% | 🔴 |
| /booking Visits | 0 | - | - | 🔴 |

*7d gemiddelde session duration sterk vertekend door 2 lange sessies op 30-31 maart (waarschijnlijk intern testen). Realistische mediaan ~15s.
**7d CTA click rate is gebaseerd op 5 clicks over 32 sessies, voornamelijk geconcentreerd op 2 april (3 clicks).

### UTM Segmentatie (gisteren)

| utm_content | Pageviews | % van totaal |
|-------------|-----------|-------------|
| bio_link | 4 | 50% |
| Geen UTM (direct/organic) | 4 | 50% |

Geen Meta Ads UTM traffic gisteren (campagne staat uit).

## 4. Funnel Drop-off (7 dagen, 30 mrt - 5 apr)

```
Landing Page View (29 personen, 100%)
        |
        | -86,2% drop-off
        v
CTA Click (4 personen, 13,8%)
        |
        | 0% drop-off (alle CTA clickers gaan door)
        v
/booking Page (4 personen, 13,8%)
```

**Gemiddelde tijd tot CTA click:** 16 seconden
**Gemiddelde tijd CTA naar /booking:** 1 seconde

**Grootste lek:** Tussen Landing Page View en CTA Click (86% drop-off). De meeste bezoekers vertrekken zonder ooit op een CTA te klikken. Maar: wie WEL klikt, gaat 100% door naar /booking. De CTA zelf werkt goed, het probleem is dat te weinig mensen er komen.

## 5. Rode Vlaggen

- **CAMPAGNE GEPAUZEERD** -- Geen Meta Ads traffic sinds 8 maart. Alle huidige bezoekers komen via bio_link of direct.
- **Bounce rate 57,1%** -- Boven target van 55%. Bij bezoekers zonder UTM (organic/direct) is de intentie lager.
- **Scroll depth 18,9%** -- Ver onder target van 60%. Bezoekers scrollen nauwelijks voorbij de hero sectie.
- **0 CTA clicks gisteren** -- Bij 7 bezoekers is 0 clicks kritiek. De pagina engageert niet genoeg om tot actie te leiden.
- **Session duration 15 seconden** -- Ver onder target van 90s. Mensen vertrekken vrijwel direct.
- **Geen betaald verkeer** -- Zonder Meta Ads is het volume te laag om statistisch significante conclusies te trekken.

## 6. Cross-referencing Analyse

Omdat de campagne sinds 8 maart gepauzeerd is, is er geen verse ad-to-page data om te analyseren. De huidige LP bezoekers (bio_link en direct) zijn een ander publiek dan Meta Ads verkeer, waardoor de LP metrics niet direct vergelijkbaar zijn met de laatst actieve campagne periode.

**Historische cross-reference (1-8 maart):**
- h13_b3_cta5 had de hoogste CTR (9,82%) maar de laagste lead conversie rate (3 leads bij 4.063 LP views = 0,07%). Dit duidt op een **ad-page mismatch**: de ad trekt clicks maar de LP converteert ze niet.
- h11_b3_cta5 had de laagste CTR (2,56%) maar de hoogste lead conversie rate (6 leads bij 445 LP views = 1,35%). De ad filtert beter: minder clicks, maar de mensen die klikken zijn serieuzer.

## 7. Top 3 Acties voor Vandaag

### 1. Beslissing: SYBB campagne heractiveren of niet
- **Wat:** Bepaal of de SYBB campagne weer aangezet wordt en met welk budget.
- **Waarom:** Al 29 dagen gepauzeerd. Zonder betaald verkeer is er te weinig volume om de funnel te optimaliseren of leads te genereren.
- **Hoe:** Meta Ads Manager, campagne "2026: SYBB" van PAUSED naar ACTIVE.
- **Verwachte impact:** Terugkeer naar ~770 LP views/dag en ~2 leads/dag bij EUR 165/dag budget.
- **Escalatie:** Rood (strategie) -- Robin moet beslissen.

### 2. Landing page hero sectie reviewen
- **Wat:** Analyseer waarom bezoekers binnen 15 seconden vertrekken en niet voorbij 19% scrollen.
- **Waarom:** Scroll depth (19%) en session duration (15s) zijn beide ver onder target. De hero/eerste sectie houdt bezoekers niet vast.
- **Hoe:** Wix Editor -- sterkere headline, urgentie toevoegen, social proof boven de fold plaatsen.
- **Verwachte impact:** Verhoging scroll depth richting 40-50%, langere sessions.
- **Escalatie:** Oranje (Wix Editor nodig).

### 3. Organische traffic bronnen uitbreiden
- **Wat:** Zolang de campagne uit staat, meer organisch verkeer naar de LP sturen via Instagram bio, stories, en email.
- **Waarom:** 50% van het verkeer komt al via bio_link. Dit is de enige actieve bron op dit moment.
- **Hoe:** Instagram Story met swipe-up naar LP, email blast naar bestaande lijst.
- **Verwachte impact:** 2-3x meer organisch verkeer (van ~4 naar ~12 bezoekers/dag).
- **Escalatie:** Groen (zelf uitvoerbaar).

---

*Rapport gegenereerd op 6 april 2026 | Data: PostHog (startyourballoonbusiness.com) + Meta Ads MCP (Pipeboard) | Campagne: 2026: SYBB (GEPAUZEERD)*
