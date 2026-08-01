# Auto-Optimize Rapport, 1 augustus 2026

**Status: geen actieve ads. Nul automatische acties uitgevoerd.**

Alle 5 campagnes in het Sempertex Ad Account (`act_567892422940728`) staan op PAUSED. Insights over `last_3d`, `last_30d` en `last_90d` geven allemaal een lege dataset terug. Laatste dag met spend was 20 april 2026, dat is 103 dagen geleden.

De kill-regels zijn daarmee niet van toepassing: er is geen enkele ad die kan worden gepauzeerd, en er is geen nieuwe data om tegen de drempels te toetsen.

**Accounts gecontroleerd:**

| Account | Resultaat |
|---------|-----------|
| `act_567892422940728` (Sempertex Ad Account) | 5 campagnes, alle PAUSED, 0 spend in 90d |
| `act_607231713057715` | Geen toegang met deze API token |

> Het tweede account uit de command-spec is niet bereikbaar. De token geeft toegang tot `act_567892422940728` en `act_1489853856181844`. Dat laatste account bevat nul campagnes. Als `act_607231713057715` echt gemonitord moet worden, moet de Pipeboard token-scope worden uitgebreid.

---

## Automatische acties uitgevoerd

Geen. Er zijn nul actieve ads, dus er valt niets te pauzeren.

**Totaal gepauzeerd: 0 ads**

---

## Waarschuwingen

Geen live waarschuwingen mogelijk zonder delivery. Frequency, CPM en Link CTR-trend vereisen actuele data.

Eén structurele waarschuwing die los staat van delivery:

| Signaal | Waarde | Actie aanbevolen |
|---------|--------|------------------|
| Corrupte pixel conversiewaarde | Adset Kopie 3 rapporteert 2 aankopen à €21.386 | Fixen vóór herstart, anders optimaliseert Meta op ruis |

Dit is gisteren al vastgesteld in het ads-rapport en is nog steeds open. Zolang dit niet gefixt is, is elke ROAS-gebaseerde budgetbeslissing waardeloos. De gerapporteerde 17,8x campagne-ROAS is een artefact.

---

## Retrospectieve analyse op link metrics

Nu er toch geen live beslissingen te nemen zijn, heb ik de laatst bekende periode (13 jan tot 20 apr 2026) opnieuw doorgerekend, maar dan strikt op **link metrics** in plaats van all-clicks. Dat is nieuw ten opzichte van eerdere rapporten en verandert het beeld.

**Campagne 2026: SYBB, volledige looptijd**

| Metric | All clicks | Link |
|--------|-----------|------|
| Clicks | 12.067 | 10.851 |
| CTR | 4,1% | **3,7%** |
| CPC | €0,21 | **€0,23** |

Op campagneniveau is het verschil klein, ongeveer 10%. Op adset-niveau is het verschil groot, en daar zit het inzicht.

**Per adset (13 jan tot 20 apr 2026)**

| Ad set | Impressions | Link clicks | Spend | Link CTR | CPC (link) | Freq | CPM |
|--------|------------:|------------:|------:|---------:|-----------:|-----:|----:|
| BATCH 2: Expertise & POC | 206.834 | 9.885 | €1.463,49 | **4,8%** | **€0,15** | 2,0 | €7,08 |
| BATCH 2: Expertise & POC, Kopie 2 | 13.955 | 174 | €141,43 | 1,3% | €0,81 | 2,0 | €10,13 |
| BATCH 2: Expertise & POC, Kopie 4 | 4.737 | 57 | €49,83 | 1,2% | €0,87 | 1,5 | €10,52 |
| BATCH 2: Expertise & POC, Kopie 3 | 16.766 | 195 | €206,99 | 1,2% | €1,06 | 1,6 | €12,35 |
| BATCH 2: Expertise & POC, Kopie 1 | 38.614 | 428 | €521,56 | 1,1% | €1,22 | 1,9 | €13,51 |
| Ad Set SYBB test set STATISCH | 16.268 | 112 | €101,74 | **0,7%** | €0,91 | 1,8 | €6,25 |

**Wat dit laat zien:**

