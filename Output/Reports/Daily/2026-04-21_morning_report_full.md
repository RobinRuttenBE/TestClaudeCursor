# Morning Report — 2026-04-21

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Ads rapport niet beschikbaar. Campagnes staan momenteel op pauze.

---

Rapport aangemaakt en lokaal gecommit (commit `08eca6d`). 

**Rapport:** `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-04-20_sybb_report.md`

**Kerninzichten:**
- Hoofdcampagne "2026: SYBB" stond gepauzeerd; "2026: SYBB Kopie" draaide gisteren (€77.85 spend, CTR 2.78%, CPC €0.65, 0 purchases)
- Bounce rate 89.3% (target <55%), slechts 2 "Book Your Spot" klikken / 71 sessies
- H13 ad is een outlier: CPC €1.02 en 0 checkouts. H11 (€0.51) en H12 (CTR 4.14%) presteren beter
- PostHog scroll depth en session duration geven 0% data → tracking config is kapot

**Push niet uitgevoerd:** branch is sterk gedivergeerd (20 lokale commits vs 106 remote). Push vereist een rebase/merge met potentiële conflicten, dat is een aparte beslissing die ik niet eigenhandig neem. Wil je dat ik dit oplos?

---

Rapport opgeslagen op `Output/Reports/Daily/2026-04-21_auto_optimize.md`.

**TL;DR:**
- **0 ads gepauzeerd** — er zijn momenteel geen actieve campagnes op `act_567892422940728` of `act_1489853856181844`. Alle campagnes staan PAUSED (inclusief `2026: SYBB` en de `- Kopie` variant).
- **Wel spend last_3d:** €262.87 / 16.825 imp / 251 link clicks → **Link CTR 1.49%**, **CPC (link) €1.05**. Beide ruim binnen de drempels — de gepauzeerde ads waren geen kill-candidaten.
- **Geen purchase-events** in de data (alleen ICO/ATC) → ROAS kan niet gemeten worden; tracking-check nodig vóór re-launch.
- **Kernvraag voor jou:** is deze pauze-staat bewust (kopie-refresh, 2026-04-19 timestamps wijzen daar op) of vergeten? Bij bewuste pauze geen actie; bij vergeten herstart: activeer `2026: SYBB`.

Niveau 2 voorstellen (bevestig pauze-intentie, pre-flight tracking, zachtere drempels in learning phase) staan in het rapport — wacht op jouw goedkeuring.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
