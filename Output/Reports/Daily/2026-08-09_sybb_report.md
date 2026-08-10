# SYBB Daily Report, zondag 9 augustus 2026

> **Databronnen:** PostHog MCP (project STX EU, id 149694, timezone UTC). Meta Ads MCP (Pipeboard) was in deze sessie niet geautoriseerd, zie sectie 2.
> Geen Google MCPs gebruikt, niet naar de Google Sheet tracker geschreven, conform instructie.

---

## 1. Samenvatting

De SYBB landing page (startyourballoonbusiness.com) registreerde op 9 augustus opnieuw **nul** events. Negende stille dag op rij, laatste activiteit was 31 juli. Er draait geen betaald budget, dus er komt hier niemand.

Het SYBB verkeer dat er wel was liep via de event registratiepagina's op sempertexeurope.com: 3 pageviews, 3 bezoekers, 3 sessies. Dat is de helft van het weekgemiddelde (6,0 pageviews) en alle drie de sessies waren oppervlakkig: één pageview, samen één klik, geen enkele ging door naar het formulier.

Het goede nieuws zit een laag dieper. De site brede registratiefunnel, die op 8 augustus op nul voltooiingen stond, herstelde: **7 starts, 2 voltooiingen, 29%**. Dat is de beste voltooiingsratio van de afgelopen week. De nul van zaterdag was dus een blip bij lage aantallen, geen kapot formulier.

Wat wél aandacht vraagt is de aanhoudende site brede degradatie: bounce rate 73,5% (7d gemiddelde 51,6%) en sessieduur 119s (7d 183s). Sectie 5 laat zien dat dit vrijwel volledig verkeersmix is en geen sitefout, maar de onderliggende trend is zorgelijk: menselijke homepage instappen zijn in vijf dagen met 85% gedaald.

---

## 2. Meta Ads Performance

**Data niet beschikbaar.** De Pipeboard Meta Ads MCP is niet geautoriseerd en autoriseren kan hier niet, de sessie is non interactief. Vijfde dag op rij zonder Meta data.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | n.b. | n.b. | n.b. |
| Impressions | n.b. | n.b. | n.b. |
| Clicks | n.b. | n.b. | n.b. |
| CTR | n.b. | n.b. | n.b. |
| CPC | n.b. | n.b. | n.b. |
| Frequency | n.b. | n.b. | n.b. |

### Wat PostHog wel bevestigt over betaald verkeer

**39 dagen nul betaald verkeer.** In de kanaalverdeling van 9 augustus bestaat er geen Paid Social kanaal. In de volledige UTM breakdown over 3 tot en met 9 augustus komt `utm_source=meta` geen enkele keer voor. De laatste `meta/cpc/sybb` klik dateert van 1 juli 2026.

Alle UTM getagde sessies van de afgelopen week:

| utm_source | medium | campagne | content | Sessies | Bounce |
|-----------|--------|----------|---------|---------|--------|
| chatgpt.com | (geen) | (geen) | (geen) | 65 | 13,8% |
| mailjet | email | workshop_tobi_promo_202608 | mail3 | 55 | 23,6% |
| Klaviyo | email | (geen) | (geen) | 6 | 33,3% |
| mailjet | email | inspiration_promo_202607 | mail2_calculator | 5 | 0,0% |
| youtube | organic | content | inspiration_page | 4 | 25,0% |
| newsletter | email | fr_client | email_link | 2 | 0,0% |
| partner | referral | distributor_evergreen_202607 | platform_button | 1 | 0,0% |
| Pinterest | organic | (geen) | (geen) | 1 | 100,0% |

Twee dingen vallen op. `chatgpt.com` is met 65 sessies en 13,8% bounce de grootste getagde bron van de week, en die 6 Klaviyo sessies missen nog steeds een `utm_campaign`, dus ze zijn niet toe te wijzen aan een mailing.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |
| h12_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |
| h13_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |
| h14_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |
| h15_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |

Geen enkele `utm_content` waarde uit de SYBB batch is binnengekomen. **Beste variant:** niet vast te stellen. **Slechtste variant:** niet vast te stellen. Er draait geen budget.

---

## 3. Landing Page Health

### 3a. startyourballoonbusiness.com (de eigenlijke SYBB landing page)

**Nul events op 9 augustus.** Negen dagen volledig stil.

