# SYBB Daily Report, dinsdag 11 augustus 2026

> **Databronnen:** PostHog MCP (project STX EU, id 149694, timezone UTC). Meta Ads MCP (Pipeboard) was in deze sessie niet geautoriseerd, zie sectie 2.
> Geen Google MCPs gebruikt, niet naar de Google Sheet tracker geschreven, conform instructie.

---

## 1. Samenvatting

De SYBB landing page (startyourballoonbusiness.com) registreerde op 11 augustus **nul** events. Elfde stille dag op rij. Laatste activiteit op dat domein was 31 juli, één enkele pageview. Er draait geen betaald budget, dus er komt daar niemand.

Het SYBB verkeer dat er wél was liep via de event registratiepagina's op sempertexeurope.com, en dat was **één pageview van één bezoeker** op de Duitse pagina `start-your-balloon-business-professionell-8/register`. Tegen een schoongemaakt weekgemiddelde van ongeveer 5 pageviews per dag is dat de zwakste SYBB dag van de maand.

Belangrijke correctie op wat een goede dag leek: de 90 SYBB pageviews van 10 augustus waren voor 82 stuks één bezoeker uit België in één sessie. Het echte weekniveau ligt rond 5 pageviews per dag, niet rond 17. Reken 10 augustus dus niet mee als vraagsignaal.

Sitebreed is het beeld dubbel. De kwaliteit is uitstekend: bounce 22,9% tegen een weekgemiddelde van 55,5%, sessieduur 8m20s tegen 3m39s, en 48 shop confirmations tegen een weekgemiddelde van 23,7. Dat is de beste conversiedag van de periode. Maar de **sessies dalen voor de achtste dag op rij**, van 1.339 op 3 augustus naar 595 op 11 augustus, min 55,6% ononderbroken. Je verliest de bovenkant van de trechter en houdt de koopintentie over. De cijfers zien er daardoor gezonder uit dan je verkeer rechtvaardigt.

---

## 2. Meta Ads Performance

**Data niet beschikbaar.** De Pipeboard Meta Ads MCP is niet geautoriseerd en autoriseren kan hier niet, de sessie is non interactief. Zevende dag op rij zonder Meta data. Autoriseren gaat via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | n.b. | n.b. | n.b. |
| Impressions | n.b. | n.b. | n.b. |
| Clicks | n.b. | n.b. | n.b. |
| CTR | n.b. | n.b. | n.b. |
| CPC | n.b. | n.b. | n.b. |
| Frequency | n.b. | n.b. | n.b. |

### Wat PostHog wel bevestigt over betaald verkeer

**Nul betaald verkeer.** In de kanaalverdeling van 11 augustus bestaat er geen Paid Social kanaal. In de volledige UTM breakdown over 13 juli tot en met 11 augustus komt `utm_source=meta` geen enkele keer voor. De enige campagne met de naam `sybb` in die periode is `instagram / bio_link`, goed voor 3 events, laatste op 14 juli.

Kanaalverdeling 11 augustus (entry host sempertexeurope.com):

| Kanaal | Sessies | Bounce | Sessieduur |
|--------|---------|--------|-----------|
| Direct | 286 | 31,8% | 8m36s |
| Referral | 193 | 21,8% | 8m00s |
| Organic Search | 90 | 1,1% | 9m53s |
| AI | 12 | 0,0% | 4m32s |
| Organic Social | 8 | 12,5% | 1m07s |
| Email | 6 | 16,7% | 0m37s |
| **Paid Social** | **0** | n.v.t. | n.v.t. |

Alle UTM getagde sessies van 11 augustus, 17 in totaal op 628:

| Source | Medium | Campagne | Content | Sessies | Bounce |
|--------|--------|----------|---------|---------|--------|
| chatgpt.com | (geen) | (geen) | (geen) | 12 | 0,0% |
| Klaviyo | email | (geen) | (geen) | 2 | 50,0% |
| mailjet | email | inspiration_promo_202607 | mail1 | 2 | 0,0% |
| mailjet | email | workshop_tobi_promo_202608 | mail3 | 1 | 0,0% |

`chatgpt.com` is opnieuw de grootste getagde bron, met 0% bounce. De Klaviyo sessies missen nog steeds een `utm_campaign`, dus ze zijn niet toe te wijzen aan een mailing.

### Ad Variant Performance

| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| h11_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |
| h12_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |
| h13_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |
| h14_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |
| h15_b3_cta5 | 0 | n.b. | n.b. | n.b. | n.b. |

**Beste variant:** niet te bepalen, nul geregistreerde klikken op alle vijf de varianten.
**Slechtste variant:** idem.

---

## 3. Landing Page Health

### 3a. SYBB landing page (startyourballoonbusiness.com)

