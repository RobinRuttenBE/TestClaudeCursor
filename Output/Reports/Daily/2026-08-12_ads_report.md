## Meta Ads Rapport, 12 augustus 2026

**De Meta Ads data kon ik niet ophalen, vijfde dag op rij.** Pipeboard is in deze sessie niet geautoriseerd, dus stappen 1 tot en met 4 konden niet draaien. Autoriseren gaat via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

### Wat PostHog bevestigt

**Nul betaald verkeer, 42 dagen.** Laatste `meta / cpc / sybb` klik: 1 juli 2026, 16:42. Geen Paid Social in de kanaalverdeling. De SYBB landing page ligt 12 dagen stil, laatste event 31 juli.

Site breed over 30 dagen: 17.251 bezoekers, 116.500 pageviews, 21.099 sessies, sessieduur 4m43s, bounce 56,2%.

### Twee dingen uit het rapport van gisteren kloppen niet

**De crawler conclusie trek ik in.** Ik heb de zwaarste bezoekers erbij gehaald: 321 pageviews in 2 sessies vanuit België op Edge, 283 vanuit Duitsland op Samsung Internet, en zo verder. Echte browsers, echte EU landen, meerdere sessies over meerdere dagen. Dat is een groothandel die een catalogus doorloopt, geen bot. Zet dus géén bot filtering aan, je zou je beste klanten wegfilteren.

**De bounce piek is voorbij.** 6 tot 9 augustus zat rond 69 tot 77%, nu 28,1% op 11 augustus met 9,1 pageviews per sessie en 8m20s sessieduur. Beste kwaliteit van de afgelopen twee weken.

### Het echte probleem

**Sessies dalen acht dagen op rij, van 1.338 op 3 augustus naar 595 op 11 augustus. Min 55,5%, ononderbroken.**

Ik heb gecheckt of dit een meetfout was, want pageviews bleven wel op peil. Maar sessies én distinct ids dalen allebei even hard mee, dus de bezoekersherkenning werkt gewoon. Er komen echt minder mensen.

Tegelijk gaat wie er wél komt veel dieper: van 4,1 naar 9,3 pageviews per sessie. Je verliest de bovenkant van de trechter en houdt de koopintentie over. Je conversie ziet er daardoor beter uit dan de gezondheid van je verkeer rechtvaardigt.

### Volgorde van handelen

1. Autoriseer Pipeboard, dit blokkeert alles
2. Onderzoek de sessiedaling, begin bij Direct (69% van je volume), check wat er rond 3 augustus veranderde
3. Zet géén bot filtering aan
4. Zet conversie events op de SYBB pagina vóór je herstart
5. Fix UTM casing naar lowercase, komma's in `utm_content` naar underscores
6. Tag de Klaviyo mails met `utm_campaign`, 109 bezoekers niet toewijsbaar
7. Zet Organic Search harder in, bouncet op 4,6% en kost geen budget
8. Pas daarna herstarten volgens 70-20-10

Punt 2 tot en met 7 hebben Pipeboard niet nodig.

Rapport staat in `Output/Reports/Daily/2026-08-12_ads_report.md`, gecommit en gepusht.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Met nul spend en een landing page die 12 dagen stil ligt levert een funnel diagnose nu niets op.
