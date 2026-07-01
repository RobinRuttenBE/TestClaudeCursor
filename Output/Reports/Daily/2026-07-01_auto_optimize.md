# Auto-Optimize Rapport — 1 juli 2026

**Run:** `/ads-auto-optimize` (alleen Meta Ads MCP + PostHog MCP, geen Google MCPs, geen Sheet-writes)
**Periode geanalyseerd:** laatste 3 dagen (28 juni – 1 juli 2026)
**Databron:** Meta Ads MCP (Pipeboard)

---

## Samenvatting

**Geen actieve Meta Ads campagnes gevonden. Er zijn geen ads om te optimaliseren.**

Alle kill-regels, waarschuwingsregels en 70-20-10 classificatie zijn niet van toepassing omdat er geen enkele actieve ad draait. Er zijn dus geen automatische acties uitgevoerd en er zijn geen voorstellen te doen.

---

## Account-status

| Account | Toegang | Campagnes | Actief |
|---------|---------|-----------|--------|
| `act_567892422940728` (primair, Sempertex) | ✅ Ja | 5 | 0 (alle PAUSED) |
| `act_1489853856181844` (overig, toegestaan) | ✅ Ja | 0 | 0 |
| `act_607231713057715` (genoemd in command) | ❌ Geen toegang | n.v.t. | n.v.t. |

> **Let op:** de API-token heeft geen toegang tot `act_607231713057715`. Toegestane accounts volgens de token: `act_1489853856181844` en `act_567892422940728`. Als er wél op `act_607231713057715` gedraaid moet worden, moet de Pipeboard-connectie opnieuw geautoriseerd worden op https://pipeboard.co/connections.

---

## Campagnes op primair account (`act_567892422940728`)

Alle 5 campagnes staan op **PAUSED**:

| Campagne | ID | Objective | Status | Dagbudget | Laatst gewijzigd |
|----------|-----|-----------|--------|-----------|------------------|
| 2026: SYBB - Kopie | 120243293329420239 | OUTCOME_SALES | PAUSED | — | 20 apr 2026 |
| 2026: SYBB | 120239435987290239 | OUTCOME_SALES | PAUSED | €100,00 | 19 apr 2026 |
| Last push Nozzle Up | 120233295855990239 | OUTCOME_SALES | PAUSED | — | 21 sep 2025 |
| Nozzle Up END OF AUGUST | 120232324822740239 | OUTCOME_SALES | PAUSED | €70,00 | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | OUTCOME_SALES | PAUSED | €30,00 | 15 sep 2025 |

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads. ✅

## ⚠️ Waarschuwingen

Geen — geen actieve ads om te beoordelen op creative fatigue, CPM of dalende Link CTR.

## 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

## 💡 Voorstellen (wacht op goedkeuring)

Er zijn geen data-gedreven optimalisatievoorstellen omdat er geen live performance-data is.

Wel drie aandachtspunten voor Robin (organisatorisch, geen ad-acties):

1. **SYBB-campagne staat uit.** De hoofdcampagne `2026: SYBB` (dagbudget €100,00) is sinds 19 april 2026 gepauzeerd. Als SYBB weer live moet, moet deze campagne handmatig geactiveerd worden — daarna kan deze auto-optimize weer echt werk doen.
2. **Dubbele campagne.** `2026: SYBB - Kopie` (aangemaakt 19 april) lijkt een kopie. Overweeg op te ruimen om verwarring te voorkomen bij een herstart.
3. **Account-toegang.** Als er advertenties op `act_607231713057715` verwacht worden, is de token-toegang daar het probleem, niet de campagnes. Opnieuw autoriseren via Pipeboard.

---

**Er zijn geen voorstellen om goed te keuren.** Zodra de SYBB-campagne (of een andere campagne) weer op ACTIVE staat en minimaal 24 uur draait, geeft een volgende run van `/ads-auto-optimize` weer echte kill-rule- en budget-analyses.
