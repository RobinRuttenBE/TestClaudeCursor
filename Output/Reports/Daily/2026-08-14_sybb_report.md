# SYBB Daily Report, 14 augustus 2026

> **Databronnen:** PostHog MCP (project STX EU, 149694, timezone UTC). Meta Ads MCP niet beschikbaar, zie sectie 2.
> **Gegenereerd:** 15 augustus 2026. Alleen PostHog en Meta Ads MCP geraadpleegd. Geen Google MCPs, niets naar de tracker Sheet geschreven.

## 1. Samenvatting

**De landing page is nu twee weken volledig stil en de SYBB verkoop loopt uitsluitend via de event pagina's op de hoofdsite.** `startyourballoonbusiness.com` stuurde op 14 augustus nul events naar PostHog. Het laatste event van dat domein kwam binnen op **31 juli 2026**, veertien dagen eerder. Alles in dit rapport dat over de landing page gaat is dus niet slecht, het is onmeetbaar.

Meta Ads is de negende dag op rij niet op te halen omdat Pipeboard niet geautoriseerd is. Dat maakt vandaag weinig uit, want PostHog kan aan de ontvangende kant meekijken en ziet over de laatste 30 dagen **nul pageviews met `utm_source=meta`, nul met `utm_medium=cpc` en nul met `utm_campaign=sybb`**, op geen enkel domein. De campagne staat aantoonbaar uit.

De SYBB event pagina's op `sempertexeurope.com` lieten gisteren 47 pageviews zien, maar van slechts **3 unieke bezoekers in 4 sessies, allemaal uit België**. Dat is intern verkeer, geen vraag uit de markt. Los daarvan verdient de bredere site aandacht: de dagelijkse bezoekers zakten van 900 op 6 augustus naar 250 gisteren.

## 2. Meta Ads Performance

**Niet beschikbaar.** De Pipeboard Meta Ads MCP vereist autorisatie en deze sessie is niet interactief, dus de OAuth flow kan hier niet draaien. Autoriseren gaat via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | geen data | geen data | n.v.t. |
| Impressions | geen data | geen data | n.v.t. |
| Clicks | geen data | geen data | n.v.t. |
| CTR | geen data | geen data | n.v.t. |
| CPC | geen data | geen data | n.v.t. |
| Frequency | geen data | geen data | n.v.t. |

**De autorisatie is niet het echte probleem.** PostHog meet aan de ontvangende kant of er advertentieverkeer binnenkomt, onafhankelijk van Pipeboard. Dit is de volledige lijst UTM getagde pageviews over 14 augustus, projectbreed:

| utm_source | utm_medium | utm_campaign | utm_content | Pageviews | Bezoekers |
|------------|-----------|--------------|-------------|-----------|-----------|
| chatgpt.com | (geen) | (geen) | (geen) | 9 | 7 |
| Pinterest | organic | (geen) | (geen) | 2 | 1 |
| mailjet | email | inspiration_promo_202607 | mail2_calculator | 1 | 1 |

Geen `meta`, geen `cpc`, geen `sybb`. Met een werkende Pipeboard koppeling zou het antwoord voor 14 augustus nog steeds "de campagne draait niet" zijn.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | geen data | n.v.t. | n.v.t. | n.v.t. | nooit gemeten |
| h12_b3_cta5 | geen data | n.v.t. | n.v.t. | n.v.t. | nooit gemeten |
| h13_b3_cta5 | geen data | n.v.t. | n.v.t. | n.v.t. | nooit gemeten |
| h14_b3_cta5 | geen data | n.v.t. | n.v.t. | n.v.t. | nooit gemeten |
| h15_b3_cta5 | geen data | n.v.t. | n.v.t. | n.v.t. | nooit gemeten |

**Beste variant:** niet te bepalen, geen enkele variant heeft in de laatste 30 dagen verkeer geleverd.
**Slechtste variant:** idem.

## 3. Landing Page Health

