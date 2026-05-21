# Meta Ads Rapport — 21 May 2026

**Periode:** last_30d (geen activiteit) + lifetime fallback voor meest recente gepauzeerde campagnes
**Bron:** Pipeboard Meta Ads MCP (account `act_567892422940728` — Sempertex Ad Account)
**Aanvullend account gecheckt:** `act_1489853856181844` (Ambition Avenue) — geen actieve of gepauzeerde campagnes
**Account `act_607231713057715` (Robin Rutten):** Geen toegang met huidige token (Pipeboard error)

---

## Status: geen actieve campagnes

Er draaien op dit moment **geen actieve Meta Ads campagnes** in het Sempertex Ad Account. Alle SYBB en Nozzle Up campagnes staan op PAUSED. Bij gebrek aan recente data (last_30d = leeg) toon ik hieronder de **lifetime performance** van de drie meest recent gepauzeerde campagnes.

---

## Overzicht per campagne (lifetime, gesorteerd op spend)

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS |
|----------|--------|------:|------------:|-------:|----:|----:|----:|------:|-----:|
| 2026: SYBB | PAUSED | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 | 17,8x |
| Last push Nozzle Up | PAUSED | €800,78 | 109.869 | 2.786 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |

**Totaal spend (lifetime, 3 campagnes):** €3.410,24
**Totaal aankopen:** 9
**Totaal omzet (Meta-attributie):** €44.870,00

---

## Underperformers

- **2026: SYBB - Kopie** — CPC €0,64 (drempel €0,50) → Te duur voor de waarde. Slechts 1 dag actief (19 → 20 april) voordat hij gepauzeerd werd. Aanbeveling: **niet herstarten** in deze vorm. Test eerst de creatives op een goedkopere TOFU traffic-campagne voordat je weer op OUTCOME_SALES draait.
- **2026: SYBB - Kopie** — CPM €16,34 (drempel €15) → Dure reach, waarschijnlijk te smalle of overlap-audience. Aanbeveling: verbreed audience of laat Advantage+ open targeten.
- **Last push Nozzle Up** — ROAS 0,8x (drempel 1x = break-even) → Niet winstgevend. 3 aankopen voor €800 spend, gemiddelde orderwaarde €208. Aanbeveling: deze campagne **niet rebooten**. CPC/CTR waren oké, maar de funnel zet niet om. Eerst landing page en aanbod fixen.
- **Last push Nozzle Up** — Frequency 2,39 (drempel 3,5) → Nog binnen marge, geen actie nodig.

---

## Top performers

- **Beste CTR:** 2026: SYBB — 4,1% (sterk boven 1% drempel, ruim boven industrie-benchmark ~1,5%)
- **Laagste CPC:** 2026: SYBB — €0,21 (uitstekend, ver onder €0,50 drempel)
- **Laagste CPM:** Last push Nozzle Up — €7,29
- **Beste ROAS (Meta-attributie):** 2026: SYBB — 17,8x (€44.247 omzet op €2.485 spend)
- **Beste add-to-cart volume:** 2026: SYBB — 53 ATCs, 36 initiate checkout, 6 purchases

---

## SYBB campagne (#1) — extra context

De hoofdcampagne **2026: SYBB** liep van 13 januari t/m ~midden april 2026. Performance was over de hele linie sterk:
- 6.992 landing page views op 12.067 clicks → 58% click → LP view (rest = bounce of bot)
- 53 add to cart → 36 initiate checkout → 6 purchases (8,5% ATC-to-purchase rate, mager)
- 15 leads, 142 view content events
- 68.615 video views (€0,04 per view, zeer goedkoop)
- Frequency 2,24 → audience nog niet uitgeput op moment van pause

De grootste lek zit dus **niet in de top van de funnel** maar in **ATC → purchase**. 53 mensen leggen in de winkelwagen, slechts 6 betalen.

---

## Samenvatting

- **Totaal spend (lifetime, 3 campagnes):** €3.410,24
- **Beste performer:** 2026: SYBB — €0,21 CPC, 4,1% CTR, 17,8x ROAS (Meta-attributie). Sterke top-of-funnel maar ATC → purchase lekt.
- **Slechtste performer:** Last push Nozzle Up — ROAS 0,8x, niet winstgevend. Funnel/aanbod zit fout, niet de ads.
- **Zwakste creative experiment:** 2026: SYBB - Kopie — CPC €0,64 en CPM €16,34. Slechts 1 dag actief, te kort voor leerinzichten.

### Aanbeveling (Hormozi 70-20-10)

1. **70% bewezen winnaar:** Herstart de **2026: SYBB** hoofdcampagne met dezelfde creatives die €0,21 CPC en 4,1% CTR leverden. Vóór relaunch eerst de **ATC → purchase fix** in de checkout flow: 53 mensen in cart, 6 betalen is 11,3% — een gezonde benchmark is 25-40%. Bekijk: pricing weergave, betaalopties, friction in checkout.
2. **20% variatie:** Test 2-3 nieuwe hook-varianten van de top-CTR ad uit 2026: SYBB op een kleine adset (€10-15/dag) voordat je groot opschaalt.
3. **10% experiment:** Houd 2026: SYBB - Kopie en Last push Nozzle Up gepauzeerd. Nozzle Up funnel staat niet, SYBB-Kopie was te kort actief om iets te leren.

**Volgende actie:** Voordat je *één* nieuwe euro op deze campagnes uitgeeft → eerst checkout funnel op startyourballoonbusiness.com diagnosen (PostHog). De ads doen hun werk; de site lekt geld.

---

## Output

- **Lokaal bestand:** `Output/Reports/Daily/2026-05-21_ads_report.md` (dit bestand)
- **Google Sheet schrijfactie:** overgeslagen (run-instructie: geen Google MCP gebruik)

---

> **Wil je funnel data toevoegen?** Geef dan de landing page metrics uit PostHog of Wix Analytics.
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
> Met die data draai ik automatisch een `/funnel-diagnose` analyse (tabel, #1 bottleneck, 3 actiepunten, SYBB benchmark vergelijking).
