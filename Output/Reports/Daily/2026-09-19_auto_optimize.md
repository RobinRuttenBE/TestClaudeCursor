## Auto-Optimize Rapport, 19 september 2026

Run: zaterdag 19 september 2026, circa 08:35 UTC. Bronnen: Pipeboard Meta Ads (directe JSON-RPC route, 1 call) en PostHog project STX EU (directe REST-route, 2 queries). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.

### Databeschikbaarheid

**Meta was niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie, en de directe route gaf op de eerste call `weekly_limit_exceeded` (30 van 30 AI tool executions, plan free, reset 21 september 2026 00:00 UTC). Verder geen Meta-calls gedaan, conform de afspraak om donderdag t/m zondag maximaal één testcall te doen.

De campagnestatus komt uit het laatste live Meta-extract van 16 september 09:03 (alle 7 campagnes PAUSED, de twee Wholesaler Campagnes sinds 4 september 11:50). Het ads-rapport van vanochtend bevestigde via PostHog dat er sindsdien geen levering is geweest.

**PostHog bevestigt de stilstand live (9 t/m 19 september):**

| Dag | Betaalde sessies (utm_source facebook/meta) | Sessies op /become-a-distributor | Formulierstarts | Inzendingen |
|---|---|---|---|---|
| 9 sep | 2 | 5 | 2 | 0 |
| 10 sep | 0 | 1 | 0 | 0 |
| 11 sep | 0 | 8 | 0 | 0 |
| 12 sep | 0 | 2 | 0 | 0 |
| 13 sep | 0 | 0 | 0 | 0 |
| 14 sep | 0 | 1 | 0 | 0 |
| 15 sep | 0 | 2 | 0 | 0 |
| 16 sep | 0 | 8 | 0 | 0 |
| 17 sep | 0 | 1 | 1 | 0 |
| 18 sep | 0 | 4 | 3 | 1 |
| 19 sep | 0 | 0 | 0 | 0 |

Laatste betaalde sessie: 9 september (2 nalopers). Laatste betaalde inzending: 4 september. De inzending van 18 september is organisch (Letland, Google of direct), zoals in het ads-rapport van vanochtend beschreven.

### ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd.** Er zijn 0 actieve ads, alle 7 campagnes staan op PAUSED. De kill-regels (Link CTR < 0,8% na 1.000 impressions, CPC (link) > €1,50 na 500 link clicks) hadden niets om op te draaien. Geen `update_ad` calls gedaan.

| Ad | Reden | Was | Nu | Performance |
|---|---|---|---|---|
| (geen) | | | | |

**Totaal gepauzeerd: 0 ads.** Vijftiende opeenvolgende dag zonder actieve ads.

### ⚠️ Waarschuwingen

Geen live 3-daagse Meta-data. Onderstaande waarschuwingen komen uit het 30d-extract van 16 september en gelden bij een herstart in de huidige vorm.

| Ad / campagne | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| Wholesaler (LIT), hele campagne | Creative fatigue | Frequency 3,97 | Verse creatives vóór herstart |
| Video 2 (SWE) | Dure reach | CPM €17,07 | Niet herstarten in deze vorm |
| Video 1 (SWE) | Dure reach en nul conversie | CPM €15,27, 0 inzendingen op 113 sessies | Definitief uit |
| Statisch 2 (LIT) | Lage conversie ondanks goedkope clicks | 0,7% conversie, €63,63 per inzending | Nieuwe hook testen |
| Pipeboard | Weeklimiet vol vanaf woensdag | 30 van 30, reset 21 sep | Eén gedeeld Meta-extract per dag cachen (voorstel 6) |

### 📊 70-20-10 Classificatie

Geen actieve ads, dus geen huidig budget te verdelen (€0,00 per dag). De indeling hieronder is de herstart-indeling op basis van het extract van 16 september. Let op: de opgeslagen rapporten bevatten geen per-ad Link CTR of CPC (link). De link-metrics op campagneniveau komen uit het ads-rapport van 6 september (LIT Link CTR 1,0% en CPC (link) €0,64, SWE Link CTR 1,8% en CPC (link) €0,73), de kosten per inzending per ad uit het extract van 16 september. Volgens het TODO in het command gelden de 70-20-10 drempels op link-metrics als richtlijn, niet als hard oordeel.

