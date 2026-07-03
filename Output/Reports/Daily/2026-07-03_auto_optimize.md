Klaar. Rapport opgeslagen, gecommit en gepusht.

## Resultaat auto-optimize — 3 juli 2026

**Geen actieve campagnes → geen optimalisatie mogelijk of nodig.** Alle campagnes staan op PAUSED, dus er zijn geen ads om tegen de kill-regels of de 70-20-10 classificatie te toetsen. Geen automatische acties uitgevoerd, geen voorstellen.

**Account-scan (alleen Meta Ads MCP gebruikt, geen Google MCPs):**

| Account | Bevinding |
|---------|-----------|
| `act_567892422940728` (primair) | 5 campagnes, **allemaal PAUSED** (2× SYBB, 3× Nozzle Up) |
| `act_1489853856181844` | 0 campagnes |
| `act_607231713057715` | **Geen toegang** met deze token |

⚠️ **Twee aandachtspunten:**
1. Het account `act_607231713057715` uit het command is niet bereikbaar met de huidige Pipeboard-token (toegestaan zijn alleen `act_1489853856181844` en `act_567892422940728`). Als dit account meegenomen moet worden, moet de tokenkoppeling in Pipeboard uitgebreid worden.
2. Zodra `2026: SYBB` weer live gaat, draai dit command opnieuw na minimaal 24 uur delivery — dan pas kunnen de kill-regels en classificatie op échte link-metrics draaien.

Rapport staat in `Output/Reports/Daily/2026-07-03_auto_optimize.md`.
