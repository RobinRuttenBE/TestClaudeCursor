# SYBB Daily Report -- 11 april 2026

## 1. Samenvatting

**Spend verdubbeld, maar CPC stijgt richting grens.** Dagelijkse spend schoot omhoog naar EUR 137,76 (vs EUR 68,21 op 10 april), waarmee het veruit de duurste dag in de 7d-periode is. Alle 5 ad sets draaien nu op volle kracht. Volume is sterk: 157 link clicks en 123 landing page views. Maar CPC steeg naar EUR 0,49, vlak onder het target van EUR 0,50. H13 leverde 2 purchases (!) en H11 genereerde 4 add-to-carts en 4 initiated checkouts. GA4 data toont 161 sessies maar 100% bounce rate en slechts 5 scroll events, wat duidt op een tracking-probleem of ernstig LP engagement issue. 14 sessies bereikten /booking en 2 bereikten /checkout.

## 2. Meta Ads Performance

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | EUR 137,76 | EUR 46,42 | ↑ (+197%) |
| Impressions | 14.466 | 5.462 | ↑ (+165%) |
| Clicks (all) | 284 | 112 | ↑ (+153%) |
| Link Clicks | 157 | 59,9 | ↑ (+162%) |
| CTR | 1,96% | 2,06% | -> (stabiel) |
| CPC | EUR 0,49 | EUR 0,41 | ↓ (+17% verslechterd) |
| Frequency | 1,63 | 1,75 | -> (stabiel) |
| Landing Page Views | 123 | 43,7 | ↑ (+181%) |
| Video Views | 2.555 | 992 | ↑ (+158%) |
| Reach | 8.890 | 3.123 | ↑ (+185%) |

**Analyse:** De forse spend-stijging toont dat alle 5 ad sets nu actief budget verbranden. Volume-metrics zijn sterk, maar de CPC-stijging van EUR 0,36 (10 apr) naar EUR 0,49 (11 apr) is zorgwekkend. Dit suggereert dat Meta het publiek sneller uitput of dat de biedingsdruk toeneemt. Bij EUR 0,49 zitten we op de rand van het EUR 0,50 target.

### Conversies

| Conversie | Gisteren | 7d Totaal |
|-----------|----------|-----------|
| View Content | 8 | 21 |
| Add to Cart | 6 | 12 |
| Initiate Checkout | 6 | 8 |
| Complete Registration | 1 | 1 |
| Purchase | 2 | 2 |
| Cost per LP View | EUR 1,12 | EUR 1,06 |
| Cost per Checkout | EUR 22,96 | EUR 40,62 |

**Opmerking:** De 2 purchases kwamen via H13 (Kopie 3). Purchase value van EUR 42.773,50 per Meta pixel lijkt incorrect geconfigureerd. De workshop kost waarschijnlijk ~EUR 350. Pixel value verificatie is nodig.

### Ad Variant Performance

| Ad (utm_content) | Spend | Link Clicks | CTR | CPC | LP Views | Cost/LP View | GA4 Sessions | GA4 Avg Duration | Conversies |
|-------------------|-------|-------------|-----|-----|----------|--------------|--------------|------------------|------------|
| **H12,B3,CTA5** | EUR 39,10 | 55 | 2,04% | EUR 0,38 | 45 | EUR 0,87 | 46 | 21,0s | 1 VC |
| **H13,B3,CTA5** | EUR 37,83 | 40 | 1,77% | EUR 0,64 | 34 | EUR 1,11 | 30 | 17,6s | 2 PUR + 2 ATC + 2 IC + 1 CR |
| **H11,B3,CTA5** | EUR 29,97 | 26 | 2,01% | EUR 0,54 | 22 | EUR 1,36 | 24 | 13,0s | 4 ATC + 4 IC + 3 VC |
| **H15,B3,CTA5** | EUR 19,19 | 26 | 2,41% | EUR 0,40 | 16 | EUR 1,20 | 24 | 48,0s | 1 VC |
| **H14,B3,CTA5** | EUR 11,67 | 10 | 1,38% | EUR 0,65 | 6 | EUR 1,95 | 11 | 52,8s | -- |

*PUR = Purchase, ATC = Add to Cart, IC = Initiate Checkout, VC = View Content, CR = Complete Registration*

