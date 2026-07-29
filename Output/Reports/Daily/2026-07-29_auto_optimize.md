# Auto-Optimize Rapport, 29 July 2026

**Databronnen:** Meta Ads MCP (Pipeboard) + PostHog MCP. Geen Google MCPs gebruikt, niet naar de Google Sheet tracker geschreven.
**Analysevenster kill-regels:** laatste 3 dagen (26 t/m 29 July 2026)
**Analysevenster historie:** January t/m April 2026

---

## Samenvatting

**Er draait niets.** Alle campagnes in het Sempertex Ad Account staan op PAUSED. De laatste euro advertentiebudget is uitgegeven in **April 2026**, ruim drie maanden geleden. In de afgelopen 30 dagen is er nul impressies, nul clicks en nul spend geregistreerd.

Kill-regels zijn daarmee niet van toepassing. Er is geen enkele ad gepauzeerd, omdat er geen enkele ad actief is.

De rest van dit rapport is daarom geen optimalisatie maar een **relaunch-briefing**: wat de historische data zegt over welke ads je moet herstarten, plus twee blokkerende problemen die je eerst moet oplossen.

---

## ⚡ Automatische acties uitgevoerd

**Geen. Er zijn nul actieve ads.**

| Controle | Resultaat |
|---|---|
| Actieve campagnes gevonden | 0 |
| Ads gepauzeerd | 0 |
| Spend laatste 3 dagen | €0.00 |
| Impressies laatste 3 dagen | 0 |

### Accountstatus

| Account | Status |
|---|---|
| `act_567892422940728` (Sempertex Ad Account) | Toegankelijk. 5 campagnes, **allemaal PAUSED** |
| `act_1489853856181844` | Toegankelijk. Geen campagnes aanwezig |
| `act_607231713057715` | **Geen toegang met dit API token.** Niet gecontroleerd |

> Het token geeft alleen toegang tot `act_567892422940728` en `act_1489853856181844`. Als er in `act_607231713057715` wel iets draait, is dat met deze run niet zichtbaar. Laat weten of dat account nog relevant is, dan kan de tokenscope aangepast worden of kan het uit het command verwijderd worden.

### Campagne-overzicht

| Campagne | Status | Dagbudget | Laatste spend |
|---|---|---|---|
| 2026: SYBB | PAUSED | €100.00 | April 2026 |
| 2026: SYBB - Kopie | PAUSED | geen | April 2026 |
| Last push Nozzle Up | PAUSED | geen | 2025 |
| Nozzle Up END OF AUGUST | PAUSED | €70.00 | 2025 |
| Campagne Nozzle Up 2025 1 | PAUSED | €30.00 | 2025 |

---

## ⚠️ Waarschuwingen

| Signaal | Waarde | Actie aanbevolen |
|---|---|---|
| **Alle advertenties uit sinds April 2026** | 91 dagen dark | Beslis of SYBB herstart wordt of formeel gestopt is |
| **SYBB landing page vrijwel dood** | 1 tot 7 views per dag, gemiddeld ~2 bezoekers | Logisch gevolg van het uitzetten van ads, geen technisch probleem |
| **Pixel purchase values zijn corrupt** | 2 aankopen gewaardeerd op €42.773,50, 4 aankopen op €1.473,50 | **Blokkerend.** Fix voor relaunch, anders is ROAS-sturing onmogelijk |
| **PostHog volgt de webshop pas sinds 15 July 2026** | Geen historie op sempertexeurope.com voor die datum | Beperkt de cross-reference met de Meta-historie |

Creative fatigue (frequency > 3.5) en dure reach (CPM > €15) zijn **niet** geconstateerd. De hoogste frequency in de hele historie was 1.95, de hoogste CPM €13.51. Beide ruim binnen de norm. De campagne is niet gestopt omdat hij opgebrand was.

### PostHog: SYBB landing page

| Metric | Laatste 30 dagen |
|---|---|
| Pageviews `startyourballoonbusiness.com` | ~55 totaal |
| Gemiddeld per dag | ~2 bezoekers |
| Laatste bezoek | 27 July 2026 |
| Paid traffic (alle sites) | 1 sessie |

Ter vergelijking: de webshop `sempertexeurope.com` deed in dezelfde periode 51.257 pageviews en 7.207 bezoekers, met een bounce rate van 57.1%. Die traffic is vrijwel volledig Direct (68.3%), Referral (15.4%) en Organic Search (11.3%). De SYBB funnel draait dus zonder aanvoer.

---

## 📊 70-20-10 Classificatie

Niet van toepassing op actieve ads, want die zijn er niet. Hieronder de classificatie van de **9 ads uit de laatste actieve periode** (March en April 2026), zodat je weet waarmee je herstart.

Alle cijfers zijn berekend op **link clicks** uit `actions.link_click`, niet op Meta's `clicks` veld.

