# Morning Report — 2026-05-22

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 22 May 2026

**Account:** Sempertex Ad Account (`act_567892422940728`) — AmbitionAvenue account heeft 0 campagnes.

**Belangrijke context:** Geen ACTIEVE campagnes in last_30d. Alle campagnes paused sinds 19-20 April 2026. Rapport gebaseerd op last_90d window (laatste meetbare data).

### Overzicht per campagne

| Campagne | Status | Spend | Imp | Clicks | CTR | CPC | CPM | Purch | ROAS |
|---|---|---|---|---|---|---|---|---|---|
| 2026: SYBB | PAUSED | €2.383,30 | 280.906 | 11.900 | 4,2% | €0,20 | €8,48 | 6 | 18,6x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 ⚠️ | €16,34 ⚠️ | 0 | 0,0x |

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 + CPM €16,34, 0 purchases. Stoppen.
- **Ad H11 (`120242894133330239`)** — CPC €0,67 maar 4 purchases en €1.474 omzet → behouden, ROAS 2,8x.

### Top performers
- **Beste ROAS:** Ad H13 (`120242894133350239`) — 207x (€42.774 omzet op €207 spend). Validatie nodig.
- **Beste CTR + Laagste CPC:** Ad H13 (`120241275557280239`) — 9,8% CTR, €0,07 CPC, 4.063 LPV.
- **Meeste checkout intent:** Ad H11 (`120242894133330239`) — 23 ATC, 23 IC, 4 purchases.

### Hoofdaanbevelingen (Hormozi 70-20-10)
1. **70%:** Reactiveer winning ad `120242894133350239` standalone, €30-50/dag, eerst week monitoren.
2. **20%:** 3 variaties op H13-hook naast origineel.
3. **10%:** 1 nieuwe hook + 1 nieuw format experimenteel.
4. Stop campagne 2026: SYBB - Kopie permanent.
5. **Verifieer pixel-attributie** van de €42.774 op 2 purchases — ROAS 207x op 1 ad vraagt om bevestiging via Shopify/Wix voor schaalbeslissing.

### Output
- Lokaal opgeslagen: `Output/Reports/Daily/2026-05-22_ads_report.md`
- Google Sheet write overgeslagen per instructie (Google MCPs uitgesloten voor deze run).

---

**Wil je funnel data toevoegen?** Geef landing page visitors, opt-in/booking clicks, add to cart, completed purchases — dan draai ik automatisch `/funnel-diagnose` en voeg de volledige analyse toe.

---

Report saved to `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-21_sybb_report.md`.

**Korte samenvatting van wat ik vond:**

- **Meta `2026: SYBB`** staat sinds 19 april PAUSED → €0 spend, 0 impressies, geen ad-variant data. Heractivatie-beslissing nodig.
- **PostHog `www.startyourballoonbusiness.com`**: gisteren 1 pageview / 1 unique / 1 sessie (direct, mobiel, US, homepage). 7d-window: 32 pageviews, ~89% bounce rate, vooral organisch Instagram-bio en directe traffic.
- **Belangrijke gap:** scroll-depth en CTA-click events zijn niet geïnstrumenteerd in PostHog — de skill-template vraagt ze, maar alleen `$pageview`, `$pageleave`, `$autocapture` en `$web_vitals` worden gevangen. Daarom staan rij 3 (scroll) en rij 7 (CTA-rate) van de Landing Page Health tabel op "niet gemeten".
- **Top-3 acties:** (1) SYBB-campagne heractiveren of officieel parkeren, (2) scroll + CTA tracking instrumenteren, (3) organische bio-link funnel audit (15 bio-link views → 1 boeking).

Geen Google MCP's gebruikt; alleen Pipeboard Meta Ads MCP en PostHog MCP, conform de instructie.

---

Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-05-22_auto_optimize.md` en gepusht.

**Samenvatting:**
- Beide toegankelijke ad accounts (`act_567892422940728` en `act_1489853856181844`) hebben **0 actieve campagnes**.
- Alle 5 campagnes in het Sempertex account staan op PAUSED (de hoofdcampagne **2026: SYBB** sinds 2026-04-19).
- 0 ads gepauzeerd, geen 70-20-10 classificatie en geen voorstellen — pre-conditie (≥1 actieve campagne) niet behaald.
- Geen Google MCPs aangeroepen, output uitsluitend lokaal opgeslagen.

Wil je dat ik de SYBB campagne reactiveer of een nieuwe campagne opzet?

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
