## Auto-Optimize Rapport — 22 juli 2026

Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-22_auto_optimize.md` (gecommit + gepusht). Alleen Meta Ads MCP (Pipeboard) gebruikt, geen Google MCPs, niets naar de tracker sheet geschreven.

**Kernconclusie: er viel niets te optimaliseren.**

- **Geen actieve campagnes** op beide toegankelijke accounts. In `act_567892422940728` staan alle 5 campagnes op PAUSED — inclusief `2026: SYBB` (sinds 19 apr 2026, €100/dag budget). Account `act_1489853856181844` is leeg.
- **Geen spend** in de laatste 3 dagen → kill-regels (Link CTR < 0,8% / CPC link > €1,50) niet van toepassing, 70-20-10 classificatie niet mogelijk.
- **0 ads gepauzeerd.**

**Twee punten die je aandacht vragen:**

1. **`act_607231713057715`** (het "secundaire" account uit het command) is **niet toegankelijk** met de huidige API-token. Toegestane accounts zijn `act_1489853856181844` en `act_567892422940728`. Fix de token-permissies of haal dit account uit de command-config.
2. **SYBB staat op pauze.** Zolang er geen campagne actief is, levert deze command geen bruikbare output. Zeg het als SYBB weer live moet — dat activeren is een Niveau 2 actie die ik niet zonder jouw akkoord uitvoer.

Zodra er weer verkeer draait, geeft de volgende run een volledige performance-analyse.
