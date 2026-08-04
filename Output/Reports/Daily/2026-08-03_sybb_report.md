# SYBB Daily Report, 3 augustus 2026

**Databronnen:** Meta Ads MCP (Pipeboard), campagne `2026: SYBB` (id `120239435987290239`, account `act_567892422940728`, Sempertex Ad Account) en PostHog MCP (project "STX EU", id 149694, org Sempertex Europe, timezone UTC).
**Peildatum:** maandag 3 augustus 2026. Vergelijkingsvenster: 28 juli t/m 3 augustus 2026.

> Naamswijziging: het PostHog project dat in eerdere rapporten "Default project" heette, heet nu "STX EU". Zelfde project id (149694), zelfde data.

---

## 1. Samenvatting

Geen enkele verandering ten opzichte van gisteren. De campagne `2026: SYBB` staat nog steeds op PAUSED en leverde op 3 augustus, net als op alle zes voorgaande dagen, nul spend, nul impressies en nul clicks. De laatste dag met echte ad delivery ligt in april 2026, inmiddels ruim drie en een halve maand geleden.

Aan de landing page kant idem: PostHog registreerde op 3 augustus **nul pageviews** op `www.startyourballoonbusiness.com`. Over het hele 7-daagse venster kwamen er 2 pageviews binnen van 2 bezoekers, beide direct verkeer, geen enkele vanuit Meta.

De drie acties uit het rapport van 2 augustus (tracking fixen, pixel values fixen, herstart-beslissing) staan alle drie nog volledig open. De meetopstelling die dit rapport veronderstelt bestaat nog steeds niet: geen scroll depth event, geen CTA click event, geen enkele UTM parameter op `$pageview`. Elke dag dat dit blijft liggen is een dag waarop een herstart opnieuw onleesbaar verkeer oplevert.

---

## 2. Meta Ads Performance

| Metric | Gisteren (3 aug) | 7d gemiddelde (28 jul t/m 3 aug) | Trend |
|--------|------------------|-----------------------------------|-------|
| Spend | € 0,00 | € 0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

Meta gaf voor alle 7 dagen een lege dataset terug. Campagnestatus PAUSED, objective OUTCOME_SALES, daily budget staat nog ingesteld op € 100,00, budget_remaining € 100,00, laatste wijziging 19 april 2026.

De gedupliceerde campagne `2026: SYBB - Kopie` (id `120243293329420239`) staat eveneens op PAUSED, laatste wijziging 20 april 2026. Ook daar nul delivery.

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

Ook bij herstart blijven de kolommen LP Bounce en LP Scroll leeg zolang PostHog geen `utm_content` vastlegt. Zie actie 1.

### Laatst bekende performance, als referentiepunt

Omdat de dagcijfers leeg zijn, hieronder wat de campagne wél heeft gedaan sinds de start op 13 januari 2026.

| Periode | Spend | Impressies | Clicks | CTR | CPC | CPM | Frequency |
|---------|-------|-----------|--------|-----|-----|-----|-----------|
| Jan (v.a. 13 jan) | € 101,74 | 16.268 | 167 | 1,03% | € 0,61 | € 6,25 | 1,81 |
| Feb | geen delivery | 0 | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. |
| Mrt | € 1.323,83 | 189.067 | 9.965 | 5,27% | € 0,13 | € 7,00 | 2,07 |
| Apr | € 1.059,47 | 91.839 | 1.935 | 2,11% | € 0,55 | € 11,54 | 2,19 |
| Mei t/m 3 aug | geen delivery | 0 | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. |
| **Totaal** | **€ 2.485,04** | **297.174** | **12.067** | **4,06%** | **€ 0,21** | **€ 8,36** | **2,09** |

Maart blijft de sterkste maand op elke KPI, met een CPC van € 0,13 tegen een target van € 0,50. April verdubbelde de CPM en verviervoudigde de CPC bij een frequency van slechts 2,19, dus die kostenstijging kwam niet van ad fatigue. Het verschil zit in de ad set structuur, niet in verzadiging.

---

## 3. Landing Page Health

