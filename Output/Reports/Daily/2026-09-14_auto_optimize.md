## Auto-Optimize Rapport, 14 september 2026

**Run:** maandag 14 september 2026, gedraaid na /ads-report. Bronnen: Meta Ads via Pipeboard (directe JSON-RPC route, 2 calls) en PostHog via de directe REST-route (project STX EU 149694). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Google Sheet geschreven. Alleen dit lokale bestand als output.

**Accounts:** act_567892422940728 (Sempertex Ad Account) is de enige bron. Het in het command genoemde act_607231713057715 bestaat niet in de Pipeboard-koppeling.

**Data-status:** Pipeboard werkte live. De weeklimiet was op maandag gereset, ondanks de resetdatum van 21 september in het antwoord van gisteren. Alle cijfers in de secties "Automatische acties" en "Waarschuwingen" zijn vandaag vers opgehaald. De ad-level cijfers in de 70-20-10 sectie komen uit het 30d-extract van 7 september, omdat er sinds 4 september geen levering meer is en die cijfers dus ongewijzigd zijn.

---

### ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd, er draait niets.**

| Check | Resultaat |
|---|---|
| `get_insights` level ad, `date_preset: last_3d` (11 t/m 13 september) | 0 rijen, geen impressions, geen spend |
| `get_campaigns` zonder status_filter | 7 campagnes, alle 7 PAUSED |
| Wholesaler Campagne (SWE) | PAUSED sinds 4 september 11:50 |
| Wholesaler Campagne (LIT) | PAUSED sinds 4 september 11:50 |
| 2026: SYBB en 2026: SYBB - Kopie | PAUSED (sinds 19 april en 27 augustus) |
| Drie Nozzle Up campagnes | PAUSED sinds september 2025 |

De kill-regels (Link CTR < 0,8% na 1.000 impressions, CPC (link) > €1,50 na 500 link clicks) hadden geen enkele ad om op te draaien. Geen `update_ad` calls gedaan.

**Totaal gepauzeerd: 0 ads** (tiende run op rij zonder levering, elfde dag sinds de pauze)

**PostHog bevestigt de stilstand live (11 t/m 14 september):**

| Datum | Sessies met utm_source=meta | Pageviews /become-a-distributor | wholesaler_form_submit |
|---|---|---|---|
| 11 september | 0 | 8 (organisch) | 0 |
| 12 september | 0 | 2 (organisch) | 0 |
| 13 september | 0 | 0 | 0 |
| 14 september (tot nu) | 0 | 0 | 0 |

Laatste betaalde inzending blijft 4 september.

---

### ⚠️ Waarschuwingen

Geen live waarschuwingen: zonder levering zijn frequency, CPM en Link CTR-daling niet meetbaar over de laatste 3 dagen.

**Waarschuwingen die blijven staan voor het moment van herstart** (op basis van het 30d-extract van 7 september, periode 8 augustus t/m 6 september):

| Ad / campagne | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| Wholesaler (LIT), campagneniveau | Creative fatigue | Freq 3,97 | Verse creatives vóór herstart, niet dezelfde 4 ads opnieuw aanzetten |
| Video 2 (SWE) | Dure reach en dure clicks | CPM €17,07, CPC (link) €0,69 | Niet herstarten in deze vorm |
| Video 1 (SWE) | Dure reach, geen conversie | CPM €15,27, CPC (link) €0,53, 0 inzendingen op 113 sessies | Definitief uit |
| Statisch 1 (LIT) | Lage Link CTR maar goede converter | Link CTR 0,6%, €36,06 per inzending | Conversie-guard nodig, anders pauzeert de kill-regel deze ad op dag 1 na herstart |
| Statisch 2 (LIT) | Goedkope clicks, zwakke conversie | CPC (link) €0,20, 0,8% sessie-naar-inzending, €63,63 per inzending | Nieuwe hook testen, niet opschalen op clicks |

---

### 📊 70-20-10 Classificatie

Er zijn 0 actieve ads, dus het huidige budget per categorie is €0,00 per dag (0% overal). De classificatie hieronder is de laatst bekende stand op de 8 Wholesaler-ads (4 LIT, 4 SWE) en dient als startpunt voor de herstart. Drempels zijn richtlijn, niet hard oordeel: de 70-20-10 grenzen zijn nog niet gekalibreerd op link metrics.

**70% Core (budget nu: €0,00/dag, huidig 0% van totaal):**
- Video 2 (LIT), €28,75 per inzending, beste converter, wel 37% Audience Network clicks
- Video 1 (LIT), €29,38 per inzending
- Statisch 1 (LIT), Link CTR 0,6%, €36,06 per inzending, hoogste sessie-naar-inzending ratio (4,0% lifetime)
- Statisch 2 (SWE), beste Link CTR van de set (4,0% all clicks CTR als indicatie), enige SWE-ad met bewezen conversie

**20% Emerging (budget nu: €0,00/dag, huidig 0% van totaal):**
- Statisch 2 (LIT), CPC (link) €0,20 maar €63,63 per inzending, potentieel als de hook verbetert
- Zweedse variant van Video 2 (LIT), nog niet gebouwd

