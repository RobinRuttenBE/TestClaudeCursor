Klaar. Rapport opgeslagen, gecommit en gepusht.

## Auto-Optimize Rapport — 23 juli 2026

**Resultaat: geen actieve campagnes, dus geen optimalisaties uitgevoerd.**

Wat ik vond via de Meta Ads MCP (alleen Meta Ads gebruikt, geen Google MCPs, niets naar de tracker Sheet):

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| act_567892422940728 (primair) | ✅ | **0** — alle 5 campagnes staan op PAUSED |
| act_1489853856181844 | ✅ | 0 |
| act_607231713057715 | ❌ | Token heeft geen toegang |

**Twee aandachtspunten:**

1. **Alles staat op PAUSED**, inclusief `2026: SYBB` (dagbudget €100.00). Zonder live ads met impressies zijn er geen kill-regels, waarschuwingen of 70-20-10 classificatie mogelijk. Wil je SYBB weer laten lopen, dan is heractiveren de eerste stap, dat doe ik niet automatisch.
2. **Toegangsprobleem:** het account `act_607231713057715` uit het command is niet toegankelijk met de huidige Pipeboard-token. Toegestane accounts zijn `act_1489853856181844` en `act_567892422940728`. Dit account moet opnieuw geautoriseerd worden als het meegenomen moet worden.

Rapport staat in `Output/Reports/Daily/2026-07-23_auto_optimize.md`. Laat weten of je een campagne wilt heractiveren of de account-toegang wilt oplossen, dan draai ik de run opnieuw met echte data.
