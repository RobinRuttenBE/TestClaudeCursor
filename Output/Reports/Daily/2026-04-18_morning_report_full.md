# Morning Report — 2026-04-18

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,10%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,01** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 83,72** over 11 actieve dagen (niet totaal/30)
> - Bron: spend EUR 920,88 · impressions 82.616 · link_clicks 910
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
> | H11, B3, CTA5 | EUR 436,37 | 32.892 | 355 | 1,08% | EUR 1,23 |
> | H13,B3,CTA5 | EUR 170,14 | 14.291 | 162 | 1,13% | EUR 1,05 |
> | H12,B3,CTA5 | EUR 124,88 | 12.929 | 154 | 1,19% | EUR 0,81 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 2026-04-18

**Periode:** last 30d (2026-03-19 t/m 2026-04-17) · **Account:** Sempertex (act_567892422940728)
Robin Rutten account: geen toegang met dit token. act_1489853856181844: geen actieve campagnes.

### Overzicht per campagne

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. | ROAS* |
|---|---|---|---|---|---|---|---|---|---|
| 2026: SYBB | Active | €920,88 | 82.616 | 1.721 | 2,1% | €0,54 | €11,15 | 6 | n.v.t. (pixel datafout) |

*Meta-rapporteerde purchase action_value van €44.247 is verdacht hoog (web_app_in_store_purchase waarde = €4,42). Behandel ROAS als indicatief.

### Overzicht per ad (top 6 op spend)

| Ad | Adset | Status | Spend | CTR | CPC | Freq. | Purch. |
|---|---|---|---|---|---|---|---|
| H11,B3,CTA5 | Kopie 1 | ACTIVE | €436,37 | 1,08% | € 1,23 | 1,79 | 4 |
| H13,B3,CTA5 | Kopie 3 | ACTIVE | €170,14 | 1,13% | € 1,05 | 1,55 | 2 |
| H12,B3,CTA5 | Kopie 2 | ACTIVE | €124,88 | 1,19% | € 0,81 | 1,87 | 0 |
| H14,B3,CTA5 | Batch 2 | PAUSED | €122,96 | 0,95% | € 0,78 | 1,34 | 0 |
| H15,B3,CTA5 | Kopie 4 | PAUSED | €49,83 | 1,20% | € 0,87 | 1,45 | 0 |
| H12,B3,CTA5 | Batch 2 | PAUSED | €14,37 | 1,19% | € 0,81 | 1,94 | 0 |

### Underperformers (actief)

- **H11 Kopie 1** — CPC €0,66 (>€0,50). Drager van 47% spend en 67% purchases → behouden, maar test nieuwe hook-variant om CPC te drukken.
- **H13 Kopie 3** — CPC €0,61 (>€0,50). ROAS-signaal onstabiel (n=2). Laat staan, niet opschalen.
- Geen CTR <1%, geen frequency >3,5, geen CPM >€15 onder actieve set.

### Top performers

- **Beste CTR (actief):** H12 Kopie 2 — 2,5%
- **Laagste CPC (actief):** H12 Kopie 2 — €0,39
- **Meeste purchases:** H11 Kopie 1 — 4 van 6
- **Beste CTR overall:** H12 Batch 2 (paused) — 4,7% (n=1.058, ruis)

### Samenvatting + aanbeveling (70-20-10)

- **70% bewezen:** schuif budget naar H11 Kopie 1 tot CPC <€0,55 zakt of frequency 3,0 nadert.
- **20% variatie:** H12 Kopie 2 heeft sterke klik-metrics, ? purchases (verifieer Wix) op 319 clicks en 127 LP views. Bottleneck zit op de landing page, niet in de creative — draai `/funnel-diagnose` op utm_content `h12_b3_cta5` (Kopie 2).
- **10% experiment:** reactiveer H12 Batch 2 in kleine adset (€5/dag) om te zien of 4,7% CTR op schaal houdt.

### Google Sheet
Overgeslagen op verzoek. Geen Google MCP calls gedaan.

Rapport opgeslagen: `Output/Reports/Daily/2026-04-18_ads_report.md`

---

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport opgeslagen in `Output/Reports/Daily/2026-04-17_sybb_report.md` en gepusht.

**Kernbevindingen 17 april:**
- Spend €86,54 (-15% vs 7d avg), CTR omhoog naar 2,32%, maar CPC €0,62 blijft 24% boven target
- Volledige bottom funnel stilstand: 0 ATC, 0 checkout, ? purchases (verifieer Wix) op 63 LP views (7d avg: 5,1 ATC/dag)
- **H12 is de winnaar**: CTR 4,24%, CPC €0,32 op slechts €8,84 spend; **H11 is de verliezer**: 76% van budget op CPC €0,72 zonder conversies
- LP view naar view content drop verslechterd van 83% naar 90%

**PostHog MCP nog steeds niet beschikbaar** (2 dagen op rij). Top actie 3 is dit herstellen vóór volgende run.

---

Klaar. Rapport opgeslagen naar `Output/Reports/Daily/2026-04-18_auto_optimize.md`.

**Samenvatting:**
- **Niveau 1 (automatisch):** 0 ads gepauzeerd. Alle 3 actieve ads passeren de kill-regels op link metrics. Geen ad heeft 500+ link clicks dus de CPC-regel is niet getriggerd.
- **Performance highlight:** CampagneROAS n.v.t. (pixel datafout) (€1.473,50 omzet op €219,11 spend in 3d). H11 is de winner metROAS n.v.t. (pixel datafout).
- **Niveau 2 voorstellen** (wachten op goedkeuring): (1) campagnebudget €100→€150/dag, (2) variaties op H12-hook (hoogste Link CTR 1,83%) en H11-hook, (3) geen audience-wijzigingen nodig, (4) overweging ad set consolidatie.
- **Compliance:** alleen Pipeboard Meta Ads MCP gebruikt. Geen Google MCPs aangesproken. Niet naar Google Sheet tracker geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 436,37 | 355 | 0 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 139,25 | 174 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 170,15 | 162 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 920,88** | **910** | **0** | **0** | **EUR 0,00** | **-** | **-** |

> Wix orders: 0 orders in periode. Update `data/wix-orders.json` met orders uit Wix admin.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
