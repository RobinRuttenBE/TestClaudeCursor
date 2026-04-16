# Auto-Optimize Rapport - 2026-04-16

**Account:** Sempertex Ad Account (`act_567892422940728`)
**Campagne:** 2026: SYBB (ID: `120239435987290239`)
**Periode:** last 3 days (2026-04-13 t/m 2026-04-15)
**Dagbudget campagne:** €100,00 (CBO)
**Tweede account** (`act_607231713057715`): niet beschikbaar met huidig API token, overgeslagen.

---

## Campagne Totaal (last 3d)

| Metric | Waarde |
|--------|--------|
| Spend | €311,19 |
| Impressions | 23.041 |
| Reach | 12.541 |
| Frequency | 1,84 |
| Link Clicks | 249 |
| Link CTR | 1,08% |
| CPC (link) | €1,25 |
| All Clicks CTR | 2,10% |
| CPC (all) | €0,64 |
| CPM | €13,51 |
| Landing Page Views | 193 |
| Purchases | 4 |
| Purchase Value | €1.473,50 |
| ROAS | 4,74x |
| Cost per Purchase | €77,80 |

---

## Actieve Ads Overzicht (3 ads in 3 ad sets)

| Ad | Ad Set | Impressions | Link Clicks | Link CTR | CPC (link) | Spend | Purchases | ROAS |
|----|--------|------------|------------|----------|-----------|-------|-----------|------|
| H11, B3, CTA5 | Kopie 1 | 14.976 | 153 | 1,02% | €1,33 | €203,89 | 4 | 7,23x |
| H12, B3, CTA5 | Kopie 2 | 2.002 | 26 | 1,30% | €1,13 | €29,50 | 0 | 0,00x |
| H13, B3, CTA5 | Kopie 3 | 5.341 | 62 | 1,16% | €1,11 | €68,76 | 0 | 0,00x |

> **Nota:** Link CTR en CPC (link) zijn berekend op `actions.link_click`, NIET op Meta's `ctr`/`cpc` velden (die all-clicks meten). All Clicks CTR lag campagnebreed op 2,10% vs. Link CTR 1,08%, wat de ~2x inflatie bevestigt.

---

## Automatische acties uitgevoerd

**Geen ads gepauzeerd. Alle actieve ads presteren boven de kill-drempelwaarden.**

### Kill-regel 1: Link CTR < 0,8% (minimum 1.000 impressions)

| Ad | Impressions | Link CTR | Trigger? |
|----|------------|----------|----------|
| H11, B3, CTA5 | 14.976 | 1,02% | Nee |
| H12, B3, CTA5 | 2.002 | 1,30% | Nee |
| H13, B3, CTA5 | 5.341 | 1,16% | Nee |

### Kill-regel 2: CPC (link) > €1,50 (minimum 500 link clicks)

| Ad | Link Clicks | CPC (link) | Trigger? |
|----|------------|-----------|----------|
| H11, B3, CTA5 | 153 | €1,33 | Nee (< 500 link clicks minimum) |
| H12, B3, CTA5 | 26 | €1,13 | Nee (< 500 link clicks minimum) |
| H13, B3, CTA5 | 62 | €1,11 | Nee (< 500 link clicks minimum) |

**Let op:** Geen enkele ad heeft het minimum van 500 link clicks bereikt voor de CPC-regel. H11 nadert de €1,50 grens bij €1,33. Dit verdient aandacht de komende dagen.

---

## Waarschuwingen

| Ad / Ad Set | Signaal | Waarde | Drempel | Status |
|-------------|---------|--------|---------|--------|
| H11 (Kopie 1) | CPC (link) nadert grens | €1,33 | €1,50 | Monitor |
| H12 (Kopie 2) | CPM nadert grens | €14,74 | €15,00 | Monitor |
| H12 (Kopie 2) | Laag volume | 2.002 imp / 3d | - | Meta geeft weinig budget |

### Creative Fatigue Check (Frequency > 3,5)

| Ad Set | Frequency (3d) | Status |
|--------|---------------|--------|
| Kopie 1 (H11) | 1,56 | OK |
| Kopie 2 (H12) | 1,96 | OK |
| Kopie 3 (H13) | 1,41 | OK |

### Dure Reach Check (CPM > €15)

| Ad Set | CPM (3d) | Status |
|--------|---------|--------|
| Kopie 1 (H11) | €13,61 | OK |
| Kopie 2 (H12) | €14,74 | Bijna (98% van drempel) |
| Kopie 3 (H13) | €12,87 | OK |

### Dalende Link CTR Check (3d < 70% van lifetime)

| Ad | Link CTR (3d) | Link CTR (lifetime) | Ratio | Status |
|----|--------------|---------------------|-------|--------|
| H11, B3, CTA5 | 1,02% | 1,04% | 98,1% | OK, stabiel |
| H12, B3, CTA5 | 1,30% | 1,10% | 118,2% | OK, verbeterd |
| H13, B3, CTA5 | 1,16% | 1,14% | 101,8% | OK, stabiel |

---

## 70-20-10 Classificatie

> **Disclaimer:** deze drempels zijn nog gekalibreerd voor link metrics (update 2026-04-13). Bij twijfel: richtlijn, geen hard oordeel.

### 70% Core (budget: €203,89/3d = €67,96/dag, huidig 65,5% van totaal)

