# Meta Ads Rapport, 9 augustus 2026

## Status databronnen

**Meta Ads data ontbreekt.** De Pipeboard connector is in deze sessie niet geautoriseerd, dus stappen 1 tot en met 4 van `/ads-report` konden niet draaien. Geen spend, impressions, CTR, CPC, CPM, conversies of ROAS. Dit is de **derde dag op rij** (7, 8 en 9 augustus).

Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Deze sessie is niet interactief, dus ik kan de OAuth flow hier niet starten.

Stap 6 (Google Sheet write) en alle Google MCPs zijn overgeslagen zoals gevraagd. PostHog is wel beschikbaar en levert de cijfers hieronder.

---

## Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| Geen data beschikbaar | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. | n.v.t. |

Underperformers en top performers kan ik niet bepalen zonder ad level data. De drempelwaarden (CPC boven €0,50, CTR onder 1%, frequency boven 3,5, CPM boven €15) blijven onbeoordeeld.

---

## Wat PostHog wel bevestigt

### Nul betaald verkeer, 39 dagen

Er is geen Paid Social kanaal in de kanaalverdeling over 30 dagen. Ik heb zes maanden UTM historie doorzocht.

| Bron | Laatste klik | Personen | Events |
|------|--------------|----------|--------|
| `meta / cpc / sybb` | 1 juli 2026, 16:42 | 1.316 | 4.479 |
| `instagram / organic / sybb` | 14 juli 2026 | 65 | 316 |
| `facebook / organic / sybb` | 10 juli 2026 | 25 | 147 |

De laatste betaalde klik is **39 dagen oud**. Ook het organische social verkeer met SYBB tagging is stilgevallen, ruim vier weken geleden.

### Site breed, 30 dagen

| Metric | Waarde | Target |
|--------|--------|--------|
| Bezoekers | 16.030 | meten |
| Pageviews | 101.897 | meten |
| Sessies | 19.364 | meten |
| Bounce rate | 56,7% | onder 55% |
| Gem. sessieduur | 4m35s | boven 90s |

Bounce rate loopt op: 54,5% op 6 augustus, 56,0% op 8 augustus, nu 56,7%. Derde meting op rij boven target.

### Laatste 7 dagen tegenover de 7 dagen daarvoor

| Metric | Nu | Vorige periode | Verschil |
|--------|-----|----------------|----------|
| Bezoekers | 6.269 | 6.254 | 0% |
| Pageviews | 33.298 | 34.817 | 4,4% lager |
| Sessies | 7.014 | 7.066 | 0,7% lager |
| Bounce rate | 55,3% | 60,0% | 4,7 punt beter |
| Sessieduur | 3m06s | 4m40s | **34% korter** |

Bounce rate verbetert op korte termijn, maar de sessieduur is met een derde ingezakt. Zelfde aantal bezoekers, fors minder tijd per sessie. Dat betekent dat mensen wel doorklikken naar een tweede pagina, maar sneller afhaken. Bounce rate alleen geeft hier een te rooskleurig beeld.

### Kanaalverdeling, 30 dagen

| Kanaal | Bezoekers | Bounce rate | Aandeel sessies |
|--------|-----------|-------------|-----------------|
| Direct | 11.550 | 63,9% | 68,9% |
| Referral | 3.189 | 63,4% | 19,0% |
| Organic Search | 1.433 | 4,9% | 8,5% |
| Email | 305 | 18,6% | 1,8% |
| AI | 183 | 16,2% | 1,1% |
| Organic Social | 94 | 18,8% | 0,6% |
| Organic Video | 8 | 12,5% | 0,05% |

Email blijft het sterkste kanaal op kwaliteit. De mailjet campagne `inspiration_promo_202607` haalt 15,2% bounce over 136 bezoekers, `workshop_tobi_promo_202608` haalt 28,3% over 43 bezoekers. Organic Search met 4,9% bounce is opvallend goed, dat verdient losse aandacht.

---

## Nieuw sinds gisteren

**De SYBB landing page ligt volledig stil.** Op startyourballoonbusiness.com is het laatste event van **31 juli 2026**, negen dagen geleden, en dat waren 2 events van 1 persoon. In de 45 dagen ervoor kwam de pagina nooit boven de 8 personen per dag uit, met 10 juli als uitschieter (33 events, 4 personen).

De pixel werkt, dat heb ik gisteren al vastgesteld. Wat ontbreekt is verkeer. Zonder ads komt er letterlijk niemand. De pagina is nu negen dagen op nul.

**UTM casing.** In de gegroepeerde query van vandaag vallen `meta/cpc/sybb` en `META/cpc/SYBB` samen op 1.316 personen. De splitsing die ik gisteren meldde staat er nog steeds in de ruwe data, dus dit blijft een fix voor de herstart.

---

## Samenvatting

**Totaal spend:** onbekend, waarschijnlijk €0,00 gezien 39 dagen zonder betaalde klik.

**Beste performer:** email, op kwaliteit. 15,2% en 18,6% bounce tegenover 56,7% site breed, over een klein maar consistent volume.

**Slechtste performer:** de SYBB funnel als geheel. Negen dagen nul bezoekers op de landing page, 39 dagen nul betaald verkeer.

**Aanbeveling:** de blokkade is niet analytisch, hij is operationeel. In volgorde:

1. **Autoriseer Pipeboard.** Drie dagen zonder ads data betekent dat elk rapport hierna weer half is. Dit blokkeert al het andere.
2. **Fix de UTM casing** naar lowercase in alle ad URLs voor je herstart. Anders splitst 14% van je betaalde verkeer weer in een aparte bucket.
3. **Zet conversie events op de SYBB pagina.** De pixel meet nu alleen pageviews en autocapture. Zonder CTA en booking events kun je de funnel niet diagnosticeren zodra het verkeer terugkomt.
4. **Verifieer conversiewaarde tracking.** De ROAS van 17,81x uit eerdere rapporten is vrijwel zeker een pixelfout.
5. **Tag de Klaviyo mails met `utm_campaign`.** 107 bezoekers zijn nu niet toewijsbaar.
6. **Onderzoek de sessieduur daling van 34%.** Dit is nieuw deze week en staat los van de ads situatie. Bounce rate verbergt het.
7. **Pas daarna herstarten volgens 70-20-10,** met budget naar de bewezen `meta/cpc/sybb` hooks uit de 1.316 personen historie.

Punt 2 tot en met 5 kun je nu doen, ze hebben Pipeboard niet nodig. Dan staat de meting klaar op het moment dat je weer budget aanzet.

---

## Google Sheet

Overgeslagen op verzoek. Rapport uitsluitend lokaal opgeslagen in `Output/Reports/Daily/2026-08-09_ads_report.md`.
