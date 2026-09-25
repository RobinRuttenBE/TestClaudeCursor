## Auto-Optimize Rapport, 25 september 2026

Run gestart: 2026-09-25 08:38 CEST. Bronnen: Pipeboard Meta Ads (directe JSON-RPC route, 1 call: ad-level last_3d, antwoord `weekly_limit_exceeded`) en PostHog project STX EU 149694 (directe REST-route, 2 HogQL queries, beide onder 0,4 seconde). De Pipeboard MCP-tools zelf meldden "requires authentication"; de directe route gebruikt dezelfde token en hetzelfde endpoint. Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.

Account: act_567892422940728 (Sempertex Ad Account). Het in het command genoemde act_607231713057715 bestaat niet (bekend sinds 2 september).

**Meta-weeklimiet vol.** De eerste en enige call kreeg `weekly_limit_exceeded` (30 van 30 gebruikt, reset_date 28 september 2026 00:00 UTC). Het ads-rapport van vanochtend 08:17 (3 calls, wél live) had het account nog bereikt. Deze run gebruikt daarom de campagnestatus uit dat ads-rapport en de per-ad link-tabel uit het live extract van 24 september (commit 0435a0b3). Beide zijn geldig: het ads-rapport van vanochtend bevestigde dat de 30d-cijfers per campagne identiek zijn aan 16, 21, 22 en 24 september, en PostHog bevestigt live dat er sinds 11 september geen betaalde sessie meer is geweest. Zonder levering veranderen per-ad cijfers niet.

### ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd.** Alle 7 campagnes staan op PAUSED (de twee Wholesaler Campagnes sinds 4 september, status uit het ads-rapport van 08:17 vanochtend). In het 3d-venster (22 t/m 24 september) was er nul levering: PostHog telt 0 sessies met `$entry_utm_source = 'facebook'` op elk van die dagen. Er was niets om de kill-regels op te draaien en er zijn geen `update_ad` calls gedaan. Tweeëntwintigste dag zonder levering.

**Totaal gepauzeerd: 0 ads** (log: 2026-09-25 08:38 CEST, reden: geen levering in het 3d-venster, Meta-call geblokkeerd door weeklimiet, PostHog bevestigt nul betaald verkeer).

### ⚠️ Waarschuwingen

Gelden op het laatste 30d-extract (25 augustus t/m 23 september) en worden pas actief bij herstart in de huidige vorm.

| Ad | Signaal | Waarde | Actie aanbevolen |
|----|---------|--------|-----------------|
| Video 2 (SWE) | Dure reach | CPM €17,07 (> €15,00) | Niet herstarten in deze vorm; audience te smal |
| Video 1 (SWE) | Dure reach | CPM €15,27 (> €15,00), 0 inzendingen op 113 sessies | Definitief uit |
| Statisch 1 (LIT) | Link CTR onder kill-drempel | Link CTR 0,6% op 28.434 impressies (< 0,8%) | Wordt bij herstart mechanisch gepauzeerd, maar is met €36,06 per inzending de derde beste converteerder. Conversie-guard nodig (voorstel 4) |
| Campagne LIT | Creative fatigue | Frequency 3,97 op campagneniveau (> 3,5); per ad max 2,91 | Verse creatives vóór herstart |
| Alle ads | Dalende Link CTR | Niet meetbaar, geen 3d-data | Geen |
| Rapportage | Meta-weeklimiet | 30 van 30, reset 28 september | Tot maandag geen Meta-calls meer doen; alle rapporten op het extract van 24 september plus PostHog |

CPC (link)-regel (> €1,50 na 500 link clicks): geen enkele ad haalt 500 link clicks (hoogste: Statisch 2 LIT met 297), dus niet van toepassing. Hoogste CPC (link) is Video 2 (SWE) met €1,11.

### Per-ad link-metrics (last 30d, 25 aug t/m 23 sep, extract van 24 september uit Meta en PostHog)

