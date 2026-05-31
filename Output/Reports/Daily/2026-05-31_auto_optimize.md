# Auto-Optimize Rapport — 31 May 2026

> Run-modus: alleen Meta Ads MCP (Pipeboard) en PostHog MCP. Geen Google MCPs aangeroepen. Output uitsluitend lokaal opgeslagen.

## Samenvatting

**Geen actieve campagnes gevonden. Geen optimalisaties uitgevoerd of voorgesteld.**

Alle campagnes in de toegankelijke ad accounts staan op PAUSED. Er zijn dus geen actieve ads om tegen de kill-regels te toetsen, te classificeren volgens 70-20-10, of budget voor te herverdelen. Dit komt overeen met de bekende status: de campagne `2026: SYBB` is gepauzeerd (zie ook recente rapporten met 0 pageviews).

---

## Data-bronnen gecontroleerd

| Ad Account | Status | Resultaat |
|---|---|---|
| `act_567892422940728` (primair, Sempertex) | Toegankelijk | 5 campagnes, **allemaal PAUSED** |
| `act_1489853856181844` | Toegankelijk | **0 campagnes** |
| `act_607231713057715` (genoemd in command) | **Geen toegang** | Token weigert: allowed accounts zijn `act_1489853856181844` en `act_567892422940728` |

> ⚠️ Het in de command genoemde account `act_607231713057715` is niet bereikbaar met de huidige Pipeboard-token. Als hier wél actieve campagnes draaien, kunnen die in deze run niet geanalyseerd worden. Controleer de token-permissies of het account-ID.

### Campagnes in `act_567892422940728` (alle PAUSED)

| Campagne | Objective | Status | Daily budget | Laatst gewijzigd |
|---|---|---|---|---|
| 2026: SYBB - Kopie | OUTCOME_SALES | PAUSED | — | 20 Apr 2026 |
| 2026: SYBB | OUTCOME_SALES | PAUSED | €100.00 | 19 Apr 2026 |
| Last push Nozzle Up | OUTCOME_SALES | PAUSED | — | 21 Sep 2025 |
| Nozzle Up END OF AUGUST | OUTCOME_SALES | PAUSED | €70.00 | 15 Sep 2025 |
| Campagne Nozzle Up 2025 1 | OUTCOME_SALES | PAUSED | €30.00 | 15 Sep 2025 |

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads. ✅

(Kill-regels Link CTR < 0.8% en CPC (link) > €1.50 zijn niet van toepassing zonder actieve, leverende ads.)

## ⚠️ Waarschuwingen

Geen — geen actieve ads om op creative fatigue, CPM of dalende Link CTR te beoordelen.

## 📊 70-20-10 Classificatie

Niet van toepassing. Geen actieve ads om te classificeren.

## 💡 Voorstellen (wacht op goedkeuring)

Geen optimalisatie-voorstellen op ad-niveau, omdat er geen live performance-data is.

Wel twee aandachtspunten voor Robin:

1. **Campagne staat uit.** Als de bedoeling is dat `2026: SYBB` weer draait, moet die eerst geactiveerd worden voordat dit command zinvolle optimalisaties kan doen. Wil je dat ik de campagne-status nakijk en een herstart voorbereid?
2. **Token-toegang tot `act_607231713057715`.** Dit account staat in de command maar is niet toegankelijk. Verifieer of dit het juiste account-ID is, of dat de Pipeboard-token uitgebreid moet worden.

---

**Conclusie:** niets te optimaliseren vandaag. Reactiveer een campagne of corrigeer de account-toegang en draai dit command opnieuw.
