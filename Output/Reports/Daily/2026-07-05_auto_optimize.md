Klaar. Het rapport staat in `Output/Reports/Daily/2026-07-05_auto_optimize.md` en is gecommit + gepusht.

## Samenvatting

**Er zijn geen automatische acties uitgevoerd — omdat er geen actieve campagnes draaien.**

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (primair) | ✅ | **0** — alle 5 campagnes PAUSED |
| `act_1489853856181844` | ✅ | **0** |
| `act_607231713057715` | ❌ geen tokentoegang | n.v.t. |

Belangrijkste bevindingen:
- De hoofdcampagne **2026: SYBB** (dagbudget €100,00) staat sinds **19 april 2026** op PAUSED. Alle Nozzle Up-campagnes zijn ook gepauzeerd.
- **Geen ads gepauzeerd**, geen waarschuwingen, geen 70-20-10 classificatie — er is simpelweg geen live data om tegen de kill-regels (Link CTR < 0.8%, CPC link > €1.50) te toetsen.
- Het in het commando genoemde secundaire account `act_607231713057715` is **niet bereikbaar** met de huidige API-token (toegestaan: `act_567892422940728` en `act_1489853856181844`).

Ik heb me strikt aan de regels gehouden: alleen Meta Ads MCP gebruikt, geen Google MCPs, niet naar de Tracker Sheet geschreven.

Twee dingen die je goedkeuring vragen (geen actie ondernomen):
1. **2026: SYBB heractiveren** als de campagne weer moet lopen — zeg het en ik zet 'm aan.
2. **Token-toegang** voor `act_607231713057715` controleren, of het commando bijwerken naar de toegestane accounts.