| Metric | 11 aug | 7d Gemiddelde | Target | Status |
|--------|--------|---------------|--------|--------|
| Pageviews | 0 | 0 | n.v.t. | ⚫ geen data |
| Bounce Rate | geen data | geen data | <55% | ⚫ |
| Avg Session Duration | geen data | geen data | >90s | ⚫ |
| Scroll 25 / 50 / 75 / 100% | geen data | geen data | >80 / 60 / 40 / 20% | ⚫ |
| CTA Click Rate | geen data | geen data | >4% | ⚫ |

Twee losse oorzaken, houd ze uit elkaar:

1. **Geen verkeer.** Het domein heeft sinds 31 juli geen enkel event meer gestuurd. Over de hele meetperiode staat het op 164 events en 69 personen, tussen 13 juni en 31 juli.
2. **Geen instrumentatie.** Ik heb de volledige event taxonomie van het project gecontroleerd. Er bestaat **geen** scroll depth event, **geen** CTA click event en **geen** `/booking` pagina. De `$pageview` properties bevatten geen scroll velden. De targets uit `CLAUDE.md` en de skill zijn op dit moment dus principieel niet meetbaar, ook niet als het verkeer morgen terugkomt.

### 3b. Sempertexeurope.com als proxy

Dit is **niet** de SYBB landing page. Het staat hier omdat de SYBB workshop nu via de event pagina's op dit domein verkoopt, en omdat het de enige plek is waar wel gemeten wordt.

| Metric | 11 aug | 7d Gemiddelde | Verschil | Trend |
|--------|--------|---------------|----------|-------|
| Sessies | 595 | 933 | -36,2% | ↓ |
| Bezoekers | 454 | 831 | -45,3% | ↓ |
| Pageviews | 5.527 | 4.744 | +16,5% | ↑ |
| Pageviews per sessie | 9,12 | 5,13 | +77,8% | ↑ |
| Bounce Rate | 22,9% | 55,5% | -58,7% | 🟢 |
| Avg Session Duration | 500s (8m20s) | 219s (3m39s) | +128,6% | 🟢 |
| Rageclicks | 217 | 114 | +90,5% | 🔴 |
| Shop confirmations | 48 | 23,7 | +102,5% | 🟢 |

> Cijfers uit de `sessions` tabel, entry host `www.sempertexeurope.com`. De Web Analytics view geeft licht andere waarden (513 sessies, 30,8% bounce, 9m39s) omdat daar de projectinstelling voor test accounts meedraait. De richting is in beide identiek.

---

## 4. Funnel Drop-off

### SYBB funnel, 11 augustus

```
SYBB pagina view (1)  →  formulier start (?)  →  registratie voltooid (?)
        100%                  niet meetbaar        niet meetbaar
```

Eén bezoeker, en geen manier om te zien wat die daarna deed. Er is **geen registratie voltooid event** in het project. De enige harde conversie die bestaat is `/shop/confirmation`, en dat is de webshop, niet de workshop inschrijving.

### Sitebrede event funnel, 11 augustus

| Stap | Volume |
|------|--------|
| Event overzicht en detailpagina's | 36 pageviews |
| `/register` pagina's | 43 pageviews in 15 sessies |
| Registratie voltooid | niet geïnstrumenteerd |

**Grootste lek:** onbekend, en dat is precies het probleem. Het lek zit tussen `/register` en de bevestiging, en daar staat geen meetpunt. Zolang dat zo is kun je geen enkele uitspraak doen over de conversie van je workshop funnel, ook niet als je Meta weer aanzet.

---

## 5. Rode Vlaggen 🚩

**1. Sessies dalen acht dagen op rij.** Van 1.339 (3 aug) naar 595 (11 aug), min 55,6% zonder één herstelmoment. Bezoekers dalen even hard mee, dus dit is geen meetfout in de sessieherkenning. Er komen echt minder mensen.

**2. Rageclicks op de winkelwagen.** 217 rageclicks op 11 augustus tegen een weekgemiddelde van 114. De concentratie zit in de shop, en 22 daarvan zitten verspreid over drie taalversies van de cart:

| Pagina | Rageclicks | Sessies |
|--------|-----------|---------|
| `/en_GB/shop/cart` | 9 | 4 |
| `/fr/shop/cart` | 7 | 2 |
| `/shop/cart` | 6 | 3 |
| `/fr/shop/category/ballons-a-modeler-260-3053` | 10 | 2 |
| `/shop/category/latex-onbedrukt-fashion-solid-white-005-3836` | 8 | 4 |

Rageclicks in de cart raken direct je omzet. Dit is geen SYBB probleem maar het is het duurste signaal in het rapport.

**3. SYBB landing page elf dagen stil.** Geen verkeer, geen budget, geen meetpunten.

