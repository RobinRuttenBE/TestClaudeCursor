# Morning Report — 2026-07-05

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport gegenereerd en opgeslagen in `Output/Reports/Daily/2026-07-05_ads_report.md`.

## Meta Ads Rapport — 5 juli 2026

**Belangrijkste bevinding: er draaien 0 actieve campagnes.** Ook de laatste 30 dagen was er geen spend — alles staat op PAUSED. Hieronder de laatste bekende performance (last_90d venster, run liep t/m ~20 april 2026).

> Het tweede account `act_607231713057715` uit de command is **niet toegankelijk** met de huidige token. Alleen Sempertex (`act_567892422940728`) en AmbitionAvenue (leeg, €0) zijn beschikbaar.

### Overzicht per campagne (gepauzeerd)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Paused | €1.059,47 | 91.839 | 1.935 | 2,1% | €0,55 | €11,54 | 6 | ~0,42x* |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,00x |
| **Totaal** | — | **€1.183,89** | **99.454** | **2.130** | **2,1%** | **€0,56** | — | **6** | — |

\* SYBB is vooral lead-gen (6 registraties, 44 add-to-carts, 33 checkouts); kost per aankoop €176,58.

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 + CPM €16,34 boven drempel, 0 aankopen → definitief pauzeren
- **Ad H11** — CPC €0,67, maar levert 4 van 6 aankopen → behouden, hook optimaliseren i.p.v. pauzeren
- **Ad H13** — CPC €0,63 → creative refresh
- **Frequency:** nergens boven 1,95 → geen fatigue, ruimte om te schalen

### Top performers
- **Beste CTR op volume:** H12 — 2,6% · **Laagste CPC:** H12 — €0,40
- **Enige converter:** **H11, B3, CTA5** — 4 aankopen + 5 registraties, de motor van de campagne

### Aanbeveling (70-20-10)
70% op bewezen winnaar **H11** + sub-€0,50 ads (**H12, H14**); 20% op **H13** met frisse hook; 10% nieuwe hook-tests **binnen** de hoofdcampagne, niet als losse "Kopie". Bij heractivatie: herstart 2026: SYBB met alleen de top-3 ads en pauzeer de Kopie definitief. Dagbudget kan veilig omhoog (lage frequency).

Google Sheet-write is overgeslagen conform de run-instructie.

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-07-04_sybb_report.md`. Hier is de kern.

## Wat de data zei

**Meta Ads — `2026: SYBB` (`120239435987290239`)**
- Status: **PAUSED**. Dagbudget €100, objective OUTCOME_SALES.
- **Nul delivery** op 4 juli én over het hele 7-daagse referentievenster (27 jun–3 jul): 0 impressies, 0 clicks, €0 spend.
- Laatste actieve maand was **april 2026**. Ter context uit de historische breakdown: Jan €102, Mrt €1.324 (beste maand, CTR 5,27% / CPC €0,13), Apr €1.059 — daarna stil.

**PostHog**
- De PostHog MCP heeft deze sessie **geen tools aangeleverd** (verbinding niet voltooid). Ik kon dus geen pageviews, bounce, scroll depth of CTA-data voor startyourballoonbusiness.com ophalen. In het rapport staat dit als "geen data" (⚪), niet als groene status — ik heb geen cijfers verzonnen.

## Gevolg voor het rapport
Er is geen live funnel om te beoordelen: geen ad-traffic aan de bovenkant én geen landing page events aan de onderkant. De secties zijn volgens de SKILL-structuur ingevuld, maar de nadruk ligt op de twee rode vlaggen.

## Top 3 acties (uit het rapport)
1. **Bevestig de status van `2026: SYBB`** — bewust gepauzeerd of per ongeluk? Elke dag pauze = 0 SYBB-instroom. (Geel — jouw goedkeuring i.v.m. budget vóór heractivatie.)
2. **Herstel de PostHog MCP-verbinding** via `/mcp` in een interactieve sessie, zodat het dagrapport niet blind is. (Groen.)
3. **Tracking-check vóór de volgende flight** — UTM-conventie + Meta Pixel valideren met `/tracking-check`. (Geel.)

Twee dingen om te weten: ik heb **alleen** de Meta Ads en PostHog MCPs aangeroepen (geen Google/Sheets), en de PostHog-connector zul je even opnieuw moeten autoriseren voordat het volgende rapport landing-page data kan tonen.

Wil je dat ik de campagne-status verder uitzoek (bijv. of er een geplande herstart is), of eerst de PostHog-verbinding oppakken?

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-07-05_auto_optimize.md` en is gecommit + gepusht.

## Samenvatting

**Er zijn geen automatische acties uitgevoerd — omdat er geen actieve campagnes draaien.**

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (primair) | ✅ | **0** — alle 5 campagnes PAUSED |
| `act_1489853856181844` | ✅ | **0** |
| `act_607231713057715` | ❌ geen tokentoegang | n.v.t. |

Belangrijkste bevindingen:
- De hoofdcampagne **2026: SYBB** (dagbudget €100,00) staat sinds **19 april 2026** op PAUSED. Alle Nozzle Up-campagnes zijn ook gepauzeerd.
- **Geen ads gepauzeerd**, geen waarschuwingen, geen 70-20-10 classificatie — er is simpelweg geen live data om tegen de kill-regels (Link CTR < 0.8%, CPC link > €1.50) te toetsen.
- Het in het commando genoemde secundaire account `act_607231713057715` is **niet bereikbaar** met de huidige API-token (toegestaan: `act_567892422940728` en `act_1489853856181844`).

Ik heb me strikt aan de regels gehouden: alleen Meta Ads MCP gebruikt, geen Google MCPs, niet naar de Tracker Sheet geschreven.

Twee dingen die je goedkeuring vragen (geen actie ondernomen):
1. **2026: SYBB heractiveren** als de campagne weer moet lopen — zeg het en ik zet 'm aan.
2. **Token-toegang** voor `act_607231713057715` controleren, of het commando bijwerken naar de toegestane accounts.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
