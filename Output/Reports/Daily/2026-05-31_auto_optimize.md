Klaar. Het rapport staat opgeslagen en is gecommit/gepusht.

## Uitkomst: niets te optimaliseren vandaag

**Er draaien geen actieve campagnes.** Daarom zijn er geen automatische acties (Niveau 1) uitgevoerd en geen voorstellen (Niveau 2) gegenereerd.

Wat ik gecontroleerd heb (alleen Meta Ads MCP, geen Google MCPs):

| Ad Account | Resultaat |
|---|---|
| `act_567892422940728` (primair) | 5 campagnes, **allemaal PAUSED** — incl. `2026: SYBB` |
| `act_1489853856181844` | 0 campagnes |
| `act_607231713057715` (genoemd in command) | **Geen token-toegang** |

Twee dingen die jouw aandacht vragen:

1. **`2026: SYBB` staat op PAUSED.** Zonder live ads kunnen de kill-regels (Link CTR < 0.8%, CPC link > €1.50) en de 70-20-10 classificatie niet draaien. Wil je dat ik een herstart voorbereid?
2. **`act_607231713057715` is niet bereikbaar** met de huidige Pipeboard-token (toegestaan zijn alleen `act_1489853856181844` en `act_567892422940728`). Mocht daar wél een campagne draaien, dan mis ik die. Verifieer het account-ID of de token-permissies.

Rapport: `Output/Reports/Daily/2026-05-31_auto_optimize.md`
