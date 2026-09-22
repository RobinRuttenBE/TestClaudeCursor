## Auto-Optimize Rapport, 22 september 2026

**Run:** 22 september 2026, 13:30 CEST (11:30 UTC). Bronnen: Pipeboard Meta Ads via directe JSON-RPC route (2 calls: ad-level `last_3d` en ad-level `last_30d` op `act_567892422940728`) en PostHog project STX EU 149694 via directe REST-route (3 queries, alle onder 0,4 seconde). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven. Weekverbruik Pipeboard na deze run: 13 van 30 calls.

**Status account:** alle 7 campagnes staan op PAUSED (status uit het ads-rapport van vanochtend, 22 september). De twee Wholesaler Campagnes (LIT en SWE) staan stil sinds 4 september. De ad-level call over de laatste 3 dagen (19 t/m 21 september) gaf `{"data": []}`: nul impressies, nul spend. Twintigste dag zonder levering. Account `act_607231713057715` uit het command bestaat niet (bekend sinds 2 september); het tweede account `act_1489853856181844` is leeg en is niet opgevraagd.

---

### ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd. Er is geen enkele ad met impressies in de laatste 3 dagen, dus de kill-regels (Link CTR < 0,8% na 1.000 impressies, CPC (link) > €1,50 na 500 link clicks) hadden niets om op te draaien. Geen `update_ad` calls gedaan.

**Totaal gepauzeerd: 0 ads**

Ter informatie: als de campagnes in de huidige vorm herstart worden, triggert **Statisch 1 (LIT)** direct de Link CTR kill-regel (0,57% op 28.434 impressies over 30 dagen). Zie de conversie-kanttekening bij de classificatie hieronder voordat je die ad daadwerkelijk laat pauzeren.

---

### 📋 Per-ad link-metrics (last 30d, 23 augustus t/m 21 september, live opgehaald)

Alle Meta-cijfers uit `get_insights` level ad, `date_preset: last_30d`. Link clicks uit `actions.link_click`, Link CTR en CPC (link) zelf berekend. Meta leads uit `actions.lead`. PostHog sessies en inzendingen per ad uit het ads-rapport van 22 september (30d, ongewijzigd sinds 16 september omdat er geen levering was).

| Ad | Ad ID | Spend | Impr. | Reach | Freq. | CPM | All clicks | All Clicks CTR | CPC (all) | Link clicks | Link CTR | CPC (link) | LPV | Meta leads | € / Meta lead | PostHog sessies | PostHog inz. | € / inz. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | 120250159503120239 | €146,91 | 19.041 | 10.024 | 1,90 | €7,72 | 453 | 2,4% | €0,32 | 242 | 1,3% | €0,61 | 28 | 3 | €48,97 | 248 | 5 | €29,38 |
| Video 2 (LIT) | 120250160387390239 | €143,74 | 17.267 | 6.847 | 2,52 | €8,32 | 247 | 1,4% | €0,58 | 179 | 1,0% | €0,80 | 21 | 4 | €35,94 | 141 | 5 | €28,75 |
| Statisch 1 (LIT) | 120250160534150239 | €144,24 | 28.434 | 9.782 | 2,91 | €5,07 | 294 | 1,0% | €0,49 | 163 | 0,6% | €0,88 | 27 | 3 | €48,08 | 134 | 4 | €36,06 |
| Statisch 2 (LIT) | 120250161077250239 | €127,25 | 26.146 | 11.021 | 2,37 | €4,87 | 623 | 2,4% | €0,20 | 297 | 1,1% | €0,43 | 45 | 1 | €127,25 | 292 | 2 | €63,63 |
| Video 1 (SWE) | 120250180000300239 | €126,75 | 8.299 | 4.055 | 2,05 | €15,27 | 238 | 2,9% | €0,53 | 139 | 1,7% | €0,91 | 31 | 0 | n.v.t. | 113 | 0 | n.v.t. |
| Video 2 (SWE) | 120250180392100239 | €127,00 | 7.441 | 3.682 | 2,02 | €17,07 | 185 | 2,5% | €0,69 | 114 | 1,5% | €1,11 | 19 | 1 | €127,00 | 97 | 2 | €63,50 |
| Statisch 1 (SWE) | 120250180580670239 | €125,36 | 10.262 | 4.769 | 2,15 | €12,22 | 281 | 2,7% | €0,45 | 157 | 1,5% | €0,80 | 44 | 2 | €62,68 | 131 | 2 | €62,68 |
| Statisch 2 (SWE) | 120250180888540239 | €128,13 | 13.265 | 6.744 | 1,97 | €9,66 | 533 | 4,0% | €0,24 | 286 | 2,2% | €0,45 | 62 | 5 | €25,63 | 256 | 3 | €42,71 |
| **Totaal** | | **€1.069,38** | **130.155** | | | €8,22 | 2.854 | 2,2% | €0,37 | **1.577** | **1,2%** | **€0,68** | 277 | 19 | €56,28 | 1.412 | 23 | €46,49 |

