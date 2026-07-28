# Auto-Optimize Rapport, 28 juli 2026

**Account:** Sempertex Ad Account (act_567892422940728)
**Periode kill-regels:** last_3d (25 t/m 27 juli 2026)
**Databronnen:** Meta Ads MCP (Pipeboard). Geen Google MCP's gebruikt, geen schrijfactie naar de Tracker Sheet.

---

## Samenvatting

**Er zijn geen actieve Meta Ads campagnes.** Alle 5 campagnes in het account staan op PAUSED. Spend over de afgelopen 3 dagen: €0,00. Ook over de afgelopen 90 dagen is er geen enkele impressie of euro spend geregistreerd.

Gevolg: de kill-regels en de 70-20-10 classificatie zijn niet van toepassing. Er is niets om automatisch te pauzeren en niets om budget over te herverdelen.

### Accountstatus

| Campagne | Status | Daily budget | Laatst gewijzigd |
|---|---|---|---|
| 2026: SYBB - Kopie | PAUSED | geen (CBO uit) | 20 apr 2026 |
| 2026: SYBB | PAUSED | €100,00 | 19 apr 2026 |
| Last push Nozzle Up | PAUSED | geen | 21 sep 2025 |
| Nozzle Up END OF AUGUST | PAUSED | €70,00 | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | PAUSED | €30,00 | 15 sep 2025 |

Laatste activiteit in het account: 20 april 2026. De ads staan dus ruim drie maanden stil.

**Tweede account:** `act_607231713057715` is niet bereikbaar met de huidige Pipeboard token. De token geeft toegang tot `act_567892422940728` (Sempertex) en `act_1489853856181844` (AmbitionAvenue, 0 campagnes, €0 lifetime spend). Als act_607231713057715 daadwerkelijk bestaat en gecheckt moet worden, moet die toegevoegd worden aan de Pipeboard connectie.

---

## Automatische acties uitgevoerd

Geen. Er zijn 0 actieve ads, dus geen enkele kill-regel kan triggeren.

| Regel | Drempel | Getriggerd |
|---|---|---|
| Lage Link CTR | < 0,8% bij ≥ 1.000 impressions | Nee, geen data |
| Hoge CPC (link) | > €1,50 bij ≥ 500 link clicks | Nee, geen data |

**Totaal gepauzeerd: 0 ads**

---

## Waarschuwingen

| Signaal | Waarde | Actie aanbevolen |
|---|---|---|
| Account volledig inactief | 0 spend sinds ± 20 april 2026 | Beslissen: heractiveren of bewust dark laten |
| Pixel leert niet meer | 99 dagen zonder conversie-events uit ads | Bij herstart 5 tot 7 dagen learning phase inplannen |
| Tweede account onbereikbaar | act_607231713057715 geen toegang | Token-scope in Pipeboard uitbreiden of ID corrigeren |
| Vorige twee rapporten leeg | 26 en 27 juli output bevat "Not logged in · Please run /login" | Scheduled run draait zonder geldige sessie, zie onderaan |

---

## 70-20-10 Classificatie

Niet toepasbaar. Er zijn geen actieve ads te classificeren.

**Budget mismatch:** Niet van toepassing. Totaal actief dagbudget is €0,00.

---

## Referentie: laatste bekende performance per campagne (lifetime)

Ter voorbereiding op een herstart. Alle metrics op **link basis** berekend uit `actions.link_click`, niet op Meta's all-clicks velden.

| Campagne | Spend | Impressies | Link clicks | Link CTR | CPC (link) | All Clicks CTR | ROAS |
|---|---|---|---|---|---|---|---|
| 2026: SYBB | €2.485,04 | 297.174 | 10.851 | 3,7% | €0,23 | 4,1% | 17,8x* |
| Last push Nozzle Up | €800,78 | 109.869 | 2.034 | 1,9% | €0,39 | 2,5% | 0,8x |
| Campagne Nozzle Up 2025 1 | €853,19 | 129.558 | 1.836 | 1,4% | €0,46 | 2,5% | 8,3x |
| 2026: SYBB - Kopie | €124,42 | 7.615 | 125 | 1,6% | €1,00 | 2,6% | geen purchases |
| Nozzle Up END OF AUGUST | €604,03 | 369.136 | 2.573 | 0,7% | €0,23 | 1,0% | 6,4x |
| **Totaal** | **€4.867,46** | **913.352** | **17.419** | **1,9%** | **€0,28** | **2,4%** | |

