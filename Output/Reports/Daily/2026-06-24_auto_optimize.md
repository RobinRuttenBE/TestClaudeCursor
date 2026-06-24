Klaar. Hier de samenvatting:

## Auto-Optimize 24 juni 2026 — geen acties nodig

**Resultaat: geen actieve campagnes gevonden, dus niets geoptimaliseerd.** Geen ads gepauzeerd, geen wijzigingen aangebracht.

**Wat ik controleerde (alleen Meta Ads MCP, geen Google MCPs):**

| Account | Toegang | Actief |
|---------|---------|--------|
| `act_567892422940728` (primair) | ✅ | 0 — alle 5 campagnes PAUSED |
| `act_607231713057715` (in command) | ❌ Geen token-toegang | n.v.t. |
| `act_1489853856181844` (wel toegestaan) | ✅ | 0 |

De hoofdcampagne **"2026: SYBB"** (€100,00/dag) staat sinds 19 april 2026 op pauze. Zonder lopende campagne is er geen Link CTR / CPC-data om kill-regels of de 70-20-10 classificatie op toe te passen.

**Twee aandachtspunten voor jou:**
1. **SYBB-campagne** — beslis of/wanneer die weer aan gaat, anders levert dit dagelijkse command geen waarde.
2. **Command-config** — `act_607231713057715` is niet toegankelijk met dit token. Toegestaan zijn `act_567892422940728` en `act_1489853856181844`. Of het token uitbreiden, of het tweede account-ID in het command corrigeren.

Rapport opgeslagen in `Output/Reports/Daily/2026-06-24_auto_optimize.md` en gecommit + gepusht.

Wil je dat ik een van de twee punten verder oppak?
