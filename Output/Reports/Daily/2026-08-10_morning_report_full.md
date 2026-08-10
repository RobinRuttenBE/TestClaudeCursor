# Morning Report — 2026-08-10

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 10 augustus 2026

**De Meta Ads data kon ik opnieuw niet ophalen.** De Pipeboard connector is in deze sessie niet geautoriseerd, dus stappen 1 tot en met 4 konden niet draaien. Geen spend, CTR, CPC of ROAS. Vierde dag op rij. Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

### Wat PostHog wel bevestigt

**Nul betaald verkeer, 40 dagen.** Laatste `META/cpc/SYBB` klik: 1 juli 2026, 16:42. Geen Paid Social kanaal in de 30-daagse kanaalverdeling. De SYBB landing page ligt tien dagen volledig stil, laatste event 31 juli.

Site breed over 30 dagen: 16.692 bezoekers, 105.156 pageviews, 20.117 sessies, sessieduur 4m30s, bounce rate 57,5%.

### De bounce rate stijging is een verkeersmix, geen site probleem

Dit corrigeert het beeld van gisteren. De sprong vanaf 6 augustus (34,8% naar 90%) zit volledig bij Direct verkeer. Referral en Organic Search blijven vlak.

Binnen Direct is de oorzaak de instappagina:

| Periode | Type instap | Sessies | Bounce |
|---------|-------------|---------|--------|
| Vóór 6 aug | Homepage | 1.810 | 3,3% |
| Vóór 6 aug | Diepe pagina | 1.349 | 86,7% |
| Ná 6 aug | Homepage | 668 | 10,0% |
| Ná 6 aug | Diepe pagina | 2.579 | 89,8% |

Diepe pagina's bouncen in beide periodes rond 87 tot 90%. Er is dus niets slechter geworden aan de site. De mix kantelde van 57% homepage naar 21% homepage, en het gemiddelde volgde. Die 2.579 diepe instappen zonder referrer zijn vrijwel zeker crawlers, zet bot filtering aan. De echte zorg is de andere kant: menselijke homepage instappen zakten met 63%.

### Volgorde van handelen

1. Autoriseer Pipeboard, dit blokkeert alles
2. Zet bot filtering aan in PostHog, je bounce en duur cijfers zijn nu vervuild
3. Fix UTM casing naar lowercase, en vervang de komma's in `utm_content` door underscores
4. Zet conversie events op de SYBB pagina
5. Verifieer conversiewaarde tracking, die ROAS van 17,81x is vrijwel zeker een pixelfout
6. Tag de Klaviyo mails met `utm_campaign`, 109 bezoekers zijn niet toewijsbaar
7. Onderzoek de daling in homepage instappen
8. Pas daarna herstarten volgens 70-20-10

Punt 2 tot en met 7 hebben Pipeboard niet nodig.

Rapport staat in `Output/Reports/Daily/2026-08-10_ads_report.md`, gecommit en gepusht.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Met nul spend en nul bezoekers op de landing page levert een funnel diagnose nu niets op.

---

Rapport staat in `Output/Reports/Daily/2026-08-09_sybb_report.md`, gecommit en gepusht.

## Wat ik wel en niet kon ophalen

**Meta Ads: niet gelukt.** De Pipeboard connector is niet geautoriseerd en deze sessie is non-interactief, dus ik kan de OAuth-flow niet draaien. Vijfde dag op rij. Autoriseren kan via je claude.ai connector-instellingen of `/mcp` in een interactieve sessie. Sectie 2 is daardoor leeg.

**PostHog: volledig gelukt.** Project STX EU (id 149694). Geen Google MCPs aangeroepen, niets naar de Google Sheet geschreven.

## Kernpunten

**De zorg van gisteren was vals alarm.** De nul registratie-voltooiingen van 8 augustus waren ruis bij lage aantallen. Op 9 augustus: 7 starts, 2 voltooiingen, 29%. Hoogste ratio van de week.

