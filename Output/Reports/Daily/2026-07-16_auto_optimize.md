# Auto-Optimize Rapport — 16 juli 2026

**Databronnen:** Meta Ads MCP (Pipeboard) — enkel. Geen Google MCPs gebruikt, niet naar de Google Sheet tracker geschreven (conform run-instructie). PostHog niet geraadpleegd: niet nodig, want er zijn geen actieve ads om tegen landingspagina-data te kruisen.
**Periode:** laatste 3 dagen (13–16 juli 2026)
**Ad accounts gecontroleerd:** `act_567892422940728` (primair), `act_1489853856181844` (tweede toegankelijke account).

---

## ⛔ Geen actieve campagnes — geen optimalisatie mogelijk

Er draaien op dit moment **geen actieve Meta Ads campagnes** in enig toegankelijk account. Daardoor zijn er geen actieve ads, geen impressions en geen link clicks over de afgelopen 3 dagen om tegen de drempelwaarden te toetsen.

### Statusoverzicht campagnes (`act_567892422940728`)

| Campagne | Status | Dagbudget | Laatst gewijzigd |
|----------|--------|-----------|------------------|
| 2026: SYBB | PAUSED | €100,00 | 19 apr 2026 |
| 2026: SYBB - Kopie | PAUSED | n.v.t. | 20 apr 2026 |
| Last push Nozzle Up | PAUSED | n.v.t. | 21 sep 2025 |
| Nozzle Up END OF AUGUST | PAUSED | €70,00 | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | PAUSED | €30,00 | 15 sep 2025 |

**Actieve campagnes: 0**

Het tweede toegankelijke account (`act_1489853856181844`) bevat eveneens geen actieve campagnes. Het in het command genoemde account `act_607231713057715` is niet toegankelijk met het huidige API-token (toegestaan zijn uitsluitend `act_567892422940728` en `act_1489853856181844`).

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd — er zijn geen actieve ads om te beoordelen. ✅

**Totaal gepauzeerd: 0 ads**

## ⚠️ Waarschuwingen

Geen — geen actieve ads, dus geen creative fatigue, dure reach of dalende Link CTR te melden.

## 📊 70-20-10 Classificatie

Niet van toepassing: geen actieve ads om te classificeren of budget over te verdelen.

## 💡 Voorstellen (wacht op goedkeuring)

De enige actie die hier zin heeft ligt op een niveau boven de kill-/budgetregels: **er staat niets aan.**

1. **Bevestig of dit bedoeld is.** De `2026: SYBB` campagne (dagbudget €100,00) staat sinds 19 april 2026 op PAUSED. Als SYBB weer live hoort te zijn, moet de campagne handmatig geactiveerd worden voordat dit command iets kan optimaliseren. Dit sluit aan bij het SYBB dagrapport van 15 juli 2026 ("campaign paused, no PostHog").
2. **Zolang alles gepauzeerd blijft** levert `/ads-auto-optimize` elke dag een leeg rapport op. Overweeg het dagelijkse auto-optimize deel van de morning-report flow te pauzeren tot er weer een campagne live is, om ruis te voorkomen.

*Geen niveau-2 acties uitgevoerd — er is niets om te herverdelen of te schalen.*

---

**Er zijn geen actieve campagnes. Wil je dat ik de `2026: SYBB` campagne activeer, of blijft alles bewust gepauzeerd?**