### Ad set: BATCH 2: Expertise & POC (traffic-geoptimaliseerd)

| Ad | Impressies | Link clicks | Link CTR | Spend | CPC (link) | LPV | Leads | Aankopen |
|---|---|---|---|---|---|---|---|---|
| H13,B3,CTA5 | 60.074 | 6.342 | 10.6% | €421.29 | €0.07 | 4.063 | 3 | **0** |
| H15,B3,CTA5 | 34.299 | 1.403 | 4.1% | €218.96 | €0.16 | 845 | 0 | **0** |
| H14,B3,CTA5 | 33.235 | 760 | 2.3% | €232.36 | €0.31 | 465 | 1 | **0** |
| H11,B3,CTA5 | 31.060 | 684 | 2.2% | €202.48 | €0.30 | 445 | 6 | **0** |
| H12,B3,CTA5 | 48.166 | 696 | 1.4% | €388.40 | €0.56 | 485 | 5 | **0** |
| **Subtotaal** | **206.834** | **9.885** | **4.8%** | **€1.463,49** | **€0.15** | **6.303** | **15** | **0** |

### Ad set: BATCH 2: Expertise & POC - Kopie (conversie-geoptimaliseerd)

| Ad | Impressies | Link clicks | Link CTR | Spend | CPC (link) | LPV | Leads | Aankopen |
|---|---|---|---|---|---|---|---|---|
| H11,B3,CTA5 (Kopie 1) | 38.614 | 428 | 1.1% | €521.56 | €1.22 | 343 | 0 | **4** |
| H13,B3,CTA5 (Kopie 3) | 16.766 | 195 | 1.2% | €206.99 | €1.06 | 171 | 0 | **2** |
| H12,B3,CTA5 (Kopie) | 13.955 | 174 | 1.2% | €141.43 | €0.81 | 139 | 0 | 0 |
| H15,B3,CTA5 (Kopie) | 4.737 | 57 | 1.2% | €49.83 | €0.87 | 36 | 0 | 0 |
| **Subtotaal** | **74.072** | **854** | **1.2%** | **€919,81** | **€1.08** | **689** | **0** | **6** |

### De belangrijkste bevinding van dit rapport

Pas je de 70-20-10 drempels uit het command letterlijk toe, dan krijg je dit:

**"Core" volgens de drempels** (Link CTR > 1.5% en CPC (link) < €0.50): H13, H15, H14 en H11 uit de traffic-ad set. Samen 9.189 link clicks, €1.075,09 spend, **0 aankopen**.

**"Emerging" volgens de drempels** (Link CTR 0.8 tot 1.5%): de vier Kopie-ads plus H12. Samen 1.550 link clicks, €1.308,21 spend, **alle 6 aankopen**.

De drempels wijzen dus exact de verkeerde kant op. De ads die als winnaars gelabeld worden hebben geen enkele euro omzet opgeleverd, en de ads die als "nog niet bewezen" gelden hebben de volledige omzet gegenereerd. Dat is geen toeval maar een structureel verschil tussen de twee ad sets:

| | Traffic ad set | Conversie ad set |
|---|---|---|
| Link CTR | 4.8% | 1.2% |
| CPC (link) | €0.15 | €1.08 |
| CPM | €6.38 tot €8.06 | €10.13 tot €13.51 |
| **LPV per link click** | **60% tot 70%** | **80% tot 88%** |
| Kosten per aankoop | geen aankopen | €153,30 |

De conversie-ad set kocht duurder verkeer in, maar dat verkeer kwam wél aan op de pagina (tot 88% doorlaadratio tegenover 60% bij goedkoop verkeer) en het kocht. H13 is het scherpste voorbeeld: in de traffic-ad set haalde die ad 6.342 link clicks voor €0.07 per stuk en nul aankopen, in de conversie-ad set haalde dezelfde hook 195 clicks voor €1.06 per stuk en twee aankopen.

**Consequentie voor het command:** de openstaande TODO over het herijken van de 70-20-10 drempels is niet cosmetisch. Op deze dataset zou budget verschuiven naar Link CTR de omzet naar nul brengen. Mijn advies is om de classificatie niet op Link CTR en CPC te baseren maar op **kosten per aankoop** en **LPV per link click**, en tot die herijking gedaan is geen enkele budget-shift op basis van CTR uit te voeren.

**Consequentie voor de kill-regels:** geen van de 9 ads zou door de huidige kill-regels gepauzeerd zijn (laagste Link CTR was 1.1%, hoogste CPC (link) €1.22 bij 428 link clicks, onder het minimum van 500). De regels zijn dus niet schadelijk geweest, maar ze zouden bij een iets hogere CPC wel precies de twee converterende ads geraakt hebben. H11 Kopie zat op €1.22 en had 4 van de 6 aankopen.

---

## 💡 Voorstellen (wacht op goedkeuring)

### 1. Fix de pixel purchase values (blokkerend, doe dit eerst)

