# Morning Report — 2026-05-08

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,13%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,02** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 88,29** over 12 actieve dagen (niet totaal/30)
> - Bron: spend EUR 1059,47 · impressions 91.839 · link_clicks 1.036
> 
> **Per-ad link metrics (hardcoded):**
> 
> | Ad | Spend | Impressions | Link Clicks | Link CTR | CPC (link) |
> |---|---|---|---|---|---|
> | H12,B3,CTA5 | EUR 14,37 | 1.058 | 20 | 1,89% | EUR 0,72 |
> | H13,B3,CTA5 | EUR 0,01 | 1 | 0 | 0,00% | EUR 0,00 |
> | H14,B3,CTA5 | EUR 122,96 | 16.551 | 158 | 0,95% | EUR 0,78 |
> | H15,B3,CTA5 | EUR 2,32 | 157 | 4 | 2,55% | EUR 0,58 |
> | H15,B3,CTA5 | EUR 49,83 | 4.737 | 57 | 1,20% | EUR 0,87 |
> | H11, B3, CTA5 | EUR 521,56 | 38.614 | 428 | 1,11% | EUR 1,22 |
> | H13,B3,CTA5 | EUR 206,99 | 16.766 | 195 | 1,16% | EUR 1,06 |
> | H12,B3,CTA5 | EUR 141,43 | 13.955 | 174 | 1,25% | EUR 0,81 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Report committed and pushed. Summary below.

---

## Meta Ads Rapport — 8 mei 2026

**Geen actieve campagnes** op Sempertex Ad Account (act_567892422940728) of het tweede toegankelijke account (act_1489853856181844). Het derde account (act_607231713057715) is niet langer toegankelijk met dit token.

Rapport gebaseerd op de twee meest recent gepauzeerde campagnes (last_30d, 2026-04-08 t/m 2026-05-07):

| Campagne | Spend | Impr. | CTR | CPC | CPM | Freq | Purchases |
|----------|-------|-------|------|-----|-----|------|-----------|
| 2026: SYBB | €1.059,47 | 91.839 | 2,1% | €0,55 | €11,54 | 2,19 | 6 |
| 2026: SYBB - Kopie | €124,42 | 7.615 | 2,6% | €0,64 | €16,34 | 1,42 | 0 |

**Top performers:** H12 (Kopie 2) — laagste CPC €0,40 + hoogste CTR met volume; H11 (Kopie 1) — ? purchases (verifieer Wix) op €521 spend.

**Underperformers:** Heel "SYBB - Kopie" (CPC + CPM beide over drempel, ? purchases (verifieer Wix)). H13 in "SYBB - Kopie" Kopie 3 is de slechtste ad (CPC €0,93, CPM €19,14).

**Belangrijkste aanbeveling:** Bij heractivatie: sluit "2026: SYBB - Kopie" af, schaal H11 + H12 in de main campagne (70-20-10 logica), audit audience overlap voordat je weer parallelle SYBB campagnes start.

**Output:** `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-08_ads_report.md` (stap 6 — Google Sheet write — overgeslagen per instructie).

> **Wil je funnel data toevoegen?** Geef LP metrics (visitors, opt-in/booking clicks, ATC, purchases) en ik draai een `/funnel-diagnose` op de gecombineerde dataset.

---

Report opgeslagen: `Output/Reports/Daily/2026-05-07_sybb_report.md`.

**Kernpunten:**
- Meta campagne `2026: SYBB` (id `120239435987290239`) staat PAUSED, nul spend gisteren én in het 7d window.
- PostHog: 1 pageview, 1 sessie, 11s, bounce 100% gisteren. 7d gemiddeld 3,4 pv/dag, 84,2% bounce.
- Tracking gap: alleen `$pageview`/`$pageleave`/`$autocapture`/`$web_vitals` gelogd, geen scroll-depth of CTA click events. 6 van 7 LP-KPIs konden daardoor niet ingevuld worden.
- Host bug: SKILL gebruikt `startyourballoonbusiness.com` zonder www, PostHog tagt alles als `www.startyourballoonbusiness.com`. Aangepast voor deze run, in rapport gemarkeerd voor SKILL-update.
- Top acties: campagne wel/niet heractiveren, PostHog scroll+CTA events instrumenteren, SKILL host fixen.

---

Rapport opgeslagen en gepusht naar GitHub.

**Samenvatting:** geen automatische acties uitgevoerd — beide toegankelijke accounts (`act_567892422940728`, `act_1489853856181844`) hebben 0 actieve campagnes. Alle 5 SYBB/Nozzle Up campagnes staan op `PAUSED` (laatste pause op 2026-04-19). Geen ads om tegen kill-regels te toetsen, geen 70-20-10 classificatie mogelijk.

**Belangrijkste actiepunt:** nieuwe SYBB-batch lanceren — zonder actieve campagne mist zowel `/ads-auto-optimize` als het Morning Report z'n Meta Ads voeding. Het rapport bevat ook twee secundaire punten (token-toegang `act_607231713057715`, drempel-kalibratie 70-20-10 op link metrics).

Rapport: `Output/Reports/Daily/2026-05-08_auto_optimize.md`

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 521,56 | 428 | 1 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 155,80 | 194 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 207,00 | 195 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 1.059,47** | **1036** | **1** | **0** | **EUR 0,00** | **-** | **-** |

> Wix orders: 0 orders in periode. Update `data/wix-orders.json` met orders uit Wix admin.

> **ONGEMATCHTE /thank-you SESSIES:**
> - Sessie op 2026-04-26, utm_content=(geen utm_content)
> - Sessie op 2026-04-18, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)

## 🎯 BUDGET AANBEVELINGEN (VERIFIED — OVERRULES EERDERE ADVIEZEN)

**Bron:** Wix Orders + Verified ROAS. Meta pixel purchase data wordt genegeerd voor budget beslissingen. Waar deze sectie conflicteert met adviezen elders in dit rapport, heeft DEZE sectie voorrang.

> Geen van de ads heeft verified Wix orders in de periode. GEEN budget herverdeling op basis van verified funnel mogelijk. Wacht op meer data — negeer Meta pixel 'best performer' claims tot die tijd.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
