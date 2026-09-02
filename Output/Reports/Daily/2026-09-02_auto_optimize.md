## Auto-Optimize Rapport, 2 september 2026

**Gegenereerd:** 2026-09-02 08:11
**Periode:** last_3d (30 augustus t/m 1 september 2026), Sempertex Ad Account act_567892422940728
**Databron:** Meta Ads via Pipeboard (directe JSON-RPC call, de MCP zelf meldde "requires authentication"). PostHog MCP gaf een 405 en is niet gebruikt; dit command heeft PostHog niet nodig omdat de wholesaler-landingspagina's niet op startyourballoonbusiness.com staan. Geen Google MCPs aangeroepen, niets naar de Tracker Sheet geschreven. Het account act_607231713057715 uit het command bestaat niet.

**Actieve campagnes:** Wholesaler Campagne (SWE) en Wholesaler Campagne (LIT). Beide OUTCOME_LEADS, 4 ad sets per campagne, elk €20,00/dag, optimalisatie op OFFSITE_CONVERSIONS. Totaal €160,00/dag. SYBB en Nozzle Up staan gepauzeerd.

**Alle metrics hieronder zijn LINK metrics** (link_click uit actions), niet Meta's all-clicks velden.

### Overzicht per ad (last_3d)

| Ad | Impr. | Link clicks | Link CTR | CPC (link) | CPM | Freq. | Spend | Leads | CPL |
|---|---|---|---|---|---|---|---|---|---|
| Statisch 2 (SWE) | 5.206 | 94 | 1,8% | €0,65 | €11,71 | 1,59 | €60,94 | 1 | €60,94 |
| Video 1 (SWE) | 3.804 | 64 | 1,7% | €0,95 | €15,98 | 1,67 | €60,80 | 0 | n.v.t. |
| Statisch 1 (SWE) | 4.564 | 63 | 1,4% | €0,92 | €12,75 | 1,75 | €58,17 | 1 | €58,17 |
| Video 2 (SWE) | 3.051 | 44 | 1,4% | €1,25 | €18,04 | 1,70 | €55,05 | 0 | n.v.t. |
| Statisch 2 (LIT) | 11.123 | 130 | 1,2% | €0,45 | €5,29 | 1,86 | €58,88 | 1 | €58,88 |
| Video 1 (LIT) | 7.547 | 84 | 1,1% | €0,72 | €8,03 | 1,63 | €60,61 | 2 | €30,31 |
| Video 2 (LIT) | 6.470 | 60 | 0,9% | €0,94 | €8,73 | 2,10 | €56,48 | 1 | €56,48 |
| Statisch 1 (LIT) | 10.306 | 52 | **0,5%** | €1,13 | €5,70 | 2,19 | €58,79 | **3** | **€19,60** |
| **Totaal** | **52.071** | **591** | **1,1%** | **€0,79** | **€9,02** | | **€469,72** | **9** | **€52,19** |

Campagneniveau: SWE Link CTR 1,6%, CPC (link) €0,89, 2 leads (CPL €117,48). LIT Link CTR 0,9%, CPC (link) €0,72, 7 leads (CPL €33,54).

### ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd.** Toelichting per regel:

| Regel | Resultaat |
|---|---|
| CPC (link) > €1,50 na ≥ 500 link clicks | Geen enkele ad heeft 500 link clicks (hoogste: Statisch 2 (LIT) met 130). Regel niet van toepassing. |
| Link CTR < 0,8% na ≥ 1.000 impressions | **Eén ad triggert: Statisch 1 (LIT)**, Link CTR 0,5% op 10.306 impressions. **Niet gepauzeerd, zie hieronder.** |

**Waarom Statisch 1 (LIT) niet automatisch is gepauzeerd**

De kill-regel is ontworpen om duidelijke underperformers te stoppen. Deze ad is op Link CTR de zwakste van de acht, maar op het campagnedoel (leads) de sterkste:

- 3 van de 7 LIT-leads in de afgelopen 3 dagen, CPL €19,60 (campagnegemiddelde €33,54, SWE €117,48)
- Lifetime: 3 leads bij €103,64 spend, CPL €34,55, tegenover Statisch 2 (LIT) met 1 lead bij €87,27 (CPL €87,27)
- De ad set optimaliseert op OFFSITE_CONVERSIONS, niet op link clicks. Meta stuurt hier op leads, en dat werkt.

De lage Link CTR heeft een aanwijsbare oorzaak: dit is de enige ad set met leeftijd 18-65 in plaats van 25-65, en de enige met noemenswaardig desktop-bereik. Het segment 18-24 (1.128 impressions, 0 leads) en desktop (1.028 impressions, Link CTR 0,2%, 0 leads) drukken het gemiddelde. Alle 3 leads komen uit 35-44 op mobiel.

Mechanisch pauzeren zou de goedkoopste leadbron van het account uitzetten en de learning phase van die ad set resetten. Dat is moeilijker terug te draaien dan één dag wachten. **Beslissing ligt bij Robin, zie voorstel 4.** Als je de regel strikt wilt toepassen, is het commando klaar:

