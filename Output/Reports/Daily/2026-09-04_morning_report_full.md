# Morning Report — 2026-09-04

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport staat in `Output/Reports/Daily/2026-09-04_ads_report.md`, gecommit en gepusht (b3a8c18a). Alleen Meta Ads (Pipeboard, via directe JSON-RPC omdat de MCP "requires authentication" meldt) en PostHog (directe REST API, MCP gaf 405) gebruikt. Geen Google MCPs, niets naar de Sheet geschreven.

## Meta Ads Rapport, 4 september 2026

Twee actieve campagnes, beide lead-campagnes naar `/en_GB/become-a-distributor`. Ze draaien sinds 27/28 augustus, dus last_30d is feitelijk lifetime. Geen ROAS mogelijk, in plaats daarvan kostprijs per formulierinzending uit PostHog.

| Campagne | Spend | Impr. | Link CTR | Link CPC | CPM | Freq. | Leads Meta | Inzendingen PostHog | € / inzending |
|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €532,78 | 85.830 | 1,0% | €0,62 | €6,21 | 3,88 | 11 | 16 | €33,30 |
| Wholesaler (SWE) | €480,76 | 37.256 | 1,8% | €0,72 | €12,90 | 3,25 | 7 | 8 | €60,10 |

PostHog telt 33 inzendingen in totaal, Meta 18. Negen inzendingen hebben geen ad-UTM.

**Belangrijkste bevinding: inzendingen dalen bij gelijk verkeer.** Van 28 t/m 31 augustus kwamen gemiddeld 5,3 inzendingen per dag binnen, van 1 t/m 3 september nog 1,7 per dag. Sessies op de landing page bleven rond de 200 per dag, bounce rate ook stabiel. De kostprijs per inzending is in vier dagen van rond €25 naar rond €95 gegaan. Frequency LIT zit op 3,88 op campagneniveau. Dit is creative fatigue, en het maakt de hook-test die op 3 september is voorgesteld urgent.

**Underperformers**
- **Video 1 (SWE)**: €121,25, 110 sessies, 0 inzendingen. CPM €15,33. Pauzeren.
- **Video 2 (SWE)**: CPM €17,10, Link CPC €1,12 (duurste ad), €59,50 per inzending. Naar €10/dag.
- **Statisch 1 (LIT)**: Link CTR 0,60%, maar 3,0% sessie-naar-inzending. Houden onder de kill-regel "0,8% én 0 inzendingen in 3 dagen". Staat nu op 2 dagen.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,42) maar €60,48 per inzending en 53 seconden op pagina. Niet opschalen.

**Top performers**
- Beste CTR: Statisch 2 (SWE), 4,0% all-clicks, 2,2% link.
- Laagste CPC: Statisch 2 (LIT), €0,20.
- Laagste kostprijs per inzending: Video 2 (LIT) €27,14, dan Video 1 (LIT) €27,91.

**Aanbevelingen in volgorde**
1. Video 1 (SWE) pauzeren, Video 2 (SWE) naar €10, vrijgekomen €30 naar Statisch 2 (SWE) en de LIT-video's. Budget-neutraal op €160/dag.
2. Creative refresh deze week: 3 hook-varianten per land in de bestaande ad sets.
3. Tracking check: verifieer of het Meta Lead-event vuurt bij inzending. Meta ziet 18, PostHog 33.
4. Statisch 1 (LIT) morgen pauzeren als er weer 0 inzendingen zijn.

**Opmerkingen**
- Het account `act_607231713057715` uit het command bestaat niet in de koppeling. Het tweede account is AmbitionAvenue, zonder spend.
- Account-totaal is €1.060,57, waarvan €47,03 niet toewijsbaar aan de twee actieve campagnes (restspend SYBB begin augustus).
- Funnel data na de inzending (gesprek gepland, distributeur actief, eerste order) zit niet in Meta of PostHog. Als je die cijfers hebt, kan ik de volledige funnel-diagnose draaien.

---

Het rapport staat in `Output/Reports/Daily/2026-09-03_sybb_report.md` en is gecommit en gepusht naar main (commit dfbdef31).

**Databronnen.** De Pipeboard MCP meldde "requires authentication" en de posthog SSE server gaf HTTP 405. Meta Ads data is opgehaald via de directe JSON-RPC call met de geconfigureerde Pipeboard-token, PostHog data via de claude.ai PostHog connector op project STX EU. Geen Google MCP's aangeroepen, niets naar de Google Sheet geschreven.

