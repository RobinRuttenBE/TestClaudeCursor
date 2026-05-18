# Auto-Optimize Rapport — 18 May 2026

> Run: `/ads-auto-optimize` op 2026-05-18. Databron: Meta Ads MCP (Pipeboard) only. Geen Google MCPs gebruikt, geen Google Sheet beschreven.

## Samenvatting

**Geen actieve Meta Ads campagnes. Geen automatische acties uitgevoerd, geen voorstellen.**

De optimalisatie-logica (kill-regels op Link CTR en CPC link, 70-20-10 classificatie, budget herverdeling) kon niet draaien omdat er geen enkele campagne live staat. Er is geen impressie-, click- of spend-data over de afgelopen 3 dagen.

## Account scan

| Account | Toegang | Resultaat |
|---------|---------|-----------|
| `act_567892422940728` (Sempertex, primair) | Ja | 5 campagnes gevonden, **allemaal PAUSED**. 0 actief. |
| `act_1489853856181844` | Ja | Geen campagnes. |
| `act_607231713057715` | Nee | Token heeft geen toegang tot dit account (toegestaan: act_1489853856181844, act_567892422940728). |

### Campagnes in act_567892422940728 (allen PAUSED)

| Campagne | ID | Objective | Status | Laatst gewijzigd |
|----------|----|-----------|--------|------------------|
| 2026: SYBB - Kopie | 120243293329420239 | OUTCOME_SALES | PAUSED | 2026-04-20 |
| 2026: SYBB | 120239435987290239 | OUTCOME_SALES | PAUSED | 2026-04-19 |
| Last push Nozzle Up | 120233295855990239 | OUTCOME_SALES | PAUSED | 2025-09-21 |
| Nozzle Up END OF AUGUST | 120232324822740239 | OUTCOME_SALES | PAUSED | 2025-09-15 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | OUTCOME_SALES | PAUSED | 2025-09-15 |

De hoofdcampagne `2026: SYBB` (dagbudget €100,00) staat sinds 2026-04-19 op pauze.

## Niveau 1 — Automatische acties

Geen ads gepauzeerd. Er zijn geen actieve ads om tegen de kill-regels (Link CTR < 0,8% bij >= 1.000 impressions; CPC link > €1,50 bij >= 500 link clicks) te toetsen.

## Niveau 2 — Voorstellen

Geen budget-, variatie- of audience-voorstellen. Zonder live performance-data is elke classificatie of budget-aanbeveling speculatief.

## Aanbevolen vervolgactie (vereist beslissing Robin)

1. **Wil je dat `2026: SYBB` (ID 120239435987290239) weer geactiveerd wordt?** Pas dan kan deze automatische optimalisatie zinvol draaien. Dit is een Niveau 2 actie en wordt niet zonder jouw expliciete goedkeuring uitgevoerd.
2. Controleer of de Pipeboard token toegang nodig heeft tot `act_607231713057715`. Nu is dat account onzichtbaar voor deze flow. (Sluit aan bij eerdere notitie: Pipeboard ziet beperkte accounts.)

---

**Conclusie: niets te optimaliseren tot er minstens 1 campagne actief staat. Geen acties uitgevoerd. Geef aan of je de SYBB campagne wilt heractiveren.**
