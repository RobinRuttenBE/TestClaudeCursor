# SYBB Daily Report — 2026-05-20

## 1. Samenvatting
Meta Ads campagne "2026: SYBB" staat op PAUSED, dus gisteren werd er geen euro gespendeerd en kwam er geen paid traffic binnen. De landing page kreeg 3 organische bezoeken (2 via Instagram bio link, 1 via Facebook bio link), allemaal op de homepage, met een gemiddelde sessieduur van ~19 seconden en geen CTA-clicks of bookings. Tot de campagne opnieuw geactiveerd wordt is dit rapport vooral een nul-meting voor organisch verkeer.

## 2. Meta Ads Performance
**Status campagne "2026: SYBB" (ID 120239435987290239): PAUSED** sinds laatste update op 2026-04-19. Geen spend, geen impressions, geen clicks, geen conversies, niet gisteren en niet in de afgelopen 7 dagen.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n/a | n/a | → |
| CPC | n/a | n/a | → |
| Frequency | n/a | n/a | → |

### Ad Variant Performance
Niet van toepassing. Geen ads draaiden op 2026-05-20. De laatste paid touch in PostHog dateert van 2026-05-14 (1 pageview met `utm_source=meta`, `utm_content=h11_b3_cta5` op `/booking`), wat een late attribution-hit lijkt te zijn van vóór de pause.

## 3. Landing Page Health
Onder geringe ruimte voor statistische conclusies (slechts 3 sessies). Bounce rate is berekend als sessies met één enkele page-event (geen vervolginteracties geregistreerd).

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 3 | 4,3 | meten | 🟡 |
| Unique visitors | 3 | 3,3 | meten | 🟡 |
| Sessies | 3 | 3,7 | meten | 🟡 |
| Avg Session Duration | 19s | 203s | >90s | 🔴 (gisteren) / 🟢 (7d gem.) |
| Bounce Rate | ~33% | <10% | <55% | 🟢 |
| Scroll 25% / 50% / 75% / 100% | geen data | geen data | >80/60/40/20% | ⚪ niet gemeten |
| CTA Click Rate | 0% | <5% | >4% | 🔴 |
| /booking visits | 0 | 1 (op 17/5) | meten | 🔴 |

**Belangrijke observatie:** Scroll-depth events (`$scroll_depth_25/50/75/100`) en CTA-click events zijn niet aanwezig in het PostHog event-taxonomy van dit project — de scroll/CTA-metrics uit de SKILL kunnen pas worden gerapporteerd zodra deze in de Wix-side tracking worden aangezet (of vervangen door autocapture-elements selector). Zie Acties.

### Traffic Mix gisteren
| Bron | Visits | Pathname | Notitie |
|------|--------|----------|---------|
| Instagram organic (bio_link) | 2 | / | Bio link op @sempertex.europe |
| Facebook organic (bio_link) | 1 | / | Bio link FB-pagina |

### Sessie-detail gisteren
| Sessie | Duur | Events | Bounce? |
|--------|------|--------|---------|
| 03:10 UTC | 20s | 3 | nee |
| 10:07 UTC | 36s | 3 | nee |
| 12:50 UTC | 0s | 1 | ja |

## 4. Funnel Drop-off
Onvoldoende volume om een betrouwbaar funnel-percentage te tonen voor 2026-05-20 alleen. Indicatie op 7-dagen window:

- Pageview op `/` → 28 sessies (100%)
- /product-page bezoek → 1 sessie (~3,6%)
- /booking bezoek → 1 sessie (~3,6%)
- /checkout bezoek → 1 sessie (~3,6%)

**Grootste lek:** verkeer vanuit bio links bekijkt de homepage en verlaat zonder door te klikken. Geen evidente CTA-engagement.

## 5. Rode Vlaggen 🚩
- **🚩 Campagne PAUSED.** Geen paid acquisition sinds minimaal 19-04. Daily report dekt momenteel alleen organisch bio link verkeer; de SYBB-funnel wordt niet gevoed.
- **🚩 Geen scroll-depth tracking.** PostHog `$pageview` event mist `$scroll_*` properties in dit project — landing page-engagement is feitelijk een blackbox tussen pageview en navigate-away.
- **🚩 Geen CTA-click events.** Geen `$autocapture` of custom CTA-click event gevonden in de event taxonomy; CTR op de pagina kan niet gemeten worden.
- **🟡 Sessieduur op 19/5–20/5 fluctueert sterk** (1409s top vs. 0s op gisteren). Met n=3 zegt dat statistisch weinig, maar markeer voor de wekelijkse rollup.

## 6. Top 3 Acties voor Vandaag

1. **Beslis over heractivatie campagne "2026: SYBB".**
   - **Wat:** in Meta Ads Manager checken of de pause bewust is (budget, creatief refresh, juridisch) en zo niet, herstarten met dezelfde h11_b3_cta5 / h12_b3_cta5 hooks die in april liepen.
   - **Waarom:** geen paid spend = funnel staat stil; de Top of Funnel die de hele SYBB-machine voedt is afgeschakeld.
   - **Hoe:** Meta Ads Manager → 2026: SYBB → status check + budget verificatie; daarna activeren.
   - **Verwachte impact:** terugkeer naar ~5-10 paid clicks per dag op €0,40–0,50 CPC (april benchmark).
   - **Escalatie:** Oranje (Robin's beslissing, niet auto).

2. **Activeer scroll-depth + CTA-click tracking op startyourballoonbusiness.com.**
   - **Wat:** PostHog autocapture is wel aan (pageviews komen door), maar `$scroll` en `$autocapture` (clicks) lijken uit te staan of niet getriggerd. Wix-tracking script controleren en `capture_pageview: 'history_change'` + autocapture-clicks aanzetten; alternatief: handmatige `posthog.capture('cta_click', {...})` op de Book Now knop.
   - **Waarom:** zonder scroll/CTA-data kan de SYBB-rapportstructuur niet correct draaien — de meeste rode vlaggen in het rapport zijn onzichtbaar.
   - **Hoe:** Wix Editor → Custom Code → PostHog snippet uitbreiden; of in CTA-buttons custom event toevoegen.
   - **Verwachte impact:** scroll 25/50/75/100% en CTA Click Rate worden meetbaar; rapport krijgt zijn volledige semantiek terug.
   - **Escalatie:** Geel (Robin's goedkeuring, Wix Editor noodzakelijk).

3. **Audit bio link verkeer: wat doen die 3-5 daily visitors?**
   - **Wat:** kijk de session recordings van 19/5–20/5 terug (de 3 langere sessies van 19/5: 1409s, 578s, 179s zijn de moeite). Identificeer of bezoekers naar /product-page of /booking scrollen of vroegtijdig droppen.
   - **Waarom:** organisch bio link verkeer is op dit moment de enige bron — als die converteert is het worth boostend in de social content.
   - **Hoe:** PostHog → Replay → filter `host = www.startyourballoonbusiness.com`, sorteer op duration.
   - **Verwachte impact:** kwalitatief inzicht in wat werkt op de homepage; vorming van hypothese voor pagina-optimalisaties zodra ads weer aan staan.
   - **Escalatie:** Groen (auto, kost 10-15 min).

---

**Bronnen:**
- Meta Ads (Pipeboard MCP): campagne `2026: SYBB` (ID 120239435987290239), account `act_567892422940728`, time_range 2026-05-20 + 7d window
- PostHog MCP: project "Default project" (id 149694), host `www.startyourballoonbusiness.com`, time_range 2026-05-13 → 2026-05-20
