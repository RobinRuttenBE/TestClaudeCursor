# SYBB Daily Report, 2 augustus 2026

**Databronnen:** Meta Ads MCP (Pipeboard), campagne `2026: SYBB` (id `120239435987290239`, account `act_567892422940728`) en PostHog MCP (project "Default project", id 149694, org Sempertex Europe, timezone UTC).
**Peildatum:** zaterdag 2 augustus 2026. Vergelijkingsvenster: 27 juli t/m 2 augustus 2026.

---

## 1. Samenvatting

De SYBB funnel staat volledig stil. De campagne `2026: SYBB` staat op PAUSED en heeft op 2 augustus nul spend, nul impressies en nul clicks, net als op elke andere dag in de afgelopen 7 dagen. De laatste dag met werkelijke ad delivery was in april 2026, ruim drie maanden geleden.

Aan de landing page kant hetzelfde beeld: PostHog registreerde op 2 augustus **nul pageviews** op `www.startyourballoonbusiness.com`. Over het hele 7-daagse venster kwamen er 3 pageviews van 3 bezoekers binnen, allemaal direct verkeer, geen enkele vanuit Meta.

Belangrijker dan de nul-cijfers is wat de tracking-audit oplevert: **de meetopstelling die dit rapport veronderstelt bestaat niet in PostHog.** Er is geen scroll depth event, geen CTA click event en geen enkele UTM parameter wordt op `$pageview` vastgelegd. Zolang dat zo blijft, kan een groot deel van de tabellen hieronder ook bij herstart van de campagne niet gevuld worden.

---

## 2. Meta Ads Performance

| Metric | Gisteren (2 aug) | 7d gemiddelde (27 jul t/m 2 aug) | Trend |
|--------|------------------|----------------------------------|-------|
| Spend | € 0,00 | € 0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

Meta gaf voor alle 7 dagen een lege dataset terug. Campagnestatus PAUSED, daily budget staat nog ingesteld op € 100,00, laatste wijziging 19 april 2026.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | niet gemeten |
| h12_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | niet gemeten |
| h13_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | niet gemeten |
| h14_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | niet gemeten |
| h15_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | niet gemeten |

**Beste variant:** niet vast te stellen, geen delivery.
**Slechtste variant:** niet vast te stellen, geen delivery.

### Laatst bekende performance, als referentiepunt

Omdat de dagcijfers leeg zijn, hieronder wat de campagne wél heeft gedaan sinds de start op 13 januari 2026.

| Periode | Spend | Impressies | Clicks | CTR | CPC | CPM | Frequency |
|---------|-------|-----------|--------|-----|-----|-----|-----------|
| Jan (v.a. 13 jan) | € 101,74 | 16.268 | 167 | 1,03% | € 0,61 | € 6,25 | 1,81 |
| Feb | geen delivery | 0 | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. |
| Mrt | € 1.323,83 | 189.067 | 9.965 | 5,27% | € 0,13 | € 7,00 | 2,07 |
| Apr | € 1.059,47 | 91.839 | 1.935 | 2,11% | € 0,55 | € 11,54 | 2,19 |
| Mei t/m 2 aug | geen delivery | 0 | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. |
| **Totaal** | **€ 2.485,04** | **297.174** | **12.067** | **4,06%** | **€ 0,21** | **€ 8,36** | **2,09** |

Maart was de sterkste maand op elke KPI. April verdubbelde de CPM en verviervoudigde de CPC bij een frequency van 2,19, dus die kostenstijging kwam niet van ad fatigue.

---

## 3. Landing Page Health

| Metric | Gisteren (2 aug) | 7d gemiddelde | Target | Status |
|--------|------------------|---------------|--------|--------|
| Pageviews | 0 | 0,4 per dag | meten | 🔴 |
| Unieke bezoekers | 0 | 0,4 per dag | meten | 🔴 |
| Bounce Rate | geen data | geen data | <55% | ⚫ |
| Avg Session Duration | geen data | geen data | >90s | ⚫ |
| Scroll 25% | niet gemeten | niet gemeten | >80% | ⚫ |
| Scroll 50% | niet gemeten | niet gemeten | >60% | ⚫ |
| Scroll 75% | niet gemeten | niet gemeten | >40% | ⚫ |
| Scroll 100% | niet gemeten | niet gemeten | >20% | ⚫ |
| CTA Click Rate | niet gemeten | niet gemeten | >4% | ⚫ |

