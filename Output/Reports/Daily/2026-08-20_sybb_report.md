# SYBB Daily Report, 20 augustus 2026

*Gegenereerd 21 augustus 2026. Bronnen: Meta Ads via Pipeboard (directe HTTP, MCP connector staat op "requires authentication"), PostHog project STX EU (149694). Geen Google MCP aangeroepen, niet naar de tracker Sheet geschreven.*

---

## 1. Samenvatting

**Er draaide niets op 20 augustus.** Campagne `2026: SYBB` staat op PAUSED en gaf nul rijen terug voor die dag. De laatste euro op het hele advertentieaccount is uitgegeven op **20 april 2026**, precies **122 dagen** geleden. Dit rapport meet dus geen performance, het meet stilte.

De oude landingspagina `startyourballoonbusiness.com` haalde **0 pageviews**. Dat is geen storing, dat is de bevestiging van wat gisteren al bleek: SYBB loopt volledig via de event pagina's op sempertexeurope.com. Daar kwamen 6 pageviews van 4 unieke personen binnen, volledig organisch.

Eén ding is wel het bekijken waard. Die 4 organische sessies gedroegen zich goed (3 van de 4 scrollden voorbij 50%, sessies van 280, 381 en 678 seconden), maar geen enkele haalde 75% scroll. Bij n=4 is dat een observatie, geen conclusie.

---

## 2. Meta Ads Performance

Campagne `2026: SYBB` (ID `120239435987290239`), account `act_567892422940728` (Sempertex Ad Account).

| Metric | 20 aug | 7d gemiddelde (13-19 aug) | Trend |
|--------|--------|---------------------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De API gaf een lege `data` array terug op campagne, adset én accountniveau. Geen delivery, geen impressies, geen kosten.

**Laatste dagen met spend op het account:**

| Datum | Spend | Impressions | Clicks |
|-------|-------|-------------|--------|
| 2026-04-17 | €86,68 | 6.006 | 139 |
| 2026-04-18 | €94,64 | 6.454 | 153 |
| 2026-04-19 | €90,38 | 6.084 | 137 |
| **2026-04-20** | **€77,85** | **4.287** | **119** |
| 2026-04-21 t/m 2026-08-20 | €0,00 | 0 | 0 |

### Ad Variant Performance

**Let op: dit is lifetime data, geen data van 20 augustus.** Er viel gisteren niets te meten. Deze tabel staat er zodat de variantvergelijking klaarligt voor het moment dat je herstart, niet omdat er iets gebeurd is.

| Ad (variant) | Spend | Impr. | Clicks | CTR | CPC | LPV | LPV rate | Purch. |
|--------------|-------|-------|--------|-----|-----|-----|----------|--------|
| H13, B3, CTA5 | €628,28 | 76.840 | 6.233 | 8,11% | €0,10 | 4.234 | 67,9% | 2 |
| H15, B3, CTA5 | €268,79 | 39.036 | 1.572 | 4,03% | €0,17 | 881 | 56,0% | 0 |
| H14, B3, CTA5 | €232,36 | 33.235 | 911 | 2,74% | €0,26 | 465 | 51,0% | 0 |
| H12, B3, CTA5 | €529,83 | 62.121 | 1.604 | 2,58% | €0,33 | 624 | 38,9% | 0 |
| H11, B3, CTA5 | €724,04 | 69.674 | 1.580 | 2,27% | €0,46 | 788 | 49,9% | **4** |
| SYBB w/ Semp (BLACK) | €101,74 | 16.268 | 167 | 1,03% | €0,61 | **0** | **0,0%** | 0 |

**Beste variant:** hangt af van wat je meet, en dat is precies het probleem. **H13** wint op elke traffic metric: 8,11% CTR, €0,10 CPC, 67,9% van de klikkers laadt daadwerkelijk de pagina. Maar **H11** leverde 4 van de 6 aankopen op 1.580 clicks, tegen 4,6x de klikprijs. Per landing page view: H11 converteert op 0,51%, H13 op 0,047%. H11 is dus ruim tien keer effectiever per bezoeker die aankomt.

**Slechtste variant:** **SYBB w/ Semp (BLACK)**, en niet vanwege de CTR. **167 clicks en nul landing page views.** Dat is geen slechte creative, dat is een kapotte bestemming of een pixel die niet vuurt. €101,74 aan klikken waarvan de pagina nooit geladen is. Test deze ad vóór je hem in welke herstart dan ook meeneemt.

---

## 3. Landing Page Health

### 3a. startyourballoonbusiness.com

| Metric | 20 aug | Target | Status |
|--------|--------|--------|--------|
| Pageviews | **0** | n.v.t. | ⚫ |

