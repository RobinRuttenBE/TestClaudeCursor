## Auto-Optimize Rapport, 13 september 2026

Run: 13 september 2026, 11:35 (lokale tijd). Bronnen: Pipeboard Meta Ads via directe JSON-RPC call (MCP meldde "requires authentication") en PostHog REST (project STX EU 149694, MCP gaf HTTP 405). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Google Sheet geschreven. Account act_567892422940728 (Sempertex Ad Account); het in het command genoemde act_607231713057715 bestaat niet in de Pipeboard-koppeling.

### Databeschikbaarheid

**Meta onbereikbaar in deze run.** De eerste en enige Pipeboard call (ad-level insights, last_3d) kreeg `weekly_limit_exceeded`: 100 van 30 wekelijkse executies gebruikt, Free plan, 0 trial credits, `reset_date` **21 september 2026 00:00 UTC**. Geen verdere Meta-calls gedaan. Live Meta-cijfers over 10 t/m 13 september ontbreken.

**PostHog live, 10 t/m 13 september (tot 11:35):**

| Datum | Site pageviews | Pageviews met utm_source=meta | Sessies met Meta entry-UTM | Pageviews /become-a-distributor | Inzendingen (wholesaler_form_submit) |
|---|---|---|---|---|---|
| 10 sep | 8.867 | 0 | 0 | 1 | 0 |
| 11 sep | 10.515 | 0 | 0 | 8 | 0 |
| 12 sep | 7.608 | 0 | 0 | 2 | 0 |
| 13 sep (deels) | 1.853 | 0 | 0 | 0 | 0 |

Nul sessies met een Meta entry-UTM in de hele periode, ook uitgesplitst per utm_campaign en utm_content. Er is dus geen betaald verkeer en geen levering. Dit sluit aan op het ads-rapport van vanochtend: alle 7 campagnes op PAUSED, de twee Wholesaler Campagnes sinds 4 september 11:50. Twaalfde dag zonder levering. Laatste inzending blijft 4 september.

### ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd, 0 acties.** Er zijn geen actieve ads, dus de kill-regels (Link CTR < 0,8% bij 1.000+ impressions, CPC (link) > €1,50 bij 500+ link clicks) hadden niets om op te draaien. Geen `update_ad` calls gedaan.

| Ad | Reden | Was | Nu | Performance |
|---|---|---|---|---|
| geen | n.v.t. | | | 0 impressions, 0 link clicks, €0,00 spend (10 t/m 13 sep, bevestigd via PostHog) |

**Totaal gepauzeerd: 0 ads**

### ⚠️ Waarschuwingen

Geen nieuwe waarschuwingen mogelijk zonder live Meta-data. De bekende waarschuwingen uit het laatste rapport met levering (7 september, cijfers 30d) blijven staan voor de herstart:

| Ad / campagne | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| Wholesaler (LIT) | Creative fatigue | Freq. 3,97 | Verse creatives vóór herstart |
| Video 2 (SWE) | Dure reach | CPM €17,07, CPC (link) €0,69 | Niet herstarten in deze vorm |
| Video 1 (SWE) | Dure reach, geen conversie | CPM €15,27, 0 inzendingen op 97 sessies | Definitief uit |
| Pipeboard | Weeklimiet | 100 van 30, reset 21 sep | Eén gedeelde Meta-call per dag cachen voor alle drie rapporten |

### 📊 70-20-10 Classificatie

Geen actieve ads, dus geen huidig budget te verdelen (€0,00 per dag). Classificatie op basis van de laatste 30d-cijfers met levering (t/m 4 september, extract 7 september), als startpunt voor de herstart. Drempels zijn richtlijn, nog niet gekalibreerd op link metrics.

**70% Core (bewezen, huidig budget €0,00):**
- Video 2 (LIT), €28,75 per inzending, goedkoopste leadbron
- Video 1 (LIT), €29,38 per inzending
- Statisch 1 (LIT), Link CTR 0,6% maar 3,8% conversie, behouden met conversie-guard
- Statisch 2 (SWE), beste All Clicks CTR 4,0%

**20% Emerging (huidig budget €0,00):**
- Statisch 2 (LIT), laagste CPC (link) €0,20, maar circa €63,63 per inzending en 0,8% conversie. Nieuwe hook nodig.

**10% Experimental (huidig budget €0,00):**
- Nog niets. De hook-test van 3 september is niet gestart; alle 8 ads gebruiken dezelfde tekst per land.

**Budget mismatch:** Nee, er is geen budget. Bij herstart zonder herverdeling ontstaat wel meteen een mismatch: de twee SWE-video's (samen circa 30% van het oude budget) horen in geen enkele categorie.

### 💡 Voorstellen (wacht op goedkeuring)

Ongewijzigd ten opzichte van 12 september. Niets uitgevoerd.

**1. Budget herverdeling / herstart**
- Wholesaler (LIT): van €0,00 naar €100,00 per dag, verdeeld 70-20-10 over Video 2, Video 1, Statisch 1 (samen €70,00), Statisch 2 met nieuwe hook (€20,00) en één nieuwe creative (€10,00).
- Wholesaler (SWE): van €0,00 naar €40,00 per dag, alleen Statisch 2 (€30,00) plus één nieuwe creative (€10,00). Video 1 en Video 2 (SWE) blijven uit.
- Reden: LIT levert inzendingen onder €30,00, SWE-video's kosten €0,53 tot €0,69 per link click zonder inzendingen.
- Verwachte impact: terug naar 1,5 tot 5 inzendingen per dag bij circa €30,00 tot €35,00 per inzending.

**2. Nieuwe variaties**
- Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT), plus één nieuwe hook voor Statisch 2 (LIT). Concrete copy staat in het rapport van 4 september (vijf Hormozi hook types, plus SEE_DETAILS versus APPLY_NOW test).

**3. Audience aanpassingen**
- LIT: vier ad sets op dezelfde audience samenvoegen tot één ad set om frequency 3,97 te doorbreken.
- SWE: audience verbreden, CPM €12,92 tegenover €6,18 in LIT.

**4. Conversie-guard op de kill-regels**
- Niet pauzeren als een ad in de laatste 7 dagen minimaal 1 PostHog-inzending onder €40,00 heeft. Zonder deze guard pauzeert auto-optimize Statisch 1 (LIT) op de eerste volle dag na herstart.

**5. Tracking fix vóór herstart**
- Meta telt 19 leads tegenover 35 inzendingen in PostHog. Lead-event op de bedankpagina controleren.

**6. Meta-call cachen**
- Eén gedeelde Pipeboard-call per dag voor ads-report, auto-optimize en SYBB-rapport. Anders zit de route na de reset van 21 september binnen 2 dagen opnieuw dicht en draaien de kill-regels weer blind.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

Zolang niets herstart is, komt elke dagelijkse run op 0 acties uit. Eerstvolgende run met live Meta-data: op of na 21 september, tenzij Pipeboard eerder naar Pro gaat of de MCP opnieuw geautoriseerd wordt.
