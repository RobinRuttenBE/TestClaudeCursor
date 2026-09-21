## Auto-Optimize Rapport, 21 september 2026

Run: 2026-09-21 13:21 CEST. Bronnen: Pipeboard Meta Ads (directe JSON-RPC route, 2 calls: ad-level last_3d en ad-level last_30d) en PostHog (directe REST-route, 2 queries). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven. Account: act_567892422940728 (Sempertex Ad Account). Het tweede account uit het command (act_607231713057715) bestaat niet in de koppeling.

**Meta was live bereikbaar.** De Pipeboard-weeklimiet is vannacht gereset. Verbruik vandaag: 3 calls (ads-rapport) + 1 (SYBB) + 2 (deze run) = 6 van 30. Blijf onder circa 5 per dag om de week te halen.

### Automatische acties uitgevoerd

| Ad | Reden | Was | Nu | Performance |
|----|-------|-----|-----|-------------|
| geen | | | | |

**Totaal gepauzeerd: 0 ads.** Geen ads gepauzeerd, er draait niets. De ad-level call met `date_preset: last_3d` (18 t/m 20 september) gaf `{"data": []}`. Alle 7 campagnes staan op PAUSED (status uit het ads-rapport van 13:06 vandaag), de twee Wholesaler Campagnes sinds 4 september 11:50. Achttiende dag zonder levering. Geen `update_ad` calls gedaan.

**PostHog bevestigt live:** 0 sessies met `$entry_utm_source = 'facebook'` of `'meta'` op 14 t/m 21 september (1.457 tot 4.537 site-brede sessies per dag, allemaal organisch of intern). Laatste betaalde sessies blijven 9 september.

### Per-ad Link-metrics (30d, 22 augustus t/m 20 september, live opgehaald)

Dit is de eerste keer sinds 7 september dat de per-ad link-cijfers vers uit Meta komen. Deze tabel is de fallback voor de rest van de week zodra de limiet weer dichtgaat. PostHog-inzendingen komen uit het ads-rapport van vanochtend (sessie-join).

| Ad | Ad ID | Spend | Impr. | Link clicks | Link CTR | CPC (link) | All Clicks CTR | CPC (all) | CPM | Freq. | Meta leads | PostHog inz. | € / inz. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Video 1 (LIT) | 120250159503120239 | €146,91 | 19.041 | 242 | 1,3% | €0,61 | 2,4% | €0,32 | €7,72 | 1,90 | 3 | 5 | €29,38 |
| Video 2 (LIT) | 120250160387390239 | €143,74 | 17.267 | 179 | 1,0% | €0,80 | 1,4% | €0,58 | €8,32 | 2,52 | 4 | 5 | €28,75 |
| Statisch 1 (LIT) | 120250160534150239 | €144,24 | 28.434 | 163 | 0,6% | €0,88 | 1,0% | €0,49 | €5,07 | 2,91 | 3 | 4 | €36,06 |
| Statisch 2 (LIT) | 120250161077250239 | €127,25 | 26.146 | 297 | 1,1% | €0,43 | 2,4% | €0,20 | €4,87 | 2,37 | 1 | 2 | €63,63 |
| Video 1 (SWE) | 120250180000300239 | €126,75 | 8.299 | 139 | 1,7% | €0,91 | 2,9% | €0,53 | €15,27 | 2,05 | 0 | 0 | n.v.t. |
| Video 2 (SWE) | 120250180392100239 | €127,00 | 7.441 | 114 | 1,5% | €1,11 | 2,5% | €0,69 | €17,07 | 2,02 | 1 | 2 | €63,50 |
| Statisch 1 (SWE) | 120250180580670239 | €125,36 | 10.262 | 157 | 1,5% | €0,80 | 2,7% | €0,45 | €12,22 | 2,15 | 2 | 2 | €62,68 |
| Statisch 2 (SWE) | 120250180888540239 | €128,13 | 13.265 | 286 | 2,2% | €0,45 | 4,0% | €0,24 | €9,66 | 1,97 | 5 | 3 | €42,71 |
| **Totaal** | | **€1.069,38** | **130.155** | **1.577** | **1,2%** | **€0,68** | 2,2% | €0,37 | €8,22 | | 19 | 23 via ad | €46,49 via ad |

Link CTR ligt gemiddeld op 55% van de All Clicks CTR en CPC (link) is 1,8 keer de CPC (all). Dat is precies de vertekening waar het command voor waarschuwt: op all-clicks lijkt elke ad gezond, op link clicks halen 2 van de 8 ads de Core-drempel niet eens bij benadering.

**Kill-regels getoetst op deze 30d-cijfers (informatief, niet uitgevoerd, er is geen actieve ad met 24 uur levering):**

- Link CTR < 0,8% bij minimaal 1.000 impressions: **Statisch 1 (LIT)** triggert met 0,6% op 28.434 impressions. Dit is tegelijk de ad met de derde laagste kosten per inzending (€36,06). Zonder conversie-guard sneuvelt deze ad op de eerste volle dag na herstart. Zie voorstel 4.
- CPC (link) > €1,50 bij minimaal 500 link clicks: geen enkele ad heeft 500 link clicks (hoogste: Statisch 2 (LIT) met 297). Niet van toepassing.

