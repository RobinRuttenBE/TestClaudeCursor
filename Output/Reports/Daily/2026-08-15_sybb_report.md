# SYBB Daily Report, 15 augustus 2026 (zaterdag)

> **Databronnen:** PostHog MCP (project STX EU, 149694, timezone UTC). Meta Ads MCP niet beschikbaar, zie sectie 2.
> **Gegenereerd:** 16 augustus 2026. Alleen PostHog en Meta Ads MCP geraadpleegd. Geen Google MCPs, niets naar de tracker Sheet geschreven.

## 1. Samenvatting

**De belangrijkste bevinding van vandaag is een correctie op het rapport van gisteren.** De 98% bounce op `/en_GB/shop/category/foil-balloons-2915` en de 96% op `/folie-ballonnen` zijn geen kapotte pagina's. Het is botverkeer. Over de laatste 7 dagen had `/folie-ballonnen` 74 sessies waarvan **nul echte**, en `/en_GB/shop/category/foil-balloons-2915` 115 sessies waarvan **3 echte, met 0% bounce**. Actiepunt 3 uit het ads rapport van 16 augustus kun je schrappen.

Gisteren spoot dezelfde bron een piek van **1.247 bots** in je data, vier keer het weekgemiddelde. Ruw gemeten zie je 1.321 bezoekers en 91,5% bounce. Na filtering blijven er **126 echte bezoekers, 135 sessies en 16,3% bounce** over. Alle cijfers in dit rapport zijn gefilterd, tenzij expliciet anders vermeld.

SYBB zelf staat stil. De landing page is de vijftiende dag zonder één event, Meta Ads is de tiende dag niet op te halen, en de SYBB event pagina's op de hoofdsite kregen gisteren **1 pageview van 1 bezoeker**.

## 2. Meta Ads Performance

**Niet beschikbaar, tiende dag op rij.** De Pipeboard Meta Ads MCP vereist autorisatie en deze sessie is niet-interactief, dus de OAuth flow kan hier niet draaien. Autoriseren gaat via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | geen data | geen data | n.v.t. |
| Impressions | geen data | geen data | n.v.t. |
| Clicks | geen data | geen data | n.v.t. |
| CTR | geen data | geen data | n.v.t. |
| CPC | geen data | geen data | n.v.t. |
| Frequency | geen data | geen data | n.v.t. |

**PostHog bevestigt aan de ontvangende kant dat er niets draait.** Dit is de volledige lijst UTM getagde pageviews over 15 augustus, projectbreed, alle domeinen:

| utm_source | utm_medium | utm_campaign | utm_content | Pageviews | Bezoekers |
|------------|-----------|--------------|-------------|-----------|-----------|
| chatgpt.com | (geen) | (geen) | (geen) | 12 | 9 |

Eén regel. Geen `meta`, geen `cpc`, geen `sybb`. Met een werkende Pipeboard koppeling zou het antwoord voor 15 augustus nog steeds "de campagne draait niet" zijn.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | geen data | n.v.t. | n.v.t. | n.v.t. | nooit gemeten |
| h12_b3_cta5 | geen data | n.v.t. | n.v.t. | n.v.t. | nooit gemeten |
| h13_b3_cta5 | geen data | n.v.t. | n.v.t. | n.v.t. | nooit gemeten |
| h14_b3_cta5 | geen data | n.v.t. | n.v.t. | n.v.t. | nooit gemeten |
| h15_b3_cta5 | geen data | n.v.t. | n.v.t. | n.v.t. | nooit gemeten |

**Beste variant:** niet te bepalen. Geen enkele variant heeft in de laatste 30 dagen verkeer geleverd.
**Slechtste variant:** idem.

## 3. Landing Page Health

### 3a. startyourballoonbusiness.com

