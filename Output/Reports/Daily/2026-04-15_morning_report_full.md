# Morning Report — 2026-04-15

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport is klaar en gepusht. Hier is de samenvatting:

## Meta Ads Rapport -- 15 april 2026

### Campagne: 2026: SYBB (laatste 30 dagen)

| Metric | Waarde |
|--------|--------|
| Spend | EUR 701,74 |
| Impressions | 66.257 |
| Reach | 34.460 |
| CTR | 2,0% |
| CPC | EUR 0,52 |
| Purchases | 2 (EUR 42.773,50) |
| ROAS | 60,95x |

### Actieve ads (3 van 21)

| Ad | CPC | CTR | Purchases | Flag |
|----|-----|-----|-----------|------|
| **H12,B3,CTA5** | EUR 0,40 | 2,3% | 0 | Beste CPC |
| **H13,B3,CTA5** | EUR 0,61 | 1,9% | 2 (299,8x ROAS) | CPC boven drempel |
| **H11, B3, CTA5** | EUR 0,66 | 1,9% | 0 | CPC boven drempel, hoogste spend |

### Key takeaways

1. **H11 is de bottleneck:** 52% van actieve spend, 13 ATC + 13 IC maar 0 purchases. Checkout drop-off onderzoeken.
2. **H12 is de efficiëntste:** laagste CPC, hoogste CTR. Draait pas sinds 9 april, meer tijd nodig.
3. **H13 is de revenue driver:** enige ad met purchases (ROAS 299,8x).
4. **Frequency (1,92) is gezond:** geen creative fatigue risico.

Rapport opgeslagen in `Output/Reports/Daily/2026-04-15_ads_report.md`.

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit PostHog of GA4. Ik heb nodig: landing page visitors, bounce rate, scroll depth, CTA clicks, /booking visits. Dan draai ik automatisch een `/funnel-diagnose` analyse.

---

SYBB Daily Report 14 april staat klaar in `Output/Reports/Daily/2026-04-14_sybb_report.md`. Gecommit en gepusht.

**Belangrijkste bevindingen:**

| Metric | Gisteren | 7d Avg | Signaal |
|---|---|---|---|
| Spend | €95,91 | €100,25 | Stabiel |
| CPC | €0,63 | €0,52 | 🚩 +21%, boven target |
| CTR | 2,09% | 2,04% | Stabiel |
| Purchases | 0 | 0,3/dag | 2e dag op rij 0 |

**3 urgente acties:**
1. **Budget shift H11 → H12** -- H11 verbrandt 66% van spend met slechtste metrics. H12 (9% budget) heeft beste CTR (2,85%) en enige add-to-carts.
2. **Checkout flow testen** -- 2 dagen 0 purchases, 0 initiated checkouts gisteren ondanks 2 ATC events. Mogelijke technische blokkade.
3. **PostHog MCP herstellen** -- PostHog MCP was niet verbonden in deze sessie. Landing page health data (bounce rate, scroll depth, CTA clicks) ontbreekt volledig. Herstart sessie om cross-referencing te herstellen.

---

## Auto-Optimize samenvatting, 15 april 2026

**Niveau 1 (uitgevoerd):** 0 ads gepauzeerd. Alle 3 actieve ads presteren boven de drempelwaarden.

**3 actieve ads status (last 3d):**

| Ad | Link CTR | CPC (link) | Spend % |
|----|----------|-----------|---------|
| H11 (Kopie 1) | 0,98% | €1,40 | 62,4% |
| H12 (Kopie 2) | 1,19% | €1,16 | 12,2% |
| H13 (Kopie 3) | 1,17% | €1,10 | 25,5% |

**Waarschuwingen:**
- H11 CPC (link) €1,40 nadert kill-grens (€1,50). Bij ~500 link clicks wordt regel scherp.
- H11 slokt 62% van budget op terwijl H12/H13 efficiënter zijn op CPC en CPM.
- Positief: H11 Link CTR verbeterd van 0,9% (gisteren) naar 0,98%. CPC gedaald van €1,45 naar €1,40.

**Niveau 2 voorstellen (wachten op goedkeuring):**
1. H11 CPC monitoring verscherpen
2. Budget herverdeling via ad set spend limits (A: min €20/dag Kopie 2, B: max €50/dag Kopie 1)
3. H12 funnel diagnose (0 checkouts/purchases op 123 lifetime link clicks)
4. H13 ROAS anomalie verifiëren (€42.773,50 purchase)

Rapport opgeslagen en gepusht. Geef aan welke voorstellen (1/2A/2B/3/4) je wil uitvoeren.

---

Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
