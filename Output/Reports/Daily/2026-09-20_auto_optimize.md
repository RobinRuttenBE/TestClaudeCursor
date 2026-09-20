## Auto-Optimize Rapport, 20 september 2026 (zondag)

**Run:** 20 september 2026, circa 09:35 UTC. Bronnen: Pipeboard directe JSON-RPC route (1 call, geblokkeerd) en PostHog REST-route project STX EU (2 queries, beide onder 3 seconden). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.

### Databeschikbaarheid

**Meta was niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie, en de directe route kreeg op de eerste en enige call (ad-level, last_3d) de melding `weekly_limit_exceeded`: 30 van 30 wekelijkse tool-executies gebruikt, reset op 21 september 2026 om 00:00 UTC. Dat is vannacht. Verdere Meta-calls zijn bewust niet gedaan.

**Fallback:** campagnestatus en per-ad cijfers komen uit het laatste live extract van 16 september (via het ads-rapport van vanochtend). PostHog bevestigt live dat dat extract nog volledig geldt: nul sessies met `$entry_utm_source = 'facebook'` sinds 10 september.

**PostHog bevestiging (sessions per dag, 6 t/m 20 september)**

| Dag | Sessies totaal | Sessies via Meta | Distributeurspagina views | Formulierstarts | Inzendingen |
|---|---|---|---|---|---|
| 6 sep | 5.990 | 2 | 4 | 0 | 0 |
| 7 sep | 1.103 | 1 | 3 | 0 | 0 |
| 8 sep | 747 | 0 | 3 | 0 | 0 |
| 9 sep | 554 | 2 | 6 | 2 | 0 |
| 10 t/m 17 sep | 29.236 | 0 | 22 | 1 | 0 |
| 18 sep | 1.654 | 0 | 4 | 3 | 1 (Letland, organisch) |
| 19 sep | 2.681 | 0 | 3 | 1 | 0 |
| 20 sep (tot 09:35 UTC) | 901 | 0 | 1 | 2 | 1 (Malta, organisch) |

Sinds 9 september geen enkele betaalde sessie meer. De twee inzendingen van de afgelopen drie dagen zijn beide organisch.

### ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd. Alle 7 campagnes in `act_567892422940728` staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Er zijn 0 actieve ads, dus de kill-regels (Link CTR < 0,8% na 1.000 impressions, CPC (link) > €1,50 na 500 link clicks) hadden niets om op te draaien. Geen `update_ad` calls gedaan. Het tweede account `act_607231713057715` uit het command bestaat niet; `act_1489853856181844` (AmbitionAvenue) is leeg.

**Totaal gepauzeerd: 0 ads**

### ⚠️ Waarschuwingen

Alle waarschuwingen komen uit het extract van 16 september en gelden bij herstart in de huidige vorm. Ze zijn ongewijzigd ten opzichte van gisteren.

| Ad / campagne | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| Wholesaler (LIT), hele campagne | Creative fatigue | Freq 3,97 | Verse creatives vóór herstart |
| Video 2 (SWE) | Dure reach én dure clicks | CPM €17,07, CPC €0,69 | Niet herstarten in deze vorm |
| Video 1 (SWE) | Dure reach, nul conversie | CPM €15,27, 0 inzendingen op 113 sessies | Definitief uit |
| Statisch 2 (LIT) | Goedkope clicks, lage conversie | CPC €0,20, 0,7% conversie, €63,63 per inzending | Nieuwe hook testen |

De CPC-waarden in deze tabel zijn CPC (all) uit het extract van 16 september. Een ad-level link-extract is er sinds de weeklimiet niet meer geweest; de eerstvolgende live run (maandag 21 september) slaat de per-ad Link CTR en CPC (link) als markdown-tabel op.

### 📊 70-20-10 Classificatie

Er draait niets, dus dit is de indeling voor de herstart, niet van het huidige budget. Huidig budget per categorie: €0,00 per dag (0% van totaal). Campagne-level link-metrics uit het ads-rapport van 5 en 6 september: LIT Link CTR 1,0% / CPC (link) €0,64, SWE Link CTR 1,8% / CPC (link) €0,73. Beide campagnes vallen daarmee in de Emerging-band op link-metrics; de indeling hieronder weegt daarom vooral kosten per inzending mee.

**70% Core (bewezen converteerders, voorgesteld €98,00 van €140,00 per dag):**
- Video 2 (LIT), €28,75 per inzending, 3,5% conversie
- Video 1 (LIT), €29,38 per inzending
- Statisch 1 (LIT), 3,0% conversie
- Statisch 2 (SWE), All Clicks CTR 4,0%, €32,03 per inzending