Nul. Geen bezoekers, dus geen bounce rate, geen scroll depth, geen CTA clicks om te rapporteren. De hosts met verkeer op 20 augustus waren `www.sempertexeurope.com` (5.099 pv) en `rezolvbv-sh-sempertex.odoo.com` (70 pv). De KPI targets uit CLAUDE.md gaan over een pagina die geen rol meer speelt in deze funnel.

### 3b. SYBB event pagina's op sempertexeurope.com

Dit is waar SYBB nu leeft. Alle verkeer organisch, geen enkele UTM parameter in het hele venster 13 t/m 20 augustus (42.374 pageviews, allemaal untagged).

| Metric | 20 aug | 7d (13-19 aug) | Target | Status |
|--------|--------|----------------|--------|--------|
| Pageviews | 6 | 83 (11,9/dag) | meten | ⚫ |
| Unieke personen | 4 | n.v.t. | meten | ⚫ |
| Sessies | 4 | 32 (4,6/dag) | meten | ⚫ |
| Bounce Rate | 25,0% (1 van 4) | 15,6% | <55% | 🟢 |
| Avg Session Duration | 335s | 1.304s | >90s | 🟢 |
| Scroll 25% | 75% (3 van 4) | zie noot | >80% | 🟡 |
| Scroll 50% | 75% (3 van 4) | zie noot | >60% | 🟢 |
| Scroll 75% | **0% (0 van 4)** | zie noot | >40% | 🔴 |
| Scroll 100% | **0% (0 van 4)** | zie noot | >20% | 🔴 |
| CTA Click Rate | niet meetbaar | niet meetbaar | >4% | ⚫ |

**Noot bij scroll:** gemeten via `$pageleave` met `$prev_pageview_max_scroll_percentage`. Op 20 augustus zijn dit **4 datapunten**. Statistisch betekent dat niets. De 7-daagse cijfers per pagina geven meer houvast:

| Pagina | n | Avg scroll | ≥25% | ≥50% | ≥75% | ≥95% |
|--------|---|-----------|------|------|------|------|
| /event/…professional-7/register | 17 | 57,3% | 14 | 11 | 4 | 3 |
| /en_GB/event/…professional-7/register | 13 | 27,5% | 6 | 5 | 0 | 0 |
| /event/…professional-9/register | 13 | 34,9% | 7 | 5 | 2 | 0 |
| /en_GB/event/…professional-8/register | 13 | 37,2% | 7 | 6 | 1 | 0 |
| /en_GB/event/…professional-9/register | 5 | 25,1% | 2 | 2 | 0 | 0 |
| /de/event/…professionell-7/register | 4 | 14,7% | 1 | 1 | 0 | 0 |
| /fr/event/…professionnel-9/register | 4 | 19,5% | 1 | 1 | 1 | 0 |

Hier zit wél een patroon in. De Nederlandstalige `/event/…professional-7/register` haalt 57,3% gemiddelde scroll, de Engelse variant van diezelfde pagina 27,5%. Duits 14,7%, Frans 19,5%. Zelfde pagina, zelfde aanbod, minder dan de helft van de scrolldiepte zodra je van taalversie wisselt. Dat wijst op een vertalings- of layoutprobleem in de niet-Nederlandse versies, niet op een aanbodprobleem.

### 3c. Sitebreed ter referentie (20 aug)

| Metric | Waarde |
|--------|--------|
| Sessies | 631 |
| Bounce rate | 38,5% |
| Avg session duration | 591s |
| Rageclicks | 144 |

De 144 rageclicks zaten niet op SYBB pagina's. Grootste concentratie: `/en_GB/shop` met 26. Buiten scope van dit rapport, maar het staat genoteerd.

---

## 4. Funnel Drop-off

**Niet te berekenen voor de betaalde funnel.** Nul ads, nul UTM verkeer, nul klikken. De stappen uit de skill (pageview → scroll 50% → CTA click → /booking) zijn leeg.

De organische funnel op 20 augustus, met de nadruk op de aantallen:

```
SYBB register pageview     4 personen   100%
  ↓
Scroll voorbij 50%         3            75%
  ↓
Scroll voorbij 75%         0             0%   ← hier stopt iedereen
  ↓
Registratie voltooid       0             0%
```

**Grootste lek:** tussen 50% en 75% scroll. Geen van de 4 bezoekers kwam voorbij driekwart van de pagina. Over 7 dagen ligt dat iets beter (bijvoorbeeld 4 van 17 op de best presterende pagina), maar het blijft de scherpste val in de reeks. Wat er onder de 75% grens staat wordt in de praktijk niet gelezen. Als de registratieknop of de prijs daar staat, is dat een concreet probleem.

Er waren op 13 t/m 20 augustus geen SYBB registratiebevestigingen zichtbaar. De 106 pageviews op `/shop/confirmation` betreffen de webshop, niet de workshop.

---

## 5. Rode Vlaggen 🚩

