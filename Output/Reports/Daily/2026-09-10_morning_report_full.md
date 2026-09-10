# Morning Report — 2026-09-10

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport staat in `Output/Reports/Daily/2026-09-10_ads_report.md`, gecommit en gepusht (1401a695). Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 10 september 2026

**Databronnen.** De Pipeboard MCP vroeg om authenticatie en de PostHog MCP gaf HTTP 405. Beide werkten via de directe route met de geconfigureerde tokens, dus dit zijn echte 30-daagse cijfers (11 augustus t/m 9 september).

**Geen actieve campagnes.** Alle zeven campagnes staan op pauze. De Wholesaler campagnes (SWE en LIT) zijn sinds 4 september uit. Meta registreert €0,00 spend van 5 t/m 9 september. Ten opzichte van gisteren is er niets veranderd behalve het venster dat één dag opschoof.

**Overzicht per campagne (last 30d)**

| Campagne | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 |

Totaal €1.069,38 spend, 1.410 betaalde sessies, 24 geattribueerde inzendingen plus 9 zonder UTM. Meta telde 277 landing page views tegenover 1.410 PostHog-sessies, dus kosten per inzending zijn op PostHog gebaseerd. ROAS is niet van toepassing bij lead-campagnes.

**Underperformers**
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27 en 0 inzendingen op 113 sessies. Niet herstarten.
- **Video 2 (SWE)**: CPC €0,69, CPM €17,07, €63,50 per inzending. Niet herstarten.
- **Video 2 (LIT)**: CPC €0,58 boven drempel, maar beste kosten per inzending (€28,75) en beste conversie (3,5%). Behouden.
- **Wholesaler (LIT)**: frequency 3,97. Bij herstart een nieuwe creative toevoegen.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20), maar 292 sessies leveren maar 2 inzendingen op. Budget verlagen.

**Top performers**
- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38

**Restverkeer.** Sinds de pauze zag PostHog 3 tot 5 sessies per dag op de distributeurpagina, waarvan 5 in totaal met ad-UTM. Die passen bij opgeslagen of gedeelde posts, niet bij levering. Laatste inzending: 4 september.

**Aanbeveling (70-20-10):** bij herstart 70% naar de bewezen LIT-set (Video 1, Video 2, Statisch 1), 20% naar Statisch 2 (SWE), 10% naar één nieuwe creative per markt. Beide SWE-video's niet herstarten. De vijf herstart-voorstellen van 3 september wachten nog op je goedkeuring.

**Wil je funnel data toevoegen?** Gesprekken gepland, distributeurs actief en eerste orders zitten niet in Meta of PostHog. Lever die aan en ik draai de volledige funnel-diagnose.

---

SYBB rapport niet beschikbaar.

---

Rapport staat in `Output/Reports/Daily/2026-09-10_auto_optimize.md`, gecommit en gepusht (be9ce493). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST route) gebruikt, beide MCPs zelf weigerden. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de Wholesaler campagnes sinds 4 september. Meta geeft over 7 t/m 9 september 0 rijen op ad- en campagneniveau, dus 0 impressions, 0 link clicks en €0,00 spend. Geen ads gepauzeerd, geen `update_ad` calls.

**PostHog bevestigt de stilstand.** 0 betaalde sessies sitewide sinds 5 september. De distributeurspagina kreeg 1 tot 5 organische bezoekers per dag. Laatste inzending blijft 4 september, 33 in totaal sinds 25 augustus.

**Zevende dag op rij zonder levering.** Niets veranderd ten opzichte van gisteren. De vijf voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT).
3. LIT ad sets samenvoegen, SWE audience verbreden.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking fix vóór herstart, Meta telt 19 leads tegenover 33 in PostHog.

Zolang er niets herstart is, blijft elke dagelijkse run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
