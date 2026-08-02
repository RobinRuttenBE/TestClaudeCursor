# Auto-Optimize Rapport, 2 August 2026

**Account:** Sempertex Ad Account (act_567892422940728)
**Analysevenster:** last_3d (30 July 2026 tot 2 August 2026)
**Databron:** Meta Ads MCP (Pipeboard). Geen Google MCP gebruikt, geen schrijfactie naar de Tracker Sheet.
**Run timestamp:** 2026-08-02

---

## Samenvatting

Er zijn **geen actieve campagnes, ad sets of ads** in het account. Alle vijf campagnes staan op PAUSED. Het account heeft in de laatste 3 dagen, en ook in de laatste 30 dagen, **EUR 0,00 uitgegeven en 0 impressions geleverd**.

Daarmee is er niets om automatisch te optimaliseren. De kill-regels hebben geen enkele ad om op te triggeren.

De laatste levering was in **April 2026**. Het account staat nu ruim drie maanden donker.

---

## ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd, er zijn geen actieve ads.**

| Ad | Reden | Was | Nu | Performance |
|----|-------|-----|-----|-------------|
| (geen) | n.v.t. | n.v.t. | n.v.t. | n.v.t. |

**Totaal gepauzeerd: 0 ads**

Kill-regels konden niet worden toegepast: 0 actieve ads, 0 impressions in het venster, dus de minimumdrempels van 1.000 impressions en 500 link clicks worden nergens gehaald.

---

## Campagnestatus

| Campagne | ID | Status | Dagbudget | Laatst gewijzigd |
|---|---|---|---|---|
| 2026: SYBB | 120239435987290239 | PAUSED | EUR 100,00 | 19 April 2026 |
| 2026: SYBB - Kopie | 120243293329420239 | PAUSED | geen | 20 April 2026 |
| Last push Nozzle Up | 120233295855990239 | PAUSED | geen | 21 September 2025 |
| Nozzle Up END OF AUGUST | 120232324822740239 | PAUSED | EUR 70,00 | 15 September 2025 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | PAUSED | EUR 30,00 | 15 September 2025 |

---

## ⚠️ Waarschuwingen

| Signaal | Waarde | Actie aanbevolen |
|---|---|---|
| Account volledig donker | 0 impressions, EUR 0,00 sinds mei 2026 | Beslis of SYBB heropstart of definitief stopt |
| Tweede account niet bereikbaar | act_607231713057715 geeft een permissiefout | Zie sectie Datakwaliteit |
| Conversiewaarden onbetrouwbaar | 6 purchases met waarde 44.247 | Pixel-waarde valideren voor je op ROAS stuurt |
| CPM verdubbelde in de Kopie ad set | EUR 6,38 tot EUR 8,06 werd EUR 10,13 tot EUR 13,51 | Audience was verzadigd bij de April-herstart |

Creative fatigue (frequency > 3,5) is nergens bereikt. De hoogste lifetime frequency per ad is 1,95, en op campagneniveau 2,24. Vermoeidheid was dus niet de reden dat de campagne stilviel.

---

## 📊 70-20-10 Classificatie

> **Let op:** dit is een **historische** classificatie op lifetime data van campagne 2026: SYBB (13 January tot 30 April 2026). Er is geen last_3d data. Gebruik dit als herstart-referentie, niet als oordeel over huidige performance.
>
> Conform de TODO in het command zijn de 70-20-10 drempels nog niet gekalibreerd voor link metrics. Onderstaande indeling is een **richtlijn**, geen hard oordeel. Er worden dan ook geen budget-shifts uitgevoerd.

**70% Core (Link CTR > 1,5% en CPC link < EUR 0,50):**

| Ad | Ad set | Impressions | Spend | Link CTR | CPC (link) |
|---|---|---|---|---|---|
| H13,B3,CTA5 | BATCH 2: Expertise & POC | 60.074 | EUR 421,29 | 10,6% | EUR 0,07 |
| H15,B3,CTA5 | BATCH 2: Expertise & POC | 34.299 | EUR 218,96 | 4,1% | EUR 0,16 |
| H14,B3,CTA5 | BATCH 2: Expertise & POC | 33.235 | EUR 232,36 | 2,3% | EUR 0,31 |
| H11,B3,CTA5 | BATCH 2: Expertise & POC | 31.060 | EUR 202,48 | 2,2% | EUR 0,30 |

