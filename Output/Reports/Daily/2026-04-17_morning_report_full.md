# Morning Report — 2026-04-17

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,09%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,01** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 85,37** over 10 actieve dagen (niet totaal/30)
> - Bron: spend EUR 853,66 · impressions 77.756 · link_clicks 844
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H12,B3,CTA5 | EUR 14,37 | 1.058 | 20 | 1,89% | EUR 0,72 |
> | H13,B3,CTA5 | EUR 0,01 | 1 | 0 | 0,00% | EUR 0,00 |
> | H14,B3,CTA5 | EUR 122,96 | 16.551 | 158 | 0,95% | EUR 0,78 |
> | H15,B3,CTA5 | EUR 2,32 | 157 | 4 | 2,55% | EUR 0,58 |
> | H15,B3,CTA5 | EUR 49,83 | 4.737 | 57 | 1,20% | EUR 0,87 |
> | H11, B3, CTA5 | EUR 386,34 | 29.404 | 313 | 1,06% | EUR 1,23 |
> | H13,B3,CTA5 | EUR 160,60 | 13.492 | 154 | 1,14% | EUR 1,04 |
> | H12,B3,CTA5 | EUR 117,23 | 12.356 | 138 | 1,12% | EUR 0,85 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

De push faalt door divergerende branches (49 lokale commits vs 31 remote). Ik stop hier met pushen om data niet te verliezen. Het rapport is wel lokaal opgeslagen en gecommit.

Rapport opgeslagen in `Output/Reports/Daily/2026-04-17_ads_report.md` en lokaal gecommit als `f81f76d`. Push faalt door branch divergence — je repo heeft 49 lokale vs 31 remote commits uit elkaar gelopen (waarschijnlijk door auto-sync conflicten op de log files). Laat me weten of ik een merge mag doen of dat je dit zelf eerst wil oplossen.

**Kernbevindingen rapport:**
- 1 actieve campagne: `2026: SYBB`, €834,24 spend / 30d, 6 purchases, CPA €139,04
- 3 actieve ads: H11 (grootste spend, enige echte converter met 4 purchases), H12 (laagste CPC €0,40, beste CTR), H13 (CPC €0,61 grensgeval)
- 🚩 Flags: H11 CPC €0,65 en H13 CPC €0,61 boven drempel €0,50
- **Data caveat:** Meta pixel rapporteert purchase_value €44.247 op 6 purchases — onrealistisch, ROAS 53x is niet bruikbaar. Check Events Manager pixel mapping voor SYBB pixel `888973173636482`

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-16_sybb_report.md`.

**Samenvatting:**
- Meta data opgehaald voor 16 april: €57,79 spend, 4.498 impressions, CTR 2,31%, CPC €0,56, **0 purchases** (vs 0,86/dag gemiddeld)
- **Kritieke bevinding:** 5 initiated checkouts, 0 purchases = 100% drop-off bij betaalstap
- **Spend daling 43%** vs 7d gemiddelde, oorzaak onduidelijk (check delivery/audience)
- **H13 beste variant** (CTR 2,40%, CPC €0,53). H11 nam 72% budget maar 0 purchases
- **PostHog MCP niet beschikbaar** in deze sessie, LP health sectie geflagd als blinde vlek

Top 3 acties: checkout flow zelf testen, spend-daling onderzoeken, PostHog MCP herstellen.

---

Rapport opgeslagen en lokaal gecommit. De push faalt door branch-divergence (50 lokale vs 31 remote commits, met merge-conflict op `logs/morning-report-2026-04-16.log` uit de auto-sync). Dit los ik niet zelf op — het is een destructieve operatie die jouw oordeel vereist.

**Samenvatting rapport:** 0 ads gepauzeerd. Alle 3 actieve SYBB ads passen de kill-regels (Link CTR >0,8%, CPC link <€1,50). H11 is Core met ROAS 8,82x (4 purchases, €1.473). H12 is de meest kansrijke emerging met Link CTR 1,5% en CPC €0,85 maar krijgt te weinig budget. Voorstel: H12 verhogen naar €15/dag, H13 verlagen naar €10/dag, experimental slot openen.

Opgeslagen: `Output/Reports/Daily/2026-04-17_auto_optimize.md`. Push wacht op handmatige resolutie van de auto-sync divergence.

---

Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