```
update_ad {"ad_id": "120250160534150239", "status": "PAUSED"}
```

**Totaal gepauzeerd: 0 ads** (0 van 8, ruim onder de 50%-grens). Alle ads draaien sinds 27 of 28 augustus, dus de 24-uursregel is overal gehaald.

### ⚠️ Waarschuwingen

| Ad | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| Video 2 (SWE) | Dure reach | CPM €18,04 (> €15) | Pauzeren, 0 leads lifetime na €84,30 (voorstel 1) |
| Video 1 (SWE) | Dure reach | CPM €15,98 (> €15) | Budget halveren tot 4 september, dan beslissen (voorstel 1) |
| Video 2 (SWE) | Instagram placement lekt | Instagram Link CTR 0,5%, CPC (link) €3,85 op €19,25 spend | Instagram uitsluiten als de ad blijft draaien |
| Statisch 2 (SWE) | Dalende Link CTR | 3d 1,8% = 74% van lifetime 2,4% | Nog boven de 70%-grens. Morgen opnieuw checken; nieuwe visual klaarzetten |
| Video 2 (LIT) | Link CTR nadert drempel | 0,9% (drempel 0,8%) | Monitoren, morgen mogelijk kill-trigger |
| Beide campagnes | Funnel-lek link click naar landing page view | SWE 45 LPV op 265 link clicks (17%), LIT 40 op 326 (12%) | Laadsnelheid en pixel van de wholesaler-pagina checken. Dit was gisteren ook al de grootste bevinding |

Creative fatigue (frequency > 3,5): geen enkele ad boven 2,2 over de laatste 3 dagen. Lifetime zit Statisch 1 (LIT) op 2,64, de LIT-doelgroep is klein, dus binnen een week nieuwe visuals nodig.

### 📊 70-20-10 Classificatie

De 70-20-10 drempels zijn nog niet gekalibreerd op link metrics (zie TODO in het command). Geen enkele ad haalt strikt Link CTR > 1,5% én CPC (link) < €0,50. Omdat dit lead-campagnes zijn, weegt CPL mee in de indeling. Classificatie is een richtlijn, geen hard oordeel.

**70% Core (budget: €40,00/dag, huidig 25% van totaal):**
- Statisch 2 (SWE): Link CTR 1,8%, CPC (link) €0,65, lifetime 4 leads bij CPL €22,14 (beste van het account)
- Statisch 2 (LIT): Link CTR 1,2%, CPC (link) €0,45 (laagste van het account), 130 link clicks in 3 dagen, maar pas 1 lead lifetime

**20% Emerging (budget: €80,00/dag, huidig 50% van totaal):**
- Video 1 (LIT): Link CTR 1,1%, CPC (link) €0,72, 2 leads in 3 dagen (CPL €30,31), potentieel
- Statisch 1 (LIT): Link CTR 0,5%, CPC (link) €1,13, maar 3 leads (CPL €19,60), leadmachine met zwakke klikratio
- Video 2 (LIT): Link CTR 0,9%, CPC (link) €0,94, lifetime 4 leads (CPL €25,40), klikratio zakt richting drempel
- Statisch 1 (SWE): Link CTR 1,4%, CPC (link) €0,92, 1 lead lifetime (CPL €87,53)

**10% Experimental (budget: €40,00/dag, huidig 25% van totaal):**
- Video 1 (SWE): Link CTR 1,7%, CPC (link) €0,95, CPM €15,98, 0 leads lifetime na €90,11
- Video 2 (SWE): Link CTR 1,4%, CPC (link) €1,25, CPM €18,04, 0 leads lifetime na €84,30

**Budget mismatch: Ja.** Core krijgt 25% in plaats van 70%, de twee SWE-video's zonder leads krijgen samen 25% in plaats van 10%. Ideale verdeling bij €160,00/dag: Core €112,00, Emerging €32,00, Experimental €16,00.

### 💡 Voorstellen (wacht op goedkeuring)

**1. Budget herverdeling**
- Statisch 2 (SWE): van €20,00/dag naar €35,00/dag (+75%). Reden: beste CPL van het account (€22,14 lifetime), hoogste Link CTR in SWE. Verwachte impact: 1 tot 2 extra Zweedse leads per week bij gelijke CPL.
- Statisch 2 (LIT): van €20,00/dag naar €30,00/dag (+50%). Reden: goedkoopste link clicks (€0,45), meeste volume. Kanttekening: pas 1 lead lifetime, dus verhoging is een test op conversie, niet alleen op klik.
- Video 2 (SWE): pauzeren (van €20,00/dag naar €0,00). Reden: 0 leads na €84,30, CPC (link) €1,25, CPM €18,04, Instagram-placement Link CTR 0,5%. Gisteren al aanbevolen. Bespaart €140,00/week.
- Video 1 (SWE): van €20,00/dag naar €10,00/dag (-50%) tot 4 september. Reden: Link CTR 1,7% is prima, maar 0 leads na €90,11 en CPM €15,98. Geen lead op 4 september: pauzeren.
- Nieuw totaal: €155,00/dag (SWE €65,00, LIT €90,00). Core-aandeel stijgt van 25% naar 42%. Volledige 70% is pas haalbaar zodra de nieuwe varianten uit voorstel 2 bewijzen dat ze leads opleveren.

