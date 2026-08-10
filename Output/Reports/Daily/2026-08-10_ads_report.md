# Meta Ads Rapport, 10 augustus 2026

**De Meta Ads data kon ik opnieuw niet ophalen.** De Pipeboard connector is in deze sessie niet geautoriseerd, dus stappen 1 tot en met 4 van `/ads-report` konden niet draaien. Geen spend, impressions, CTR, CPC, CPM, conversies of ROAS. Vierde dag op rij. Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

De onderstaande analyse komt volledig uit PostHog.

---

## Overzicht per campagne

Niet beschikbaar. Zonder Pipeboard geen campagne, adset of ad niveau data.

## Underperformers

Niet te bepalen zonder Meta data. De drempelwaarden (CPC boven €0,50, CTR onder 1%, frequency boven 3,5, CPM boven €15) zijn niet toetsbaar.

## Top performers

Niet te bepalen.

---

## Wat PostHog wel bevestigt

### Nul betaald verkeer, 40 dagen

Laatste `META/cpc/SYBB` klik: **1 juli 2026, 16:42**. Vier events, één persoon. Daarna niets.

In de kanaalverdeling over 30 dagen ontbreekt Paid Social volledig:

| Kanaal | Sessies | Bounce rate | Gem. duur |
|--------|---------|-------------|-----------|
| Direct | 13.874 | 63,2% | 195s |
| Referral | 5.340 | 48,3% | 292s |
| Organic Search | 1.903 | 4,7% | 585s |
| Email | 430 | 16,5% | 305s |
| AI | 213 | 15,0% | 210s |
| Organic Social | 117 | 16,2% | 153s |
| Organic Video | 8 | 12,5% | 77s |
| **Paid Social** | **0** | | |

### UTM casing is nog steeds fout

De enige Meta klik ooit gemeten kwam binnen als `utm_source=META`, `utm_campaign=SYBB`, `utm_content=H14,B3,CTA5`. De standaard schrijft lowercase voor met underscores: `meta`, `sybb`, `h14_b3_cta5`. Komma's in `utm_content` breken bovendien de match met de tracker kolommen. Dit moet gefixt zijn vóór je herstart, anders is je eerste week aan data weer niet te koppelen.

### SYBB landing page ligt tien dagen stil

Laatste event op startyourballoonbusiness.com: **31 juli**, 2 events van 1 persoon. De pixel werkt, dat is eerder vastgesteld. Wat ontbreekt is verkeer.

### Site breed, 30 dagen

16.692 bezoekers, 105.156 pageviews, 20.117 sessies, gemiddelde sessieduur 4m30s, bounce rate 57,5%.

---

## De bounce rate stijging is een verkeersmix, geen site probleem

Dit is de belangrijkste vondst van vandaag en hij corrigeert het beeld van gisteren.

De dagelijkse bounce rate springt vanaf 6 augustus:

| Dag | Sessies | Gem. duur | Bounce |
|-----|---------|-----------|--------|
| 5 aug | 1.135 | 300s | 34,8% |
| 6 aug | 1.049 | 203s | 63,1% |
| 7 aug | 951 | 165s | 66,5% |
| 8 aug | 865 | 149s | 70,5% |
| 9 aug | 747 | 119s | 73,5% |
| 10 aug (deels) | 185 | 117s | 84,9% |

Uitgesplitst per kanaal zit de sprong volledig bij Direct. Referral schommelt tussen 47% en 73% zonder trend, Organic Search blijft onder 9%. Alleen Direct gaat van 36% naar 90%.

Binnen Direct is de oorzaak de instappagina:

| Periode | Type instap | Sessies | Bounce |
|---------|-------------|---------|--------|
| Vóór 6 aug | Homepage | 1.810 | 3,3% |
| Vóór 6 aug | Diepe pagina | 1.349 | 86,7% |
| Ná 6 aug | Homepage | 668 | 10,0% |
| Ná 6 aug | Diepe pagina | 2.579 | 89,8% |

Diepe pagina's bouncen in **beide** periodes rond 87 tot 90%. Er is dus niets slechter geworden aan de site. Wat er gebeurde: homepage instappen zakten met 63%, terwijl instappen op diepe productpagina's bijna verdubbelden. De mix kantelde van 57% homepage naar 21% homepage, en de gemiddelde bounce rate volgde mee.

Twee dingen volgen hieruit:

1. **Die 2.579 diepe instappen met 90% bounce zijn vrijwel zeker crawlers.** Direct verkeer dat zonder referrer op een specifieke productpagina landt, één pagina bekijkt en vertrekt, is de handtekening van bots. Zet bot filtering aan in PostHog en controleer of `filterTestAccounts` in je rapportages meeloopt. Zolang dit meetelt is elke bounce rate en sessieduur in je rapporten vervuild.

2. **De echte zorg is de andere kant: homepage instappen zakten van 1.810 naar 668.** Dat is menselijk verkeer dat wegvalt. Dat verdient onderzoek los van de ads situatie.

De conclusie van gisteren, dat de sessieduur daling losstond en apart onderzoek verdiende, klopte in richting maar niet in oorzaak. Zowel de duur daling als de bounce stijging komen uit dezelfde mixverschuiving.

---

## Samenvatting

- **Totaal spend**: onbekend, Pipeboard niet geautoriseerd
- **Betaald verkeer**: nul, al 40 dagen
- **Beste performer**: niet te bepalen
- **Slechtste performer**: niet te bepalen
- **Grootste blokkade**: Pipeboard autorisatie

## Volgorde van handelen

1. **Autoriseer Pipeboard.** Dit blokkeert alle ads rapportage, vier dagen op rij.
2. **Zet bot filtering aan in PostHog.** Al je bounce en duur cijfers zijn nu vervuild door crawler verkeer op productpagina's.
3. **Fix UTM casing naar lowercase in alle ad URLs**, en vervang de komma's in `utm_content` door underscores.
4. **Zet conversie events op de SYBB pagina.** De pixel meet nu alleen pageviews.
5. **Verifieer conversiewaarde tracking.** De eerder gerapporteerde ROAS van 17,81x is vrijwel zeker een pixelfout.
6. **Tag de Klaviyo mails met `utm_campaign`.** 109 bezoekers zijn nu niet toewijsbaar naar campagne.
7. **Onderzoek de daling in homepage instappen** van 1.810 naar 668.
8. **Pas daarna herstarten** volgens 70-20-10, budget naar de bewezen `meta/cpc/sybb` hooks.

Punt 2 tot en met 7 kun je nu al doen, die hebben Pipeboard niet nodig. Dan staat je meting schoon klaar zodra er weer budget loopt.

---

## Google Sheet

Overgeslagen op verzoek. Rapport opgeslagen in `Output/Reports/Daily/2026-08-10_ads_report.md`.
