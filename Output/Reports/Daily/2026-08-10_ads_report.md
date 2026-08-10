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
