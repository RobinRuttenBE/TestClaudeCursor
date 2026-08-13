# SYBB Daily Report, woensdag 12 augustus 2026

> **Databronnen:** PostHog MCP (project STX EU, id 149694, timezone UTC). Meta Ads MCP (Pipeboard) was in deze sessie niet geautoriseerd, zie sectie 2.
> Geen Google MCPs gebruikt, niet naar de Google Sheet tracker geschreven, conform instructie.

---

## 1. Samenvatting

De SYBB landing page (startyourballoonbusiness.com) registreerde op 12 augustus **nul** events. Twaalfde stille dag op rij. Het domein heeft sinds 31 juli geen enkel event meer gestuurd. Er draait geen betaald budget, dus er komt daar niemand.

Het SYBB verkeer dat er wél was liep via de event registratiepagina's op sempertexeurope.com: **één pageview van één bezoeker** op de Duitse pagina `start-your-balloon-business-professionell-7/register`. Tegen een schoongemaakt weekgemiddelde van ongeveer 5 pageviews per dag is dat opnieuw de bodem, twee dagen op rij.

Sitebreed zakken de sessies voor de **negende dag op rij**, van 1.338 op 3 augustus naar 457 op 12 augustus, min 65,8% ononderbroken. Tegelijk zien de kwaliteitscijfers er spectaculair uit: bounce 11,4% tegen een weekgemiddelde van 52,7%, sessieduur 604s tegen 284s. **Geloof die cijfers niet.** Ze worden veroorzaakt door het self-referral probleem uit het rapport van 13 augustus, dat nog steeds niet is opgelost: 165 van de 457 sessies (36,1%) hebben je eigen domein als verwijzer. Opgebroken sessies kunnen per definitie niet bouncen, dus hoe erger de fragmentatie, hoe mooier je bounce rate. De cijfers verbeteren omdat de meting kapot is, niet omdat de site beter werkt.

---

## 2. Meta Ads Performance

**Data niet beschikbaar.** De Pipeboard Meta Ads MCP is niet geautoriseerd en autoriseren kan hier niet, de sessie is non interactief. Achtste dag op rij zonder Meta data. Autoriseren gaat via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | n.b. | n.b. | n.b. |
| Impressions | n.b. | n.b. | n.b. |
| Clicks | n.b. | n.b. | n.b. |
| CTR | n.b. | n.b. | n.b. |
| CPC | n.b. | n.b. | n.b. |
| Frequency | n.b. | n.b. | n.b. |

### Wat PostHog wel bevestigt over betaald verkeer

**Nul betaald verkeer.** In de kanaalverdeling van 12 augustus bestaat er geen Paid Social kanaal. Geen enkele sessie draagt `utm_source=meta` of een `sybb` campagne.

Kanaalverdeling 12 augustus (entry host www.sempertexeurope.com):

| Kanaal | Sessies | Bounce | Sessieduur |
|--------|---------|--------|-----------|
| Direct | 206 | 14,1% | 9m12s |
| Referral | 168 | 10,7% | 11m51s |
| Organic Search | 67 | 3,0% | 10m18s |
| AI | 10 | 20,0% | 2m11s |
| Organic Social | 5 | 20,0% | 0m49s |
| Email | 1 | 0,0% | 0m02s |
| **Paid Social** | **0** | n.v.t. | n.v.t. |

Alle UTM getagde sessies van 12 augustus, 12 in totaal op 457:

| Source | Medium | Campagne | Content | Sessies | Bounce |
|--------|--------|----------|---------|---------|--------|
| chatgpt.com | (geen) | (geen) | (geen) | 10 | 20,0% |
| Klaviyo | email | (geen) | (geen) | 1 | 0,0% |
| Pinterest | organic | (geen) | (geen) | 1 | 100,0% |

`chatgpt.com` is voor de derde dag op rij je grootste getagde bron. De Klaviyo sessie mist nog steeds een `utm_campaign`, dus die is niet toe te wijzen aan een mailing.

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

| Metric | 12 aug | 7d Gemiddelde | Target | Status |
|--------|--------|---------------|--------|--------|
| Pageviews | 0 | 0 | n.v.t. | ⚫ geen data |
| Bounce Rate | geen data | geen data | <55% | ⚫ |
| Avg Session Duration | geen data | geen data | >90s | ⚫ |
| Scroll 25 / 50 / 75 / 100% | geen data | geen data | >80 / 60 / 40 / 20% | ⚫ |
| CTA Click Rate | geen data | geen data | >4% | ⚫ |

