# SYBB Daily Report — 21 May 2026

## 1. Samenvatting
Zeer rustige dag. Meta-campagne **`2026: SYBB`** staat al weken op **PAUSED**, dus 0 spend, 0 impressies, 0 clicks. Het kleine beetje landingspagina-verkeer dat we kregen op `www.startyourballoonbusiness.com` (1 directe mobiele bezoeker uit de VS) is organisch. Zonder live ads en zonder scroll-tracking is dit rapport vooral een **observatie van de stilte**, geen performance-analyse.

## 2. Meta Ads Performance

Campagne **`2026: SYBB`** (ID `120239435987290239`, account `Sempertex Ad Account`) staat sinds **2026-04-19** op PAUSED. Insights endpoint geeft een lege dataset voor zowel 21 mei als de 7d-vergelijking.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

### Ad Variant Performance
Geen actieve ads. De Meta-spend pijplijn (`h11_b3_cta5` t/m `h15_b3_cta5`) is volledig uit de lucht. De enige paid-attributed pageview in de hele afgelopen week was 1 hit met `utm_content=h11_b3_cta5` op `/booking` op 17 mei, vrijwel zeker een test of late klik.

**Beste variant:** n.v.t. (campagne staat uit)
**Slechtste variant:** n.v.t.

## 3. Landing Page Health

Host: `www.startyourballoonbusiness.com` (let op: PostHog tagt de canonieke host als `www.`, niet de naakte domain).

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 1 | 4,6 / dag | n.v.t. | ⚪ |
| Unique Visitors | 1 | 3,3 / dag | n.v.t. | ⚪ |
| Sessions | 1 | 3,4 / dag | n.v.t. | ⚪ |
| Bounce Rate | 100% (1/1) | ~89% (24/27) | <55% | 🔴 |
| Avg Session Duration | 0s | ~63s | >90s | 🔴 |
| Scroll 25% / 50% / 75% / 100% | niet gemeten | niet gemeten | >80/60/40/20% | ⚪ |
| CTA Click Rate (autocapture clicks / pageviews) | 500% (5 clicks / 1 pv) | ~70% | >4% | 🟢* |

*De CTA-rate is misleidend door autocapture: PostHog tagt elke `click` op een element, niet alleen "Book Now". Bij N=1 sessie is dit één bezoeker die rondklikt, geen funnel-signaal.

