## Auto-Optimize Rapport, 21 augustus 2026

**Databron:** Meta Ads via Pipeboard (`pk_...f246`, directe HTTP calls, de MCP connector staat in deze sessie op "requires authentication"). Geen Google MCP aangeroepen, niet naar de tracker Sheet geschreven.

**Accountcorrectie:** `act_607231713057715` uit het commando bestaat niet. Het tweede account is `act_1489853856181844` (AmbitionAvenue): nul campagnes, nul spend, €0,00 lifetime. Alleen `act_567892422940728` (Sempertex Ad Account) bevat data.

---

### ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd. Er valt niets te pauzeren.**

| Check | Resultaat |
|---|---|
| Actieve campagnes (`status_filter: ACTIVE`) | 0 van 5 |
| Account insights `last_3d` | lege dataset, nul rijen |
| Account insights `last_7d` | lege dataset, nul rijen |
| Spend laatste 3 dagen | €0,00 |
| Impressions laatste 3 dagen | 0 |

Alle vijf campagnes staan op PAUSED. De kill-regels vereisen minimaal 1.000 impressions (Link CTR regel) of 500 link clicks (CPC regel) binnen het venster van 3 dagen. Geen enkele ad haalt die drempel, want geen enkele ad levert uit. Nul acties is hier het correcte resultaat, geen storing.

**Totaal gepauzeerd: 0 ads.**

---

### ⚠️ Waarschuwingen

| Ad / object | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| H13,B3,CTA5 (Kopie) | status ACTIVE onder paused campagne | effective_status CAMPAIGN_PAUSED | Op PAUSED zetten vóór unpause |
| H12,B3,CTA5 (Kopie) | status ACTIVE onder paused campagne | effective_status CAMPAIGN_PAUSED | Op PAUSED zetten vóór unpause |
| H11, B3, CTA5 (Kopie) | status ACTIVE onder paused campagne | effective_status CAMPAIGN_PAUSED | Op PAUSED zetten vóór unpause |
| H13,B3,CTA5 (Kopie 3) | Dure reach | CPM €19,14 | Boven drempel €15 |
| H12,B3,CTA5 (Kopie 2) | Dure reach | CPM €18,92 | Boven drempel €15 |
| SYBB w/ Semp (BLACK) | 112 link clicks, 0 landing page views | 0,0% doorloop | Bestemming of pixel stuk, testen |
| Creative fatigue | Geen enkele ad boven Frequency 3,5 | hoogste 3,37 | Geen actie |

**De drie ACTIVE ads zijn het echte risico.** Ze zitten in campagne "2026: SYBB - Kopie". Zet je die campagne aan, dan starten H13, H12 en H11 onmiddellijk. Precies die drie Kopie-varianten hebben de duurste CPC (link) van het hele account: €1,12, €1,03 en €0,89. Ze zouden binnen een dag door je eigen kill-regel gepauzeerd worden. Zonde van het geld en van de learning phase.

---

### 📊 Kill-rule dry run op lifetime data

Omdat er niets draait, heb ik de kill-regels losgelaten op de lifetime cijfers. Dit is wat er zou gebeuren als je vandaag alles onveranderd aanzet:

| Ad | Link CTR | Impressions | Zou gepauzeerd worden? |
|---|---|---|---|
| Ad 1 - Eind Aug | 0,7% | 369.136 | **Ja**, Link CTR < 0,8% |
| SYBB w/ Semp (BLACK) | 0,7% | 16.268 | **Ja**, Link CTR < 0,8% |
| Ad 1 - nieuwe doelgroep | 0,6% | 27.705 | **Ja**, Link CTR < 0,8% |

Geen enkele ad triggert de CPC (link) regel. De hoogste CPC (link) is €1,22, onder de drempel van €1,50.

**Hier zit een probleem met de regel zelf.** "Ad 1 - Eind Aug" zou gepauzeerd worden op een Link CTR van 0,7%. Diezelfde ad heeft de op één na laagste CPC (link) van het account (€0,23), 2.104 landing page views, 6 aankopen en €3.849,00 aan plausibele omzet op €604,03 spend. Dat is 6,4x ROAS. De Link CTR regel kijkt naar doorklikratio en negeert wat er ná de klik gebeurt. Bij een brede doelgroep op groot volume is een lage CTR met lage CPC precies wat je wil.

