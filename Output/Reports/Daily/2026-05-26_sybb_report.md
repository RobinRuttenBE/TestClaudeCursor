# SYBB Daily Report — 26 May 2026

## 1. Samenvatting
De Meta Ads campagne "2026: SYBB" stond gisteren volledig op PAUSED. Geen spend, geen impressies, geen ad clicks. Het verkeer op startyourballoonbusiness.com bestond uit 3 organische/directe sessies (2 desktop US, 1 desktop UK), zonder UTM-tagging en zonder verdere on-page interacties. Zonder actieve campagne en zonder CTA/scroll tracking is er feitelijk geen funnel om te diagnostiseren, alleen herstart-werk.

## 2. Meta Ads Performance

Campagne status: **PAUSED** (laatst geüpdatet 2026-04-19). Geen spend in de afgelopen 30 dagen.

| Metric | Gisteren (26 May) | 7d Gemiddelde | Trend |
|--------|-------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n/a | n/a | → |
| CPC | n/a | n/a | → |
| Frequency | n/a | n/a | → |

### Ad Variant Performance
Geen actieve ads gisteren. Alle utm_content varianten (h11_b3_cta5 … h15_b3_cta5) staan in pause-modus. Geen data om te vergelijken.

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | 0 | – | – | – | – |
| h12_b3_cta5 | 0 | – | – | – | – |
| h13_b3_cta5 | 0 | – | – | – | – |
| h14_b3_cta5 | 0 | – | – | – | – |
| h15_b3_cta5 | 0 | – | – | – | – |

**Beste variant:** n.v.t. (campagne pauze).
**Slechtste variant:** n.v.t. (campagne pauze).

**Lifetime context (13 Jan – 27 May 2026, ter referentie):** 297.174 impressies, 12.067 clicks, €2.485 spend, CTR 4,06%, CPC €0,21, frequency 2,24, 15 leads, 6 purchases, 53 add-to-carts. Sterke top-of-funnel signalen, zwakke conversie naar booking. Deze campagne wacht op herstart of nieuwe creatives.

## 3. Landing Page Health

Bron: PostHog `Default project`, host `www.startyourballoonbusiness.com`. Alleen `$pageview` events worden gevangen; geen click-, scroll- of session-duration events geconfigureerd.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 3 | 2,1 / dag | – | – |
| Sessies | 3 | 2,1 / dag | – | – |
| Unique visitors | 3 | – | – | – |
| Bounce Rate | 100% (3/3) | ~100% | <55% | 🔴 |
| Avg Session Duration | 0s | 0s | >90s | 🔴 |
| Scroll 25% | n/a | n/a | >80% | ⚪ niet getrackt |
| Scroll 50% | n/a | n/a | >60% | ⚪ niet getrackt |
| Scroll 75% | n/a | n/a | >40% | ⚪ niet getrackt |
| Scroll 100% | n/a | n/a | >20% | ⚪ niet getrackt |
| CTA Click Rate | n/a | n/a | >4% | ⚪ niet getrackt |

**7d traffic detail (per dag, pageviews):**
- 2026-05-19: 6
- 2026-05-20: 3
- 2026-05-21: 1
- 2026-05-22: 2
- 2026-05-23: 0
- 2026-05-24: 0
- 2026-05-25: 0
- 2026-05-26: 3

**Verkeersbron gisteren:** 100% `$direct` referrer, alle 3 zonder UTM-parameters. Geografie: 2 desktop US, 1 desktop UK.

> ⚠️ De 100% bounce + 0s duration is een gevolg van single-event sessies met alleen één `$pageview`. Dit kan zowel echt afhaken zijn als een tracking-gap (geen scroll/engagement events). Met n=3 niet statistisch betekenisvol.

## 4. Funnel Drop-off

Funnel niet meetbaar: er zijn geen CTA-click events of `/booking` pageviews vastgelegd in PostHog voor 26 May. Met alleen 3 sessies en alleen `$pageview` tracking is een funnel-analyse niet uitvoerbaar.

```
Pageview (3) → Scroll 50% (?) → CTA Click (?) → /booking (?)
```

**Grootste lek:** onbekend. Eerste lek dat we wél kunnen vaststellen: er is geen traffic-aanvoer (campagne pauze) én geen on-page tracking om te meten wat er gebeurt als er wel iemand binnenkomt.

## 5. Rode Vlaggen 🚩

