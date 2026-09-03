# Auto-Optimize Rapport, 3 september 2026

**Run:** 2026-09-03 18:55 CEST (handmatig, niet-interactief)
**Periode:** 31 augustus t/m 2 september 2026 (Meta `last_3d`)
**Bronnen:** Meta Ads via Pipeboard (act_567892422940728, Sempertex Ad Account) en PostHog project STX EU (149694). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.
**Tweede account:** `act_607231713057715` bestaat niet in deze Pipeboard-koppeling. Het enige andere account is AmbitionAvenue (act_1489853856181844), zonder spend.

Alle CTR's en CPC's in dit rapport zijn **Link CTR** en **CPC (link)**, berekend uit `actions.link_click`. Meta's `clicks`, `ctr` en `cpc` velden zijn genegeerd.

---

## ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd.**

| Ad | Regel | Waarde | Data | Besluit |
|----|-------|--------|------|---------|
| Statisch 1 (LIT) | Link CTR < 0,8% | Link CTR 0,48% | 12.389 impressions, 60 link clicks | Kill-regel triggert (2e dag op rij). **Niet gepauzeerd**, zie toelichting. |
| Alle 8 ads | CPC (link) > €1,50 | n.v.t. | Geen enkele ad heeft 500 link clicks | Regel niet van toepassing |

**Toelichting Statisch 1 (LIT), 18:55 CEST:** de regel is bedoeld om duidelijke underperformers te stoppen. Deze ad is op de campagnedoelstelling (leads) geen underperformer:

| Bron | Laatste 3 dagen | Lifetime (sinds 27 aug) |
|------|-----------------|--------------------------|
| Meta leads | 1 (CPL €61,05) | 3 (CPL €43,92) |
| PostHog `wholesaler_form_submit` | 2 (€30,52 per inzending) | 4 (€32,94 per inzending) |
| Sessie-naar-inzending | 2 op 58 sessies (3,4%) | 4 op 99 sessies (4,0%, hoogste van alle 8 ads) |

De lage Link CTR zit aantoonbaar in Facebook (0,35%) en desktop (0,10% op 1.989 impressions). Wie wél doorklikt, converteert bovengemiddeld. Pauzeren zou 1 van de 2 LIT-ads met inzendingen in de laatste 3 dagen uitschakelen en de learning phase resetten.

**Regel voor de volgende run, zolang Robin niets anders beslist:** Statisch 1 (LIT) wordt automatisch gepauzeerd zodra de ad 3 opeenvolgende dagen 0 form submits heeft in PostHog én de Link CTR onder 0,8% blijft. Robin kan dit vandaag nog overrulen via voorstel 5 hieronder.

Pauzeer-commando staat klaar (alleen op verzoek):
```
update_ad  ad_id=120250160534150239  status=PAUSED
```

---

## ⚠️ Waarschuwingen

| Ad | Signaal | Waarde | Actie aanbevolen |
|----|---------|--------|-----------------|
| Video 2 (SWE) | Dure reach | CPM €18,16 (> €15) | 1 inzending lifetime na €113,21. Instagram: CPM €21,36, Link CTR 0,74%. Budget verlagen of Instagram uitsluiten (voorstel 1 en 3). |
| Video 1 (SWE) | Dure reach + geen conversies | CPM €15,60 (> €15), 0 leads en 0 inzendingen na €115,49 (6 dagen) | Pauzeren (voorstel 1). Link CTR zakt naar 80% van lifetime, nog boven de 70%-grens. |
| Video 2 (LIT) | Nep-clicks Audience Network | 25 van 68 link clicks (37%) komen van Audience Network met Link CTR 10,1% en 2 landing page views | Audience Network uitsluiten (voorstel 3). Facebook 0,74%, Instagram 0,39% Link CTR. Wél 5 inzendingen lifetime, dus ad zelf behouden. |
| Statisch 2 (LIT) | Hoge clicks, lage conversie | Link CTR 1,13%, CPC (link) €0,43 (goedkoopste), maar 0 inzendingen in 3 dagen en 2 lifetime (€57,66 per inzending) | Niet opschalen op basis van clicks alleen. Landing page ontvangt 221 sessies, 10 form starts, 2 submits. |
| Beide campagnes | Meta pixel telt te weinig | Meta: 85 landing page views en 5 leads. PostHog: 521 sessies en 9 form submits in dezelfde 3 dagen | Tracking checken (voorstel 4). Ad sets optimaliseren op OFFSITE_CONVERSIONS met een onvolledig signaal. |