Advies: maak de kill-regel voorwaardelijk. Pauzeer alleen bij Link CTR < 0,8% **én** CPC (link) > €0,50 **én** nul aankopen. Dan overleeft Eind Aug en sneuvelen BLACK en "nieuwe doelgroep" alsnog.

---

### 🔍 Het adset-effect, antwoord op de openstaande vraag uit het ads rapport

Vanochtend stond de vraag open welke adset H13 op €0,07 per klik leverde. Antwoord: **BATCH 2: Expertise & POC**, de originele adset. De dure variant draaide in **BATCH 2: Expertise & POC - Kopie 3**.

Het is geen incident. Elke hook die in beide adsets draaide, presteert slechter in de kopie:

| Hook | Origineel (Expertise & POC) | Kopie | Factor |
|---|---|---|---|
| H13 | €0,07 CPC (link), 10,6% Link CTR | €1,06, 1,2% | **15,1x duurder** |
| H15 | €0,16, 4,1% | €0,87, 1,2% | 5,4x duurder |
| H11 | €0,30, 2,2% | €1,22, 1,1% | 4,1x duurder |
| H12 | €0,56, 1,5% | €0,81, 1,3% | 1,4x duurder |

Vier van de vier. Het verschil zit niet in de hook, het zit in de adset. De originele adset wint op elke creative.

**Maar dan de omdraaiing.** De vier verifieerbare SYBB aankopen komen uit H11 in **Kopie 1**, de dure adset (€1,22 per klik, €368,38 per order, 2,8x ROAS). De goedkope adset leverde 5.808 link clicks en nul aankopen. H13 alleen al: 6.342 link clicks, 4.063 landing page views, **nul aankopen**.

De goedkope adset koopt volume dat niet koopt. De dure adset koopt klanten. Beslis op ROAS, niet op CPC (link).

---

### 📊 70-20-10 Classificatie

Nul actieve ads, dus dit is een herstartplan, geen momentopname. Huidig budget per categorie is €0,00 over de hele linie. Conform de TODO in het commando zijn de drempels nog niet gekalibreerd voor link metrics, dus dit is richtlijn en geen hard oordeel. Geen budget-shifts uitgevoerd.

**70% Core, bewezen op omzet:**
- **Eerste advertentie Nozzle Up** (3 ads Nozzle Up deel 1), Link CTR 2,1%, CPC (link) €0,35, 6 aankopen, €1.180,21 per order, ROAS 23,8x
- **Ad 1 - Eind Aug** (Bredere Doelgroep), Link CTR 0,7%, CPC (link) €0,23, 6 aankopen, €641,50 per order, ROAS 6,4x
- **Ad 1 Denise EU**, Link CTR 1,2%, CPC (link) €0,42, 3 aankopen, €207,67 per order, ROAS 4,0x
- **H11, B3, CTA5** in Kopie 1, Link CTR 1,1%, CPC (link) €1,22, 4 aankopen, €368,38 per order, ROAS 2,8x

**20% Emerging, sterke klikprestatie zonder bewezen omzet:**
- **H15,B3,CTA5** (origineel), Link CTR 4,1%, CPC (link) €0,16, 845 LPV, 0 aankopen
- **Ad 2 USA Audrey**, Link CTR 3,1%, CPC (link) €0,46
- **Ad 1 USA Denise**, Link CTR 2,7%, CPC (link) €0,44
- **H14,B3,CTA5** (origineel), Link CTR 2,3%, CPC (link) €0,31
- **H11, B3, CTA5** (origineel), Link CTR 2,2%, CPC (link) €0,30
- **Ad 2 Audrey EU**, Link CTR 1,7%, CPC (link) €0,34

**10% Experimental, blijft interessant maar onbewezen:**
- **H13,B3,CTA5** (origineel), Link CTR 10,6%, CPC (link) €0,07, 4.063 LPV, **0 aankopen**. Extreem goedkoop verkeer dat niet converteert. Houden als traffic-test, niet als conversie-ad.
- **H12,B3,CTA5** (origineel), Link CTR 1,5%, CPC (link) €0,56
- **FOMO** en **Business** (Nozzle Up), Link CTR 1,5% en 1,2%, CPC (link) €0,49 en €0,53

