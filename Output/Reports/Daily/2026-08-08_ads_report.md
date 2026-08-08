# Meta Ads Rapport, 8 augustus 2026

## Status: Meta Ads data niet opgehaald

De Pipeboard connector is in deze sessie niet geautoriseerd. Stap 1 tot en met 4 van `/ads-report` konden daardoor niet draaien. Er is geen live spend, impressions, CTR, CPC, CPM, conversie of ROAS beschikbaar.

Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Dit is dezelfde blokkade als op 6 augustus, nu twee dagen op rij.

Stap 6 (Google Sheet write) en alle Google MCPs zijn overgeslagen zoals gevraagd. Rapport uitsluitend lokaal opgeslagen.

---

## Wat PostHog wel laat zien

### Site breed, laatste 30 dagen

| Metric | Waarde | Target | Oordeel |
|--------|--------|--------|---------|
| Bezoekers | 15.379 | n.v.t. | |
| Pageviews | 99.218 | n.v.t. | |
| Sessies | 18.588 | n.v.t. | |
| Bounce rate | 56,0% | <55% | Net onder target |
| Gem. sessieduur | 4m39s | >90s | Ruim boven target |

Bounce rate is 56,0% tegenover 54,5% bij de meting van 6 augustus. Anderhalf procentpunt slechter in twee dagen, en daarmee net over de 55% grens. Klein signaal, nog geen probleem, maar het gaat de verkeerde kant op.

### Kanalen, laatste 30 dagen

| Kanaal | Bezoekers | Pageviews | Bounce rate | Aandeel |
|--------|-----------|-----------|-------------|---------|
| Direct | 11.040 | 52.183 | 62,9% | 68,6% |
| Referral | 3.072 | 20.809 | 63,8% | 19,1% |
| Organic Search | 1.394 | 23.898 | 4,9% | 8,7% |
| Email | 305 | 1.045 | 18,4% | 1,9% |
| AI | 179 | 989 | 16,8% | 1,1% |
| Organic Social | 93 | 282 | 19,0% | 0,6% |
| Organic Video | 7 | 12 | 14,3% | 0,0% |

**Paid Social ontbreekt volledig.** Nul betaald verkeer in 30 dagen. Dit bevestigt onafhankelijk dat alle campagnes gepauzeerd staan.

### Wanneer stopte het betaalde verkeer precies

Zes maanden UTM historie doorzocht op betaalde parameters:

| utm_source | utm_medium | utm_campaign | Events | Personen | Laatste hit |
|------------|------------|--------------|--------|----------|-------------|
| meta | cpc | sybb | 3.867 | 1.141 | **3 juni 2026** |
| META | cpc | SYBB | 612 | 189 | **1 juli 2026** |
| instagram | organic | sybb | 316 | 65 | 14 juli 2026 |
| facebook | organic | sybb | 147 | 25 | 10 juli 2026 |

Laatste betaalde klik: **1 juli 2026, 38 dagen geleden.**

---

## Twee bevindingen die aandacht vragen

### 1. UTM casing splitst je attributie in tweeën

Er lopen twee varianten van dezelfde campagne naast elkaar: `meta/cpc/sybb` (1.141 personen) en `META/cpc/SYBB` (189 personen). PostHog behandelt dit als twee losse bronnen.

De tracking standard in CLAUDE.md schrijft lowercase voor. De uppercase variant is de meest recente, dus de fout zit in de laatst gebouwde ads. Bij herstart betekent dit 14% van je betaalde verkeer in een aparte bucket, wat elke CPC en conversie vergelijking scheeftrekt.

**Actie:** controleer alle ad URLs op lowercase UTM parameters vóór je budget aanzet.

### 2. Correctie op het rapport van 6 augustus: de SYBB pixel staat er wel

Op 6 augustus concludeerde ik dat startyourballoonbusiness.com niet gemeten wordt. Dat klopt niet. De host stuurt wel degelijk data:

- 81 events, 32 unieke personen in 30 dagen
- `$pageview`, `$web_vitals`, `$pageleave` en `$autocapture` vuren allemaal
- Laatste event: **31 juli 2026**

De pixel werkt. Wat ontbreekt is verkeer. Vanaf 1 juli, toen de ads stopten, zakte de pagina naar 1 tot 6 pageviews per dag, en sinds 31 juli komt er niets meer binnen. Dat is geen meetprobleem maar een distributieprobleem.

Dit verandert de prioriteitsvolgorde: pixel plaatsen is niet meer nodig. Wat je wel moet checken vóór herstart is of de conversie events op die pagina goed staan, want in de 30 dagen data zie ik alleen pageviews en autocapture, geen expliciete CTA of booking events.

---

## Email is het enige kanaal dat presteert

| Campagne | Bezoekers | Bounce rate |
|----------|-----------|-------------|
| `mailjet / email / inspiration_promo_202607` | 136 | 15,2% |
| `Klaviyo / email / (none)` | 107 | 22,5% |
| `mailjet / email / workshop_tobi_promo_202608` | 43 | 26,7% |

Tegenover 56,0% site breed is dat drie keer zo betrokken. Bij 305 bezoekers is het volume klein, maar de kwaliteit is de hoogste van alle kanalen.

De Klaviyo mails missen nog steeds `utm_campaign`. 107 bezoekers zijn daardoor niet toe te wijzen aan een specifieke mail.

---

## Wat te doen, in volgorde

1. **Autoriseer Pipeboard.** Zonder dit blijft elk ads rapport half werk. Twee dagen op rij geen spend data.
2. **Fix UTM casing** in alle ad URLs naar lowercase, vóór herstart.
3. **Zet conversie events op de SYBB pagina.** De pixel meet nu alleen pageviews. Zonder CTA en booking events kun je de 0,5% checkout conversie uit het rapport van 4 augustus niet diagnosticeren.
4. **Verifieer de conversiewaarde tracking** op sempertexeurope.com. De ROAS van 17,81x uit eerdere metingen is vrijwel zeker een pixelfout.
5. **Tag Klaviyo mails** met `utm_campaign` volgens de tracking standard.
6. **Pas daarna herstarten** volgens 70-20-10: budget naar de bewezen `meta/cpc/sybb` hooks die 1.141 personen brachten, 20% naar variaties daarop, 10% experimenteel.

De bounce rate beweging van 54,5% naar 56,0% is het bijhouden waard, maar met nul spend is er nu weinig te optimaliseren. De echte blokkade is de connector.

---

## Google Sheet

Overgeslagen op verzoek. Rapport uitsluitend opgeslagen in `Output/Reports/Daily/2026-08-08_ads_report.md`.
