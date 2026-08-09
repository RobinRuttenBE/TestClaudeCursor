# SYBB Daily Report, zaterdag 8 augustus 2026

> **Databronnen:** PostHog MCP (project STX EU, id 149694). Meta Ads MCP (Pipeboard) was in deze sessie niet geautoriseerd, zie sectie 2.
> Geen Google MCPs gebruikt, niet naar de Google Sheet tracker geschreven, conform instructie.

---

## 1. Samenvatting

De SYBB landing page (startyourballoonbusiness.com) heeft op 8 augustus **nul** events geregistreerd, de achtste stille dag op rij. Het echte SYBB verkeer loopt via de event registratiepagina's op sempertexeurope.com, en dáár was 8 augustus juist een goede dag: 10 pageviews van 5 unieke bezoekers over 5 sessies, ongeveer het dubbele van het weekgemiddelde, met **nul bounces**. Alle vijf de sessies waren serieus betrokken.

Het probleem zit één stap verder in de funnel. Van die 5 sessies bereikte er 1 het registratieformulier en **0** de bevestigingspagina. Site breed voltooide niemand op 8 augustus een registratie, terwijl er 6 mensen aan begonnen.

Daarnaast loopt er sinds 6 augustus een bredere degradatie op de hele site: de bounce rate klom van 38,7% (5 aug) naar 73,8% (8 aug) en de sessieduur zakte van 300s naar 149s. Dit is niet SYBB specifiek en verdient losse aandacht.

---

## 2. Meta Ads Performance

**Data niet beschikbaar.** De Pipeboard Meta Ads MCP is niet geautoriseerd in deze sessie, en autoriseren kan hier niet omdat de sessie non interactief is. Vierde dag op rij zonder Meta data.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | n.b. | n.b. | n.b. |
| Impressions | n.b. | n.b. | n.b. |
| Clicks | n.b. | n.b. | n.b. |
| CTR | n.b. | n.b. | n.b. |
| CPC | n.b. | n.b. | n.b. |
| Frequency | n.b. | n.b. | n.b. |

### Wat PostHog wel bevestigt over betaald verkeer

**38 dagen nul betaald verkeer.** In de volledige UTM breakdown over de laatste 30 dagen komt `utm_source=meta` niet één keer voor. De laatste `meta/cpc/sybb` klik dateert van 1 juli 2026. Er is ook geen Paid Social kanaal in de sessiedata.

Het verkeer dat er wél was op 8 augustus, per UTM:

| utm_source | medium | campagne | Events | Personen |
|-----------|--------|----------|--------|----------|
| chatgpt.com | (geen) | (geen) | 10 | 7 |
| mailjet | email | workshop_tobi_promo_202608 | 1 | 1 |

De `workshop_tobi_promo_202608` mailing is vrijwel uitgewerkt: 42 events op 5 augustus, 8 op 6 aug, 5 op 7 aug, 1 op 8 aug.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |
| h12_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |
| h13_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |
| h14_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |
| h15_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |

Geen enkele `utm_content` waarde uit de SYBB batch is in 30 dagen in PostHog binnengekomen. **Beste variant:** niet vast te stellen. **Slechtste variant:** niet vast te stellen. Er draait geen budget.

---

## 3. Landing Page Health

### 3a. startyourballoonbusiness.com (de eigenlijke SYBB landing page)

**Nul events op 8 augustus.** Laatste activiteit: 31 juli 2026, 2 events van 1 persoon. Acht dagen volledig stil.

Verloop van de stilte (events per dag op dat domein):

| Datum | Events | Personen |
|-------|--------|----------|
| 1 t/m 8 aug | 0 | 0 |
| 31 jul | 2 | 1 |
| 29 jul | 2 | 1 |
| 27 jul | 1 | 1 |
| 20 jul | 8 | 6 |
| 10 jul | 33 | 4 |

De pixel werkt, de bron van bezoekers ontbreekt. Zonder ads komt hier niemand.

### 3b. SYBB registratiepagina's op sempertexeurope.com (waar het echte verkeer zit)

| Metric | 8 aug | 7d gemiddelde | Trend |
|--------|-------|---------------|-------|
| Pageviews | 10 | 4,7 | ↑ |
| Unieke bezoekers | 5 | 2,7 | ↑ |
| Sessies | 5 | 2,7 | ↑ |
| Bounces | 0 | n.v.t. | → |

Bezochte SYBB pagina's op 8 augustus:

| Pagina | Pageviews | Personen |
|--------|-----------|----------|
| `/event/start-your-balloon-business-professional-8/register` | 4 | 2 |
| `/en_GB/event/start-your-balloon-business-professional-9/register` | 3 | 2 |
| `/fr/event/start-your-balloon-business-professionnel-8/register` | 1 | 1 |
| `/event/start-your-balloon-business-professional-7/register` | 1 | 1 |
| `/event/start-your-balloon-business-professional-9/register` | 1 | 1 |

