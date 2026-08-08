# SYBB Daily Report, 7 augustus 2026

**Databronnen:** PostHog MCP (project STX EU, id 149694). Meta Ads MCP (Pipeboard) **niet beschikbaar**.
**Gegenereerd:** 8 augustus 2026

---

## 1. Samenvatting

De SYBB funnel draait op nul betaald verkeer. Voor de derde dag op rij kon de Meta Ads data niet worden opgehaald, en PostHog bevestigt waarom dat waarschijnlijk niet uitmaakt: er is op 7 augustus geen enkele betaalde klik binnengekomen, net als op elke andere dag in de afgelopen maand. De landing page startyourballoonbusiness.com kreeg gisteren nul pageviews.

Wat er wel gebeurde, gebeurde op sempertexeurope.com. De SYBB event pagina's kregen 10 views van 4 personen, ruim vier keer het weekgemiddelde van 2,4 views per dag. Klein in absolute zin, maar het is de enige SYBB beweging die er is.

Het echte signaal van gisteren zit elders: de site brede bounce rate sprong naar 71,2% tegenover 50,3% weekgemiddelde, en de sessieduur zakte met 28%. Dat is bijna volledig toe te schrijven aan Direct verkeer met 80,9% bounce. Zie sectie 5.

---

## 2. Meta Ads Performance

**Niet beschikbaar.** De Pipeboard connector is in deze sessie niet geautoriseerd, dus campagne `2026: SYBB` kon niet worden uitgelezen. Geen spend, impressions, clicks, CTR, CPC of frequency. Dit is de derde opeenvolgende dag zonder Meta data (6, 7 en 8 augustus).

Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

### Wat PostHog wel kan vaststellen

PostHog meet het resultaat van de ads, ook zonder toegang tot de ads zelf. Over de periode 8 juli tot en met 8 augustus is er **nul verkeer** met `utm_medium=cpc` of een Meta gerelateerde `utm_source`. Geen enkele klik.

Alle UTM getagde bezoekers op 7 augustus:

| Bron | Medium | Campagne | Content | Events | Personen |
|------|--------|----------|---------|--------|----------|
| mailjet | email | workshop_tobi_promo_202608 | mail3 | 18 | 5 |
| mailjet | email | inspiration_promo_202607 | mail2_calculator | 13 | 1 |
| youtube | organic | content | inspiration_page | 11 | 3 |
| Pinterest | organic | (geen) | (geen) | 1 | 1 |

Email en organic dragen de dag. Betaald staat op nul.

### Ad Variant Performance

Niet te rapporteren. Er zijn geen clicks per `utm_content` variant (h11_b3_cta5 tot en met h15_b3_cta5) omdat er geen betaald verkeer loopt. De hele variant tabel uit de skill is leeg zolang de campagne stilstaat.

---

## 3. Landing Page Health

### startyourballoonbusiness.com

| Metric | 7 aug | Laatste 14d | Status |
|--------|-------|-------------|--------|
| Pageviews | 0 | 3 totaal | 🔴 |
| Unieke bezoekers | 0 | 3 totaal | 🔴 |
| Sessies | 0 | 3 totaal | 🔴 |

De pixel werkt, maar er komt niemand. De laatste hit op dit domein was **31 juli 2026**, zeven dagen voor de rapportdatum. Over 25 juli tot 8 augustus staan er in totaal 3 pageviews van 3 personen. Bounce rate, scroll depth en sessieduur zijn op nul verkeer niet te berekenen.

### sempertexeurope.com (waar de SYBB funnel feitelijk draait)

| Metric | 7 aug | 7d gemiddelde | Target | Trend | Status |
|--------|-------|---------------|--------|-------|--------|
| Bezoekers | 854 | 854 | meten | → | n.v.t. |
| Pageviews | 4.066 | 4.574 | meten | ↓ | n.v.t. |
| Sessies | 885 | 949 | meten | → | n.v.t. |
| Bounce Rate | 71,2% | 50,3% | <55% | ↑ | 🔴 |
| Avg Session Duration | 171s | 237s | >90s | ↓ | 🟢 |
| Scroll 25 / 50 / 75 / 100% | geen data | geen data | >80 / 60 / 40 / 20% | n.v.t. | ⚪ |
| CTA Click Rate | geen data | geen data | >4% | n.v.t. | ⚪ |

7d gemiddelde loopt van 31 juli tot en met 6 augustus.

