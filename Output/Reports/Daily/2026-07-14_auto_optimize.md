# Auto-Optimize Rapport — 14 juli 2026

**Databron:** Meta Ads MCP (Pipeboard) — uitsluitend. Geen Google MCPs aangeroepen, niet naar de Tracker Google Sheet geschreven.
**Analyseperiode:** laatste 3 dagen (last_3d)
**Primair account:** act_567892422940728

---

## ⛔ Geen optimalisatie uitgevoerd — geen actieve campagnes

Er draaien op dit moment **geen actieve Meta Ads campagnes** op de toegankelijke accounts. De kill-regels, waarschuwingsregels en 70-20-10 classificatie konden daarom niet worden toegepast: er is geen live ad-data over de afgelopen 3 dagen.

### Wat is gecontroleerd

| Account | Status token | Actieve campagnes | Bijzonderheden |
|---------|-------------|-------------------|----------------|
| `act_567892422940728` (Sempertex primair) | ✅ Toegang | **0 actief** | Alle 5 campagnes staan op PAUSED |
| `act_607231713057715` (uit command) | ❌ Geen toegang | n.v.t. | Token geeft geen toegang tot dit account |
| `act_1489853856181844` (extra toegankelijk) | ✅ Toegang | **0 actief** | Geen actieve campagnes |

### Campagnes op primair account (act_567892422940728) — allemaal PAUSED

| Campagne | Status | Laatst gewijzigd | Objective |
|----------|--------|------------------|-----------|
| 2026: SYBB | PAUSED | 2026-04-19 | OUTCOME_SALES |
| 2026: SYBB - Kopie | PAUSED | 2026-04-20 | OUTCOME_SALES |
| Last push Nozzle Up | PAUSED | 2025-09-21 | OUTCOME_SALES |
| Nozzle Up END OF AUGUST | PAUSED | 2025-09-15 | OUTCOME_SALES |
| Campagne Nozzle Up 2025 1 | PAUSED | 2025-09-15 | OUTCOME_SALES |

De hoofdcampagne `2026: SYBB` (dagbudget €100,00) staat sinds 19 april 2026 op PAUSED.

---

## ⚡ Automatische acties uitgevoerd

Geen. Er zijn geen actieve ads om tegen de kill-regels te toetsen.

- **Gepauzeerd wegens lage Link CTR (< 0,8%):** 0 ads
- **Gepauzeerd wegens hoge CPC (link) (> €1,50):** 0 ads
- **Totaal gepauzeerd:** 0 ads

## ⚠️ Waarschuwingen

Geen — geen actieve ads om op creative fatigue (freq > 3,5), dure reach (CPM > €15) of dalende Link CTR te controleren.

## 📊 70-20-10 Classificatie

Niet van toepassing. Zonder actieve ads en zonder impressiedata is classificatie in Core/Emerging/Experimental niet mogelijk.

## 💡 Voorstellen (wacht op goedkeuring)

Optimalisatie-voorstellen (budget, variaties, audiences) vereisen live performancedata. Die is er nu niet. In plaats daarvan twee aandachtspunten voor Robin:

**1. Account-toegang herstellen**
- Het account `act_607231713057715` dat in het `/ads-auto-optimize` command staat, is **niet toegankelijk** met de huidige Pipeboard/Meta-token.
- Toegankelijke accounts volgens het token: `act_567892422940728` en `act_1489853856181844`.
- Actie: controleer of `act_607231713057715` nog het juiste account-ID is, of koppel het juiste Facebook-login opnieuw via https://pipeboard.co/connections. Werk daarna het account-ID in het command bij.

**2. Campagne heractiveren indien SYBB weer moet lopen**
- Als SYBB weer traffic moet krijgen: heractiveer `2026: SYBB` (act_567892422940728, dagbudget €100,00). Dit is een Niveau 2 actie en gebeurt alleen op jouw expliciete goedkeuring.
- Zolang alles op PAUSED staat, heeft dit dagelijkse auto-optimize script geen werk en kan het overgeslagen worden tot er weer een campagne live is.

---

**Conclusie:** Geen actie nodig/mogelijk vandaag — 0 actieve campagnes op de toegankelijke accounts. Wil je dat ik `2026: SYBB` heractiveer of het toegangsprobleem op `act_607231713057715` verder uitzoek? Geef het aan.