Twee losse oorzaken, houd ze uit elkaar:

1. **Geen verkeer.** Laatste event op dit domein was 31 juli 2026, 21:12 UTC. Over de hele meetperiode staat het op 224 events en 91 personen.
2. **Geen instrumentatie.** Ik heb de event taxonomie en de volledige `$pageview` property lijst opnieuw gecontroleerd. Er bestaat **geen** scroll depth event of property, **geen** CTA click event en **geen** `/booking` pagina. De scroll en CTA targets uit `CLAUDE.md` en de skill zijn op dit moment principieel niet meetbaar, ook niet als het verkeer morgen terugkomt.

### 3b. Sempertexeurope.com als proxy

Dit is **niet** de SYBB landing page. Het staat hier omdat de SYBB workshop nu via de event pagina's op dit domein verkoopt, en omdat het de enige plek is waar wel gemeten wordt.

| Metric | 12 aug | 7d Gemiddelde | Verschil | Trend |
|--------|--------|---------------|----------|-------|
| Sessies | 457 | 846,0 | -46,0% | ↓ |
| Bezoekers | 324 | 740,7 | -56,3% | ↓ |
| Pageviews | 3.971 | 4.547,0 | -12,7% | ↓ |
| Pageviews per sessie | 8,69 | 5,37 | +61,7% | ↑ |
| Bounce Rate | 11,4% | 52,7% | -78,4% | ⚠️ artefact |
| Avg Session Duration | 604s (10m04s) | 284s (4m44s) | +112,4% | ⚠️ artefact |
| Rageclicks | 116 | 120,9 | -4,1% | → |
| Shop confirmations | 26 | 25,0 | +4,0% | → |

> Cijfers uit de `sessions` tabel, entry host `www.sempertexeurope.com`, 7d gemiddelde over 5 tot en met 11 augustus. Het ads rapport van 13 augustus noemde 340 sessies voor deze dag, dat is de Web Analytics view met de projectinstelling voor test accounts actief. De richting is in beide identiek.

**Waarom bounce en duur artefacten zijn:** zie sectie 5. Zolang je eigen domein 36,1% van je sessies aanlevert, meet je fragmentatie, geen gedrag.

### SYBB event pagina's op sempertexeurope.com

| Dag | Pageviews | Personen |
|-----|-----------|----------|
| 6 aug | 1 | 1 |
| 7 aug | 10 | 4 |
| 8 aug | 10 | 5 |
| 9 aug | 3 | 3 |
| 10 aug | 90 | 8 |
| 11 aug | 1 | 1 |
| **12 aug** | **1** | **1** |

Ruw 7d gemiddelde 16,7. Schoongemaakt, zonder de 82 pageviews van één Belgische bezoeker op 10 augustus, ongeveer **5,0 per dag**. Reken met 5, niet met 16,7.

---

## 4. Funnel Drop-off

### SYBB funnel, 12 augustus

```
SYBB pagina view (1)  →  formulier start (?)  →  registratie voltooid (?)
        100%                  niet meetbaar        niet meetbaar
```

Eén bezoeker op `/de/event/start-your-balloon-business-professionell-7/register`, en geen manier om te zien wat die daarna deed. Er is **geen registratie voltooid event** in het project. De enige harde conversie die bestaat is `/shop/confirmation`, en dat is de webshop, niet de workshop inschrijving.

**Grootste lek:** niet vast te stellen. Met één bezoeker en nul conversie events is er geen funnel om te lekken. Het echte lek zit bovenaan: er komt niemand.

---

## 5. Rode Vlaggen 🚩

1. **Self-referral blokkeert nog steeds alle analyse.** 165 van 457 sessies (36,1%) hebben `www.sempertexeurope.com` als entry referring domain. Ook `www.mollie.com` staat er nog in. Dit is punt 2 uit het rapport van 13 augustus en is niet opgelost. Gevolg: sessietelling opgeblazen, bounce rate kunstmatig laag (11,4%), en de oorspronkelijke bron van elke opgebroken sessie valt terug naar Direct.
2. **Bounce rate van 11,4% is geen goed nieuws.** Organic Search op 3,0% bounce is fysiek onwaarschijnlijk. Dit is het artefact, niet een prestatie. Neem geen enkele beslissing op basis van dit cijfer.
3. **Negende dag sessiedaling op rij.** 1.338 (3 aug) naar 457 (12 aug), min 65,8%, geen enkele dag onderbroken. Organic Search zakte in dezelfde periode van ongeveer 90 naar 67, dus de pixel ligt er niet uit. De daling is echt.
4. **Rageclick concentratie op de shop overzichtspagina.** 50 van de 116 rageclicks op 12 augustus komen van `/en_GB/shop`, van slechts 2 personen. Nog eens 10 op één rose gold folie categorie. Twee mensen die 60 keer woedend klikken op de Engelse shop wijst op iets dat niet reageert.
5. **Session replay dekt vrijwel niets.** 3 recordings op 457 sessies, en 2 daarvan hebben nul activiteit. Je kunt geen enkel gedragsvraagstuk met replay beantwoorden op dit volume.
6. **Nul SYBB conversie events.** Bij >50 bezoekers per dag op de site en actieve workshop pagina's is er geen enkele manier om een inschrijving te meten.