**20% Emerging (Link CTR 0,8% tot 1,5%):**

| Ad | Ad set | Impressions | Spend | Link CTR | CPC (link) |
|---|---|---|---|---|---|
| H12,B3,CTA5 | BATCH 2: Expertise & POC | 48.166 | EUR 388,40 | 1,5% | EUR 0,56 |
| H12,B3,CTA5 | BATCH 2 Kopie | 13.955 | EUR 141,43 | 1,3% | EUR 0,81 |
| H15,B3,CTA5 | BATCH 2 Kopie | 4.737 | EUR 49,83 | 1,2% | EUR 0,87 |
| H13,B3,CTA5 | BATCH 2 Kopie | 16.766 | EUR 206,99 | 1,2% | EUR 1,06 |
| H11,B3,CTA5 | BATCH 2 Kopie | 38.614 | EUR 521,56 | 1,1% | EUR 1,22 |

De vier Kopie-varianten vallen op Link CTR in de Emerging-band, maar hun CPC (link) ligt boven de Emerging-bandbreedte van EUR 0,50 tot EUR 0,80. Ze zijn dus Emerging op doorklik, maar duur op kosten. Geen van hen haalde 500 link clicks, dus de CPC kill-regel zou ook bij heropstart niet direct vuren.

**10% Experimental:**

| Ad | Ad set | Impressions | Spend | Link CTR | CPC (link) |
|---|---|---|---|---|---|
| SYBB w/ Semp (BLACK) | Ad Set SYBB test set STATISCH | 16.268 | EUR 101,74 | 0,7% | EUR 0,91 |

Deze ad zit onder de kill-drempel van 0,8% Link CTR bij ruim 16.000 impressions. Bij een heropstart hoort deze niet terug te komen in zijn huidige vorm. De ad staat al op PAUSED.

**Budget mismatch:** niet van toepassing. Er loopt geen budget, dus er is niets te herverdelen.

---

## Wat de historische data laat zien

Campagne 2026: SYBB, lifetime (13 January tot 30 April 2026):

| Metric | Waarde |
|---|---|
| Spend | EUR 2.485,04 |
| Impressions | 297.174 |
| Reach | 132.674 |
| Link clicks | 10.851 |
| **Link CTR** | **3,7%** |
| **CPC (link)** | **EUR 0,23** |
| All Clicks CTR | 4,1% |
| CPC (all) | EUR 0,21 |
| Landing page views | 6.992 |
| Leads | 15 |
| Purchases | 6 |
| CPM | EUR 8,36 |
| Frequency | 2,24 |

Per maand:

| Maand | Spend | Impressions | Link clicks | Link CTR | CPC (link) | CPM |
|---|---|---|---|---|---|---|
| January 2026 | EUR 101,74 | 16.268 | 112 | 0,7% | EUR 0,91 | EUR 6,25 |
| March 2026 | EUR 1.323,83 | 189.067 | 9.703 | 5,1% | EUR 0,14 | EUR 7,00 |
| April 2026 | EUR 1.059,47 | 91.839 | 1.036 | 1,1% | EUR 1,02 | EUR 11,54 |
| May tot August 2026 | EUR 0,00 | 0 | 0 | n.v.t. | n.v.t. | n.v.t. |

Drie observaties die er toe doen bij een herstart:

1. **March was het sterke blok, April brak weg.** Link CTR zakte van 5,1% naar 1,1% en CPC (link) steeg van EUR 0,14 naar EUR 1,02, dus ruim zeven keer duurder. Tegelijk steeg CPM van EUR 7,00 naar EUR 11,54. Dit is het patroon van een verzadigde audience in dezelfde targeting, niet van slechte creatives.

2. **De Kopie ad set presteerde structureel slechter dan het origineel.** Dezelfde hooks (H11, H12, H13, H15) haalden in de Kopie-set een CPM van EUR 10,13 tot EUR 13,51 tegen EUR 6,38 tot EUR 8,06 in de originele set. Zelfde creative, andere kostprijs, wat opnieuw naar audience-verzadiging wijst.

3. **H13 is een uitschieter die verificatie verdient.** 10,6% Link CTR bij EUR 0,07 CPC ligt 2,6 keer boven de op een na beste ad. Maar slechts 64,1% van die link clicks werd een landing page view, dus circa 2.279 klikken kwamen nooit aan op de pagina. Voor je hierop opschaalt: check of dit echte intentie is of accidentele klikken op een misleidend klikbaar element.