### Waarschuwingen

Alle waarschuwingen zijn 30d-cijfers en gelden bij een herstart in de huidige vorm.

| Ad | Signaal | Waarde | Actie aanbevolen |
|----|---------|--------|-----------------|
| Wholesaler Campagne (LIT) | Creative fatigue | Freq 3,97 (campagne-niveau) | Verse creatives vóór herstart, LIT ad sets samenvoegen |
| Video 2 (SWE) | Dure reach en dure clicks | CPM €17,07, CPC (link) €1,11 | Niet herstarten |
| Video 1 (SWE) | Dure reach, nul conversie | CPM €15,27, 0 inzendingen op 139 link clicks | Definitief uit |
| Statisch 1 (LIT) | Lage Link CTR | 0,6% | Audience-fix (25-65, geen desktop) en conversie-guard |
| Statisch 2 (LIT) | Clicks zonder conversie | CPC (link) €0,43 maar €63,63 per inzending | Nieuwe hook testen, niet opschalen op clicks |
| Dalende Link CTR | n.v.t. | Geen last_3d data | Pas meetbaar na herstart |

**PostHog wholesaler-funnel, 14 t/m 21 september (live):** 23 organische pageviews op /become-a-distributor, 7 formulierstarts, 1 formulierfout (20 september), 2 inzendingen (Letland 18 september, Malta 20 september). Vandaag tot nu toe 1 pageview. Het formulier hapert dus ook zonder betaald verkeer; de 24,8% doorloop van start naar inzending uit het ads-rapport staat.

### 70-20-10 Classificatie

Gebaseerd op de 30d Link-metrics hierboven. De drempels uit het command zijn nog gekalibreerd op all-clicks (TODO in het command), dus dit is een richtlijn, geen hard oordeel. Er draait momenteel niets, dus het huidige budget per categorie is €0,00. De percentages verwijzen naar de verdeling zoals die tot 4 september liep (8 ads x €20,00 = €160,00 per dag).

**70% Core (huidig budget €0,00, tot 4 september 12,5% van totaal):**
- Statisch 2 (SWE), Link CTR 2,2%, CPC (link) €0,45, €42,71 per inzending. De enige ad die beide Core-drempels haalt.

**20% Emerging (huidig budget €0,00, tot 4 september 50,0% van totaal):**
- Video 1 (LIT), Link CTR 1,3%, CPC (link) €0,61, €29,38 per inzending. Op conversie de nummer 2.
- Video 2 (LIT), Link CTR 1,0%, CPC (link) €0,80, €28,75 per inzending. Op conversie de nummer 1.
- Statisch 2 (LIT), Link CTR 1,1%, CPC (link) €0,43, €63,63 per inzending. Goedkoopste link clicks, zwakste converteerder.
- Statisch 1 (SWE), Link CTR 1,5%, CPC (link) €0,80, €62,68 per inzending.

**10% Experimental (huidig budget €0,00):**
- Geen nieuwe ads. Alle 8 ads hebben meer dan 7.000 impressions.

**Buiten de indeling (tot 4 september 37,5% van totaal):**
- Video 1 (SWE), Link CTR 1,7% maar CPC (link) €0,91 en 0 inzendingen. Stoppen.
- Video 2 (SWE), Link CTR 1,5% maar CPC (link) €1,11. Stoppen.
- Statisch 1 (LIT), Link CTR 0,6%, CPC (link) €0,88, maar €36,06 per inzending. Mechanisch een kill, op conversie een blijver.

**Budget mismatch:** Ja. Tot de pauze kreeg de enige Core-ad 12,5% van het budget en ging 37,5% naar de drie ads die op link-metrics of conversie afvallen. Bij herstart moet dat omgedraaid worden, zie voorstel 1.

**Kanttekening bij de indeling:** de link-metrics en de conversie-ranking spreken elkaar op twee ads tegen (Statisch 1 (LIT) en Statisch 2 (LIT)). Voor een lead-campagne is kosten per inzending de betere maat. Voorstel 7 legt daarom nieuwe drempels vast die beide combineren.

### Voorstellen (wachten op goedkeuring)

**1. Herstart en budget herverdeling** (nieuw uitgewerkt op link-metrics, budget €140,00 per dag)
- Wholesaler (LIT), €100,00 per dag:
  - Video 2 (LIT): van €20,00 naar €25,00 per dag (+25%). Beste kosten per inzending.
  - Video 1 (LIT): van €20,00 naar €25,00 per dag (+25%). Tweede beste kosten per inzending.
  - Statisch 1 (LIT): van €20,00 naar €20,00 per dag (0%), alleen met audience-fix uit voorstel 3 en conversie-guard uit voorstel 4.
  - Statisch 2 (LIT): van €20,00 naar €15,00 per dag (-25%), met nieuwe Vraag-hook uit voorstel 2.
  - Nieuwe creative (LIT): €15,00 per dag als Experimental.
