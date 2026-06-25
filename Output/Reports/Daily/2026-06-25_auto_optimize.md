Klaar. Hier is de uitkomst.

## Auto-Optimize — 25 juni 2026

**Geen optimalisaties uitgevoerd of voorgesteld — er draaien geen actieve Meta Ads campagnes.**

Wat ik vond:
- **`act_567892422940728` (Sempertex, primair):** geen actieve campagnes. Alle 5 campagnes staan op `PAUSED`, inclusief `2026: SYBB` (dagbudget €100,00, gepauzeerd sinds 19 apr) en de kopie ervan.
- **`act_1489853856181844`:** toegankelijk, geen actieve campagnes.
- **`act_607231713057715` (in het command genoemd):** **niet toegankelijk** met de huidige token. Toegestane accounts: `act_1489853856181844` en `act_567892422940728`. Als hier campagnes draaien, moet de token-toegang eerst worden uitgebreid.

Gevolg:
- **Niveau 1 (kill-regels):** 0 ads gepauzeerd — er is geen live ad-data om Link CTR / CPC (link) tegen te toetsen.
- **Niveau 2 (voorstellen):** geen data-gedreven voorstellen mogelijk. Wel de operationele observatie dat `/ads-auto-optimize` geen waarde levert zolang alles gepauzeerd blijft.

Rapport opgeslagen op `Output/Reports/Daily/2026-06-25_auto_optimize.md` en gecommit + gepusht naar GitHub. Alleen Meta Ads MCP gebruikt; geen Google MCPs, geen schrijfacties naar de tracker-sheet.

Wil je dat ik `2026: SYBB` weer activeer, of de scheduled auto-optimize run tijdelijk pauzeer tot er weer campagnes live staan?
