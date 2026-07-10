# Auto-Optimize Rapport — 10 juli 2026

**Run:** 2026-07-10 (automatische Meta Ads optimalisatie, laatste 3 dagen)
**Databronnen:** Meta Ads MCP (Pipeboard). PostHog niet geraadpleegd (geen actieve ads om te cross-referencen).
**Primair account:** `act_567892422940728` (Sempertex)

---

## Samenvatting

**Geen actieve campagnes gevonden. Geen acties uitgevoerd, geen voorstellen.**

Alle campagnes op het primaire account staan op `PAUSED`. Er zijn dus geen actieve ads waarop de kill-regels (Link CTR < 0.8%, CPC (link) > €1.50) of de 70-20-10 classificatie kunnen worden toegepast. Dit sluit aan op het daily report van 2026-07-09, waarin al werd vastgesteld dat de SYBB-campagne gepauzeerd is.

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads. ✅

## ⚠️ Waarschuwingen

Geen — geen actieve delivery, dus geen creative fatigue, dure reach of dalende Link CTR te meten.

## 📊 70-20-10 Classificatie

Niet van toepassing. Er zijn geen actieve ads om te classificeren.

**Budget mismatch:** Nee — er staat geen budget live.

## 💡 Voorstellen (wacht op goedkeuring)

Geen data-gedreven voorstellen mogelijk zonder actieve delivery. Wel één operationeel aandachtspunt (zie hieronder).

---

## Accountstatus (context)

### Primair account `act_567892422940728`
Actieve campagnes: **0**. Alle 5 campagnes staan op PAUSED:

| Campagne | Status | Dagbudget | Laatst gewijzigd |
|----------|--------|-----------|------------------|
| 2026: SYBB - Kopie | PAUSED | — | 2026-04-20 |
| 2026: SYBB | PAUSED | €100,00 | 2026-04-19 |
| Last push Nozzle Up | PAUSED | — | 2025-09-21 |
| Nozzle Up END OF AUGUST | PAUSED | €70,00 | 2025-09-15 |
| Campagne Nozzle Up 2025 1 | PAUSED | €30,00 | 2025-09-15 |

### Secundair account `act_607231713057715`
**Niet toegankelijk** met het huidige API-token. Melding van de Meta Ads MCP:
> This API token does not have access to account act_607231713057715. Allowed accounts: act_1489853856181844, act_567892422940728.

Dit account kon dus niet worden geanalyseerd. Let op: het token heeft wél toegang tot `act_1489853856181844`, dat niet in dit command staat. Als daar campagnes draaien, worden die nu niet meegenomen — check met Robin of dit account relevant is voor de auto-optimize.

---

## Actiepunt voor Robin

Er valt niets te optimaliseren zolang alles gepauzeerd staat. Twee dingen om te beslissen:

1. **SYBB heractiveren?** De campagne `2026: SYBB` (€100/dag) staat sinds april op pauze. Zodra die weer live gaat, kan dit command dagelijks de kill-regels en 70-20-10 verdeling toepassen.
2. **Account-scope kloppen?** Het command verwijst naar `act_607231713057715` (geen toegang). Het token dekt wél `act_1489853856181844`. Wil je dat account meenemen, of de command-configuratie bijwerken?

---

*Rapport gegenereerd door /ads-auto-optimize. Alleen Meta Ads MCP gebruikt. Geen Google MCP's aangeroepen, niet naar de Tracker Sheet geschreven.*
