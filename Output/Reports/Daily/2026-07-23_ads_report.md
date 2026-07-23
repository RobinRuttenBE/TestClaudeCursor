Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-23_ads_report.md` en gecommit + gepusht. Alleen de Meta Ads MCP is gebruikt — geen Google MCPs, geen write naar de Tracker Sheet.

## Meta Ads Rapport — 23 juli 2026

⚠️ **Geen actieve campagnes.** Alles staat op PAUSED, €0 spend in de laatste 30 dagen. Ik heb daarom de lifetime data van de 5 meest recente gepauzeerde campagnes getoond (fallback-regel). Het genoemde tweede account `act_607231713057715` is niet toegankelijk onder deze login.

| Campagne | Spend | CTR | CPC | CPM | Aankopen | ROAS* |
|----------|-------|-----|-----|-----|----------|-------|
| 2026: SYBB | €2.485,04 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | €853,19 | 2,5% | €0,26 | €6,59 | 6 | 8,3x* |
| Last push Nozzle Up | €800,78 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | €604,03 | 1,0% | €0,17 | €1,64 | 6 | 6,4x* |
| 2026: SYBB - Kopie | €124,42 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

**Kernpunten:**
- **Beste performer:** 2026: SYBB — 4,1% CTR, €0,21 CPC, veruit het sterkste verkeer. De hooks werken.
- **Underperformers:** *SYBB - Kopie* (CPC €0,64 + CPM €16,34, 0 aankopen → schrappen) en *Nozzle Up END OF AUGUST* (CTR 1,0%, grensgeval maar economics gezond).
- **ROAS onbetrouwbaar:** €7.374/order en €1.180/order wijzen op een fout in de pixel purchase-waarde. Stuur op aantal aankopen + CPA, niet op ROAS, tot dat geverifieerd is.
- **Echte knelpunt = funnel, niet de ads:** 6.992 LP-views → 6 aankopen op de hoofdcampagne.
- **Aanbeveling (70-20-10):** bij heropstart één bewezen campagne (2026: SYBB), pixel-waarde fixen, en prioriteit op landing page conversie.

---

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4 — visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose`; gezien de 6.992 LP-views → 6 aankopen is dat hier de belangrijkste analyse.
