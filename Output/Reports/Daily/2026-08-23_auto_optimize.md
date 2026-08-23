# Auto-Optimize Rapport, 23 August 2026

**Account:** Sempertex Ad Account (`act_567892422940728`)
**Periode kill-regels:** last_3d (20 t/m 23 August 2026)
**Databron:** Meta Ads MCP (Pipeboard) via directe JSON-RPC. PostHog niet geraadpleegd, niet nodig voor dit command.
**Run timestamp:** 2026-08-23

---

## Samenvatting

Er is niets geoptimaliseerd, omdat er niets draait. Alle 5 campagnes in het account staan op PAUSED en er is 0 impressies en EUR 0,00 spend in de afgelopen 3, 30 en 90 dagen. De kill-regels kunnen dus per definitie niet triggeren.

Belangrijker dan het lege rapport is wat eronder zit: er staat een gepauzeerde campagne klaar met EUR 100,00 per dag aan actieve ad sets, gevuld met precies de zwakste creatives. Zie de waarschuwing hieronder.

---

## Automatische acties uitgevoerd

**Geen ads gepauzeerd.** Er zijn geen actief leverende ads om te beoordelen.

| Controle | Uitkomst |
|---|---|
| Ads met >= 1.000 impressies in last_3d | 0 |
| Ads met >= 500 link clicks in last_3d | 0 |
| Kill-regel Link CTR < 0,8% getriggerd | Niet van toepassing |
| Kill-regel CPC (link) > EUR 1,50 getriggerd | Niet van toepassing |

Conform de regel "minimaal 24 uur actief en voldoende data" is elke ad overgeslagen wegens ontbrekende data, niet wegens goede prestaties.

---

## Accountstatus

| Campagne | Status | Spend 2026 YTD | Impressies 2026 YTD |
|---|---|---|---|
| 2026: SYBB | PAUSED | EUR 2.485,04 | 297.174 |
| 2026: SYBB - Kopie | PAUSED | EUR 124,42 | 7.615 |
| Last push Nozzle Up | PAUSED | EUR 0,00 (2025: EUR 800,78) | 0 |
| Nozzle Up END OF AUGUST | PAUSED | EUR 0,00 (2025: EUR 604,03) | 0 |
| Campagne Nozzle Up 2025 1 | PAUSED | EUR 0,00 (2025: EUR 853,19) | 0 |

**Spend per maand 2026:**

| Maand | Spend |
|---|---|
| January | EUR 101,74 |
| February | EUR 0,00 |
| March | EUR 1.323,83 |
| April | EUR 1.183,89 |
| May t/m 23 August | EUR 0,00 |

Laatste levering was in April 2026. Het account ligt nu ongeveer vier maanden stil.

---

## Waarschuwingen

| Signaal | Detail | Actie aanbevolen |
|---|---|---|
| **Scherpe campagne klaar om te vuren** | Campagne "2026: SYBB - Kopie" is PAUSED, maar bevat 3 ACTIEVE ad sets met samen EUR 100,00 per dag budget, elk met 1 ACTIEVE ad | Controleer voor je de campagne ooit unpauset |
| **Budget staat op de zwakke varianten** | De 3 actieve ads scoorden historisch 1,5% tot 1,8% Link CTR. De winnaar met 10,6% Link CTR staat PAUSED | Herzie welke creatives actief staan |
| Geen creative fatigue meetbaar | Frequency niet te bepalen zonder levering | Geen |
| Geen CPM-signaal meetbaar | Geen impressies in de periode | Geen |

**Detail van de scherpe campagne:**

| Ad set | Status | Dagbudget | Actieve ad | Historische Link CTR |
|---|---|---|---|---|
| BATCH 2: Expertise & POC - Kopie 1 | ACTIVE | EUR 35,00 | H11, B3, CTA5 | 1,5% |
| BATCH 2: Expertise & POC - Kopie 3 | ACTIVE | EUR 45,00 | H13, B3, CTA5 | 1,7% |
| BATCH 2: Expertise & POC - Kopie 2 | ACTIVE | EUR 20,00 | H12, B3, CTA5 | 1,8% |

