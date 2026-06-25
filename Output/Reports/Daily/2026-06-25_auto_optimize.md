# Auto-Optimize Rapport — 25 juni 2026

**Run:** `/ads-auto-optimize` (automatische optimalisatie)
**Periode geanalyseerd:** laatste 3 dagen (last_3d)
**Databron:** Meta Ads MCP (Pipeboard). Geen Google MCPs, geen PostHog nodig (geen actieve ads).
**Primair account:** `act_567892422940728` (Sempertex)

---

## Samenvatting

**Geen actieve Meta Ads campagnes gevonden. Geen optimalisaties uitgevoerd of voorgesteld.**

Alle campagnes in het Sempertex account staan op `PAUSED`. Er is geen live ad-data over de afgelopen 3 dagen, dus er zijn geen kill-regels toegepast, geen waarschuwingen gegenereerd en geen 70-20-10 classificatie mogelijk.

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er draaien geen actieve ads. ✅

| Ad | Reden | Was | Nu | Performance |
|----|-------|-----|-----|-------------|
| — | — | — | — | Geen actieve ads |

**Totaal gepauzeerd: 0 ads**

---

## ⚠️ Waarschuwingen

Geen waarschuwingen — geen actieve creatives om op te beoordelen (frequency, CPM, Link CTR-daling).

---

## 📊 70-20-10 Classificatie

Niet van toepassing. Er zijn geen actieve ads om te classificeren in Core / Emerging / Experimental.

**Budget mismatch:** Nee — er staat geen budget live.

---

## 💡 Voorstellen (wacht op goedkeuring)

Geen data-gedreven voorstellen mogelijk zonder live performance. Wel een operationele observatie:

**1. Campagne-status**
- De campagne `2026: SYBB` (ID `120239435987290239`, dagbudget €100,00) staat sinds 19 april 2026 op `PAUSED`.
- Er is een kopie `2026: SYBB - Kopie` (ID `120243293329420239`), eveneens `PAUSED`, laatst bijgewerkt 20 april 2026.
- Zolang beide gepauzeerd blijven, levert `/ads-auto-optimize` geen optimalisatiewaarde op. Overweeg de campagne te heractiveren of de scheduled run tijdelijk uit te zetten.

---

## Status accounts en campagnes

### Account `act_567892422940728` (Sempertex — primair)
Geen actieve campagnes. Alle campagnes `PAUSED`:

| Campagne | ID | Status | Dagbudget | Laatst bijgewerkt |
|----------|-----|--------|-----------|-------------------|
| 2026: SYBB - Kopie | 120243293329420239 | PAUSED | — | 20 apr 2026 |
| 2026: SYBB | 120239435987290239 | PAUSED | €100,00 | 19 apr 2026 |
| Last push Nozzle Up | 120233295855990239 | PAUSED | — | 21 sep 2025 |
| Nozzle Up END OF AUGUST | 120232324822740239 | PAUSED | €70,00 | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | 120230372047970239 | PAUSED | €30,00 | 15 sep 2025 |

### Account `act_1489853856181844`
Toegankelijk met huidige token. Geen actieve campagnes.

### Account `act_607231713057715` (uit command genoemd)
**Niet toegankelijk** met de huidige API-token. Toegestane accounts voor deze token: `act_1489853856181844`, `act_567892422940728`. Dit account kon niet worden gecontroleerd. Als hier wel campagnes draaien, moet de token-toegang worden uitgebreid voordat `/ads-auto-optimize` dit account kan meenemen.

---

## Datakwaliteit & beperkingen
- Geen enkele ad voldeed aan de minimale dataverplichting (≥24u actief, ≥1.000 impressions / ≥500 link clicks), simpelweg omdat er niets actief draait.
- Kill-regels (Link CTR < 0,8% na ≥1.000 impressions; CPC (link) > €1,50 na ≥500 link clicks) zijn niet getriggerd — er was niets om tegen te toetsen.
- De link-metric berekeningen (Link CTR = `link_click / impressions`, CPC (link) = `spend / link_click`) konden niet worden uitgevoerd bij gebrek aan `actions`-data.

---

**Conclusie: niets te optimaliseren vandaag. Er draaien geen actieve Meta Ads campagnes.** Wil je dat ik `2026: SYBB` weer activeer, of de auto-optimize scheduled run pauzeer tot er weer campagnes live staan?
