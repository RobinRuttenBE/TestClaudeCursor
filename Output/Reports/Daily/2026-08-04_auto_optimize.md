# Auto-Optimize Rapport, 4 augustus 2026

**Run:** 2026-08-04, Meta Ads MCP (Pipeboard) only. Geen Google MCP calls, geen schrijfactie naar de tracker Sheet.
**Accounts:** `act_567892422940728` (primair), `act_1489853856181844` (leeg).

---

## Samenvatting

**Er is niets te optimaliseren, want er draait niets.** Alle 5 campagnes in het Sempertex account staan op PAUSED. Nul impressions en nul spend in de laatste 3, 30 én 90 dagen. Geen enkele kill-regel kan vuren, want er is geen live ad.

Wat dit rapport wél doet: de historische ads doorrekenen op **link metrics** in plaats van all-clicks, zodat er een gekalibreerde startpositie ligt op het moment dat de campagne weer aan gaat.

### Data-beperkingen

- `act_607231713057715` is **niet toegankelijk** met de huidige Pipeboard token. Toegestaan zijn alleen `act_1489853856181844` en `act_567892422940728`. Als daar iets draait, zit het niet in dit rapport.
- `act_1489853856181844` bevat nul campagnes.
- Alle cijfers hieronder zijn **lifetime** (13 jan 2026 tot heden), niet last_3d. Last_3d is leeg.

---

## ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd. Er zijn nul actieve ads.**

| Regel | Drempel | Kandidaten | Actie |
|-------|---------|-----------|-------|
| Lage Link CTR | < 0,8% bij ≥ 1.000 impressions | 0 actieve ads | Niet van toepassing |
| Hoge CPC (link) | > €1,50 bij ≥ 500 link clicks | 0 actieve ads | Niet van toepassing |

**Totaal gepauzeerd: 0 ads.**

---

## ⚠️ Waarschuwingen

Geen live waarschuwingen, want er is geen delivery. De frequency- en CPM-signalen hieronder zijn historisch en gelden pas weer bij herstart.

| Ad | Ad set | Signaal | Waarde | Beoordeling |
|----|--------|---------|--------|-------------|
| Alle ads | Alle | Creative fatigue | Freq 1,45 tot 1,95 | Ruim onder 3,5. Geen fatigue. |
| H11, B3, CTA5 | Kopie 1 | Dure reach | CPM €13,51 | Onder €15, maar 2,1x het origineel |
| H13,B3,CTA5 | Kopie 3 | Dure reach | CPM €12,35 | Onder €15, maar 1,8x het origineel |
| H13,B3,CTA5 | Kopie 3 | **Verdachte conversiewaarde** | €42.773,50 | Zie waarschuwing hieronder |

### Kritiek: de ROAS-data is niet bruikbaar als stuurmiddel

Ad `H13,B3,CTA5` in Kopie 3 rapporteert €42.773,50 conversiewaarde op €206,99 spend. Dat is een ROAS van 206x vanaf een starter landingspagina. Vrijwel zeker een pixelfout (waarde in centen, of verkeerd ordertotaal doorgegeven).

**Waarom dit hier uitmaakt:** de 70-20-10 regel promoveert elke ad met ROAS > 2x automatisch naar Core. Deze ad heeft een Link CTR van 1,2% en een CPC (link) van €1,06, dus objectief zwak, maar zou puur op de kapotte ROAS het grootste budget krijgen. **Zet geen budget op ROAS tot de pixel geverifieerd is.**

---

## 📊 70-20-10 Classificatie (lifetime, link metrics)

Alle berekeningen op `actions.link_click`, niet op Meta's `clicks`/`ctr`/`cpc` velden.

### 70% Core, bewezen winners