Verhouding link versus all-clicks over alle 8 ads: Link CTR is 55% van All Clicks CTR, CPC (link) is 1,8 keer CPC (all). Dat bevestigt de aanname in het command. PostHog telt 35 inzendingen in 30d, waarvan 23 aan een ad te koppelen; de rest is organisch of zonder UTM.

---

### ⚠️ Waarschuwingen

Alle waarschuwingen gelden pas bij herstart; er loopt nu geen levering.

| Ad | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| Video 2 (SWE) | Dure reach | CPM €17,07 (> €15,00) | Audience verbreden of creative vervangen vóór herstart |
| Video 1 (SWE) | Dure reach | CPM €15,27 (> €15,00) | Niet herstarten: 0 inzendingen op 113 sessies |
| Video 2 (SWE) | CPC (link) richting kill-drempel | €1,11 (drempel €1,50 na 500 link clicks; nu 114) | Bij herstart na 500 link clicks opnieuw toetsen |
| Statisch 1 (LIT) | Link CTR onder kill-drempel | 0,6% op 28.434 impressies | Zou mechanisch gepauzeerd worden, maar levert €36,06 per inzending (derde beste). Zie voorstel 4 |
| Campagne LIT (campagne-niveau) | Creative fatigue | Frequency 3,97 (ad-niveau 1,90 t/m 2,91) | Verse creatives bij herstart, ad sets overlappen op hetzelfde publiek |
| Statisch 2 (LIT) | Goedkope clicks, dure leads | CPC (link) €0,43 maar €63,63 per inzending | Nieuwe hook testen, huidige trekt kijkers, geen aanvragers |

Creative fatigue op ad-niveau: geen enkele ad boven frequency 3,5. Dalende Link CTR (3d < 70% van lifetime): niet toetsbaar zonder 3d-data.

---

### 📊 70-20-10 Classificatie

Gebaseerd op link-metrics over 30 dagen. De drempels uit het command zijn nog niet gekalibreerd voor link-metrics (TODO in het command), dus deze indeling is een richtlijn. Er is nu geen actief budget; percentages zijn de spend-verdeling van de laatste levering (30d, €1.069,38).

**70% Core (huidig 12,0% van spend, €128,13):**
- Statisch 2 (SWE), Link CTR 2,2%, CPC (link) €0,45, €25,63 per Meta lead, €42,71 per PostHog inzending. Enige ad die beide Core-drempels haalt.

**20% Emerging (huidig 50,8% van spend, €543,26):**
- Video 1 (LIT), Link CTR 1,3%, CPC (link) €0,61, €29,38 per inzending. Beste volume (5 inzendingen).
- Video 2 (LIT), Link CTR 1,0%, CPC (link) €0,80, €28,75 per inzending. Beste kosten per inzending, conversie 3,5%.
- Statisch 1 (SWE), Link CTR 1,5%, CPC (link) €0,80, €62,68 per inzending. Net onder Core op CPC.
- Statisch 2 (LIT), Link CTR 1,1%, CPC (link) €0,43, €63,63 per inzending. Core op CPC, Emerging op Link CTR, zwak op conversie (0,7%).

**10% Experimental (huidig 0,0% van spend):**
- Geen ads met minder dan 500 impressies. Er is al drie weken niets nieuws gelanceerd.

**Onder de drempels (huidig 37,2% van spend, €397,99):**
- Statisch 1 (LIT), Link CTR 0,6%, CPC (link) €0,88. Onder kill-drempel op Link CTR, maar €36,06 per inzending.
- Video 1 (SWE), Link CTR 1,7%, CPC (link) €0,91, 0 inzendingen. Definitief uit.
- Video 2 (SWE), Link CTR 1,5%, CPC (link) €1,11, €63,50 per inzending. Uit in huidige vorm.