| Datum | Events | Personen |
|-------|--------|----------|
| 1 t/m 9 aug | 0 | 0 |
| 31 jul | 2 | 1 |
| 29 jul | 2 | 1 |
| 27 jul | 1 | 1 |
| 23 jul | 1 | 1 |
| 21 jul | 2 | 1 |
| 20 jul | 8 | 6 |

De pixel werkt, de bron van bezoekers ontbreekt.

### 3b. SYBB registratiepagina's op sempertexeurope.com

| Metric | 9 aug | 7d gemiddelde | Trend |
|--------|-------|---------------|-------|
| Pageviews | 3 | 6,0 | ↓ |
| Unieke bezoekers | 3 | 4,0 | ↓ |
| Sessies | 3 | 4,3 | ↓ |
| Clicks totaal | 1 | n.b. | ↓ |

De drie sessies van 9 augustus, elk met precies één pageview:

| Pagina | Sessie | Events | Clicks |
|--------|--------|--------|--------|
| `/fr/event/start-your-balloon-business-professionnel-8/register` | 019fe73d | 4 | 1 |
| `/event/start-your-balloon-business-professional-8/register` | 019fe57c | 3 | 0 |
| `/event/start-your-balloon-business-professional-7/register` | 019fe6f2 | 3 | 0 |

Dit is een scherp contrast met 8 augustus, toen 5 sessies nul bounces hadden en één bezoeker bijna veertig minuten op de pagina bleef. Zondag leverde drie vluchtige bezoeken zonder interactie.

### 3c. Site breed (sempertexeurope.com)

| Metric | 9 aug | 7d Gemiddelde | Target | Status |
|--------|-------|---------------|--------|--------|
| Bezoekers | 709 | 947 | meten | ↓ 25% |
| Pageviews | 2.819 | 4.725 | meten | ↓ 40% |
| Sessies | 747 | 1.052 | meten | ↓ 29% |
| Bounce Rate | 73,5% | 51,6% | <55% | 🔴 |
| Avg Session Duration | 119s | 183s | >90s | 🟢 |
| Scroll 25 / 50 / 75 / 100% | niet gemeten | niet gemeten | >80/60/40/20% | ⚫ |
| CTA Click Rate | niet gemeten | niet gemeten | >4% | ⚫ |

⚫ = **niet meetbaar**. Er bestaat geen scroll event in dit PostHog project en er is geen CTA click event gedefinieerd. Dit is een meetgat, geen slechte score. Zie actie 3.

Kanaalverdeling 9 augustus:

| Kanaal | Sessies | Bounce | Avg duur |
|--------|---------|--------|----------|
| Direct | 560 | 87,1% | 58s |
| Referral | 117 | 49,6% | 198s |
| Organic Search | 52 | **1,9%** | **604s** |
| AI | 14 | 7,1% | 61s |
| Email | 4 | 25,0% | 242s |

Organic Search is met 52 sessies klein maar uitzonderlijk sterk: 1,9% bounce en ruim tien minuten gemiddelde sessieduur. Van de 117 Referral sessies zijn er 113 interne verwijzingen vanaf `www.sempertexeurope.com` zelf, dus dat is grotendeels sessie hersplitsing en geen echte externe aanwas.

---

## 4. Funnel Drop-off

### SYBB funnel, 9 augustus

```
SYBB register pagina    3 sessies    100%
        ↓                            -100%
/registratie formulier  0 sessies      0%
        ↓                              n.b.
/registratie-voltooid   0 sessies      0%
```

**Grootste lek: de register pagina zelf, opnieuw.** Alle drie de sessies stopten daar. Op 8 augustus was dat 4 van de 5. Twee dagen op rij is de stap van register pagina naar formulier het enige echte lek in de SYBB funnel.

### Site brede registratiefunnel (alle events, niet alleen SYBB)

| Datum | `/registratie` starts | `/registratie-voltooid` | Voltooiing |
|-------|----------------------|------------------------|------------|
| **9 aug** | **7** | **2** | **29%** |
| 8 aug | 6 | 0 | 0% |
| 7 aug | 13 | 2 | 15% |
| 6 aug | 13 | 3 | 23% |
| 5 aug | 17 | 1 | 6% |
| 4 aug | 21 | 5 | 24% |
| 3 aug | 10 | 2 | 20% |

**Dit corrigeert de zorg van gisteren.** De nul voltooiingen van 8 augustus waren ruis bij lage aantallen, geen kapot formulier. 29% is de hoogste ratio van de week.

### De twee voltooide registraties, van dichtbij

