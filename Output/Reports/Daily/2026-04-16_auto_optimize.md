# Auto-Optimize Rapport — 2026-04-16

**Campagne:** 2026: SYBB (act_567892422940728)
**Periode:** last 3d (2026-04-13 t/m 2026-04-15)
**Dagbudget:** EUR 100,00 (CBO)
**Timestamp:** 2026-04-16

> Account `act_607231713057715` niet toegankelijk via huidige token. Analyse beperkt tot `act_567892422940728`.

---

## Campagne Totalen (last 3d)

| Metric | Waarde |
|--------|--------|
| Impressions | 23.041 |
| Reach | 12.541 |
| Link clicks | 249 |
| All clicks | 484 |
| Spend | EUR 311,19 |
| Link CTR | 1,1% |
| All Clicks CTR | 2,1% |
| CPC (link) | EUR 1,25 |
| CPC (all) | EUR 0,64 |
| CPM | EUR 13,51 |
| Frequency | 1,84 |
| Purchases | 4 |
| Purchase value | EUR 1.473,50 |
| ROAS | 4,74x |

---

## Ad-niveau Performance (last 3d)

| Ad | Ad Set | Impressions | Link Clicks | Spend | Link CTR | CPC (link) | Purchases | ROAS | Freq | CPM |
|----|--------|-------------|-------------|-------|----------|------------|-----------|------|------|-----|
| H11, B3, CTA5 | Kopie 1 | 14.976 | 153 | EUR 203,89 | 1,02% | EUR 1,33 | 4 | 7,23x | 1,56 | EUR 13,61 |
| H12,B3,CTA5 | Kopie 2 | 2.002 | 26 | EUR 29,50 | 1,30% | EUR 1,13 | 0 | 0,00x | 1,96 | EUR 14,74 |
| H13,B3,CTA5 | Kopie 3 | 5.341 | 62 | EUR 68,76 | 1,16% | EUR 1,11 | 0 | 0,00x | 1,41 | EUR 12,87 |

> **Nota:** Link CTR en CPC (link) zijn berekend op `actions.link_click`, NIET op Meta's `ctr`/`cpc` velden (die all-clicks meten). All Clicks CTR lag campagnebreed op 2,1% vs. Link CTR 1,1%, wat de ~2x inflatie bevestigt.

---

## Automatische acties uitgevoerd

**Geen ads gepauzeerd. Alles presteert boven de drempelwaarden.**

### Kill-regel check:

| Ad | Regel | Waarde | Drempel | Min. data | Status |
|----|-------|--------|---------|-----------|--------|
| H11, B3, CTA5 | Link CTR | 1,02% | < 0,8% | 14.976 imp (>= 1.000) | PASS |
| H11, B3, CTA5 | CPC (link) | EUR 1,33 | > EUR 1,50 | 153 link clicks (< 500 min) | SKIP (te weinig data) |
| H12,B3,CTA5 | Link CTR | 1,30% | < 0,8% | 2.002 imp (>= 1.000) | PASS |
| H12,B3,CTA5 | CPC (link) | EUR 1,13 | > EUR 1,50 | 26 link clicks (< 500 min) | SKIP (te weinig data) |
| H13,B3,CTA5 | Link CTR | 1,16% | < 0,8% | 5.341 imp (>= 1.000) | PASS |
| H13,B3,CTA5 | CPC (link) | EUR 1,11 | > EUR 1,50 | 62 link clicks (< 500 min) | SKIP (te weinig data) |

> Geen enkele ad triggert een kill-regel. CPC (link) check is voor alle 3 ads overgeslagen wegens onvoldoende link clicks (< 500 minimum).

---

## Waarschuwingen

| Ad | Signaal | Waarde | Drempel | Actie aanbevolen |
|----|---------|--------|---------|-----------------|
| H12,B3,CTA5 | CPM nadert limiet | EUR 14,74 | EUR 15,00 | Monitor. Audience mogelijk te smal in Kopie 2 |
| H12,B3,CTA5 | Weinig data | 2.002 imp / 26 link clicks | n.v.t. | Meer tijd geven, Meta CBO geeft weinig budget |
| H13,B3,CTA5 | Geen conversies | 0 purchases bij EUR 68,76 spend | n.v.t. | Monitor nog 3-5 dagen. Bij EUR 150+ spend zonder purchase: heroverweeg |

> Frequency, creative fatigue en Link CTR decline: niet van toepassing. Alle ads zijn pas ~7 dagen oud (aangemaakt 2026-04-09), frequency onder 2,0 voor alle ads.

---

## 70-20-10 Classificatie

> **Let op:** Drempels zijn RICHTLIJN (oorspronkelijk gekalibreerd op all-clicks, nu toegepast op link metrics). Bij twijfel wordt gerapporteerd maar niet geacteerd.

### 70% Core (budget: EUR 67,96/dag, huidig 67,5% van totaal)

