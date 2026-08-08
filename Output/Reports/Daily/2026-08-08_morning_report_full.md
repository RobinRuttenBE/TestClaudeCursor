# Morning Report — 2026-08-08

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 8 augustus 2026

**De Meta Ads data kon ik niet ophalen.** De Pipeboard connector is in deze sessie niet geautoriseerd, dus stappen 1 tot en met 4 konden niet draaien. Geen spend, CTR, CPC of ROAS. Tweede dag op rij. Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

### Wat PostHog wel bevestigt

**Nul betaald verkeer** in 30 dagen. Er is geen Paid Social kanaal. Ik heb zes maanden UTM historie doorzocht en de laatste betaalde klik dateert van **1 juli 2026, 38 dagen geleden.**

Site breed over 30 dagen: 15.379 bezoekers, 99.218 pageviews, bounce rate 56,0%, gemiddelde sessieduur 4m39s. Die bounce rate stond op 6 augustus nog op 54,5%, dus hij is net over je 55% target geschoven.

Email blijft het enige kanaal dat presteert: 15,2% en 22,5% bounce tegenover 56,0% site breed.

### Twee dingen die ik onderweg vond

**Je UTM casing splitst de attributie.** Er lopen twee varianten naast elkaar: `meta/cpc/sybb` met 1.141 personen en `META/cpc/SYBB` met 189. PostHog telt dat als twee bronnen. De uppercase variant is de recentste, dus de fout zit in de laatst gebouwde ads. Bij herstart zit 14% van je betaalde verkeer in een aparte bucket.

**Correctie op mijn rapport van 6 augustus:** ik schreef toen dat startyourballoonbusiness.com niet gemeten wordt. Dat klopt niet. De pixel staat er wel en stuurt data, 81 events van 32 personen, laatste hit 31 juli. Wat ontbreekt is verkeer, niet meting. Wel zie ik alleen pageviews en autocapture, geen expliciete CTA of booking events. Dat is wat er nog moet gebeuren voor je die 0,5% checkout conversie kunt diagnosticeren.

### Volgorde van handelen

1. Autoriseer Pipeboard, dit blokkeert al het andere
2. Fix UTM casing naar lowercase in alle ad URLs
3. Zet conversie events op de SYBB pagina, de pixel meet nu alleen pageviews
4. Verifieer conversiewaarde tracking, die ROAS van 17,81x is vrijwel zeker een pixelfout
5. Tag de Klaviyo mails met `utm_campaign`, 107 bezoekers zijn nu niet toewijsbaar
6. Pas daarna herstarten volgens 70-20-10, met budget naar de bewezen `meta/cpc/sybb` hooks

Rapport staat in `Output/Reports/Daily/2026-08-08_ads_report.md`, gecommit en gepusht.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Met nul spend levert een funnel diagnose nu weinig op. Zinvoller zodra er weer budget loopt.

---

Rapport staat in `Output/Reports/Daily/2026-08-07_sybb_report.md`, gecommit en gepusht.

## Wat er niet lukte

**Meta Ads data kon ik niet ophalen.** De Pipeboard connector is in deze sessie niet geautoriseerd. Derde dag op rij. Sectie 2 en de hele ad variant tabel zijn daardoor leeg. Autoriseren via je claude.ai connector instellingen of `/mcp` in een interactieve sessie.

Geen Google MCPs aangeroepen, niets naar de tracker Sheet geschreven.

## Wat PostHog wel liet zien

**Nul betaalde clicks in 30 dagen.** Ik heb alle UTM getagde traffic van 8 juli tot 8 augustus doorzocht. Geen enkele `cpc` of Meta bron. Dat maakt de ontbrekende Pipeboard data minder erg dan het lijkt: er is waarschijnlijk niets om te rapporteren.

**startyourballoonbusiness.com kreeg 0 pageviews op 7 augustus.** Laatste hit was 31 juli. Drie pageviews in twee weken tijd. Bounce, scroll en sessieduur zijn op nul verkeer niet te berekenen.