1. **Campagne staat 122 dagen stil.** Laatste spend 20 april 2026. Elke KPI in dit rapport die over ads gaat is per definitie nul. Dit is het enige punt dat er vandaag echt toe doet.
2. **Nul UTM tagging op al het verkeer.** 42.374 pageviews in acht dagen, geen enkele met `utm_source`. Op dit moment kun je organisch en betaald niet uit elkaar houden. Zodra je herstart is attributie blind, tenzij je dit eerst oplost.
3. **SYBB w/ Semp (BLACK): 167 clicks, 0 landing page views.** Kapotte bestemming of pixel. Staat er sinds april, is nooit onderzocht.
4. **Scroll 75% op 0%.** Zowel gisteren (0 van 4) als structureel zwak over 7 dagen. De onderkant van de registratiepagina wordt niet bereikt.
5. **Niet-Nederlandse taalversies scrollen half zo diep.** 57,3% (NL) tegen 27,5% (EN), 19,5% (FR), 14,7% (DE) op vergelijkbare pagina's.
6. **UK gedraagt zich anders dan de rest van Europa.** Op 20 augustus: 108 unieke personen, 2,4 pageviews per persoon. België 16,5, Nederland 16,2, Duitsland 10,2, Frankrijk 8,8. Het VK levert het op één na hoogste bezoekersaantal en het laagste engagement van alle kernmarkten. Dat past bij de botsignalering uit het rapport van 21 augustus en niet bij echt koopgedrag. Filter dit voor je een nulmeting vastlegt.

Niet gevlagd: frequency (geen delivery), CPC stijging (geen spend), CTA click rate (niet meetbaar zonder tracking).

---

## 6. Top 3 Acties voor Vandaag

### 1. Zet UTM tagging live vóór je één euro uitgeeft
**Wat:** implementeer de UTM conventie uit CLAUDE.md (`utm_source=meta`, `utm_medium=cpc`, `utm_campaign=sybb`, `utm_content=hXX_bX_ctaX`, `utm_term=batch_X`) op de event pagina URLs van sempertexeurope.com, niet op de oude landing page.
**Waarom:** 42.374 pageviews zonder één UTM parameter. Zonder dit kun je na herstart niet zien welke ad werkt.
**Hoe:** `update_ad_url_tags` via Pipeboard per ad, of handmatig in Meta Ads Manager op adset niveau.
**Verwachte impact:** het verschil tussen een meetbare en een onmeetbare herstart.
**Escalatie:** 🟡 Geel, jouw goedkeuring op de definitieve URL structuur.

### 2. Diagnoseer SYBB w/ Semp (BLACK): 167 clicks, nul pagina's geladen
**Wat:** open de bestemmings-URL van deze ad handmatig, controleer of de Meta pixel vuurt, en archiveer de ad als de bestemming dood is.
**Waarom:** 100% verlies tussen klik en pageview is geen optimalisatieprobleem, dat is stuk. €101,74 al verbrand.
**Hoe:** `get_ad_creatives` voor de bestemmings-URL, dan handmatig testen met de PostHog debugger open.
**Verwachte impact:** voorkomt dat een kapotte ad meegaat in de herstart.
**Escalatie:** 🟢 Groen, dit kan ik uitvoeren zodra je het zegt.

### 3. Verplaats de registratie-CTA boven de 75% scroll grens
**Wat:** check waar de registratieknop en de prijs staan op `/event/start-your-balloon-business-professional-*/register` en trek ze omhoog, richting het bovenste 50% van de pagina.
**Waarom:** 0 van 4 bezoekers gisteren en structureel weinig over 7 dagen kwamen voorbij 75%. Alles onder die grens wordt niet gelezen.
**Hoe:** Odoo event pagina template. Begin met de Nederlandse versie (beste scroll, dus het schoonste referentiepunt), meet 7 dagen, rol dan uit naar EN, FR en DE.
**Verwachte impact:** de enige actie in deze lijst die iets kan opleveren zonder advertentiebudget.
**Escalatie:** 🟠 Oranje, vereist een aanpassing in de Odoo template.

---

## 7. Kanttekeningen bij dit rapport

- **De Meta cijfers zijn niet zwak, ze zijn afwezig.** Alles in sectie 2 met een lifetime label is historie uit maart en april 2026.
- **De PostHog dagcijfers steunen op 4 sessies.** Percentages op zo'n basis zijn illustratief, niet significant. De 7-daagse tabellen zijn bruikbaarder.
- **De skill gaat uit van startyourballoonbusiness.com als funnel.** Die aanname klopt niet meer. Dat is nu op twee opeenvolgende dagen bevestigd. De skill in `skills/daily-sybb-report/SKILL.md` verdient een update naar de event pagina's op sempertexeurope.com.
- **De zes lifetime SYBB aankopen zijn nog niet geverifieerd in Odoo.** Dat punt staat sinds gisteren open en de conversiecijfers in sectie 2 hangen eraan.