**Scroll depth en CTA clicks staan nog steeds niet in de event taxonomie.** PostHog ontvangt op dit project alleen `$pageview`, `$rageclick`, autocapture en een set custom events (`inspiration_view`, `video_click`, `social_click`, `calc_mix`, `reorder_answered`). Er is geen scroll event en geen CTA of booking event. Dit stond ook al in het rapport van 8 augustus en is nog niet opgelost. Zolang dit ontbreekt zijn vier van de zeven rijen in deze tabel structureel leeg.

### SYBB pagina's specifiek

| Dag | SYBB views | SYBB personen |
|-----|-----------|---------------|
| **7 aug** | **10** | **4** |
| 6 aug | 1 | 1 |
| 5 aug | 1 | 1 |
| 4 aug | 4 | 2 |
| 3 aug | 3 | 3 |
| 2 aug | 3 | 2 |
| 1 aug | 1 | 1 |
| 31 jul | 4 | 3 |

Gisteren was de beste SYBB dag van de week, 10 views tegenover een weekgemiddelde van 2,4. De views verdeelden zich over `/event/start-your-balloon-business-professional-8/register` (5 views, 2 personen) en `/event/start-your-balloon-business-professional-7/register` (3 views, 2 personen). De `/events` hub zelf trok 14 views van 11 personen.

---

## 4. Funnel Drop-off

**Niet te berekenen.** De funnel uit de skill vereist vier stappen:

```
Pageview (100%)  →  Scroll 50% (?)  →  CTA Click (?)  →  /booking (?)
     ✅ gemeten        ❌ geen event      ❌ geen event     ❌ geen event
```

Alleen stap 1 wordt gemeten. Stap 2, 3 en 4 bestaan niet als event in dit project.

Wat wel meetbaar is, is een ruwe proxy op de main site: van 858 bezoekers op 7 augustus bereikten 11 personen de `/events` hub (1,3%) en 4 personen een SYBB registratiepagina (0,5%).

**Grootste lek:** de stap van site bezoeker naar events hub. 98,7% van je bezoekers ziet je workshop aanbod nooit. Maar let op, dit is een proxy zonder intentiefilter en de meeste van die 858 bezoekers kwamen voor de shop, niet voor educatie. Top pagina's van gisteren waren `/shop` (190 views), `/web/login` (90) en de homepage (86). Zie de kanttekening in sectie 6.

---

## 5. Rode Vlaggen 🚩

**1. Bounce rate 71,2%, ruim 41% boven het weekgemiddelde van 50,3%** 🔴
Dit is de scherpste afwijking van de dag. De oorzaak is te isoleren:

| Kanaal | Bezoekers | Views | Bounce Rate | Aandeel sessies |
|--------|-----------|-------|-------------|-----------------|
| Direct | 615 | 2.262 | **80,9%** | 71,2% |
| Referral | 161 | 1.018 | 70,3% | 18,6% |
| Organic Search | 70 | 742 | 1,4% | 8,1% |
| AI | 9 | 35 | 22,2% | 1,0% |
| Email | 5 | 5 | 20,0% | 0,6% |
| Organic Video | 3 | 3 | 33,3% | 0,3% |
| Organic Social | 1 | 1 | 100% | 0,1% |

Direct verkeer is 72% van je sessies en bounct op 80,9%. Organic Search bounct op 1,4%, wat een verdacht lage waarde is. Deze combinatie, veel Direct met extreem hoge bounce naast Organic met bijna nul bounce, wijst eerder op bot of crawler verkeer dan op een echte gedragsverandering bij je publiek. Verifieer dit voordat je conclusies trekt over pagina kwaliteit.

**2. Sessieduur gedaald van 237s naar 171s, min 28%** 🟡
Nog steeds boven het target van 90s, dus geen alarm op zichzelf. Maar dezelfde richting als de bounce rate, en waarschijnlijk dezelfde oorzaak.

**3. Nul betaald verkeer, 37 dagen op rij** 🔴
De laatste betaalde klik dateert van 1 juli 2026. Dat is geen dagafwijking meer, dat is een stilgevallen kanaal.

**4. Landing page zonder verkeer, 7 dagen op rij** 🔴
startyourballoonbusiness.com kreeg voor het laatst een bezoeker op 31 juli.

**5. Conversie events ontbreken nog steeds** 🔴
Geen scroll, geen CTA click, geen booking event. Dit blokkeert secties 3 en 4 van dit rapport permanent, niet incidenteel.

### Niet rood