**De SYBB event pagina's op de main site hadden juist hun beste dag van de week:** 10 views van 4 personen, tegenover een weekgemiddelde van 2,4. Kleine getallen, maar het is de enige SYBB beweging die er is.

## Het signaal dat wel opviel

Site brede bounce rate sprong naar **71,2%** tegenover 50,3% weekgemiddelde. Uitgesplitst per kanaal zit het bijna volledig in Direct: 615 bezoekers, 72% van je sessies, bounce 80,9%. Organic Search bounct tegelijk op 1,4%.

Die combinatie is verdacht. Ik heb het als rode vlag opgenomen, maar met de expliciete waarschuwing dat dit eerst op bots gecontroleerd moet worden voor je er iets mee doet.

## Drie beperkingen die je moet weten

1. **Scroll en CTA events bestaan nog steeds niet** in dit PostHog project. Vier van de zeven rijen in de Landing Page Health tabel en de complete funnel in sectie 4 zijn daardoor structureel leeg, niet incidenteel. Dit stond ook al in het rapport van 8 augustus.

2. **De skill aanname klopt niet meer.** Die gaat uit van een landing page gevoed door Meta ads. Beide zijn op 7 augustus onwaar. Ik heb sectie 3 en 4 daarom op sempertexeurope.com gedraaid en dat expliciet gemarkeerd in een kanttekening onderaan.

3. **De targets uit de skill** (bounce <55%, CTA >4%) zijn geijkt op een landing page met betaald verkeer. Ze passen niet één op één op een webshop met 4.000 pageviews per dag. De 🔴 op bounce betekent "onderzoek dit", niet "de landing page faalt".

De cross-referencing tussen beide bronnen, wat de kern van dit rapport hoort te zijn, was deze run niet mogelijk. Geen ad data en geen ad verkeer om tegen elkaar te leggen.

---

## Auto-Optimize, 8 augustus 2026

**De run is niet uitgevoerd. Nul ads gepauzeerd, en dat is een blokkade, geen goedkeuring.**

De Pipeboard connector is opnieuw niet geautoriseerd, derde dag op rij. Zonder `actions.link_click`, `impressions` en `spend` op ad niveau zijn de kill-regels niet te evalueren. Lees dit dus niet als "alles presteert boven de drempelwaarden".

### Wat PostHog wel bevestigt, en dat verandert de prioriteit

**Er is geen betaald verkeer.** Over 5 tot 8 augustus bestaat het kanaal Paid Social niet in de data, en op UTM niveau staat er geen enkele `meta / cpc` regel.

| Kanaal | Bezoekers | Bounce rate |
|--------|-----------|-------------|
| Direct | 2.053 | 66,3% |
| Referral | 544 | 66,8% |
| Organic Search | 214 | 4,7% |
| Email | 50 | 25,0% |
| **Paid Social** | **0** | n.v.t. |

Er valt dus waarschijnlijk niets te pauzeren omdat er niets draait. De vraag is niet welke ad je stopt, maar wanneer je herstart.

Eén kanttekening die ik niet kan wegnemen zonder Meta data: als er ads liepen met kapotte UTM tags, komen die als Direct binnen. Direct staat op 71,1% met 66,3% bounce, wat hoog is. Sterk signaal, geen bewijs.

### Waar ik geen voorstellen op doe

Budget herverdeling, nieuwe variaties en audience aanpassingen heb ik overgeslagen. Elk concreet bedrag zou verzonnen zijn zonder ad data. Wat er wel toe doet:

1. Autoriseer Pipeboard, dit blokkeert alles
2. Bevestig of er campagnes actief zijn, PostHog zegt van niet sinds 1 juli
3. Fix de UTM casing vóór herstart, `META/cpc/SYBB` splitst nu 14% van je verkeer af
4. Kalibreer de 70-20-10 drempels voor link metrics, die TODO staat nog open in het command en classificeert nu te streng
5. Zet conversie events op de SYBB pagina, de pixel meet alleen pageviews

Geen Google MCPs aangeroepen, niets naar de Tracker Sheet geschreven. Rapport staat in `Output/Reports/Daily/2026-08-08_auto_optimize.md`, gecommit en gepusht.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