| Ad | Ad set | Spend | Impressions | Link clicks | Link CTR | CPC (link) |
|----|--------|-------|------------|-------------|----------|-----------|
| H13,B3,CTA5 | BATCH 2: Expertise & POC | €421,29 | 60.074 | 6.342 | **10,6%** | **€0,07** |
| H15,B3,CTA5 | BATCH 2: Expertise & POC | €218,96 | 34.299 | 1.403 | 4,1% | €0,16 |
| H14,B3,CTA5 | BATCH 2: Expertise & POC | €232,36 | 33.235 | 760 | 2,3% | €0,31 |
| H11, B3, CTA5 | BATCH 2: Expertise & POC | €202,48 | 31.060 | 684 | 2,2% | €0,30 |

Alle vier halen Link CTR > 1,5% én CPC (link) < €0,50. H13 is de uitschieter: 2,6x de Link CTR van de nummer twee en een CPC (link) die 4,4x lager ligt dan de op één na beste.

### 20% Emerging, potentieel

| Ad | Ad set | Spend | Impressions | Link clicks | Link CTR | CPC (link) |
|----|--------|-------|------------|-------------|----------|-----------|
| H12,B3,CTA5 | BATCH 2: Expertise & POC | €388,40 | 48.166 | 696 | 1,4% | €0,56 |
| H12,B3,CTA5 | Kopie 2 | €141,43 | 13.955 | 174 | 1,2% | €0,81 |
| H15,B3,CTA5 | Kopie 4 | €49,83 | 4.737 | 57 | 1,2% | €0,87 |

### 10% Experimental / onder de maat

| Ad | Ad set | Spend | Impressions | Link clicks | Link CTR | CPC (link) |
|----|--------|-------|------------|-------------|----------|-----------|
| H13,B3,CTA5 | Kopie 3 | €206,99 | 16.766 | 195 | 1,2% | €1,06 |
| H11, B3, CTA5 | Kopie 1 | €521,56 | 38.614 | 428 | 1,1% | €1,22 |
| SYBB w/ Semp (BLACK) | Ad Set SYBB test set STATISCH | €101,74 | 16.268 | 112 | **0,7%** | €0,91 |

**Budget mismatch: ja, en fors.** Historisch ging €919,81 (37,0% van de €2.485,04 totale spend) naar de vier Kopie-ads plus de statische test. Die groep haalde samen 966 link clicks. De vier Core ads kregen €1.075,09 (43,3%) en haalden 9.189 link clicks. Bijna even veel budget, 9,5x minder resultaat.

### Wat de kill-regels zouden doen bij herstart as-is

| Ad | Regel | Waarde | Uitkomst |
|----|-------|--------|----------|
| SYBB w/ Semp (BLACK) | Link CTR < 0,8% bij ≥ 1.000 imp | 0,7% bij 16.268 imp | **Zou pauzeren** |
| H11, B3, CTA5 (Kopie 1) | CPC (link) > €1,50 bij ≥ 500 lc | €1,22 bij 428 lc | Haalt drempel niet, en 428 lc < 500 minimum |
| Overige 8 ads | Beide | Binnen drempels | Blijven actief |

Slechts 1 van de 10 ads triggert een kill-regel. Dat bevestigt het beeld uit het dagrapport: **het probleem zit niet in de ads, het zit na de klik.** H13 leverde 6.342 link clicks voor €0,07 per stuk en daaruit kwam nul checkout.

---

## 💡 Voorstellen (wacht op goedkeuring)

Niveau 2 acties. Geen hiervan is uitgevoerd.

### 1. Verifieer de pixel voordat er budget aan gaat

- **Actie:** controleer de conversiewaarde die de pixel doorgeeft op de SYBB checkout, specifiek de 2 aankopen goed voor €42.773,50 op `H13,B3,CTA5` (Kopie 3, ad id `120242894133350239`).
- **Reden:** €21.386 per aankoop op een starter workshop is niet reëel. Zolang dit erin zit is elke ROAS-gestuurde beslissing ruis, en Meta's eigen optimalisatie ook.
- **Verwachte impact:** maakt de Core-classificatie betrouwbaar. Zonder fix promoveert de 70-20-10 regel de zwakste ad naar het hoogste budget.