Niet getriggerd: CPC drempels, frequency en ad fatigue, allemaal omdat er geen Meta data en geen spend is.

---

## 6. Top 3 Acties voor Vandaag

### 1. Sluit interne domeinen uit als verwijzer in PostHog

- **Wat:** voeg `sempertexeurope.com`, `mollie.com` en de `odoo.com` domeinen toe aan de excluded referrers in je PostHog projectinstellingen.
- **Waarom:** 165 van 457 sessies (36,1%) komen van je eigen domein. Dit is de tweede dag dat deze actie bovenaan staat en de vierde dag dat het probleem meetbaar is.
- **Hoe:** PostHog, project 149694, Settings, Web analytics, excluded referrers. Handmatig, kost vijf minuten.
- **Verwachte impact:** sessietelling daalt zichtbaar (waarschijnlijk richting 300 per dag), bounce rate stijgt naar een realistisch niveau, en Direct krimpt ten gunste van de echte bronnen. Pas daarna is elk ander cijfer in dit rapport te vertrouwen.
- **Escalatie:** 🟡 Geel, Robin goedkeuring. Let op: je historische cijfers worden hierdoor niet herschreven, alleen nieuwe data.

### 2. Zet een registratie conversie event op de SYBB event pagina's

- **Wat:** instrumenteer een `sybb_registration_started` en `sybb_registration_completed` event op de `/event/start-your-balloon-business-*/register` pagina's.
- **Waarom:** je hebt vandaag één SYBB bezoeker gehad en kon niet zien of die zich inschreef. Zonder dit event is elke funnel in dit rapport een lege huls, en kun je straks geen Meta campagne beoordelen ook al staat Pipeboard morgen aan.
- **Hoe:** via de Odoo website editor of de PostHog autocapture action builder op de submit knop van het registratieformulier.
- **Verwachte impact:** je krijgt voor het eerst een meetbare SYBB conversie. Dit is de voorwaarde voor elk rendementsoordeel over de workshop.
- **Escalatie:** 🟠 Oranje, vereist een ingreep in de site.

### 3. Bekijk de twee rageclick sessies op /en_GB/shop

- **Wat:** open de replay of reproduceer handmatig wat er stuk is op de Engelse shop overzichtspagina en de rose gold 32 inch categorie.
- **Waarom:** 60 van de 116 rageclicks van gisteren komen van deze twee pagina's, van slechts 2 personen. Dat is geen spreiding, dat is één kapot element.
- **Hoe:** [PostHog Replay](https://eu.posthog.com/project/149694/replay), filter op pathname `/en_GB/shop`. Test daarna zelf in een incognito venster.
- **Verwachte impact:** klein in volume, maar het is de enige concrete, oplosbare UX fout die vandaag in de data zichtbaar is. De rest van dit rapport wacht op meetinfrastructuur.
- **Escalatie:** 🟢 Groen, gewoon uitzoeken.

---

## 7. Cross-referencing

De vijf standaard kruisverbanden uit de skill (Ad CTR versus LP Bounce, CTR versus Scroll, CPC versus Conversie, Variant versus LP gedrag, Frequency versus Bounce) zijn geen van alle te berekenen. Ze hebben allemaal Meta data aan de ene kant en LP instrumentatie aan de andere kant nodig, en beide ontbreken.

Wat de twee bronnen samen wél zeggen: PostHog bevestigt onafhankelijk dat er niets draait op Meta. Nul Paid Social sessies, nul `utm_source=meta`, nul klikken op de vijf ad varianten. Het ontbreken van Pipeboard verandert de conclusie voor 12 augustus dus niet. Zodra er weer budget loopt, verandert dat direct, en dan heb je actie 1 en 2 nodig om er iets van te kunnen zeggen.