**Niet getriggerd:** creative fatigue (hoogste frequency 2,36 bij Statisch 1 LIT, campagne LIT 2,82, grens 3,5), dalende Link CTR (laagste verhouding 3d/lifetime is 80% bij Video 1 SWE, grens 70%).

---

## 📊 Performance per ad (31 aug t/m 2 sep)

| Ad | Spend | Impr. | Link clicks | Link CTR | CPC (link) | CPM | Freq | Meta LPV | Meta leads | PostHog sessies | Form submits | € per submit |
|----|-------|-------|-------------|----------|------------|-----|------|----------|------------|-----------------|--------------|--------------|
| Statisch 2 (SWE) | €61,89 | 5.748 | 110 | **1,91%** | €0,56 | €10,77 | 1,56 | 20 | 2 | 95 | 1 | €61,89 |
| Video 2 (SWE) | €56,68 | 3.122 | 44 | 1,41% | €1,29 | €18,16 | 1,74 | 8 | 0 | 28 | 0 | n.v.t. |
| Video 1 (SWE) | €60,10 | 3.853 | 54 | 1,40% | €1,11 | €15,60 | 1,66 | 8 | 0 | 41 | 0 | n.v.t. |
| Statisch 1 (SWE) | €59,57 | 4.845 | 64 | 1,32% | €0,93 | €12,30 | 1,77 | 11 | 1 | 34 | 1 | €59,57 |
| Video 1 (LIT) | €61,18 | 8.402 | 95 | 1,13% | €0,64 | €7,28 | 1,60 | 8 | 1 | 95 | **3** | **€20,39** |
| Statisch 2 (LIT) | €60,65 | 12.420 | 140 | 1,13% | **€0,43** | €4,88 | 1,82 | 17 | 0 | 124 | 0 | n.v.t. |
| Video 2 (LIT) | €57,89 | 6.783 | 68 | 1,00% | €0,85 | €8,53 | 2,06 | 6 | 0 | 47 | 1 | €57,89 |
| Statisch 1 (LIT) | €61,05 | 12.389 | 60 | 0,48% | €1,02 | €4,93 | 2,36 | 7 | 1 | 58 | 2 | €30,52 |
| **Totaal** | **€479,01** | **57.562** | **635** | **1,10%** | **€0,75** | €8,32 | | **85** | **5** | **521** | **8** (+1 zonder UTM) | **€59,88** |

Campagneniveau: LIT €240,77, Link CTR 0,91%, CPC (link) €0,66, 6 inzendingen (€40,13 per inzending). SWE €238,24, Link CTR 1,55%, CPC (link) €0,88, 2 inzendingen (€119,12 per inzending). SWE wint op clicks, LIT wint op conversies.

**Funnel-correctie op het rapport van 2 september:** gisteren stond dat maar 12 tot 17% van de link clicks een landing page view werd. Dat was de Meta-pixel. PostHog ziet 521 sessies op 635 link clicks (82,0%). Het lek zit niet in de landing page maar in de meting: Meta registreert 13,4% van de bezoeken als landing page view en 5 van de 9 inzendingen als lead.

Lifetime per ad (sinds 27/28 aug):

| Ad | Spend | Link CTR | CPC (link) | Meta leads | Meta CPL | Form submits | € per submit |
|----|-------|----------|------------|------------|----------|--------------|--------------|
| Statisch 2 (SWE) | €115,18 | 2,20% | €0,44 | 5 | €23,04 | 4 | €28,80 |
| Video 1 (SWE) | €115,49 | 1,75% | €0,88 | 0 | n.v.t. | 0 | n.v.t. |
| Statisch 1 (SWE) | €113,61 | 1,58% | €0,77 | 2 | €56,80 | 2 | €56,80 |
| Video 2 (SWE) | €113,21 | 1,57% | €1,09 | 0 | n.v.t. | 1 | €113,21 |
| Video 1 (LIT) | €134,08 | 1,28% | €0,61 | 3 | €44,69 | 5 | €26,82 |
| Statisch 2 (LIT) | €115,31 | 1,16% | €0,42 | 1 | €115,31 | 2 | €57,66 |
| Video 2 (LIT) | €130,89 | 1,10% | €0,76 | 4 | €32,72 | 5 | €26,18 |
| Statisch 1 (LIT) | €131,77 | 0,59% | €0,88 | 3 | €43,92 | 4 | €32,94 |