**Nul events op 15 augustus.** Het laatste event van dit domein kwam binnen op **31 juli 2026**, vijftien dagen geleden. De volledige historie van de laatste 45 dagen is 22 dagen met verkeer, allemaal in juli, met een piek van 33 pageviews op 10 juli. Sinds 1 augustus: niets.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 0 | 0 | n.v.t. | 🔴 geen verkeer |
| Bounce Rate | onmeetbaar | onmeetbaar | <55% | 🔴 geen verkeer |
| Avg Session Duration | onmeetbaar | onmeetbaar | >90s | 🔴 geen verkeer |
| Scroll 25% | nooit gemeten | nooit gemeten | >80% | 🔴 event bestaat niet |
| Scroll 50% | nooit gemeten | nooit gemeten | >60% | 🔴 event bestaat niet |
| Scroll 75% | nooit gemeten | nooit gemeten | >40% | 🔴 event bestaat niet |
| Scroll 100% | nooit gemeten | nooit gemeten | >20% | 🔴 event bestaat niet |
| CTA Click Rate | nooit gemeten | nooit gemeten | >4% | 🔴 event bestaat niet |

Twee verschillende problemen, twee verschillende acties. De bovenste drie rijen zijn stil omdat er geen bezoekers zijn. De onderste vijf zijn stil omdat de events **nooit hebben bestaan**. De volledige event lijst van dit project bevat geen enkel scroll of CTA event: alleen `$pageview`, `$autocapture`, `$web_vitals`, `$pageleave`, `$rageclick` en een reeks custom events voor de inspiratie, family en wholesaler secties.

### 3b. SYBB event pagina's op sempertexeurope.com

Dit is waar SYBB feitelijk verkocht wordt. Ook hier is het stil.

| Metric | 15 aug | 7d Gemiddelde | Trend |
|--------|--------|---------------|-------|
| Pageviews SYBB pagina's | 1 | 22,0 | ↓ |
| Unieke bezoekers | 1 | 3,4 | ↓ |
| Sessies | 1 | 3,4 | ↓ |

De enige hit gisteren was `/en_GB/event/start-your-balloon-business-professional-7/register`. De 7-daagse cijfers worden bovendien gedomineerd door twee uitschieters (90 pageviews van 8 bezoekers op 10 augustus, 47 van 3 bezoekers op 14 augustus). Dat zijn een handvol mensen die veel pagina's aantikken, geen vraagstroom.

Over de hele week hebben alle SYBB registratiepagina's samen, over alle vier de talen, ongeveer 100 pageviews van hooguit 15 unieke bezoekers gehad.

### 3c. Hoofdsite, gefilterd op echt verkeer

| Metric | 15 aug | 7d Gemiddelde | Target | Status |
|--------|--------|---------------|--------|--------|
| Echte bezoekers | 126 | 254,1 | n.v.t. | ↓ |
| Echte sessies | 135 | 296,7 | n.v.t. | ↓ |
| Bounce Rate | 16,3% | 26,4% | <55% | 🟢 |
| Avg Session Duration | 427s | 455,7s | >90s | 🟢 |

Ruwe, ongefilterde cijfers ter vergelijking: 3.172 pageviews, 1.321 bezoekers, 1.336 sessies, 91,5% bounce, 43s gemiddelde sessieduur. Het verschil tussen die twee tabellen is precies het probleem dat in sectie 5 staat.

## 4. Funnel Drop-off

**Niet te bouwen.** De funnel uit de skill vereist vier stappen en drie daarvan bestaan niet als event in dit project.

| Stap | Status |
|------|--------|
| 1. Pageview op startyourballoonbusiness.com | 0 gisteren, 0 sinds 31 juli |
| 2. Scroll voorbij 50% | event bestaat niet |
| 3. CTA klik | event bestaat niet |
| 4. Pageview op /booking | pad bestaat niet, registratie loopt via `/event/.../register` |

**Grootste lek:** het lek zit vóór de funnel. Er is geen verkeer om te verliezen, en zelfs als het er was zou je niet kunnen zien waar het weglekt. De meetinfrastructuur is de blokkade, niet de conversie.