**Geen enkele metric is meetbaar voor 14 augustus.** De reden verschilt per rij en dat verschil bepaalt de actie.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 0 | 0 | n.v.t. | 🔴 tracking dood |
| Bounce Rate | onmeetbaar | onmeetbaar | <55% | 🔴 tracking dood |
| Avg Session Duration | onmeetbaar | onmeetbaar | >90s | 🔴 tracking dood |
| Scroll 25% | nooit gemeten | nooit gemeten | >80% | 🔴 event bestaat niet |
| Scroll 50% | nooit gemeten | nooit gemeten | >60% | 🔴 event bestaat niet |
| Scroll 75% | nooit gemeten | nooit gemeten | >40% | 🔴 event bestaat niet |
| Scroll 100% | nooit gemeten | nooit gemeten | >20% | 🔴 event bestaat niet |
| CTA Click Rate | nooit gemeten | nooit gemeten | >4% | 🔴 event bestaat niet |

Twee losse problemen, niet één:

1. **De tracking is dood.** Het domein `www.startyourballoonbusiness.com` verstuurde tussen 16 en 31 juli nog 19 pageviews van 19 bezoekers, allemaal `$direct` en zonder UTM. Sinds 31 juli komt er niets meer binnen.
2. **Scroll depth en CTA clicks zijn nooit geïmplementeerd.** In de volledige event taxonomie van dit project bestaan die events niet. De KPI targets in `CLAUDE.md` voor scroll 25/50/75/100% en CTA click rate meten op dit moment dus niets, ook niet als de tracking morgen weer aan gaat.

### Waar de SYBB vraag wél gemeten wordt

De SYBB workshop verkoopt via event pagina's op `sempertexeurope.com`. Dat verkeer is er wel:

| Dag | Pageviews | Unieke bezoekers | Sessies |
|-----|-----------|------------------|---------|
| 14 aug | 47 | 3 | 4 |
| 13 aug | 2 | 2 | 2 |
| 12 aug | 1 | 1 | 1 |
| 11 aug | 1 | 1 | 1 |
| 10 aug | 90 | 8 | 8 |
| 9 aug | 3 | 3 | 3 |
| 8 aug | 10 | 5 | 5 |
| 7 aug | 10 | 4 | 4 |
| **7d gemiddelde** | **16,7** | **3,4** | **3,4** |

47 pageviews klinkt als een piek van bijna 3x het gemiddelde, maar de opsplitsing ontkracht dat volledig:

| Sessie | Duur | Pageviews | Unieke paden | Referrer | Land |
|--------|------|-----------|--------------|----------|------|
| 019ffff8 | 4m 09s | 36 | 12 | `/de/event/start-your-balloon-business-professionell-9/register` | België |
| 019fff2b | 58m 37s | 9 | 2 | `/en_GB/events` | België |
| 019ffff1 | 0s | 1 | 1 | `/en_GB/events` | België |
| 01a0009e | 0s | 1 | 1 | `/events` | België |

Eén sessie bekeek 12 verschillende taalvarianten van dezelfde SYBB registratiepagina in vier minuten. Dat is een interne controle of contentbewerking, geen prospect. **De werkelijke externe SYBB vraag op 14 augustus is nul.**

Sessies die binnenkomen op een event pagina, ter referentie:

| Metric | 14 aug | 7d gemiddelde | Opmerking |
|--------|--------|---------------|-----------|
| Sessies | 3 | 9,6 | te klein voor conclusies |
| Bounce rate | 0,0% | 19,3% | 3 sessies, statistisch betekenisloos |
| Avg sessieduur | 245s | 434s | idem |
| Pageviews per sessie | 2,7 | 4,9 | idem |

## 4. Funnel Drop-off

De funnel uit de skill (`Pageview → Scroll 50% → CTA Click → /booking`) is **niet te bouwen**. Stap 2 en 3 bestaan niet als event, stap 4 bestaat niet als pagina. Er is geen `/booking` pad in het project.

Wat wel meetbaar is, is de route over de hoofdsite:

```
/events hub          26 pageviews (NL) + 15 (EN) + 14 (DE) + 2 (FR)  =  57
      ↓
SYBB register pagina  47 pageviews, maar slechts 3 bezoekers
      ↓
Registratie voltooid  NIET MEETBAAR, geen bevestigingsevent
```

**Grootste lek:** niet aan te wijzen, en dat is zelf de bevinding. De funnel eindigt blind. De enige `confirmation` pagina's in het project (`/shop/confirmation` en taalvarianten, 698 pageviews over 30 dagen) horen bij de webshop, niet bij event registraties. Er is dus geen enkele manier om te zien of een bezoeker van een SYBB register pagina daadwerkelijk boekt.

