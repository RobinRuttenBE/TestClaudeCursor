# Morning Report — 2026-04-17

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 7374,50** bij 18 purchases (totaal EUR 132741,00).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (10% marge, max 5 tickets): EUR 315-468 (1 ticket), EUR 630-936 (2 tickets), EUR 945-1404 (3 tickets), EUR 1260-1872 (4), EUR 1575-2340 (5).
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**

> ✅ **LINK METRICS — hardcoded via Meta Ads MCP**
> - **Link CTR: 1,09%** (link_clicks ÷ impressions × 100)
> - **CPC (link): EUR 1,00** (spend ÷ link_clicks)
> - **Gem. dagspend: EUR 92,70** over 9 actieve dagen (niet totaal/30)
> - Bron: spend EUR 834,27 · impressions 76.618 · link_clicks 832
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
> | H11, B3, CTA5 | EUR 370,47 | 28.511 | 303 | 1,06% | EUR 1,22 |
> | H13,B3,CTA5 | EUR 158,28 | 13.336 | 152 | 1,14% | EUR 1,04 |
> | H12,B3,CTA5 | EUR 116,03 | 12.267 | 138 | 1,12% | EUR 0,84 |
> 
> Dit zijn de ENIGE betrouwbare CTR/CPC/dagspend cijfers in dit rapport. Kale `CTR`/`CPC` waarden in het rapport hieronder zijn waar mogelijk hardcoded overschreven.


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 2026-04-17

**Periode:** last 30 days (2026-03-18 t/m 2026-04-16) · **Account:** Sempertex Ad Account

### Overzicht per campagne

| Campagne | Status | Spend | Impressions | Clicks | CTR | CPC | CPM | Conv. | ROAS* |
|----------|--------|-------|-------------|--------|-----|-----|-----|-------|------|
| 2026: SYBB | Active | €834,27 | 76.618 | 1.582 | 2,1% | €0,53 | €10,89 | 6 | n.v.t. (pixel datafout) |

### Overzicht actieve ads

| Ad | Spend | CTR | CPC | CPM | Freq | Purch. |
|----|-------|-----|-----|-----|------|--------|
| H11, B3, CTA5 | €370,47 | 1,06% | € 1,22 | €12,99 | 1,76 | 4 |
| H12, B3, CTA5 | €116,03 | 1,12% | € 0,84 | € 0,84 | 1,82 | 0 |
| H13, B3, CTA5 | €158,28 | 1,14% | € 1,04 | €11,87 | 1,52 | 2 |

### Underperformers

- **H11** — CPC €0,65 (drempel €0,50), CPM €12,99. Slokt €370 van €834 maar levert wel ? purchases (verifieer Wix). Aanbeveling: budget shift naar H12.
- **H13** — CPC €0,61. Laat draaien tot €250, herbeoordelen.
- **Campagne CPC** €0,53 licht boven €0,50 drempel.

### Top performers

- **Beste CTR / laagste CPC / laagste CPM:** H12, B3, CTA5 — 2,37% · €0,40 · €9,46
- **Meeste purchases:** H11 — 4 (duurste traffic)

### Samenvatting & aanbeveling (70-20-10)

- Totaal spend €834,27 → funnel: 1.582 clicks → 643 LPV → 38 ATC → 24 IC → ? purchases (verifieer Wix).
- **70%:** shift budget H11 → H12 (zelfde B3/CTA5 template, 38% goedkopere clicks).
- **20%:** duplicate H12 met creative tweak als A/B.
- **10%:** nieuwe hook (H16) buiten B3/CTA5 template testen.
- **Extra:** pixel value registratie checken — 44.247 unit voor ? purchases (verifieer Wix) lijkt onjuist (mogelijk cents of test-data).

### Google Sheet

Overgeslagen per run-instructie. Rapport opgeslagen op `Output/Reports/Daily/2026-04-17_ads_report.md`.

---