| Metric | Gisteren (3 aug) | 7d gemiddelde | Target | Status |
|--------|------------------|---------------|--------|--------|
| Pageviews | 0 | 0,3 per dag | meten | 🔴 |
| Unieke bezoekers | 0 | 0,3 per dag | meten | 🔴 |
| Bounce Rate | geen data | geen data | <55% | ⚫ |
| Avg Session Duration | geen data | geen data | >90s | ⚫ |
| Scroll 25% | niet gemeten | niet gemeten | >80% | ⚫ |
| Scroll 50% | niet gemeten | niet gemeten | >60% | ⚫ |
| Scroll 75% | niet gemeten | niet gemeten | >40% | ⚫ |
| Scroll 100% | niet gemeten | niet gemeten | >20% | ⚫ |
| CTA Click Rate | niet gemeten | niet gemeten | >4% | ⚫ |

Legenda: 🟢 op of boven target, 🟡 binnen 20% van target, 🔴 meer dan 20% onder target, ⚫ event bestaat niet in PostHog of te weinig volume voor een betrouwbaar cijfer.

### Verkeer per dag op startyourballoonbusiness.com

| Dag | Pageviews | Unieke bezoekers | Sessies |
|-----|-----------|------------------|---------|
| 28 jul | 0 | 0 | 0 |
| 29 jul | 1 | 1 | 1 |
| 30 jul | 0 | 0 | 0 |
| 31 jul | 1 | 1 | 1 |
| 1 aug | 0 | 0 | 0 |
| 2 aug | 0 | 0 | 0 |
| **3 aug** | **0** | **0** | **0** |
| **Totaal 7d** | **2** | **2** | **2** |

Over de laatste 30 dagen (5 juli t/m 3 augustus): 44 pageviews, 41 unieke bezoekers, 41 sessies. Gemiddeld 1,5 pageview per dag.

### Is de tracking wel in orde?

Ja. Ter controle het verkeer op de webshop in hetzelfde PostHog project, over hetzelfde venster:

| Dag | SYBB pageviews | Webshop pageviews | Webshop bezoekers |
|-----|----------------|-------------------|-------------------|
| 28 jul | 0 | 5.832 | 820 |
| 29 jul | 1 | 6.743 | 947 |
| 30 jul | 0 | 3.908 | 862 |
| 31 jul | 1 | 3.716 | 813 |
| 1 aug | 0 | 2.668 | 675 |
| 2 aug | 0 | 3.256 | 748 |
| **3 aug** | **0** | **5.540** | **1.213** |

PostHog ingestie is volledig gezond, met 5.540 pageviews op 3 augustus vanaf `www.sempertexeurope.com`. De nul op SYBB is dus geen meetfout. Er komt letterlijk niemand.

### UTM segmentatie

Nog steeds niet mogelijk. Ik heb de event taxonomy van `$pageview` opnieuw gecontroleerd: geen enkele UTM property wordt vastgelegd (`utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term` ontbreken allemaal). De hele UTM conventie uit CLAUDE.md, `utm_content=hXX_bX_ctaX`, komt nergens in de analytics terecht.

Wat wel meetbaar is, is de referring domain. Over de laatste 60 dagen (4 juni t/m 3 augustus):

| Referrer | Pageviews | Personen | Laatst gezien |
|----------|-----------|----------|---------------|
| `$direct` | 69 | 68 | 31 jul |
| `t-sml.mtrbio.com` (Metricool link-in-bio) | 21 | 15 | 14 jul |
| `www.startyourballoonbusiness.com` (intern) | 1 | 1 | 1 jul |

Geen enkele pageview vanaf `facebook.com` of `instagram.com`. Consistent met nul ad delivery.

### Session recordings

Nul nieuwe recordings op de SYBB pagina in het 7-daagse venster. Alle 20 meest recente recordings in het project starten op `www.sempertexeurope.com`, geen enkele op SYBB. Geen rage clicks op SYBB in de afgelopen 60 dagen. De events `$dead_click` en `$exception` bestaan niet in dit project, dus dead clicks en JavaScript errors zijn structureel niet te rapporteren.

