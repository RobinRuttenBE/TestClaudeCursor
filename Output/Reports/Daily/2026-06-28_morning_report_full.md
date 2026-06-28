# Morning Report — 2026-06-28

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 28 juni 2026

> **Let op:** er zijn **geen actieve campagnes**. Alles staat op PAUSED, geen spend in de laatste 30 dagen. Onderstaande cijfers zijn de **laatst bekende (lifetime) performance** per campagne. Het tweede account (AmbitionAvenue) heeft €0,00 spend en geen campagnes.

### Overzicht per campagne (gesorteerd op spend, lifetime)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Campagne Nozzle Up 2025 1 | PAUSED | €853,19 | 129.558 | 3.291 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | PAUSED | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | PAUSED | €604,03 | 369.136 | 3.638 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

### Underperformers

- **2026: SYBB - Kopie** — CPC €0,64 (drempel €0,50) en CPM €16,34 (drempel €15) → te duur, te weinig volume om te leren. Niet los heractiveren; vouw terug in hoofdcampagne.
- **Nozzle Up END OF AUGUST** — CTR 0,99% (drempel 1%) → goedkope brede reach maar zwakke hook. Hook-test nodig.
- **Last push Nozzle Up** — ROAS 0,8x → verlieslatend format, niet kopiëren.
- Geen campagne met frequency > 3,5 (hoogste 2,89).

### Top performers

- **Beste CTR:** 2026: SYBB — 4,1%
- **Laagste CPC:** Nozzle Up END OF AUGUST — €0,17
- **Beste ROAS:** 2026: SYBB — 17,8x

### Samenvatting

- **Totaal spend (lifetime, 5 campagnes):** €4.867,46 | 21 purchases | blended ROAS ~11,5x
- **Beste performer:** **2026: SYBB** — hoogste CTR, laagste CPC binnen de lijn, beste ROAS, meeste leads (15) en landing page views (6.992). De bewezen winnaar.
- **Slechtste performer:** **2026: SYBB - Kopie** (nul purchases, duurste CPC/CPM) en **Last push Nozzle Up** (ROAS 0,8x).
- **Aanbeveling (70-20-10):** Er draait nu niets. Grootste hefboom = de bewezen winnaar heractiveren: zet **2026: SYBB** weer aan, 70% budget op de winnende adsets, 20% op varianten van de hooks die 4,1% CTR opleverden, 10% experiment. Laat de "Kopie" en het "Last push" format met rust.

> Purchase values komen uit de Meta pixel en gedragen zich als B2B-orders (~€7.300 gem. orderwaarde). Behandel ROAS als directioneel, niet boekhoudkundig.

### Google Sheet
Overgeslagen op verzoek. Rapport opgeslagen in `Output/Reports/Daily/2026-06-28_ads_report.md`.

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Met die cijfers draai ik automatisch een `/funnel-diagnose` (tabel, #1 bottleneck, 3 actiepunten, SYBB-vergelijking) en voeg die toe aan het rapport. Ik kan de PostHog-data van de SYBB landing page er ook bij halen als je dat wilt.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-06-27_sybb_report.md`. Twee belangrijke bevindingen:

## Wat ik vond

**Meta Ads (✅ opgehaald via Pipeboard MCP)**
- Campagne **"2026: SYBB"** bestaat (id `120239435987290239`) maar staat op **PAUSED**.
- **Nul delivery** elke dag van 20–27 June 2026: geen spend, impressions of clicks. Er is dus geen ad- of variant-data om te rapporteren.

**PostHog (❌ niet beschikbaar)**
- Er is **geen PostHog MCP server verbonden** met deze sessie. Beschikbare MCP servers: ga4, google, imessage, instagram, lottiefiles, pipeboard-meta-ads.
- Conform je strikte regel heb ik **geen Google MCP** (ook niet ga4) als vervanging gebruikt. Landing page health en de funnel/cross-reference analyse konden daarom niet worden gemaakt.

## Belangrijkste acties
1. **Beslis over de campagne-status** — `2026: SYBB` draait niet, dus er komt momenteel geen SYBB-acquisitie via Meta binnen.
2. **Herstel de PostHog MCP verbinding** — zonder PostHog werkt de kern van dit rapport (LP-data + cross-referencing) niet.
3. Draai het rapport opnieuw zodra de campagne live is én PostHog beschikbaar is.

Wil je dat ik de campagne activeer (daarvoor heb ik je expliciete goedkeuring nodig, want het is een budget-/strategiebeslissing), of laten we 'm bewust gepauzeerd?

---

Klaar. Rapport opgeslagen en gepusht. De korte samenvatting:

## ⛔ Geen optimalisatie uitgevoerd — geen actieve campagnes

Er draaide niets om te optimaliseren. Wat ik vond:

- **`act_567892422940728`** (primair): 5 campagnes, **allemaal PAUSED**. De hoofdcampagne **2026: SYBB** staat sinds 19 april 2026 op pauze — insights-check over de laatste 3 dagen bevestigt **0 spend, 0 impressions**.
- **`act_1489853856181844`**: 0 actieve campagnes.
- **`act_607231713057715`** (genoemd in het command): **geen toegang** met het huidige Pipeboard-token. Toegestane accounts zijn alleen `act_567892422940728` en `act_1489853856181844`.

Daardoor: geen kill-regels getriggerd, geen ads gepauzeerd, geen 70-20-10 classificatie, geen budgetvoorstellen — allemaal niet van toepassing zonder live delivery.

**Twee aandachtspunten voor jou:**
1. Geen enkele campagne is live. Wil je dat dit command zinvol werkt, activeer dan eerst minimaal één campagne (vermoedelijk **2026: SYBB**) en draai het opnieuw.
2. `act_607231713057715` is niet bereikbaar. Check of dit het juiste account-ID is, of herautoriseer de Pipeboard-connectie via https://pipeboard.co/connections — anders blijft dit account buiten elke geautomatiseerde optimalisatie.

Alle output is uitsluitend lokaal opgeslagen; geen Google MCPs aangeroepen en niet naar de Google Sheet tracker geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
