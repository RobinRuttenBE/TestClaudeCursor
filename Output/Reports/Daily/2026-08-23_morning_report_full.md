# Morning Report — 2026-08-23

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

API Error: Your computer went to sleep mid-response. The response above may be incomplete.

---

No PostHog MCP surfaced. Let me check the configured MCP servers and test the Pipeboard direct call in parallel.
API Error: Your computer went to sleep mid-response. The response above may be incomplete.

---

Rapport staat in `Output/Reports/Daily/2026-08-23_auto_optimize.md`, gecommit en gepusht.

## Kort: er viel niets te optimaliseren, maar er is wel iets gevonden

**Geen automatische acties uitgevoerd.** Alle 5 campagnes staan op PAUSED, met 0 impressies en €0,00 spend over last_3d, last_30d én last_90d. De kill-regels kunnen niet triggeren bij nul data. Laatste levering was April 2026, het account ligt ongeveer vier maanden stil.

**De echte vondst zit een niveau dieper.** Campagne "2026: SYBB - Kopie" staat op PAUSED, maar bevat 3 ACTIEVE ad sets met samen €100,00 per dag aan budget, elk met één actieve ad. Zolang de campagne gepauzeerd is gebeurt er niets. Zet iemand die campagne aan, dan start er direct €100/dag.

En dat budget staat op precies de verkeerde creatives:

| Nu actief | Historische Link CTR | CPC (link) |
|---|---|---|
| H11 (Kopie 1), €35/dag | 1,5% | €0,89 |
| H13 (Kopie 3), €45/dag | 1,7% | €1,12 |
| H12 (Kopie 2), €20/dag | 1,8% | €1,03 |

Terwijl **H13 in de originele ad set 10,6% Link CTR haalde tegen €0,07 per link click**, en gepauzeerd staat. Alle vier de Core-ads staan uit, 100% van het klaargezette budget staat op de onderste groep.

Opvallend detail: dezelfde hook H13 scoorde 10,6% in de originele ad set en 1,2% in "Kopie 3". Zelfde hook, body en CTA. Het verschil zit dus in targeting of placement, niet in de copy. Dat uitzoeken is waarschijnlijk meer waard dan welke nieuwe hook dan ook.

## Twee dingen die je moet weten over de data

- **De Pipeboard MCP meldde "requires authentication".** Via directe JSON-RPC calls werkt de token gewoon, dus de data is compleet. Dit stond al in je memory en klopte.
- **Het account `act_607231713057715` uit het command bestaat niet.** Er zijn maar twee accounts: Sempertex (`act_567892422940728`) en AmbitionAvenue (leeg, €0 spend). Dat ID mag uit het command weg.

Ook goed om te weten: de MCP negeert `time_increment`, dus een dagelijkse uitsplitsing kon ik niet ophalen. De maandcijfers heb ik via losse queries per maandvenster afgeleid.

De voorstellen in het rapport (creative-selectie herstellen, 70-20-10 budgetverdeling bij herstart) wachten op je goedkeuring, zoals het command voorschrijft. Ik heb niets gewijzigd aan de campagnestructuur.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