**20% Emerging (potentieel, voorgesteld €28,00 per dag):**
- Zweedse variant van Video 2 (LIT), nog niet gemaakt
- Statisch 2 (LIT), CPC (all) €0,20 maar 0,7% conversie, alleen met nieuwe hook

**10% Experimental (tests, voorgesteld €14,00 per dag):**
- Nieuwe Vraag-hook voor Statisch 2 (LIT)
- Targeting-test Letland en Malta, op basis van de twee organische inzendingen van 18 en 20 september

**Niet meenemen:** Video 1 (SWE) en Video 2 (SWE).

**Budget mismatch:** Nee, er is geen budget om te verdelen. Bij herstart geldt de verdeling hierboven.

### 💡 Voorstellen (wacht op goedkeuring)

De zes voorstellen van 3, 16 en 19 september staan ongewijzigd open. Nieuw vandaag is de aanvulling op nummer 3 met Malta.

**1. Budget herverdeling (herstart)**
- Wholesaler (LIT): van €0,00 per dag naar €100,00 per dag, verdeeld 70-20-10 zoals hierboven
- Wholesaler (SWE): van €0,00 per dag naar €40,00 per dag, alleen Statisch 2 (SWE) plus de Zweedse Video 2 variant, zonder de twee SWE-video's
- Reden: LIT leverde 16 inzendingen op €562,14 (€35,13 per stuk), SWE 8 op €507,24 (€63,41). LIT is bijna twee keer zo efficiënt.
- Verwachte impact: bij gelijke conversie circa 3 inzendingen per dag op LIT en 0,6 per dag op SWE

**2. Nieuwe variaties**
- Gebaseerd op winnende ad Statisch 2 (SWE), All Clicks CTR 4,0%:
  - Variatie A: zelfde visual, Bewijs-hook met het aantal Europese distributeurs, statisch
  - Variatie B: zelfde hook, 6 seconden video met productclose-up, vertical
- Gebaseerd op Video 2 (LIT), beste kosten per inzending €28,75:
  - Variatie A: Zweedse vertaling, zelfde script
  - Variatie B: zelfde script, ander eerste shot (artiest aan het werk in plaats van product)
- Gebaseerd op Statisch 2 (LIT), goedkoopste clicks maar zwakste conversie:
  - Variatie A: Vraag-hook "Still buying balloons from a wholesaler that does not use them?" met directe link naar het formulier
  - Variatie B: Voor-en-na hook, marge zonder en met distributeurschap, statisch

**3. Audience aanpassingen**
- LIT ad sets samenvoegen tot één ad set, Audience Network uitsluiten
- SWE audience verbreden (frequency 3,29 op een klein publiek)
- Statisch 1 (LIT): leeftijd 25 tot 65, desktop uitsluiten
- Letland toevoegen aan de LIT-targeting (organische inzending 18 september)
- **Nieuw:** Malta toevoegen als testland in de Experimental-laag (organische inzending vandaag 09:13 UTC, directe landing op de Engelse homepage, 10 pageviews in 24 minuten, sessie eindigde op de wachtwoord-reset pagina, dus vermoedelijk direct een klantaccount aangemaakt)
- Reden: twee nieuwe markten in drie dagen zonder één euro advertentiebudget

**4. Conversie-guard op de kill-regels**
- Ads met een conversie boven 2,5% niet automatisch pauzeren op alleen Link CTR of CPC (link), zodat Statisch 1 (LIT) en Video 2 (LIT) niet op dag 1 na herstart sneuvelen

**5. Funnel fix vóór herstart**
- Van start naar inzending komt 24,8% door (141 starts, 35 inzendingen, 22 fouten in 30 dagen). Dat lek eerst dichten, anders betaal je bij herstart drie van de vier formulierstarters voor niets.

**6. Eén gedeeld Meta-extract per dag**
- De weeklimiet van 30 calls was op woensdag al vol. Auto-optimize stuitte er deze week vijf dagen op rij op (16, 17, 19, 20 september en de SYBB-run van 19 september). Eén gecachte campaign-level plus ad-level call per dag voor de drie rapporten houdt het onder 15 calls per week.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

### Operationeel

- Reset van de Pipeboard-limiet: 21 september 2026 om 00:00 UTC. Maandag draait auto-optimize weer live met ad-level last_3d in één call, en slaat de per-ad link-tabel op als markdown.
- Logboek automatische acties: geen acties, 20 september 2026 09:35 UTC, reden: 0 actieve ads en Meta op weeklimiet.
