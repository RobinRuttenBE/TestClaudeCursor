## Auto-Optimize Rapport, 15 september 2026

**Run:** 15 september 2026, avond. Databronnen: Meta Ads via Pipeboard (directe JSON-RPC route, 3 calls, geen weeklimiet) en PostHog project STX EU (directe REST-route, 2 queries). Beide MCP-servers zelf weigerden opnieuw (Pipeboard vraagt auth, PostHog geeft HTTP 405). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.

**Periode kill-regels:** last_3d, 12 t/m 14 september 2026. Account: act_567892422940728 (Sempertex Ad Account). Het in het command genoemde act_607231713057715 bestaat niet in de Pipeboard-koppeling.

### Stand van zaken

Er draait niets. Meta geeft over 12 t/m 14 september nul rijen op campagne- én ad-niveau. Alle 7 campagnes staan op PAUSED:

| Campagne | Status | Laatst gewijzigd |
|---|---|---|
| Wholesaler Campagne (SWE) | PAUSED | 4 sep 2026 11:50 |
| Wholesaler Campagne (LIT) | PAUSED | 4 sep 2026 11:50 |
| 2026: SYBB - Kopie | PAUSED | 27 aug 2026 |
| 2026: SYBB | PAUSED | 19 apr 2026 |
| Last push Nozzle Up | PAUSED | 21 sep 2025 |
| Nozzle Up END OF AUGUST | PAUSED | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | PAUSED | 15 sep 2025 |

PostHog bevestigt de stilstand live: nul sessies met `utm_source=meta` sinds 12 september, nul `wholesaler_form_submit` events sinds 8 september. Laatste betaalde inzending blijft 4 september. Dit is de twaalfde dag zonder levering.

### ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd. Er is geen levering, dus geen enkele ad haalt de minimale data (1.000 impressions of 500 link clicks) om een kill-regel te triggeren. Geen `update_ad` calls gedaan.

**Totaal gepauzeerd: 0 ads**

### ⚠️ Waarschuwingen

Geen live waarschuwingen over last_3d (geen data). Ter herinnering de vlaggen uit het laatste extract met levering (30d, 16 aug t/m 14 sep), relevant bij herstart:

| Ad | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| Wholesaler (LIT), campagneniveau | Creative fatigue | Freq 3,97 | Verse creatives bij herstart |
| Video 2 (SWE) | Dure reach | CPM €17,07, CPC (all) €0,69 | Niet herstarten in deze vorm |
| Video 1 (SWE) | Dure reach, 0 inzendingen | CPM €15,27, 113 sessies, 0 inzendingen | Definitief uit |
| Statisch 1 (LIT) | Mechanische Link CTR-trigger op 4 sep | Link CTR 0,2% bij 1.830 imp, maar 3,0% conversie | Conversie-guard nodig vóór herstart |

### 📊 70-20-10 Classificatie

Er zijn 0 actieve ads, dus geen live classificatie mogelijk. Onderstaande indeling is de herstart-set op basis van het 30d-extract (kosten per inzending op PostHog gebaseerd):

**70% Core (huidig budget €0,00/dag):**
- Video 2 (LIT), €28,75 per inzending, 3,5% conversie
- Video 1 (LIT), €29,38 per inzending
- Statisch 1 (LIT), 3,0% conversie, goedkoopste converter ondanks lage Link CTR
- Statisch 2 (SWE), All Clicks CTR 4,0%, €32,03 per inzending

**20% Emerging (huidig budget €0,00/dag):**
- Zweedse variant van Video 2 (LIT), nog te maken

**10% Experimental (huidig budget €0,00/dag):**
- Nieuwe Vraag-hook voor Statisch 2 (LIT), huidige versie €63,63 per inzending bij kortste sessies (52s)

**Budget mismatch:** Ja. Totaal budget is €0,00 per dag, dus 100% van de bewezen set krijgt niets. De herstart-voorstellen hieronder lossen dit op.

### 💡 Voorstellen (wacht op goedkeuring)

Ongewijzigd ten opzichte van 14 september. Geen nieuwe data, dus geen reden om ze aan te passen.

**1. Budget herverdeling (herstart)**
- Wholesaler Campagne (LIT): van €0,00/dag naar €100,00/dag, 70-20-10 verdeeld over Video 2, Video 1, Statisch 1, Statisch 2 en één nieuwe creative.
- Wholesaler Campagne (SWE): van €0,00/dag naar €40,00/dag, alleen Statisch 2 plus één nieuwe creative, zonder Video 1 en Video 2 (SWE).
- Reden: LIT levert inzendingen onder €35,13, SWE onder €63,41 met de video's erin en rond €32,03 op Statisch 2 alleen.
- Verwachte impact: 3 tot 4 inzendingen per dag tegen ongeveer €35,00 per stuk, mits de funnel-fix (voorstel 5) eerst is gedaan.

**2. Nieuwe variaties**
- Gebaseerd op Statisch 2 (SWE), All Clicks CTR 4,0%: twee variaties (andere CTA, ander visual).
- Gebaseerd op Video 2 (LIT), €28,75 per inzending: twee variaties, waarvan één Zweedse versie.
- Nieuwe Vraag-hook voor Statisch 2 (LIT) als 10% experiment.

**3. Audience aanpassingen**
- LIT ad sets samenvoegen (frequency 3,97 wijst op verzadiging bij gesplitste sets).
- Audience Network uitsluiten.
- SWE audience verbreden.
- Statisch 1 (LIT) naar 25-65 zonder desktop-placement.

**4. Conversie-guard op de kill-regels**
- Ad niet pauzeren als er in dezelfde periode minimaal 1 PostHog-inzending onder €40,00 is. Anders sneuvelt Statisch 1 (LIT) op dag 1 na herstart.

**5. Tracking en funnel fix vóór herstart**
- Meta telt 19 leads tegenover 35 in PostHog. Formulier: 137 starts, 21 fouten, 35 inzendingen over 30d; 102 starters haken af. Eerst fixen vóór er weer budget op gaat.

**6. Eén gedeeld Meta-extract per dag cachen**
- Voor ads-report, sybb-report en auto-optimize samen, anders valt de gratis Pipeboard weeklimiet later deze week opnieuw dicht. Deze run gebruikte bewust maar 3 calls.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

Zolang niets herstart is, blijft elke run op 0 acties uitkomen.

### Log

- 2026-09-15 avond: get_insights campaign last_3d, 0 rijen. get_insights ad last_3d, 0 rijen. get_campaigns, 7 campagnes, alle PAUSED. PostHog sessions utm_source=meta sinds 12 sep: 0. PostHog wholesaler_form_submit sinds 8 sep: 0. Geen update_ad calls.