| Ad | Spend | Impr. | Link clicks | Link CTR | CPC (link) | All Clicks CTR | CPC (all) | CPM | Freq. | Meta leads | PostHog sessies | PostHog inz. | € / inz. (PostHog) | Conv. |
|----|------:|------:|------------:|---------:|-----------:|---------------:|----------:|----:|------:|-----------:|----------------:|-------------:|-------------------:|------:|
| Video 1 (LIT) | €146,91 | 19.041 | 242 | 1,3% | €0,61 | 2,4% | €0,32 | €7,72 | 1,90 | 3 | 248 | 5 | €29,38 | 2,0% |
| Video 2 (LIT) | €143,74 | 17.267 | 179 | 1,0% | €0,80 | 1,4% | €0,58 | €8,32 | 2,52 | 4 | 141 | 5 | €28,75 | 3,5% |
| Statisch 1 (LIT) | €144,24 | 28.434 | 163 | 0,6% | €0,88 | 1,0% | €0,49 | €5,07 | 2,91 | 3 | 134 | 4 | €36,06 | 3,0% |
| Statisch 2 (LIT) | €127,25 | 26.146 | 297 | 1,1% | €0,43 | 2,4% | €0,20 | €4,87 | 2,37 | 1 | 292 | 2 | €63,63 | 0,7% |
| Video 1 (SWE) | €126,75 | 8.299 | 139 | 1,7% | €0,91 | 2,9% | €0,53 | €15,27 | 2,05 | 0 | 113 | 0 | n.v.t. | 0,0% |
| Video 2 (SWE) | €127,00 | 7.441 | 114 | 1,5% | €1,11 | 2,5% | €0,69 | €17,07 | 2,02 | 1 | 97 | 2 | €63,50 | 2,1% |
| Statisch 1 (SWE) | €125,36 | 10.262 | 157 | 1,5% | €0,80 | 2,7% | €0,45 | €12,22 | 2,15 | 2 | 131 | 2 | €62,68 | 1,5% |
| Statisch 2 (SWE) | €128,13 | 13.265 | 286 | 2,2% | €0,45 | 4,0% | €0,24 | €9,66 | 1,97 | 5 | 256 | 3 | €42,71 | 1,2% |
| **Totaal** | **€1.069,38** | **130.155** | **1.577** | **1,2%** | **€0,68** | **2,2%** | **€0,37** | **€8,22** | | **19** | **1.412** | **23** | **€46,49** | **1,6%** |

Definities: Link clicks = `actions.link_click`; Link CTR = link clicks / impressies; CPC (link) = spend / link clicks. PostHog sessies = sessions met `$entry_utm_source = 'facebook'` per `$entry_utm_campaign` en `$entry_utm_content`; PostHog inzendingen = unieke sessies met `wholesaler_form_submit` via join op sessions. Daarnaast 9 inzendingen zonder UTM (organisch, waaronder Letland 18 sep en Malta 20 sep), totaal 32 unieke inzend-sessies in 30d. Link CTR is gemiddeld 55% van All Clicks CTR, CPC (link) 1,8 keer CPC (all). Het venster van vandaag (26 aug t/m 24 sep) bevat dezelfde levering: 25 augustus had nog geen spend (eerste betaalde sessie 27 augustus) en 24 september had nul betaald verkeer. Vanaf 27 september valt 27 augustus uit het venster en gaan de LIT-cijfers dalen zonder dat er iets gebeurde.

### 📊 70-20-10 Classificatie

Richtlijn-drempels (nog niet gekalibreerd op link-metrics, zie TODO in het command). Geen budget-shifts uitgevoerd. Alle ads staan op PAUSED; "budget" is het 30d-aandeel in de spend van €1.069,38.

**70% Core (huidig 12,0% van totaal):**
- Statisch 2 (SWE): Link CTR 2,2%, CPC (link) €0,45, 3 inzendingen à €42,71. Enige ad die beide Core-drempels haalt.

**20% Emerging (huidig 51,9% van totaal):**
- Video 1 (LIT): Link CTR 1,3%, CPC (link) €0,61, €29,38 per inzending. Op conversie een Core-kandidaat.
- Video 2 (LIT): Link CTR 1,0%, CPC (link) €0,80, €28,75 per inzending, beste conversie (3,5%). Op conversie een Core-kandidaat.
- Statisch 2 (LIT): Link CTR 1,1%, CPC (link) €0,43, maar 0,7% conversie. Goedkoop verkeer dat niet invult.
- Statisch 1 (SWE): Link CTR 1,5%, CPC (link) €0,80, €62,68 per inzending.

