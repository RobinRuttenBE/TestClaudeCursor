# Meta Ads Rapport, 12 augustus 2026

## Status databronnen

**Meta Ads data ontbreekt, vijfde dag op rij.** De Pipeboard connector is in deze sessie niet geautoriseerd. Stappen 1 tot en met 4 van het command konden niet draaien. Geen spend, impressions, CTR, CPC, CPM, conversies of ROAS beschikbaar.

Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Ik kan dit zelf niet starten, deze sessie is niet interactief.

Stap 6 (Google Sheet write) en alle Google MCPs zijn overgeslagen zoals gevraagd. PostHog heeft wel gewerkt.

## Overzicht per campagne

Niet beschikbaar. Zie hierboven.

## Underperformers

Niet beoordeelbaar zonder Meta data. De drempels (CPC boven € 0,50, CTR onder 1%, frequency boven 3,5, CPM boven € 15,00) blijven ongetoetst.

---

## Wat PostHog wel laat zien

### Betaald verkeer staat 42 dagen stil

Laatste klik met `meta / cpc / sybb`: **1 juli 2026, 16:42**. Sindsdien niets.

| UTM combinatie | Pageviews | Laatst gezien |
|----------------|-----------|---------------|
| instagram / organic / sybb | 71 | 14 juli 2026 |
| facebook / organic / sybb | 29 | 10 juli 2026 |
| meta / cpc / sybb | 727 | 1 juli 2026 |

In de 30 daagse kanaalverdeling komt Paid Social niet voor. Dat bevestigt het: er loopt niets.

### SYBB landing page ligt 12 dagen stil

Laatste event op `www.startyourballoonbusiness.com`: **31 juli 2026, 21:12**. Over de laatste 120 dagen 1.014 pageviews van 754 bezoekers. Nul activiteit sinds 31 juli.

### Site breed, 30 dagen

| Metric | Waarde |
|--------|--------|
| Bezoekers | 17.251 |
| Pageviews | 116.500 |
| Sessies | 21.099 |
| Gem. sessieduur | 4m43s |
| Bounce rate | 56,2% |

De periode-vergelijking die PostHog erbij geeft is onbruikbaar (de vorige periode heeft 47 bezoekers, tracking liep toen nog niet). Negeer die percentages.

### Kanaalverdeling, 30 dagen

| Kanaal | Bezoekers | Aandeel | Bounce |
|--------|-----------|---------|--------|
| Direct | 12.438 | 68,8% | 64,0% |
| Referral | 3.387 | 18,7% | 61,7% |
| Organic Search | 1.609 | 8,9% | 4,6% |
| Email | 317 | 1,8% | 18,5% |
| AI | 218 | 1,2% | 14,1% |
| Organic Social | 99 | 0,5% | 18,9% |
| Organic Video | 8 | 0,04% | 12,5% |

Organic Search bouncet op 4,6%. Dat is uitzonderlijk goed en het beste kanaal dat je hebt. AI verkeer (voornamelijk ChatGPT, 214 bezoekers) bouncet op 14,1% en groeit als stille vijfde bron.

---

## Twee correcties op het rapport van gisteren

### 1. De crawler conclusie houdt geen stand

Gisteren stelde ik dat de 2.579 diepe instappen zonder referrer vrijwel zeker crawlers waren. Dat klopt niet. De bezoekers met de hoogste pageview aantallen zijn echte browsers uit echte EU landen, met meerdere sessies over meerdere dagen:

| Pageviews | Sessies | Browser | Land |
|-----------|---------|---------|------|
| 321 | 2 | Microsoft Edge | BE |
| 283 | 3 | Samsung Internet | DE |
| 173 | 2 | Firefox | DE |
| 173 | 2 | Chrome | DE |
| 167 | 4 | Chrome | BE |

Dit is B2B catalogusgedrag, geen bot. Een groothandel die 300 productpagina's doorloopt voor een bestelling ziet er precies zo uit. **Zet dus geen bot filtering aan, dat advies van gisteren trek ik in.** Je zou je beste klanten uit de data filteren.

