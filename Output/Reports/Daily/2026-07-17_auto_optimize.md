# Auto-Optimize Rapport — 17 juli 2026

**Run:** automatische Meta Ads optimalisatie (last_3d venster)
**Databronnen:** Meta Ads MCP (Pipeboard). PostHog niet nodig (geen actieve ads).
**Accounts gecontroleerd:**
- `act_567892422940728` (Sempertex, primair)
- `act_1489853856181844` (tweede toegankelijke account onder dit token)
- `act_607231713057715` (gevraagd, maar GEEN toegang met dit API token — overgeslagen)

---

## Samenvatting

**Er zijn geen actieve campagnes of ads. Er is niets geoptimaliseerd en niets gepauzeerd.**

Alle campagnes in het primaire account staan op PAUSED, inclusief de hoofdcampagne `2026: SYBB`. Het tweede toegankelijke account (`act_1489853856181844`) bevat geen actieve campagnes. In de afgelopen 3 dagen is er nul spend en nul impressions geregistreerd. Dit sluit aan bij de laatste dagrapportage van 16 juli 2026 ("campaign paused").

De kill-regels (Link CTR en CPC link) en de 70-20-10 classificatie zijn daarom niet van toepassing: er is geen live performance data om tegen de drempelwaarden te toetsen.

---

## ⚡ Automatische acties uitgevoerd

Geen ads gepauzeerd. Er waren geen actieve ads om te beoordelen. ✅

**Totaal gepauzeerd: 0 ads**

---

## ⚠️ Waarschuwingen

Geen creative fatigue, dure reach of dalende Link CTR om te melden. Geen actieve ads = geen signalen.

Wel één operationele waarschuwing:

| Onderwerp | Signaal | Actie aanbevolen |
|-----------|---------|------------------|
| Account toegang | `act_607231713057715` niet toegankelijk met huidig token (toegestaan: `act_1489853856181844`, `act_567892422940728`) | Controleer of dit account nog relevant is; werk het command bij of herstel token-permissies |

---

## 📊 70-20-10 Classificatie

Niet van toepassing. Er zijn geen actieve ads om te classificeren.

**Budget mismatch:** Nee (geen actief budget in omloop).

---

## 📁 Campagne status (primair account `act_567892422940728`)

| Campagne | Status | Objective | Dagbudget | Laatst gewijzigd |
|----------|--------|-----------|-----------|------------------|
| 2026: SYBB | PAUSED | OUTCOME_SALES | €100.00 | 19 apr 2026 |
| 2026: SYBB - Kopie | PAUSED | OUTCOME_SALES | n.v.t. | 20 apr 2026 |
| Last push Nozzle Up | PAUSED | OUTCOME_SALES | n.v.t. | 21 sep 2025 |
| Nozzle Up END OF AUGUST | PAUSED | OUTCOME_SALES | €70.00 | 15 sep 2025 |
| Campagne Nozzle Up 2025 1 | PAUSED | OUTCOME_SALES | €30.00 | 15 sep 2025 |

Last_3d insights op campagne `2026: SYBB` en op accountniveau: leeg (0 spend, 0 impressions).

---

## 💡 Voorstellen (wacht op goedkeuring)

Er zijn geen data-gedreven budget-, variatie- of audience-voorstellen mogelijk zonder actieve ads.

Enige actie-aanbeveling voor Robin:

**1. SYBB campagne herstarten**
- De hoofdcampagne `2026: SYBB` staat sinds 19 april 2026 op PAUSED. Zolang deze uit staat levert `/ads-auto-optimize` geen optimalisatiewaarde.
- Beslis of SYBB weer live moet. Zo ja: heractiveer de campagne, dan pakt de volgende run de performance-analyse en kill-regels op.
- Zo nee: overweeg deze dagelijkse auto-optimize run tijdelijk te pauzeren tot er weer een actieve campagne draait.

---

**Er staan geen actieve ads, dus er is geen actie of goedkeuring nodig. Wil je de SYBB campagne heractiveren zodat de optimalisatie weer kan draaien?**