**10% Experimental (huidig 0,0% van totaal):**
- Geen. Alle 8 ads hebben ruim boven 500 impressies.

**Buiten de indeling (huidig 36,1% van totaal):**
- Statisch 1 (LIT): Link CTR 0,6% onder de kill-drempel, maar €36,06 per inzending. Zonder conversie-guard verdwijnt een goede converteerder.
- Video 1 (SWE): CPC (link) €0,91, CPM €15,27, 0 inzendingen. Uit.
- Video 2 (SWE): CPC (link) €1,11, CPM €17,07. Uit.

**Budget mismatch: Ja.** De enige Core-ad kreeg 12,0% in plaats van 70%, en 36,1% ging naar drie ads die op link-metrics of conversie afvallen. Belangrijker: de link-metric indeling en de conversie-ranking spreken elkaar tegen. Op kosten per inzending is de top drie Video 2 (LIT), Video 1 (LIT), Statisch 1 (LIT); op Link CTR staan die op plek 5, 4 en 8. Daarom geen mechanische budget-shift op de richtlijn-drempels (voorstel 7).

### PostHog funnel /become-a-distributor (live, 25 september 08:38 CEST)

| Dag | Sessies site | Betaald (facebook) | Pageviews site | Sessies distributor-pagina | wholesaler_page_view | form_start | form_submit | form_error |
|-----|------:|------:|------:|------:|------:|------:|------:|------:|
| 18 sep | 1.654 | 0 | 4.136 | 4 | | | | |
| 19 sep | 2.682 | 0 | 5.056 | 2 | | | | |
| 20 sep | 1.457 | 0 | 3.903 | 4 | | | | |
| 21 sep | 2.175 | 0 | 8.211 | 4 | 4 | 0 | 0 | 0 |
| 22 sep | 1.155 | 0 | 6.563 | 6 | 3 | 0 | 0 | 0 |
| 23 sep | 643 | 0 | 5.655 | 3 | 3 | 0 | 0 | 0 |
| 24 sep | 530 | 0 | 4.702 | 4 | 4 | 0 | 0 | 0 |
| 25 sep (tot run) | 29 | 0 | 183 | 0 | 0 | 0 | 0 | 0 |

Geen nieuwe inzendingen sinds Malta op 20 september; vijfde dag op rij zonder formulierstart. Organisch verkeer op de pagina blijft 3 tot 6 sessies per dag. Sitebreed dalen de sessies sinds 21 september (2.175 naar 530), terwijl de pageviews per sessie stijgen (3,8 naar 8,9); dat wijst op minder, maar dieper klikkend verkeer, mogelijk het wegvallen van een bot- of preview-golf rond het weekend. Niet relevant voor de kill-regels, wel voor de SYBB-rapportage.

### 💡 Voorstellen (wacht op goedkeuring)

Dezelfde zeven als op 22 en 24 september, ongewijzigd omdat de data ongewijzigd is. Niets uitgevoerd.

**1. Budget herverdeling bij herstart** (totaal €140,00 per dag: LIT €100,00, SWE €40,00)
- Video 2 (LIT): van €0,00 (gepauzeerd, was circa €4,80) naar €35,00 per dag. Reden: beste conversie (3,5%) en laagste kosten per inzending (€28,75).
- Video 1 (LIT): naar €30,00 per dag. Reden: €29,38 per inzending, Link CTR 1,3%.
- Statisch 1 (LIT): naar €20,00 per dag, alleen mét conversie-guard (voorstel 4). Reden: €36,06 per inzending ondanks Link CTR 0,6%.
- Statisch 2 (LIT): naar €15,00 per dag met nieuwe hook (voorstel 2). Reden: goedkoopste link clicks (€0,43), slechtste conversie (0,7%).
- Statisch 2 (SWE): naar €25,00 per dag. Reden: enige Core-ad op link-metrics, Link CTR 2,2%.
- Statisch 1 (SWE): naar €15,00 per dag. Reden: Emerging, €62,68 per inzending.
- Video 1 (SWE) en Video 2 (SWE): €0,00. Reden: CPM boven €15,00, CPC (link) boven €0,90, samen 2 inzendingen op €253,75.
- Verwachte impact: bij gelijke conversie circa 3,5 tot 4 inzendingen per dag in plaats van 1,2 per dag in de oorspronkelijke run.

