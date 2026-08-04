# Meta Ads Rapport, 4 augustus 2026

**Account:** Sempertex Ad Account (`act_567892422940728`), EUR
**Periode primair:** last 30 days (5 juli tot 4 augustus 2026)
**Databron:** Meta Ads MCP (Pipeboard)

---

## Belangrijkste bevinding

**Er draait niets. Nul euro spend in de afgelopen 30 en zelfs 90 dagen.**

Alle 5 campagnes in het account staan op PAUSED. De laatste euro is uitgegeven in **april 2026**. Het account ligt nu ongeveer 3,5 maand stil.

Het rapport toont daarom de laatste bekende performance per gepauzeerde campagne (lifetime data), zodat je weet waarmee je opnieuw kunt starten.

### Account toegang
- `act_567892422940728` (Sempertex Ad Account), toegankelijk, lifetime spend €4.867,46
- `act_1489853856181844` (AmbitionAvenue), toegankelijk, lifetime spend €0,00, geen campagnes
- `act_607231713057715` (Robin Rutten), **niet toegankelijk** met de huidige Pipeboard token. Foutmelding: "This API token does not have access". Als hier campagnes draaien, zijn die niet zichtbaar in dit rapport.

---

## Spend per maand (volledige historie account)

| Maand | Spend | Impressions | Clicks | CTR | CPC | CPM | Frequency |
|-------|-------|-------------|--------|-----|-----|-----|-----------|
| 2025-07 | €185,08 | 23.597 | 952 | 4,0% | €0,19 | €7,84 | 3,74 |
| 2025-08 | €855,76 | 201.642 | 3.518 | 1,7% | €0,24 | €4,24 | 2,05 |
| 2025-09 | €1.217,16 | 383.324 | 5.245 | 1,4% | €0,23 | €3,18 | 2,18 |
| 2026-01 | €101,74 | 16.268 | 167 | 1,0% | €0,61 | €6,25 | 1,81 |
| 2026-03 | €1.323,83 | 189.067 | 9.965 | 5,3% | €0,13 | €7,00 | 2,07 |
| 2026-04 | €1.183,89 | 99.454 | 2.130 | 2,1% | €0,56 | €11,90 | 2,27 |
| **2026-05 t/m 08** | **€0,00** | 0 | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. |

Duidelijke trend binnen 2026: maart was het sterkste kwartaal ooit qua efficiëntie (CTR 5,3%, CPC €0,13). In april verslechterde alles fors (CPC €0,56, CPM €11,90) en daarna is alles stopgezet.

---

## Overzicht per campagne (laatste bekende performance, gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Freq. | Aankopen | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|----------|------|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 2,24 | 6 | 17,81x (zie waarschuwing) |
| Campagne Nozzle Up 2025 1 | PAUSED | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 2,89 | 6 | 8,30x |
| Last push Nozzle Up | PAUSED | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 2,39 | 3 | 0,78x |
| Nozzle Up END OF AUGUST | PAUSED | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 2,24 | 6 | 6,37x |
| 2026: SYBB, Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 1,42 | 0 | 0,00x |

Looptijden: 2026: SYBB (13 jan 2026), 2026: SYBB Kopie (19 apr 2026), Last push Nozzle Up (15 sep 2025), Nozzle Up END OF AUGUST (26 aug 2025), Campagne Nozzle Up 2025 1 (23 jul 2025).

### Waarschuwing bij de ROAS van 2026: SYBB
De 17,81x is niet betrouwbaar. Van de totale conversiewaarde van €44.247 komt **€42.773,50 uit 2 aankopen op één enkele ad** (H13, B3, CTA5 in adset "BATCH 2: Expertise & POC, Kopie 3"). Dat is €21.386 per aankoop vanaf een SYBB starter landingspagina. Dat is vrijwel zeker een pixel fout, bijvoorbeeld een waarde in centen of een verkeerd doorgegeven ordertotaal.

Extra signaal: het `web_app_in_store_purchase` veld rapporteert voor dezelfde campagne een waarde van €4,42 in plaats van €44.247. Dat schaalverschil wijst op een inconsistente waardeconfiguratie in de pixel.

**Realistische ROAS zonder die 2 aankopen: 0,59x** (€1.473,50 omzet op €2.485,04 spend).

---

## Ad performance, campagne 2026: SYBB

