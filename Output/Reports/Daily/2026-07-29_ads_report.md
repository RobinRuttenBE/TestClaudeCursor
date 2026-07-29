## Meta Ads Rapport, 29 juli 2026

**Alleen Meta Ads MCP en PostHog gebruikt. Geen Google MCPs aangeroepen, stap 6 (Sheet write) overgeslagen.**

> **Belangrijkste bevinding: er draait niets.** Nul actieve campagnes, en nul spend in de laatste 30 én 90 dagen. Alle 5 campagnes staan op PAUSED sinds circa 20 april 2026. De cijfers hieronder zijn daarom **lifetime**, niet last 30 days.

### Overzicht per campagne (lifetime, op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Aank. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

Tweede account (AmbitionAvenue) gecheckt: geen campagnes.

### Underperformers

- **2026: SYBB - Kopie**, CPC €0,64 (drempel €0,50) én CPM €16,34 (drempel €15), nul conversies. Niet heropstarten, archiveren.
- **Nozzle Up END OF AUGUST**, CTR 0,99%. Wel bij een CPM van €1,64, dus dit was goedkope brede reach. Alleen voor awareness, niet voor sales.
- **Last push Nozzle Up**, ROAS 0,78x, de enige campagne die geld verloor.
- **SYBB w/ Semp (BLACK)** (ad), CTR 1,0% en nul conversies op €101,74. De enige statische ad. Video wint hier met 9,8% tegenover 1,0%.
- **Frequency:** nergens boven 3,5 (max 2,89). Geen creative fatigue.

### Top performers

- **Beste CTR + laagste CPC:** H13,B3,CTA5 in ad set *BATCH 2: Expertise & POC*, **9,8% CTR bij €0,07 CPC**. Dat is 2,4x de campagne-CTR en een fractie van de €0,50 target.
- **Meeste leads:** H11, B3, CTA5 (Kopie 1) met 6 leads op €202,48.

### Twee dingen die je moet weten voordat je hierop stuurt

**1. De ROAS van 17,8x is niet hard.** De pixel-waarden kloppen niet: 6 registraties met een waarde van €86.100 (€14.350 per stuk) is hoger dan de aankoopwaarde van €44.247. Repareer de value pass-through voor je op ROAS optimaliseert. Voor SYBB is `lead` (15) en `complete_registration` (6) sowieso de echte KPI.

**2. De Kopie ad sets kosten je geld.** Kopie 1 t/m 4 draaien exact dezelfde vier creatives als BATCH 2, maar consequent duurder: dezelfde H13-creative kost €0,07 in BATCH 2 en €0,63 in Kopie 3. Dat is 9x. Ze splitsen het leervolume zonder eigen bijdrage. Consolideren naar één ad set.

### Aanbeveling (70-20-10)

- **70%** op H13 en H15 uit BATCH 2, de bewezen winnaars. Geconcentreerd, niet gespreid over tien ads.
- **20%** op H12 en H14 als variatie, nieuwe hook op het bewezen B3/CTA5 frame.
- **10%** nieuwe hooks. Geen statische creatives meer.

Eerst dit: ad sets consolideren en pixel-waarden repareren. Maar de nuchtere eerste beslissing is of SYBB überhaupt weer aan moet, want er loopt sinds april niets.

Opgeslagen in `Output/Reports/Daily/2026-07-29_ads_report.md` en gecommit + gepusht (`5a90c12b`).

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

Ik kan die ook zelf uit PostHog halen als je wilt, maar met nul ad-verkeer sinds april wordt dat een historische analyse in plaats van een live funnel diagnose. Zeg het maar.