**Beste variant: H13,B3,CTA5.** De enige variant met purchases (2x). Daarnaast 2 add-to-carts, 2 initiated checkouts en 1 complete registration. Ondanks een hogere CPC (EUR 0,64) levert H13 de diepste funnel-conversies.

**Volume winnaar: H12,B3,CTA5.** Meeste link clicks (55) en LP views (45) bij de laagste CPC (EUR 0,38) en cost per LP view (EUR 0,87). Beste efficiency voor traffic generatie.

**Funnel performer: H11,B3,CTA5.** 4 add-to-carts en 4 initiated checkouts. Consistente mid-funnel performer, bevestigt de trend van 10 april.

**Engagement verrassing: H15,B3,CTA5.** Langste gemiddelde sessieduur via GA4 (48,0s), wat suggereert dat deze hook bezoekers dieper engageert op de LP, ondanks een lager volume.

**Zwakste variant: H14,B3,CTA5.** Laagste CTR (1,38%), hoogste CPC (EUR 0,65), slechts 6 LP views, nul conversies. Wel langste GA4 sessieduur (52,8s) maar op extreem laag volume (11 sessies).

### Ad Set Performance

| Ad Set | Spend | CPC | CTR | Frequency | LP Views |
|--------|-------|-----|-----|-----------|----------|
| Kopie 2 (H12) | EUR 39,10 | EUR 0,38 | 2,04% | 1,40 | 45 |
| Kopie 3 (H13) | EUR 37,83 | EUR 0,64 | 1,77% | 1,23 | 34 |
| Kopie 1 (H11) | EUR 29,97 | EUR 0,54 | 2,01% | 1,35 | 22 |
| Kopie 4 (H15) | EUR 19,19 | EUR 0,40 | 2,41% | 1,33 | 16 |
| Origineel (H14) | EUR 11,67 | EUR 0,65 | 1,38% | 1,26 | 6 |

**Budget verdeling:** Meta verdeelt het budget ongelijk. Kopie 2 (H12) en Kopie 3 (H13) krijgen samen 56% van de spend, terwijl het originele ad set (H14) naar de achtergrond verdwijnt.

## 3. Landing Page Health

### GA4 Metrics (startyourballoonbusiness.com)

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Sessies | 161 | 77,7 | - | ↑ |
| Unieke gebruikers | 154 | 73,4 | - | ↑ |
| Pageviews | 177 | 93,9 | - | ↑ |
| Bounce Rate (GA4) | 100% | 87,0% | <55% | 🔴 |
| Avg Session Duration | ~22s | 31,4s | >90s | 🔴 |
| Engagement Rate | 0% | 13,1% | - | 🔴 |
| Scroll Events (90%) | 5 (3,3%) | ~4,6/dag | >20% | 🔴 |
| /booking Visits | 14 | - | - | 🟡 |
| /checkout Visits | 2 | - | - | 🟡 |
| Nieuwe bezoekers | 94% | - | - | - |

**KRITIEK: Bounce rate 100% maar 14 /booking visits.** GA4 rapporteert 0 engaged sessions op 11 april, terwijl 14 sessies de /booking pagina bereikten en 2 sessies zelfs /checkout. Dit is tegenstrijdig en wijst op een GA4 configuratie-issue: ofwel de engagement timer is niet correct ingesteld, ofwel de /booking en /checkout bezoeken zijn aparte sessies (geen doorkliks vanuit de LP).

### UTM Segmentation (GA4, alleen Paid Social)

| Ad Variant | Sessies | Users | Pageviews | Avg Duration |
|------------|---------|-------|-----------|--------------|
| h12_b3_cta5 | 46 | 46 | 49 | 21,0s |
| h13_b3_cta5 | 30 | 29 | 34 | 17,6s |
| h11_b3_cta5 | 24 | 22 | 26 | 13,0s |
| h15_b3_cta5 | 24 | 23 | 25 | 48,0s |
| h14_b3_cta5 | 11 | 11 | 12 | 52,8s |
| (direct / niet-meta) | 26 | 25 | 31 | ~7,1s |

**Cross-reference Meta vs GA4:** Meta rapporteert 123 LP views, GA4 registreert 135 Paid Social sessies. Het verschil van ~10% is normaal door tracking discrepanties.

## 4. Funnel Drop-off