**4. Meta data zeven dagen niet beschikbaar.** Je vliegt blind op de betaalde kant.

**5. Nul instrumentatie op de SYBB funnel.** Geen scroll, geen CTA click, geen registratie voltooid.

Niet getriggerd: CPC drempels, frequency en ad fatigue kunnen niet beoordeeld worden zonder Meta data. Bounce en scroll drempels zijn niet van toepassing, er is geen LP verkeer.

---

## 6. Top 3 Acties voor Vandaag

### 1. Zet een registratie voltooid event op de event funnel

- **Wat:** een custom event op de bevestigingsstap van `/event/*/register`, plus een CTA click event op de inschrijfknop van de event detailpagina.
- **Waarom:** sectie 4. Je hebt 43 register pageviews in 15 sessies op één dag en geen enkele manier om te zien hoeveel daarvan doorkomen. Dit blokkeert elke funnel uitspraak, nu en na een herstart.
- **Hoe:** handmatig in de Odoo of Wix template van de registratiepagina, custom event via de PostHog snippet.
- **Verwachte impact:** maakt de workshop funnel voor het eerst meetbaar. Zonder dit blijft elk volgend rapport een schatting.
- **Escalatie:** 🟠 Oranje, vereist toegang tot de pagina templates.

### 2. Onderzoek de sessiedaling, begin bij Direct

- **Wat:** achterhaal wat er rond 3 augustus veranderde. Direct is 286 van de 595 sessies, dus daar zit het volume en daar zit de daling.
- **Waarom:** acht dagen ononderbroken min 55,6%. Dit is de enige trend in het rapport die niet vanzelf herstelt, en hij ondermijnt alles wat je daarna aan de funnel doet.
- **Hoe:** check of er rond 3 augustus een mailing stopte, een campagne afliep, of een redirect of consent banner wijzigde. Vergelijk entry pagina's van 3 augustus met 11 augustus.
- **Verwachte impact:** herstel van de bovenkant van de trechter. Je huidige goede bounce en sessieduur zijn een mix effect, geen verbetering.
- **Escalatie:** 🟡 Geel.

### 3. Autoriseer Pipeboard

- **Wat:** autoriseer de Meta Ads connector via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.
- **Waarom:** zevende dag zonder data. Secties 2 en de hele cross reference tussen ad en pagina blijven leeg.
- **Hoe:** claude.ai connector instellingen.
- **Verwachte impact:** heropent spend, CPC, CTR, frequency en de per variant analyse.
- **Escalatie:** 🟢 Groen, alleen jouw handeling.

> **Bewust niet in de top 3:** de rageclicks op de cart. Het is het duurste signaal in het rapport, maar het valt buiten de SYBB scope. Pak het op in het ads of shop spoor, niet hier.

---

## 7. Cross-Referencing

De kern van dit rapport is het combineren van Meta en PostHog. Dat kan vandaag niet, want één van de twee bronnen ontbreekt en de andere heeft geen SYBB verkeer. Wat wel te zeggen valt:

- **Ad CTR vs LP Bounce:** niet te bepalen, nul klikken en nul LP sessies.
- **Frequency vs Bounce:** niet te bepalen.
- **Kwaliteit vs volume, sitebreed:** dit is de enige echte cross reference die overblijft. Bounce daalt van 55,5% naar 22,9% en sessieduur meer dan verdubbelt, terwijl sessies met 36% dalen. Die twee bewegen samen omdat je oppervlakkig verkeer verliest, niet omdat de site beter werd. Interpreteer de groene cijfers in sectie 3b dus als mix effect.
- **Eén sterk signaal:** Organic Search bouncet op 1,1% met bijna 10 minuten sessieduur, over 90 sessies. Dat is je gezondste kanaal en het kost geen budget.

---

## 8. Datakwaliteit

| Punt | Status |
|------|--------|
| Meta Ads MCP (Pipeboard) | ❌ niet geautoriseerd, 7e dag |
| PostHog MCP | ✅ werkt |
| SYBB landing page tracking | ⚠️ actief maar nul verkeer sinds 31 juli |
| Scroll depth events | ❌ bestaan niet in het project |
| CTA click events | ❌ bestaan niet in het project |
| `/booking` pagina | ❌ bestaat niet |
| Registratie voltooid event | ❌ bestaat niet |
| Klaviyo UTM tagging | ⚠️ `utm_campaign` ontbreekt |
| Session recordings | ✅ actief, geen opname met SYBB pagina op 11 aug |

---

*Rapport gegenereerd op 12 augustus 2026. Alleen Meta Ads MCP en PostHog MCP geraadpleegd. Geen Google MCPs, niet naar de Google Sheet tracker geschreven.*
