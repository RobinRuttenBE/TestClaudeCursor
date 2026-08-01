# SYBB Daily Report, 31 juli 2026

## 1. Samenvatting

De SYBB funnel stond gisteren volledig stil. Campagne `2026: SYBB` is PAUSED en heeft op 31 juli nul impressies, nul clicks en nul spend gedraaid. Laatste dag met delivery was **19 april 2026**, dat is 103 dagen geleden. De landing page ving gisteren precies **1 pageview** op, direct verkeer, geen UTM, geen CTA click, geen /booking bezoek. Er valt dus niets te optimaliseren aan ads of pagina, de enige echte vraag is wanneer de campagne weer aan gaat.

**Belangrijkste observatie:** de meetopstelling werkt wel. In april registreerde PostHog 1.976 pageviews op startyourballoonbusiness.com terwijl de ads liepen. De stilte van nu is geen trackingprobleem, het is gewoon geen budget.

---

## 2. Meta Ads Performance

Campagne `2026: SYBB` (ID 120239435987290239), status PAUSED, daily budget €100 (inactief).

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

Alle 6 ad sets in de campagne staan op PAUSED, inclusief `BATCH 2: Expertise & POC` en de 4 duplicaten daarvan. Ook de zustercampagne `2026: SYBB - Kopie` staat uit. Op accountniveau was er in heel juli 2026 geen enkele campagne met delivery.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |
| h12_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |
| h13_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |
| h14_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |
| h15_b3_cta5 | 0 | n.v.t. | n.v.t. | geen data | geen data |

**Beste variant:** niet te bepalen, geen delivery.
**Slechtste variant:** niet te bepalen, geen delivery.

### Laatst bekende performance (referentiepunt)

Voor context, de campagne lifetime cijfers tot en met 19 april 2026:

| Metric | Lifetime |
|--------|----------|
| Spend | €2.485,04 |
| Impressions | 297.174 |
| Clicks | 12.067 |
| CTR | 4,06% |
| CPC | €0,21 |
| CPM | €8,36 |
| Frequency | 2,09 |

Laatste actieve week (14 tot 19 april): CPC liep op naar €0,62 en CTR zakte naar 2,23%, tegen €0,13 en 5,27% in maart. De campagne werd dus niet op zijn best gepauzeerd, hij was al aan het verzwakken.

---

## 3. Landing Page Health

startyourballoonbusiness.com, PostHog project Default project (149694).

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 1 | 0,4 per dag | meten | ⚪ |
| Sessies | 1 | 0,4 per dag | meten | ⚪ |
| Bounce Rate | 100% (1 van 1 sessie) | 100% | <55% | ⚪ n=1 |
| Avg Session Duration | 15s | 8s | >90s | ⚪ n=1 |
| Scroll 25% | geen data | geen data | >80% | ⚪ |
| Scroll 50% | geen data | geen data | >60% | ⚪ |
| Scroll 75% | geen data | geen data | >40% | ⚪ |
| Scroll 100% | geen data | geen data | >20% | ⚪ |
| CTA Click Rate | 0% (0 clicks) | 0% | >4% | ⚪ n=1 |

Geen enkel statuslampje op groen, geel of rood gezet, want bij 1 sessie is elk percentage betekenisloos. 100% bounce op één bezoeker zegt niets over de pagina.

**Sessiedetail 31 juli:** 1 sessie (`019fba05-701a-786c-a9ec-cf87bc80b9c0`), 1 pageview op `/`, referrer `$direct`, geen utm_source, geen utm_campaign, geen utm_content. Dus geen Meta verkeer, zoals verwacht bij een gepauzeerde campagne.

**Scroll depth ontbreekt:** op 31 juli is er geen `$pageleave` event vastgelegd, en dat is het event dat de max scroll percentage meedraagt. Zonder pageleave is er geen scroll data. Ook `$autocapture` stond gisteren niet aan op deze sessie, waardoor CTA clicks sowieso niet meetbaar waren. Dit is een aandachtspunt voor de herstart, zie actie 2.

**Verkeer in perspectief:**

| Maand | Pageviews | Sessies | Bezoekers |
|-------|-----------|---------|-----------|
| maart 2026 | 32 | 10 | 7 |
| april 2026 | 1.976 | 1.515 | 1.349 |
| mei 2026 | 91 | 76 | 68 |
| juni 2026 | 49 | 44 | 44 |
| juli 2026 | 51 | 47 | 47 |

De piek in april valt exact samen met de ad delivery. Sinds mei is er een organische bodem van ongeveer 50 pageviews per maand, dat is ruwweg 1,6 per dag.

---

## 4. Funnel Drop-off

Pageview (1) → Scroll 50% (geen meting) → CTA Click (0) → /booking (0)

Met één bezoeker is er geen funnel te tekenen. **Grootste lek:** de instroom zelf. Er komt niets binnen om te laten vallen.

Ter referentie, de lifetime paginaverdeling op het domein laat zien dat de funnel wel volledig getrackt is toen er verkeer was:

| Pad | Pageviews (lifetime) |
|-----|----------------------|
| `/` | 1.839 |
| `/booking` | 165 |
| `/product-page/start-your-balloon-business-professional` | 79 |
| `/checkout` | 54 |
| `/review` | 24 |
| `/thank-you-page` | 9 + 1 |

Dat is 1.839 landingen naar 165 booking bezoeken (9,0%), naar 54 checkouts (2,9% van landingen), naar 10 thank-you pageviews (0,54% van landingen). Het grootste lek historisch zit tussen `/` en `/booking`: 91% van de bezoekers klikt nooit door. Dat sluit aan bij het beeld uit het ads rapport van 1 augustus, waar 12.262 clicks slechts 6 aankopen opleverden.

---

## 5. Rode Vlaggen 🚩