\* De purchase value van €44.247 op 6 purchases in de SYBB campagne is vrijwel zeker een trackingartefact (gemiddelde orderwaarde €7.374). Ook de complete_registration value van €86.100 op 6 registraties klopt niet. Behandel de ROAS van deze campagne als onbetrouwbaar tot de pixel value-mapping gecontroleerd is.

### Wat dit zegt over de drempelwaarden

Het verschil tussen link en all-clicks is precies zoals verwacht bij de herziening van 13 april: de all-clicks CTR ligt gemiddeld 1,3x hoger dan de Link CTR (2,4% versus 1,9%). Op accountniveau zou geen enkele campagne op de nieuwe €1,50 CPC-drempel zijn gesneuveld, maar "Nozzle Up END OF AUGUST" met een Link CTR van 0,7% zou wel onder de 0,8% drempel zijn gevallen terwijl de all-clicks CTR van 1,0% nog acceptabel leek. De nieuwe drempels doen dus wat ze moeten doen.

De enige echte kill-kandidaat op CPC is "2026: SYBB - Kopie" met €1,00 per link click, maar die haalt de minimum van 500 link clicks niet (125 clicks) en valt dus buiten de regel. Terecht gepauzeerd geweest op basis van CPM (€16,34, ruim boven de €15 waarschuwingsdrempel).

---

## Voorstellen (wacht op goedkeuring)

Bij nul actieve ads zijn budget-herverdelingen en audience-aanpassingen zinloos. Deze drie voorstellen gaan over herstart en over het systeem zelf.

**1. Fix de scheduled run (hoogste prioriteit)**
De rapporten van 26 en 27 juli bevatten alleen "Not logged in · Please run /login". De geautomatiseerde /ads-auto-optimize draait dus al twee dagen zonder geldige sessie en zou ook geen ads hebben kunnen pauzeren als die wel actief waren geweest.
- Actie: check de auth van de scheduled task en voeg een guard toe die faalt met een expliciete foutmelding in plaats van de outputfile te overschrijven met een loginprompt.
- Verwachte impact: het verschil tussen een automatisering die werkt en een die stilletjes niets doet.

**2. Herstartplan SYBB met winnende hook-basis**
Als de ads weer aan gaan, is "2026: SYBB" de logische basis: 3,7% Link CTR en €0,23 CPC (link) over 297k impressies is ver boven de Core-drempel van 1,5% Link CTR / €0,50 CPC.
- Actie: herstart met €50 per dag in plaats van de oude €100, om de learning phase te doorlopen zonder groot risico. Na 5 tot 7 dagen opschalen als Link CTR boven 2,5% blijft.
- Voorwaarde: eerst voorstel 3 afhandelen, anders stuurt de campagne op vervuilde conversiedata.

**3. Pixel value-mapping controleren voor herstart**
De purchase- en registration-waarden in de SYBB campagne zijn niet plausibel. Als de campagne op OUTCOME_SALES met value optimisation herstart terwijl de pixel foute bedragen doorstuurt, optimaliseert Meta richting ruis.
- Actie: verifieer op startyourballoonbusiness.com welk bedrag het Purchase event meestuurt en of het CompleteRegistration event überhaupt een waarde hoort te hebben.
- Verwachte impact: betrouwbare ROAS-rapportage en correcte biedoptimalisatie vanaf dag 1.

---

## Openstaand: 70-20-10 drempels

De classificatiedrempels in het command staan nog gekalibreerd op all-clicks metrics (zie TODO in `.claude/skills/ads-auto-optimize`). Op basis van de lifetime data hierboven een voorstel voor link-gebaseerde drempels, ter goedkeuring:

| Categorie | Huidige richtlijn | Voorstel op basis van accountdata |
|---|---|---|
| Core | Link CTR > 1,5% en CPC (link) < €0,50 | Link CTR > 2,5% en CPC (link) < €0,35 |
| Emerging | Link CTR 0,8 tot 1,5% of CPC €0,50 tot €0,80 | Link CTR 1,2 tot 2,5% of CPC €0,35 tot €0,70 |
| Experimental | < 500 impressies | ongewijzigd |

Onderbouwing: de accountmediaan ligt op 1,6% Link CTR en €0,39 CPC (link). Met de huidige drempels zou de helft van de historische campagnes als Core kwalificeren, wat de categorie betekenisloos maakt. De voorgestelde waarden houden alleen de echte uitschieters over, in de praktijk de SYBB campagne.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

---

*Gegenereerd: 28 juli 2026. Geen automatische wijzigingen doorgevoerd in het ad account.*