### 3c. Site breed (sempertexeurope.com)

| Metric | 8 aug | 7d gemiddelde | Target | Status |
|--------|-------|---------------|--------|--------|
| Bezoekers | 766 | 863 | meten | ↓ 11% |
| Pageviews | 2.830 | 4.699 | meten | ↓ 40% |
| Sessies | 826 | 964 | meten | ↓ 14% |
| Bounce Rate | 73,8% | 51,4% | <55% | 🔴 |
| Avg Session Duration | 154s | 185s | >90s | 🟢 |
| Scroll 25 / 50 / 75 / 100% | niet gemeten | niet gemeten | >80/60/40/20% | ⚫ |
| CTA Click Rate | niet gemeten | niet gemeten | >4% | ⚫ |

⚫ = **niet meetbaar**. Er bestaat geen scroll event in dit PostHog project en de `sessions` tabel heeft geen scroll kolom. Er is ook geen CTA click event gedefinieerd. Dit is een meetgat, geen slechte score. Zie actie 3.

---

## 4. Funnel Drop-off

### SYBB funnel, 8 augustus

```
SYBB register pagina    5 sessies    100%
        ↓                             -80%
/registratie formulier  1 sessie      20%
        ↓                            -100%
/registratie-voltooid   0 sessies      0%
```

**Grootste lek: de register pagina zelf.** Vier van de vijf sessies kwamen op de SYBB register pagina en gingen niet door naar het formulier.

De duidelijkste casus is een sessie van 39 minuten (2.331s) via Organic Social. Deze bezoeker kwam binnen op de homepage, ging naar `/events`, klikte door naar `/event/start-your-balloon-business-professional-8/register`, en **eindigde daar**. Geen bounce, 16 clicks, bijna veertig minuten aandacht, en toch geen registratie. Dat is geen interesse probleem.

De enige sessie die het formulier bereikte was Frans: 8 pagina's, **283 clicks**, 1.901s, route `/fr/shop` → `/fr/event/start-your-balloon-business-professionnel-8/register` → `/fr/registratie` → terug naar `/fr/shop`. Ook deze rondde niet af. 283 clicks in één sessie op een registratieformulier wijst op wrijving, niet op twijfel.

### Site brede registratie funnel (alle events, niet alleen SYBB)

| Datum | `/registratie` starts | `/registratie-voltooid` | Voltooiing |
|-------|----------------------|------------------------|------------|
| 8 aug | 6 | **0** | **0%** |
| 7 aug | 15 | 2 | 13% |
| 6 aug | 11 | 4 | 36% |
| 5 aug | 23 | 1 | 4% |
| 4 aug | 26 | 7 | 27% |

En de shop checkout, ter vergelijking:

| Datum | Checkout pageviews |
|-------|--------------------|
| 8 aug | 15 |
| 7 aug | 40 |
| 6 aug | 32 |
| 5 aug | 77 |
| 4 aug | 69 |

---

## 5. Rode Vlaggen 🚩

**1. Nul registratie voltooiingen site breed op 8 augustus.** Zes mensen begonnen, niemand kwam aan. De dagen ervoor lag dat tussen 4% en 36%. Bij deze aantallen kan dit toeval zijn, maar in combinatie met de 283 click sessie is het het onderzoeken waard.

**2. Direct verkeer is in vier dagen ingestort in kwaliteit.** Dit is de motor achter de site brede bounce stijging. Direct is 66% van alle sessies.

| Datum | Direct sessies | Bounce | Avg duur |
|-------|---------------|--------|----------|
| 2 aug | 622 | 38,0% | 76s |
| 4 aug | 758 | 37,1% | 176s |
| 5 aug | 723 | 37,0% | 224s |
| 6 aug | 729 | 76,8% | 179s |
| 7 aug | 640 | 80,4% | 107s |
| 8 aug | 572 | **88,7%** | **50s** |

**3. Het betrokken direct verkeer is verdwenen, niet verslechterd.** Op 4 augustus kwamen 277 direct sessies binnen op `/en_GB` met 3,2% bounce. Op 8 augustus zijn dat er nog 32. De homepage instappers (`/`, `/en_GB`, `/de`) zakten van ongeveer 450 sessies naar ongeveer 53. Wat overblijft is een lange staart van losse, diepe instappen met hoge bounce. Meest waarschijnlijke verklaring: een herkenbaar terugkerend segment is weggevallen (weekend plus de aflopende mailjet campagne), waardoor een constante bodem van bot en scraper verkeer nu het gemiddelde bepaalt. **Dit is een hypothese, geen vaststelling.** Verifieer voordat je erop stuurt.

