# Meta Ads Rapport, 13 augustus 2026

**Meta Ads data ontbreekt, zesde dag op rij.** Pipeboard is in deze sessie niet geautoriseerd, dus stap 1 tot en met 4 van `/ads-report` konden niet draaien. Er is geen campagne, ad set of ad niveau data. Autoriseren gaat via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd. Dit rapport staat lokaal.

## Overzicht per campagne

Niet beschikbaar. Geen spend, impressions, clicks, CTR, CPC, CPM, conversies of ROAS. De drempelwaarden uit stap 5 (CPC boven €0,50, CTR onder 1,0%, frequency boven 3,5, CPM boven €15,00) konden nergens op toegepast worden.

Wat PostHog wel bevestigt: **er draait niets.**

- Laatste betaalde klik op de site: **14 juli 2026, 13:01 UTC**, dertig dagen geleden. Gemeten over negentig dagen op `utm_source` in meta, facebook, instagram, fb, ig of `utm_medium` in cpc, paid, paidsocial, paid_social.
- Geen Paid Social in de kanaalverdeling over dertig dagen.
- SYBB landing page: 1 tot 7 pageviews per dag in juli, laatste event **31 juli**. Effectief stil.

## Site breed, laatste 30 dagen

| Metric | Waarde |
|---|---|
| Bezoekers | 17.423 |
| Pageviews | 120.566 |
| Sessies | 21.457 |
| Gem. sessieduur | 4m52s |
| Bounce rate | 55,6% |

Kanalen, gesorteerd op aandeel:

| Kanaal | Bezoekers | Pageviews | Aandeel | Bounce |
|---|---|---|---|---|
| Direct | 12.534 | 62.810 | 68,6% | 63,5% |
| Referral | 3.422 | 25.606 | 18,7% | 61,0% |
| Organic Search | 1.659 | 29.487 | 9,1% | 4,5% |
| Email | 317 | 1.163 | 1,7% | 18,5% |
| AI | 230 | 1.173 | 1,3% | 14,6% |
| Organic Social | 102 | 312 | 0,6% | 19,3% |
| Organic Video | 8 | 15 | 0,0% | 12,5% |

## Correctie op de rapporten van 11 en 12 augustus

**De "sessies dalen acht dagen op rij" conclusie trek ik in. De meting gaat niet ver genoeg terug om die uitspraak te dragen.**

Wekelijkse sessies, tien weken terug:

| Week vanaf | Sessies | Pageviews | PV per sessie |
|---|---|---|---|
| 10 aug (4 dagen) | 1.529 | 16.383 | 10,7 |
| 3 aug | 6.820 | 33.108 | 4,9 |
| 27 jul | 6.232 | 32.017 | 5,1 |
| 20 jul | 4.789 | 26.059 | 5,4 |
| 13 jul | 2.088 | 14.768 | 7,1 |
| 6 jul | 17 | 20 | 1,2 |
| 29 jun | 7 | 8 | 1,1 |
| 22 jun | 13 | 14 | 1,1 |
| 15 jun | 7 | 8 | 1,1 |
| 8 jun | 9 | 10 | 1,1 |
| 1 jun | 8 | 8 | 1,0 |

Vóór 13 juli meet PostHog 7 tot 17 sessies per week. Dat is geen verkeer, dat is testverkeer. **De tracking op de hoofdsite is rond 13 juli live gegaan en heeft zich daarna over de site uitgerold.** De stijging van 298 naar 974 sessies per dag tussen 13 juli en 3 augustus is grotendeels die uitrol, geen groei.

Daarmee vervalt de basis onder "iets is kapot gegaan rond 3 augustus". Er is geen periode van vóór 13 juli om 3 augustus mee te vergelijken. De normale volumes van deze site zijn simpelweg onbekend.

## Wat er wél daalt, en wat niet

Sessies per dag sinds de piek:

