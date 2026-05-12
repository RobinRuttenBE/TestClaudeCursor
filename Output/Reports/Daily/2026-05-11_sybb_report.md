# SYBB Daily Report: 11 May 2026

## 1. Samenvatting

Campagne `2026: SYBB` staat naar verwachting nog steeds op PAUSED (22e dag, sinds 19/20 april), maar de Meta Ads MCP gaf vandaag een "Facebook connection required" foutmelding waardoor geen live ad-data opgehaald kon worden. Op de landing page kwamen 4 pageviews binnen (4 sessies, 4 bounces, 0s gemiddelde duur), waarvan twee op een nieuwe `/review` route. 100% bounce rate, 0 `/booking` views. De vierde achtereenvolgende dag van feitelijke stilstand, en bovenop dat is de Pipeboard token verlopen of disconnected. Twee blokkers tegelijk: de strategische beslissing (relaunch-or-stop) en de tooling-keten.

## 2. Meta Ads Performance

| Metric | Gisteren (11 mei) | 7d Gemiddelde (4-10 mei) | Trend |
|--------|-------------------|---------------------------|-------|
| Spend | n/a (MCP error) | €0,00 (paused) | n/a |
| Impressions | n/a (MCP error) | 0 | n/a |
| Clicks | n/a (MCP error) | 0 | n/a |
| CTR | n/a | n/a | n/a |
| CPC | n/a | n/a | n/a |
| Frequency | n/a | n/a | n/a |

**MCP status:** beide pogingen (`get_ad_accounts`, `get_campaigns`, `get_insights` voor campaign `120239435987290239`) gaven `Facebook connection required. Connect your account at https://pipeboard.co/connections`. De cached Meta API token van Pipeboard is verlopen of de connectie is verbroken. Tot herstel kan geen ad-data (spend, impressies, clicks, frequency, ad-level UTM performance) gemeten worden.

**Context (laatste actieve venster, 11-19 april 2026, 30d aggregates uit voorgaand rapport):**

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

Niet meetbaar. Campagne staat naar verwachting 22 dagen paused (sinds 19 april), en zelfs als er activiteit was kan dit rapport het door de Pipeboard MCP storing niet ophalen. PostHog ziet op 11 mei nul `utm_medium=cpc utm_campaign=sybb` sessies, wat consistent is met een paused campagne.

## 3. Landing Page Health (www.startyourballoonbusiness.com)

| Metric | Gisteren (11 mei) | 7d Gemiddelde (4-10 mei) | Target | Status |
|--------|-------------------|---------------------------|--------|--------|
| Pageviews | 4 | 3,1/dag | n/a | informatief |
| Unique visitors | 4 | 2,6/dag | n/a | informatief |
| Sessions | 4 | 2,6/dag | n/a | informatief |
| Bounce Rate | 100% (4/4) | 77,8% (14/18) | <55% | 🔴 (volume te laag voor signaal) |
| Avg Session Duration | 0s | ~24s | >90s | 🔴 (volume te laag voor signaal) |
| Scroll 25%+ | n/m | n/m | >80% | n/m (geen scroll-events getrackt) |
| Scroll 50%+ | n/m | n/m | >60% | n/m |
| Scroll 75%+ | n/m | n/m | >40% | n/m |
| Scroll 100% | n/m | n/m | >20% | n/m |
| CTA Click Rate | n/m | n/m | >4% | n/m (geen CTA events getrackt) |

**Belangrijk:** PostHog tracking blijft beperkt tot `$pageview` en `$web_vitals`. Scroll milestones en CTA-clicks worden nog steeds niet gevuurd. Engagement-KPI's uit de skill-target tabel zijn niet meetbaar tot scroll- en CTA-tracking opnieuw worden gewired. Dit is dezelfde meet-gap als gisteren en eergisteren.

### Pageviews per dag (4-11 mei)