Geen van de standaard triggers vuurt, omdat er geen data is om ze op te vuren. Wat er wel staat:

- 🚩 **103 dagen geen delivery.** Campagne `2026: SYBB` staat sinds 19 april 2026 stil. Meta's leerfase is volledig verlopen, bij herstart begin je opnieuw met een koude campagne.
- 🚩 **Pixel/tracking gat op de landing page.** Geen `$pageleave` en geen `$autocapture` op de sessie van gisteren betekent dat scroll depth en CTA clicks nu niet meetbaar zijn. Als de campagne morgen aan gaat, meet je alleen pageviews en ben je blind voor precies de metrics waar dit rapport op stuurt.
- 🚩 **Bekende pixel value corruptie.** Uit het ads rapport van 1 augustus: adset Kopie 3 rapporteerde 2 aankopen à €21.386. Zolang dit niet gefixt is, optimaliseert Meta bij herstart op ruis.
- ⚠️ **Verzwakkende trend bij pauzemoment.** CPC €0,62 en CTR 2,23% in de laatste actieve week, tegen €0,13 en 5,27% in maart. De creatives waren op. Frequency was met 1,41 laag, dus dat was niet de oorzaak, het waren de duplicaat adsets die elkaar beconcurreerden.

---

## 6. Top 3 Acties voor Vandaag

**1. Beslis of SYBB weer aan gaat, en zo ja op welke datum**

- **Wat:** knoop doorhakken over herstart van campagne `2026: SYBB`. Zonder besluit is dit rapport 103 dagen op rij hetzelfde.
- **Waarom:** nul delivery sinds 19 april, terwijl het daily budget van €100 nog ingesteld staat. Er is geen data om op te sturen.
- **Hoe:** Meta Ads Manager, campagne `2026: SYBB` (120239435987290239). Bij herstart: één campagne, één adset, geen duplicaten. De 4 kopieën van `BATCH 2: Expertise & POC` presteerden op elke metric slechter dan het origineel.
- **Verwachte impact:** herstel van meetbare funnel data binnen 48 uur na activatie.
- **Escalatie level:** Rood (strategie, Robin beslist)

**2. Herstel de landing page tracking voordat er budget in gaat**

- **Wat:** controleer of PostHog `$pageleave` (scroll depth) en `$autocapture` (CTA clicks) actief zijn op startyourballoonbusiness.com, en fix de pixel conversiewaarde.
- **Waarom:** op de sessie van 31 juli ontbreken beide events. Zonder pageleave geen scroll depth, zonder autocapture geen CTA click rate. Vier van de zeven KPI's uit dit rapport zijn dan structureel leeg. Daarbovenop stuurt de Meta pixel corrupte purchase values.
- **Hoe:** PostHog project settings, autocapture en pageleave capture aanzetten. Voor de pixel: Meta Events Manager, test events op `/checkout` en `/thank-you-page` valideren tegen de echte ticketprijs (circa €368).
- **Verwachte impact:** volledige rapportage vanaf dag 1 van de herstart, en Meta optimaliseert op echte in plaats van corrupte waarde.
- **Escalatie level:** Oranje (technische ingreep in Wix en PostHog)

**3. Fix de sprong van `/` naar `/booking` voor je opnieuw traffic inkoopt**

- **Wat:** de doorklik van landing page naar booking pagina aanpakken, dat is historisch het grootste lek.
- **Waarom:** 1.839 landingen leverden 165 booking bezoeken op, 9,0% doorklik. De ads deden hun werk (CPC €0,21, CTR 4,06% lifetime), de pagina niet. Nieuwe euro's in dezelfde pagina stoppen herhaalt hetzelfde resultaat.
- **Hoe:** begin met de CTA boven de vouw en de eerste sectie. Gebruik de SYBB 8 pillars als check: adresseert de hero het probleem waar de bezoeker mee binnenkomt, of pitcht hij meteen de workshop? Erken waarde, creëer gap, positioneer workshop, directe actie.
- **Verwachte impact:** elke procentpunt op de `/` naar `/booking` stap is bij het aprilvolume ongeveer 15 extra booking bezoeken per 1.500 sessies.
- **Escalatie level:** Oranje (Wix Editor)

---

## 7. Cross-Reference Analyse

Niet uit te voeren voor 31 juli. Er is geen ad data om tegen de landing page data te leggen, en de enige sessie op de pagina kwam direct binnen zonder UTM.

De cross-reference die uit de historische data wel overeind staat: **lage CPC met lage conversie**. Lifetime kocht de campagne clicks voor €0,21 met een CTR van 4,06%, terwijl slechts 9,0% van de landingen doorklikte naar `/booking` en 0,54% de thank-you pagina haalde. Goedkoop verkeer dat niet converteert wijst op een mismatch tussen de belofte in de ad en wat de pagina levert, niet op een biedprobleem. Dat is precies waar actie 3 op zit.

---

## Bronnen en beperkingen

- **Meta Ads:** Pipeboard Meta Ads MCP, account `act_567892422940728` (Sempertex Ad Account, EUR). Campagne, adset en account niveau opgevraagd voor 25 tot en met 31 juli 2026, plus lifetime en april dagbreakdown als referentie.
- **PostHog:** PostHog MCP, project Default project (149694), organisatie Sempertex Europe, timezone UTC. Queries op host `www.startyourballoonbusiness.com`.
- **Niet gebruikt op instructie:** geen Gmail, Google Calendar, Drive, Sheets, Docs of Slides. Niet naar de Meta Ads Tracker Google Sheet geschreven.
- **Beperking:** alle percentages voor 31 juli zijn gebaseerd op n=1 sessie en zijn statistisch betekenisloos. Ze staan in de tabel om de structuur consistent te houden, niet om op te sturen.