**70% Core (voorstel €98,00 per dag van €140,00 totaal):**
- Video 2 (LIT), €28,75 per inzending, 3,5% conversie, beste converteerder
- Video 1 (LIT), €29,38 per inzending
- Statisch 1 (LIT), 3,0% conversie, raakt een CPC-drempel maar converteert
- Statisch 2 (SWE), All Clicks CTR 4,0%, €32,03 per inzending

**20% Emerging (voorstel €28,00 per dag):**
- Zweedse variant van Video 2 (LIT), nieuw te maken, nog geen data

**10% Experimental (voorstel €14,00 per dag):**
- Nieuwe Vraag-hook voor Statisch 2 (LIT), All Clicks CPC €0,20 maar 0,7% conversie

**Niet meenemen:** Video 1 (SWE) en Video 2 (SWE).

**Budget mismatch:** niet te bepalen, er loopt geen budget. Bij herstart volgens bovenstaande verdeling is er geen mismatch.

### 💡 Voorstellen (wacht op goedkeuring)

De zes voorstellen van 3, 16 en 17 september staan ongewijzigd open. Er is geen nieuwe Meta-data die ze verandert. Eén aanvulling bij voorstel 3 op basis van de organische inzending van 18 september.

**1. Budget herverdeling (herstart)**
- Wholesaler (LIT): van €0,00 naar €100,00 per dag, verdeeld 70-20-10 zoals hierboven
- Wholesaler (SWE): van €0,00 naar €40,00 per dag, alleen Statisch 2 (SWE) plus een nieuwe variant, zonder de twee SWE-video's
- Reden: LIT levert de goedkoopste inzendingen (€35,13 gemiddeld tegen €63,41 bij SWE)
- Verwachte impact: circa 3 tot 4 inzendingen per dag bij de kosten per inzending van augustus

**2. Nieuwe variaties**
- Gebaseerd op Statisch 2 (SWE) (All Clicks CTR 4,0%): variatie A met een Callout-hook gericht op Zweedse ballonwinkels, variatie B met een Proof-hook op de EU-certificering uit `sempertex-company-heritage-and-vision.md`
- Gebaseerd op Video 2 (LIT) (beste converteerder): variatie A als Zweedse vertaling met dezelfde eerste 3 seconden, variatie B met een andere CTA (formulier direct in plaats van pagina)
- Gebaseerd op Statisch 2 (LIT): nieuwe Vraag-hook in plaats van de huidige, want de clicks zijn goedkoop maar de bezoekers converteren niet

**3. Audience aanpassingen**
- LIT ad sets samenvoegen tegen de frequency van 3,97
- Audience Network uitsluiten op beide campagnes
- SWE audience verbreden (CPM €12,92 wijst op een te smal publiek)
- Statisch 1 (LIT) naar 25-65 zonder desktop
- **Nieuw:** Letland toevoegen aan de LIT-targeting bij herstart. Reden: eerste inzending ooit uit Letland op 18 september, organisch, zonder betaald verkeer.

**4. Conversie-guard op de kill-regels**
- Een ad met minimaal 1 inzending in de laatste 3 dagen wordt niet automatisch gepauzeerd, ook niet bij Link CTR onder 0,8%. Anders sneuvelt Statisch 1 (LIT) op dag 1 na herstart.

**5. Tracking en funnel fix vóór herstart**
- Meta telt 19 leads tegenover 33 betaalde inzendingen in PostHog. Van 138 formulierstarts komen 34 door (24,6%). Eerst het formulier fixen, dan budget.

**6. Eén gedeeld Meta-extract per dag**
- Het ads-rapport haalt 's ochtends de data op en schrijft die als markdown-tabel weg (campagne- en ad-niveau, inclusief Link CTR en CPC (link)). SYBB-rapport en auto-optimize lezen dat bestand in plaats van Pipeboard opnieuw aan te roepen. Dan blijft de weeklimiet van 30 calls de hele week toereikend. Dit is de vierde dag deze week dat auto-optimize op de limiet stuit.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

Wijzigingen ten opzichte van 17 september: geen nieuwe Meta-data, geen acties. Nieuw is alleen de organische inzending van 18 september en de daaruit volgende aanvulling op voorstel 3.