Legenda: 🟢 op of boven target, 🟡 binnen 20% van target, 🔴 meer dan 20% onder target, ⚫ event bestaat niet in PostHog of te weinig volume voor een betrouwbaar cijfer.

### Verkeer per dag op startyourballoonbusiness.com

| Dag | Pageviews | Unieke bezoekers |
|-----|-----------|------------------|
| 27 jul | 1 | 1 |
| 28 jul | 0 | 0 |
| 29 jul | 1 | 1 |
| 30 jul | 0 | 0 |
| 31 jul | 1 | 1 |
| 1 aug | 0 | 0 |
| **2 aug** | **0** | **0** |

Over de laatste 30 dagen (4 juli t/m 2 augustus): 46 pageviews in totaal. Ter vergelijking, de webshop `www.sempertexeurope.com` deed op 2 augustus 3.256 pageviews van 748 bezoekers in hetzelfde PostHog project. De SYBB pagina is dus goed aangesloten op PostHog, er komt alleen vrijwel niemand.

### UTM segmentatie

Niet mogelijk. PostHog legt op `$pageview` geen enkele UTM property vast (`utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term` ontbreken allemaal in de event taxonomy). De hele UTM conventie uit CLAUDE.md, `utm_content=hXX_bX_ctaX`, komt dus nergens in de analytics terecht. Cross-referencing per ad variant is daarmee onmogelijk, ook bij volle campagne.

Wat wel meetbaar is, is de referring domain. Over de laatste 60 dagen:

| Referrer | Pageviews | Personen | Laatst gezien |
|----------|-----------|----------|---------------|
| `$direct` | 70 | 70 | 31 jul |
| `t-sml.mtrbio.com` (Metricool link-in-bio) | 21 | 17 | 14 jul |
| `www.startyourballoonbusiness.com` (intern) | 1 | 1 | 1 jul |

Geen enkele pageview vanaf `facebook.com` of `instagram.com`. Consistent met nul ad delivery.

---

## 4. Funnel Drop-off

Op 2 augustus is elke stap nul. Hieronder daarom het 60-daagse venster (4 juni t/m 2 augustus), het kleinste venster met genoeg volume om iets te zien.

```
Pageview homepage       91  (100%)
   ↓  -95,6%
Scroll 50%              niet gemeten
   ↓
CTA click               niet gemeten
   ↓
Pageview /checkout       4  (4,4%)
   ↓  -75,0%
Pageview /booking        1  (1,1%)
```

**Grootste lek:** de homepage zelf. Van 91 bezoeken bereiken er 4 de checkout. Maar met 91 pageviews over twee maanden is dat statistisch niets waard, en de twee middelste stappen ontbreken volledig, dus de echte diagnose is niet te stellen.

Wat wél opvalt in de laatst bekende ads-data: in maart telde Meta 9.703 link clicks tegen 6.174 landing page views, een verlies van 36% tussen klik en geladen pagina. In april 1.036 link clicks tegen 818 landing page views, 21% verlies. Dat is een laadtijd- of redirect-probleem op de pagina zelf, geen creative-probleem, en het staat los van de campagnestop.

---

## 5. Rode Vlaggen 🚩

1. **Campagne staat 3+ maanden stil.** Laatste delivery april 2026, status PAUSED, budget nog wel ingesteld. Elke week extra stilstand veroudert de pixel-signalen en maakt een nieuwe learning phase duurder.
2. **Nul landing page verkeer op de rapportdag.** 0 pageviews op 2 augustus, 3 in zeven dagen. Onder elke drempel waarop een KPI betekenis heeft.
3. **Geen scroll depth tracking.** Er bestaat geen scroll event in het PostHog project. Vier van de zeven KPI-rijen in de skill kunnen structureel niet gevuld worden.
4. **Geen CTA click tracking op de SYBB pagina.** De enige click-events in het project (`video_click`, `instagram_click`, `social_click`) vuren op de webshop, niet op SYBB. CTA Click Rate is niet berekenbaar.
5. **Geen UTM capture.** Zonder `utm_content` in PostHog is de koppeling ad variant naar paginagedrag, het hele punt van dit rapport, onmogelijk.
6. **Pixel-waardes kloppen niet.** April rapporteert 6 purchases met € 44.247,00 totaalwaarde, dus € 7.374,50 per SYBB-ticket, plus € 86.100,00 op `complete_registration`. Elke ROAS-beslissing op basis hiervan is giswerk.
7. **36% verlies tussen link click en landing page view** in maart, 21% in april. Wijst op traagheid of een redirect-stap op de pagina.