## 5. Rode Vlaggen 🚩

### 🚩 1. Botpiek van 1.247 bezoekers vervuilt al je rapportage

Gisteren registreerde PostHog 1.321 bezoekers, waarvan **1.247 met exact één pageview en referrer direct**. De signatuur is eenduidig: één pageview per persoon, verspreid over Brazilië, Seychellen, Colombia, Argentinië, India en Irak, allemaal op categoriepagina's.

| Landingspagina | Bot pageviews 15 aug |
|---|---|
| /en_GB/shop/category/foil-balloons-2915 | 99 |
| /folie-ballonnen | 73 |
| /en_GB/foil-balloons | 25 |
| /en_GB/shop/category/latex-balloons-2911 | 23 |
| /de/folienballons | 19 |

Dagelijkse omvang van dit patroon in augustus: 445, 596, 753, 687, 670, 628, 609, 564, 551, 341, 244, 137, 201, 145, en dan **1.247** op 15 augustus. Het weekgemiddelde was 312.

**Dit verklaart ook de "daling" die drie rapporten op rij is gemeld.** De bezoekersdaling van ~900 begin augustus naar ~250 rond 13 augustus was grotendeels dit botverkeer dat wegebde. Gefilterd bewoog je echte publiek van ongeveer 257 naar 251. Er was geen daling.

### 🚩 2. De 98% bounce pagina's zijn niet stuk

Direct gevolg van punt 1. Sessies per landingspagina, 9 tot en met 15 augustus:

| Landingspagina | Sessies | Bounce ruw | Echte sessies | Bounce echt |
|---|---|---|---|---|
| /folie-ballonnen | 74 | 100,0% | **0** | n.v.t. |
| /en_GB/shop/category/foil-balloons-2915 | 115 | 97,4% | **3** | **0,0%** |
| /de/shop/category/latex-ballons-2911 | 12 | 58,3% | 5 | 0,0% |
| /shop | 82 | 31,7% | 70 | 20,0% |
| / (homepage) | 447 | 11,9% | 415 | 5,1% |

`/folie-ballonnen` heeft in zeven dagen geen enkele echte bezoeker gehad. Dat is geen defect, dat is een pagina waar niemand komt. De drie echte bezoekers van de Engelse foil pagina bouncten geen van allen.

### 🚩 3. Rage clicks op de modelleerballonnen categorie

61 rage clicks van 11 bezoekers gisteren. Niet willekeurig verdeeld:

| Pagina | Rage clicks |
|---|---|
| Modelleerballonnen 260 (EN, NL, DE, incl. paginering) | 25 |
| /shop/cart | 5 (2 bezoekers) |
| Diverse Franse kleurcategorieën | 9 |

Modelleerballonnen 260 verzamelt 41% van alle rage clicks van gisteren, over drie talen en drie paginanummers. Dat wijst op een element dat op de categorietemplate niet reageert, waarschijnlijk paginering of een filter. De vijf rage clicks in de winkelwagen van twee bezoekers zijn de duurste van het stel, dat is friction op het punt van betalen.

### 🚩 4. Referrer exclusies staan nog steeds niet aan

Vierde rapport op rij. Op 15 augustus kwamen 1.811 pageviews van 114 bezoekers binnen met referrer `www.sempertexeurope.com`, je eigen domein. Dat is 57% van al je pageviews die als "verwijzend verkeer" wordt geteld.

### 🚩 Niet getriggerd

CPC boven target, frequency boven 3,0 en CPC stijging boven 20% zijn niet te beoordelen zonder Meta Ads data. Bounce boven 70% per UTM segment is niet te beoordelen, er is maar één UTM segment (chatgpt.com) en dat is te klein.

## 6. Top 3 Acties voor Vandaag

### 1. Zet bot filtering aan in PostHog