**2. Nieuwe variaties**

Alle 8 ads gebruiken exact dezelfde copy: kop "Become a Sempertex partner in Sweden/Lithuania", body "Sempertex Europe is looking for official wholesale partners in ... Party shops and wholesalers: premium latex balloons, shipped from Belgium, with a ready-to-sell starter package. Two minute form, then an intake call." Het verschil in Link CTR zit dus volledig in de visual. Winnende visual: Statisch 2 (Link CTR 1,8% SWE, 1,2% LIT). De huidige hook is een Statement. Voorstel: 3 copy-varianten op de Statisch 2 visual, per land, zodat we voor het eerst hook-tekst testen in plaats van alleen beeld.

- Variatie A (Label, Hormozi type 1): "Party shops and wholesalers in Sweden: Sempertex is looking for you." Body ongewijzigd. Format: Statisch 2 visual.
- Variatie B (Vraag, type 2): "Do your customers ask for Sempertex balloons you can't stock yet?" Body: "Become an official wholesale partner. Premium latex, shipped from Belgium, ready-to-sell starter package. Two minute form, then an intake call." Format: Statisch 2 visual.
- Variatie C (Conditioneel, type 3): "If you sell balloons in Lithuania and you're not yet a Sempertex partner, read this." Body ongewijzigd. Format: Statisch 2 visual, tweede versie met Video 1 (LIT) omdat die in Litouwen het meeste leads per euro geeft.
- Verdeling volgens 70-20-10: winnende combinatie (Statisch 2 + huidige copy) blijft 70%, varianten A en B krijgen elk €10,00/dag als 20%, variant C €5,00/dag als 10%-experiment.
- UK spelling in alle varianten. Geen concurrenten benoemen.

**3. Audience aanpassingen**
- Statisch 1 (LIT), ad set 120250160534160239: leeftijd van 18-65 naar 25-65, gelijk aan de andere 7 ad sets. Reden: 18-24 gaf 1.128 impressions, Link CTR 0,8%, 0 leads. Dit haalt de Link CTR van de ad omhoog richting de 0,8%-drempel zonder de leadbron (35-44, alle 3 leads) te raken.
- Statisch 1 (LIT): desktop uitsluiten. Reden: 1.028 impressions, Link CTR 0,2%, CPC (link) €1,77, 0 leads. Andere ad sets krijgen nauwelijks desktop-verkeer.
- Video 2 (SWE), alleen als de ad niet gepauzeerd wordt: Instagram uitsluiten. Reden: Instagram 980 impressions, Link CTR 0,5%, CPC (link) €3,85 tegenover Facebook Link CTR 1,8%, CPC (link) €0,98.
- Alle 8 ad sets: Audience Network uitsluiten. Reden: minimaal volume (max 211 impressions bij Video 2 (LIT)) met onrealistische Link CTR tot 8,5% en 0 landing page views. Dat zijn per-ongeluk-tikken die de link click cijfers vervuilen en het funnel-lek deels verklaren.
- SWE 25-34 is in alle 4 Zweedse ads het zwakste segment (Link CTR 0,7% tot 1,4%, CPC (link) €0,58 tot €1,70, 0 leads). Nog te weinig lead-data voor uitsluiting; opnieuw beoordelen op 5 september.

**4. Beslissing over Statisch 1 (LIT)**
- Optie A: laten draaien op €20,00/dag en de audience-fix uit voorstel 3 toepassen. Aanbevolen.
- Optie B: kill-regel strikt toepassen en pauzeren. Dan verliest LIT zijn goedkoopste leadbron (CPL €19,60).
- Structureel: overweeg voor lead-campagnes een CPL-uitzondering op de Link CTR-regel, bijvoorbeeld "niet pauzeren als CPL < 50% van campagnegemiddelde". Dan hoeft dit niet elke dag geëscaleerd te worden.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers (1, 2, 3, 4A of 4B).**

### Log

| Timestamp | Actie | Reden |
|---|---|---|
| 2026-09-02 08:11 | Kill-regel Link CTR getriggerd op Statisch 1 (LIT) (0,5% op 10.306 impr.), NIET gepauzeerd | Beste CPL van het account (€19,60), lead-geoptimaliseerde ad set, ter beslissing aan Robin voorgelegd |
| 2026-09-02 08:11 | Kill-regel CPC (link) niet van toepassing | Geen ad met ≥ 500 link clicks |
| 2026-09-02 08:11 | 0 ads gepauzeerd, 0 budgetwijzigingen, 0 audience-wijzigingen | Niveau 2 acties wachten op goedkeuring |
