## Auto-Optimize Rapport, 5 september 2026

**Run:** 2026-09-05, Sempertex Ad Account `act_567892422940728`
**Bronnen:** Meta Ads (Pipeboard, directe JSON-RPC omdat de MCP "requires authentication" meldt) en PostHog (claude.ai connector, project STX EU). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.
**Periode:** last_3d = 2 t/m 4 september 2026

### Status van het account

**Er draait niets.** Beide Wholesaler campagnes (SWE en LIT), alle 8 ad sets en alle 8 ads staan op PAUSED. De pauze is op 4 september tussen 11:50 en 11:52 handmatig gezet, 25 minuten nadat auto-optimize Statisch 1 (LIT) had stilgezet. Het tweede account (AmbitionAvenue, `act_1489853856181844`) heeft geen campagnes. Het account `act_607231713057715` uit het command bestaat niet in de koppeling.

PostHog bevestigt dat het verkeer is gestopt: 237 wholesaler pageviews op 3 september, 61 op 4 september (tot de pauze), 1 op 5 september.

### Automatische acties uitgevoerd

Geen ads gepauzeerd. Er zijn geen actieve ads waarop de kill-regels van toepassing zijn.

**Totaal gepauzeerd door deze run: 0 ads**

### Slotcijfers laatste 3 draaidagen (2 t/m 4 september)

Ter referentie de cijfers waarop de kill-regels zouden hebben gedraaid als de ads nog actief waren. PostHog sessies en inzendingen zijn gekoppeld via `utm_content`.

| Ad | Spend | Impr. | Link clicks | Link CTR | CPC (link) | CPM | Freq. | Leads Meta | Sessies PostHog | Kill-regel |
|---|---|---|---|---|---|---|---|---|---|---|
| Statisch 2 (SWE) | €40,47 | 5.052 | 89 | 1,8% | €0,45 | €8,01 | 1,42 | 1 | 93 | Nee |
| Video 2 (SWE) | €45,23 | 2.871 | 43 | 1,5% | €1,05 | €15,75 | 1,52 | 1 | 32 | Nee |
| Statisch 1 (SWE) | €39,80 | 3.537 | 44 | 1,2% | €0,90 | €11,25 | 1,56 | 1 | 29 | Nee |
| Video 1 (SWE) | €38,38 | 2.733 | 31 | 1,1% | €1,24 | €14,04 | 1,45 | 0 | 19 | Nee |
| Video 1 (LIT) | €43,00 | 6.527 | 65 | 1,0% | €0,66 | €6,59 | 1,43 | 0 | 70 | Nee |
| Statisch 2 (LIT) | €41,87 | 10.533 | 98 | 0,9% | €0,43 | €3,98 | 1,62 | 0 | 101 | Nee |
| Video 2 (LIT) | €43,83 | 5.358 | 39 | 0,7% | €1,12 | €8,18 | 1,95 | 0 | 33 | Ja, Link CTR < 0,8% |
| Statisch 1 (LIT) | €42,91 | 11.213 | 64 | 0,6% | €0,67 | €3,83 | 2,32 | 0 | 47 | Ja, Link CTR < 0,8% (al gepauzeerd 4 sep 11:25) |
| **Totaal** | **€335,49** | **47.824** | **473** | **1,0%** | **€0,71** | **€7,02** | **2,34** | **3** | **424** | |

PostHog telde in deze 3 dagen 5 formulierinzendingen (3 op 2 sep, 1 op 3 sep, 1 op 4 sep) tegenover 3 leads bij Meta. Dat is €67,10 per inzending, tegenover ongeveer €25 in de eerste vijf campagnedagen. De pauze was terecht.

Video 2 (LIT) zou bij een herstart op dag 1 opnieuw de kill-regel raken (0,7% Link CTR bij 5.358 impressions). Zie voorstel 4.

### Waarschuwingen

| Ad | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| Video 2 (SWE) | Dure reach | CPM €15,75 | Niet opnieuw activeren zonder bredere SWE audience |
| Video 1 (SWE) | Dure reach en 0 inzendingen lifetime | CPM €14,04, €126,75 zonder inzending | Niet opnieuw activeren |
| Statisch 1 (LIT) | Frequency stijgt snel | 2,32 in 3 dagen, 3,97 campagne lifetime | Nieuwe eerste zin of andere audience |
| Video 2 (LIT) | Frequency stijgt snel | 1,95 in 3 dagen | Creative vervangen voor herstart |
| Wholesaler (LIT) | Creative fatigue campagnebreed | Freq. 3,97 lifetime, 4 ad sets op dezelfde audience | Ad sets samenvoegen |

### 70-20-10 Classificatie

Er zijn 0 actieve ads, dus er is geen actueel budget om te verdelen. Huidig budget per categorie: €0,00/dag. De classificatie hieronder is gebaseerd op de laatste 3 draaidagen plus de lifetime-cijfers uit het ads-rapport van vanochtend, en dient als uitgangspunt voor de herstart.

