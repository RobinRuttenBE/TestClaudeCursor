# Auto-Optimize Rapport, 2026-05-06

**Run:** `/ads-auto-optimize`
**Tijdstip:** 2026-05-06 (ochtend)
**Periode:** last_3d (Meta Ads)
**Bronnen:** Meta Ads MCP (Pipeboard). Google MCPs uitgesloten conform run-instructie.
**Accounts gecontroleerd:**
- `act_567892422940728` (Sempertex primair)
- `act_1489853856181844` (secundair, toegankelijk via token)
- `act_607231713057715` (genoemd in command, GEEN toegang met huidig token, overgeslagen)

---

## Samenvatting

**Geen automatische acties uitgevoerd. Geen voorstellen gegenereerd.**

Alle campagnes in beide toegankelijke accounts staan op `PAUSED`. Er is geen ad-spend, impressies, of click-data over de afgelopen 3 dagen om de kill-regels of 70-20-10 classificatie tegen te evalueren.

---

## 1. Status per account

### `act_567892422940728`, Sempertex (primair)

5 campagnes opgehaald, allemaal `PAUSED`:

| Campagne | Status | Daily budget | Laatst geüpdatet |
|---|---|---|---|
| 2026: SYBB - Kopie | PAUSED | n.v.t. | 2026-04-20 |
| 2026: SYBB | PAUSED | €100,00 | 2026-04-19 |
| Last push Nozzle Up | PAUSED | n.v.t. | 2025-09-21 |
| Nozzle Up END OF AUGUST | PAUSED | €70,00 | 2025-09-15 |
| Campagne Nozzle Up 2025 1 | PAUSED | €30,00 | 2025-09-15 |

Account-level insights `last_3d`: leeg. Geen spend, impressies of clicks.
Campagne-level insights `last_7d` op `2026: SYBB` (120239435987290239): leeg.

### `act_1489853856181844` (secundair)

0 campagnes. Account is leeg.

### `act_607231713057715`

Geen toegang met huidig API-token. Token-foutmelding van Pipeboard:
> *"This API token does not have access to account act_607231713057715. Allowed accounts: act_1489853856181844, act_567892422940728"*

Aanbeveling: als dit account daadwerkelijk in gebruik is, voeg het toe aan de Pipeboard-tokenscope. Anders verwijder de referentie uit `.claude/commands/ads-auto-optimize.md`.

---

## 2. Automatische acties uitgevoerd (Niveau 1)

**Geen.** Er zijn geen actieve ads om tegen kill-regels te evalueren.

| Ad | Reden | Was | Nu |
|---|---|---|---|
| n.v.t. | n.v.t. | n.v.t. | n.v.t. |

**Totaal gepauzeerd: 0 ads** (er was niets actief om te pauzeren).

---

## 3. Waarschuwingen

**Geen ad-niveau waarschuwingen** (geen actieve creatives, geen frequency- of CPM-data).

**Operationele waarschuwing, alle campagnes paused:**
- `2026: SYBB` is sinds 2026-04-19 paused (laatste update). Daarvoor was dit de hoofd-traffic-bron voor `startyourballoonbusiness.com`.
- Geen Meta-traffic naar de SYBB landing page betekent dat de PostHog-funnel-metrics in de morning report grotendeels nul zullen zijn voor de paid-source. Eventuele organic/direct traffic blijft natuurlijk doorlopen.
- Dit is een statusconstatering, geen aanbeveling. Robin bepaalt of/wanneer SYBB weer aan gaat.

---

## 4. 70-20-10 Classificatie

Niet van toepassing. 0 actieve ads, dus geen Core/Emerging/Experimental indeling.

---

## 5. Voorstellen (Niveau 2)

**Geen ad-optimalisatie voorstellen** (geen data om op te bouwen).

**Wel: één procesvoorstel voor Robin** (geen automatische actie, alleen ter overweging):

1. **SYBB-relaunch beslissen**
   - De `2026: SYBB` campagne staat al ~17 dagen op pause (sinds 2026-04-19).
   - Als je nieuwe creatives klaar wilt hebben voor relaunch, is dit een goed moment voor een batch via `/ad-combinator` + `/ads-batch-upload`.
   - Als de pause bewust open-eindig is (bijv. wachten op nieuwe LP-versie of seizoens-timing), prima. Maar zorg dat dit ergens als project-status genoteerd staat zodat de morning report niet elke dag een leeg rapport oplevert.

2. **Account-toegang opruimen**
   - Pipeboard-token mist `act_607231713057715`. Beslis: extra toegang regelen óf de referentie uit het command verwijderen.

---

## 6. Data-kwaliteit en guardrails

| Check | Resultaat |
|---|---|
| Min. 24u actief vereist | n.v.t. (geen actieve ads) |
| Max. 50% actieve ads pauzeren in één run | n.v.t. (0/0) |
| Link metrics gebruikt (geen all-clicks) | n.v.t. (geen data) |
| Google MCPs vermeden | ja, uitsluitend Pipeboard Meta Ads MCP gebruikt |
| Output enkel lokaal opgeslagen | ja, deze file in `Output/Reports/Daily/` |

---

## Volgende stap

- Geen tool-actie vereist.
- Bij eerstvolgende SYBB-relaunch: rerun `/ads-auto-optimize` na 24 tot 72 uur zodra er voldoende impressies en link-clicks zijn voor de kill-regels (≥1.000 imp respectievelijk ≥500 link clicks).
