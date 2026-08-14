## Meta Ads Rapport, 14 augustus 2026

**Pipeboard is niet geautoriseerd, zevende dag op rij.** Stap 1 tot en met 4 konden niet draaien. Geen spend, impressions, CTR, CPC, CPM of ROAS, dus de underperformer- en top-performer-secties zijn leeg. Autoriseren gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

### Er draait sowieso niets

Over 90 dagen: **Paid Social 0 bezoekers.** Paid Search 2, Paid Unknown 1. Geen `utm_source=meta`, geen `utm_campaign=sybb` in de data. Zelfs met werkende Pipeboard-toegang zou je vandaag een rapport over nul actieve campagnes krijgen.

De enige getagde campagnes die verkeer opleveren zijn e-mail: `inspiration_promo_202607` (140 bezoekers), Klaviyo (109), `workshop_tobi_promo_202608` (46).

Geen enkele pagina van `startyourballoonbusiness.com` staat in de top 25. Alle 25 posities zijn de hoofdsite.

### Ik nuanceer mijn conclusie van gisteren

Het rapport van 13 augustus noemde de daling van 73,2% "geen meetfout". Kijk naar de laatste 7 dagen versus de 7 daarvoor:

| Metric | Laatste 7d | Vorige 7d | Verschil |
|--------|-----------|-----------|----------|
| Sessies | 4.451 | 7.601 | -41,0% |
| **Pageviews** | **31.017** | **36.656** | **-15,0%** |
| Sessieduur | 5m27s | 3m51s | +42,0% |

Sessies min 41%, pageviews maar min 15%, duur plus 42%. Dat is niet wegvallend verkeer. Dat is minder sessie-fragmentatie: dezelfde mensen, bijna evenveel pagina's, minder losse sessies. **De echte daling in consumptie is ongeveer 15%, niet 73%.** Er is geen acuut lek. Er is een meetprobleem.

### Dat meetprobleem staat er nog steeds

Mijn advies van gisteren, punt 2, is niet uitgevoerd. `www.sempertexeurope.com` is nog altijd je op één na grootste verkeersbron: 665 bezoekers en 6.630 pageviews in een week, 17,1% van je verkeer. Daardoor is Direct kunstmatig 69,9%.

Zet je Meta aan zonder dit te fixen, dan komt een deel van je betaalde bezoekers terug als Direct en reken je de campagne af op een verzonnen cijfer.

### Volgorde

1. Autoriseer Pipeboard
2. **Sluit `sempertexeurope.com`, `mollie.com`, Odoo en shipping-portal uit als verwijzer in PostHog**, instelling van vijf minuten, blokkeert al het andere
3. Conversie-events op de SYBB pagina vóór nieuw budget
4. Herwaardeer de daling pas na stap 2
5. Alles van vóór 13 juli als niet bestaand behandelen
6. UTM lowercase, komma's in `utm_content` naar underscores
7. Organic Search harder inzetten: 1.714 bezoekers, 30.804 pageviews, 4,6% bounce, zonder budget

Punt 2 tot en met 7 hebben Pipeboard niet nodig.

Losse observatie: `/en_GB/latex-balloons/fashion-solid/blue---040-2` haalt 329 bezoekers en exact 329 pageviews, bounce 100,0%. Gratis verkeer dat volledig wegloopt.

Rapport staat in `Output/Reports/Daily/2026-08-14_ads_report.md`, gecommit en gepusht.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