### 2. Herstart selectief, niet de hele campagne

Bij het weer aanzetten van `2026: SYBB` (daily budget staat op €100,00):

| Categorie | Ads | Voorstel budget/dag | Aandeel |
|-----------|-----|--------------------|---------|
| Core | H13, H15, H14, H11 (originelen, BATCH 2) | €70,00 | 70% |
| Emerging | H12 origineel + 1 nieuwe variant op H13 | €20,00 | 20% |
| Experimental | 1 nieuwe hook | €10,00 | 10% |

- **Niet herstarten:** de vier Kopie-adsets en `Ad Set SYBB test set STATISCH`. De Kopie-adsets hebben structureel 2x tot 9x hogere CPC (link) bij identieke creative, puur door opnieuw te moeten leren. Statisch haalt 0,7% Link CTR en zou direct gepauzeerd worden.
- **Verwachte impact:** op basis van de historische blended CPC (link) van de Core-groep (€0,12) levert €70,00/dag ongeveer 583 link clicks per dag, tegen ongeveer 66 per dag als het budget verdeeld blijft zoals het was.

### 3. Fix de landingspagina eerst

- **Actie:** zet de campagne niet aan tot de landingspagina conversie meetbaar boven 0,5% ligt.
- **Reden:** H13 kocht 6.342 bezoekers voor €0,07 per stuk, uitstekend, met nul checkouts als resultaat. Nozzle Up haalde 19,0% bezoeker naar checkout met dezelfde pixel. Target uit de KPI-tabel is > 5%.
- **Verwachte impact:** dit is de enige hefboom die orde van grootte uitmaakt. De ads zijn al goedkoop genoeg.

### 4. Nieuwe variaties op de winnende hook

Gebaseerd op `H13,B3,CTA5`, Link CTR 10,6%, CPC (link) €0,07. Dat is 2,6x de nummer twee, dus dit is de hook om op door te bouwen. Concrete hook-teksten volgen uit de 7 Hormozi hook types en `sybb-8-pillars.md`, maar de formatkeuze staat nu al vast:

- **Variatie A:** zelfde hook, andere CTA. Blijf bij video, statisch is getest en haalde 0,7% Link CTR.
- **Variatie B:** zelfde hook, kortere edit onder de 15 seconden.
- **Variatie C:** zelfde hook, andere body en dezelfde opening.

Deze drie horen in de 20% Emerging bucket, niet in Core, tot ze eigen data hebben.

### 5. Kalibreer de 70-20-10 drempels

De drempels in het command staan gemarkeerd als TODO: ze zijn gekalibreerd op all-clicks en nooit herzien voor link metrics. Deze dataset geeft nu een echte basis:

| Categorie | Huidige drempel | Voorstel op basis van deze data |
|-----------|----------------|--------------------------------|
| Core | Link CTR > 1,5% én CPC (link) < €0,50 | Ongewijzigd. Splitst de set zuiver: 4 originelen erboven, alle Kopieën eronder. |
| Emerging | Link CTR 0,8 tot 1,5% of CPC €0,50 tot €0,80 | Verruim CPC-band naar €0,50 tot €0,90, anders vallen Kopie 2 en 4 ten onrechte uit |
| ROAS > 2x als Core-criterium | Actief | **Opschorten** tot de pixel geverifieerd is |

---

## Volgende stap

De logische vervolgcheck is PostHog: staat er nog verkeer op startyourballoonbusiness.com, en is de conversie na de klik verbeterd sinds april? Dat bepaalt of voorstel 3 al afgevinkt kan worden. Niet meegenomen in deze run.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

---

*Gegenereerd 2026-08-04 via `/ads-auto-optimize`. Bron: Meta Ads MCP (Pipeboard), account `act_567892422940728`, lifetime insights per ad. Link CTR = `actions.link_click / impressions`. CPC (link) = `spend / actions.link_click`. Meta's `clicks`, `ctr` en `cpc` velden zijn niet gebruikt.*