1. **De originele adset was 4x beter dan elke kopie.** Link CTR 4,8% tegen 1,1 tot 1,3%. CPC (link) €0,15 tegen €0,81 tot €1,22. Identieke creatives, dramatisch ander resultaat. Dit is klassieke audience-fragmentatie: vijf duplicaten bieden tegen elkaar op dezelfde doelgroep, de leerfase wordt vijf keer opnieuw doorlopen, en het budget versnippert.

2. **De STATISCH adset zou de kill-regel hebben getriggerd.** Link CTR 0,7% bij 16.268 impressions ligt onder de drempel van 0,8% bij minimaal 1.000 impressions. Was deze adset vandaag actief geweest, dan was hij automatisch gepauzeerd. Op all-clicks CTR (1,03%) zou hij onder de oude drempel zijn doorgeglipt. De herziene link-drempel van 13 april vangt hem wel. Dat is precies waarvoor die aanpassing bedoeld was.

3. **Geen van de kopieën haalde de CPC-kill-regel.** Kopie 1 zat op €1,22 en Kopie 3 op €1,06, beide onder de €1,50-drempel. Maar geen van hen haalde de 500 link clicks die daarvoor minimaal nodig zijn, dus de regel had sowieso niet gevuurd. Ze waren slecht, maar niet slecht genoeg om automatisch te sneuvelen. Dat is een gat in de regelset, zie voorstel 4.

---

## 70-20-10 Classificatie

Op de laatst bekende data. Alles staat PAUSED, dus dit is een herstart-baseline, geen live verdeling.

**70% Core, bewezen winners**
- `BATCH 2: Expertise & POC` (origineel), Link CTR 4,8%, CPC (link) €0,15. Ruim binnen de Core-definitie (Link CTR > 1,5% en CPC (link) < €0,50). Kreeg historisch 58,9% van het budget.

**20% Emerging, potentieel**
- Geen. Alle vier de kopieën zitten met Link CTR 1,1 tot 1,3% net binnen de CTR-band, maar hun CPC (link) van €0,81 tot €1,22 ligt boven de Emerging-bovengrens van €0,80. Formeel vallen ze buiten alle drie de categorieën.

**10% Experimental, tests**
- `Kopie 4`, 4.737 impressions. Onder de 500-impressions-grens zit hij niet, maar met 57 link clicks is het oordeel statistisch dun.

**Budget mismatch: ja.** De enige Core-asset kreeg 58,9% van het budget in plaats van 70%. De 41,1% die naar kopieën en statisch ging (€1.021,55) leverde 966 link clicks op. Datzelfde geld in de originele adset had bij €0,15 per link click ongeveer **6.800 link clicks** opgeleverd. De duplicatiestrategie heeft dus grofweg 5.800 link clicks gekost.

> **Let op:** de 70-20-10 drempels staan in de command nog gemarkeerd als niet-gekalibreerd voor link metrics. Bovenstaande classificatie is een richtlijn. Ik voer op basis hiervan geen budget-shifts uit, conform die instructie. De data hierboven is wel bruikbaar om de drempels definitief vast te stellen, zie voorstel 5.

---

## Voorstellen (wacht op goedkeuring)

Er draait niets, dus dit zijn herstart-voorstellen in plaats van optimalisaties.

**1. Fix de pixel conversiewaarde voordat er één euro in gaat**
- Adset Kopie 3 stuurt aankoopwaarden van €21.386 mee op een ticket van circa €368.
- Reden: Meta optimaliseert bij OUTCOME_SALES op waarde. Met deze ruis stuurt het algoritme budget naar de verkeerde signalen. Elke ROAS-drempel in dit systeem is nu onbetrouwbaar.
- Verwachte impact: zonder deze fix zijn kill-regels op ROAS en alle budgetvoorstellen ongefundeerd.
- **Dit is de blocker. De rest heeft geen zin zolang dit open staat.**

**2. Herstart geconsolideerd, niet gedupliceerd**
- Eén campagne, één adset, nul kopieën. Reactiveer `BATCH 2: Expertise & POC` (origineel) en laat de vier kopieën plus STATISCH permanent gepauzeerd.
- Budget: van €100,00/dag campagne-breed naar €100,00/dag op één adset.
- Reden: de data hierboven. Identieke creatives, 4x betere Link CTR en 8x lagere CPC (link) in het origineel. De duplicaten kostten €1.021,55 voor 966 link clicks.
- Verwachte impact: bij gelijk budget en de historische €0,15 CPC (link) gaat de campagne van circa 4.400 naar circa 8.900 link clicks per €1.300 spend.

