# Morning Report — 2026-06-30

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

API Error: Connection closed mid-response. The response above may be incomplete.

---

API Error: Connection closed mid-response. The response above may be incomplete.

---

Klaar. Rapport opgeslagen, gecommit en gepusht.

## Samenvatting — Auto-Optimize 30 juni 2026

**Geen actieve campagnes gevonden, dus geen acties uitgevoerd.**

- **`act_567892422940728`** (Sempertex, primair): toegankelijk, maar alle 5 campagnes staan op **PAUSED** — inclusief `2026: SYBB` (€100/dag).
- **`act_607231713057715`**: het token heeft **geen toegang** tot dit account (alleen `act_567892422940728` en `act_1489853856181844` zijn toegestaan).
- **`act_1489853856181844`**: toegankelijk, **0 actieve campagnes**.

Daardoor:
- ⚡ **0 ads gepauzeerd** (geen kill-regels van toepassing zonder live ads)
- ⚠️ Geen waarschuwingen (niets te meten)
- 📊 Geen 70-20-10 classificatie of budgetvoorstellen mogelijk

**Aandachtspunt:** de `2026: SYBB`-campagne staat sinds 19 april op pauze. Zolang er geen campagne live is, levert dit command elke run een leeg rapport. Zodra je een campagne activeert, hervatten de kill-regels (Link CTR < 0.8% / CPC link > €1.50) en de budgetanalyse automatisch.

Rapport: `Output/Reports/Daily/2026-06-30_auto_optimize.md`

Alleen Meta Ads MCP gebruikt; geen Google MCPs aangeroepen en niets naar de Google Sheet geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
