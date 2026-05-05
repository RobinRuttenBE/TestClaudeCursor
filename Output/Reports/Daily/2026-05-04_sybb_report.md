# SYBB Daily Report — 2026-05-04

## 1. Samenvatting
De SYBB campagne staat sinds 19 april op PAUSED en heeft gisteren dus geen euro uitgegeven, geen impressies geleverd en geen klikken opgeleverd. De landing page kreeg slechts 2 organische bezoekers (beide bounced), waardoor er feitelijk niets te optimaliseren is op ad of LP niveau. Beslismoment: óf de campagne her-activeren, óf deze daily pauzeren tot er weer betaalde traffic loopt.

## 2. Meta Ads Performance

**Status campagne `2026: SYBB` (id 120239435987290239):** PAUSED sinds 2026-04-19. Daily budget €100 staat nog ingesteld maar is niet actief. Een paused kopie `2026: SYBB - Kopie` (id 120243293329420239) is aangemaakt op 2026-04-19, maar nooit live gegaan.

| Metric | Gisteren (2026-05-04) | 7d Gemiddelde (2026-04-27..05-03) | Trend |
|--------|----------------------|------------------------------------|-------|
| Spend | €0,00 | €0,00 | → (geen activiteit) |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

**Laatste actieve dag was 2026-04-19** (€43,81 spend, 2.756 impressions, 61 clicks, CTR 2,21%, CPC €0,72, freq 1,35).

**Lifetime referentie campagne (2026-01-13..2026-04-19):** €2.485,04 spend, 297K impressions, 12.067 clicks, CTR 4,06%, CPC €0,21, freq 2,24, 6.992 landing page views, 6 attributed purchases.

### Ad Variant Performance
Geen ad-level data beschikbaar voor 2026-05-04 of het 7d venster — alle ads liggen stil. Variant performance kan pas weer ge-evalueerd worden zodra de campagne her-activeert.

## 3. Landing Page Health (www.startyourballoonbusiness.com)

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 2 | 4,1 / dag | — | 🔴 verwaarloosbaar volume |
| Unique visitors | 2 | ~3 / dag | — | 🔴 |
| Sessions | 2 | 23 totaal (3,3 / dag) | — | 🔴 |
| Bounce Rate | 100% | 65,2% | <55% | 🔴 |
| Avg Session Duration | 0s* | 269s (4:29) | >90s | 🟢 (7d) / 🔴 (gisteren) |
| Scroll 25% | 0% | 21,7% | >80% | 🔴 |
| Scroll 50% | 0% | 21,7% | >60% | 🔴 |
| Scroll 75% | 0% | 17,4% | >40% | 🔴 |
| Scroll 100% | 0% | 13,0% | >20% | 🔴 |
| CTA Click Rate | 0% | n.v.t. (6 autocaptures over 8 dagen) | >4% | 🔴 |

*0s gisteren omdat beide sessies single-pageview zijn zonder $pageleave; geen scroll-events binnengekomen.

**Belangrijkste caveat:** alle LP cijfers staan op verwaarloosbaar lage volumes. De 7d bounce rate van 65% en lage scroll depth zijn statistisch betekenisloos bij 23 sessies — dit zegt meer over het soort bezoek (organisch + bio link) dan over de pagina kwaliteit zelf.

### UTM segmentatie (laatste 8 dagen, 2026-04-27..05-04)
| Bron | Pageviews | Sessions |
|------|-----------|----------|
| (geen UTM, direct/onbekend) | 17 | 13 |
| instagram / organic / sybb / bio_link | 14 | 12 |
| meta / cpc / sybb (paid) | 0 | 0 |

Nul Meta paid traffic deze week — bevestigt dat de campagne stilligt. Het enige geattribueerde verkeer komt uit de Instagram bio link.

## 4. Funnel Drop-off
Pageview (2) → Scroll 50% (0) → CTA Click (0) → /booking (0)

Met 2 bouncende bezoekers is funnel-analyse niet zinvol. Grootste lek = volledige top-of-funnel: er komt simpelweg geen verkeer binnen omdat ads uit staan.

## 5. Rode Vlaggen 🚩
1. **Campagne PAUSED sinds 16 dagen** — er zit geen budget op SYBB acquisitie. Alle KPIs blijven hierdoor 0 of irrelevant.
2. **Bounce rate 100% gisteren** (n=2) — niet actiehaar door volume, maar wel 0% scroll-engagement op iedere bezoeker.
3. **Geen $pageleave events op gisteren** — single pageview sessies zonder duration of scroll signaal. Als de scroll-depth tracking überhaupt nog werkt is moeilijk te zien tot er volume is.
4. **`2026: SYBB - Kopie` bestaat sinds 19 april en is nooit live** — risico dat deze ongebruikt blijft bestaan of per ongeluk dubbel actief gezet wordt.

## 6. Top 3 Acties voor Vandaag

1. **Beslis: SYBB campagne her-activeren of formeel pauzeren**
   - Wat: kies tussen (a) origineel `2026: SYBB` un-pausen op huidige €100/dag, (b) `2026: SYBB - Kopie` reviewen, fixen en lanceren, of (c) campagne archiveren en daily report tijdelijk uitzetten.
   - Waarom: 16 dagen zonder spend = 16 dagen zonder data = deze rapport is leeg tot er weer iets loopt.
   - Hoe: handmatig in Meta Ads Manager. Bij keuze (b) eerst diff checken tussen origineel en kopie.
   - Verwachte impact: terug naar bruikbare dagrapporten en pipeline van nieuwe leads.
   - Escalatie: 🟡 Robin goedkeuring (budget impact €100/dag).

2. **Opruimen: doe iets met `2026: SYBB - Kopie`**
   - Wat: kopie ofwel archiveren ofwel productioneel maken (naamgeving, ad sets, creatives valideren).
   - Waarom: zwevende paused kopieën verstoren rapportage en kunnen per ongeluk activeren.
   - Hoe: Meta Ads Manager → archive of merge intent in originele campagne.
   - Verwachte impact: schoner account, eenduidige rapportage.
   - Escalatie: 🟢 auto / 🟡 Robin keuze.

3. **Verifieer LP tracking voor het moment dat ads weer aan gaan**
   - Wat: snelle smoke-test op www.startyourballoonbusiness.com met een UTM-test URL (`?utm_source=meta&utm_medium=cpc&utm_campaign=sybb&utm_content=test_001`) en check of $pageview, $pageleave, scroll percentage en autocapture op CTA's allemaal binnenkomen in PostHog.
   - Waarom: 16 dagen zonder verkeer betekent dat eventuele tracking-breuken niet zichtbaar waren; je wilt dat de eerste betaalde klikken bruikbare data opleveren.
   - Hoe: open de URL, scroll naar bottom, klik elke primary CTA. Daarna PostHog HogQL: pageviews + scroll % per session_id van vandaag.
   - Verwachte impact: voorkomt dat eerste week na re-launch geen bruikbare LP cijfers oplevert.
   - Escalatie: 🟢 Robin zelf in 5 min.

## 7. Cross-References
Niet van toepassing: zonder Meta clicks en met n=2 LP sessies kunnen er geen ad-vs-LP correlaties worden getrokken. Cross-referencing kan pas weer betekenisvol worden zodra de campagne minimaal 2-3 dagen draait met >100 clicks/dag.