---

## 💡 Voorstellen (wacht op goedkeuring)

**1. Beslis eerst of SYBB heropstart**

Het account staat drie maanden stil met een dagbudget van EUR 100,00 klaarstaand op de SYBB-campagne. Zonder die beslissing zijn alle andere voorstellen theoretisch.
Reden: er is geen enkele optimalisatie mogelijk op een account dat niet levert.
Verwachte impact: geen, dit is een go of no-go.

**2. Bij heropstart: nieuwe audience, niet nieuwe creatives**

- Herstart de originele ad set BATCH 2: Expertise & POC met de vier Core ads (H13, H15, H14, H11), niet de Kopie-set.
- Vervang of verbreed de targeting. Bouw een lookalike op de 6.992 landing page views of de 15 leads, of verbreed geografisch.
- Start op EUR 30,00 per dag in plaats van EUR 100,00 en schaal pas op na 3 dagen boven de drempels.

Reden: de creatives waren in March bewezen (5,1% Link CTR, EUR 0,14 CPC link). De April-instorting was CPM-gedreven, niet creative-gedreven. Nieuwe creatives op een verzadigde audience lost het probleem niet op.
Verwachte impact: terugkeer richting het March CPM-niveau van EUR 7,00, en daarmee CPC (link) onder EUR 0,50.

**3. Repareer de pixel-waarden voor je op ROAS stuurt**

De campagne rapporteert 6 purchases met een gezamenlijke waarde van 44.247 en 6 registraties met een waarde van 86.100. Dat is EUR 7.374 per aankoop, wat niet klopt voor een SYBB-workshop. Er staat daarnaast een tweede purchase-waarde van 4,42 in dezelfde data.
Reden: zolang dit niet klopt is elke ROAS-gebaseerde beslissing, inclusief de 70-20-10 Core-regel op ROAS > 2x, waardeloos.
Verwachte impact: betrouwbare Core-classificatie en bruikbare cost per purchase.

**4. Nieuwe variaties op de winnende hooks**

Alleen relevant zodra punt 1 en 2 rond zijn. Gebaseerd op de drie hoogste Link CTR hooks: H13 (10,6%), H15 (4,1%) en H14 (2,3%). De hook-teksten zelf staan niet in de insights data, alleen de codes. Ik kan hier concrete varianten voor schrijven zodra je de bijbehorende hook-teksten aanlevert of me de creatives laat ophalen.

**5. Kalibreer de 70-20-10 drempels**

Het command draagt nog een openstaande TODO: de 70-20-10 drempels zijn gezet op all-clicks metrics, terwijl de kill-regels sinds 13 April 2026 op link metrics draaien. De SYBB lifetime data geeft nu een concrete ijkpunt: all-clicks CTR 4,1% tegen Link CTR 3,7%, en CPC (all) EUR 0,21 tegen CPC (link) EUR 0,23. Ik kan een voorstel voor gekalibreerde drempels uitwerken als je dat wil.

---

## Datakwaliteit en beperkingen

- **act_607231713057715 is niet opvraagbaar.** Het Pipeboard-token geeft: "This API token does not have access to account act_607231713057715. Allowed accounts: act_1489853856181844, act_567892422940728". Dit account staat wel in het command genoemd. Ofwel klopt het ID niet meer, ofwel mist de connectie de rechten. Controleer dit op pipeboard.co/connections.
- **act_1489853856181844 (AmbitionAvenue)** is wel bereikbaar en bevat 0 campagnes en EUR 0,00 spend. Geen relevante data.
- **Geen last_3d data beschikbaar.** Alle cijfers in dit rapport zijn lifetime of per maand, en zijn als zodanig gelabeld. De kill-regels en de 70-20-10 indeling zijn niet toegepast als beslissing, alleen als referentie.
- **Ad-level insights waren te groot voor één respons** en zijn lokaal uitgelezen. Alle 10 ads van campagne 2026: SYBB zijn meegenomen.
- **Landing page views ontbreken volledig in January 2026** (0 LPV bij 112 link clicks), wat er op wijst dat de tracking toen nog niet live stond. Vergelijk January daarom niet met March en April.
- **Google MCP tools zijn niet aangeroepen** conform de instructie voor deze run. Er is niet naar de Meta Ads Tracker Google Sheet geschreven.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef de nummers aan.**
