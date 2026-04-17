De push faalt door divergerende branches (49 lokale commits vs 31 remote). Ik stop hier met pushen om data niet te verliezen. Het rapport is wel lokaal opgeslagen en gecommit.

Rapport opgeslagen in `Output/Reports/Daily/2026-04-17_ads_report.md` en lokaal gecommit als `f81f76d`. Push faalt door branch divergence — je repo heeft 49 lokale vs 31 remote commits uit elkaar gelopen (waarschijnlijk door auto-sync conflicten op de log files). Laat me weten of ik een merge mag doen of dat je dit zelf eerst wil oplossen.

**Kernbevindingen rapport:**
- 1 actieve campagne: `2026: SYBB`, €834,24 spend / 30d, 6 purchases, CPA €139,04
- 3 actieve ads: H11 (grootste spend, enige echte converter met 4 purchases), H12 (laagste CPC €0,40, beste CTR), H13 (CPC €0,61 grensgeval)
- 🚩 Flags: H11 CPC €0,65 en H13 CPC €0,61 boven drempel €0,50
- **Data caveat:** Meta pixel rapporteert purchase_value €44.247 op 6 purchases — onrealistisch, ROAS 53x is niet bruikbaar. Check Events Manager pixel mapping voor SYBB pixel `888973173636482`
