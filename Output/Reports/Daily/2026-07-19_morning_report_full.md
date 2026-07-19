# Morning Report — 2026-07-19

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

API Error: Connection closed mid-response. The response above may be incomplete.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-07-18_sybb_report.md`. Kort samengevat wat ik vond:

## Wat er aan de hand is

**Meta Ads (via Pipeboard MCP — werkte):**
- De campagne **"2026: SYBB"** (`120239435987290239`) staat op **PAUSED**, laatst gewijzigd 19 april 2026 (dagbudget €100, OUTCOME_SALES).
- Gisteren (18 juli 2026): **nul** spend/impressies/clicks — `get_insights` gaf een lege dataset. Ook over de **laatste 7 én 30 dagen geen enkele spend** op het account.
- Er bestaat ook een gepauzeerde kopie **"2026: SYBB - Kopie"** (`120243293329420239`) — let op dubbele levering bij heractivatie.

**PostHog (MCP — NIET bereikbaar):**
- De PostHog MCP-server is in deze sessie nooit met tools verschenen (bleef "connecting"). Ik heb meerdere keren gezocht; geen enkele PostHog-tool geladen. Landing page health, scroll depth, funnel en cross-referencing konden dus **niet** worden opgehaald.
- Conform je strikte regel heb ik **geen** alternatieve bron gebruikt (geen Google Gmail/Calendar/Drive/Sheets/Docs) en niet naar de Google Sheet-tracker geschreven.

## Belangrijkste acties (staan ook in het rapport)
1. Beslis of SYBB weer live moet — heractiveer bewust één campagne, niet beide.
2. Herstel/autoriseer de PostHog MCP-connectie in een interactieve sessie en genereer het rapport opnieuw voor de landing page-cijfers.
3. Draai daarna een verse dagrapportage met `utm_content`-varianten gekruist met LP-gedrag.

Het rapport is bewust een **status- en dataverificatierapport** i.p.v. een performancerapport, omdat er gisteren simpelweg geen SYBB-activiteit en geen PostHog-data was. Wil je dat ik de PostHog-connectie probeer te diagnosticeren, of het rapport later opnieuw draai zodra die weer verbonden is?

---

De run kon **niet** worden voltooid. De Meta Ads API gaf op elke call — bij beide accounts, op elk endpoint, over 7 pogingen in ~1,5 minuut — dezelfde fout terug:

```
"An unexpected error has occurred. Please retry your request later."
type: OAuthException · is_transient: true · code 2
```

Dit is een **tijdelijke storing aan Meta-zijde**, geen configuratiefout. Zelfs de lichtste call (`get_account_info`) faalt, dus het is niet accountspecifiek. Ik heb geen data opgehaald en dus ook **geen ads gepauzeerd en geen voorstellen gedaan** — conform de regel "bij twijfel over datakwaliteit: meld dit en sla over" heb ik niets geraden of gefabriceerd.

Twee dingen die ik onderweg vond:

1. **`act_607231713057715` is niet toegankelijk** met het huidige token. De toegestane accounts zijn `act_567892422940728` (primair, correct) en `act_1489853856181844` (een extra account dat niet in het command stond). Check of je die tweede misschien bedoelde.
2De rest is puur de Meta-storing.

**Aanbeveling:** wacht 15-30 minuten en draai `/ads-auto-optimize` opnieuw — transient OAuth-fouten lossen zich meestal vanzelf op. Blijft het hangen, dan de Pipeboard/Meta OAuth-koppeling opnieuw autoriseren.

Statusrapport opgeslagen in `Output/Reports/Daily/2026-07-19_auto_optimize.md` (alleen lokaal, niets naar Google Sheets geschreven).

Wil je dat ik het over pakweg 20 minuten automatisch opnieuw probeer?

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