Zolang de campagne op PAUSED staat levert dit niets. Zet je de campagne aan, dan start er direct EUR 100,00 per dag op deze drie varianten.

---

## Historische performance (1 March t/m 30 April 2026)

Dit is de laatste periode met echte levering. Gebruikt als referentie, niet als basis voor automatische acties.

Alle metrics zijn link-gebaseerd: Link CTR = link_click / impressies, CPC (link) = spend / link_click.

| Ad | Ad set | Impressies | Link clicks | Spend | Link CTR | CPC (link) |
|---|---|---|---|---|---|---|
| H13, B3, CTA5 | BATCH 2: Expertise & POC | 60.074 | 6.342 | EUR 421,29 | 10,6% | EUR 0,07 |
| H15, B3, CTA5 | BATCH 2: Expertise & POC | 34.299 | 1.403 | EUR 218,96 | 4,1% | EUR 0,16 |
| H14, B3, CTA5 | BATCH 2: Expertise & POC | 33.235 | 760 | EUR 232,36 | 2,3% | EUR 0,31 |
| H11, B3, CTA5 | BATCH 2: Expertise & POC | 31.060 | 684 | EUR 202,48 | 2,2% | EUR 0,30 |
| H12, B3, CTA5 | Kopie 2 | 1.367 | 25 | EUR 25,87 | 1,8% | EUR 1,03 |
| H13, B3, CTA5 | Kopie 3 | 2.466 | 42 | EUR 47,21 | 1,7% | EUR 1,12 |
| H11, B3, CTA5 | Kopie 1 | 3.782 | 58 | EUR 51,34 | 1,5% | EUR 0,89 |
| H12, B3, CTA5 | BATCH 2: Expertise & POC | 48.166 | 696 | EUR 388,40 | 1,5% | EUR 0,56 |
| H12, B3, CTA5 | Kopie 2 | 13.955 | 174 | EUR 141,43 | 1,2% | EUR 0,81 |
| H15, B3, CTA5 | Kopie 4 | 4.737 | 57 | EUR 49,83 | 1,2% | EUR 0,87 |
| H13, B3, CTA5 | Kopie 3 | 16.766 | 195 | EUR 206,99 | 1,2% | EUR 1,06 |
| H11, B3, CTA5 | Kopie 1 | 38.614 | 428 | EUR 521,56 | 1,1% | EUR 1,22 |

**Totaal:** 288.521 impressies, 10.864 link clicks, EUR 2.507,72 spend, Link CTR 3,8%, CPC (link) EUR 0,23.

Twee dingen springen eruit. H13 in de originele ad set haalde 10,6% Link CTR tegen EUR 0,07 per link click, ruim een factor 2,5 boven de op een na beste ad. En dezelfde hook H13 in "Kopie 3" haalde slechts 1,2%, dus het verschil zit niet in de hook alleen maar in de combinatie van ad set en targeting.

---

## 70-20-10 Classificatie

De drempels in het command zijn nog niet gekalibreerd voor link metrics, zie de TODO in `.claude/commands`. Onderstaande indeling is dus een richtlijn op historische data. Er worden geen budget-shifts uitgevoerd.

**Core, bewezen winners (Link CTR > 1,5% en CPC (link) < EUR 0,50):**
- H13, B3, CTA5 (BATCH 2: Expertise & POC), Link CTR 10,6%, CPC (link) EUR 0,07
- H15, B3, CTA5 (BATCH 2: Expertise & POC), Link CTR 4,1%, CPC (link) EUR 0,16
- H14, B3, CTA5 (BATCH 2: Expertise & POC), Link CTR 2,3%, CPC (link) EUR 0,31
- H11, B3, CTA5 (BATCH 2: Expertise & POC), Link CTR 2,2%, CPC (link) EUR 0,30

