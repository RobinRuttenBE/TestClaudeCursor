# SYBB Daily Report: 10 May 2026

## 1. Samenvatting

Campagne `2026: SYBB` staat nu 21 dagen op PAUSED (sinds 19/20 april). Gisteren opnieuw geen Meta Ads activiteit (€0 spend, 0 impressies, 0 clicks). Landing page kreeg 3 pageviews, allemaal direct verkeer zonder UTM, alle 3 sessies bouncen direct. Derde achtereenvolgende dag dat dit rapport in feite een stilstand-rapport is. De relaunch-of-stop beslissing is nu kritiek geworden, het venster om data te verzamelen voor een nieuwe seizoens-piek loopt vast.

## 2. Meta Ads Performance

| Metric | Gisteren (10 mei) | 7d Gemiddelde (3-9 mei) | Trend |
|--------|-------------------|--------------------------|-------|
| Spend | €0,00 | €0,00 | → (paused) |
| Impressions | 0 | 0 | → (paused) |
| Clicks | 0 | 0 | → (paused) |
| CTR | n/a | n/a | n/a |
| CPC | n/a | n/a | n/a |
| Frequency | n/a | n/a | n/a |

**Context (laatste actieve venster, 11-19 april 2026, 30d aggregates):**

| Metric | Waarde | Target | Status |
|--------|--------|--------|--------|
| Spend totaal | €872,28 | n/a | informatief |
| Impressions | 68.069 | n/a | informatief |
| Clicks | 1.433 | n/a | informatief |
| Reach | 46.145 | n/a | informatief |
| CTR | 2,11% | >1% | 🟢 |
| CPC | €0,61 | <€0,50 | 🔴 22% boven target |
| CPM | €12,81 | n/a | informatief |
| Frequency | 1,48 | <3,0 | 🟢 |

### Ad Variant Performance

Niet van toepassing voor 10 mei (campagne paused, 0 ads serveerden, 0 utm_content varianten in PostHog op deze datum).

## 3. Landing Page Health (www.startyourballoonbusiness.com)

| Metric | Gisteren (10 mei) | 7d Gemiddelde (3-9 mei) | Target | Status |
|--------|-------------------|--------------------------|--------|--------|
| Pageviews | 3 | 3,0/dag | n/a | informatief |
| Unique visitors | 3 | ~2,3/dag | n/a | informatief |
| Sessions | 3 | 2,3/dag | n/a | informatief |
| Bounce Rate | 100% | 68,8% | <55% | 🔴 (volume te laag voor signaal) |
| Avg Session Duration | 0s | 54,7s | >90s | 🔴 (volume te laag voor signaal) |
| Scroll 25%+ | n/m | n/m | >80% | n/m (geen scroll-events getrackt) |
| Scroll 50%+ | n/m | n/m | >60% | n/m |
| CTA Click Rate | n/m | n/m | >4% | n/m (geen CTA events getrackt) |

**Belangrijk:** met 3 pageviews op 10 mei en 21 over 3-9 mei is alle ratio-data statistisch betekenisloos. PostHog tracking op de landing page bevat momenteel alleen `$pageview` en `$web_vitals` events, geen scroll milestones of CTA-clicks. Engagement-KPI's uit de skill-target tabel zijn dus niet meetbaar tot scroll- en CTA-tracking opnieuw gewired wordt.

### Pageviews per dag (3-10 mei)

| Datum | Pageviews | Sessions | Unieke bezoekers |
|-------|-----------|----------|------------------|
| 3 mei | 2 | 1 | 1 |
| 4 mei | 2 | 2 | 2 |
| 5 mei | 8 | 6 | 6 |
| 6 mei | 4 | 2 | 2 |
| 7 mei | 1 | 1 | 1 |
| 8 mei | 2 | 2 | 2 |
| 9 mei | 2 | 2 | 2 |
| **10 mei** | **3** | **3** | **3** |
| **Totaal 8d** | **24** | **19** | **19** |

### Trafficbron breakdown (10 mei)

| Bron | Pageviews | Sessions |
|------|-----------|----------|
| direct / no UTM | 3 | 3 |
| **Totaal** | **3** | **3** |

100% van het verkeer op 10 mei was direct, zonder UTM-tagging. Geen Meta-, Instagram-, of Facebook-attributie. Bio link traffic, dat in voorgaande dagen 60% van het organisch volume leverde, is op 10 mei niet zichtbaar in de UTM-data.

### Pagina breakdown (10 mei)

| Pad | Pageviews |
|-----|-----------|
| `/` (landing page) | 3 |

Alle 3 pageviews op de homepage. Geen `/checkout`, `/review`, of `/booking` pageviews. Funnel-vervolg vond niet plaats.

## 4. Funnel Drop-off

Niet betrouwbaar berekenbaar op 10 mei. Ruwe volume-stappen:

```
Pageview /          3   (100%)
Pageview /checkout  0   (0%)
Pageview /review    0   (0%)
Pageview /booking   0   (0%)
```

**Grootste lek:** geen ad delivery dus geen instroom om een lek over te detecteren. Zelfs het kleine bio link / direct verkeer dat vorige week nog 3 `/checkout` views over 8 dagen genereerde, viel gisteren weg.