### Meta Ads Funnel
```
Impressions (14.466)  -->  Clicks (284)  -->  Link Clicks (157)  -->  LP Views (123)  -->  Add to Cart (6)  -->  Checkout (6)  -->  Purchase (2)
   100%                     1,96%              1,09%                  0,85%                0,04%                0,04%              0,01%
```

### Landing Page Funnel (GA4)
```
LP Visit (151 sessies op /)  -->  /booking (14)  -->  /checkout (2)  -->  Purchase (2)
         100%                        9,3%                1,3%              1,3%
```

**Grootste lek: LP bezoek naar /booking.** 90,7% van LP bezoekers verlaat de pagina zonder /booking te bezoeken. Maar 9,3% naar /booking is een verbetering die consistent is met de eerdere rapportages. Het echte probleem zit in het volume: bij 151 LP sessies levert 9,3% slechts 14 /booking bezoeken op.

**Positief: /booking naar /checkout conversie.** 14,3% van /booking bezoekers gaat door naar /checkout (2/14). En 100% van /checkout bezoekers koopt (2/2), al zijn de aantallen te klein voor conclusies.

## 5. Rode Vlaggen 🚩

### 1. CPC NADERT TARGET (EUR 0,49 vs target EUR 0,50)
CPC steeg van EUR 0,36 (10 apr) naar EUR 0,49 (11 apr), een stijging van 36% in 1 dag. Dit is direct gerelateerd aan de spend-verdubbeling. Twee ad sets zitten boven target: H13 (EUR 0,64) en H14 (EUR 0,65). Bij EUR 137,76 dagelijkse spend wordt de audience sneller uitgeput.

### 2. GA4 BOUNCE RATE 100% MET 0 ENGAGED SESSIONS
Terwijl 14 sessies /booking bereikten, rapporteert GA4 nul engaged sessions. Dit is een tracking-anomalie. Mogelijke oorzaken: (a) GA4 engagement tracking is defect, (b) de /booking visits zijn aparte sessies via directe navigatie, niet doorkliks. Dit moet onderzocht worden voordat LP optimalisatie beslissingen genomen worden.

### 3. SLECHTS 5 SCROLL EVENTS OP 177 PAGEVIEWS (2,8%)
Het standaard GA4 scroll event triggert bij 90% scroll depth. Bij 177 pageviews scrolt slechts 2,8% naar de onderkant van de pagina. Dit bevestigt eerdere signalen dat de meeste bezoekers de pagina verlaten voordat ze de CTA bereiken. Of: scroll tracking is niet correct geconfigureerd.

### 4. SPEND VERDUBBELD ZONDER EVENREDIGE CONVERSIE-STIJGING
Spend steeg van EUR 68,21 naar EUR 137,76 (+102%), maar add-to-carts stegen van 4 naar 6 (+50%) en LP views van 65 naar 123 (+89%). De marginale kosten per conversie stijgen.

### 5. PIXEL PURCHASE VALUE INCORRECT
De 2 purchases tonen een waarde van EUR 42.773,50 totaal. Bij een SYBB workshop prijs van ~EUR 350 zou de waarde ~EUR 700 moeten zijn. De Meta pixel rapporteert een verkeerde waarde, wat ROAS berekeningen onmogelijk maakt.

## 6. Top 3 Acties voor Vandaag

### 1. Onderzoek de GA4 engagement tracking
- **Wat:** Controleer waarom GA4 0 engaged sessions rapporteert terwijl bezoekers /booking en /checkout bereiken. Check de GA4 engagement timer instelling en of enhanced measurement (scroll tracking) actief is.
- **Waarom:** Twee databronnen spreken elkaar tegen. Meta pixel registreert 6 add-to-carts en 2 purchases, GA4 zegt 0% engagement. Zonder betrouwbare LP data optimaliseren we blind.
- **Hoe:** GA4 Admin > Property > Data Streams > Enhanced Measurement. Check of scroll tracking en site search aan staan. Overweeg custom scroll events (25/50/75/100%) toe te voegen via GTM.
- **Verwachte impact:** Betrouwbare funnel data voor alle toekomstige rapporten.
- **Escalatie:** Oranje (GA4/GTM configuratie)

