# Morning Report — 2026-06-26

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Done. Rapport opgeslagen in `Output/Reports/Daily/2026-06-26_ads_report.md`.

## Meta Ads Rapport — 26 June 2026

**Belangrijk:** er zijn **geen actieve campagnes** (beide accounts staan volledig op PAUSED, geen spend in de laatste 30 dagen). Hieronder de **lifetime performance** van de 5 meest recente gepauzeerde campagnes.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|--------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

\* SYBB ROAS is **onbetrouwbaar**: de purchase-waarde (€44.247 / 6 = €7.374 per aankoop) oogt als een pixel value-misconfiguratie. CTR/CPC/CPM zijn wel betrouwbaar en uitstekend.

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 (>€0,50) én CPM €16,34 (>€15). Kleine, dure kopie-test. Niet heractiveren in deze vorm.
- **Nozzle Up END OF AUGUST** — CTR 1,0% (grensgeval). Enorme goedkope reach (CPM €1,64) maar lage engagement.
- **Last push Nozzle Up** — ROAS 0,8x, onder break-even. Afsluit-burst rendeerde niet.

### Top performers
- **Beste CTR**: 2026: SYBB — 4,1%
- **Laagste CPC**: Nozzle Up END OF AUGUST — €0,17
- **Beste betrouwbare ROAS**: Campagne Nozzle Up 2025 1 — 8,3x

### Samenvatting
- **Totaal spend**: €4.867,46 (lifetime, komt exact overeen met account-totaal)
- **Beste performer**: Nozzle Up 2025 1 (8,3x ROAS, gezonde CTR/CPC) — bewezen winnaar
- **Slechtste performer**: Last push Nozzle Up (0,8x ROAS)
- **Aanbeveling (70-20-10)**: er draait nu niets. Zet 70% budget op de bewezen winnaars (SYBB hoofdcampagne + Nozzle Up 2025 1). **Verifieer eerst de SYBB pixel purchase-value** voor je opschaalt, anders stuur je op een vals ROAS-signaal.

### Google Sheet
Overgeslagen op verzoek (strikte MCP-regel). Alleen lokaal opgeslagen.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Wil je dat ik bovendien de PostHog landing page data (startyourballoonbusiness.com) ophaal om de SYBB-funnel te diagnosticeren? Dan combineer ik die met de Meta-data hierboven.

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-06-25_sybb_report.md` (gecommit en gepusht).

**Belangrijkste bevindingen voor 25 juni:**

1. **Meta Ads — campagne ligt stil.** "2026: SYBB" (`120239435987290239`) staat op **PAUSED**. Nul delivery gisteren, nul over de hele 7-daagse vergelijkingsperiode (18–24 jun), en ook nul over de laatste 30 dagen (controle). Dus: geen spend, impressies, clicks of leads via Meta.

2. **PostHog — niet beschikbaar deze run.** De PostHog MCP stond op "connecting" maar registreerde geen tools. Ik heb het meerdere keren geprobeerd via ToolSearch; er kwamen geen `mcp__posthog__*` functies beschikbaar. De landing page sectie kon dus niet gevuld worden. Dit is duidelijk geflagd in het rapport (sectie 3 + rode vlag).

3. **Extra signaal:** er bestaat een tweede gepauzeerde campagne "2026: SYBB - Kopie" (`120243293329420239`) — mogelijk opruimwerk.

**Top acties in het rapport:** beslissen over heractivatie van de campagne, de PostHog MCP-verbinding herstellen vóór het volgende rapport, en de duplicaat-campagne opruimen.

Conform de strikte regel heb ik **alleen** de Meta Ads MCP en (poging tot) PostHog MCP gebruikt — geen Gmail, Calendar, Drive, Sheets, Docs of Slides, en niets naar de Google Sheet tracker geschreven. Output staat uitsluitend lokaal.

Twee dingen om te weten: zolang de campagne gepauzeerd blijft, zal elk dagelijks rapport leeg zijn aan adzijde. En de PostHog-helft blijft ontbreken tot die MCP-verbinding werkt — wil je dat ik daar nu naar kijk?

---

Klaar. Het rapport staat opgeslagen in `Output/Reports/Daily/2026-06-26_auto_optimize.md` en is gecommit + gepusht.

## Uitkomst van deze run

**Er is niets te optimaliseren: alle campagnes staan op PAUSED.**

Wat ik vond bij het ophalen van de data (alleen Meta Ads MCP gebruikt, geen Google MCPs, niet naar de Sheet geschreven):

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (primair) | ✅ | **0** — alle 5 campagnes PAUSED |
| `act_1489853856181844` | ✅ | 0 |
| `act_607231713057715` | ❌ geen toegang | n.v.t. |

Twee dingen die ik wil aanstippen:

1. **Het in het command genoemde alternatieve account `act_607231713057715` is niet toegankelijk** met de huidige token. De token geeft toegang tot `act_567892422940728` en `act_1489853856181844`. Ik heb dat tweede toegankelijke account meegenomen, ook leeg.

2. **De hoofdcampagne 2026: SYBB (dagbudget €100,00) staat sinds 19 april op PAUSED.** Dit sluit aan op het SYBB dagrapport van gisteren.

Omdat er geen live delivery is, zijn de kill-regels (Link CTR < 0,8%, CPC (link) > €1,50) niet getriggerd, is er geen 70-20-10 classificatie mogelijk en zijn er geen data-gedreven voorstellen.

**Wil je de SYBB campagne opnieuw activeren?** Zo ja, dan draait deze auto-optimize flow bij de volgende run op echte data. Zolang alles gepauzeerd blijft, kan de dagelijkse run worden overgeslagen.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
