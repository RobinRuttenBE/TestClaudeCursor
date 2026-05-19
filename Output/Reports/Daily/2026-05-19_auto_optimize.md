# Auto-Optimize Rapport, 19 May 2026

Bron: Sempertex Ad Account `act_567892422940728` (primair). Periode: laatste 3 dagen (`last_3d`). Data: Meta Ads MCP (Pipeboard).

## Samenvatting

**Geen actieve campagnes gevonden. Geen automatische acties uitgevoerd, geen optimalisaties mogelijk.**

Alle campagnes in het primaire account staan op PAUSED, inclusief de SYBB campagne. Er zijn dus geen actieve ads waarop de kill-regels of de 70-20-10 classificatie toegepast kunnen worden.

## Account- en campagnestatus

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (Sempertex, primair) | Ja | 0 |
| `act_1489853856181844` | Ja | 0 |
| `act_607231713057715` | Geen toegang (token mist permissie) | n.v.t. |

Campagnes in `act_567892422940728` (allemaal PAUSED):

| Campagne | ID | Objective | Status | Laatst gewijzigd |
|----------|-----|-----------|--------|------------------|
| 2026: SYBB - Kopie | 120243293329420239 | OUTCOME_SALES | PAUSED | 2026-04-20 |
| 2026: SYBB | 120239435987290239 | OUTCOME_SALES | PAUSED | 2026-04-19 |
| Last push Nozzle Up | 120233295855990239 | OUTCOME_SALES | PAUSED | 2025-09-21 |
| Nozzle Up END OF AUGUST | 120232324822740239 | OUTCOME_SALES | PAUSED | 2025-09-15 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | OUTCOME_SALES | PAUSED | 2025-09-15 |

## Automatische acties uitgevoerd

Geen ads gepauzeerd. Er zijn geen actieve ads om te beoordelen tegen de kill-regels (Link CTR < 0.8% bij minimaal 1.000 impressions, of CPC (link) > €1.50 bij minimaal 500 link clicks).

**Totaal gepauzeerd: 0 ads**

## Waarschuwingen

Geen. Geen actieve creatives om op fatigue (Frequency > 3.5), dure reach (CPM > €15) of dalende Link CTR te controleren.

## 70-20-10 Classificatie

Niet van toepassing. Geen actieve ads om te classificeren in Core / Emerging / Experimental.

## Voorstellen (wacht op goedkeuring)

Eén structureel punt, geen ad-niveau optimalisatie:

**1. SYBB campagne staat uit**
- Campagne "2026: SYBB" (120239435987290239, daily budget €100.00) is sinds 2026-04-19 PAUSED. De kopie "2026: SYBB - Kopie" sinds 2026-04-20.
- Zolang deze uit staat levert het dagelijkse auto-optimize draaien geen waarde op en is er geen funnel-data via Meta.
- Aanbeveling: bevestig of SYBB bewust gepauzeerd is. Zo ja, dan kan de dagelijkse auto-optimize tijdelijk stilgelegd worden tot heractivatie. Zo nee: heractiveer de campagne, daarna kan dit command weer ads optimaliseren.

**2. Tweede account toegang**
- `act_607231713057715` is niet bereikbaar met de huidige Pipeboard token (alleen `act_1489853856181844` en `act_567892422940728` toegestaan). Als dit account ads moet draaien, moet de token-permissie of accountkoppeling hersteld worden.

---

**Wil je een of meer van deze voorstellen oppakken? Geef aan welke nummers.**

*Run uitgevoerd op 2026-05-19. Alleen Meta Ads MCP en PostHog MCP gebruikt. Geen Google services aangeroepen, geen schrijfacties naar de Google Sheet tracker.*
