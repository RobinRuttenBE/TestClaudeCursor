Klaar. Rapport opgeslagen en gepusht.

## Auto-Optimize Rapport — 15 juli 2026

**Geen automatische acties uitgevoerd, geen optimalisaties mogelijk.** Alle campagnes op beide toegankelijke ad accounts staan op PAUSED — er zijn geen actieve ads om te toetsen.

**Data-check (Meta Ads MCP, `last_3d`):**

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (primair) | ✅ | 0 (SYBB + 4 Nozzle Up campagnes allemaal PAUSED) |
| `act_1489853856181844` | ✅ | 0 |
| `act_607231713057715` (secundair uit command) | ❌ geen toegang | n.v.t. |

**Twee aandachtspunten voor jou:**

1. **Account-toegang**: het secundaire account in het command (`act_607231713057715`) is niet bereikbaar met dit token. Het token wijst naar `act_1489853856181844`. Wil je het command-ID corrigeren, of de token-toegang laten uitbreiden?

2. **SYBB staat gepauzeerd** (net als in het rapport van 14 juli). Zolang de campagne uit staat, heeft deze run niets te optimaliseren. Zodra "2026: SYBB" weer live gaat, pikt de volgende auto-optimize run automatisch de kill-regels (Link CTR / CPC link) en 70-20-10-classificatie op.

Rapport: `Output/Reports/Daily/2026-07-15_auto_optimize.md` — uitsluitend lokaal opgeslagen, geen Google MCPs aangeroepen, niet naar de tracker Sheet geschreven.