**3. Diagnose de landing page vóór de herstart, niet de ads**
- 12.262 clicks leverden 6 aankopen op, dat is 0,05% click-to-purchase bij circa €435 kosten per aankoop op een ticket van circa €368.
- Reden: de ads deden hun werk tegen €0,15 per link click. Het lek zit na de klik. Meer budget op werkende ads vergroot alleen het verlies.
- Concreet: haal de PostHog data voor startyourballoonbusiness.com op (bounce rate, scroll depth, CTA click rate, /booking visits) en toets tegen de KPI-targets. Dat mag binnen de regels van deze run, maar ik heb het niet uit eigen beweging gedaan omdat dit command scoped is op ad-optimalisatie.

**4. Voeg een tussenliggende kill-regel toe voor lage-volume verspillers**
- Voorstel: pauzeer ads met CPC (link) > €0,80 na minimaal 150 link clicks (nu: > €1,50 na 500 link clicks).
- Reden: Kopie 1 verbrandde €521,56 op een CPC (link) van €1,22 zonder ooit de kill-regel te raken, omdat hij de 500 link clicks niet haalde. Bij 150 link clicks was hij na circa €180 gestopt. Dat had €340 bespaard op één adset.
- Verwachte impact: verspilling wordt 2 tot 3x sneller afgekapt bij ads die nooit volume maken.

**5. Kalibreer de 70-20-10 drempels definitief op link metrics**
- De command markeert dit nog als TODO. Deze dataset is de eerste met volledige link-metrics per adset en is groot genoeg om het op te lossen.
- Voorstel op basis van de spreiding hierboven: Core = Link CTR > 2,5% én CPC (link) < €0,35. Emerging = Link CTR 0,8 tot 2,5% óf CPC (link) €0,35 tot €0,80. Experimental = < 1.000 impressions.
- Reden: met de huidige waarden valt de enige echte winnaar (4,8% / €0,15) ruim in Core, maar vallen alle andere adsets in een gat tussen de categorieën. De voorgestelde grenzen sluiten dat gat.
- Verwachte impact: classificatie wordt bruikbaar voor automatische budget-shifts in plaats van alleen rapportage.

**6. Nieuwe variaties, gebaseerd op de winnende hooks**
- Uit het ads-rapport van gisteren: H13 haalde 9,8% CTR en €0,07 CPC in de originele adset, H11 en H15 volgden.
- Ik heb bewust nog geen concrete varianten uitgeschreven. Zonder gefixte pixel en een gediagnosticeerde landing page test je nieuwe creatives tegen een kapotte funnel, en dan meet je niets. Zeg het als je ze toch nu wilt hebben, dan schrijf ik 2 tot 3 varianten per winnende hook uit volgens de Hormozi hook types.

---

## Uitvoeringslog

| Tijd | Actie | Resultaat |
|------|-------|-----------|
| 2026-08-01 | Campagnes opgehaald `act_567892422940728` | 5 campagnes, alle PAUSED |
| 2026-08-01 | Campagnes opgehaald `act_1489853856181844` | 0 campagnes |
| 2026-08-01 | Campagnes opgehaald `act_607231713057715` | Geweigerd, token heeft geen toegang |
| 2026-08-01 | Insights `last_3d` account-niveau | Lege dataset |
| 2026-08-01 | Insights `last_30d` en `last_90d` campagne-niveau | Lege dataset |
| 2026-08-01 | Insights `maximum` campagne + adset-niveau | Data opgehaald, retrospectief geanalyseerd |
| 2026-08-01 | Automatische pauzeer-acties | Geen, nul actieve ads |

**Databronnen:** uitsluitend Meta Ads MCP (Pipeboard). Geen Google MCPs aangeroepen, niet naar de Tracker Google Sheet geschreven. PostHog niet bevraagd omdat dit command op ad-optimalisatie scoped is en er geen ad-data was om tegen te cross-referencen.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef de nummers aan. Voorstel 1 blokkeert de rest.**