**Maar er is een echt patroon in het formulier.** Eén sessie genereerde 831 clicks in 6 minuten en 21 seconden op `/registratie`, met 8 rageclicks en 804 clicks zonder herkenbare elementtekst. Dat is ruim twee clicks per seconde. De dag ervoor deed een Franse sessie 283 clicks op hetzelfde formulier. Beide rondden uiteindelijk af, maar dit is precies het gedrag dat minder gemotiveerde bezoekers laat afhaken. Van de 7 starts haalden er 5 het einde niet.

**SYBB landing page: negende stille dag.** Nul events sinds 31 juli. Op de register-pagina's op de hoofdsite: 3 sessies, samen 1 klik, geen enkele door naar het formulier. Twee dagen op rij is die stap het enige echte lek in de SYBB funnel.

**Bounce rate 73,5% is nog steeds verkeersmix, geen sitefout.** 495 van de 560 directe sessies waren diepe instappen zonder referrer met 94,9% bounce en 33s duur. Vrijwel zeker crawlers. De echte zorg is de andere kant: menselijke homepage-instappen zakten van 435 (4 aug) naar 65 (9 aug).

Twee kanttekeningen die ik in het rapport heb gezet: 9 augustus was een zondag, dus een deel van de volumedaling is normaal weekendpatroon, en de crawler-verklaring blijft een hypothese tot bot filtering aan staat.

## Top 3 acties

1. **Bot filtering aanzetten in PostHog** (🟢 groen, tien minuten). Zonder dit blijft dit rapport dagelijks een rood cijfer melden dat niets over de site zegt.
2. **Registratieformulier zelf testen** (🟠 oranje). Zoek het element dat clicks slikt zonder reactie. Recording `019fe75f-dd2b-7667-86f5-c06ab87847f0` staat klaar. Dit is de enige actie die direct omzet raakt.
3. **Scroll depth en CTA click events aanzetten** (🟠 oranje). Vier van de zeven KPI's uit de skill zijn nu structureel niet meetbaar.

---

Het command kon niet draaien. De kern ervan hangt volledig op de Meta Ads MCP, en die is dicht.

**Wat er aan de hand is**

De Pipeboard connector is in deze sessie niet geautoriseerd. Vierde dag op rij, hetzelfde als in het ads rapport van vanochtend. Zonder ad-level insights zijn er geen impressions, link clicks of spend, dus:

- De kill-regels zijn niet geëvalueerd, niet "gehaald". Er zijn nul ads gepauzeerd omdat er niets te meten viel.
- 70-20-10 classificatie en alle budget-, variatie- en audience-voorstellen vervallen, die zijn puur afgeleid van performance data.

Autoriseren kan alleen jij, via je claude.ai connector instellingen of `/mcp` in een interactieve sessie. Deze sessie is non-interactief.

**Wat PostHog wel liet zien**

Nul betaald verkeer over de laatste zeven dagen. Geen enkele `meta` bron, geen enkele `cpc` medium in de UTM verdeling. De enige getagde bronnen zijn e-mail (mailjet, klaviyo), organic (youtube, pinterest) en één partner referral. Laatste betaalde klik blijft 1 juli.

Dat maakt de blokkade urgenter dan een gemist rapport. Er zijn twee scenario's en je kunt ze nu niet uit elkaar houden: óf de campagnes staan uit, en dan valt er niets te optimaliseren, óf ze draaien wel en de tracking is stuk, en dan verbrand je budget dat je niet ziet. Twee minuten in Meta Ads Manager beantwoordt dat, ook zonder Pipeboard.

Let ook op de 32.973 pageviews zonder bron over 5.908 personen. Gecombineerd met de crawler-bevinding van vanochtend is dat cijfer vervuild, dus zet bot filtering aan voordat je die cross-references weer gaat gebruiken.

Alleen de Meta Ads MCP en PostHog MCP zijn benaderd, geen Google MCPs, niets naar de tracker Sheet. Rapport staat in `Output/Reports/Daily/2026-08-10_auto_optimize.md`, gecommit en gepusht.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