**10% Experimental (budget nu: €0,00/dag, huidig 0% van totaal):**
- Nieuwe hook-variaties (zie voorstel 2), nog niet gebouwd
- Video 1 (SWE) en Video 2 (SWE) horen hier niet meer thuis, beide zijn afgeschreven

**Budget mismatch:** Niet meetbaar, totaal budget is €0,00. Bij de laatste actieve stand (3 september) kreeg Core 37,5% in plaats van 70% en kregen de twee SWE-video's 25% in plaats van 10%. Het herstartplan in voorstel 1 corrigeert dat.

---

### 💡 Voorstellen (wacht op goedkeuring)

Ongewijzigd ten opzichte van 13 september. Er is geen nieuwe data die ze verandert, alleen een elfde dag zonder levering en zonder inzendingen.

**1. Budget herverdeling (herstart)**
- Wholesaler Campagne (LIT): van €0,00/dag naar €100,00/dag, verdeeld 70-20-10: €70,00 over Video 2, Video 1 en Statisch 1 (met conversie-guard), €20,00 naar Statisch 2 met nieuwe hook, €10,00 naar één nieuwe creative.
- Wholesaler Campagne (SWE): van €0,00/dag naar €40,00/dag, alleen Statisch 2 (€30,00) plus één nieuwe creative (€10,00). Video 1 (SWE) en Video 2 (SWE) blijven uit.
- Reden: LIT leverde 16 inzendingen op €562,14 (€35,13 per stuk), SWE 7 op €507,24 (€72,46). Elke dag stilstand kost bij het LIT-tempo ongeveer 0,5 inzending.
- Verwachte impact: 15 tot 20 inzendingen per maand bij €140,00/dag, mits verse creatives de frequency van 3,97 doorbreken.

**2. Nieuwe variaties**
- Gebaseerd op de winnende visual Statisch 2 (SWE) (hoogste CTR van de set):
  - Variatie A: Statement-hook ("The balloon brand professionals ask for by name"), zelfde visual, CTA "Become a distributor"
  - Variatie B: Label-hook ("For wholesalers who want a range that sells itself"), carrousel met de 9 latex lijnen
- Gebaseerd op Video 2 (LIT) (beste converter, €28,75 per inzending):
  - Variatie A: zelfde video, Zweedse copy en targeting (SWE)
  - Variatie B: eerste 3 seconden vervangen door een Vraag-hook ("Still ordering balloons from three different suppliers?")
- Nieuwe hook voor Statisch 2 (LIT): Vraag-hook in plaats van de huidige generieke copy, omdat de clicks goedkoop zijn maar de sessies kort (52s).

**3. Audience aanpassingen**
- LIT: de vier ad sets samenvoegen tot één ad set met €100,00/dag zodat Meta het budget zelf over de winnende ads verdeelt. Reden: frequency 3,97 op vier losse smalle sets.
- LIT: Audience Network uitsluiten op alle ads. Reden: 37% van de Video 2 (LIT) link clicks kwam daarvandaan zonder sessies in PostHog.
- SWE: audience verbreden (interesses uitbreiden naar party supply retail en event decoration). Reden: CPM €12,92 tegenover €6,18 in LIT, te smal publiek.
- Statisch 1 (LIT): leeftijd naar 25-65 en desktop uitsluiten. Reden: de lage Link CTR zat in Facebook desktop, de conversies op mobiel.

**4. Conversie-guard op de kill-regels** (herhaald voorstel)
- Regel toevoegen aan dit command: een ad wordt niet gepauzeerd op Link CTR < 0,8% als PostHog in dezelfde 3 dagen minimaal 1 inzending onder €40,00 laat zien. Zonder deze regel sneuvelt Statisch 1 (LIT) op de eerste volle dag na herstart (0,2% op 1.830 impressions op 4 september).

**5. Tracking fix vóór herstart** (herhaald voorstel)
- Meta telde 19 leads tegenover 35 inzendingen in PostHog over 30 dagen. Controleer op /become-a-distributor of het Lead-event vuurt bij formulierinzending (pixel of Conversions API). Zolang dat lek er is, optimaliseren de ad sets op de helft van het signaal.

**6. Eén gedeelde Meta-call per dag cachen** (herhaald voorstel)
- Vandaag gebruikte deze run 2 Pipeboard-calls, het ads-rapport 4. Met drie dagelijkse rapporten valt de gratis weeklimiet later in de week weer dicht. Eén 30d-extract per dag in `output/reports/daily/` dat de drie rapporten delen, lost dat op.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

---

### Log

| Timestamp | Actie | Resultaat |
|---|---|---|
| 2026-09-14 (run) | `get_insights` act_567892422940728, level ad, last_3d | 0 rijen |
| 2026-09-14 (run) | `get_campaigns` act_567892422940728 | 7 campagnes, alle PAUSED |
| 2026-09-14 (run) | PostHog HogQL sessions utm_source=meta vanaf 11 september | 0 sessies |
| 2026-09-14 (run) | PostHog HogQL events /become-a-distributor vanaf 11 september | 10 organische pageviews, 0 inzendingen |
| 2026-09-14 (run) | `update_ad` | niet aangeroepen, geen kandidaten |
