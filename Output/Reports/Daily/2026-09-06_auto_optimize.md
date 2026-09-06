## Auto-Optimize Rapport, 6 september 2026

Gegenereerd: 2026-09-06 11:30 CEST. Bronnen: Meta Ads via Pipeboard (alle routes geblokkeerd, zie hieronder) en PostHog via de claude.ai connector (project STX EU, 149694). Geen Google MCPs aangeroepen, niets naar de Meta Ads Tracker Sheet geschreven.

**Samenvatting.** Meta Ads data was voor de tweede dag op rij op geen enkele route bereikbaar. De kill-regels kunnen daardoor niet draaien. PostHog bevestigt dat er sinds 5 september geen betaald verkeer meer binnenkomt en dat alle 8 Wholesaler-ads dus effectief stilstaan. Er is één uitzondering om te controleren: één echte Zweedse bezoeker kwam vanochtend via Instagram binnen op de Video 1 (SWE) UTM.

### Databronnen en status

| Route | Status vandaag | Detail |
|---|---|---|
| Pipeboard MCP (claude.ai connector en lokale server) | Geblokkeerd | "requires authentication", niet te herstellen in een non-interactieve sessie |
| Pipeboard directe JSON-RPC (`pk_`-token) | Geblokkeerd | "You have reached the weekly limit for AI tool executions on your Free plan" |
| Facebook-token uit Instagram MCP | Verlopen | Ongeldig sinds 24 augustus, geen ander Meta-token in `~/.claude.json` |
| PostHog claude.ai connector | Werkt | Alle queries hieronder komen hier vandaan |

Het tweede account uit het command (`act_607231713057715`) bestaat niet in de koppeling. Het tweede echte account is AmbitionAvenue (`act_1489853856181844`), zonder campagnes.

### ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd. De kill-regels vereisen impressions en link clicks over `last_3d` uit Meta, en die data is niet beschikbaar. Er is bovendien niets om op te draaien: volgens de laatst bekende stand (4 september, 11:52) staan beide Wholesaler-campagnes, alle 8 ad sets en alle 8 ads op PAUSED. De SYBB-campagne staat sinds 19 april op pauze.

**Totaal gepauzeerd: 0 ads**

**Actielog**
- 2026-09-06 11:30 CEST: `get_campaigns` via Pipeboard JSON-RPC geprobeerd, antwoord "weekly limit reached". Geen Meta-data.
- 2026-09-06 11:30 CEST: PostHog gequeryd op betaalde pageviews, wholesaler-events en sessiedetails 2 t/m 6 september. Resultaten hieronder.

### PostHog bevestiging: betaald verkeer per dag

Betaalde sessies (pageviews met `utm_medium=paid`, `utm_source=facebook` of een `fbclid`) op sempertexeurope.com:

| Dag | Sessies LIT | Sessies SWE | Zonder UTM (fbclid) | Totaal | Form starts | Inzendingen |
|---|---|---|---|---|---|---|
| 2 sep | 79 | 54 | 5 | 138 | 5 | 3 |
| 3 sep | 108 | 76 | 2 | 186 | 5 | 1 |
| 4 sep | 22 | 25 | 3 | 50 | 4 | 1 |
| 5 sep | 0 | 0 | 4 | 4 | 0 | 0 |
| 6 sep (tot nu) | 0 | 1 | 0 | 1 | 0 | 0 |

De vier fbclid-sessies op 5 september kwamen via proballoonshop.co.uk (een Britse retailer die naar de inspiratiepagina linkt) en één direct bezoek uit de Filipijnen. Dat is organisch Facebook-verkeer, geen ad-levering. Sinds de pauze zijn er 0 form starts en 0 inzendingen.

**Check Video 1 (SWE).** Om 04:53 UTC kwam een bezoeker uit Zweden (Android, Chrome, referrer instagram.com) binnen op `/en_GB/become-a-distributor` met `utm_campaign=wholesaler_se&utm_content=video_01`. De sessie is echt: pageview, autocapture en web vitals, 11 seconden op de pagina. Om 06:31 UTC volgde alleen een pageleave met dezelfde UTM in een andere sessie-id, waarschijnlijk dezelfde persoon die de tab later sloot. Eén bezoeker in 48 uur tegenover 10 sessies per dag toen de ad live was, wijst niet op actieve levering. Meest waarschijnlijke oorzaak: een opgeslagen of gedeelde ad-post op Instagram. Omdat ik dit niet in Meta kan verifiëren: **open Ads Manager en controleer of Video 1 (SWE) echt op PAUSED staat.**

### ⚠️ Waarschuwingen

Geen verse Meta-data, dus geen nieuwe waarschuwingen. Deze signalen uit de eindstand van 4 september blijven staan voor de herstart:

