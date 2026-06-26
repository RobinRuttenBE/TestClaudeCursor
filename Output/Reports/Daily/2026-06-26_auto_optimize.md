# Auto-Optimize Rapport — 26 juni 2026

> Run uitgevoerd via `/ads-auto-optimize`. Databron: uitsluitend Meta Ads MCP (Pipeboard). Geen Google MCPs aangeroepen, niet naar de tracker Google Sheet geschreven. Output enkel lokaal opgeslagen.

## Samenvatting

**Geen actieve campagnes gevonden. Geen optimalisaties uitgevoerd of mogelijk.**

Alle Meta Ads campagnes in de toegankelijke accounts staan op PAUSED. Er is dus geen live performance data over de afgelopen 3 dagen, geen ad die een kill-regel kan triggeren, en geen budget om te herverdelen. Dit sluit aan op het SYBB dagrapport van 25 juni 2026, waarin de SYBB campagne als gepauzeerd werd gemarkeerd.

## Account status

| Account | Toegang | Actieve campagnes | Opmerking |
|---------|---------|-------------------|-----------|
| `act_567892422940728` (primair) | ✅ Ja | 0 | Alle 5 campagnes staan PAUSED |
| `act_1489853856181844` | ✅ Ja | 0 | Geen actieve campagnes |
| `act_607231713057715` | ❌ Nee | n.v.t. | API token heeft geen toegang tot dit account |

> Let op: het in het command genoemde alternatieve account `act_607231713057715` is **niet** toegankelijk met de huidige API token. De token geeft toegang tot `act_567892422940728` en `act_1489853856181844`. Het tweede toegankelijke account is meegenomen in de check.

## Campagnes in primair account (`act_567892422940728`)

Alle campagnes staan op PAUSED. Geen enkele is actief:

| Campagne | Objective | Status | Dagbudget | Laatst gewijzigd |
|----------|-----------|--------|-----------|------------------|
| 2026: SYBB - Kopie | OUTCOME_SALES | PAUSED | n.v.t. | 20 apr 2026 |
| 2026: SYBB | OUTCOME_SALES | PAUSED | €100,00 | 19 apr 2026 |
| Last push Nozzle Up | OUTCOME_SALES | PAUSED | n.v.t. | 21 sep 2025 |
| Nozzle Up END OF AUGUST | OUTCOME_SALES | PAUSED | €70,00 | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | OUTCOME_SALES | PAUSED | €30,00 | 15 sep 2025 |

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads om tegen de kill-regels te toetsen. ✅

De kill-regels (Link CTR < 0,8% na ≥1.000 impressions; CPC (link) > €1,50 na ≥500 link clicks) zijn niet van toepassing zonder live delivery.

## ⚠️ Waarschuwingen

Geen waarschuwingen. Zonder actieve delivery is er geen creative fatigue, dure reach of dalende Link CTR te meten.

## 📊 70-20-10 Classificatie

Niet uitvoerbaar. Er zijn geen actieve ads om te classificeren in Core / Emerging / Experimental, en geen budget om te verdelen.

**Budget mismatch:** n.v.t.

## 💡 Voorstellen (wacht op goedkeuring)

Geen data-gedreven voorstellen mogelijk, omdat er geen live performance data is. Het enige zinvolle vervolg is een beslissing op campagne-niveau:

**1. Campagne heractiveren of bewust gepauzeerd laten**
- De hoofdcampagne **2026: SYBB** (dagbudget €100,00) staat sinds 19 apr 2026 op PAUSED.
- Actie vereist van Robin: wil je SYBB opnieuw activeren (dan kan deze auto-optimize flow vanaf de volgende run echt werk doen), of blijft de campagne bewust uit?
- Zolang alles gepauzeerd blijft, levert deze dagelijkse auto-optimize run niets op en kan hij worden overgeslagen.

---

**Er is op dit moment niets te optimaliseren omdat alle campagnes gepauzeerd zijn. Wil je de SYBB campagne opnieuw activeren? Geef het door, dan draait de optimalisatie bij de volgende run op echte data.**
