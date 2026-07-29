# Morning Report — 2026-07-29

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

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

---

Rapport staat in `Output/Reports/Daily/2026-07-28_sybb_report.md`, gecommit en gepusht.

**Alleen Meta Ads MCP en PostHog MCP gebruikt.** Geen Google-tools aangeroepen, niets naar de tracker Sheet geschreven.

## Wat de data laat zien

**Meta Ads:** de campagne `2026: SYBB` staat op PAUSED sinds 19 april 2026. Nul spend, impressies en clicks op 28 juli, en ook nul over het hele venster 22 t/m 28 juli. Op accountniveau is er tussen 1 april en 28 juli alleen delivery in april: mei, juni en juli hebben nul spend over álle campagnes.

**PostHog:** de landing page kreeg 0 pageviews op 28 juli. Over de week 22 t/m 28 juli waren het er 2 in totaal, tegen 18 de week ervoor.

Drie dingen die verder gingen dan het lege dagcijfer:

1. **April was al aan het verslechteren voordat er gepauzeerd werd.** CPC ging van €0,13 (maart) naar €0,55 (april), CTR halveerde van 5,27% naar 2,11%, frequency liep op naar 2,19. Klassieke fatigue. Relevant omdat dezelfde creatives opnieuw aanzetten waarschijnlijk op april-niveau start, niet op maart-niveau.

2. **De tracking is deels stukgelopen.** `$autocapture` en `$pageleave` zijn na 10 juli niet meer gezien, terwijl `$pageview` doorloopt tot 27 juli. Er bestaat bovendien geen CTA-click event. Daarmee zijn 5 van de 7 KPI's uit de skill (bounce rate, scroll 25/50/75/100%, CTA click rate) op dit moment structureel niet meetbaar, ook niet na heractivatie.

3. **De 90-daagse scroll-baseline wijst naar de hero, niet naar paginalengte.** Van de 30 gemeten homepage-sessies haalt 70% de 25%, 53% de 50%, 40% de 75%. Wie voorbij de helft komt leest meestal uit; de uitval zit bovenaan. Steekproef is klein, dus indicatie, geen hard cijfer.

Ik heb ook een UTM-conventiefout gevonden: één ad stuurt `META / SYBB / H14,B3,CTA5` in hoofdletters met komma's in plaats van lowercase met underscores. PostHog telt dat als aparte waarde, wat de per-variant rapportage vervuilt zodra er weer volume is.

De kernvraag voor jou: staat SYBB bewust uit, of hoort dit te draaien? Zolang dat onbeslist is, blijft dit dagrapport hetzelfde beeld geven.

---

Committed and pushed. Report saved to `Output/Reports/Daily/2026-07-29_auto_optimize.md`.

## Wat ik vond

**Er draait niets.** Alle 5 campagnes in `act_567892422940728` staan op PAUSED. Laatste spend was **April 2026**, 91 dagen geleden. Nul impressies en nul spend in de laatste 30 dagen. Geen ads gepauzeerd, want er is niets om te pauzeren.

Ik heb het rapport daarom omgebouwd tot een relaunch-briefing op basis van de laatste actieve periode (March/April, 9 ads, €2.383,30).

## De belangrijkste bevinding

De 70-20-10 drempels uit het command wijzen op deze data **exact de verkeerde kant op**:

| | "Core" volgens drempels | "Emerging" volgens drempels |
|---|---|---|
| Link clicks | 9.185 | 1.550 |
| Spend | €1.075,09 | €1.308,21 |
| **Aankopen** | **0** | **alle 6** |

De traffic-geoptimaliseerde ad set haalde 4,8% Link CTR voor €0,15 per click en leverde **nul omzet**. De conversie-ad set haalde 1,2% Link CTR voor €1,08 per click en leverde **alle 6 aankopen**. Het verschil zit in klikkwaliteit: 80 tot 88% van die clicks laadde de pagina echt, tegenover 60 tot 70% bij het goedkope verkeer.

Scherpste voorbeeld: dezelfde hook H13 deed 6.342 clicks à €0,07 met nul aankopen in de ene ad set, en 195 clicks à €1,06 met twee aankopen in de andere.

De TODO in het command over het herijken van die drempels is dus niet cosmetisch. Budget verschuiven naar Link CTR zou hier de omzet naar nul brengen. Ook goed om te weten: geen enkele ad zou door de huidige kill-regels geraakt zijn, maar H11 Kopie zat met €1,22 CPC (link) dicht bij de €1,50-grens en had 4 van de 6 aankopen.

## Twee dingen die je aandacht nodig hebben

1. **Pixel purchase values zijn corrupt.** 2 aankopen gerapporteerd als €42.773,50, 4 aankopen als €1.473,50. Ik heb daarom bewust geen ROAS berekend, dat zou verzonnen zijn. Dit is blokkerend voor elke omzetgestuurde beslissing.

2. **`act_607231713057715` is niet toegankelijk** met dit token (alleen `act_567892422940728` en `act_1489853856181844` zijn toegestaan). Als daar iets draait, is dat niet meegenomen. Het command noemt dat account wel als bron, dus dat gat blijft anders stilzwijgend bestaan.

PostHog bevestigt het beeld: de SYBB landing page doet ~2 bezoekers per dag. Wel merk ik op dat PostHog de webshop pas sinds 15 July 2026 volgt, dus cross-referencing met de Meta-historie is beperkt.

De 5 voorstellen in het rapport wachten op je goedkeuring, ik heb niets aan de campagnes gewijzigd.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
