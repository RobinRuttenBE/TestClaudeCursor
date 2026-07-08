# Auto-Optimize Rapport, 8 juli 2026

**Run:** /ads-auto-optimize (alleen Meta Ads MCP + PostHog MCP, geen Google MCPs)
**Periode:** laatste 3 dagen (last_3d)
**Metric-basis:** Link CTR en CPC (link), nooit all-clicks

---

## Samenvatting

**Geen actieve campagnes gevonden. Geen acties uitgevoerd, geen voorstellen mogelijk.**

Alle campagnes in het Sempertex Ad Account staan op PAUSED. Er zijn dus geen live ads die tegen de kill-regels of de 70-20-10 classificatie getoetst kunnen worden.

---

## Accountstatus

| Account | Status | Bevinding |
|---------|--------|-----------|
| `act_567892422940728` (Sempertex, primair) | Toegankelijk | 0 actieve campagnes. 5 campagnes totaal, allemaal PAUSED. |
| `act_1489853856181844` (toegankelijk via token) | Toegankelijk | 0 campagnes (leeg). |
| `act_607231713057715` (secundair uit command) | **Niet toegankelijk** | Token heeft geen toegang tot dit account. Toegestane accounts: `act_1489853856181844`, `act_567892422940728`. |

### Campagnes in `act_567892422940728` (allemaal PAUSED)

| Campagne | ID | Status | Daily budget | Laatst gewijzigd |
|----------|-----|--------|--------------|------------------|
| 2026: SYBB - Kopie | 120243293329420239 | PAUSED | n.v.t. | 20 apr 2026 |
| 2026: SYBB | 120239435987290239 | PAUSED | €100,00 | 19 apr 2026 |
| Last push Nozzle Up | 120233295855990239 | PAUSED | n.v.t. | 21 sep 2025 |
| Nozzle Up END OF AUGUST | 120232324822740239 | PAUSED | €70,00 | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | PAUSED | €30,00 | 15 sep 2025 |

---

## Automatische acties uitgevoerd

Geen ads gepauzeerd. Er zijn geen actieve ads, dus de kill-regels (Link CTR < 0,8% na >= 1.000 impressions, CPC (link) > €1,50 na >= 500 link clicks) zijn niet van toepassing.

## Waarschuwingen

Geen. Zonder live delivery is er geen data over frequency, CPM of Link CTR-trend om te beoordelen.

## 70-20-10 Classificatie

Niet van toepassing. Er zijn geen actieve ads om te classificeren of budget over te herverdelen.

## Voorstellen (Niveau 2)

Geen data-gedreven voorstellen mogelijk zonder live campagne.

---

## Aandachtspunten voor Robin

1. **De SYBB-campagne staat uit.** `2026: SYBB` (daily budget €100,00) is sinds 19 april 2026 gepauzeerd. Zolang deze op PAUSED staat levert /ads-auto-optimize en het dagelijkse SYBB-rapport geen performance-data. Als de campagne weer moet lopen, zet hem handmatig op ACTIVE, daarna kan deze run wel optimaliseren.
2. **Tweede account niet bereikbaar.** Het command verwijst naar `act_607231713057715`, maar de huidige API-token heeft daar geen toegang. Toegestane accounts zijn `act_1489853856181844` (leeg) en `act_567892422940728`. Controleer of dit het juiste account-ID is of dat de token-permissies uitgebreid moeten worden.

---

*Gegenereerd door /ads-auto-optimize. Databronnen: Meta Ads MCP (Pipeboard). Geen Google MCPs gebruikt, niet naar de Google Sheet geschreven.*