| Ad | Link CTR | CPC (link) | ROAS | Reden |
|----|----------|------------|------|-------|
| H11, B3, CTA5 | 1,02% | EUR 1,33 | 7,23x | ROAS > 2x (4 purchases, EUR 1.473,50 waarde) |

H11 is de duidelijke winnaar. Alle 4 purchases komen van deze ad. ROAS van 7,23x is uitstekend. Meta's CBO alloceert al ~68% van het budget hieraan.

### 20% Emerging (budget: EUR 32,75/dag, huidig 32,5% van totaal)

| Ad | Link CTR | CPC (link) | ROAS | Reden |
|----|----------|------------|------|-------|
| H12,B3,CTA5 | 1,30% | EUR 1,13 | 0,00x | Hoogste Link CTR, maar 0 purchases. Slechts EUR 29,50 spend, te weinig data |
| H13,B3,CTA5 | 1,16% | EUR 1,11 | 0,00x | Goede Link CTR, 0 purchases. EUR 68,76 spend, begint significanter te worden |

Beide ads tonen goede Link CTR (boven de 0,8% kill-drempel en in de 0,8-1,5% emerging range). Geen van beide heeft nog een purchase. H12 heeft opvallend de hoogste Link CTR (1,30%) maar krijgt het minste budget van Meta CBO.

### 10% Experimental (budget: EUR 0,00/dag, huidig 0,0% van totaal)

Geen experimentele ads actief. Alle 3 ads gebruiken dezelfde body (B3) en CTA (CTA5) structuur met verschillende hooks (H11, H12, H13).

### Budget alignment

| Categorie | Ideaal | Huidig | Delta |
|-----------|--------|--------|-------|
| Core (H11) | 70% | 67,5% | -2,5% (goed aligned) |
| Emerging (H12+H13) | 20% | 32,5% | +12,5% (iets boven ideaal) |
| Experimental | 10% | 0,0% | -10,0% (geen experimentele ads) |

**Budget mismatch:** Mild. Meta CBO doet het werk goed door H11 het leeuwendeel te geven. De emerging ads krijgen iets meer dan ideaal (32,5% vs 20%), maar dat is logisch omdat CBO ze nog test. Geen experimentele ads actief, wat een gemiste kans is voor de 10% test-bucket.

---

## Voorstellen (wacht op goedkeuring)

### 1. Budget: geen actie nodig

Meta CBO verdeelt het budget al effectief. H11 krijgt ~68% (dicht bij 70% ideaal). Handmatig ingrijpen in CBO verdeling is hier niet aangeraden.

### 2. Nieuwe variaties (experimentele bucket vullen)

Er draait momenteel 0% experimenteel budget. Om de 70-20-10 regel te volgen:

**Gebaseerd op winnende hook H11 (Link CTR 1,02%, ROAS 7,23x):**
- Variatie A: H11 met andere body (B1 of B2) en zelfde CTA5. Test of de body impact heeft op conversie.
- Variatie B: H11 met andere CTA (CTA1, CTA2, of CTA3). Test of een andere call-to-action de conversieratio verbetert.

**Gebaseerd op H12 (hoogste Link CTR 1,30%):**
- Variatie C: H12 met body B1 of B2. Als de hook de hoogste doorklikratio levert, is het interessant om te testen of een andere body tot conversies leidt.

> Start elk als nieuwe ad in een bestaande ad set (of aparte test ad set) met beperkt budget. Laat minimaal 1.000 impressions draaien voor beoordeling.

### 3. Audience aanpassingen

Geen dringende aanpassingen nodig:
- Targeting is breed (18-65, NL/BE/LU/DE) met Advantage Audience aan
- Frequency is laag (max 1,96) wat wijst op voldoende audience headroom
- CPM van H12 (EUR 14,74) nadert de EUR 15 grens, maar dit kan ook aan lagere relevance score liggen i.p.v. audience saturatie

**Optioneel:** Overweeg om een ad set te maken met specifiekere targeting (bijv. 25-45, interest in "balloon decoration" of "event planning") als tegenhanger van de brede Advantage Audience sets. Dit kan als experimentele bucket dienen.

### 4. Observaties en aandachtspunten

- **H11 is verantwoordelijk voor 100% van de purchases.** Als deze ad vermoeidheidssignalen gaat tonen, heb je geen backup converter. Prioriteit: variaties van H11 creeren.
- **H13 heeft EUR 68,76 gespend zonder purchase.** Nog niet alarmerend, maar als dit bij EUR 150+ spend nog steeds 0 purchases is, overweeg pauzeren.
- **Alle ads gebruiken dezelfde B3/CTA5 combinatie.** Dit maakt het moeilijk om te bepalen of de hook of de body/CTA de conversie-driver is. Test met andere body/CTA combinaties zou dit onthullen.
- **Link CTR vs All Clicks CTR inflatie:** campagnebreed 1,1% vs 2,1% (~1,9x). Dit bevestigt waarom kill-regels op link metrics moeten draaien.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**