Niet van toepassing vandaag: CPC-stijging, bounce rate per UTM segment, frequency boven 3,0. Alle drie vereisen delivery die er niet is.

---

## 6. Top 3 Acties voor Vandaag

### 1. Zet scroll depth, CTA click en UTM capture aan in PostHog

- **Wat:** voeg aan `www.startyourballoonbusiness.com` een scroll depth event toe op 25/50/75/100%, een click event op de Book Now CTA, en zorg dat posthog-js de UTM parameters uit de URL meestuurt op `$pageview`.
- **Waarom:** vandaag zijn 5 van de 12 KPI-rijen in dit rapport niet meetbaar, en de UTM-koppeling die de cross-reference tussen Meta en PostHog mogelijk maakt bestaat niet. Herstart van de campagne zonder deze fix levert opnieuw een half rapport op.
- **Hoe:** aanpassing in de PostHog snippet op de landing page (Wix Editor of via de PostHog toolbar autocapture-actie voor de CTA).
- **Verwachte impact:** dit rapport wordt van ongeveer 40% gevuld naar volledig, en ad-variant-analyse per `utm_content` wordt mogelijk.
- **Escalatie:** 🟠 Oranje, vereist Wix Editor toegang.

### 2. Fix de pixel purchase values vóór de herstart

- **Wat:** corrigeer de waarde die de Meta pixel meestuurt bij `purchase` en `complete_registration` op de checkout.
- **Waarom:** € 7.374,50 per verkocht ticket en € 86.100,00 op registraties zijn onmogelijk. De ROAS die Meta rapporteert is daarmee waardeloos, en Meta optimaliseert de campagne op dat signaal.
- **Hoe:** Meta Events Manager, controleer de value parameter bij het purchase event, daarna testen met de Pixel Helper.
- **Verwachte impact:** betrouwbare ROAS, en Meta's algoritme optimaliseert weer op echte waarde in plaats van ruis.
- **Escalatie:** 🟡 Geel, Robin beslist wanneer.

### 3. Beslis over de herstart, en herstart dan op de bewezen ad set

- **Wat:** kies een startdatum voor `2026: SYBB` en zet die aan met de originele BATCH 2 ad set, niet met de gedupliceerde campagne `2026: SYBB - Kopie`.
- **Waarom:** maart draaide op CPC € 0,13 en CTR 5,27% via BATCH 2. April, na het dupliceren van ad sets, ging naar CPC € 0,55 en CPM € 11,54 bij een frequency van slechts 2,19. Het verschil zit in de duplicaten, niet in de hooks of in verzadiging.
- **Hoe:** Meta Ads Manager, campagne 120239435987290239 op ACTIVE, kopie-campagne archiveren. Volg 70-20-10: 70% op de bewezen hooks uit BATCH 2, 20% varianten op dezelfde B3 body en CTA5, 10% één nieuwe angle.
- **Verwachte impact:** terug naar het maart-niveau qua CPC in plaats van opnieuw beginnen op april-kosten.
- **Escalatie:** 🔴 Rood, strategische beslissing met budget-impact.

Volgorde is bewust: actie 1 en 2 zijn meetwerk dat af moet zijn vóór actie 3, anders koop je opnieuw verkeer dat je niet kunt lezen.

---

## Verantwoording databronnen

Dit rapport gebruikt uitsluitend de Meta Ads MCP (Pipeboard) en de PostHog MCP. Er is geen enkele Google MCP aangeroepen (Gmail, Calendar, Drive, Sheets, Docs, Slides) en er is niet naar de Meta Ads Tracker Google Sheet geschreven. Output staat alleen lokaal in `Output/Reports/Daily/2026-08-02_sybb_report.md`.