### 2. De bounce piek is voorbij

De piek van 6 tot 9 augustus is weggetrokken. Sessiekwaliteit is nu het hoogst van de afgelopen 14 dagen.

| Dag | Sessies | PV per sessie | Duur | Bounce |
|-----|---------|---------------|------|--------|
| 11 aug | 595 | 9,1 | 8m20s | 28,1% |
| 10 aug | 655 | 9,3 | 6m33s | 42,4% |
| 9 aug | 739 | 3,8 | 2m00s | 76,8% |
| 8 aug | 849 | 3,3 | 2m28s | 73,6% |
| 7 aug | 941 | 4,3 | 2m41s | 71,2% |
| 6 aug | 1.037 | 4,6 | 3m16s | 69,1% |
| 5 aug | 1.106 | 5,3 | 5m03s | 38,5% |

---

## Het echte probleem van vandaag

**Sessies dalen acht dagen op rij, en de daling is echt.**

Van 1.338 sessies op 3 augustus naar 595 op 11 augustus. Dat is **min 55,5% in acht dagen**, ononderbroken.

Ik heb gecontroleerd of dit een meetfout kon zijn, want pageviews bleven wel op peil (6.138 op 10 augustus). Dat patroon past bij een kapotte bezoekersherkenning. Maar de sessietelling en het aantal distinct ids dalen allebei even hard mee, dus de identificatie werkt gewoon. Er komen echt minder mensen.

Wat er tegelijk gebeurt: wie er wél komt, gaat veel dieper. Van 4,1 naar 9,3 pageviews per sessie, van 2m19s naar 8m20s. Je verliest de bovenkant van de trechter en houdt de koopintentie over. Op korte termijn ziet je conversie er daardoor beter uit dan de gezondheid van je verkeer rechtvaardigt.

Met nul advertentiebudget al 42 dagen is dat geen verrassing. De vraag is of er daarnaast nog iets stuk is.

---

## Top performers

Beperkt tot organisch verkeer, want er is geen betaald verkeer.

- **Beste bounce rate**: Organic Search, 4,6% over 1.609 bezoekers
- **Beste email campagne**: `mailjet / email / inspiration_promo_202607`, 140 bezoekers
- **Sterkste groeier**: AI verkeer (ChatGPT), 218 bezoekers op 14,1% bounce

## Samenvatting

- **Totaal spend**: onbekend, Meta data niet beschikbaar
- **Betaald verkeer**: nul, al 42 dagen
- **Grootste risico**: sessies min 55,5% in acht dagen, oorzaak nog niet vastgesteld
- **Grootste kans**: Organic Search bouncet op 4,6% en is onderbenut

## Volgorde van handelen

1. **Autoriseer Pipeboard.** Dit blokkeert het hele rapport, vijfde dag.
2. **Onderzoek de sessiedaling.** Begin bij Direct verkeer, daar zit 69% van je volume. Check of er iets veranderd is aan de site, de navigatie, of een redirect rond 3 augustus.
3. **Zet géén bot filtering aan.** Advies van gisteren ingetrokken, zie correctie hierboven.
4. **Zet conversie events op de SYBB pagina** voordat je campagnes herstart, anders meet je straks weer niets.
5. **Fix UTM casing naar lowercase** en vervang komma's in `utm_content` door underscores.
6. **Tag de Klaviyo mails met `utm_campaign`.** 109 bezoekers zijn nu niet toewijsbaar.
7. **Zet Organic Search harder in.** Beste kanaal dat je hebt en het kost geen advertentiebudget.
8. **Pas daarna campagnes herstarten**, volgens 70-20-10 op de bewezen SYBB hooks.

Punt 2 tot en met 7 hebben Pipeboard niet nodig.

---

*Data 12 augustus is gedeeltelijk, tot 06:01 UTC. Bron: PostHog project STX EU (149694). Meta Ads: niet beschikbaar.*
