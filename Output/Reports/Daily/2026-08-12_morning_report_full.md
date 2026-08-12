# Morning Report — 2026-08-12

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

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

---

Rapport staat in `Output/Reports/Daily/2026-08-11_sybb_report.md`, gecommit en gepusht (`efd1a916`).

## Wat er niet lukte

**Meta Ads MCP (Pipeboard) is in deze sessie niet geautoriseerd**, zevende dag op rij. De sessie is non-interactief, dus autoriseren kan hier niet. Dat gaat via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Sectie 2 van het rapport is daardoor leeg, net als de hele cross-reference tussen ad en pagina. Geen Google MCPs aangeroepen, niet naar de Sheet tracker geschreven.

## Wat PostHog wel liet zien

**De SYBB landing page ligt elf dagen stil.** Nul events op 11 augustus, laatste activiteit 31 juli. Over de hele meetperiode 164 events van 69 personen. Nul betaald verkeer ook: geen Paid Social kanaal, en `utm_source=meta` komt in dertig dagen UTM-data geen enkele keer voor.

**Het SYBB verkeer dat er was: één pageview.** Via de Duitse event registratiepagina op de hoofdsite. Daarbij een correctie die je moet weten: de 90 SYBB pageviews van 10 augustus waren voor 82 stuks één bezoeker uit België in één sessie. Het echte weekniveau is ongeveer 5 pageviews per dag, niet 17. Reken 10 augustus niet mee als vraagsignaal.

**Twee dingen die ik niet kon meten, en dat is het echte probleem.** Er bestaat in het project geen scroll depth event, geen CTA click event en geen `/booking` pagina. En ook de event funnel op sempertexeurope.com heeft geen registratie-voltooid event. Je had op 11 augustus 43 register-pageviews in 15 sessies en er is geen enkele manier om te zien hoeveel daarvan doorkwamen. De targets uit CLAUDE.md zijn dus principieel niet meetbaar, ook niet als het verkeer morgen terugkomt.

**Sitebreed: goede cijfers om de verkeerde reden.** Bounce 22,9% tegen weekgemiddelde 55,5%, sessieduur 8m20s tegen 3m39s, 48 shop confirmations tegen 23,7. Maar sessies dalen voor de achtste dag op rij, van 1.339 op 3 augustus naar 595 nu, min 55,6% ononderbroken. Je verliest oppervlakkig verkeer en houdt koopintentie over, dus die groene cijfers zijn mix-effect en geen verbetering.

**Buiten scope maar te duur om te laten liggen:** 217 rageclicks, waarvan 22 verspreid over drie taalversies van de winkelwagen. Dat raakt direct je omzet. Ik heb het in het rapport bewust buiten de top 3 gehouden omdat het geen SYBB-probleem is.

## Top 3 acties

1. Zet een registratie-voltooid event op de event funnel, dit blokkeert elke conversie-uitspraak
2. Onderzoek de sessiedaling, begin bij Direct (286 van 595 sessies), check wat er rond 3 augustus veranderde
3. Autoriseer Pipeboard

Eén ding om te bevestigen: een eerdere notitie zegt dat campagne `2026: SYBB` sinds 19 april op PAUSED staat. Dat verklaart de nul spend, maar ik kon het deze sessie niet verifiëren zonder Meta-toegang.

---

Rapport staat in `Output/Reports/Daily/2026-08-12_auto_optimize.md`, gecommit en gepusht (`db1971e4`).

**De run is geblokkeerd, vijfde dag op rij.** De Pipeboard Meta Ads connector is niet geautoriseerd en deze sessie is niet-interactief, dus ik kan de OAuth flow hier niet starten. Zonder ad-level `impressions`, `link_click` en `spend` zijn de kill-regels niet te evalueren. Beide ad accounts onbereikbaar.

**Gepauzeerd: 0 ads.** Niet omdat alles goed presteert, maar omdat er niets beoordeeld is. 70-20-10 classificatie en alle budget-, variatie- en audience-voorstellen vervallen om dezelfde reden.

Autoriseren kan alleen jij, via je claude.ai connector instellingen of `/mcp` in een interactieve sessie.

Wat PostHog wel liet zien:

- **Nul betaald verkeer.** Paid Social komt niet voor in de kanaalverdeling over 3 dagen, en over 30 dagen staat er geen enkele `meta / cpc / sybb` regel. De enige "campagne" regels zijn mailjet en Klaviyo email.
- **De sessiedaling zet door, nu negen dagen ononderbroken.** Van 1.271 op 3 augustus naar 514 op 11 augustus, min 59,6%. Gisteren stond dit op acht dagen. Geen enkele dag omhoog. Dit is groter dan elk ad-optimalisatie effect dat je hierna zou boeken, dus dit gaat voor.
- Direct is 67,9% van je volume én je slechtste bounce rate (67,4%). Daar begint het onderzoek. Organic Search bouncet op 1,7% en kost niets.

Punten 2 tot en met 6 in het rapport (sessiedaling onderzoeken, conversie events op de SYBB pagina, Klaviyo `utm_campaign` tagging, UTM casing, Organic Search) hebben Pipeboard niet nodig.

Geen Google MCPs aangeroepen, niets naar de Tracker Sheet geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