**4. SYBB landing page acht dagen op nul.** Zie sectie 3a.

**5. Meta Ads blind, dag vier.** Geen spend, CPC, CTR of frequency. Ad fatigue en CPC stijging zijn niet te controleren.

**6. Scroll depth en CTA clicks zijn niet meetbaar.** Vier van de zeven KPI's uit de skill kunnen niet gerapporteerd worden.

**7. Vroege waarschuwing voor vandaag (9 aug, deels).** 139 sessies met 94,2% bounce en 23s gemiddelde duur. Als dit tegen het einde van de dag zo blijft, is het geen weekendpatroon meer maar een storing.

---

## 6. Top 3 Acties voor Vandaag

### 1. Test de registratieflow zelf, in het Frans

- **Wat:** Doorloop `/fr/event/start-your-balloon-business-professionnel-8/register` tot en met de bevestiging, op mobiel en desktop. Let op validatiefouten, verplichte velden en de betaalstap.
- **Waarom:** Nul voltooiingen site breed op 8 augustus bij 6 starts, plus één sessie met 283 clicks en 1.901s die op het formulier strandde. Die twee samen wijzen naar een kapot of vastlopend veld, niet naar afhakende bezoekers.
- **Hoe:** Handmatig in de browser. Bekijk daarna de session recording van sessie `019fe1d4-ac21-70f8-9123-eff0e980eb76` in PostHog.
- **Verwachte impact:** Als hier een bug zit, is dit de enige actie in dit rapport die direct omzet raakt.
- **Escalatie:** 🟠 Oranje, mogelijk Wix Editor werk.

### 2. Verifieer of het direct verkeer echt is weggevallen of alleen anders gemeten

- **Wat:** Vergelijk de direct sessies van 4 en 8 augustus op browser, device en referring domain. Check of er tussen 5 en 6 augustus iets aan de site, het cookie consent of de PostHog snippet is gewijzigd.
- **Waarom:** Bounce rate van 37% naar 88,7% en sessieduur van 224s naar 50s in drie dagen, terwijl checkout pageviews van 77 naar 15 zakten. Dat laatste maakt een puur meetprobleem minder waarschijnlijk, dus dit kan echt omzetverlies zijn.
- **Hoe:** PostHog, breakdown op `$browser` en `$device_type` binnen het Direct kanaal. Daarnaast de deploy of publicatiegeschiedenis van de site nakijken.
- **Verwachte impact:** Bepaalt of dit een meetfout is (dan negeren) of een echt probleem (dan urgent).
- **Escalatie:** 🟡 Geel, jouw beoordeling nodig.

### 3. Zet scroll depth en CTA click events aan

- **Wat:** Voeg scroll depth events (25/50/75/100%) en een expliciet CTA click event toe op de SYBB register pagina's en op startyourballoonbusiness.com.
- **Waarom:** Vier van de zeven Landing Page Health KPI's zijn nu niet in te vullen. Zodra er weer budget loopt, kun je zonder deze events geen ad variant aan paginagedrag koppelen, en dat is precies waar dit rapport voor bedoeld is.
- **Hoe:** PostHog autocapture aanvullen met custom events, via de Wix Editor of de PostHog snippet.
- **Verwachte impact:** Maakt het rapport voor het eerst volledig invulbaar. Doe dit nu het rustig is, niet als het budget al loopt.
- **Escalatie:** 🟠 Oranje, Wix Editor werk.

**Vervolgens:** autoriseer Pipeboard via je claude.ai connector instellingen of `/mcp` in een interactieve sessie. Zonder dat blijft de helft van dit rapport leeg.

---

## Cross-referencing

De gebruikelijke kruisverbanden (Ad CTR versus LP bounce, CPC versus conversie, frequency versus bounce) zijn niet te maken: er is geen ad data en er is geen verkeer op de landing page. Wat wel opvalt:

**Nul bounces op de SYBB pagina's bij nul conversies.** Dat is de meest bruikbare observatie van vandaag. De 5 bezoekers waren allemaal betrokken, één van hen bijna veertig minuten. Het probleem zit niet in de aantrekkingskracht van SYBB en niet in de pagina zelf, maar in de stap van pagina naar formulier naar bevestiging. Dat is goed nieuws voor de positionering en slecht nieuws voor de techniek.

**Organische aanwas doet het werk dat ads zouden moeten doen.** Het SYBB verkeer op 8 augustus kwam via Organic Social, Organic Search en Referral. Bij nul spend leveren die 5 betrokken sessies op. Dat is een bruikbare bodem om vanaf te herstarten zodra Pipeboard weer werkt.
