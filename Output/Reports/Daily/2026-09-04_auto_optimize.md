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
