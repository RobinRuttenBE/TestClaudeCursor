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