| Dag | Sessies | Pageviews | Bezoekers |
|---|---|---|---|
| 13 aug (deels) | 46 | 224 | 48 |
| 12 aug | 340 | 4.103 | 292 |
| 11 aug | 513 | 5.652 | 460 |
| 10 aug | 630 | 6.404 | 562 |
| 9 aug | 712 | 2.844 | 700 |
| 8 aug | 826 | 2.874 | 772 |
| 7 aug | 892 | 4.157 | 864 |
| 6 aug | 963 | 5.135 | 909 |
| 5 aug | 1.021 | 6.079 | 964 |
| 4 aug | 1.136 | 6.464 | 1.066 |
| 3 aug | 1.270 | 5.555 | 1.218 |

Van 1.270 naar 340, min 73,2%. Week op week, hele dagen vergeleken: 974 naar 494 sessies per dag, min 49,3%.

**Dit is geen tracking uitval.** Organic Search via Google blijft in dezelfde periode vlak: 72, 67, 68, 76, 66, 52, 51, 92, 77, 57 sessies per dag, zonder trend. Als de pixel eruit lag, was Google mee gedaald. De meting werkt.

De daling zit volledig in Direct en Referral:

| Referrer | Sessies laatste 4d | 4d daarvoor |
|---|---|---|
| (direct) | 1.363 | 2.609 |
| www.sempertexeurope.com | 1.124 | 1.593 |
| www.google.com | 262 | 250 |
| www.mollie.com | 59 | 47 |
| www.bing.com | 17 | 13 |
| rezolvbv-sh-sempertex.odoo.com | 20 | 11 |
| chatgpt.com | 15 | 3 |

## Het echte probleem zit in de meting zelf

**Je op één na grootste verkeersbron is je eigen domein.** `www.sempertexeurope.com` levert 1.124 sessies in vier dagen, ruim een kwart van je totaal. Een site kan zichzelf niet doorverwijzen. Dit betekent dat sessies opbreken tijdens de bezoek: iemand navigeert intern of komt terug van Mollie, en PostHog telt dat als een nieuwe sessie met jouw eigen site als referrer.

Dat verklaart drie dingen tegelijk:

1. **Je sessietelling is opgeblazen.** Onbekend hoeveel, maar de zelfverwijzing plus Mollie is minstens een kwart.
2. **Die 4,5% bounce rate op Organic Search is geen prestatie, het is een artefact.** Een opgebroken sessie heeft per definitie een vorige pagina en bouncet dus nooit. Geen enkel echt kanaal bouncet op 4,5%.
3. **Attributie is stuk.** Elke sessie die opbreekt verliest zijn oorspronkelijke bron en belandt in Direct of in de zelfverwijzing. Dat is precies waarom Direct 68,6% van je verkeer lijkt te zijn.

Zolang dit niet gefixt is kun je geen enkele campagne eerlijk beoordelen. Je zou Meta straks afrekenen op cijfers die het systeem zelf verzint.

## Volgorde van handelen

1. **Autoriseer Pipeboard.** Blokkeert alles op ad niveau, zesde dag.
2. **Fix de zelfverwijzing.** Zet `www.sempertexeurope.com`, `sempertexeurope.com`, `mollie.com` en de Odoo domeinen op de lijst met uitgesloten verwijzingen in PostHog, en check de cross domain instelling. Dit is de blokkade voor alle andere analyse.
3. **Herwaardeer daarna pas de verkeersdaling.** Met correcte sessies kan het beeld flink verschuiven.
4. **Behandel alles van vóór 13 juli als niet bestaand.** Bouw je basislijn vanaf augustus op, met schone meting.
5. **Zet conversie events op de SYBB pagina** vóór je herstart. Nu meet je daar niets.
6. **Fix UTM casing naar lowercase**, komma's in `utm_content` naar underscores.
7. **Tag de Klaviyo mails met `utm_campaign`.** Email is 317 bezoekers en bouncet op 18,5%, dat is je beste betaalbare kanaal na organic.
8. **Zet Organic Search harder in.** 1.659 bezoekers, 29.487 pageviews, kost geen budget.
9. **Pas daarna herstarten volgens 70-20-10.**

Punt 2 tot en met 8 hebben Pipeboard niet nodig.

## Google Sheet

Overgeslagen op verzoek. Rapport staat in `Output/Reports/Daily/2026-08-13_ads_report.md`.