| Ad | Adset | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | LPV | IC | Aankopen |
|----|-------|-------|-------|--------|-----|-----|-----|-------|-----|----|----------|
| H11, B3, CTA5 | Kopie 1 | €521,56 | 38.614 | 784 | 2,0% | €0,67 | €13,51 | 1,85 | 343 | 23 | 4 |
| H13, B3, CTA5 | Expertise & POC | €421,29 | 60.074 | 5.902 | 9,8% | €0,07 | €7,01 | 1,57 | 4.063 | 0 | 0 |
| H12, B3, CTA5 | Expertise & POC | €388,40 | 48.166 | 1.248 | 2,6% | €0,31 | €8,06 | 1,78 | 485 | 2 | 0 |
| H14, B3, CTA5 | Expertise & POC | €232,36 | 33.235 | 911 | 2,7% | €0,26 | €6,99 | 1,46 | 465 | 0 | 0 |
| H15, B3, CTA5 | Expertise & POC | €218,96 | 34.299 | 1.465 | 4,3% | €0,15 | €6,38 | 1,50 | 845 | 1 | 0 |
| H13, B3, CTA5 | Kopie 3 | €206,99 | 16.766 | 331 | 2,0% | €0,63 | €12,35 | 1,64 | 171 | 4 | 2 |
| H11, B3, CTA5 | Expertise & POC | €202,48 | 31.060 | 796 | 2,6% | €0,25 | €6,52 | 1,63 | 445 | 0 | 0 |
| H12, B3, CTA5 | Kopie 2 | €141,43 | 13.955 | 356 | 2,6% | €0,40 | €10,13 | 1,95 | 139 | 6 | 0 |
| SYBB w/ Semp (BLACK) | STATISCH test | €101,74 | 16.268 | 167 | 1,0% | €0,61 | €6,25 | 1,81 | 0 | 0 | 0 |
| H15, B3, CTA5 | Kopie 4 | €49,83 | 4.737 | 107 | 2,3% | €0,47 | €10,52 | 1,45 | 36 | 0 | 0 |

LPV = landing page views, IC = initiate checkout.

## Ad performance, campagne 2026: SYBB Kopie

| Ad | Adset | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | LPV | IC |
|----|-------|-------|-------|--------|-----|-----|-----|-------|-----|-----|
| H11, B3, CTA5 | Kopie 1 | €51,34 | 3.782 | 95 | 2,5% | €0,54 | €13,57 | 1,22 | 42 | 3 |
| H13, B3, CTA5 | Kopie 3 | €47,21 | 2.466 | 51 | 2,1% | €0,93 | €19,14 | 1,20 | 36 | 1 |
| H12, B3, CTA5 | Kopie 2 | €25,87 | 1.367 | 49 | 3,6% | €0,53 | €18,92 | 1,35 | 22 | 2 |

---

## Underperformers

Drempels: CPC boven €0,50, CTR onder 1%, frequency boven 3,5, CPM boven €15.

### Campagne niveau
- **2026: SYBB, Kopie**, CPC €0,64 (drempel €0,50) en CPM €16,34 (drempel €15). Deze kopie presteerde op elk vlak slechter dan het origineel, tegen 3x de klikprijs. Aanbeveling: niet heractiveren, archiveren en het origineel als basis nemen.
- **Nozzle Up END OF AUGUST**, CTR 1,0% (0,99%, net onder drempel). Enorme reach (369k impressies) tegen een spotgoedkope CPM van €1,64, maar de creative pakte niet. Aanbeveling: dit was een breed bereikformat, alleen herhalen als retargeting laag, niet als prospecting.

### Ad niveau
- **H13, B3, CTA5 (Kopie 3)**, in de Kopie campagne CPC €0,93 en CPM €19,14. Slechtste kliksefficiëntie van het hele account. Aanbeveling: deze adset variant niet opnieuw gebruiken.
- **H12, B3, CTA5 (Kopie 2)**, Kopie campagne, CPM €18,92 en CPC €0,53. Zelfde conclusie.
- **H11, B3, CTA5 (Kopie 1)**, hoofdcampagne, CPC €0,67 bij €521,56 spend, de duurste ad van het account. Wel de enige ad met 4 echte aankopen. Aanbeveling: hook behouden, targeting en plaatsingen herzien om de CPC omlaag te krijgen.
- **H13, B3, CTA5 (Kopie 3)**, hoofdcampagne, CPC €0,63. Zelfde hook presteerde in de reguliere adset 9x goedkoper (€0,07). Het probleem zit dus in de adset, niet in de creative.
- **SYBB w/ Semp (BLACK)**, statische test januari, CPC €0,61 en CTR 1,0%. Aanbeveling: statisch werkt niet voor dit publiek, blijf bij video.

---

## Top performers

- **Beste CTR:** H13, B3, CTA5 in adset "BATCH 2: Expertise & POC", **9,8%**. Dat is meer dan het dubbele van de campagne gemiddelde en bijna 4x het accountgemiddelde.
- **Laagste CPC:** dezelfde ad, **€0,07**. Ruim onder het target van €0,50 uit de SYBB KPI tabel.
- **Beste ROAS (betrouwbaar):** Campagne Nozzle Up 2025 1, **8,30x** (€7.081,25 omzet op €853,19 spend, 6 aankopen à gemiddeld €1.180). Dit is een geloofwaardig B2B ordervolume.
- **Goedkoopste reach:** Nozzle Up END OF AUGUST, CPM €1,64.

---

## De echte bottleneck: de landingspagina, niet de ads