---

## 📊 70-20-10 Classificatie

De 70-20-10 drempels zijn nog niet gekalibreerd op link metrics (zie TODO in het command). Geen enkele ad haalt strikt "Link CTR > 1,5% én CPC (link) < €0,50". Onderstaande indeling combineert Link CTR met de werkelijke inzendingen, als richtlijn.

**70% Core (huidig budget €60,00/dag, 37,5% van totaal):**
- Statisch 2 (SWE): Link CTR 1,91%, CPC (link) €0,56, Meta CPL lifetime €23,04, 4 inzendingen (€28,80). Beste hook-visual van het account.
- Video 1 (LIT): Link CTR 1,13%, CPC (link) €0,64, 3 inzendingen in 3 dagen (€20,39), 5 lifetime (€26,82).
- Video 2 (LIT): Link CTR 1,00%, CPC (link) €0,85, 5 inzendingen lifetime (€26,18, goedkoopste van het account).

**20% Emerging (huidig budget €60,00/dag, 37,5% van totaal):**
- Statisch 1 (LIT): Link CTR 0,48% (kill-regel), maar 4 inzendingen lifetime (€32,94) en de hoogste sessie-naar-inzending ratio. Verdient de audience-fix uit voorstel 3.
- Statisch 2 (LIT): goedkoopste clicks (€0,43), maar 2 inzendingen lifetime (€57,66). Potentieel als de landing page beter converteert voor dit verkeer.
- Statisch 1 (SWE): Link CTR 1,32%, CPC (link) €0,93, 2 inzendingen (€56,80). Middenmoot.

**10% Experimental / oordeel uitgesteld (huidig budget €40,00/dag, 25,0% van totaal):**
- Video 1 (SWE): 7.491 impressions, 0 leads, 0 inzendingen na €115,49. Geen experiment meer, dit is een verliezer.
- Video 2 (SWE): 6.616 impressions, 1 inzending na €113,21, CPM €18,16.

**Budget mismatch: Ja.** Core krijgt 37,5% in plaats van 70%. De twee SWE-video's zonder resultaat krijgen 25% in plaats van 10%. Kanttekening: de steekproef is klein (1 tot 5 inzendingen per ad), dus verschuif gematigd en budget-neutraal.

---

## 💡 Voorstellen (wacht op goedkeuring)

**1. Budget herverdeling (budget-neutraal, blijft €160,00/dag)**

| Ad set | Van | Naar | Reden |
|--------|-----|------|-------|
| Video 1 (SWE) | €20,00 | **Pauzeren** | 0 leads, 0 inzendingen na €115,49 en 6 dagen. CPM €15,60. |
| Video 2 (SWE) | €20,00 | €10,00 | 1 inzending na €113,21. Laat lopen op laag budget tot 6 september, dan definitief oordeel. |
| Statisch 2 (SWE) | €20,00 | €30,00 | Beste Link CTR (1,91%) en beste Meta CPL (€23,04). |
| Video 1 (LIT) | €20,00 | €30,00 | 3 inzendingen in 3 dagen, €20,39 per inzending. |
| Video 2 (LIT) | €20,00 | €30,00 | Goedkoopste inzendingen lifetime (€26,18). Combineer met AN-uitsluiting (voorstel 3). |
| Statisch 1 (LIT), Statisch 2 (LIT), Statisch 1 (SWE) | €20,00 | €20,00 | Ongewijzigd. |

Resultaat: Core 56% (€90), Emerging 38% (€60), Experimental 6% (€10). Verwachte impact: zelfde spend, naar schatting 2 tot 3 extra inzendingen per week doordat €30/dag verschuift van ads zonder resultaat naar ads met €20 tot €29 per inzending. Verhogingen van 50% resetten de learning phase van de ad set. Doe dit 's ochtends, niet 's avonds.

**2. Nieuwe variaties**

Alle 8 ads gebruiken exact dezelfde copy. Titel "Become a Sempertex partner in [land]", body "Sempertex Europe is looking for official wholesale partners in [land]. Party shops and wholesalers: premium latex balloons, shipped from Belgium, with a ready-to-sell starter package. Two minute form, then an intake call.", CTA SEE_DETAILS. Het enige verschil tussen de ads is de visual. De hook-test is dus nog niet gestart.