## 5. Rode Vlaggen 🚩

- 🚩 **Campagne 21 dagen paused.** Sinds 19 april geen ad spend, dus geen attribuable conversies, geen pixel-warmte opbouw, geen retargeting pool refresh. Op basis van het april-venster betekent dit ruwweg €40-50/dag aan gederfde traffic en pijplijn.
- 🚩 **100% bounce rate op 10 mei (3/3 sessies, 0s avg duur).** Met 3 sessies geen statistisch signaal, maar het patroon van 8 dagen op rij sub-10 pageviews bevestigt dat de landing page feitelijk niet wordt bezocht.
- 🚩 **Geen scroll- of CTA-tracking events binnen.** Alleen `$pageview` en `$web_vitals`. De skill-target KPI's voor scroll depth en CTA click rate zijn niet meetbaar; bij relaunch is dit een blokkerende meet-gap.
- 🚩 **Zero `/booking`, `/checkout`, `/review` events op 10 mei.** Workshop-funnel volledig stil; geen enkel conversiesignaal, geen warm publiek opgebouwd.
- 🚩 **CPC tijdens laatste actieve venster (€0,61) lag 22% boven target.** Zonder creative refresh blijft dit punt onverbeterd bij relaunch.
- 🚩 **Derde dag op rij identiek "stilstand"-rapport.** Iedere dag dat dit rapport draait zonder beslissing is verspilde meet-cyclus.

## 6. Top 3 Acties voor Vandaag

1. **Forceer vandaag de relaunch-of-stop beslissing voor SYBB campagne.**
   - **Waarom:** 21 dagen paused, derde achtereenvolgende dag met identiek stilstand-rapport. Iedere dag uitstel kost ~€40-50 aan gederfde pijplijn op basis van het april-venster, plus verlies van pixel-warmte voor retargeting.
   - **Hoe:** Robin neemt vandaag besluit. Bij relaunch: nieuwe creatives klaar voor 13 mei, budget set op minimaal €70/dag, geplande continu-loop van 14 dagen voor evaluatie. Bij stop: SYBB uit dagelijkse morning report flow halen tot nieuw besluit; vervang de slot in het rapport met een actieve campagne.
   - **Verwachte impact:** elimineert lege rapportcyclus; bij relaunch herstel naar ~100 pageviews/dag binnen week 1.
   - **Escalatie:** 🟠 Robin (strategie + budget).

2. **Wire scroll- en CTA-tracking events op www.startyourballoonbusiness.com voordat de campagne relauncht.**
   - **Waarom:** PostHog ontvangt momenteel alleen `$pageview` en `$web_vitals`. Drie van de zeven KPI-targets in de skill (Scroll 25/50/75%, CTA Click Rate) zijn dus structureel niet meetbaar. Bij relaunch zonder deze events draait het rapport opnieuw met "n/m" velden en blijft optimalisatie gokwerk.
   - **Hoe:** check de Wix custom code voor PostHog snippet, voeg `posthog.capture('scroll_milestone', {pct: 25/50/75/100})` toe via scroll listener, en `posthog.capture('cta_click', {cta_id: ...})` op alle "Book now" knoppen. Verifieer in PostHog Activity feed binnen 1 uur na deploy.
   - **Verwachte impact:** scroll depth en CTA click rate beschikbaar in volgend rapport; betekenisvolle ad-vs-page diagnose mogelijk vanaf relaunch dag 1.
   - **Escalatie:** 🟠 Robin laat dit doen door technical resource (Wix Editor + custom code).

3. **Plan voor relaunch: 2-3 nieuwe ad creatives op basis van laatste actieve venster, mét UTM-conventie volgens CLAUDE.md.**
   - **Waarom:** CPC zat op €0,61 (22% boven target) en relaunch met identieke creatives loopt vrijwel direct in ad fatigue (frequency was al 1,48 op 30d). Tegelijk: 0 UTM-getagde sessies op 10 mei toont dat zelfs als verkeer zou binnenkomen, attributie momenteel ontbreekt.
   - **Hoe:** kies 2-3 best presterende `utm_content` varianten uit april-batch (h11-h15_b3_cta5), bouw daar nieuwe hooks bij op basis van `Bronnen/Sempertex Europe/sybb-8-pillars.md`. Tag elke ad met UTM-conventie `utm_source=meta utm_medium=cpc utm_campaign=sybb utm_content=hXX_bX_ctaX utm_term=batch_4`. Lever vóór 13 mei aan.
   - **Verwachte impact:** CPC terug richting <€0,50, full UTM-attributie in rapporten vanaf relaunch dag 1, frequency onder 2,0 in eerste 14 dagen.
   - **Escalatie:** 🟡 Robin goedkeuring voor briefing en oplevering.

---

**Data sources:** Meta Ads MCP (Pipeboard), account `act_567892422940728`, campaign `120239435987290239` ("2026: SYBB"). PostHog MCP, project `Default project` (id 149694), host `www.startyourballoonbusiness.com`.

**Geen Google Sheets, Drive, Gmail, Calendar, Docs of Slides aangeroepen voor dit rapport.**