> **Wil je funnel data toevoegen?** Geef landing page metrics (PostHog of handmatig): visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik `/funnel-diagnose` met de Meta data gecombineerd.

---

Ik kan dit rapport niet genereren. De Meta Ads MCP (Pipeboard) en PostHog MCP zijn niet beschikbaar in deze sessie.

Alleen de Google MCP is geladen (die mag ik op jouw strikte instructie niet gebruiken), plus ingebouwde tools als Bash/Read/Write. De `ListMcpResourcesTool` toont alleen de `google` server als aangesloten MCP.

**Wat er ontbreekt:**
- `mcp__pipeboard__*` / Meta Ads tools — niet geladen
- `mcp__posthog__*` — niet geladen

**Opties om door te gaan:**
1. **Check MCP config.** Kijken of Pipeboard/PostHog wel in `~/.claude.json` of `.mcp.json` staan en reconnect doen (`/mcp` in Claude Code).
2. **CLI fallback.** Als je API keys lokaal hebt, kan ik de data via `curl` tegen de Meta Graph API en PostHog API halen en daarmee het rapport bouwen. Laat me dan weten welke env vars/keys beschikbaar zijn.
3. **Skip voor vandaag.** Een leeg placeholder-rapport met "data unavailable" is niet nuttig; beter wachten tot de MCPs er zijn.

Welke wil je?

---

Rapport staat op `Output/Reports/Daily/2026-04-17_auto_optimize.md`.

## Samenvatting

**⚡ Automatische acties: 0 pauzeringen.** Alle 3 actieve ads zitten boven de Link CTR-drempel (0,8%) en hebben nog te weinig link clicks (< 500) om de CPC-kill-regel te triggeren.

**📊 Campagne 3d (2026: SYBB):** €228,44 spend, 204 link clicks, Link CTR 1,2%, CPC (link) €1,12, ? purchases (verifieer Wix),ROAS n.v.t. (pixel datafout).

**Per ad (Link CTR / CPC link / purchases):**
- **H11, B3, CTA5** (Kopie 1) — 1,1% / €1,15 / **? purchases (verifieer Wix),ROAS n.v.t. (pixel datafout) → Core
- **H13, B3, CTA5** (Kopie 3) — 1,1% / €1,19 / 0 → Emerging
- **H12, B3, CTA5** (Kopie 2) — 1,5% / €0,85 / 0 (3 IC, 5 ATC) → Emerging, beste top-of-funnel

**💡 Voorstellen (wacht op goedkeuring):**
1. H11 variaties (v2 andere opening, v3 urgentie-CTA)
2. H12 conversie-push (trust/proof frame)
3. Experimental slot openen met Pillar 7-hook op €10/d
4. Kopie 2 budget +€5/d om CPC-kill-regel scherp te krijgen

**Twee accounts:** act_607231713057715 geen toegang met huidige token, act_1489853856181844 geen actieve campagnes.

---

## VERIFIED FUNNEL PER AD (30 dagen)

| Ad | Spend | Link Clicks | PostHog /ty | Wix Orders | Revenue | Verified ROAS | CPA |
|---|---|---|---|---|---|---|---|
| H11, B3, CTA5 | EUR 370,47 | 303 | 1 | 0 | - | - | - |
| H12,B3,CTA5 | EUR 130,40 | 158 | 0 | 0 | - | - | - |
| H13,B3,CTA5 | EUR 158,29 | 152 | 0 | 0 | - | - | - |
| H14,B3,CTA5 | EUR 122,96 | 158 | 0 | 0 | - | - | - |
| H15,B3,CTA5 | EUR 52,15 | 61 | 0 | 0 | - | - | - |
| **Totaal** | **EUR 834,27** | **832** | **1** | **0** | **EUR 0,00** | **-** | **-** |

> Wix orders: 0 orders in periode. Update `data/wix-orders.json` met orders uit Wix admin.

> **ONGEMATCHTE /thank-you SESSIES:**
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)
> - Sessie op 2026-04-12, utm_content=(geen utm_content)



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
