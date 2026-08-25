# Auto-Optimize Rapport, 25 augustus 2026

**Run:** 2026-08-25, automatische run via /ads-auto-optimize
**Periode:** laatste 3 dagen (22 t/m 24 augustus 2026)
**Data bronnen:** Meta Ads (Pipeboard, directe JSON-RPC calls). Geen Google services gebruikt, conform run-instructie.
**Account:** act_567892422940728 (Sempertex Ad Account)

## Samenvatting

Er draaien op dit moment geen actieve Meta Ads campagnes. Alle 5 campagnes in het Sempertex account staan op PAUSED en het account had nul delivery (geen spend, geen impressions) in de afgelopen 3 dagen. Er waren daardoor geen kill-regels te toetsen, geen automatische acties uit te voeren, en geen 70-20-10 classificatie of budgetvoorstellen te maken.

## Accountstatus

| Campagne | Status | Dagbudget | Laatst gewijzigd |
|----------|--------|-----------|------------------|
| 2026: SYBB - Kopie | PAUSED | (geen, ABO) | 2026-04-20 |
| 2026: SYBB | PAUSED | EUR 100,00 | 2026-04-19 |
| Last push Nozzle Up | PAUSED | (geen, ABO) | 2025-09-21 |
| Nozzle Up END OF AUGUST | PAUSED | EUR 70,00 | 2025-09-15 |
| Campagne Nozzle Up 2025 1 | PAUSED | EUR 30,00 | 2025-09-15 |

Account-level insights over de laatste 3 dagen: lege dataset, dus EUR 0,00 spend en 0 impressions.

**Overige accounts:**
- act_607231713057715 (genoemd in het command): bestaat niet of geen toegang. De token heeft alleen toegang tot act_567892422940728 en act_1489853856181844. Advies: verwijder dit account uit het /ads-auto-optimize command.
- act_1489853856181844 (AmbitionAvenue): bevat geen campagnes.

## Automatische acties uitgevoerd

Geen. Er zijn geen actieve ads om tegen de kill-regels (Link CTR < 0.8% bij 1.000+ impressions, CPC link > EUR 1,50 bij 500+ link clicks) te toetsen.

**Totaal gepauzeerd: 0 ads**

## Waarschuwingen

Geen ad-level waarschuwingen. Wel een structureel signaal: dit is minimaal de tweede opeenvolgende dag zonder ad delivery (het SYBB rapport van 2026-08-24 meldde ook al geen delivery). Zolang alle campagnes gepauseerd zijn, levert de dagelijkse auto-optimize run geen actiepunten op.

## 70-20-10 Classificatie

Niet van toepassing, geen actieve ads.

## Voorstellen (wacht op goedkeuring)

Geen budget-, variatie- of audiencevoorstellen mogelijk zonder actieve delivery. Enige beslispunt voor Robin:

1. **Campagnes herstarten of niet.** Als SYBB weer moet draaien, geef aan welke campagne (2026: SYBB of de Kopie-variant) geactiveerd moet worden en met welk dagbudget. Zonder die beslissing blijft deze run dagelijks leeg.
2. **Command opschonen.** act_607231713057715 uit het /ads-auto-optimize command verwijderen, want de token heeft er geen toegang toe en volgens eerdere runs bestaat het account niet.

---
*Log: 0 automatische acties uitgevoerd. Geen Google Sheet writes, lokaal rapport only.*