De `action_values` uit Meta zijn intern tegenstrijdig:

| Ad | Aankopen | `purchase` waarde | `web_app_in_store_purchase` | `complete_registration` |
|---|---|---|---|---|
| H11 Kopie 1 | 4 | 1.473,50 | 0,15 | 43.750 |
| H13 Kopie 3 | 2 | 42.773,50 | 4,28 | 42.350 |

Twee aankopen zouden €42.773,50 waard zijn en vier aankopen €1.473,50. Dat kan niet allebei kloppen. Daarnaast rapporteert dezelfde aankoop drie verschillende waarden afhankelijk van het action type. Er zit vrijwel zeker een verkeerde `value` parameter of een eenheidsfout (euro's tegenover centen) in de pixel-implementatie op de checkout.

**Zonder deze fix is ROAS niet te berekenen en is elke budgetbeslissing op omzet blind.** Ik heb daarom bewust geen ROAS-cijfers in dit rapport opgenomen.

Verwachte impact: maakt sturen op werkelijke omzet mogelijk in plaats van op proxy-metrics.

### 2. Herstart met de conversie-ad set, niet met de CTR-winnaars

- Reactiveer campagne `2026: SYBB` met **alleen de ad set BATCH 2: Expertise & POC - Kopie**
- Start op **€40.00 per dag** in plaats van de eerder ingestelde €100.00, om eerst te valideren dat de conversieroute nog werkt
- Laat de traffic-geoptimaliseerde ad set uit staan tot punt 1 is opgelost

Reden: die ad set leverde 6 van de 6 aankopen op 26% van het link-clickvolume. De traffic-ad set leverde 9.885 link clicks en nul omzet.

Verwachte impact: bij gelijkblijvende kosten per aankoop van €153,30 levert €40.00 per dag ongeveer 1 aankoop per 4 dagen. Dat is genoeg signaal om binnen twee weken te beslissen over opschalen.

### 3. Budgetverdeling bij relaunch

| Categorie | Ads | Voorgesteld budget | Aandeel |
|---|---|---|---|
| Bewezen converters | H11 Kopie, H13 Kopie | €28.00 per dag | 70% |
| Onbewezen uit dezelfde ad set | H12 Kopie, H15 Kopie | €8.00 per dag | 20% |
| Nieuwe hooks | zie punt 4 | €4.00 per dag | 10% |

Let op: deze verdeling is gebaseerd op aankopen, niet op de Link CTR-drempels uit het command. Dat is een bewuste afwijking, zie de bevinding hierboven.

### 4. Nieuwe variaties op de converterende hooks

Gebaseerd op wat daadwerkelijk omzet maakte, niet op wat de meeste clicks trok:

**Basis: H11 (4 aankopen, hoogste LPV-ratio van 80.1%)**
- Variatie A: zelfde hook, andere CTA gericht op de prijs-pilaar uit `sybb-8-pillars.md`, statisch beeld in plaats van video
- Variatie B: zelfde hook, opening verlengd met een concrete kostenberekening uit `pricing-balloons-strategy.md`

**Basis: H13 (2 aankopen, hoogste LPV-ratio van 87.7%)**
- Variatie C: zelfde hook, geherformuleerd als Hormozi "hidden insight" opening
- Variatie D: zelfde hook, gericht op de materials & quality pilaar

Alle vier draaien in de conversie-geoptimaliseerde ad set, niet in een traffic-ad set. Dit is expliciet het 10% experimentele budget.

### 5. Beslis over `act_607231713057715`

Het command noemt dit account als tweede bron, maar het API token heeft er geen toegang toe. Ofwel de tokenscope uitbreiden, ofwel het account uit `.claude/commands/ads-auto-optimize` verwijderen zodat toekomstige runs niet stilzwijgend een gat laten.

---

## Logboek

| Tijdstip | Actie | Resultaat |
|---|---|---|
| 2026-07-29 | Campagnes opgehaald, beide toegankelijke accounts | 5 campagnes, 0 actief |
| 2026-07-29 | Insights laatste 3 dagen | Geen data |
| 2026-07-29 | Insights laatste 30 dagen, dagelijkse breakdown | 31 dagen zonder spend |
| 2026-07-29 | Ad-level insights March en April 2026 | 9 ads, cijfers sluiten exact aan op campagnetotalen |
| 2026-07-29 | PostHog web overview en host-breakdown | SYBB LP ~2 bezoekers per dag |
| 2026-07-29 | Automatische pauzeeracties | Geen uitgevoerd, geen actieve ads |

**Datavalidatie:** de som van de 9 ads komt op 280.906 impressies, 10.739 link clicks en €2.383,30 spend. Dat sluit exact aan op de campagnetotalen voor March plus April. Het verschil met de lifetime spend van €2.485,04 is de €101,74 uit January, die buiten dit venster valt.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef de nummers aan.**