**Belangrijkste bevindingen voor 3 september:**
- **Meta Ads:** campagne `2026: SYBB` en de kopie staan nog op PAUSED, nul spend en nul impressies over de hele week. Het account draaide alleen de wholesaler campagnes LIT en SWE.
- **Landing page:** startyourballoonbusiness.com had 0 bezoekers, ook over de afgelopen 7 dagen.
- **Werkelijke funnel (event registratiepagina's op sempertexeurope.com):** 2 bezoekers tegenover een 7-daags gemiddelde van 6,1. Beide kwamen via site navigatie, één shopbezoeker die de FR-pagina van editie 47 bekeek, één directe bezoeker die editie 8 en 9 vergeleek. Geen bounces, geen rage clicks, geen recordings.
- **Weekbeeld:** 30 unieke bezoekers in 7 dagen, verdeeld over 6 edities. Edities 9, 47 en 48 zijn nieuw sinds eind augustus, editie 7 blijft de trekker met 15 bezoekers.
- **Conversie:** nog steeds onmeetbaar, er is geen registratie-voltooid event. Wel nieuw vastgesteld dat autocapture en pageleave site-breed draaien, dus bounce en sessieduur op de event funnel zijn betrouwbaar.

**Top 3 acties in het rapport:** een registratie-voltooid event toevoegen, handmatig checken of de inschrijving een klantaccount vereist, en de nieuwe edities 47 en 48 één owned verkeersbron geven met UTM's via nieuwsbrief of story.

**Memory bijgewerkt:** in de PostHog-referentie staat nu dat de claude.ai PostHog connector als alternatief werkt en hoe je recordings telt via de replay-tabel.

---

Klaar. Rapport staat in `Output/Reports/Daily/2026-09-04_auto_optimize.md`, gecommit en gepusht (a09e7c01). Alleen Meta Ads (Pipeboard via directe JSON-RPC, MCP meldt "requires authentication") en PostHog (claude.ai connector) gebruikt. Geen Google MCPs, niets naar de Sheet.

**Automatische actie uitgevoerd**
- **Statisch 1 (LIT) gepauzeerd.** Link CTR 0,5% op 14.147 impressions in de laatste 3 dagen, 0 inzendingen. Meta bevestigde de statuswijziging. Dit is de pauze die het ads-rapport van vanochtend al aankondigde.

**Kill-regel getriggerd maar niet uitgevoerd**
- **Video 2 (LIT)** zit met 0,7% net onder de drempel, maar is de goedkoopste leadbron van het account (5 inzendingen, €28,54 per inzending, 1 inzending in de laatste 3 dagen). Pauzeren op CTR alleen zou de LIT lead-flow schaden. Ik heb de ad laten draaien en de beslissing aan jou voorgelegd: conversie-guard aan de regel toevoegen, of strikt pauzeren in de volgende run.

**Waarschuwingen**
- Video 2 (SWE) CPM €16,67 en Video 1 (SWE) €14,55. Zweedse reach is twee keer zo duur als Litouwse.
- LIT campagne-frequency 3,88 lifetime door vier ad sets op dezelfde audience. Inzendingen zijn gedaald van 5,2 naar 1,5 per dag bij stabiel verkeer.

**Belangrijkste vondst**
- Alle 8 ads gebruiken exact dezelfde tekst per land. De enige variabele is het visual. De hook-test die op 3 september is voorgesteld is dus nog niet gestart.

**Voorstellen die op goedkeuring wachten**
1. Budget herverdeling, neutraal op €140/dag: Video 1 (SWE) pauzeren (€126 zonder inzending), Statisch 2 (SWE) naar €35, Video 1 (LIT) naar €30, Statisch 2 (LIT) naar €10.
2. Vijf concrete copy-variaties per Hormozi hook type, plus een SEE_DETAILS versus APPLY_NOW test.
3. SWE audience verbreden naar 21+ en placements beperken tot feeds. LIT ad sets samenvoegen naar 2 met Advantage+ budget.
4. Beslissing over Video 2 (LIT).
5. Tracking check: Meta telt 18 leads, PostHog 33.

Opmerking: het account act_607231713057715 uit het command bestaat niet in de koppeling. Het tweede account is AmbitionAvenue, zonder campagnes.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
