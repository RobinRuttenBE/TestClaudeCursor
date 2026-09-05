Rapport staat in `Output/Reports/Daily/2026-09-05_ads_report.md`, gecommit en gepusht (f1c9e871). Alleen Meta Ads (Pipeboard via directe JSON-RPC, de MCP meldt "requires authentication") en PostHog (claude.ai connector) gebruikt. Geen Google MCPs, niets naar de Sheet.

## Meta Ads Rapport, 5 september 2026

**Er draait niets meer.** Beide Wholesaler campagnes en alle 8 ads zijn op 4 september tussen 11:50 en 11:52 handmatig gepauzeerd, 25 minuten nadat auto-optimize alleen Statisch 1 (LIT) had stilgezet. Sindsdien geen spend en geen verkeer. Dit rapport is de eindafrekening over 27 augustus t/m 4 september.

| Campagne | Spend | Impr. | Link CTR | Link CPC | CPM | Freq. | Leads Meta | Inzendingen PostHog | € / inzending |
|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,13 | 90.887 | 1,0% | €0,64 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 39.267 | 1,8% | €0,73 | €12,92 | 3,29 | 8 | 8 | €63,41 |
| Totaal | €1.069,37 | 130.154 | 1,2% | €0,68 | €8,22 | 3,73 | 19 | 33 | €32,41 |

**Belangrijkste bevinding.** De eerste vijf dagen leverden 27 inzendingen op, de laatste vier dagen nog 6, bij stabiel verkeer van rond 200 sessies per dag. De kostprijs per inzending ging van ongeveer €25 naar €67 in de laatste drie draaidagen. De creative fatigue van gisteren is bevestigd, dus de pauze was verdedigbaar.

**Underperformers**
- **Video 1 (SWE)**: €126,75, 0 inzendingen, CPM €15,27. Niet opnieuw activeren.
- **Video 2 (SWE)**: CPM €17,07, duurste link click (€1,11), €63,50 per inzending.
- **Statisch 1 (LIT)**: Link CTR 0,6%, maar wel de beste sessie-naar-inzending ratio van LIT (3,2%).
- **LIT campagne**: frequency 3,97 door vier ad sets op dezelfde audience.

**Top performers**
- Beste CTR: Statisch 2 (SWE), 2,2% link.
- Laagste CPC: Statisch 2 (LIT), €0,43 link.
- Goedkoopste inzendingen: Video 2 (LIT) €28,75 en Video 1 (LIT) €29,38.

**Aanbeveling voor de herstart (70-20-10)**
1. Eerst tracking fixen. Meta ziet 19 leads, PostHog 33, en 9 inzendingen hebben geen UTM. Meta optimaliseert nu op de helft van het signaal.
2. 70% op Video 1 (LIT), Video 2 (LIT) en Statisch 2 (SWE). Richtbudget LIT €60/dag, SWE €40/dag.
3. 20% op dezelfde visuals met nieuwe hooks. Alle 8 ads gebruikten tot nu toe exact dezelfde tekst.
4. 10% op Statisch 1 (LIT) met een nieuwe eerste zin.
5. LIT ad sets samenvoegen zodat de frequency onder 3,5 blijft.

**Opmerkingen**
- Het account `act_607231713057715` uit het command bestaat niet. Het tweede account is AmbitionAvenue, zonder spend.
- Funnel data na de inzending (gesprek gepland, distributeur actief, eerste order) zit niet in Meta of PostHog. Als je die cijfers aanlevert, draai ik de volledige funnel-diagnose.