**2. Nieuwe variaties**
- Gebaseerd op winnende hook Statisch 2 (SWE) (Link CTR 2,2%): variatie A als Zweedse video-versie van dezelfde hook (video-format, zelfde CTA); variatie B als statische versie met Proof-hook (aantal actieve Zweedse wholesalers, Sempertex heritage) in plaats van de huidige hook.
- Gebaseerd op Video 2 (LIT) (beste conversie 3,5%): Zweedse vertaling met identieke body en CTA, nieuwe ad set in campagne SWE.
- Gebaseerd op Statisch 2 (LIT) (veel clicks, weinig inzendingen): nieuwe Vraag-hook gericht op wholesalers die al latex verkopen, met de aanvraagdrempel expliciet in de body, zodat de klik beter kwalificeert.
- Concrete copy volgt zodra ik de huidige ad-copy mag ophalen; dat kost één extra Meta-call (get_ad_creatives), op zijn vroegst maandag 28 september na de reset.

**3. Audience aanpassingen**
- LIT: de vier ad sets samenvoegen tot één ad set met de vier creatives, zodat Meta zelf verdeelt en de frequency (3,97 op campagneniveau) daalt.
- Alle campagnes: Audience Network uitsluiten als placement. Reden: goedkope clicks zonder inzendingen passen bij dat placement-patroon; te verifiëren met een placement-breakdown na herstart.
- SWE: verbreden (interesse-targeting losser of Advantage+ audience). Reden: CPM €12,22 tot €17,07 wijst op een te smal publiek.
- Testlanden: Letland en Malta als kleine testad sets (€5,00 per dag elk). Reden: de enige twee organische inzendingen sinds de pauze kwamen daar vandaan (18 en 20 september).

**4. Conversie-guard op de kill-regels**
- Een ad met kosten per inzending onder €40,00 (PostHog) wordt niet automatisch gepauzeerd op Link CTR alleen. Reden: Statisch 1 (LIT) zou anders bij herstart direct uitgaan.

**5. Formulierfout en pixel-lead-event fixen vóór herstart**
- 30d: 22 formulierfouten op 141 starts (15,6%); Meta telde 19 leads tegenover 23 geattribueerde PostHog-inzendingen. Eerst dichten, dan budget.

**6. Eén gedeeld Meta-extract per dag**
- Ads-report, SYBB-rapport en auto-optimize gebruiken nu elk eigen calls. De limiet van 30 per week zat vandaag, vrijdag, al vol vóór deze run, terwijl het ads-rapport van 08:17 nog 3 calls kon doen. Eén cache-bestand per dag houdt de limiet de hele week open en voorkomt dat de derde run van de dag structureel zonder Meta-data draait.

**7. Nieuwe 70-20-10 drempels op link-metrics**
- Voorstel: Core = Link CTR > 1,0% én CPC (link) < €0,70 óf kosten per inzending < €40,00; Emerging = Link CTR 0,6% tot 1,0% of CPC (link) €0,70 tot €1,00; Experimental = < 500 impressies. Dan komen Video 1 (LIT), Video 2 (LIT), Statisch 1 (LIT) en Statisch 2 (SWE) in Core, wat overeenkomt met de conversie-ranking.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

---
Meta weekverbruik: 30 van 30, reset 28 september 00:00 UTC. Tot dan doen ads-report, SYBB en auto-optimize alleen nog de ene testcall en draaien op dit extract plus PostHog. Opmerking bij het archief: de bestanden van 21, 22 en 24 september bevatten op schijf alleen de chatsamenvatting; de volledige per-ad tabel van 24 september staat in commit 0435a0b3. Controleer na opslaan met grep op "CPC (link)".