Beide zijn de moeite waard omdat ze laten zien hoeveel wrijving er in het formulier zit, ook als het uiteindelijk lukt.

**Sessie `019fe75f`** kwam via Organic Search (Google) binnen op de homepage, 29 pageviews, 611s. Op `/registratie` genereerde deze bezoeker in 6 minuten en 21 seconden **831 clicks**, waarvan **8 rageclicks**, plus 25 `change` events en precies één klik op "Indienen". Van die 831 clicks hadden er 804 geen herkenbare elementtekst. Ruim twee clicks per seconde op een registratieformulier is geen normaal invulgedrag. De registratie werd om 16:43:59 wel voltooid.

**Sessie `019fe79d`** kwam direct binnen op `/de/shop`, ging via `/de/registratie` naar `/de/registratie-voltooid`, 8 pageviews, 45 clicks, 245s. Dit is hoe het hoort te lopen.

Het patroon van 831 clicks sluit aan bij de Franse sessie van 8 augustus met 283 clicks op hetzelfde formulier. **Twee dagen, twee sessies met abnormale klikvolumes op `/registratie`.** Dat is nu een patroon en geen incident meer.

---

## 5. Rode Vlaggen 🚩

**1. SYBB landing page negen dagen op nul.** Zie sectie 3a. Alleen op te lossen met budget of een andere verkeersbron.

**2. Meta Ads blind, dag vijf.** Geen spend, CPC, CTR of frequency. Ad fatigue en CPC stijging zijn niet te controleren.

**3. Registratieformulier genereert abnormale klikvolumes.** 831 clicks met 8 rageclicks in één sessie op 9 augustus, 283 clicks in één sessie op 8 augustus. Beide op `/registratie`. Site breed was `/registratie` gisteren met 8 rageclicks van 1 persoon de nummer één rageclick pagina. Dit kost je waarschijnlijk voltooiingen bij minder vasthoudende bezoekers.

**4. Bounce rate 73,5%, maar het is de verkeersmix en niet de site.** De analyse van gisteren houdt stand. Binnen Direct verkeer:

| Datum | Instap | Sessies | Bounce | Avg duur |
|-------|--------|---------|--------|----------|
| 9 aug | Homepage | 65 | 27,7% | 250s |
| 9 aug | Diepe pagina | 495 | 94,9% | 33s |
| 8 aug | Homepage | 58 | 13,8% | 359s |
| 8 aug | Diepe pagina | 514 | 96,1% | 15s |
| 5 aug | Homepage | 420 | 4,5% | 302s |
| 5 aug | Diepe pagina | 303 | 79,5% | 116s |
| 4 aug | Homepage | 435 | 2,5% | 212s |
| 4 aug | Diepe pagina | 323 | 82,0% | 128s |

Diepe pagina instappen bouncen al de hele week hoog. Wat kantelde is de verhouding: op 4 augustus was 57% van het directe verkeer een homepage instap, op 9 augustus nog 12%.

**5. De echte zorg: menselijke homepage instappen zijn met 85% gedaald.** Van 435 directe homepage sessies op 4 augustus naar 65 op 9 augustus. Die 495 diepe instappen zonder referrer met 94,9% bounce en 33s zijn vrijwel zeker crawlers. Zolang bot filtering uit staat, vervuilen ze elk gemiddelde in dit rapport. **Dit blijft een hypothese**, zie actie 2.

**6. Scroll depth en CTA clicks zijn niet meetbaar.** Vier van de zeven Landing Page Health KPI's uit de skill kunnen niet gerapporteerd worden.

**7. Weekendeffect meewegen.** 9 augustus was een zondag, 8 augustus een zaterdag. Een deel van de volumedaling is normaal weekendpatroon. De vergelijking met 4 en 5 augustus (dinsdag en woensdag) overdrijft de daling dus. Beoordeel de trend opnieuw op maandagdata.

---

## 6. Top 3 Acties voor Vandaag

### 1. Zet bot filtering aan in PostHog

- **Wat:** Schakel bot en crawler filtering in op projectniveau in PostHog.
- **Waarom:** 495 van de 560 directe sessies op 9 augustus waren diepe instappen zonder referrer met 94,9% bounce en 33s gemiddelde duur. Ze bepalen nu het site brede gemiddelde en maken bounce rate en sessieduur onbruikbaar als stuurmiddel. Zolang dit aan staat, rapporteert dit document elke dag een rood cijfer dat niets over de site zegt.
- **Hoe:** PostHog projectinstellingen, sectie Bot detection. Vergelijk daarna de bounce rate van 9 augustus voor en na filtering.
- **Verwachte impact:** Herstelt de betrouwbaarheid van vier metrics in sectie 3c. Kost tien minuten.
- **Escalatie:** 🟢 Groen, direct uit te voeren.