---

## 4. Funnel Drop-off

Op 3 augustus is elke stap nul. Hieronder daarom het 60-daagse venster (4 juni t/m 3 augustus), het kleinste venster met enigszins bruikbaar volume.

```
Pageview homepage (/)     86  (100%)
   ↓  -95,3%
Scroll 50%                niet gemeten
   ↓
CTA click                 niet gemeten
   ↓
Pageview /checkout         4  (4,7%)
   ↓  -75,0%
Pageview /booking          1  (1,2%)
```

**Grootste lek:** de homepage zelf. Van 86 bezoeken bereiken er 4 de checkout. Maar met 86 pageviews over twee maanden is dat statistisch waardeloos, en de twee middelste stappen ontbreken volledig, dus een echte diagnose is niet te stellen.

Wat wél hard is, komt uit de laatst bekende ads-data:

| Maand | Link clicks | Landing page views | Verlies |
|-------|-------------|--------------------|---------|
| Mrt | 9.703 | 6.174 | 36,4% |
| Apr | 1.036 | 818 | 21,0% |

Ruim een derde van de betaalde clicks in maart bereikte de pagina nooit. Dat is een laadtijd- of redirect-probleem op de pagina zelf, geen creative-probleem, en het staat los van de campagnestop. Bij een herstart op maart-volume betekent 36% verlies ongeveer € 480 aan weggegooid budget per maand.

---

## 5. Rode Vlaggen 🚩

1. **Campagne staat 3,5 maand stil.** Laatste delivery april 2026, status PAUSED, budget nog wel ingesteld op € 100 per dag. Elke week extra stilstand veroudert de pixel-signalen en maakt een nieuwe learning phase duurder.
2. **Nul landing page verkeer op de rapportdag.** 0 pageviews op 3 augustus, 2 in zeven dagen. Onder elke drempel waarop een KPI betekenis heeft.
3. **Geen scroll depth tracking.** Er bestaat geen scroll event in het PostHog project. Vier van de zeven KPI-rijen uit de skill kunnen structureel niet gevuld worden.
4. **Geen CTA click tracking op de SYBB pagina.** De enige click-events in het project (`video_click`, `instagram_click`, `social_click`) vuren op de webshop, niet op SYBB. CTA Click Rate is niet berekenbaar.
5. **Geen UTM capture.** Zonder `utm_content` in PostHog is de koppeling ad variant naar paginagedrag, het hele punt van dit rapport, onmogelijk.
6. **Pixel-waardes kloppen niet.** April rapporteert 6 purchases met € 44.247,00 totaalwaarde, dus € 7.374,50 per SYBB-ticket, terwijl `add_to_cart` in dezelfde maand € 350,00 per stuk meestuurt. Daarnaast € 86.100,00 op 6 `complete_registration` events, oftewel € 14.350,00 per registratie. Een factor 21 verschil tussen wat de cart zegt en wat de purchase zegt. Elke ROAS-beslissing hierop is giswerk, en Meta optimaliseert wel degelijk op dit signaal.
7. **36% verlies tussen link click en landing page view** in maart, 21% in april. Wijst op traagheid of een redirect-stap op de pagina.
8. **Nieuw vandaag: alle drie de acties van 2 augustus staan nog open.** Geen tracking-wijziging, geen pixel-fix, geen statuswijziging op de campagne. Dit rapport is daarmee identiek aan dat van gisteren.

Niet van toepassing vandaag: CPC-stijging, bounce rate per UTM segment, frequency boven 3,0. Alle drie vereisen delivery die er niet is.

---

## 6. Top 3 Acties voor Vandaag

De volgorde is bewust ongewijzigd ten opzichte van 2 augustus. Actie 1 en 2 zijn meetwerk dat af moet zijn vóór actie 3, anders koop je opnieuw verkeer dat je niet kunt lezen.

### 1. Zet scroll depth, CTA click en UTM capture aan in PostHog

