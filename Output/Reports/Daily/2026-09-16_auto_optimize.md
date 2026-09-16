## Auto-Optimize Rapport — 16 september 2026

**Run:** 16 september 2026, middag. Analysevenster: 13 t/m 15 september (last_3d), met PostHog live tot en met vandaag.
**Bronnen:** Meta Ads via Pipeboard (directe JSON-RPC route, 1 call) en PostHog via directe REST-route (2 queries). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.

### Databeschikbaarheid

| Bron | Status | Gevolg |
|---|---|---|
| Pipeboard MCP (claude.ai en lokaal) | Vraagt autorisatie, niet bruikbaar in deze sessie | Directe route geprobeerd |
| Pipeboard directe route | `weekly_limit_exceeded`, 30 van 30 calls gebruikt, reset_date 21 september 2026 00:00 UTC | Geen verse ad-level cijfers over 13 t/m 15 september |
| Ads-rapport 16 september 09:03 | Live Meta-data van vanochtend: alle 7 campagnes PAUSED, nul rijen voor 9 t/m 15 september | Campagnestatus overgenomen |
| PostHog REST | Werkt, twee queries onder 5 seconden | Live bevestiging van stilstand |

Het ads-rapport van vanochtend had de Meta-data nog live (geen weeklimiet om 09:03). Daarna verbruikte de SYBB-run de resterende calls. De enige call van deze run kreeg direct de limietmelding. Zie voorstel 6.

### ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd — er is niets om te beoordelen.**

- Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes (LIT en SWE) sinds 4 september 11:50.
- Meta gaf vanochtend nul rijen voor 9 t/m 15 september op campagne- en ad-niveau. De acht Wholesaler-ads (4 LIT, 4 SWE) hebben dus 0 impressions en 0 link clicks in het analysevenster.
- Kill-regels (Link CTR < 0,8% na 1.000 impressions, CPC (link) > €1,50 na 500 link clicks) hadden geen data om op te draaien. Geen `update_ad` calls gedaan.

**Totaal gepauzeerd: 0 ads**

**PostHog live bevestiging (10 t/m 16 september):**

| Meting | Waarde |
|---|---|
| Sessies met Meta-UTM (utm_source facebook/meta, utm_medium paid/cpc) | 0 |
| `wholesaler_form_submit` | 0 |
| `wholesaler_form_start` | 0 |
| `wholesaler_page_view` (organisch) | 14 in totaal: 1, 6, 2, 0, 1, 2, 2 per dag van 10 t/m 16 september |

Laatste betaalde inzending blijft 4 september. Vandaag is de dertiende dag zonder levering.

### ⚠️ Waarschuwingen

| Ad | Signaal | Waarde | Actie aanbevolen |
|---|---|---|---|
| Geen | Geen levering in het venster, dus geen frequency-, CPM- of Link CTR-signalen | n.v.t. | n.v.t. |

Structurele waarschuwingen uit het laatste 30d-overzicht (17 augustus t/m 15 september, ongewijzigd sinds 4 september) blijven staan voor de herstart:

| Ad of campagne | Signaal | Waarde (30d) | Actie bij herstart |
|---|---|---|---|
| Wholesaler (LIT) | Creative fatigue | Frequency 3,97 | Verse creatives, niet dezelfde set herstarten |
| Video 2 (SWE) | Dure reach en dure clicks | CPM €17,07, CPC (all) €0,69 | Niet herstarten in deze vorm |
| Video 1 (SWE) | Dure reach, nul conversie | CPM €15,27, 0 inzendingen op 113 sessies | Definitief uit |
| Statisch 1 (LIT) | Mechanische kill-trigger | Link CTR 0,5% op laatste ochtend 4 september, maar een van de drie goedkoopste converters | Conversie-guard nodig (voorstel 4) |

### 📊 70-20-10 Classificatie

Er zijn 0 actieve ads, dus er is geen huidig budget te verdelen (€0,00 per dag, 0% in elke categorie). De classificatie hieronder is de laatst bekende stand op basis van het 30d-overzicht en de ad-level link-metrics van 4 en 5 september. Ze dient als startverdeling voor de herstart, niet als oordeel over lopende levering.

**70% Core (huidig €0,00 per dag, 0% van totaal):**
- Video 2 (LIT) — beste kosten per inzending €28,75, conversie 3,5% op sessies. Link CTR zat onder 0,8% op 3 dagen vóór de pauze, maar de conversie rechtvaardigt behoud.
- Video 1 (LIT) — €29,38 per inzending.
- Statisch 1 (LIT) — conversie 3,0%, €0,53 CPC (link) in laatste extract. Alleen met conversie-guard.
- Statisch 2 (SWE) — beste Link CTR van de set (1,8%), €32,03 per inzending.

**20% Emerging (huidig €0,00 per dag, 0% van totaal):**
- Zweedse variant van Video 2 (LIT) — nog niet gebouwd, hangt op voorstel 2.
- Statisch 2 (LIT) — goedkoopste clicks (€0,43 CPC (link), €0,20 CPC (all)) maar €63,63 per inzending en 0,7% conversie. Alleen met nieuwe hook.

**10% Experimental (huidig €0,00 per dag, 0% van totaal):**
- Nieuwe Vraag-hook voor Statisch 2 (LIT) — 0 impressions, nog te maken.

