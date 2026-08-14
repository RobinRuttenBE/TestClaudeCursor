# Meta Ads Rapport, 14 augustus 2026

**Periode:** last 30 days (15 juli t/m 14 augustus 2026)
**Bronnen:** Meta Ads MCP (Pipeboard) en PostHog MCP. Geen Google MCPs, geen Sheet write.

---

## Status: geen Meta Ads data, zevende dag op rij

Pipeboard is niet geautoriseerd in deze sessie. Stap 1 tot en met 4 van `/ads-report` konden niet draaien:

| Stap | Wat | Status |
|------|-----|--------|
| 1 | Ad accounts ophalen | Geblokkeerd, geen auth |
| 2 | Actieve campagnes | Geblokkeerd, geen auth |
| 3 | Campagne insights | Geblokkeerd, geen auth |
| 4 | Ad-level insights | Geblokkeerd, geen auth |
| 5 | Underperformers markeren | Niet mogelijk zonder data |
| 6 | Google Sheet write | Overgeslagen op verzoek |

Geen spend, geen impressions, geen CTR, CPC, CPM of ROAS. Dus ook geen underperformer- en top-performer-secties. Die zijn vandaag leeg omdat de data ontbreekt, niet omdat er niets te melden valt.

**Oplossen:** autoriseer de Pipeboard connector via je claude.ai connector instellingen, of draai `/mcp` in een interactieve Claude Code sessie. Dit is de zevende dag dat dit rapport hierop strandt.

---

## Wat PostHog wel bevestigt: er draait niets

Ik heb de kanaalverdeling over 90 dagen opgehaald om te checken of er überhaupt betaald verkeer binnenkomt.

| Kanaal (90 dagen) | Bezoekers | Aandeel |
|-------------------|-----------|---------|
| Direct | 12.770 | 68,4% |
| Referral | 3.484 | 18,7% |
| Organic Search | 1.716 | 9,2% |
| Email | 320 | 1,7% |
| AI | 237 | 1,3% |
| Organic Social | 139 | 0,7% |
| Organic Video | 10 | 0,1% |
| **Paid Search** | **2** | **0,0%** |
| **Paid Unknown** | **1** | **0,0%** |
| **Paid Social** | **0** | **0,0%** |

Drie betaalde bezoekers in negentig dagen. **Paid Social bestaat niet in de data.** Er is geen enkele Meta-getagde sessie, geen `utm_source=meta`, geen `utm_campaign=sybb` in de UTM-verdeling.

De enige getagde campagnes die verkeer opleveren zijn e-mail:

| Campagne | Bezoekers | Pageviews |
|----------|-----------|-----------|
| `mailjet / email / inspiration_promo_202607` | 140 | 300 |
| `Klaviyo / email / (none)` | 109 | 177 |
| `mailjet / email / workshop_tobi_promo_202608` | 46 | 87 |

Conclusie: de Pipeboard-autorisatie is niet het enige probleem. Zelfs met werkende toegang zou je vandaag een rapport over nul actieve campagnes krijgen. Er staat niets aan.

---

## De SYBB landing page ligt er nog steeds uit

In de top 25 pagina's over 30 dagen staat **geen enkele pagina van `startyourballoonbusiness.com`**. Alle 25 posities zijn `www.sempertexeurope.com`. Dat sluit aan op de constatering van 13 augustus dat de landing page stilligt sinds 31 juli.

---

## Correctie op mijn eigen conclusie van gisteren

Het rapport van 13 augustus meldde een verkeersdaling van 73,2% en noemde die "geen meetfout". Die framing klopt niet helemaal. De cijfers over de laatste zeven dagen versus de zeven dagen daarvoor:

| Metric | Laatste 7d | Vorige 7d | Verschil |
|--------|-----------|-----------|----------|
| Bezoekers | 3.686 | 6.801 | -46,0% |
| Sessies | 4.451 | 7.601 | -41,0% |
| **Pageviews** | **31.017** | **36.656** | **-15,0%** |
| Sessieduur | 5m27s | 3m51s | +42,0% |
| Bounce rate | 55,5% | 52,6% | +2,9pp |

