# Auto-Optimize Rapport — 22 juni 2026

> Run-modus: handmatig via `/ads-auto-optimize`. Databronnen: uitsluitend Meta Ads MCP (Pipeboard). Geen Google MCPs aangeroepen, geen schrijfacties naar de Google Sheet tracker. Analyseperiode: laatste 3 dagen (19–22 juni 2026).

## Samenvatting

**Geen actieve ads om te optimaliseren.** Alle campagnes op beide toegankelijke ad accounts staan op PAUSED. Er was geen delivery (0 impressions, €0,00 spend) in de afgelopen 3 dagen. Er zijn dus geen kill-regels getriggerd en geen voorstellen te doen.

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads. ✅

**Totaal gepauzeerd: 0 ads**

---

## ⚠️ Waarschuwingen

Geen waarschuwingen. Zonder delivery is er geen creative fatigue, CPM- of Link CTR-signaal te meten.

---

## 📊 70-20-10 Classificatie

Niet van toepassing. Er zijn geen actieve ads om te classificeren.

**Budget mismatch:** Nee — er staat geen budget live.

---

## 💡 Voorstellen (wacht op goedkeuring)

Geen optimalisatie-voorstellen mogelijk zonder live data. Wel één operationeel aandachtspunt:

**1. Campagnestatus**
De hoofdcampagne **2026: SYBB** (`120239435987290239`, daily budget €100,00) staat sinds 19 april 2026 op PAUSED. Zolang deze niet live is, levert zowel `/ads-report` als `/ads-auto-optimize` lege rapporten op. Actie aan Robin: bevestig of SYBB bewust gepauzeerd blijft of weer geactiveerd moet worden. Pas daarna heeft auto-optimalisatie weer nut.

---

## Bekeken accounts & campagnes

### Account `act_567892422940728` (Sempertex — primair)
Alle campagnes PAUSED:

| Campagne | ID | Status | Daily budget |
|----------|-----|--------|--------------|
| 2026: SYBB - Kopie | 120243293329420239 | PAUSED | — |
| 2026: SYBB | 120239435987290239 | PAUSED | €100,00 |
| Last push Nozzle Up | 120233295855990239 | PAUSED | — |
| Nozzle Up END OF AUGUST | 120232324822740239 | PAUSED | €70,00 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | PAUSED | €30,00 |

- Actieve campagnes (`status_filter: ACTIVE`): **0**
- Delivery campagne 2026: SYBB (last_3d): **0 impressions, €0,00 spend**

### Account `act_607231713057715`
Niet toegankelijk met het huidige API-token. Toegestane accounts volgens Meta: `act_1489853856181844`, `act_567892422940728`.

### Account `act_1489853856181844`
- Actieve campagnes (`status_filter: ACTIVE`): **0**

---

## Definities gehanteerd (ter referentie)

| Metric | Formule |
|--------|---------|
| Link CTR | `actions.link_click / impressions × 100` (niet Meta's `ctr`) |
| CPC (link) | `spend / actions.link_click` (niet Meta's `cpc`) |

Kill-drempels (herzien 2026-04-13): Link CTR < 0,8% bij ≥ 1.000 impressions → pauzeren; CPC (link) > €1,50 bij ≥ 500 link clicks → pauzeren. Geen van beide kon getriggerd worden bij 0 delivery.

---

*Rapport gegenereerd: 22 juni 2026. Volgende run draait automatisch na het volgende `/ads-report`, of zodra SYBB weer live gaat.*