De ads deden hun werk. De funnel daarna niet.

| Campagne | Landing page views | Initiate checkout | LPV naar IC | Aankopen |
|----------|-------------------|-------------------|-------------|----------|
| 2026: SYBB | 6.992 | 36 | **0,5%** | 6 |
| Campagne Nozzle Up 2025 1 | 1.733 | 329 | **19,0%** | 6 |
| Last push Nozzle Up | 1.920 | 236 | **12,3%** | 3 |
| Nozzle Up END OF AUGUST | 2.104 | 141 | **6,7%** | 6 |

De SYBB campagne stuurde **4x meer verkeer** naar de landingspagina dan Nozzle Up 2025 1, maar leverde **9x minder checkouts** op. De conversie van bezoeker naar checkout is bij SYBB 38x slechter dan bij Nozzle Up.

Het scherpste voorbeeld: de winnende ad H13 leverde **4.063 landing page views voor €421,29** (€0,10 per bezoeker, uitstekend) en daaruit kwamen **nul** checkouts. Dat is geen creative probleem. Dat is een pagina probleem.

Ter vergelijking met de KPI targets uit de SYBB skill: het target LP conversie is >5% op 30 dagen en >8% op 90 dagen. De gemeten 0,5% zit daar een factor 10 onder.

---

## Samenvatting

- **Totaal spend last 30 days: €0,00.** Geen actieve campagnes, geen delivery.
- **Totaal spend lifetime account: €4.867,46** over 913.352 impressies, 21.977 clicks, CTR 2,4%, CPC €0,22, CPM €5,33.
- **Beste performer:** de hook H13 in adset "BATCH 2: Expertise & POC". 9,8% CTR en €0,07 CPC zijn uitzonderlijke cijfers. Op traffic acquisitie is dit een bewezen winnaar.
- **Slechtste performer:** campagne 2026: SYBB Kopie. €124,42 uitgegeven, hoogste CPC (€0,64) en hoogste CPM (€16,34) van het account, nul aankopen. De duplicatie heeft de learnings van het origineel weggegooid en opnieuw moeten leren.
- **Grootste risico:** de ROAS rapportage is niet te vertrouwen zolang één ad €21.386 per aankoop rapporteert.

### Aanbevelingen

**1. Fix eerst de tracking, dan pas budget aanzetten (deze week)**
Zolang de pixel waardes van €21.386 doorgeeft, kun je geen enkele optimalisatiebeslissing op ROAS baseren en optimaliseert Meta zelf ook op ruis. Controleer de purchase event value configuratie op de checkout, met name of de waarde in euro's of centen wordt doorgegeven. Draai daarna `/tracking-check` op de SYBB pagina.

**2. Fix de landingspagina voor je opnieuw traffic koopt**
0,5% van bezoeker naar checkout betekent dat elke euro adspend voor 99,5% verdampt na de klik. Meer budget op dezelfde pagina is geld verbranden. Nozzle Up bewees dat 19% haalbaar is met hetzelfde account en dezelfde pixel. Draai `/funnel-diagnose` met PostHog scroll depth en CTA click data om te zien waar bezoekers afhaken.

**3. Herstart volgens 70-20-10, niet met een schone lei**
Er ligt €4.867 aan learnings in dit account. Gooi dat niet weg met een nieuwe duplicatie.
- **70% budget:** hook H13 in de originele "BATCH 2: Expertise & POC" adset structuur, dat is de bewezen traffic winnaar. Plus H11 als tweede, de enige hook die überhaupt aankopen produceerde.
- **20% variaties:** H15 (4,3% CTR, €0,15 CPC) is de sterkste runner up, maak daar 2 tot 3 varianten van met een andere opening.
- **10% experiment:** nieuwe hooks. Statisch (SYBB w/ Semp BLACK) is al getest en werkt niet, blijf bij video.

**4. Archiveer de Kopie campagne**
Duplicaties met "Kopie" in de naam presteren structureel slechter in dit account. Alle drie de Kopie adsets in de hoofdcampagne hebben een hogere CPC dan hun origineel (€0,67 vs €0,25, €0,63 vs €0,07, €0,40 vs €0,31). Werk in bestaande adsets verder in plaats van te dupliceren.

**5. Zet het account niet aan zonder budgetplan**
Maart 2026 draaide op CPC €0,13, april op €0,56. Dat is een verviervoudiging binnen één maand. Zoek uit wat er in april is veranderd (nieuwe adsets, audience, seizoen) voordat je opnieuw €1.000 per maand inzet.

---

## Google Sheet
Overgeslagen op verzoek. Er is niet naar de Meta Ads Tracker geschreven. Dit rapport staat lokaal opgeslagen in `Output/Reports/Daily/2026-08-04_ads_report.md`.

---

*Gegenereerd met `/ads-report` op 4 augustus 2026. Databron: Meta Ads MCP (Pipeboard). Geen Google MCP calls uitgevoerd.*
