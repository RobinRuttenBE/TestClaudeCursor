# Morning Report — 2026-07-09

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport gegenereerd en opgeslagen in `Output/Reports/Daily/2026-07-09_ads_report.md`.

## Meta Ads Rapport — 9 juli 2026

**Belangrijk: er draaien momenteel geen actieve campagnes.** Alle campagnes in het Sempertex Ad Account staan op PAUSED. Hieronder de laatst geregistreerde lifetime-performance van de recentste gepauzeerde campagnes. Het tweede account (`act_607231713057715`) is niet toegankelijk met deze token; AmbitionAvenue heeft €0 spend.

### Overzicht per campagne

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|--------|------|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,80x* |
| Last push Nozzle Up | PAUSED | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,78x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,00x |

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 (>€0,50) én CPM €16,34 (>€15) → laten vallen, presteert overal slechter dan het origineel.
- **Last push Nozzle Up** — ROAS 0,78x, onder break-even → archiveren.

### Top performers
- **Beste CTR / laagste CPC**: 2026: SYBB (4,1% / €0,21) — de bewezen winnaar.

### Belangrijkste bevindingen
- **Datawaarschuwing:** SYBB's purchase-waarde (€44.247 op 6 aankopen) is onrealistisch → pixel purchase-value verkeerd geconfigureerd. De 17,80x ROAS is **niet betrouwbaar**; beoordeel SYBB op CTR/CPC en funnel-signalen (15 leads, 53 add-to-cart, 36 checkouts).
- **Conversie-gap:** 12.067 clicks → 6 purchases. De bottleneck zit na de klik, niet in de ad.
- **Aanbeveling (70-20-10):** heractiveer SYBB als kern (fix eerst de pixel), laat de kopie vallen, archiveer Nozzle Up.

De Google Sheet-write (stap 6) is op verzoek overgeslagen.

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` op de SYBB-data — juist die conversie-gap (12.067 clicks → 6 purchases) is het onderzoeken waard.

---

Klaar. Rapport gegenereerd en opgeslagen in `Output/Reports/Daily/2026-07-08_sybb_report.md`, gecommit en gepusht.

## Wat ik vond

**Meta Ads (Pipeboard MCP) — wel bereikbaar:**
- Campagne **`2026: SYBB`** (ID `120239435987290239`) staat op **PAUSED** (laatst gewijzigd 20 april).
- **Nul delivery** op 8 juli: geen spend, impressions of clicks. Een controle over de volledige laatste 30 dagen bevestigt hetzelfde. De funnel krijgt op dit moment geen betaald verkeer.
- Er is ook een tweede paused campagne `2026: SYBB - Kopie` — let op dat je bij heractivatie de juiste kiest.

**PostHog MCP — niet beschikbaar deze run:**
- De server stond in de verbindingslijst, maar stelde geen tools beschikbaar (vier zoekpogingen, geen enkele PostHog-tool). Landing page data (bounce, scroll, CTA) kon ik daardoor niet ophalen. Die secties staan expliciet als "geen data" met een rode vlag.

**Strikte regel gevolgd:** alleen Meta Ads MCP geraadpleegd, geen Google MCPs, niets naar de Google Sheet tracker geschreven, output enkel lokaal.

## Belangrijkste acties (staan uitgewerkt in het rapport)
1. Beslis of SYBB actief hoort te zijn en zet de juiste campagne live (nul verkeer al 30 dagen).
2. Herstel de PostHog MCP-verbinding via een interactieve sessie (`/mcp`), draai daarna dit rapport opnieuw voor volledige data.
3. Verifieer creatives, UTM-tagging en landing page tracking vóór heractivatie.

Wil je dat ik na herstel van PostHog het rapport opnieuw draai, of wil je dat ik de campagne-heractivatie voorbereid?

---

Klaar. Hier is de samenvatting van de `/ads-auto-optimize` run voor **9 juli 2026**:

## Belangrijkste bevinding: er valt niets te optimaliseren

**Er zijn 0 actieve campagnes.** Alle 5 campagnes op het primaire account `act_567892422940728` staan op **PAUSED** — inclusief de hoofdcampagne **2026: SYBB** (€100,00/dag), die sinds 19 april 2026 op pauze staat.

**Gevolg:**
- ⚡ **0 ads gepauzeerd** — geen live delivery, dus de kill-regels (Link CTR < 0.8%, CPC (link) > €1,50) konden nergens op triggeren.
- 📊 **Geen 70-20-10 classificatie** — zonder impressions/link clicks/spend kan geen ad worden ingedeeld.
- 💡 **Geen data-gedreven budget-/variatie-voorstellen** mogelijk.

## Twee zaken die jouw beslissing vragen

1. **Heractivatie SYBB?** Alles staat op PAUSED. Is dat bewust, of moet de SYBB-campagne weer aan? Zolang alles gepauzeerd is heeft de dagelijkse auto-optimalisatie geen functie.
2. **Secundair account `act_607231713057715` is onbereikbaar** — token-fout. De Pipeboard-connectie geeft alleen toegang tot `act_1489853856181844` en `act_567892422940728`. Opvallend: dat eerste account (`...181844`) is wél toegankelijk maar staat niet in het command — mogelijk relevant om toe te voegen. Wil je dat ik dat account meeneem in een volgende run?

Rapport opgeslagen in `Output/Reports/Daily/2026-07-09_auto_optimize.md` en gecommit + gepusht. Conform de strikte regel: alleen Meta Ads MCP gebruikt, geen Google-services, niets naar de Google Sheet geschreven.

Wil je dat ik iets met de bovenstaande punten doe?

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
