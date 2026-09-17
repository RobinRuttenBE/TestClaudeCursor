# Morning Report — 2026-09-17

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Het rapport staat in `Output/Reports/Daily/2026-09-17_ads_report.md`, gecommit en gepusht (22832628). Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 17 september 2026

**Meta was vandaag niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie en de directe route zat op de eerste call al op de weeklimiet (30 van 30, reset 21 september). De Meta-cijfers komen daarom uit het live extract van gisteren 09:03. PostHog (directe REST-route) bevestigde dat het 30d-venster van vandaag exact dezelfde levering bevat: nul betaalde sessies tussen 14 en 20 augustus en nul sinds 10 september. De cijfers zijn dus ongewijzigd geldig.

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Veertiende dag zonder levering. Gisteren kwamen 9 organische pageviews op de distributeurspagina, geen formulierstarts, geen inzendingen.

**Overzicht per campagne (last 30d)**

| Campagne | Spend | Impr. | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 90.888 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 |
| Wholesaler (SWE) | €507,24 | 39.267 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 |
| **Totaal** | **€1.069,38** | 130.155 | 2,2% | €0,37 | €8,22 | | 19 | 35 (incl. 11 zonder UTM) |

ROAS niet van toepassing, het zijn lead-campagnes. All-in kosten per inzending: €30,55.

**Underperformers**

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar 0,7% conversie en €63,63 per inzending. Nieuwe hook testen.
- **Video 2 (LIT)** en **Statisch 1 (LIT)** raken een CPC- of CTR-drempel maar converteren het best. Behouden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 2 (SWE) €32,03

**Funnel /become-a-distributor (30d):** 1.751 pageviews, 134 formulierstarts, 21 fouten, 33 inzendingen. Slechts 24,6% van de starters komt door. Dat lek eerst dichten vóór herstart.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. De zes voorstellen van 3 en 16 september wachten nog op jouw goedkeuring.

**Operationeel:** tot maandag 21 september draaien alle Meta-rapporten op het extract van 16 september. Voorstel 6 (één gedeeld Meta-extract per dag cachen voor de drie rapporten) blijft urgent, anders is de limiet elke week vanaf woensdag vol.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.

---

API Error: Your computer went to sleep mid-response. The response above may be incomplete.
API Error: Your computer went to sleep mid-response. The response above may be incomplete.

---

Rapport staat in `Output/Reports/Daily/2026-09-17_auto_optimize.md`, gecommit en gepusht (ec7aa520). Alleen Pipeboard (directe JSON-RPC route, 1 call) en PostHog (directe REST-route, 2 queries) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september. Er zijn 0 actieve ads, dus de kill-regels hadden niets om op te draaien. Geen `update_ad` calls gedaan.

**Meta was niet live bereikbaar.** De Pipeboard MCP vraagt autorisatie, en de directe route zat op de eerste call al op de weeklimiet (30 van 30, reset 21 september). De campagnestatus komt uit het live extract van gisteren 09:03.

**PostHog bevestigt de stilstand live.** Nul sessies met een Meta-UTM sinds 10 september, nul formulierstarts, nul inzendingen. Gisteren 9 organische pageviews op de distributeurspagina. Laatste betaalde inzending blijft 4 september, veertiende dag zonder levering.

**De zes voorstellen staan ongewijzigd en wachten op je goedkeuring:**

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE), twee op Video 2 (LIT), een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE audience verbreden, Statisch 1 (LIT) naar 25-65 zonder desktop.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking en funnel fix vóór herstart: Meta telt 19 leads tegenover 35 in PostHog, en 102 van 137 formulierstarters haken af.
6. Eén gedeeld Meta-extract per dag cachen voor de drie rapporten. Dit is de derde run vandaag die op de limiet stuit.

Eén observatie: de opgeslagen dagrapporten bevatten geen per-ad tabellen met link-metrics, dus de 70-20-10 indeling draait nu op campagne-cijfers van 6 september plus kosten per inzending per ad. Bij de volgende live ad-level call sla ik die tabel expliciet op.

Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
