# Morning Report — 2026-05-18

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,37%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,10** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 69,22** over 2 actieve dagen (niet totaal/30)
> - Bron: spend EUR 138,45 · impressions 9.210 · link_clicks 126
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H11, B3, CTA5 | EUR 85,09 | 5.715 | 73 | 1,28% | EUR 1,17 |
> | H13,B3,CTA5 | EUR 36,85 | 2.475 | 33 | 1,33% | EUR 1,12 |
> | H12,B3,CTA5 | EUR 16,51 | 1.020 | 20 | 1,96% | EUR 0,83 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 18 May 2026

⚠️ **Geen actieve campagnes** in beide accounts. AmbitionAvenue is leeg (€0). Hieronder de laatste lifetime performance van de 5 meest recente gepauzeerde campagnes uit het Sempertex Ad Account.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

**Totaal spend:** €4.867,46

### Underperformers
- **2026: SYBB - Kopie**: CPC €0,64 én CPM €16,34, 0 conversies. Schrappen of herbouwen.
- **Nozzle Up END OF AUGUST**: CTR 0,99%. Goedkope reach, zwakke hook, vervang de hook bij heractivatie.
- **Ad "SYBB w/ Semp (BLACK)"**: CPC €0,61, CTR 1,0%, 0 conversies. Zwakste SYBB creative.

Geen frequency-overschrijdingen (max 3,37).

### Top performers
- **Beste CTR**: ad H13,B3,CTA5 (2026: SYBB) — 9,8%
- **Laagste CPC**: ad H13,B3,CTA5 (2026: SYBB) — €0,07
- **Beste ROAS**: 2026: SYBB — 17,8x (vertekend door één grote wholesale order; structureel solide is Nozzle Up 2025 1 op 8,3x)

### Aanbeveling (70-20-10)
70% budget op de bewezen SYBB-winnaars (hooks H13 + H15, B3, CTA5: 4 tot 10% CTR, €0,07 tot €0,15 CPC), 20% op variaties, 10% experimenten. "Kopie" en "BLACK" niet heractiveren. Focus de volgende live-gang op de SYBB hook-winnaars, één campagne perfect.

**Google Sheet:** overgeslagen per run-regel. Rapport opgeslagen in `Output/Reports/Daily/2026-05-18_ads_report.md` (gecommit + gepusht).

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Met die data draai ik automatisch een `/funnel-diagnose` en voeg ik de volledige funnel-analyse (tabel, #1 bottleneck, 3 actiepunten, SYBB-vergelijking) toe aan het rapport.

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-05-17_sybb_report.md` en is gecommit + gepusht.

## Kernbevindingen

**Meta Ads (Pipeboard MCP):** De campagne **2026: SYBB** (`120239435987290239`) staat sinds 19 april op **PAUSED**. Nul spend, impressies en clicks, niet alleen op 17 mei maar de hele week (10 t/m 17 mei). Er is dus geen paid ad-data om te analyseren.

**PostHog (`www.startyourballoonbusiness.com`):**
- 17 mei: 7 pageviews, 6 unieke bezoekers, 5 sessies, allemaal single pageview
- Bounce rate 100% (7d gemiddelde ~86%)
- Verkeer kwam van Instagram/Facebook bio links (`utm_content=bio_link`) en direct, niet van ad-varianten
- 1 van 7 pageviews bereikte `/booking`

**Twee belangrijke datagaten, eerlijk gerapporteerd in plaats van ingevuld:**
1. De SYBB Meta-campagne ligt al 8 dagen stil terwijl het dagrapport erop is ingericht, een strategische beslissing nodig.
2. Scroll depth en CTA clicks worden niet getrackt in PostHog, dus 5 van de 7 landing-page-KPI's en de funnel zijn onmeetbaar. Die staan in het rapport als "niet getrackt" (⚪), niet als verzonnen cijfers.

De strikte regel is gevolgd: alleen Pipeboard Meta Ads MCP en PostHog MCP gebruikt, geen Google MCPs, geen schrijfactie naar de Tracker-sheet, output enkel als lokale markdown.

---

Klaar. Hier is de uitkomst van `/ads-auto-optimize` voor 18 May 2026:

## Geen actieve campagnes — geen optimalisatie mogelijk

De flow kon niet draaien zoals bedoeld, want **er staat geen enkele Meta Ads campagne live**:

| Account | Resultaat |
|---------|-----------|
| `act_567892422940728` (primair) | 5 campagnes, **allemaal PAUSED** |
| `act_1489853856181844` | Geen campagnes |
| `act_607231713057715` | Token heeft geen toegang |

De hoofdcampagne **`2026: SYBB`** (dagbudget €100,00, ID 120239435987290239) staat sinds 2026-04-19 op pauze. Alle Nozzle Up campagnes zijn al sinds september 2025 inactief.

**Niveau 1 (automatisch):** geen ads gepauzeerd, er zijn geen actieve ads om tegen de kill-regels te toetsen.
**Niveau 2 (voorstellen):** geen, zonder live data is elke classificatie of budget-aanbeveling speculatief.

PostHog is niet bevraagd: zonder ad-traffic is er niets te cross-referencen. Geen Google MCPs gebruikt, geen Google Sheet beschreven, conform de strikte regel.

Rapport opgeslagen in `Output/Reports/Daily/2026-05-18_auto_optimize.md` en gecommit + gepusht naar `main`.

## Beslissing nodig

Wil je dat ik de campagne **`2026: SYBB`** weer activeer? Dat is een Niveau 2 actie, dus ik voer het niet zonder jouw expliciete akkoord uit. Pas met minstens één actieve campagne heeft deze dagelijkse auto-optimalisatie zin.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 85,09 | 73 | 0 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 16,51 | 20 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 36,85 | 33 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 138,45** | **126** | **0** | **0** | **EUR 0,00** | **-** | **-** |

> Wix orders: 0 orders in periode. Update `data/wix-orders.json` met orders uit Wix admin.

> **ONGEMATCHTE /thank-you SESSIES:**
> - Sessie op 2026-04-26, utm_content=(geen utm_content)
> - Sessie op 2026-04-18, utm_content=(geen utm_content)

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

> Geen van de ads heeft verified Wix orders in de periode. GEEN budget herverdeling op basis van verified funnel mogelijk. Wacht op meer data — negeer Meta pixel 'best performer' claims tot die tijd.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