- Wholesaler (SWE), €40,00 per dag:
  - Statisch 2 (SWE): van €20,00 naar €28,00 per dag (+40%). Enige Core-ad.
  - Zweedse variant van Video 2 (LIT): €12,00 per dag als Experimental.
  - Video 1 (SWE), Video 2 (SWE), Statisch 1 (SWE): van €20,00 naar €0,00 per dag. Statisch 1 (SWE) is Emerging op link-metrics maar €62,68 per inzending rechtvaardigt geen budget naast Statisch 2 (SWE).
- Reden: Core en de twee beste converteerders krijgen samen 55,7% van het budget in plaats van 37,5%, de drie zwakste ads gaan van 37,5% naar 0%.
- Verwachte impact: bij gelijke conversiekosten circa 4 inzendingen per dag in plaats van 1,2 (35 inzendingen in 30 dagen tot 4 september), voor 12,5% minder dagbudget.
- Voorwaarde: eerst voorstel 5 (funnel fix).

**2. Nieuwe variaties**
Top 3 hooks op Link CTR zijn Statisch 2 (SWE) 2,2%, Video 1 (SWE) 1,7% en Statisch 1 (SWE) / Video 2 (SWE) 1,5%. Alle 8 ads delen dezelfde copy, dus het verschil zit in de visual en het land, niet in de hook. De hook-test is nog niet gestart.
- Op de Statisch 2 (SWE) visual, drie hooks volgens Hormozi: Statement (claim over marge of levertijd), Label (spreekt de professionele decorateur direct aan), Vraag (opent met het probleem van onbetrouwbare voorraad). Andere CTA per variant.
- Zweedse variant van Video 2 (LIT), zelfde script, Zweedse ondertiteling en landing.
- Nieuwe Vraag-hook voor Statisch 2 (LIT), om te toetsen of de goedkope clicks met een scherpere kwalificatie wél converteren.
- De exacte huidige copy heb ik deze run niet opgehaald (kost een extra Meta-call, `get_ad_creatives`). Zeg het als ik die morgen mag doen.

**3. Audience aanpassingen**
- LIT ad sets samenvoegen tot één ad set. Reden: frequency 3,97 op campagne-niveau tegenover 1,9 tot 2,9 per ad, het publiek overlapt.
- Audience Network overal uitsluiten. Reden: op 3 september kwam 37% van de link clicks van Video 2 (LIT) uit Audience Network.
- Statisch 1 (LIT) naar 25-65 en desktop uitsluiten. Reden: de lage Link CTR zat in Facebook desktop, wie doorklikt converteert.
- SWE audience verbreden. Reden: CPM €12,22 tot €17,07 tegenover €4,87 tot €8,32 in LIT.
- Letland en Malta toevoegen als testlanden in een Experimental ad set. Reden: twee organische inzendingen (18 en 20 september) zonder betaald verkeer.

**4. Conversie-guard op de kill-regels**
Pauzeer niet op Link CTR < 0,8% als de ad in de laatste 3 dagen minimaal 1 PostHog-inzending onder €40,00 heeft. Zonder deze regel pauzeert auto-optimize Statisch 1 (LIT) op de eerste volle dag na herstart.

**5. Funnel fix vóór herstart**
Van 141 formulierstarts komen 35 door (24,8%), 22 fouten in 30 dagen en opnieuw een fout op 20 september. Meta telt 19 leads tegenover 35 in PostHog. Eerst het formulier en de pixel repareren, anders koopt voorstel 1 verkeer voor een lekkende pagina.

**6. Eén gedeeld Meta-extract per dag**
Drie rapporten per dag deden vorige week 30 calls vóór woensdag. Vandaag 6 calls. Eén cache-bestand per ochtend houdt de limiet de hele week open.

**7. Nieuw: drempels 70-20-10 kalibreren op link-metrics** (sluit de TODO in het command)
Op basis van de echte 30d-verdeling (Link CTR 0,6% tot 2,2%, mediaan 1,4%; CPC (link) €0,43 tot €1,11, mediaan €0,80):
- Core: Link CTR > 1,5% én CPC (link) < €0,60, óf kosten per PostHog-inzending < €40,00.
- Emerging: Link CTR 0,8% tot 1,5% óf CPC (link) €0,60 tot €0,90, én kosten per inzending < €70,00.
- Experimental: minder dan 500 impressions.
- Alles daarbuiten stopt.
Met deze drempels vallen Video 1 (LIT), Video 2 (LIT), Statisch 1 (LIT) en Statisch 2 (SWE) in Core, wat overeenkomt met de conversie-ranking.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers (1 t/m 7).**

### Log

- 2026-09-21 13:21 CEST: ad-level `get_insights` last_3d op act_567892422940728: 0 rijen. Geen actieve ads, geen kill-regel toegepast, geen `update_ad` calls.
- 2026-09-21 13:21 CEST: ad-level `get_insights` last_30d: 8 rijen, per-ad link-tabel opgeslagen in dit bestand.
- 2026-09-21 13:21 CEST: PostHog sessions per dag (14 t/m 21 september): 0 betaalde sessies. Wholesaler-events: 2 organische inzendingen, 1 fout.
