# Auto-Optimize Rapport — 11 July 2026

**Databron:** Meta Ads MCP (Pipeboard) — uitsluitend. Geen Google MCPs aangeroepen, niet naar de Meta Ads Tracker Google Sheet geschreven.
**Periode:** laatste 3 dagen (`last_3d`)
**Metrics:** alle kill-regels op Link CTR en CPC (link), conform command-definities.

---

## Samenvatting

**Er zijn momenteel GEEN actieve Meta Ads campagnes. Er is niets om te optimaliseren.**

Alle campagnes in de toegankelijke ad accounts staan op PAUSED. Zonder actieve ads kunnen de kill-regels (Niveau 1) niet triggeren en zijn er geen ads om te classificeren (70-20-10) of voorstellen (Niveau 2) voor te doen.

---

## Accounts gecontroleerd

| Account | Status | Bevinding |
|---------|--------|-----------|
| `act_567892422940728` (Sempertex — primair) | ✅ Toegankelijk | 0 actieve campagnes. Alle 5 campagnes PAUSED. |
| `act_1489853856181844` | ✅ Toegankelijk | 0 actieve campagnes. |
| `act_607231713057715` | ❌ Geen toegang | API-token heeft geen toegang tot dit account. Toegestane accounts: `act_1489853856181844`, `act_567892422940728`. |

> **Let op:** het command noemt `act_607231713057715` als te controleren account, maar de huidige Pipeboard-token heeft daar geen toegang toe. Als dit account actieve campagnes bevat, kan dit rapport die niet zien. Controleer de Pipeboard-connectie/permissies als hier wel campagnes verwacht worden.

## Campagne-status primair account (`act_567892422940728`)

| Campagne | Objective | Status | Daily budget | Laatst gewijzigd |
|----------|-----------|--------|--------------|------------------|
| 2026: SYBB - Kopie | OUTCOME_SALES | PAUSED | — | 20 Apr 2026 |
| 2026: SYBB | OUTCOME_SALES | PAUSED | €100.00 | 19 Apr 2026 |
| Last push Nozzle Up | OUTCOME_SALES | PAUSED | — | 21 Sep 2025 |
| Nozzle Up END OF AUGUST | OUTCOME_SALES | PAUSED | €70.00 | 15 Sep 2025 |
| Campagne Nozzle Up 2025 1 | OUTCOME_SALES | PAUSED | €30.00 | 15 Sep 2025 |

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads om te evalueren. ✅

**Totaal gepauzeerd: 0 ads**

## ⚠️ Waarschuwingen

Geen — geen actieve ads om creative fatigue, CPM of dalende Link CTR op te meten.

## 📊 70-20-10 Classificatie

Niet van toepassing — geen actieve ads om te classificeren.

**Budget mismatch:** N.v.t.

## 💡 Voorstellen (wacht op goedkeuring)

Geen data-gedreven voorstellen mogelijk zonder actieve ads.

**Enige actiepunt (organisatorisch, geen ad-optimalisatie):**
- De hoofdcampagne "2026: SYBB" staat sinds 19 Apr 2026 op PAUSED. Als de SYBB-campagne weer moet lopen, moet die eerst handmatig geactiveerd worden voordat dit command zinvolle optimalisaties kan uitvoeren. Dit is een strategische keuze voor Robin, geen automatische actie.

---

**Geen voorstellen om goed te keuren. Zodra er campagnes actief staan (en/of de Pipeboard-token toegang krijgt tot `act_607231713057715`), draai dit command opnieuw voor een volledige analyse.**
