## Auto-Optimize Rapport — 11 July 2026

Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-11_auto_optimize.md` (gecommit en gepusht).

**Belangrijkste bevinding: er zijn geen actieve Meta Ads campagnes, dus er is niets te optimaliseren.**

| Account | Status | Bevinding |
|---------|--------|-----------|
| `act_567892422940728` (primair) | ✅ Toegang | 0 actieve campagnes — alle 5 op PAUSED |
| `act_1489853856181844` | ✅ Toegang | 0 actieve campagnes |
| `act_607231713057715` | ❌ Geen toegang | Token heeft geen rechten op dit account |

Concreet:
- **⚡ Automatische acties:** 0 ads gepauzeerd (geen actieve ads om tegen de kill-regels te toetsen).
- **⚠️ Waarschuwingen:** geen.
- **📊 70-20-10 / 💡 Voorstellen:** niet van toepassing zonder actieve ads.

Twee dingen om te weten:
1. De hoofdcampagne **"2026: SYBB" staat sinds 19 Apr 2026 op PAUSED** (net als de kopie). Als die weer moet lopen, moet je 'm handmatig activeren — daarna kan dit command pas echte optimalisaties doen.
2. Het command noemt `act_607231713057715`, maar de huidige Pipeboard-token heeft **geen toegang** tot dat account. Als je daar wél campagnes verwacht, moet de Pipeboard-connectie/permissies gecheckt worden — anders blijft dat account onzichtbaar voor dit rapport.

Ik heb me strikt aan de regel gehouden: alleen de Meta Ads MCP gebruikt, geen Google MCPs, en niets naar de Google Sheet geschreven.