**Budget mismatch:** Nee in de huidige stand (alles staat op nul). Ja bij de vorige verdeling vóór 4 september: beide SWE-video's kregen samen ongeveer een kwart van het budget terwijl ze in geen enkele categorie thuishoren.

> De 70-20-10 drempels zijn nog gekalibreerd op all-clicks. Op link-metrics haalt geen enkele Wholesaler-ad de harde Core-grens (Link CTR > 1,5% én CPC (link) < €0,50). De classificatie hierboven weegt daarom kosten per PostHog-inzending mee, conform de TODO in het command. Geen budget-shifts uitgevoerd.

### 💡 Voorstellen (wacht op goedkeuring)

Ongewijzigd ten opzichte van 15 september. Zolang niets herstart is, komt elke run op 0 acties uit.

**1. Budget herverdeling (herstart)**
- Wholesaler (LIT): van €0,00 per dag naar €100,00 per dag. Verdeling: €70,00 over Video 2, Video 1 en Statisch 1 (LIT) met verse creatives, €20,00 naar Statisch 2 (LIT) met nieuwe hook, €10,00 naar één experiment.
- Wholesaler (SWE): van €0,00 per dag naar €40,00 per dag. Alleen Statisch 2 (SWE) plus één nieuwe creative. Beide SWE-video's niet meenemen.
- Reden: LIT levert €35,13 per inzending tegenover €63,41 voor SWE, en de vier Core-ads zitten alle onder €33,00 per inzending.
- Verwachte impact: bij 24 inzendingen per 30 dagen op €1.069,38 (vorige periode) geeft dezelfde efficiëntie op €140,00 per dag circa 95 tot 120 inzendingen per 30 dagen, mits de funnel-fix uit voorstel 5 eerst staat.

**2. Nieuwe variaties**
- Gebaseerd op Statisch 2 (SWE), Link CTR 1,8%: variatie A met Proof-hook (aantal Europese distributeurs of jaren productie), statisch; variatie B met Callout-hook gericht op Zweedse groothandels, statisch.
- Gebaseerd op Video 2 (LIT), €28,75 per inzending: variatie A dezelfde video met Zweedse ondertiteling en copy; variatie B eerste 3 seconden vervangen door een Vraag-hook, rest gelijk.
- Gebaseerd op Statisch 2 (LIT), goedkoopste clicks maar zwakste conversie: één nieuwe Vraag-hook die de doelgroep (professionele inkoper) al in de eerste zin filtert, zodat de goedkope clicks ook kwalificeren.

**3. Audience aanpassingen**
- LIT: beide ad sets samenvoegen, Audience Network uitsluiten. Reden: frequency 3,97 op een gesplitst publiek, en Statisch 2 (LIT) trekt korte sessies die passen bij Audience Network-verkeer.
- SWE: audience verbreden (interesses uitbreiden of lookalike op de 35 PostHog-inzendingen). Reden: CPM €12,92 tegenover €6,18 voor LIT.
- Statisch 1 (LIT): leeftijd 25 tot 65, desktop uitsluiten. Reden: vorige uitsplitsing toonde geen conversie op desktop.

**4. Conversie-guard op de kill-regels**
- Een ad met minimaal 1 PostHog-inzending onder €40,00 in de laatste 7 dagen niet pauzeren, ook niet bij Link CTR < 0,8%. Zonder deze guard pauzeert auto-optimize Statisch 1 (LIT) op de eerste volle dag na herstart.

**5. Tracking en funnel fix vóór herstart**
- Meta telt 19 leads tegenover 35 in PostHog over 30 dagen. Pixel-event `Lead` op de bedankpagina of via server-side event koppelen aan `wholesaler_form_submit`.
- Van 137 formulierstarts komen 35 inzendingen door (24,8%), met 21 formulierfouten. Eerst het formulier fixen, anders lekt driekwart van elk nieuw budget weg.

**6. Eén gedeeld Meta-extract per dag**
- De gratis Pipeboard-limiet (30 calls per week) is vandaag op woensdag al vol. Eén cron-run om 08:00 die campaign-level 30d, ad-level 30d en de campagnelijst ophaalt en in `Output/Reports/Daily/YYYY-MM-DD_meta_extract.json` cachet, waarna ads-report, SYBB-report en auto-optimize daaruit lezen. Kost 3 calls per dag in plaats van 5 tot 8, en houdt de hele week open.
- Alternatief: Pro-upgrade bij Pipeboard, of een System User token met `ads_read` voor de Marketing API zodat de limiet vervalt.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

---

*Log automatische acties, 16 september 2026:*
- 09:08 UTC — Pipeboard directe call `get_insights` (level ad, last_3d): `weekly_limit_exceeded`, 30/30, reset 2026-09-21T00:00:00Z. Geen verdere Meta-calls gedaan.
- PostHog query 1 (sessies met Meta-UTM sinds 10 september): 0 rijen.
- PostHog query 2 (wholesaler events sinds 10 september): alleen `wholesaler_page_view`, 14 in totaal, 0 starts, 0 inzendingen.
- Geen `update_ad` calls. 0 ads gepauzeerd van 0 actieve ads.