### 2. Verlaag spend of pauzeer underperformers om CPC te drukken
- **Wat:** Pauzeer H14 (CPC EUR 0,65, 0 conversies) en overweeg H13 budget te verlagen (CPC EUR 0,64, maar wel 2 purchases). Richt budget naar H12 (CPC EUR 0,38) en H15 (CPC EUR 0,40).
- **Waarom:** Campagne CPC van EUR 0,49 is 1 cent onder target. H14 en H13 trekken het gemiddelde omhoog. Door underperformers te pauzeren kan de campagne-CPC zakken naar ~EUR 0,40 zonder volume te verliezen.
- **Hoe:** Meta Ads Manager > 2026: SYBB > Pauzeer "BATCH 2: Expertise & POC" (H14 origineel). Monitor H13 (Kopie 3) nog 2 dagen vanwege de purchases.
- **Verwachte impact:** CPC-daling naar EUR 0,38-0,42 range. Budget verschuift automatisch naar efficientere variants.
- **Escalatie:** Geel (Robin goedkeuring)

### 3. Fix Meta Pixel purchase value
- **Wat:** Corrigeer de pixel value configuratie zodat purchase events de werkelijke transactiewaarde rapporteren in plaats van EUR 42.773,50.
- **Waarom:** Zonder correcte purchase values is ROAS niet te berekenen. Dit maakt budget-optimalisatie gebaseerd op waarde onmogelijk.
- **Hoe:** Check de Wix/payment integratie. Waarschijnlijk stuurt het checkout systeem een incorrecte `value` parameter mee in het `fbq('track', 'Purchase')` event. Fix in de Wix site code of via server-side Conversions API.
- **Verwachte impact:** Correcte ROAS tracking voor ROI-gebaseerde optimalisatie.
- **Escalatie:** Oranje (Wix site code aanpassing)

---

### Cross-Reference Insights

| Pattern | Bevinding |
|---------|-----------|
| **Ad CTR vs LP Bounce** | Alle variants hebben 100% GA4 bounce rate ondanks varierende CTR (1,38%-2,41%). Dit duidt op een universeel LP probleem of GA4 tracking issue, niet een ad-specifiek probleem. |
| **H13: Hoge CPC maar conversies** | H13 heeft de duurste CPC (EUR 0,64) maar levert als enige purchases. Meta optimaliseert H13 mogelijk richting conversion-likely audience, wat duurdere clicks verklaart. |
| **H15: Lage volume, hoge engagement** | H15 heeft slechts 24 GA4 sessies maar de langste sessieduur (48,0s). De hook trekt minder mensen maar wie klikt, blijft langer. Verdient meer budget voor een eerlijke test. |
| **H12: Volume king** | H12 levert de meeste LP views (45) bij de laagste CPC (EUR 0,38). Maar 0 conversie-events richting purchase. Goede traffic driver, slechte closer. |
| **H11: Mid-funnel consistent** | H11 genereerde weer add-to-carts (4) en initiated checkouts (4), net als op 10 april. Consistent de sterkste mid-funnel performer. |
| **Spend scaling = CPC pressure** | EUR 137,76 spend (3x het 6d-gemiddelde van ~EUR 31/dag) correleert direct met CPC-stijging. De audience pool wordt sneller uitgeput bij dit volume. |

---

### KPI Dashboard vs Targets

| KPI | 11 april | 10 april | Target 30d | Status |
|-----|----------|----------|-----------|--------|
| LP Bounce Rate | 100% (GA4) | n/a | <55% | 🔴 |
| LP Conversie Rate | 1,3% (/checkout) | - | >5% | 🔴 |
| Avg Scroll Depth | 2,8% (90%+) | - | >60% | 🔴 |
| CTA Click Rate | 9,3% (/booking) | - | >4% | 🟢 |
| Meta CPC | EUR 0,49 | EUR 0,36 | <EUR 0,50 | 🟡 |
| Cost per LP View | EUR 1,12 | EUR 1,05 | - | ↓ verslechterd |
| Time on Page | ~22s (gem) | - | >90s | 🔴 |

---

*Rapport gegenereerd: 12 april 2026*
*Databronnen: Meta Ads MCP (Pipeboard), GA4 (SYBB property 528249861)*
*Campagne: 2026: SYBB (ID: 120239435987290239) | Account: Sempertex Ad Account (act_567892422940728)*
*Status: ACTIEF | 5 ad sets, 5 ad variants | Dagbudget: ~EUR 137,76 geleverd*
*GA4 data: BESCHIKBAAR maar engagement tracking toont anomalieen (0 engaged sessions, onderzoek vereist)*
