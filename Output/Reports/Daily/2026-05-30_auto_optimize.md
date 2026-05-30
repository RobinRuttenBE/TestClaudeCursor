Klaar. Hier is wat er gebeurde:

## Auto-Optimize — 30 mei 2026

**Er draaien geen actieve Meta Ads campagnes**, dus er is niets te optimaliseren. De run is correct gestopt na de data-check.

**Bevindingen:**
- **`act_567892422940728` (Sempertex, primair):** 0 actieve campagnes. Alles staat op PAUSED, inclusief `2026: SYBB` (dagbudget €100,00, gepauzeerd sinds 19 april). Dit klopt met het SYBB dagrapport van 29 mei ("campaign paused, no LP traffic").
- **`act_607231713057715` (secundair, uit het command):** **niet toegankelijk** met de huidige token. De token kent alleen `act_567892422940728` en `act_1489853856181844`. → Het account-ID in het command lijkt verouderd, het melden waard.
- **`act_1489853856181844` (extra toegankelijk):** ook 0 actieve campagnes.

**Acties:**
- ⚡ Niveau 1 (automatisch pauzeren): **0 ads** — geen actieve ads om tegen de kill-regels te toetsen.
- 💡 Niveau 2 (voorstellen): geen data-gedreven voorstellen mogelijk zonder live performance. Enig operationeel signaal: als SYBB weer moet draaien, moet jij de campagne reactiveren.

Alleen de Meta Ads MCP is gebruikt; geen Google MCPs, geen schrijfacties naar de tracker-sheet. Rapport opgeslagen op `Output/Reports/Daily/2026-05-30_auto_optimize.md` en gecommit + gepusht.

Twee dingen om over te beslissen:
1. Wil je `2026: SYBB` heractiveren? Draai dit command dan opnieuw zodra de campagne ≥24 uur live is.
2. Klopt het secundaire account-ID in het command nog? Mogelijk moet `act_607231713057715` vervangen worden door `act_1489853856181844`.
