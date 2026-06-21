# Morning Report — 2026-06-21

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Error: Reached max turns (30)

---

Het rapport is opgeslagen: `Output/Reports/Daily/2026-06-20_sybb_report.md`.

Belangrijk om te weten — twee zaken bepaalden de inhoud:

**1. Meta Ads — campagne stond stil**
`2026: SYBB` (id `120239435987290239`) is **PAUSED** en had op 20 June 2026 geen enkele delivery. Ik heb gisteren, last_7d én een dag-voor-dag breakdown over de laatste 30 dagen opgevraagd: Meta retourneert overal een lege dataset. De campagne heeft simpelweg niet gelopen. Geen spend, impressies, clicks of leads om te rapporteren.

**2. PostHog MCP was niet beschikbaar**
De PostHog MCP exposeert tijdens deze run geen tools en geen resources (bevestigd via meerdere zoekopdrachten + `ListMcpResourcesTool`). Daardoor kon ik de Landing Page Health en Funnel Drop-off secties niet vullen. Conform jouw strikte regel heb ik **geen** Google-bron als alternatief gebruikt, **niets** naar de Tracker Google Sheet geschreven, en **geen cijfers geschat** — die secties staan op "niet beschikbaar".

**Wat ik je aanraad:**
- Beslis of `2026: SYBB` bewust gepauzeerd is of weer live moet (€100/dag budget staat klaar).
- Herstel de PostHog MCP-verbinding; daarna kan ik het rapport opnieuw draaien met volledige LP- en funneldata.

Wil je dat ik nu een ander/actief campagne controleer, of het rapport opnieuw genereer zodra PostHog weer verbonden is?

---

Klaar. Hier de samenvatting van deze run:

## Auto-Optimize — 21 June 2026

**Geen optimalisatie uitgevoerd: er zijn geen actieve campagnes.**

Wat ik vond (alleen Meta Ads MCP gebruikt, geen Google MCPs, niets naar de tracker geschreven):

| Account | Resultaat |
|---|---|
| `act_567892422940728` (Sempertex) | 5 campagnes, **allemaal PAUSED** |
| `act_607231713057715` (uit command) | ❌ Token heeft geen toegang |
| `act_1489853856181844` (wel toegestaan) | 0 campagnes |

De hoofdcampagne **"2026: SYBB"** (€100/dag) staat sinds 19 April 2026 op PAUSED. Omdat er geen ads live zijn, zijn er geen kill-regels getoetst, geen ads gepauzeerd, geen 70-20-10 classificatie en geen budget-voorstellen mogelijk.

**Twee aandachtspunten:**
1. Wil je dat ik de **SYBB-campagne heractiveer**? Daarna kan auto-optimize pas echte data analyseren.
2. Het command verwijst naar `act_607231713057715`, maar de token geeft daar geen toegang toe — mogelijk verkeerd account-ID of permissies die bijgewerkt moeten worden.

Rapport opgeslagen in `Output/Reports/Daily/2026-06-21_auto_optimize.md` en gecommit + gepusht.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
