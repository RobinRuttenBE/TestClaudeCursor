# SYBB Daily Report, 2026-04-20

**Status: niet gegenereerd met verse data — Pipeboard Meta Ads MCP vereist OAuth-authenticatie en PostHog MCP is niet beschikbaar in deze sessie.**

## Waarom geen verse data

Strikte run-regels: alleen Meta Ads MCP (Pipeboard) en PostHog MCP toegestaan. Google MCPs verboden.

- **Pipeboard Meta Ads MCP**: server is geregistreerd (`mcp__pipeboard-meta-ads__*` en `mcp__claude_ai_Pipeboard_Meta_Ads__*`), maar alleen de `authenticate` en `complete_authentication` tools zijn geladen. De daadwerkelijke data-tools (campagne insights, ad set insights, ad insights) worden pas na succesvolle OAuth geladen. Authenticate call liep, maar vereist dat Robin de authorize-URL in de browser opent en terugkoppelt via `complete_authentication`. In een geautomatiseerde morning-report run zonder interactieve sessie kan dit niet voltooid worden.
- **PostHog MCP**: staat niet in de deferred tool lijst van deze sessie. Geen `posthog_*` tools gevonden via ToolSearch. Zonder PostHog geen pageviews, bounce rate, scroll depth, session duration, CTA click rate of session recordings voor `startyourballoonbusiness.com`.

## Laatst bekende staat (uit 2026-04-19 rapport en 2026-04-20 ads rapport)

Campagne **2026: SYBB - Kopie** (ID 120243293329420239), Sempertex Ad Account `act_567892422940728`. Live sinds 2026-04-19 14:25. Oorspronkelijke "2026: SYBB" op PAUSED sinds 2026-04-19 14:29.

### Dag 1 performance (2026-04-19, laatst beschikbare cijfers)

| Metric | Waarde |
|--------|--------|
| Spend | €45,65 |
| Impressions | 3.320 |
| Clicks (all) | 75 |
| Link clicks | 49 |
| CTR | 2,26% |
| CPC (all) | €0,61 |
| Frequency | 1,21 |
| Landing Page Views (Meta pixel) | 37 |
| Initiate Checkout | 4 |
| IC action value | €1.400 |

### Ad variant ranking (laatst bekend)

| Variant | Signaal |
|---------|---------|
| **H12, B3, CTA5** | Winnaar: hoogste CTR (2,82%), laagste all-clicks CPC (€0,48), 1 IC op laagste budget |
| **H11, B3, CTA5** | Meeste volume, 80% LPV rate, 2 van 4 IC's |
| **H13, B3, CTA5** | Pauzeer-kandidaat: laagste CTR (2,01%), hoogste CPM (€15,79), hoogste all-clicks CPC (€0,79) |

### Open vragen die dit rapport had moeten beantwoorden

- Wat is de stand op dag 2 (2026-04-20)? Bevestigt H12 zijn voorsprong, of was dag 1 een variance?
- Hoe verhoudt de Meta-gerapporteerde LPV (37) zich tot PostHog pageviews? Het 24,5% gat tussen link clicks (49) en LPV (37) op dag 1 is nog niet gediagnosticeerd.
- Bounce rate per utm_content — cruciaal voor ad-pagina match analyse.
- Scroll depth distributie — faalt de hero of engaged mensen zich tot voorbij 50%?
- CTA click rate richting `/booking` — staat dit boven de 4% target?
- Frequency op dag 2 — nog ruim onder 3, geen fatigue verwacht, maar te bevestigen.

## Rode vlaggen (structureel, niet dag-specifiek)

- **Observability pijplijn faalt op opeenvolgende dagen.** 2026-04-21 ads rapport en 2026-04-20 SYBB rapport beide zonder verse data. Dit is nu een observability-incident, geen data-incident.
- **PostHog MCP is al minstens sinds 2026-04-19 niet beschikbaar.** Daily report 2026-04-19 meldde dit expliciet. Twee dagen later nog niet opgelost.
- **Pipeboard Meta Ads OAuth token is niet persistent over morning-report runs.** Elk ochtend-script-run moet opnieuw authenticeren — dat werkt alleen interactief.

## Top 3 acties voor vandaag

1. **Pipeboard Meta Ads opnieuw autoriseren en de OAuth-flow tot het einde doorlopen.** Open de URL uit de `authenticate` call van deze sessie, of trigger een nieuwe in een interactieve sessie. Controleer daarna of de tools de OAuth vasthouden over een herstart. Als dat niet lukt, is de conclusie dat morning-report zonder interactie niet werkt en moet de `/ads-report` en `/sybb-report` stap handmatig getriggerd worden.
2. **PostHog MCP terug configureren in `.claude/settings.json` of het equivalent.** Zonder PostHog verliest het SYBB rapport de helft van zijn waarde (bounce, scroll, CTA, recordings). Verifieer dat het project "Default project" bereikbaar is en site filter op `startyourballoonbusiness.com` werkt.
3. **Na herstel beide dagen (2026-04-20 en 2026-04-21) alsnog backfillen.** Draai `/sybb-report` twee keer met expliciete datum en overschrijf deze status-files. Dan is de trend-lijn weer compleet.

---

**Rapport opgeslagen in:** `Output/Reports/Daily/2026-04-20_sybb_report.md`
**Data bronnen gebruikt:** geen (Pipeboard auth pending, PostHog MCP afwezig).
**Geen Google MCPs gebruikt.** Geen verzonnen cijfers.
