Klaar. Rapport opgeslagen op `Output/Reports/Daily/2026-07-21_auto_optimize.md` en gepusht naar GitHub.

## Uitkomst van deze run

**Geen automatische acties uitgevoerd — er zijn geen actieve Meta Ads campagnes.**

Wat ik vond (alleen via Meta Ads MCP / Pipeboard, geen Google MCPs, niets naar de Tracker Sheet):

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (primair) | ✅ | 0 — alle 5 campagnes PAUSED |
| `act_1489853856181844` | ✅ | 0 — geen campagnes |
| `act_607231713057715` | ❌ | Token heeft **geen toegang** tot dit account |

Twee dingen om te weten:

1. **De SYBB-campagne staat op PAUSED** (`120239435987290239`, daily budget €100,00). Zonder live ads zijn er geen kill-regel-checks (Link CTR < 0.8%, CPC link > €1.50), geen fatigue-signalen en geen 70-20-10 classificatie mogelijk. Zodra SYBB weer ≥24 uur draait, levert een volgende run de volledige analyse.
2. **`act_607231713057715` is niet bereikbaar** met de huidige Pipeboard-token. Toegestane accounts zijn `act_1489853856181844` en `act_567892422940728`. Als dat account echt gemonitord moet worden, moet de juiste Facebook-connection gekoppeld worden in Pipeboard.

Er zijn geen voorstellen die op goedkeuring wachten — laat weten wanneer SYBB weer live staat, dan draai ik de complete optimalisatie.
