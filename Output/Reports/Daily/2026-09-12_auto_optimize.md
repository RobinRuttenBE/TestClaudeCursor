## Auto-Optimize Rapport — 12 september 2026

**Run:** 12 september 2026, zaterdag (middag). Bronnen: Pipeboard Meta Ads (directe JSON-RPC route, MCP meldde "requires authentication") en PostHog project STX EU (directe REST-route, MCP gaf HTTP 405). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.

**Databeperking:** de allereerste Pipeboard call (campaign-level, last_3d) kreeg `weekly_limit_exceeded` (100 van 30 gebruikt, reset maandag 14 september 00:00 UTC). Er zijn dus geen live Meta-cijfers over 9 t/m 12 september. De campagnestatus komt uit het ads-rapport van vanochtend (alle 7 campagnes PAUSED, live opgehaald om 09:48), de ad-level cijfers uit het rapport van 7 september. PostHog is wél live en bevestigt dat er geen levering is.

### ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er is geen levering om de kill-regels op te draaien.

| Ad | Reden | Was | Nu | Performance |
|----|-------|-----|-----|-------------|
| — | — | — | — | 0 impressions, 0 link clicks, €0,00 spend (9 t/m 12 sep) |

**Totaal gepauzeerd: 0 ads.** Geen `update_ad` calls gedaan.

Log:
- 2026-09-12 middag — Pipeboard call 1 (get_insights, campaign, last_3d): weekly_limit_exceeded. Geen verdere Meta-calls gedaan om de limiet niet verder te belasten.
- 2026-09-12 middag — PostHog check gedraaid als vervangende levering-check (zie hieronder). Uitkomst: geen betaald verkeer, dus kill-regels niet van toepassing.

### 📡 Live bevestiging via PostHog (8 t/m 12 september)

| Dag | Sessies met utm_source=meta | Verwijzing Facebook/Instagram | Distributeurspagina (alle) | SYBB landing page (alle) | Inzendingen |
|-----|-----|-----|-----|-----|-----|
| 8 sep | 0 | 2 | 3 | 3 | 0 |
| 9 sep | 0 | 3 | 5 | 2 | 0 |
| 10 sep | 0 | 1 | 1 | 6 | 0 |
| 11 sep | 0 | 0 | 8 | 3 | 0 |
| 12 sep (tot nu) | 0 | 0 | 1 | 4 | 0 |

Toelichting:
- Nul sessies met een Meta-UTM in de entry-URL of ergens in de sessie-URL's. Ook op ad-niveau (`utm_content`) is de tabel leeg over 9 t/m 12 september.
- De handvol Facebook/Instagram-verwijzingen op 8 t/m 10 september zijn organische klikken zonder UTM, geen ad-levering.
- Laatste wholesaler-inzending blijft 4 september. Sinds 1 september: 6 inzendingen (1, 3, 1, 1), daarna niets.
- Het hoge sitewide sessievolume op 10 en 11 september (4.355 en 6.970) staat los van ads en raakt de distributeurs- en SYBB-pagina's niet.

**Tiende dag op rij zonder levering** (Wholesaler LIT en SWE gepauzeerd sinds 4 september 11:50, SYBB al langer stil).

### ⚠️ Waarschuwingen

Niets nieuws over de laatste 3 dagen (geen levering). De bekende signalen uit het laatste rapport met data (7 september, 30d) blijven staan voor de herstart:

| Ad / campagne | Signaal | Waarde | Actie aanbevolen |
|----|-------|-----|-----------------|
| Wholesaler (LIT), hele campagne | Creative fatigue | Freq 3,97 | Verse creatives vóór herstart |
| Video 2 (SWE) | Dure reach | CPM €17,07, CPC (all) €0,69 | Niet herstarten in deze vorm |
| Video 1 (SWE) | Dure reach + 0 conversie | CPM €15,27, 0 inzendingen op 113 sessies | Niet herstarten |
| Statisch 1 (LIT) | Lage Link CTR | Link CTR 0,6% (30d), 0,2% op 4 sep ochtend | Behouden, converteert op €36,06 per inzending; conversie-guard nodig |
| Pipeboard Free plan | Weeklimiet | 100 van 30 calls | Elke dagelijkse run na maandag valt opnieuw binnen 1 dag dicht als drie rapporten apart callen |

### 📊 70-20-10 Classificatie

Huidig budget per categorie: €0,00 per dag over de hele linie, want alles staat op PAUSED. De classificatie hieronder is de laatst bekende stand (Meta 30d t/m 6 september plus PostHog inzendingen) en dient als herstartplan, niet als oordeel over de afgelopen 3 dagen.

