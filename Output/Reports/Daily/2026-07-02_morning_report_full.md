# Morning Report — 2026-07-02

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport gegenereerd en opgeslagen. Hier de samenvatting:

## Meta Ads Rapport — 2 juli 2026

⚠️ **Er draaien momenteel GEEN actieve campagnes.** Op geen enkel toegankelijk account (Sempertex `act_567892422940728` en `act_1489853856181844`) staat een campagne actief. Het Robin Rutten account (`act_607231713057715`) is niet benaderbaar met de huidige token. Hieronder de laatste performance van de recentste **gepauzeerde** campagnes.

### Overzicht per campagne (gesorteerd op spend)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |

### Top performers
- **Beste CTR & laagste CPC:** ad **H13,B3,CTA5** — 9,8% CTR bij €0,07 CPC. Duidelijke winnaar.
- **Beste ROAS:** 2026: SYBB — 17,8x (let op: 6 pixel-aankopen met hoge orderwaarde).

### Underperformers
- **H11,B3,CTA5 (v2)** — CPC €0,67 + CPM €13,51, hoogste spend (€521,56) van de campagne → herverdelen naar H13.
- **H13,B3,CTA5 (v2)** — CPC €0,63, presteert veel slechter dan het origineel → dupe uitzetten.
- **SYBB w/ Semp (BLACK)** — CTR 1,0% + CPC €0,61, laagste engagement → creatief vervangen.
- **2026: SYBB - Kopie** (campagne) — CPC €0,64 + CPM €16,34 bij 0 aankopen → opschonen.

### Aanbeveling (70-20-10)
Bij heractivatie: 70% budget achter de bewezen winnaar **H13,B3,CTA5**, 20% varianten in díe stijl (geen nieuwe BLACK-varianten), 10% experiment. Ruim de duplicaat-ads en de "Kopie"-campagne op.

**Google Sheet:** overgeslagen per instructie. Rapport opgeslagen in `Output/Reports/Daily/2026-07-02_ads_report.md`.

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4.
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Dan draai ik automatisch een `/funnel-diagnose` en voeg de volledige funnel-analyse toe aan het rapport.

---

Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-01_sybb_report.md`, gecommit en gepusht.

## Samenvatting van de run

**Meta Ads (Pipeboard MCP):** Campagne `2026: SYBB` (ID `120239435987290239`) staat op **PAUSED**. Campagne-, dag- én ad-level insights gaven allemaal lege datasets terug voor 1 juli én de hele week 25 juni–1 juli. Dus: nul spend, impressions en clicks. Er is geen ad-performance om te rapporteren.

**PostHog:** De **PostHog MCP was niet verbonden** in deze sessie — alleen de Pipeboard Meta Ads server was beschikbaar voor data. Conform je strikte instructie heb ik **geen** Google/GA4-bron als vervanging gebruikt. De Landing Page-secties zijn daarom leeg gemarkeerd (⚪ / "geen data").

**Twee rode vlaggen in het rapport:**
1. 🚩 Campagne staat uit → SYBB-funnel groeit al ≥7 dagen niet.
2. 🚩 PostHog MCP niet verbonden → landing page monitoring ligt stil.

**Top 3 acties:** (1) beslissen of `2026: SYBB` weer live moet, (2) PostHog MCP-verbinding herstellen zodat morgen weer LP-data meekomt, (3) creatives/UTM's checken terwijl de campagne uit staat.

Twee dingen om te weten voor de volgende run: er was **geen cross-reference analyse** mogelijk (beide zijden leeg), en als je wél landing page data in het rapport wilt, moet de PostHog MCP-server eerst weer verbonden worden.

---

Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-02_auto_optimize.md` en gepusht.

## Auto-Optimize Rapport — 2 juli 2026

**Kernbevinding: er zijn geen actieve Meta Ads campagnes, dus niets te optimaliseren.**

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (primair) | ✅ | 0 — alle 5 campagnes PAUSED |
| `act_607231713057715` | ❌ | Token heeft geen toegang |
| `act_1489853856181844` | ✅ | 0 |

**⚡ Automatische acties:** geen ads gepauzeerd — er zijn geen actieve ads om tegen de kill-regels (Link CTR < 0,8% / CPC (link) > €1,50) te toetsen.

**⚠️ Waarschuwingen:** geen — geen actieve creatives.

**📊 70-20-10:** niet van toepassing.

**💡 Enige actiepunt (jouw beslissing):** `2026: SYBB` (dagbudget €100,00) staat sinds 19 april 2026 op pauze. Zolang die uit staat is er geen delivery en dus geen data om op te optimaliseren. Wil je de SYBB-campagne heractiveren? Zodra hij live staat levert dit command vanaf dag 1 weer echte optimalisaties op.

Opmerkingen:
- Conform de strikte regel: alleen Meta Ads MCP gebruikt, geen Google MCP's, niet naar de Tracker Sheet geschreven.
- `act_607231713057715` uit het command is niet bereikbaar met dit token (toegestaan: `act_567892422940728` en `act_1489853856181844`) — vermeld voor het geval de tokenpermissies bijgewerkt moeten worden.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