| Ad | Link CTR | CPC (link) | ROAS | Reden |
|----|----------|-----------|------|-------|
| H11, B3, CTA5 | 1,02% | €1,33 | 7,23x | ROAS > 2x. Enige ad met purchases (4 stuks, €1.473,50 waarde) |

H11 is de duidelijke revenue driver. Alle 4 purchases komen uit deze ad. ROAS van 7,23x is excellent. Link CTR en CPC (link) zijn niet best-in-class, maar de conversies compenseren ruim.

### 20% Emerging (budget: €98,26/3d = €32,75/dag, huidig 31,6% van totaal)

| Ad | Link CTR | CPC (link) | ROAS | Potentieel |
|----|----------|-----------|------|-----------|
| H12, B3, CTA5 | 1,30% | €1,13 | 0,00x | Hoogste Link CTR, laagste CPC (link). Nog geen conversies, maar sterkste engagement metrics. Verdient meer budget/tijd. |
| H13, B3, CTA5 | 1,16% | €1,11 | 0,00x | Solide Link CTR, laagste CPC (link). Lifetime toont 2 purchases (€42.773,50 waarde, mogelijke high-ticket attributie). Stabiele performer. |

### 10% Experimental (budget: €0,00/3d, huidig 0,0% van totaal)

Er zijn momenteel geen experimentele ads actief. Alle ads draaien al > 500 impressions.

### Budget Mismatch

| Categorie | Huidig % | Ideaal % | Delta |
|-----------|---------|---------|-------|
| Core (H11) | 65,5% | 70% | -4,5% |
| Emerging (H12+H13) | 31,6% | 20% | +11,6% |
| Experimental | 0,0% | 10% | -10,0% |

**Analyse:** De verdeling is redelijk gebalanceerd voor een CBO-campagne. Meta stuurt al het meeste budget naar H11 (de converter). De oververtegenwoordiging van Emerging (31,6% vs 20%) is acceptabel omdat er geen experimental ads zijn. Het ontbreken van experimental ads is het grootste aandachtspunt.

---

## Voorstellen (wacht op goedkeuring)

### 1. H11 CPC (link) bewaken

H11 zit op €1,33 CPC (link), 89% van de €1,50 kill-grens. Nog niet genoeg link clicks (153 < 500 minimum) om de kill-regel te activeren, maar als de trend aanhoudt wordt dit een probleem.

**Voorstel:** Geen directe actie. Dagelijks monitoren. Als CPC (link) boven €1,40 komt bij 300+ link clicks, overweeg dan een creative refresh voor H11 met dezelfde hook maar een ander format (bijv. carrousel i.p.v. video) om de CPC te drukken.

### 2. H12 verdient meer budget/runway

H12 heeft de beste engagement metrics (Link CTR 1,30%, CPC link €1,13) maar krijgt slechts 9,5% van het budget (€29,50 van €311,19). Dit is een CBO-effect: Meta stuurt budget naar H11 omdat die converteert.

**Voorstel:** Geef H12 een minimum ad set budget van €15/dag om te garanderen dat het voldoende data verzamelt voor een eerlijke vergelijking. Na 7 dagen evalueren of er conversies komen.

### 3. Experimentele ads toevoegen (10% budget)

Er draaien momenteel 0 experimentele ads. Volgens de 70-20-10 regel zou 10% van het budget (~€10/dag) naar nieuwe tests moeten gaan.

**Voorstel:** Lanceer 2 nieuwe ad variaties gebaseerd op winnende hooks:
- **Variatie A:** H12-hook (hoogste Link CTR) in een carrousel format i.p.v. video. Zelfde CTA5 en B3.
- **Variatie B:** H11-hook (meeste conversies) met een alternatieve CTA. Bijv. CTA6 ("Bekijk het programma") i.p.v. CTA5.
- Startbudget: minimaal €5/dag per ad in een apart ad set.

### 4. H13 lifetime purchase waarde controleren

H13 toont in lifetime data 2 purchases met een totale waarde van €42.773,50. Dit lijkt abnormaal hoog voor een SYBB workshop. Dit kan komen door:
- Correcte hoge-waarde attributie (bijv. corporate boeking)
- Meta pixel misfire of dubbeltelling
- View-through attributie op een onverwachte conversie

**Voorstel:** Controleer in de webshop backend of er daadwerkelijk 2 bestellingen van ~€21.000 zijn geweest die via H13 zijn binnengekomen. Als dit klopt, verdient H13 meer budget. Als het een tracking error is, moet het pixel gecontroleerd worden.

---

## Samenvatting

| Item | Status |
|------|--------|
| Ads gepauzeerd | 0 |
| Kill-regels getriggerd | 0 |
| Waarschuwingen | 2 (H11 CPC nadert grens, H12 CPM nadert grens) |
| Core ads | 1 (H11, ROAS 7,23x) |
| Emerging ads | 2 (H12, H13) |
| Experimental ads | 0 (aandachtspunt) |
| Totale ROAS campagne | 4,74x |

De campagne draait gezond. Geen ads hoeven gepauzeerd. De prioriteit is: (1) CPC (link) van H11 in de gaten houden, (2) H12 meer runway geven, (3) experimentele ads toevoegen, (4) H13 purchase waarde verifieren.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

*Rapport gegenereerd: 2026-04-16 | Data: Meta Ads MCP (Pipeboard) | Account: act_567892422940728*