| Datum | Pageviews | Sessions | Unieke bezoekers | Bounces |
|-------|-----------|----------|------------------|---------|
| 4 mei | 2 | 2 | 2 | 2 |
| 5 mei | 8 | 6 | 6 | 4 |
| 6 mei | 4 | 2 | 2 | 0 |
| 7 mei | 1 | 1 | 1 | 1 |
| 8 mei | 2 | 2 | 2 | 2 |
| 9 mei | 2 | 2 | 2 | 2 |
| 10 mei | 3 | 3 | 3 | 3 |
| **11 mei** | **4** | **4** | **4** | **4** |
| **Totaal 8d** | **26** | **22** | **22** | **18** |

### Trafficbron breakdown (11 mei)

| Bron | Pageviews | Sessions |
|------|-----------|----------|
| direct / no UTM | 3 | 3 |
| instagram / organic / sybb / bio_link | 1 | 1 |
| **Totaal** | **4** | **4** |

Drie van vier sessies zonder UTM. Eén sessie vanuit Manychat bio link (`t-sml.mtrbio.com`) met `utm_source=instagram utm_medium=organic utm_campaign=sybb utm_content=bio_link`. Nul `utm_medium=cpc` sessies, consistent met paused campagne.

### Pagina breakdown (11 mei)

| Pad | Pageviews |
|-----|-----------|
| `/` (landing page) | 2 |
| `/review` | 2 |

**Nieuw signaal:** 2 pageviews op `/review`, twee aparte sessies kort na elkaar (20:36:03 en 20:36:14 UTC, beide $direct referrer). Het pad `/review` kwam in de afgelopen 8 dagen niet eerder voor. Mogelijk een testbezoek van Robin/team of een gedeelde directe link. Beide sessies bouncen direct (0s duur). Geen `/booking`, `/checkout` of conversiestap. Indien dit een nieuw onderdeel van de funnel is verdient het tracking-attentie.

## 4. Funnel Drop-off

Niet betrouwbaar berekenbaar op 11 mei (4 pageviews totaal). Ruwe volume-stappen:

```
Pageview /          2   (50% van totaal)
Pageview /review    2   (50% van totaal)
Pageview /checkout  0   (0%)
Pageview /booking   0   (0%)
```

**Grootste lek:** zonder ad-instroom en zonder scroll/CTA-events is er geen funnel om over te diagnosticeren. Alle 4 sessies eindigden op één pagina. Met 0 `/booking` views over 8 opeenvolgende dagen is de workshop-funnel volledig stil.

## 5. Rode Vlaggen 🚩