- **Wat:** activeer bot en crawler filtering in PostHog project settings, en zet daarna de referrer exclusies aan voor `sempertexeurope.com`, `rezolvbv-sh-sempertex.odoo.com` en `sempertexeurope.shipping-portal.com`.
- **Waarom:** 1.247 van 1.321 bezoekers gisteren waren bots, 94%. Elk rapport dat je nu leest, inclusief de bounce rates waar je gisteren actie op wilde nemen, is vervuild. En je staat op het punt betaald verkeer aan te zetten naar dezelfde pagina's.
- **Hoe:** PostHog project settings, sectie filtering. Vijf tot tien minuten werk.
- **Verwachte impact:** je dagrapport gaat van 1.321 naar ongeveer 126 bezoekers en van 91,5% naar 16,3% bounce. Dat is geen verlies, dat is de waarheid. Vanaf dat moment kun je op je eigen cijfers vertrouwen.
- **Escalatie:** Geel, jouw goedkeuring, ik kan de instelling niet zelf zetten.

### 2. Autoriseer Pipeboard, en schrap actiepunt 3 uit het ads rapport

- **Wat:** autoriseer de Pipeboard connector. Ga níet handmatig `/en_GB/shop/category/foil-balloons-2915` en `/folie-ballonnen` inspecteren.
- **Waarom:** de autorisatie loopt tien dagen. Los daarvan: de pagina-inspectie die gisteren als actiepunt 3 stond, is achterhaald door de data hierboven. Nul en drie echte sessies in zeven dagen, met 0% bounce. Er is niets kapot, dat zou verspilde tijd zijn.
- **Hoe:** claude.ai connector instellingen, of `/mcp` in een interactieve sessie.
- **Verwachte impact:** vanaf morgen sectie 2 met echte cijfers. Al blijft het antwoord "de campagne draait niet" tot je spend aanzet.
- **Escalatie:** Geel.

### 3. Meet de SYBB event pagina's voordat er budget in gaat

- **Wat:** definieer twee conversie-events op `/event/start-your-balloon-business-*/register` in alle vier de talen: één op het openen van het registratieformulier, één op een succesvolle registratie. Zet daarnaast scroll depth tracking op die pagina's aan.
- **Waarom:** sectie 4 is drie rapporten op rij leeg. SYBB verkoopt via deze pagina's, niet via de landing page, en er wordt op dit moment geen enkel signaal na de pageview gemeten. De pagina's kregen deze week ongeveer 100 pageviews van hooguit 15 mensen, dus je hebt nu de rust om dit goed te zetten.
- **Hoe:** PostHog autocapture actions op de registratieknop, of `posthog.capture()` in de Odoo event template. Bestaande custom events als `family_cta_click` en `wholesaler_cta_click` zijn het werkende voorbeeld.
- **Verwachte impact:** de eerste dag dat er wél betaald verkeer is, weet je meteen of mensen doorklikken. Zonder dit meet je alleen dat ze arriveerden.
- **Escalatie:** Oranje, dit raakt de Odoo templates.

### Kanttekening

Al drie rapporten op rij is de kern hetzelfde: er is geen SYBB campagne actief en de meetinfrastructuur is niet klaar. Dat is geen slecht nieuws, dat is een lege agenda vlak vóór de piek. Actie 1 en 3 kosten samen minder dan een dagdeel en bepalen of het eerste euro's advertentiebudget straks meetbaar zijn of niet.

---

### Bronvermelding

Alle cijfers uit PostHog project STX EU (149694), timezone UTC, opgehaald op 16 augustus 2026. Meting over 15 augustus 2026 00:00 tot 16 augustus 2026 00:00 UTC. Het 7-daags gemiddelde loopt van 8 tot en met 14 augustus 2026. "Echte" cijfers sluiten sessies uit met exact één pageview én referrer direct. Meta Ads MCP (Pipeboard) niet geraadpleegd wegens ontbrekende autorisatie. Geen Google MCPs gebruikt, niets naar de Meta Ads Tracker Sheet geschreven.