**Budget mismatch:** Ja. De enige Core-ad kreeg 12,0% van het budget in plaats van 70%, en 37,2% ging naar ads die op link-metrics onder de drempels vallen. Bij de vorige levering was het budget gelijk verdeeld over 8 ad sets (circa €125,00 tot €147,00 per ad), zonder onderscheid naar prestatie. Geen budget-shift uitgevoerd: de campagnes staan stil en de drempels zijn nog niet gekalibreerd.

**Kanttekening bij de indeling:** de link-metrics en de conversie-ranking lopen uiteen. Op kosten per inzending is de top 3 Video 2 (LIT) €28,75, Video 1 (LIT) €29,38 en Statisch 1 (LIT) €36,06; op link-metrics staat alleen Statisch 2 (SWE) in Core. Voor lead-campagnes hoort kosten per inzending het laatste woord te hebben. Dat is de kern van voorstel 7.

---

### 📈 PostHog live bevestiging (sessions en events)

Betaalde sessies (`$entry_utm_source = 'facebook'`) per dag, 12 t/m 22 september: 0 op elke dag. Site-breed liepen er 538 tot 5.834 sessies per dag, dus de tracking werkt; er is alleen geen betaald verkeer.

Funnel /become-a-distributor per dag (custom events, live opgehaald, de events-tabel antwoordde vanmiddag weer normaal):

| Dag | Pageviews | Formulierstarts | Fouten | Inzendingen |
|---|---|---|---|---|
| 15 sep | 2 | 0 | 0 | 0 |
| 16 sep | 9 | 0 | 0 | 0 |
| 17 sep | 1 | 1 | 0 | 0 |
| 18 sep | 4 | 3 | 0 | 1 |
| 19 sep | 3 | 1 | 0 | 0 |
| 20 sep | 2 | 2 | 1 | 1 |
| 21 sep | 4 | 0 | 0 | 0 |
| 22 sep (t/m 11:30 UTC) | 2 | 0 | 0 | 0 |

Sessies op de distributeurspagina, 12 t/m 22 september: 1 tot 8 per dag, allemaal organisch. Op 21 september geen nieuwe inzending (dat kon vanochtend niet bevestigd worden, nu wel). De twee organische inzendingen van 18 september (Letland) en 20 september (Malta) blijven de enige sinds de pauze. De formulierfout van 20 september staat nog open (voorstel 5).

---

### 💡 Voorstellen (wacht op goedkeuring)

Dezelfde zeven voorstellen als op 21 september, nu met de live 30d link-cijfers van vandaag eronder. Niets hiervan is uitgevoerd.

**1. Herstart met herverdeeld budget (LIT €100,00 per dag, SWE €40,00 per dag)**
- Statisch 2 (SWE): van €0,00 naar €28,00 per dag (70% van SWE). Reden: enige Core-ad, Link CTR 2,2%, CPC (link) €0,45, €25,63 per Meta lead.
- Video 1 (LIT): van €0,00 naar €35,00 per dag. Video 2 (LIT): van €0,00 naar €35,00 per dag. Reden: €29,38 en €28,75 per inzending, samen 10 van de 23 gekoppelde inzendingen.
- Statisch 1 (LIT): van €0,00 naar €20,00 per dag, alleen met verse creative. Reden: €36,06 per inzending, maar Link CTR 0,6% zou de kill-regel triggeren; nieuwe visual moet die boven 0,8% brengen.
- Statisch 2 (LIT): van €0,00 naar €10,00 per dag met nieuwe hook (Experimental-budget). Reden: goedkoopste link clicks (€0,43) maar 0,7% conversie.
- Statisch 1 (SWE): van €0,00 naar €12,00 per dag. Reden: Link CTR 1,5%, net onder Core.
- Video 1 (SWE) en Video 2 (SWE): blijven op €0,00. Reden: 0 inzendingen respectievelijk CPC (link) €1,11 en CPM €17,07.
- Verwachte impact: bij gelijke conversie circa 3,5 inzendingen per dag op €140,00, ofwel circa €40,00 per inzending in plaats van €46,49.

**2. Nieuwe variaties op de winnende hooks**
- Gebaseerd op Statisch 2 (SWE) (Link CTR 2,2%, beste van alle 8): drie hook-varianten op dezelfde visual, Statement-hook, Label-hook ("For balloon shops in Sweden that…") en Vraag-hook. Format: statisch, zelfde CTA.
- Gebaseerd op Video 2 (LIT) (beste conversie, 3,5%): Zweedse variant met dezelfde opbouw, ondertiteling in het Zweeds. Format: video 15 tot 20 seconden.
- Gebaseerd op Video 1 (SWE) (Link CTR 1,7%, maar 0 inzendingen): de hook werkt, de belofte niet. Nieuwe body en CTA gericht op de aanvraag, zelfde eerste 3 seconden.
- Voor Statisch 2 (LIT): nieuwe Vraag-hook die filtert op wholesalers in plaats van kijkers ("Do you sell balloons to professionals in Lithuania?").
- Het ophalen van de huidige ad-copy kost één extra Meta-call (`get_ad_creatives`); niet gedaan zonder akkoord.

