Klaar. Hier is de samenvatting:

## Auto-Optimize Rapport — 29 June 2026

**Belangrijkste bevinding: er zijn geen actieve campagnes om te optimaliseren.**

| Account | Status |
|---------|--------|
| `act_567892422940728` (primair) | ✅ Toegankelijk — maar **0 actieve campagnes**, alle 5 staan op PAUSED |
| `act_607231713057715` (secundair) | ❌ Token heeft geen toegang |

**Acties:**
- ⚡ **0 ads gepauzeerd** — geen actieve ads om tegen de kill-regels (Link CTR < 0.8%, CPC link > €1.50) te toetsen
- ⚠️ Geen waarschuwingen, geen 70-20-10 classificatie, geen budgetvoorstellen — allemaal niet van toepassing zonder live ads

**Twee operationele aandachtspunten:**
1. De `2026: SYBB` campagne (dagbudget €100,00) is de meest recente live SYBB-campagne en staat nu op PAUSED. Zodra die weer actief is (en ≥24u loopt), draait deze run automatisch de volledige analyse.
2. Het Pipeboard-token mist toegang tot `act_607231713057715`. Het heeft wél toegang tot `act_1489853856181844` — dat account staat niet in dit command. Laat weten of dat relevant is, of herauthoriseer de Meta-connectie als het secundaire account meegenomen moet worden.

Rapport opgeslagen in `Output/Reports/Daily/2026-06-29_auto_optimize.md` en gepusht naar GitHub. Conform de strikte regel zijn alleen de Meta Ads MCP gebruikt, geen Google MCPs en niets naar de Google Sheet geschreven.

Wil je dat ik de `2026: SYBB` campagne weer activeer zodat de optimalisatie iets te doen heeft?