Rageclicks daalden naar 65 van 20 personen, tegenover een weekgemiddelde van 111 per dag. De piek van 5 augustus (220) is voorbij. Dead clicks worden op dit project niet gemeten.

---

## 6. Top 3 Acties voor Vandaag

### 1. Autoriseer Pipeboard, en verifieer of campagne `2026: SYBB` überhaupt nog loopt

**Wat:** Autoriseer de Pipeboard connector via je claude.ai connector instellingen. Open daarna Meta Ads Manager en controleer de status van campagne `2026: SYBB`.
**Waarom:** PostHog ziet 37 dagen geen betaalde klik. Dat betekent één van twee dingen: de campagne staat uit, of hij loopt met kapotte tracking en je betaalt voor verkeer dat je niet meet. Deze twee scenario's vragen tegenovergestelde acties, en je kunt ze niet uit elkaar houden zonder de spend data.
**Hoe:** Connector instellingen op claude.ai, of `/mcp` in een interactieve sessie.
**Verwachte impact:** Ontgrendelt secties 2 en 4 van dit rapport. Zonder dit blijft dit rapport half.
**Escalatie:** 🟡 Geel, jouw actie nodig.

### 2. Zet scroll en CTA events op de SYBB pagina's

**Wat:** Voeg drie events toe: scroll depth (25/50/75/100%), CTA click op de "Book Now" knop, en een booking confirmation event. Zowel op startyourballoonbusiness.com als op de `/event/start-your-balloon-business-professional-*/register` pagina's.
**Waarom:** Vier van de zeven rijen in sectie 3 zijn leeg en de complete funnel in sectie 4 is onberekenbaar. Dit is de derde dag dat dit gerapporteerd wordt zonder dat er iets veranderde. Zolang dit blijft staan kun je een pagina die verkeer krijgt niet optimaliseren, want je ziet alleen dat mensen kwamen, niet wat ze deden.
**Hoe:** PostHog autocapture config uitbreiden met scroll tracking, plus custom events via de PostHog snippet. De registratiepagina's draaien op Odoo, daar kan het via een custom JS blok.
**Verwachte impact:** Maakt het verschil tussen "10 mensen keken" en "10 mensen keken, 6 scrollden voorbij de prijs, 1 klikte". Dat eerste is een getal, dat tweede is een diagnose.
**Escalatie:** 🟠 Oranje, technische implementatie.

### 3. Filter bot verkeer uit voor je de bounce rate serieus neemt

**Wat:** Controleer of de 615 Direct bezoekers van gisteren echt zijn. Bekijk een steekproef session recordings van Direct sessies met bounce, en zet zo nodig PostHog's bot filtering strakker.
**Waarom:** 80,9% bounce op Direct naast 1,4% op Organic Search is geen normaal patroon. Als dit bots zijn, is je werkelijke bounce rate dichter bij het weekgemiddelde van 50,3% en is rode vlag 1 een spookmelding. Als het geen bots zijn, is er gisteren iets kapot gegaan op je entry pagina's en dan is het urgent. Je kunt nu niet zeggen welke.
**Hoe:** PostHog project settings, "Filter out internal and test users" plus de bot blocklist. Daarna deze query herhalen.
**Verwachte impact:** Voorkomt dat je optimaliseert op een cijfer dat niet je publiek beschrijft.
**Escalatie:** 🟢 Groen, kan direct.

---

## Kanttekening bij dit rapport

De skill `daily-sybb-report` gaat ervan uit dat de SYBB funnel op startyourballoonbusiness.com draait, gevoed door Meta ads. Geen van beide is op 7 augustus waar. De verkoop loopt via de event registratiepagina's op sempertexeurope.com en er is geen advertentiebudget actief.

De cijfers in sectie 3 en 4 beschrijven daarom de main site, niet de landing page. De targets uit de skill (bounce <55%, scroll >60%, CTA >4%) zijn geijkt op een landing page met betaald verkeer en zijn niet één op één toepasbaar op een webshop met 4.000 pageviews per dag. Lees de 🔴 op bounce rate als "onderzoek dit", niet als "de landing page faalt".

De cross-referencing tussen Meta Ads en PostHog, wat de kern van dit rapport hoort te zijn, was deze run niet mogelijk. Er is geen ad data en geen ad verkeer om tegen elkaar te leggen.

**Gebruikte bronnen:** PostHog MCP (project STX EU). Meta Ads MCP niet geautoriseerd. Geen Google MCPs aangeroepen, geen writes naar de Meta Ads Tracker Google Sheet.