## 5. Rode Vlaggen 🚩

1. **Landing page tracking is 14 dagen dood.** Laatste event 31 juli 2026. Dit is de langste stilte tot nu toe en het loopt op.
2. **Nul Meta verkeer over 30 dagen, projectbreed.** Niet weinig, nul. De campagne `2026: SYBB` levert niets af.
3. **Pipeboard negen dagen niet geautoriseerd.** Blokkeert alle spend, CPC en frequency data, ook het `/ads-report` en `/ads-auto-optimize` commando.
4. **Scroll depth en CTA click events bestaan niet.** Vier van de zeven KPI targets in `CLAUDE.md` zijn onmeetbaar bij de bron.
5. **Geen registratie bevestigingsevent.** De SYBB funnel heeft geen conversiepunt, dus conversie ratio is per definitie niet te berekenen.
6. **Sitebrede bezoekersdaling.** 900 → 858 → 758 → 692 → 511 → 434 → 287 → 372 → 250 unieke bezoekers van 6 tot 14 augustus. Dat is 55% onder het 7 daags gemiddelde van 559 en de trend is negen dagen consistent dalend. Dit staat los van SYBB, maar het is het grootste cijfer in de dataset en verdient een aparte blik.

Geen rode vlag op frustratie: alle 105 rage clicks van gisteren zaten op webshop pagina's (`/shop/cart`, categoriepagina's), geen enkele op een SYBB of event pagina.

## 6. Top 3 Acties voor Vandaag

### 1. Zet de PostHog tracking op de landing page terug aan, of schrap de pagina uit dit rapport

- **Wat:** Controleer of de PostHog snippet nog in de Wix pagina van `startyourballoonbusiness.com` staat en of de project API key nog klopt (`phc_yosUlZYJ35Lkjw3qfcwu4cm4x07lF7cIY17F8AqIpNB`). Als de pagina bewust is uitgefaseerd, haal hem dan uit de skill en herschrijf het rapport rond de event pagina's.
- **Waarom:** 14 dagen nul events, terwijl de skill de halve rapportstructuur op dit domein baseert.
- **Hoe:** Wix Editor, custom code sectie. De Wix MCP vraagt ook om autorisatie, dus dit is handwerk.
- **Verwachte impact:** Secties 3 en 4 worden weer invulbaar, of het rapport wordt eerlijk korter.
- **Escalatie:** 🟠 Oranje, Wix Editor. Bij uitfaseren 🔴 Rood, strategiekeuze.

### 2. Autoriseer Pipeboard en bevestig daarna of de campagne bewust uit staat

- **Wat:** Autoriseer de Pipeboard Meta Ads connector, en kijk vervolgens in Meta Ads Manager of `2026: SYBB` gepauzeerd is of leeg budget heeft.
- **Waarom:** Negen dagen zonder data, plus nul Meta verkeer in PostHog over 30 dagen. Die twee samen wijzen op een uitgezette campagne, maar zonder Pipeboard blijft dat een gok.
- **Hoe:** claude.ai connector instellingen, of `/mcp` in een interactieve sessie.
- **Verwachte impact:** Sectie 2 wordt invulbaar en `/ads-auto-optimize` werkt weer.
- **Escalatie:** 🟡 Geel, jouw goedkeuring nodig.

### 3. Voeg een registratie bevestigingsevent toe aan de SYBB event pagina's

- **Wat:** Laat de Odoo event registratie een PostHog event vuren bij een voltooide inschrijving, bijvoorbeeld `event_registration_completed` met de event naam en taal als property.
- **Waarom:** De funnel eindigt nu blind. Zonder conversiepunt is de KPI "LP Conversie Rate >5%" niet te berekenen, ook niet als alles anders wel werkt.
- **Hoe:** Odoo website tracking, of een pageview op een bevestigingspad dat uniek is voor events.
- **Verwachte impact:** De SYBB funnel krijgt voor het eerst een meetbaar einde, waarmee ad spend beoordeeld kan worden zodra de campagne weer aan gaat.
- **Escalatie:** 🟡 Geel, jouw goedkeuring nodig.

---

*Vervolg: zolang de landing page tracking dood is en Meta geen verkeer levert, blijft dit rapport grotendeels een tracking status. De eerste twee acties bepalen of het morgen inhoudelijk kan worden.*
