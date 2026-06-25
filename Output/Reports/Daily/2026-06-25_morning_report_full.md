# Morning Report — 2026-06-25

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Klaar. Het rapport is opgeslagen, gecommit en gepusht.

**Korte recap:**
- Alleen Meta Ads MCP (Pipeboard) gebruikt, geen Google MCPs, niet naar de Google Sheet geschreven.
- Geen actieve campagnes → lifetime data van de gepauzeerde SYBB campagnes getoond.
- Winnaar = ad **H13** (€0,07 CPC, 9,8% CTR); 4 underperformers geflagd.
- Belangrijkste actiepunt: **pixel purchase value herstellen** — de ROAS is nu onbruikbaar.

Geef de landing page metrics door (visitors, opt-in/booking clicks, add to cart, purchases) als je de funnel diagnose erbij wilt, dan draai ik die automatisch.

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-06-24_sybb_report.md` en is gecommit + gepusht.

## Wat er uit de data kwam

**Meta Ads (Pipeboard MCP) — account `act_567892422940728`:**
- Campagne `2026: SYBB` (en de kopie) staat op **PAUSED**, daily budget €100.
- Geen spend/impressies/clicks op 24 juni, en ook niets in de laatste 7 dagen. Op accountniveau is 24 juni helemaal leeg. Er was dus geen betaalde activiteit om te rapporteren.

**PostHog (MCP):**
- De PostHog MCP-tools zijn deze run **niet beschikbaar geworden** (server stond als "connecting" maar leverde geen tools; meerdere zoekpogingen leverden niets op). Landing page health, scroll depth en funnel drop-off konden daardoor niet worden opgehaald.

## Belangrijke keuze
Ik heb **geen cijfers geschat of verzonnen** voor de ontbrekende secties — die zijn expliciet gemarkeerd als "geen data". Beide databeperkingen staan als rode vlaggen in het rapport.

## Twee dingen die je aandacht vragen
1. **De SYBB campagne staat al langer op pauze** — zonder heractivatie blijft dit dagrapport elke ochtend leeg. Wil je hem weer live, of is dit bewust?
2. **PostHog MCP-verbinding herstellen** vóór de volgende run, anders blijft de helft van het rapport blind.

Naleving van je strikte regel: alleen Meta Ads MCP en (poging tot) PostHog MCP gebruikt, geen enkele Google MCP, en de output is uitsluitend naar een lokaal markdown-bestand geschreven.

---

Klaar. Hier is de uitkomst.

## Auto-Optimize — 25 juni 2026

**Geen optimalisaties uitgevoerd of voorgesteld — er draaien geen actieve Meta Ads campagnes.**

Wat ik vond:
- **`act_567892422940728` (Sempertex, primair):** geen actieve campagnes. Alle 5 campagnes staan op `PAUSED`, inclusief `2026: SYBB` (dagbudget €100,00, gepauzeerd sinds 19 apr) en de kopie ervan.
- **`act_1489853856181844`:** toegankelijk, geen actieve campagnes.
- **`act_607231713057715` (in het command genoemd):** **niet toegankelijk** met de huidige token. Toegestane accounts: `act_1489853856181844` en `act_567892422940728`. Als hier campagnes draaien, moet de token-toegang eerst worden uitgebreid.

Gevolg:
- **Niveau 1 (kill-regels):** 0 ads gepauzeerd — er is geen live ad-data om Link CTR / CPC (link) tegen te toetsen.
- **Niveau 2 (voorstellen):** geen data-gedreven voorstellen mogelijk. Wel de operationele observatie dat `/ads-auto-optimize` geen waarde levert zolang alles gepauzeerd blijft.

Rapport opgeslagen op `Output/Reports/Daily/2026-06-25_auto_optimize.md` en gecommit + gepusht naar GitHub. Alleen Meta Ads MCP gebruikt; geen Google MCPs, geen schrijfacties naar de tracker-sheet.

Wil je dat ik `2026: SYBB` weer activeer, of de scheduled auto-optimize run tijdelijk pauzeer tot er weer campagnes live staan?

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