**Emerging, potentieel:**
- H12, B3, CTA5 (BATCH 2: Expertise & POC), Link CTR 1,5%, CPC (link) EUR 0,56

**Experimental of onder de maat:**
- Alle 7 varianten in de "Kopie" ad sets, Link CTR 1,1% tot 1,8%, CPC (link) EUR 0,81 tot EUR 1,22

**Budget mismatch: ja.** Op dit moment staat 100% van het klaargezette budget (EUR 100,00 per dag) op ads uit de onderste groep. De vier Core ads staan allemaal op PAUSED en krijgen 0%.

---

## Voorstellen (wacht op goedkeuring)

**1. Herstel de creative-selectie voor je herstart**

Zet in de campagne "2026: SYBB - Kopie" de actieve ads terug naar de bewezen varianten uit de originele ad set, of kopieer H13 en H15 uit "BATCH 2: Expertise & POC" naar de actieve ad sets.

Reden: de drie nu actieve ads presteerden historisch 1,5% tot 1,8% Link CTR tegen EUR 0,89 tot EUR 1,12 per link click. H13 haalde 10,6% tegen EUR 0,07. Verwachte impact: bij gelijk budget een factor 5 tot 10 meer link clicks.

**2. Budgetverdeling bij herstart**

Voorstel bij een herstart op EUR 100,00 per dag:
- H13 variant: van EUR 45,00 naar EUR 70,00 per dag
- H15 variant: van EUR 35,00 naar EUR 20,00 per dag
- H14 of H11 variant als test: van EUR 20,00 naar EUR 10,00 per dag

Reden: volgt de 70-20-10 verdeling met H13 als bewezen Core. Verwachte impact: hoogste volume link clicks per euro op basis van de March/April data.

**3. Onderzoek waarom dezelfde hook zo verschillend presteert**

H13 haalde 10,6% in de originele ad set en 1,2% in "Kopie 3". Zelfde hook, zelfde body, zelfde CTA. Het verschil zit dus in targeting, plaatsing of creative-asset.

Reden: als dit verschil begrepen is, is dat waardevoller dan welke nieuwe hook dan ook. Voorstel: vergelijk de targeting en placements van beide ad sets voor je herstart.

**4. Nieuwe variaties op de winnende hook**

Pas zinvol na een herstart met vers data. De hook achter H13 verdient 2 tot 3 varianten volgens de 70-20-10 regel, maar zonder actuele levering is elke nieuwe variant een gok op vier maanden oude data.

---

## Datakwaliteit en beperkingen

- De Pipeboard MCP meldde "requires authentication". Data is opgehaald via directe JSON-RPC calls, die wel werken. Zie de memory `reference-pipeboard-direct-http`.
- Het in het command genoemde account `act_607231713057715` bestaat niet. Het account overzicht toont alleen `act_567892422940728` (Sempertex, EUR 4.867,46 lifetime) en `act_1489853856181844` (AmbitionAvenue, EUR 0,00 spend, leeg). Advies: corrigeer dit account-ID in het command.
- De MCP-wrapper negeert de parameter `time_increment`, waardoor een dagelijkse uitsplitsing niet beschikbaar is. De maandcijfers zijn afgeleid via losse queries per maandvenster.
- Er is geen ROAS beschikbaar, er zijn geen purchase-conversies geregistreerd in de opgehaalde periode.

---

## Conclusie

Geen automatische acties nodig of mogelijk. Het account ligt sinds April 2026 stil.

De enige actie die telt: laat de campagne "2026: SYBB - Kopie" niet aangaan zonder eerst de creative-selectie te corrigeren. Nu zou EUR 100,00 per dag naar de zwakste varianten gaan terwijl de winnaar met 10,6% Link CTR gepauzeerd blijft staan.
