# Morning Report — 2026-07-01

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 1 juli 2026

⚠️ **Belangrijk: er zijn geen actieve campagnes.** Beide ad accounts staan volledig op pauze en in de **laatste 30 dagen is er €0,00 uitgegeven**. Hieronder de meest recente gepauzeerde campagnes met hun laatste (lifetime) performance.

**Accounts:** Sempertex (`act_567892422940728`, €4.867,46 lifetime, alles PAUSED) · AmbitionAvenue (`act_1489853856181844`, €0,00, leeg).

### Overzicht per campagne (gepauzeerd, gesorteerd op spend)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. | ROAS |
|----------|--------|-------|-------|--------|-----|-----|-----|--------|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | Paused | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | Paused | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | Paused | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

**\*ROAS-caveat SYBB:** €42.773 van de €44.247 komt uit slechts **2 aankopen op één ad (H13)** — waarschijnlijk grote B2B-orders. De ROAS is dus vertekend; de betrouwbaarste ROAS in het account is **Nozzle Up 2025 1 (8,3x)**.

### Underperformers
- **2026: SYBB - Kopie** — CPC €0,64 én CPM €16,34 (beide boven drempel) → klein testkopietje, 0 purchases. Niet zo heractiveren.
- **Last push Nozzle Up** — ROAS 0,8x (verliesgevend) → budget naar de bewezen "Nozzle Up 2025 1"-opzet.
- **Ad H11/H13 (set b)** binnen SYBB — CPC €0,63–0,67 terwijl dezelfde hooks in set a 3–9x goedkoper draaien → dure duplicaten killen.
- **SYBB w/ Semp (BLACK)** — CPC €0,61, CTR 1,0%, 0 conversies → uitfaseren.
- Geen creative fatigue: hoogste frequency was 1,95 (drempel 3,5).

### Top performers
- **Beste CTR + laagste CPC:** Hook **H13,B3,CTA5** — **9,8% CTR, €0,07 CPC** (5.902 clicks). Duidelijke winnaar.
- **Goedkoopste reach:** Nozzle Up END OF AUGUST — CPM €1,64.

### Aanbeveling (70-20-10)
1. **70% — schaal H13** als hoofdhook bij heractivatie van 2026: SYBB, op de goedkope adset; kill de dure duplicaten.
2. **20% — varieer** met H15/H12 (sterke CTR/CPC) op H13's stramien.
3. **10% — experiment:** nieuwe hook op de goedkope END-OF-AUGUST-targeting (CPM €1,64).

**Opgeslagen naar:** `Output/Reports/Daily/2026-07-01_ads_report.md` · Google Sheet-stap overgeslagen conform de strikte regel van deze run (geen Google MCPs).

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose` over de gecombineerde Meta + funnel data (bottleneck + 3 actiepunten + SYBB-vergelijking).

Zal ik het rapport ook committen en pushen naar GitHub (conform je auto-commit voorkeur)?

---

Rapport opgeslagen: `Output/Reports/Daily/2026-06-30_sybb_report.md`

**Belangrijkste bevindingen — beide databronnen leverden geen bruikbare cijfers:**

1. **Meta Ads (wél verbonden, echte data):** de campagne `2026: SYBB` staat op **PAUSED** en had **nul delivery** over de hele periode 24–30 juni — geen spend, impressions of clicks. Dit is geen fout; de campagne levert simpelweg niets. Budget staat wel ingesteld op €100/dag, maar loopt niet zolang hij gepauzeerd is.

2. **PostHog: niet beschikbaar.** Er was **geen PostHog MCP verbonden** in deze sessie (de geconnecteerde servers waren o.a. pipeboard-meta-ads, instagram, google, granola, maar geen PostHog). Landing-page-analytics voor startyourballoonbusiness.com kon dus niet opgehaald worden. Ik heb dit expliciet als data-gat gemarkeerd in plaats van cijfers te verzinnen.

**Regel gevolgd:** alleen de Meta Ads MCP (Pipeboard) geraadpleegd. Geen Gmail, Calendar, Drive, Sheets, Docs of Slides aangeroepen; niets naar de Google Sheet tracker geschreven; output enkel lokaal opgeslagen.

**Top acties in het rapport:**
1. Beslis of `2026: SYBB` weer live moet (of bevestig dat de pauze bewust is).
2. Herstel de PostHog MCP-connectie.
3. Draai het rapport opnieuw zodra beide bronnen live zijn.

Wil je dat ik de SYBB-campagne activeer (status → ACTIVE) in Meta Ads Manager, of laat je hem bewust op pauze staan?

---

Klaar. Rapport opgeslagen en gepusht.

## Uitkomst: geen actieve ads om te optimaliseren

De run heeft alleen de Meta Ads MCP (Pipeboard) gebruikt — geen Google MCPs, geen Sheet-writes. Wat ik vond:

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| `act_567892422940728` (primair) | ✅ | **0** — alle 5 campagnes PAUSED |
| `act_1489853856181844` (toegestaan) | ✅ | 0 |
| `act_607231713057715` (in command genoemd) | ❌ geen toegang | n.v.t. |

Omdat er **geen enkele actieve ad draait**, konden de kill-regels (Link CTR < 0.8%, CPC (link) > €1.50) niet triggeren, is er geen 70-20-10 classificatie mogelijk, en zijn er geen data-gedreven voorstellen. Er zijn dus **geen ads gepauzeerd** en **niets uitgevoerd** — correct gedrag, geen actie is de juiste actie.

**Twee dingen die je aandacht verdienen:**

1. **De SYBB-campagne staat uit.** `2026: SYBB` (dagbudget €100,00) is sinds 19 april 2026 gepauzeerd. Zolang die uit staat heeft deze command niets te optimaliseren. Zet 'm handmatig op ACTIVE als SYBB weer moet lopen.
2. **`act_607231713057715` is niet toegankelijk** met de huidige Pipeboard-token (toegestaan: `act_1489853856181844` + `act_567892422940728`). Als daar ads verwacht worden, is dit een autorisatie-issue — opnieuw koppelen via https://pipeboard.co/connections.

Rapport staat in `Output/Reports/Daily/2026-07-01_auto_optimize.md`.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