**Belangrijke meet-gap:** er zijn **geen scroll-events** (`$scroll`, `$rageclick` op CTA's, custom `cta_click`) ingericht. Het rapport-template vraagt scroll 25/50/75/100% en CTA-click-rate als KPI's, maar PostHog vangt momenteel alleen `$pageview`, `$pageleave`, `$autocapture`, `$web_vitals`. → Action item (zie sectie 6).

## 4. Funnel Drop-off

Gisteren (1 sessie):
```
Pageview (/) — 1
  → Scroll 50%       — niet gemeten
  → CTA Click        — niet onderscheidbaar van autocapture
  → /booking         — 0
  → /checkout        — 0
```

7d-window (27 sessies):
```
Pageview (/)        — 23 sessies (~85%)
  → /product-page    — 1
  → /booking         — 2 (1 paid h11_b3_cta5, 1 organic IG bio)
  → /checkout        — 1 (organic IG bio)
```

**Grootste lek:** stap `/` → `/booking` in de organische funnel. 11 pageviews vanuit Instagram-bio en 4 vanuit Facebook-bio leveren samen slechts 1 `/booking`-bezoek op (~6,7% klik-door naar boeking). Dat is laag voor warm bio-link verkeer.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne staat sinds 19 april op PAUSED.** Geen paid traffic naar SYBB sinds ~5 weken. Als SYBB nog een prioriteit is voor Q2, is dit de #1 blocker.
- 🚩 **Bounce rate ~89% over 7 dagen.** 24 van 27 sessies bekijken één pagina en vertrekken. Geen scroll-data om te weten of ze überhaupt onder de hero komen.
- 🚩 **Scroll & CTA tracking ontbreken.** Het SYBB-rapport-template leunt zwaar op scroll-depth en CTA-click metrics; zonder die events kun je niet beslissen of de landing page faalt of de traffic-kwaliteit faalt.
- 🚩 **Eenmalig paid-attributed bezoek (`h11_b3_cta5`) een week geleden** is de enige ad-getagde data in PostHog → geen variant-vergelijking mogelijk.
- ⚠️ Naakte domain (`startyourballoonbusiness.com` zonder `www.`) heeft 0 events. Skill-doc en `tracking-standards` verwijzen naar de naakte domain — check of PostHog snippet op alle subdomeinen identiek geconfigureerd is.

## 6. Top 3 Acties voor Vandaag

1. **Beslis: SYBB-campagne herstarten of officieel parkeren.**
   - **Wat:** Open Ads Manager, kies tussen ACTIVATE (met fris budget en mogelijk vernieuwde creatives) of een formele kill-decision met logboek-notitie.
   - **Waarom:** 5+ weken radiostilte op paid SYBB. Het dagelijkse rapport heeft geen signaal om op te draaien zolang de campagne uit staat. Q2-doelen lopen achter.
   - **Hoe:** Meta Ads Manager → campagne `2026: SYBB` (ID `120239435987290239`). Bij heractivatie: alle 5 ad-varianten heractiveren en `last_7d` performance benchmark zetten.
   - **Verwachte impact:** zonder beslissing blijft dit rapport leeg. Met heractivatie: binnen 48u eerste UTM-data per variant.
   - **Escalatie:** 🟡 Robin-beslissing (strategisch + budget).

2. **Instrumenteer scroll-depth en `cta_click` events in PostHog op `www.startyourballoonbusiness.com`.**
   - **Wat:** Voeg PostHog `posthog.capture('scroll_depth', { percent: 25/50/75/100 })` toe via scroll-listener én een expliciete `cta_click` event op alle "Book Now" / "Get Started" buttons.
   - **Waarom:** Het skill-rapport-template eist scroll 25/50/75/100% en CTA-click-rate als kern-KPI's; zonder deze events zijn rijen 3 en 5 van het rapport permanent leeg.
   - **Hoe:** Wix custom code blok op de landingspagina, of via Wix Editor PostHog snippet → custom event triggers per element. Test op staging vóór live push.
   - **Verwachte impact:** vanaf morgen kunnen we ad-CTR vs LP-scroll en LP-CTA cross-references daadwerkelijk doen, in plaats van n.v.t. invullen.
   - **Escalatie:** 🟠 Wix Editor + dev-tijd (~1u).

3. **Onderzoek de organische bio-link funnel: `/` → `/booking` levert ~6,7% door-klik.**
   - **Wat:** Bekijk de homepage-hero van `www.startyourballoonbusiness.com` met de ogen van een Insta-bio-klikker. Is de CTA boven de fold? Match het frame met de Metricool bio-link copy?
   - **Waarom:** 15 organische bio-link pageviews → 1 boeking. Dit is gratis warm verkeer; iedere extra %-punt conversie kost niets. Met paid uit, is organic je enige bron.
   - **Hoe:** Open `t-sml.mtrbio.com` link → land op `www.startyourballoonbusiness.com/` → noteer eerste 3 frictiepunten. Eventueel A/B-test hero-CTA copy via Wix.
   - **Verwachte impact:** verdubbeling organic bio→booking conversie = van ~1 naar ~2 boekingen/week, nul mediakosten.
   - **Escalatie:** 🟢 zelfstandig (visuele audit).

---

## Bijlage: Data Sources

- **Meta Ads:** Pipeboard MCP — account `act_567892422940728` (Sempertex Ad Account, EUR). Campagne `120239435987290239` ("2026: SYBB"), status PAUSED.
- **PostHog:** project "Default project" (id 149694) in org "Sempertex Europe". Host `www.startyourballoonbusiness.com`. Person-on-events mode actief. Project tz: UTC.
- **Periode:** 2026-05-21 (gisteren), vergelijking 2026-05-14 t/m 2026-05-20 (7d).
- **Niet geraadpleegd (conform run-instructies):** Gmail, Google Calendar, Google Drive, Google Sheets, Google Docs, Google Slides. Geen schrijven naar Meta Ads Tracker.