1. **Campagne 2026: SYBB staat op PAUSED.** Geen actieve top-of-funnel. Alle dagelijkse KPI-doelen (CPC <€0,50, CTR-targets) zijn momenteel niet van toepassing.
2. **Geen UTM-tagging op het verkeer dat binnenkomt.** Alle 3 sessies kwamen binnen zonder utm_source/medium/campaign. Het is dus onmogelijk om bron-attribuutie te doen wanneer de campagne weer aan gaat — UTM-conventie (`utm_source=meta`, `utm_medium=cpc`, `utm_campaign=sybb`, `utm_content=hXX_bX_ctaX`) moet bevestigd worden in de ad-URL's.
3. **PostHog event-dekking is incompleet.** Alleen `$pageview` wordt gevangen. Geen autocapture clicks, geen scroll-depth, geen `/booking` conversie-event. Hierdoor zijn vrijwel alle KPI's uit `skills/daily-sybb-report/SKILL.md` (bounce rate, scroll 25/50/75/100%, CTA click rate, funnel drop-off) niet meetbaar.
4. **Traffic-volume staat structureel laag.** Over de afgelopen 30 dagen gemiddeld ~3-4 pageviews per dag, met meerdere nul-dagen. Voor betrouwbare optimalisatie is minimaal ~50-100 sessies/dag nodig.

## 6. Top 3 Acties voor Vandaag

### 1. Beslis: herstart de SYBB campagne of haal hem uit het rapport
- **Wat:** Robin neemt vandaag beslissing of "2026: SYBB" (ID `120239435987290239`) wordt heractiveerd met huidige creatives, met nieuwe creatives, of dat de campagne formeel wordt stopgezet en uit deze daily report-flow gehaald wordt.
- **Waarom:** Campagne staat sinds ~19 april op PAUSED (zie `updated_time`). Lifetime data toont 12k clicks à €0,21 met 15 leads (lead-conversie ~0,1% van clicks) en 6 purchases. Top-of-funnel doet het goed (CTR 4%), bottom-of-funnel lekt. Daily rapport zonder actieve campagne is een hol ritueel.
- **Hoe:** Meta Ads Manager → campagne `2026: SYBB` → review ads & landing page → activeer of archiveer.
- **Verwachte impact:** binnen 24u weer meetbare ad-data; rapport wordt zinvol.
- **Escalatie:** Rood (strategie — Robin beslist).

### 2. Implementeer PostHog event-tracking voor SYBB landing page
- **Wat:** Voeg in PostHog (of via Wix custom code) tracking toe voor: (a) scroll-depth events op 25/50/75/100%, (b) click events op alle CTA-knoppen op startyourballoonbusiness.com, (c) een `/booking` `$pageview` als conversie marker, (d) autocapture inschakelen voor algemene engagement.
- **Waarom:** Zonder deze events kan dit dagrapport zes van zeven Landing Page Health KPI's niet meten, en kan de funnel drop-off niet berekend worden. Dit is de bottleneck voor alle data-gedreven optimalisatie van SYBB.
- **Hoe:** Wix Editor / Custom Code → PostHog snippet met `posthog.capture` op scroll thresholds en CTA clicks. Of inschakelen PostHog autocapture als die nog uit staat.
- **Verwachte impact:** vanaf morgen complete funnel-zichtbaarheid.
- **Escalatie:** Oranje (Wix Editor wijziging).

### 3. Borg UTM-conventie op alle SYBB ad URL's vóór re-launch
- **Wat:** Controleer dat alle ads in `2026: SYBB` de landing page URL hebben getagd volgens convention: `?utm_source=meta&utm_medium=cpc&utm_campaign=sybb&utm_content=hXX_bX_ctaX&utm_term=batch_X`. Inclusief de `- Kopie` variant van de campagne.
- **Waarom:** Gisteren kwamen 3 sessies binnen zónder UTM's — als de campagne wordt heractiveerd zonder UTM-borging blijft attributie per ad-variant onmogelijk en valt de hele "Ad Variant Performance" sectie weg.
- **Hoe:** Meta Ads Manager → per ad → website URL field controleren en corrigeren. Cross-check met `Kennis/tracking-standards`.
- **Verwachte impact:** per-variant performance kan vanaf re-launch gemeten worden.
- **Escalatie:** Geel (Robin goedkeuring per ad).

---

*Bronnen: Meta Ads MCP (Pipeboard), account `act_567892422940728`, campagne `120239435987290239`. PostHog MCP, project `Default project` (149694), host `www.startyourballoonbusiness.com`. Datumbereik: 2026-05-26 (UTC).*
