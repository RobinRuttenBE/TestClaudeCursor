# Morning Report — 2026-05-19

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,31%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,22** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 43,81** over 1 actieve dagen (niet totaal/30)
> - Bron: spend EUR 43,81 · impressions 2.756 · link_clicks 36
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H11, B3, CTA5 | EUR 17,52 | 1.118 | 18 | 1,61% | EUR 0,97 |
> | H13,B3,CTA5 | EUR 22,26 | 1.406 | 16 | 1,14% | EUR 1,39 |
> | H12,B3,CTA5 | EUR 4,03 | 232 | 2 | 0,86% | EUR 2,02 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 19 May 2026

> **Geen actieve campagnes** in beide accounts (Sempertex `act_567892422940728` en AmbitionAvenue `act_1489853856181844`). Hieronder de laatste lifetime performance van de meest recente gepauzeerde campagnes. De `last_30d` periode bevat geen spend.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|------|------|
| 2026: SYBB | Paused | €2.383,30 | 280.906 | 11.900 | 4,2% | €0,20 | €8,48 | 6 | 18,6x* |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

\* ROAS 2026: SYBB op basis van 6 purchases / €44.247 (gem. ±€7.374, B2B wholesale). Attributie verifiëren voor heractivatie.

### Underperformers
- **2026: SYBB - Kopie**, CPC €0,64 + CPM €16,34, 0 purchases. Niet heractiveren; gebruik de hoofdcampagne.
- **Last push Nozzle Up**, ROAS 0,8x (onder break-even). Hook is gezond, probleem zit in aanbod/conversie.
- **Nozzle Up END OF AUGUST**, CTR 1,0% (grensgeval), maar topefficiënt op CPM €1,64 en ROAS 6,4x. Hook aanscherpen.
- Geen frequency-flags (max 2,89).

### Top performers
- **Beste CTR:** 2026: SYBB, 4,2%
- **Laagste CPC:** Nozzle Up END OF AUGUST, €0,17
- **Beste ROAS:** 2026: SYBB, 18,6x (met caveat); betrouwbaarste zonder caveat: Campagne Nozzle Up 2025 1, 8,3x

### Samenvatting
- **Totaal spend:** €4.765,72 (lifetime, 5 gepauzeerde campagnes)
- **Beste:** 2026: SYBB (bewezen winnaar op engagement én ROAS)
- **Slechtste:** Last push Nozzle Up (ROAS < 1x) en SYBB - Kopie (duur, 0 conversie)
- **Aanbeveling (70-20-10):** 70% op heractivatie 2026: SYBB met bestaande creatives, 20% op de Nozzle Up structuur (6,4x–8,3x ROAS), 10% experiment. Stop "Kopie" en "Last push". Eerst de €44.247 purchase-attributie verifiëren.

### Google Sheet
Overgeslagen op verzoek. Opgeslagen in `Output/Reports/Daily/2026-05-19_ads_report.md` (gecommit en gepusht).

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` met alle beschikbare data en voeg de volledige diagnose toe aan dit rapport.

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-05-18_sybb_report.md`, gecommit en gepusht.

## Kernbevindingen voor 18 mei 2026

**Meta Ads (Pipeboard MCP):** De campagne **"2026: SYBB" staat op PAUSED**. Nul delivery op 18 mei en in het hele 7-daagse venster (€0 spend, 0 impressies, 0 clicks). Laatste activiteit was eenmalig op 19 april. Dit is de hoofdoorzaak van alle lage cijfers.

**PostHog (startyourballoonbusiness.com):**
- 4 pageviews, 3 unieke bezoekers, 3 sessies, allemaal via de organische `bio_link` (geen paid verkeer, consistent met de pauze)
- Avg sessieduur 121s, mediaan 59s
- Funnel: 3 landingspagina bezoekers → 0 naar /booking (100% drop-off, lage N)

## Twee aandachtspunten

1. **Funnel ligt stil** omdat de campagne gepauzeerd is. Beslissing nodig: heractiveren of bewust gepauzeerd laten (Robin goedkeuring).
2. **Datagat in tracking:** dit PostHog project legt alleen `$pageview`, `$dead_click` en `$rageclick` vast. Er zijn geen scroll-, pageleave- of CTA-click-events, dus **bounce rate, scroll depth en CTA click rate konden niet gerapporteerd worden**. Dit heb ik expliciet als datagat in het rapport gemarkeerd met een reparatie-aanbeveling, niet met verzonnen cijfers.

Conform de strikte regel zijn uitsluitend de Meta Ads MCP en PostHog MCP gebruikt; geen enkele Google MCP en niet naar de Tracker Sheet geschreven.

---

Klaar. Hier het resultaat van de auto-optimize run.

## Auto-Optimize Rapport, 19 May 2026

### ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd, want er zijn geen actieve campagnes of ads.**

Alle campagnes in het primaire account `act_567892422940728` staan op **PAUSED**, inclusief de SYBB campagne (gepauzeerd sinds 2026-04-19). De ACTIVE-filter gaf voor alle toegankelijke accounts een lege lijst terug.

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (primair) | Ja | 0 |
| `act_1489853856181844` | Ja | 0 |
| `act_607231713057715` | Geen toegang (token mist permissie) | n.v.t. |

Omdat er geen actieve ads zijn, konden de kill-regels (Link CTR < 0.8% en CPC (link) > €1.50) en de 70-20-10 classificatie niet toegepast worden. Geen waarschuwingen, geen budget-analyse mogelijk.

### 💡 Twee aandachtspunten (Niveau 2, wacht op goedkeuring)

1. **SYBB campagne staat uit.** "2026: SYBB" (daily budget €100,00) is sinds 2026-04-19 gepauzeerd. Bevestig of dit bewust is: zo ja, kan de dagelijkse auto-optimize tijdelijk stilliggen tot heractivatie; zo nee, heractiveer dan de campagne.
2. **Account `act_607231713057715` onbereikbaar** met de huidige Pipeboard token. Token-permissie herstellen als dit account ads moet draaien.

Het rapport is opgeslagen in `Output/Reports/Daily/2026-05-19_auto_optimize.md` en gecommit + gepusht naar GitHub. Alleen Meta Ads MCP gebruikt, geen Google services aangeroepen.

Wil je dat ik iets met punt 1 of 2 doe?

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 17,52 | 18 | 0 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 4,03 | 2 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 22,26 | 16 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 43,81** | **36** | **0** | **0** | **EUR 0,00** | **-** | **-** |

> Wix orders: 0 orders in periode. Update `data/wix-orders.json` met orders uit Wix admin.

> **ONGEMATCHTE /thank-you SESSIES:**
> - Sessie op 2026-04-26, utm_content=(geen utm_content)

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

> Geen van de ads heeft verified Wix orders in de periode. GEEN budget herverdeling op basis van verified funnel mogelijk. Wacht op meer data — negeer Meta pixel 'best performer' claims tot die tijd.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