**70% Core (voorgesteld budget bij herstart: €100/dag van €140):**
- Statisch 2 (SWE): Link CTR 1,8%, CPC (link) €0,45, 93 sessies in 3 dagen, beste CTR van het account
- Video 1 (LIT): Link CTR 1,0%, CPC (link) €0,66, €29,38 per inzending lifetime
- Statisch 2 (LIT): Link CTR 0,9%, CPC (link) €0,43, meeste sessies van het account (101 in 3 dagen)

**20% Emerging (voorgesteld budget bij herstart: €30/dag):**
- Video 2 (LIT): Link CTR 0,7%, CPC (link) €1,12, maar goedkoopste leadbron lifetime (€28,75 per inzending). Alleen herstarten met nieuwe hook
- Statisch 1 (SWE): Link CTR 1,2%, CPC (link) €0,90, 1 lead in 3 dagen

**10% Experimental (voorgesteld budget bij herstart: €10/dag):**
- Statisch 1 (LIT): Link CTR 0,6%, maar beste sessie-naar-inzending ratio van LIT (3,2% lifetime). Alleen herstarten met nieuwe eerste zin

**Niet herstarten:**
- Video 1 (SWE): 0 inzendingen op €126,75 lifetime, CPM €14,04
- Video 2 (SWE): CPM €15,75, CPC (link) €1,05, €63,50 per inzending lifetime

**Budget mismatch:** Niet van toepassing, er draait niets. Bij de laatste configuratie kreeg elke ad €20/dag, dus Core kreeg 37,5% van het budget in plaats van 70%.

### Voorstellen (wacht op goedkeuring)

De voorstellen 1 t/m 5 uit de rapporten van 3 en 4 september staan nog open. Hieronder de geconsolideerde versie, aangepast aan de situatie dat alles stil staat.

**1. Tracking fixen voor de herstart**
- Meta zag 19 leads, PostHog 33 inzendingen over de hele campagne. 9 inzendingen hadden geen UTM.
- Meta optimaliseert op de helft van het signaal. Zolang dat zo is, wordt elke herstart duurder dan nodig.
- Actie: controleer de pixel lead-event op `/en_GB/become-a-distributor` en de UTM-doorgifte naar het formulier voordat er budget aan gaat.

**2. Budget herverdeling bij herstart (70-20-10, totaal €140/dag)**
- Statisch 2 (SWE): van €20/dag naar €40/dag (+100%)
- Video 1 (LIT): van €20/dag naar €30/dag (+50%)
- Statisch 2 (LIT): van €20/dag naar €30/dag (+50%)
- Video 2 (LIT): €20/dag, alleen met nieuwe hook
- Statisch 1 (SWE): van €20/dag naar €10/dag (-50%)
- Statisch 1 (LIT): van €20/dag naar €10/dag (-50%), alleen met nieuwe eerste zin
- Video 1 (SWE) en Video 2 (SWE): €0, niet herstarten
- Verwachte impact: zelfde totaalbudget, maar 71% naar de drie ads die samen de goedkoopste inzendingen leverden.

**3. Nieuwe hook-variaties**
- Alle 8 ads gebruikten tot nu toe exact dezelfde tekst per land. De enige variabele was het visual. Er is dus nog geen enkele hook getest.
- Gebaseerd op het winnende visual Statisch 2 (Link CTR 1,8% SWE, 0,9% LIT) stel ik per land drie tekstvarianten voor, volgens de Hormozi hook types:
  - Variatie A (Call Out, label): "Balloon shops in Sweden: your customers are asking for Sempertex. Here is how to stock it."
  - Variatie B (Bold statement): "The number one latex balloon brand for professionals is still not on your shelf."
  - Variatie C (Question): "How many decorators in your area order their balloons abroad because you do not carry them?"
- Zelfde drie varianten voor Litouwen met de landnaam aangepast. Format: statisch visual van Statisch 2, CTA-knop test SEE_DETAILS versus APPLY_NOW.

**4. Beslissing over Video 2 (LIT)**
- De ad raakt de kill-regel op Link CTR (0,7%), maar is lifetime de goedkoopste leadbron (€28,75 per inzending).
- Optie a: conversie-guard toevoegen aan de kill-regel (niet pauzeren als kosten per PostHog-inzending onder €40 liggen).
- Optie b: strikt pauzeren op Link CTR en de video alleen terugzetten met een nieuwe hook.
- Mijn advies: optie a, omdat lead-campagnes op inzendingen beoordeeld moeten worden, niet op doorklikratio.

**5. Audience en structuur**
- LIT: 4 ad sets samenvoegen naar 2 (statisch en video) met Advantage+ campagnebudget, zodat de frequency onder 3,5 blijft.
- SWE: audience verbreden naar 21+ en placements beperken tot feeds. De Zweedse CPM (€12,92 lifetime) is twee keer de Litouwse.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

### Log

| Timestamp | Actie | Reden |
|---|---|---|
| 2026-09-05 | Geen wijzigingen in Meta Ads | 0 actieve campagnes, 0 actieve ads |
