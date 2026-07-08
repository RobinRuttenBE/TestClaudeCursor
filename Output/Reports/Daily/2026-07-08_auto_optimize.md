## Auto-Optimize Rapport, 8 juli 2026

**Er is niets om te optimaliseren: geen enkele actieve campagne.** Alle campagnes staan op PAUSED.

### ⚡ Automatische acties uitgevoerd
Geen ads gepauzeerd. Er zijn geen actieve ads, dus de kill-regels (Link CTR < 0,8% of CPC (link) > €1,50) waren niet van toepassing.

### 📊 Accountstatus

| Account | Bevinding |
|---------|-----------|
| `act_567892422940728` (primair) | 5 campagnes, **allemaal PAUSED**, inclusief `2026: SYBB` (€100,00/dag) |
| `act_1489853856181844` | Leeg |
| `act_607231713057715` (secundair uit command) | **Niet toegankelijk** met deze token |

### ⚠️ Twee aandachtspunten voor jou

1. **De SYBB-campagne staat uit.** `2026: SYBB` is sinds 19 april 2026 gepauzeerd. Zolang die op PAUSED staat is er geen live data, en kan noch deze optimizer noch het dagelijkse SYBB-rapport iets meten. Zet hem op ACTIVE als hij weer moet lopen, dan pakt de volgende run wel op.
2. **Tweede account niet bereikbaar.** Het command noemt `act_607231713057715`, maar de token heeft daar geen toegang (toegestaan: `act_1489853856181844` en `act_567892422940728`). Controleer het account-ID of de token-permissies.

Rapport opgeslagen in `Output/Reports/Daily/2026-07-08_auto_optimize.md` en gecommit + gepusht naar GitHub. Alleen Meta Ads MCP gebruikt, geen Google MCPs, niet naar de Google Sheet geschreven.