- 🚩 **Pipeboard Meta Ads MCP gaf vandaag een "Facebook connection required" error.** Tot herstel kan deze rapportflow geen Meta Ads data ophalen. Reconnect via https://pipeboard.co/connections of refresh van het cached access token nodig. Sinds yesterday's rapport (10 mei) wel werkte, is dit een verse degradatie.
- 🚩 **Campagne 22 dagen paused** (sinds 19 april). Vierde achtereenvolgende dag van stilstand-rapport, zelfde pijplijn-derving van ruwweg €40-50/dag aan voorbije traffic en pixel-warmte-verlies.
- 🚩 **100% bounce rate op 11 mei (4/4 sessies, 0s avg duur).** Volumes blijven te laag voor statistisch signaal, maar 18 bounces op 22 sessies over 8 dagen (77,8% bounce) bevestigt dat de pagina structureel niet engaget. Op 6 mei waren er nog 2 sessies zonder bounce, daarna alleen nog full-bounce dagen.
- 🚩 **Nieuwe `/review` pageviews zonder context.** Twee sessies op `/review` binnen 11 seconden, $direct referrer, beide bouncen. Onbekend of dit een interne test, een gedeelde link, of een nieuwe ongetrackte route is. Indien functioneel onderdeel van de funnel: tracking incompleet.
- 🚩 **Geen scroll- of CTA-tracking events binnen.** Onveranderd sinds gisteren. Bij relaunch is dit een blokkerende meet-gap (zie actie #2).
- 🚩 **Zero `/booking` of `/checkout` events** voor de 8e dag op rij. Workshop-funnel volledig stil.

## 6. Top 3 Acties voor Vandaag

1. **Repareer de Pipeboard Meta Ads MCP connectie vóór 13 mei.**
   - **Wat:** ga naar https://pipeboard.co/connections, reconnect het Meta/Facebook account, en valideer met een test-call (`get_ad_accounts`) dat de cached token weer geldig is.
   - **Waarom:** zonder werkende Meta Ads MCP draait deze rapportflow blind voor ad-data. Als de campagne deze week relauncht (zie actie #3) kan dat niet zonder dagelijkse spend/CPC/frequency tracking. Dit blokkeert ook `/morning-report`, `/ads-report`, `/ads-optimize` en `/ads-auto-optimize`.
   - **Verwachte impact:** herstel van alle Meta Ads gedreven rapportages binnen 1 dag.
   - **Escalatie:** 🟡 Robin handmatig reconnect via Pipeboard UI.

2. **Onderzoek de twee `/review` pageviews van 11 mei.**
   - **Wat:** check Wix Editor of er een `/review` route bestaat, wat erop staat, en of er PostHog tracking events op gedefinieerd zijn. Bepaal of dit een nieuwe funnel-stap is, een testpagina, of dead weight.
   - **Waarom:** `/review` is in 8 dagen niet eerder verschenen en pop't nu twee keer binnen 11 seconden op met directe referrer. Als dit een actieve route is (bv. testimonials, social proof, vroege funnel-stap), moet hij meegenomen worden in de funnel-definitie. Als hij verouderd is, doodlinken of redirecten.
   - **Hoe:** Wix Editor → Pages, zoek `/review`. Trek de huidige HTML/component op. Plaats PostHog scroll- en CTA-tracking als hij behouden blijft.
   - **Verwachte impact:** funnel-definitie wordt actueel; voorkomt dat we straks 5% extra traffic missen in alle conversie-berekeningen.
   - **Escalatie:** 🟡 Robin checkt zelf in Wix Editor.

3. **Forceer vandaag de relaunch-of-stop beslissing voor SYBB campagne én wire scroll/CTA tracking voordat de relaunch live gaat.**
   - **Wat:** beslis (a) relaunch op 13 mei met 2-3 nieuwe creatives, of (b) volledige stop en verwijder SYBB uit dagelijks rapport. Onafhankelijk van die keuze: voeg `posthog.capture('scroll_milestone', {pct: 25/50/75/100})` toe via scroll listener en `posthog.capture('cta_click', {cta_id: ...})` op alle "Book Now" knoppen.
   - **Waarom:** 22 dagen paused = vierde dag stilstand-rapport. Iedere dag uitstel kost ~€40-50 aan gederfde pijplijn plus pixel-warmte-verlies voor retargeting. Zonder scroll/CTA tracking blijft het rapport bij relaunch alsnog "n/m" voor 4 van 8 KPI's en is optimalisatie gokwerk.
   - **Hoe:** bij relaunch — nieuwe ads klaar voor 13 mei met UTM-conventie `utm_source=meta utm_medium=cpc utm_campaign=sybb utm_content=hXX_bX_ctaX utm_term=batch_4`, budget ≥€70/dag, 14d evaluatievenster. Tracking-events via Wix custom code, verifieer in PostHog Activity feed binnen 1 uur na deploy. Coördineer met actie #1 zodat Meta Ads MCP weer leeft.
   - **Verwachte impact:** elimineert lege rapportcyclus; bij relaunch herstel naar ~100 pageviews/dag binnen week 1, met betekenisvolle scroll/CTA data vanaf dag 1.
   - **Escalatie:** 🟠 Robin (strategie + budget + tracking-deploy).

---

**Data sources:** Meta Ads MCP (Pipeboard) — **niet beschikbaar vandaag** (Facebook connection required). Account `act_567892422940728`, campaign `120239435987290239` ("2026: SYBB") referenties uit voorgaand rapport (10 mei). PostHog MCP, project `Default project` (id 149694), host `www.startyourballoonbusiness.com`.

**Geen Google Sheets, Drive, Gmail, Calendar, Docs of Slides aangeroepen voor dit rapport.**
