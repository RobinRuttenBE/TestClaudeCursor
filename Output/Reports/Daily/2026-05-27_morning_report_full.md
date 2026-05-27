# Morning Report — 2026-05-27

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport opgeslagen. Hier de samenvatting:

## Meta Ads Rapport — 27 mei 2026

**Status:** geen actieve campagnes. Laatste 30 dagen = €0 spend. Alle SYBB activiteit staat sinds 19/20 april op pauze. Lifetime data van de gepauzeerde campagnes gebruikt als referentie.

### Overzicht (lifetime)

| Campagne | Status | Spend | CTR | CPC | CPM | Purchases |
|----------|--------|------:|----:|----:|----:|----------:|
| 2026: SYBB | PAUSED | €2.485,04 | 4,1% | €0,21 | €8,36 | 6 |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 2,6% | €0,64 | €16,34 | 0 |

### Top performer
- **`H13,B3,CTA5` (BATCH 2)** — 9,82% CTR · €0,07 CPC · €421 spend → bewezen winner, schaal-kandidaat

### Underperformers (pauzeren vóór relaunch)
- 4 Kopie-varianten binnen 2026: SYBB (CPC > €0,50)
- Volledige "2026: SYBB - Kopie" campagne (alle 3 ads boven CPC en CPM drempels)
- `SYBB w/ Semp (BLACK)` statische ad (CTR maar 1,03%)

### Belangrijkste signaal
12.067 link clicks → 6.992 LP views → 6 purchases (0,09% LP→purchase) zit ruim onder de >5% benchmark. **Funnel diagnose vereist vóór nieuwe spend.**

### Bestanden
- ✅ Opgeslagen: `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-27_ads_report.md`
- ⏭️ Google Sheet write **overgeslagen** per run-instructie

**Wil je funnel data toevoegen?** Lever LP visitors, opt-in/booking clicks, ATC en completed purchases aan en ik draai automatisch een `/funnel-diagnose`.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-05-26_sybb_report.md`.

**Kern bevindingen voor 26 mei 2026:**

- **Meta Ads** — campagne `2026: SYBB` (ID `120239435987290239`) staat op **PAUSED** sinds ~19 april. Geen spend gisteren of in de laatste 30 dagen. Lifetime referentie: 297k impressies, €2.485 spend, CTR 4,06%, CPC €0,21, 15 leads, 6 purchases.
- **PostHog landing page** — `www.startyourballoonbusiness.com`: 3 pageviews / 3 sessies / 3 unique visitors, 100% bounce, 0s duration. 100% direct traffic, geen UTM-tags. 2 desktop US, 1 desktop UK. 7d-trend: 6-3-1-2-0-0-0-3.
- **Tracking gap** — alleen `$pageview` wordt gevangen. Scroll depth, CTA clicks en `/booking` conversie events ontbreken, dus 6 van 7 Landing Page KPI's uit de skill zijn niet meetbaar.

**Top 3 acties:** (1) beslis re-launch of formeel stop campagne, (2) implementeer scroll/CTA/booking events in PostHog, (3) borg UTM-tagging op alle ad URL's vóór re-launch.

Alleen Meta Ads MCP en PostHog MCP gebruikt; geen Google MCPs aangeroepen en geen schrijfacties naar de Tracker Sheet.

---

Rapport opgeslagen op `Output/Reports/Daily/2026-05-27_auto_optimize.md`.

**Kernconclusie:** geen automatische acties uitgevoerd — alle 5 campagnes in het Sempertex Ad Account staan op `PAUSED` (SYBB sinds 2026-04-19/20, Nozzle Up sinds september 2025). Het secundaire AmbitionAvenue account is leeg. Zonder actieve delivery zijn de kill-regels (Link CTR < 0.8%, CPC link > €1.50) niet toepasbaar.

Open vraag voor jou: is dit verwacht, of moet de SYBB-campagne weer aan? Het morning report draaide vanochtend nog op SYBB-data, dus de pauze is mogelijk recent. Laat het weten als je een re-activatie of refresh-review wil.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