Kijk naar de derde rij. **Sessies dalen 41%, maar pageviews maar 15%, en de sessieduur stijgt 42%.** Dat is niet het patroon van wegvallend verkeer. Als er echt mensen wegblijven, dalen pageviews en sessies ongeveer even hard en blijft de duur gelijk.

Wat je hier ziet is minder sessie-fragmentatie: dezelfde mensen bekijken bijna evenveel pagina's, maar hun bezoek wordt in minder losse sessies geknipt. De eerdere sessietelling was opgeblazen. De echte daling in consumptie is ongeveer 15%, niet 73%.

Dat verandert de prioriteit. Er is geen acuut lek waar bezoekers verdwijnen. Er is een meetprobleem dat je cijfers al weken onbruikbaar maakt.

---

## Het meetprobleem staat er nog steeds

Mijn advies van gisteren, punt 2, is niet uitgevoerd. Over de laatste zeven dagen:

| Verwijzende domein | Bezoekers | Aandeel |
|--------------------|-----------|---------|
| `$direct` | 2.719 | 69,9% |
| **`www.sempertexeurope.com`** | **665** | **17,1%** |
| `www.google.com` | 387 | 10,0% |
| `rezolvbv-sh-sempertex.odoo.com` | 6 | 0,2% |
| `sempertexeurope.shipping-portal.com` | 3 | 0,1% |

Je eigen domein is nog altijd je op één na grootste verkeersbron, goed voor 665 bezoekers en 6.630 pageviews in een week. Zolang dit staat, wordt elke opgebroken sessie als nieuw bezoek geteld en verliest de oorspronkelijke bron zijn attributie naar Direct. Dat verklaart die 69,9% Direct.

Zet je Meta straks aan zonder dit te fixen, dan zie je een deel van je betaalde bezoekers terug als Direct en reken je de campagne af op een verzonnen cijfer.

---

## Losse observatie

`www.sempertexeurope.com/en_GB/latex-balloons/fashion-solid/blue---040-2` haalt 329 bezoekers en exact 329 pageviews, bounce rate 100,0%. Eén pageview per bezoeker, niemand klikt door. Dat ruikt naar een pagina die extern gelinkt wordt (of hoog in Google staat) maar geen enkele volgende stap biedt. 329 bezoekers per maand is klein maar het is gratis verkeer dat volledig wegloopt.

---

## Aanbeveling

De Hormozi 70-20-10 regel gaat over budget verdelen over bewezen winnaars, variaties en experimenten. Je hebt op dit moment nul bewezen winnaars in de data, dus die verdeling is niet in te vullen. Wat er wel toe doet, op volgorde:

1. **Autoriseer Pipeboard.** Zonder dit blijft dit rapport zeven dagen op rij hetzelfde.
2. **Sluit `sempertexeurope.com`, `mollie.com` en de Odoo- en shipping-portal-domeinen uit als verwijzer in PostHog.** Dit blokkeert alle andere analyse en is een instelling van vijf minuten.
3. **Zet conversie-events op de SYBB pagina live vóór je opnieuw budget uitgeeft.** Anders koop je verkeer dat je niet kunt beoordelen.
4. **Herwaardeer de verkeersdaling pas na stap 2.** De 73% uit eerdere rapporten is grotendeels sessie-artefact, de echte daling is ongeveer 15%.
5. **Behandel alle data van vóór 13 juli als niet bestaand.** De tracking op de hoofdsite ging toen pas live.
6. **UTM-hygiëne:** lowercase doorvoeren, komma's in `utm_content` vervangen door underscores. `Klaviyo` en `mailjet` staan nu met afwijkende casing in de data.
7. **Organic Search harder inzetten.** 1.714 bezoekers en 30.804 pageviews over 30 dagen met een bounce rate van 4,6%, zonder budget. Dat is je best presterende kanaal en het krijgt geen aandacht.

Punt 2 tot en met 7 hebben Pipeboard niet nodig. Die kun je vandaag doen.

---

## Google Sheet

Overgeslagen op verzoek. Rapport opgeslagen in `Output/Reports/Daily/2026-08-14_ads_report.md`.