| Ad of campagne | Signaal | Waarde (27 aug t/m 4 sep) | Actie aanbevolen |
|---|---|---|---|
| Wholesaler (LIT) campagne | Creative fatigue | Frequency 3,97 | Ad sets samenvoegen, nieuwe hooks |
| Video 2 (SWE) | Dure reach | CPM €17,07, CPC (link) €1,11 | Niet terugzetten |
| Video 1 (SWE) | Dure reach, geen conversie | CPM €15,27, €126,75 spend, 0 inzendingen | Niet terugzetten |
| Tracking | Meta ziet 19 leads, PostHog 33 | 9 inzendingen zonder UTM | Fixen voor herstart |
| Databron | Meta 2 dagen onbereikbaar | Weeklimiet Pipeboard Free | Zie randvoorwaarde onder de voorstellen |

### 📊 70-20-10 Classificatie

Huidig budget: €0,00 per dag, alles staat op PAUSED. De classificatie hieronder is de laatst bekende stand (27 augustus t/m 4 september) en geldt als vertrekpunt voor de herstart. Per-ad Link CTR en CPC (link) zijn niet volledig bewaard in eerdere rapporten; waar bekend staan ze erbij.

**70% Core (voorgesteld €100 van €140 per dag):**
- Statisch 2 (SWE): Link CTR 2,2%, beste doorklik van het account
- Video 1 (LIT): €29,38 per inzending
- Video 2 (LIT): €28,75 per inzending, goedkoopste leadbron. Link CTR zat op 4 september op 0,7%, net onder de kill-drempel; zie voorstel 4

**20% Emerging (voorgesteld €30 van €140 per dag):**
- Statisch 2 (LIT): CPC (link) €0,43, laagste van het account, maar €60,48 per inzending
- Statisch 1 (LIT): Link CTR 0,6% (gepauzeerd door auto-optimize op 4 september), maar 3,2% sessie-naar-inzending. Alleen terug met een nieuwe eerste zin

**10% Experimental (voorgesteld €10 van €140 per dag):**
- Nieuwe hook-varianten op het Statisch 2 visual (zie voorstel 3). Alle 8 ads gebruikten tot nu toe exact dezelfde tekst per land

**Niet herstarten:** Video 1 (SWE) en Video 2 (SWE).

**Budget mismatch:** Niet van toepassing, er loopt geen budget.

### 💡 Voorstellen (wacht op goedkeuring)

Ongewijzigd ten opzichte van 5 september. Niets hiervan is uitgevoerd.

**0. Randvoorwaarde: Meta-data herstellen**
- Kies één van: Pipeboard upgraden naar Pro, de Pipeboard connector opnieuw autoriseren via `/mcp` in een interactieve sessie, of een Meta System User token met `ads_read` en `ads_management` als fallback op de Marketing API.
- Reden: zonder Meta-data kan auto-optimize niet pauzeren, niet classificeren en de herstart niet bewaken.
- Verwachte impact: morning report, ads-report en auto-optimize werken weer vanaf de volgende run.

**1. Tracking fixen voor de herstart**
- Meta telt 19 leads, PostHog 33 inzendingen, 9 inzendingen hebben geen UTM. Meta optimaliseert op de helft van het signaal.
- Actie: Meta pixel lead-event koppelen aan `wholesaler_form_submit` en UTM's op alle ad-URL's controleren.

**2. Budget herverdeling bij herstart, €140,00 per dag**
- Statisch 2 (SWE): €40,00 per dag
- Video 1 (LIT): €30,00 per dag
- Video 2 (LIT): €30,00 per dag
- Statisch 2 (LIT): €20,00 per dag
- Statisch 1 (LIT) met nieuwe hook: €10,00 per dag
- Experimentele hook-varianten: €10,00 per dag
- Video 1 (SWE) en Video 2 (SWE): niet terugzetten (€0,00)
- Verwachte impact: kostprijs per inzending terug richting €25 tot €30 in plaats van €67.

**3. Nieuwe variaties**
- Drie hook-varianten per land op het winnende Statisch 2 visual, plus een CTA-test SEE_DETAILS versus APPLY_NOW. Copy staat uitgewerkt in het rapport van 4 september.

**4. Beslissing over Video 2 (LIT)**
- Optie A (mijn advies): conversie-guard toevoegen aan de kill-regel, zodat een ad met Link CTR onder 0,8% pas wordt gepauzeerd als er ook 0 inzendingen zijn in 3 dagen.
- Optie B: strikt pauzeren bij de volgende run zodra de Link CTR weer onder 0,8% zit.

**5. Audience aanpassingen**
- LIT: vier ad sets samenvoegen naar twee met Advantage+ budget, om de frequency onder 3,5 te houden.
- SWE: audience verbreden naar 21+ en placements beperken tot feeds, om de CPM onder €15 te krijgen.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**
