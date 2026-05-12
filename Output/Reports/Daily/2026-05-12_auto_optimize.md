Rapport opgeslagen op `Output/Reports/Daily/2026-05-12_auto_optimize.md`.

**Uitkomst:**
- **BLOCKED** — Pipeboard Meta Ads MCP geeft op beide accounts (`act_567892422940728` en `act_607231713057715`) `Facebook connection required`. Geen campagne-, ad set- of ad-data opgehaald.
- **Niveau 1: 0 ads gepauzeerd** — geen data om kill-regels (Link CTR < 0,8%, CPC link > €1,50) op uit te voeren.
- **Niveau 2: geen voorstellen** — kan 70-20-10 niet classificeren zonder live performance data.

**Vereiste actie:** Reauthenticeer Pipeboard via de OAuth URL in het rapport (of via https://pipeboard.co/connections), daarna run je `/ads-auto-optimize` opnieuw. Let op: vorige run (11 mei) had ook 0 actieve campagnes — SYBB staat sinds 2026-04-19 PAUSED. Zelfs na auth-herstel kan de uitkomst nog steeds "geen levering" zijn, waarmee de heropstart-discussie de echte vraag deze week is.

Geen Google MCPs aangeroepen, niets naar de Google Sheet tracker geschreven.