Gebaseerd op de winnende visual Statisch 2 (Link CTR 1,91% SWE, 1,13% LIT), 3 varianten per land met de Hormozi hook-types (Statements zijn 47,9% van zijn top-hooks, Commando's 21,5%):

- Variatie A, Statement (scarcity): "Sweden does not have an official Sempertex wholesaler yet." / "Lithuania does not have an official Sempertex wholesaler yet." Body ongewijzigd. CTA: APPLY_NOW. Hypothese: first-mover urgentie verhoogt de sessie-naar-inzending ratio.
- Variatie B, Label (call-out): "Party shop owners in Sweden: this one is for you." Body begint met het starterspakket in plaats van met Sempertex Europe. CTA: SIGN_UP. Hypothese: identificatie in de eerste regel, hogere Link CTR op Facebook waar Statisch 1 (LIT) nu 0,35% haalt.
- Variatie C, Vraag: "Would you rather wait weeks for balloon stock, or have it shipped from Belgium in days?" Body ongewijzigd, plus regel "Made in our own factory, certified for the EU market." (proof uit `sempertex-company-heritage-and-vision.md`). CTA: LEARN_MORE. Hypothese: het logistieke voordeel is de concrete reden om nu te schakelen.

Alles in UK spelling, geen concurrenten benoemd. Budget per variant €10,00/dag als 10%-experiment, binnen de bestaande campagnes.

**3. Audience aanpassingen**

- Statisch 1 (LIT): leeftijd 18-65 naar 25-65. Het 18-24 segment kost €4,89 op 1.521 impressions zonder inzendingen. Alle andere 7 ad sets staan al op 25-65.
- Statisch 1 (LIT): desktop uitsluiten. 1.989 impressions, 2 link clicks (Link CTR 0,10%), €5,06 zonder resultaat.
- Alle 8 ad sets: Audience Network uitsluiten. 45 link clicks in 3 dagen met 4 landing page views. Spend is klein (€3,85) maar de nep-clicks vervuilen de Link CTR en het conversiesignaal. Video 2 (LIT) haalt 37% van zijn link clicks daar vandaan.
- Video 2 (SWE): Instagram uitsluiten als de ad blijft draaien. CPM €21,36, Link CTR 0,74%, 0 inzendingen.

**4. Tracking check (geen ad-wijziging, wel prioriteit)**

Meta ziet 85 landing page views en 5 leads waar PostHog 521 sessies en 9 `wholesaler_form_submit` events ziet. Check op `/en_GB/become-a-distributor`: vuurt het Meta Pixel PageView-event, en is het Lead-event gekoppeld aan de formulierinzending (pixel of Conversions API)? Zolang Meta minder dan de helft van de conversies ziet, optimaliseren de ad sets op een half signaal en komen ze nooit uit de learning phase. Dit heeft meer effect dan elke budget-shift hierboven.

**5. Beslissing kill-regel Statisch 1 (LIT)**

- **A (aanbevolen):** laten draaien met de audience-fix uit voorstel 3, en de kill-regel voor lead-campagnes structureel aanpassen naar "Link CTR < 0,8% én 0 form submits in de laatste 3 dagen". Ik pas dit dan aan in het command.
- **B:** strikt pauzeren volgens de huidige regel. Ik voer dit direct uit na je bevestiging.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers (1, 2, 3, 4, 5A of 5B).**

---

## Log

| Tijd (CEST) | Actie | Detail |
|-------------|-------|--------|
| 18:40 | Data opgehaald | Pipeboard direct JSON-RPC: get_campaigns, get_adsets, get_ads, get_insights (ad, campaign, day, publisher_platform, age, device_platform), get_ad_creatives. PostHog HogQL: sessions en wholesaler_* events. |
| 18:50 | Kill-regel geëvalueerd | Statisch 1 (LIT) triggert Link CTR < 0,8% (0,48% op 12.389 impressions). Niet gepauzeerd, motivatie hierboven. 0 van 8 ads gepauzeerd (grens 50%). |
| 18:50 | CPC (link) regel | Niet van toepassing, geen ad boven 500 link clicks. |
| 18:55 | Rapport opgeslagen | `Output/Reports/Daily/2026-09-03_auto_optimize.md`. Geen Google MCPs, geen Sheet. |