### 2. Test het registratieformulier zelf, op zoek naar de klikval

- **Wat:** Doorloop `/registratie` op desktop en mobiel tot en met de bevestiging. Zoek specifiek naar een element dat clicks slikt zonder zichtbare reactie: een dropdown, een datumveld, een landenkeuze of een captcha.
- **Waarom:** 831 clicks in 381 seconden waarvan 804 zonder elementtekst, plus 8 rageclicks, plus een tweede sessie met 283 clicks de dag ervoor. Beide bezoekers rondden af, maar dit is precies het gedrag dat minder gemotiveerde bezoekers laat afhaken. Van de 7 starts op 9 augustus haalden er 5 het einde niet.
- **Hoe:** Handmatig in de browser. Bekijk daarna de session recording van `019fe75f-dd2b-7667-86f5-c06ab87847f0` in PostHog, en de heatmap op `/registratie`. Er zijn 183 opnames van 9 augustus beschikbaar, waarvan 8 met console errors.
- **Verwachte impact:** Dit is de enige actie in dit rapport die direct omzet raakt. Alle SYBB registraties lopen straks door ditzelfde formulier.
- **Escalatie:** 🟠 Oranje, mogelijk Wix Editor werk.

### 3. Zet scroll depth en CTA click events aan

- **Wat:** Voeg scroll depth events (25/50/75/100%) en een expliciet CTA click event toe op de SYBB register pagina's en op startyourballoonbusiness.com.
- **Waarom:** Vier van de zeven Landing Page Health KPI's zijn nu niet in te vullen, en de SYBB funnel eindigt twee dagen op rij op de register pagina zonder dat we weten of mensen de CTA überhaupt zien. Zodra er budget loopt kun je zonder deze events geen ad variant aan paginagedrag koppelen, en dat is de kern van dit rapport.
- **Hoe:** PostHog autocapture aanvullen met custom events, via de Wix Editor of de PostHog snippet.
- **Verwachte impact:** Maakt het rapport voor het eerst volledig invulbaar. Doe dit nu het rustig is.
- **Escalatie:** 🟠 Oranje, Wix Editor werk.

**Vervolgens:** autoriseer Pipeboard via je claude.ai connector instellingen of `/mcp` in een interactieve sessie. Zonder dat blijft sectie 2 elke dag leeg en blijft de helft van dit rapport onbruikbaar.

---

## Cross-referencing

De standaard kruisverbanden uit de skill (Ad CTR versus LP bounce, CPC versus conversie, frequency versus bounce) zijn voor de vijfde dag niet te maken: geen ad data, geen verkeer op de landing page. Wat de twee bronnen die er wel zijn samen laten zien:

**De SYBB pagina trekt geen aandacht meer zonder externe aanjager.** Op 8 augustus leverden 5 organische sessies nul bounces en één sessie van bijna veertig minuten. Op 9 augustus leverden 3 sessies samen één klik. Het verschil is niet de pagina, het is wie er langskomt. Zonder ads of een mailing is het SYBB verkeer volledig afhankelijk van toeval, en dat schommelt tussen betrokken en vluchtig.

**De aflopende mailjet campagne verklaart een groot deel van de weekdaling.** `workshop_tobi_promo_202608` was goed voor 55 sessies over de week, maar liep terug van 42 events op 5 augustus naar vrijwel niets. Het wegvallen van dat betrokken segment is een grotere factor in de bounce rate stijging dan enige verandering aan de site.

**Het knelpunt zit in de techniek, niet in de propositie.** Twee dagen op rij eindigt de SYBB funnel op de register pagina, en twee dagen op rij vertoont het onderliggende registratieformulier abnormaal klikgedrag. Als je één ding fixt voordat het budget weer aan gaat, is het dat formulier. Anders koop je verkeer dat op dezelfde plek blijft steken.

**Organic Search is de meest ondergewaardeerde bron van deze week.** 52 sessies, 1,9% bounce, 604s gemiddeld. Dat is bij nul spend de enige bron die structureel diep betrokken bezoekers levert. De sessie die de registratie voltooide kwam daar vandaan.