- **Wat:** voeg aan `www.startyourballoonbusiness.com` een scroll depth event toe op 25/50/75/100%, een click event op de Book Now CTA, en zorg dat posthog-js de UTM parameters uit de URL meestuurt op `$pageview`.
- **Waarom:** vandaag zijn 7 van de 9 KPI-rijen in sectie 3 niet meetbaar, en de UTM-koppeling die de cross-reference tussen Meta en PostHog mogelijk maakt bestaat niet. Herstart van de campagne zonder deze fix levert opnieuw een half rapport op.
- **Hoe:** aanpassing in de PostHog snippet op de landing page (Wix Editor), of voor de CTA via een autocapture-actie in de PostHog toolbar. Dat laatste kan zonder Wix-toegang en kost tien minuten, dus begin daarmee.
- **Verwachte impact:** dit rapport gaat van ongeveer 40% gevuld naar volledig, en ad-variant-analyse per `utm_content` wordt mogelijk.
- **Escalatie:** 🟠 Oranje, scroll en UTM vereisen Wix Editor. De CTA-actie via de toolbar is 🟢 Groen.

### 2. Fix de pixel purchase values vóór de herstart

- **Wat:** corrigeer de waarde die de Meta pixel meestuurt bij `purchase` en `complete_registration` op de checkout.
- **Waarom:** € 7.374,50 per verkocht ticket en € 14.350,00 per registratie zijn onmogelijk, zeker naast een `add_to_cart` waarde van € 350,00 in dezelfde maand. De ROAS die Meta rapporteert is daarmee waardeloos, en Meta optimaliseert de campagne op dat signaal.
- **Hoe:** Meta Events Manager, controleer de value parameter bij het purchase event, daarna testen met de Pixel Helper. Neem € 350,00 als referentiewaarde, dat is wat de cart nu meestuurt.
- **Verwachte impact:** betrouwbare ROAS, en Meta's algoritme optimaliseert weer op echte waarde in plaats van ruis.
- **Escalatie:** 🟡 Geel, Robin beslist wanneer.

### 3. Beslis over de herstart, en herstart dan op de bewezen ad set

- **Wat:** kies een startdatum voor `2026: SYBB` en zet die aan met de originele BATCH 2 ad set, niet met de gedupliceerde campagne `2026: SYBB - Kopie`.
- **Waarom:** maart draaide op CPC € 0,13 en CTR 5,27% via BATCH 2. April, na het dupliceren van ad sets, ging naar CPC € 0,55 en CPM € 11,54 bij een frequency van slechts 2,19. Het verschil zit in de duplicaten, niet in de hooks of in verzadiging.
- **Hoe:** Meta Ads Manager, campagne `120239435987290239` op ACTIVE, kopie-campagne `120243293329420239` archiveren. Volg 70-20-10: 70% op de bewezen hooks uit BATCH 2, 20% varianten op dezelfde B3 body en CTA5, 10% één nieuwe angle.
- **Verwachte impact:** terug naar het maart-niveau qua CPC in plaats van opnieuw beginnen op april-kosten.
- **Escalatie:** 🔴 Rood, strategische beslissing met budget-impact.

---

## Cross-referencing

De vijf cross-references uit de skill vragen alle vijf om gelijktijdige Meta- en PostHog-data. Met nul delivery en nul pageviews is geen enkele te maken. De enige cross-reference die vandaag wél iets oplevert is historisch: de 36% wegval tussen Meta link clicks en Meta landing page views in maart, tegenover 6.174 landing page views die PostHog in diezelfde periode niet aan een ad kon koppelen omdat UTM capture ontbreekt. Dat is precies het gat dat actie 1 dicht.

---

## Verantwoording databronnen

Dit rapport gebruikt uitsluitend de Meta Ads MCP (Pipeboard) en de PostHog MCP. Er is geen enkele Google MCP aangeroepen (Gmail, Calendar, Drive, Sheets, Docs, Slides) en er is niet naar de Meta Ads Tracker Google Sheet geschreven. Output staat alleen lokaal in `Output/Reports/Daily/2026-08-03_sybb_report.md`.