**Niet herstarten:**
- Alle vier de **Kopie-adsets** en de campagne **2026: SYBB - Kopie** (€124,42 spend, 0 aankopen, CPM tot €19,14)
- **SYBB w/ Semp (BLACK)**, tracking stuk
- **Ad 1 - nieuwe doelgroep**, Link CTR 0,6%, CPC (link) €0,83, 0 aankopen

**Budget mismatch:** Niet van toepassing. Er staat €0,00 uit. Ingestelde daily budgets op de paused campagnes zijn 2026: SYBB €100,00, Nozzle Up END OF AUGUST €70,00, Campagne Nozzle Up 2025 1 €30,00.

---

### 💰 Correctie op de account-ROAS

Eén ad vervuilt het beeld. **H13 in Kopie 3** rapporteert €42.773,50 pixel-omzet op 2 aankopen. Dat is **€21.386,75 per order**. Onmogelijk voor een B2B ballonorder.

De andere vier converterende ads zijn wél plausibel: €1.180,21, €641,50, €368,38 en €207,67 per order.

| | Spend | Pixel-omzet | ROAS |
|---|---|---|---|
| Zoals Meta het rapporteert | €4.867,46 | €55.800,25 | 11,5x |
| Na verwijdering van H13 Kopie 3 | €4.867,46 | €13.026,75 | **2,7x** |

2,7x is het getal waar je op mag sturen. Het blijft pixel-attributie, dus de verificatie in Odoo van vanochtend blijft staan.

---

### 💡 Voorstellen (wacht op goedkeuring)

**1. Opruimen vóór herstart (geen budget, wel nodig)**
- Zet H13, H12 en H11 in campagne "2026: SYBB - Kopie" op PAUSED. Ze staan nu op ACTIVE en starten mee zodra je die campagne aanzet.
- Archiveer campagne "2026: SYBB - Kopie" volledig. €124,42 spend, 195 link clicks, nul aankopen, hoogste CPM's van het account.
- Test de bestemming van "SYBB w/ Semp (BLACK)". 112 link clicks en nul landing page views betekent gebroken URL of pixel.

**2. Herstart klein, alleen in de originele adset**
- Campagne 2026: SYBB, alleen adset **BATCH 2: Expertise & POC**, start op €20,00 per dag in plaats van de ingestelde €100,00.
- Verdeling: 70% H11 (de enige SYBB creative met verifieerbare aankopen), 20% H15, 10% H13 als traffic-test.
- Reden: alle vier de Kopie-adsets presteren slechter op elke hook. Verwachte impact: CPC (link) rond €0,30 in plaats van €1,00 plus.
- Belangrijk voorbehoud: de aankopen kwamen uit Kopie 1, niet uit het origineel. Draai twee weken en beslis op aankopen, niet op CPC.

**3. Nieuwe variaties op de winnende hooks**
De creative-headlines in Meta zijn: H11 en H12 "And you're invited!", H13 "Learn about pricing, marketing & more!", H14 "Your chance awaits!", H15 "Your chance to do the same awaits."

- Op H13 (10,6% Link CTR, nul aankopen). De hook trekt aan, de belofte is te breed. Smal hem in tot één pilaar uit `sybb-8-pillars.md`, bijvoorbeeld pricing alleen. Variatie A: een concreet prijsprobleem als opening. Variatie B: dezelfde belofte met een kwalificerende zin die niet-kopers wegfiltert.
- Op H11 (2,2% Link CTR, alle vier de aankopen). Dit is je enige bewezen SYBB hook. Bouw hier twee varianten op: zelfde belofte in ander format, en zelfde belofte met een andere CTA.
- Op de Nozzle Up winnaar (ROAS 23,8x). Die creative is nooit hergebruikt voor SYBB. De overdracht is het proberen waard.

**4. Kalibreer de kill-regels**
Maak de Link CTR regel voorwaardelijk: pauzeer alleen bij Link CTR < 0,8% **én** CPC (link) > €0,50 **én** nul aankopen. Zonder die aanpassing pauzeert de volgende run "Ad 1 - Eind Aug", je op één na goedkoopste en op één na winstgevendste ad.

**5. Documenteer de hooks**
De H-codes staan nergens in de kennisbank. Ik kan H11 tot H15 alleen via de Meta creative-namen terugvinden, en die zijn onvolledig (H11 en H12 delen dezelfde naam). Zonder de volledige hook-teksten in `Kennis/Voorgaande campagnes/` is elke variatie-opdracht giswerk.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**