**3. Audience aanpassingen**
- LIT: de vier ad sets samenvoegen tot één ad set met vier ads. Reden: campagne-frequency 3,97 bij ad-frequency van maximaal 2,91 betekent dat de ad sets elkaar overlappen op hetzelfde publiek.
- Audience Network uitsluiten op beide campagnes. Reden: Statisch 2 (LIT) heeft 623 all clicks tegenover 297 link clicks en 45 landing page views; dat patroon past bij goedkope placements met lage intentie.
- Statisch 1 (LIT): leeftijd 25 tot 65, desktop uitsluiten. Reden: laagste Link CTR (0,6%) bij hoogste impressies (28.434), de ad wordt breed getoond aan mensen die niet doorklikken.
- SWE: publiek verbreden (interesses balloon decoration, party supply retail, event styling toevoegen). Reden: CPM €9,66 tot €17,07 tegenover €4,87 tot €8,32 in LIT.
- Letland en Malta als testlanden met €10,00 per dag elk. Reden: organische inzendingen op 18 en 20 september zonder enige advertentie.

**4. Conversie-guard op de kill-regels**
- Regel toevoegen aan dit command: een ad met minimaal 3 inzendingen in 30d en kosten per inzending onder €40,00 wordt niet automatisch gepauzeerd op Link CTR, maar gerapporteerd. Reden: Statisch 1 (LIT) zou anders bij herstart na 1.000 impressies weg zijn terwijl het de derde beste converteerder is.

**5. Funnel en pixel fix vóór herstart**
- Formulierfout op /become-a-distributor oplossen (opnieuw een fout op 20 september, 22 fouten op 141 starts in de laatste 30d met levering).
- Meta pixel lead-event controleren: Meta telt 19 leads waar PostHog 35 inzendingen ziet. Reden: zonder correcte lead-signalen optimaliseert Meta op de verkeerde mensen.

**6. Eén gedeeld Meta-extract per dag**
- Ads-report haalt 's ochtends campaign-level 30d, ad-level 30d en de campagnelijst op en schrijft ze naar `output/reports/daily/YYYY-MM-DD_meta_extract.json`. SYBB-rapport en auto-optimize lezen dat bestand en doen alleen hun eigen 3d- of campagne-call. Reden: vandaag 13 van 30 calls na drie rapporten; zonder delen sluit de limiet woensdag of donderdag opnieuw.

**7. 70-20-10 drempels kalibreren op link-metrics**
- Voorstel: Core = Link CTR > 1,2% én CPC (link) < €0,70, of kosten per inzending < €40,00 met minimaal 3 inzendingen. Emerging = Link CTR 0,8% tot 1,2% of CPC (link) €0,70 tot €1,00. Onder de drempels = Link CTR < 0,8% of CPC (link) > €1,00 zonder conversie-uitzondering.
- Uitkomst op de huidige 8 ads: Core wordt Statisch 2 (SWE), Video 1 (LIT), Video 2 (LIT) en Statisch 1 (LIT); Emerging wordt Statisch 2 (LIT) en Statisch 1 (SWE); onder de drempels blijven Video 1 (SWE) en Video 2 (SWE). Dat komt overeen met de conversie-ranking en sluit de TODO in het command.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

---

### Log

| Tijd (UTC) | Actie | Resultaat |
|---|---|---|
| 11:26 | Pipeboard `get_insights` act_567892422940728, level ad, last_3d | http 200 in 2,6s, `{"data": []}` |
| 11:28 | Pipeboard `get_insights` act_567892422940728, level ad, last_30d | http 200 in 3,0s, 8 rijen met `actions` |
| 11:28 | PostHog sessions: sessies en betaalde sessies per dag sinds 12 sep | 0,34s, 0 betaald op elke dag |
| 11:28 | PostHog sessions: sessies op /become-a-distributor per dag | 0,37s |
| 11:28 | PostHog events: wholesaler funnel per dag sinds 15 sep | 0,37s |
| 11:30 | `update_ad` calls | Geen (0 ads gepauzeerd) |