**70% Core (voorgesteld €98,00/dag — huidig 0% van totaal):**
- Video 2 (LIT) — €28,75 per inzending, beste converter van het account
- Video 1 (LIT) — €29,38 per inzending
- Statisch 1 (LIT) — Link CTR 0,6%, maar €36,06 per inzending (conversie-guard vereist)
- Statisch 2 (SWE) — All Clicks CTR 4,0%, beste CTR van het account

**20% Emerging (voorgesteld €28,00/dag — huidig 0% van totaal):**
- Statisch 2 (LIT) — CPC (all) €0,20, laagste van het account, maar 0,7% conversie en kortste sessies — potentieel met nieuwe hook
- Zweedse variant van Video 2 (LIT) — nog niet gebouwd

**10% Experimental (voorgesteld €14,00/dag — huidig 0% van totaal):**
- Eén nieuwe creative per markt (LIT en SWE) om de frequentie van 3,97 te doorbreken — 0 impressions, te vroeg voor oordeel

**Budget mismatch:** Ja. Alle categorieën staan op €0,00, dus 0% Core in plaats van 70%. De mismatch is niet op te lossen met een budget-shift, alleen met een herstart (voorstel 1).

Uit: Video 1 (SWE) en Video 2 (SWE) komen in geen enkele categorie terug.

### 💡 Voorstellen (wacht op goedkeuring)

Ongewijzigd ten opzichte van 7 t/m 11 september. Er is geen nieuwe data die ze verandert.

**1. Budget herverdeling (herstart)**
- Wholesaler (LIT): van €0,00/dag naar €100,00/dag, verdeeld 70-20-10 over Video 2, Video 1, Statisch 1 (Core), Statisch 2 (Emerging) en één nieuwe creative (Experimental)
- Wholesaler (SWE): van €0,00/dag naar €40,00/dag, alleen Statisch 2 plus één nieuwe creative; Video 1 en Video 2 (SWE) blijven uit
- Reden: LIT levert op €35,13 per inzending tegenover €72,46 voor SWE; de twee SWE-video's zijn de duurste ads van het account
- Verwachte impact: bij gelijke conversie circa 3 tot 4 inzendingen per dag uit LIT en 0,5 per dag uit SWE

**2. Nieuwe variaties**
- Gebaseerd op winnende hook Statisch 2 (SWE) (All Clicks CTR 4,0%):
  - Variatie A: zelfde visual, CTA "Become the Sempertex distributor for your region" — statisch
  - Variatie B: zelfde hook als carrousel met 3 productlijnen — carrousel
- Gebaseerd op Video 2 (LIT) (€28,75 per inzending):
  - Variatie A: Zweedse ondertiteling en Zweedse landing-UTM — video
  - Variatie B: eerste 3 seconden vervangen door een proof-hook (aantal Europese distributeurs) — video
- Voor Statisch 2 (LIT): nieuwe hook testen, huidige haalt clicks op €0,20 maar converteert 0,7%

**3. Audience aanpassingen**
- LIT: de ad sets samenvoegen om de frequentie van 3,97 te drukken en Meta meer ruimte te geven
- SWE: audience verbreden (frequency 3,29 bij CPM €12,92 wijst op een te smal publiek)
- Reden: beide campagnes zaten vóór de pauze boven frequency 3 met stijgende CPM

**4. Conversie-guard op de kill-regels**
- Niet pauzeren wanneer een ad in de laatste 7 dagen minimaal 1 PostHog-inzending onder €40,00 heeft, ook al zit de Link CTR onder 0,8%
- Reden: Statisch 1 (LIT) triggerde op 4 september mechanisch de Link CTR-regel terwijl het een van de drie goedkoopste converters is

**5. Tracking fix vóór herstart**
- Meta telt 19 leads tegenover 33 in PostHog over dezelfde periode; pixel-event op de bedankpagina nakijken zodat Meta's optimalisatie op echte leads draait

**6. Eén gedeelde Meta-call per dag cachen**
- Ads-report, SYBB-report en auto-optimize ieder apart laten callen kost 6 tot 10 Pipeboard-calls per dag; het Free plan geeft er 30 per week. Eén cache-bestand per dag (campaign-level 30d en ad-level last_3d) houdt de limiet buiten beeld tot maandag
- Zonder deze fix valt de auto-optimize na maandag opnieuw binnen 2 dagen droog

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**
