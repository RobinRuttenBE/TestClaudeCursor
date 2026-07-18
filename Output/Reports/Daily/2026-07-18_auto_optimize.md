Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-18_auto_optimize.md`, gecommit en gepusht.

## Samenvatting

**Geen optimalisaties uitgevoerd — er zijn geen actieve campagnes.**

Wat ik gecheckt heb (alleen Meta Ads MCP, geen Google MCPs, niets naar de Google Sheet geschreven):

- **`act_567892422940728`** (primair) → 0 actieve campagnes. Alle 5 campagnes staan PAUSED, inclusief `2026: SYBB` (dagbudget €100,00, laatst gewijzigd 19 April 2026) en de kopie ervan.
- **`act_1489853856181844`** (token-toegestaan) → geen campagnes.
- **`act_607231713057715`** (in command genoemd) → **niet toegankelijk** met deze API-token. Toegestane accounts zijn alleen `act_1489853856181844` en `act_567892422940728`.

**Resultaat:** 0 ads gepauzeerd, geen waarschuwingen, geen 70-20-10 classificatie mogelijk, 0 voorstellen. De kill-regels en budget-logica hebben geen delivery om op te werken.

**Enige relevante actie voor jou:** de SYBB-campagne staat gepauzeerd. Wil je die opnieuw activeren? Zodra er ≥ 24 uur delivery is, draait dit command automatisch de kill-regels en classificatie.

Eén ding om te weten: het account `act_607231713057715` uit het command is niet bereikbaar met de huidige token — als daar wél live campagnes draaien, moet de token-toegang eerst geregeld worden voordat ik dat kan meenemen.
