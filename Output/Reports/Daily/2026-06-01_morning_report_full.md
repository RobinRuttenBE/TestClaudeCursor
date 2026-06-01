# Morning Report — 2026-06-01

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 1 juni 2026

**Live data niet beschikbaar.** De Pipeboard Meta Ads MCP en PostHog MCP zijn deze sessie niet online gekomen — ToolSearch vindt geen `get_campaigns`, `get_insights`, of `get_ad_accounts` tools. Geen Python/CLI fallback in `scripts/`. Ik heb dus geen verse cijfers kunnen pullen.

### Laatste bekende state (uit 2026-05-31_ads_report.md)

| Campagne | Status | Spend (lifetime) | CTR | CPC | CPM | ROAS |
|----------|--------|------------------|-----|-----|-----|------|
| 2026: SYBB | PAUSED | €2.485,04 | 4,1% | €0,21 | €8,36 | 17,8x |
| 2026: SYBB - Kopie | PAUSED | €124,42 | 2,6% | €0,64 | €16,34 | 0,0x |

Spend last_30d op 31 mei: **€0,00** — alles gepauzeerd. Tenzij sinds gisteren iets aan staat, verandert dit niet.

### Aanbeveling (onveranderd)
Reactiveer `2026: SYBB` (bewezen 70%, ROAS 17,8x). Niet schalen vóór LPV → view content drop (98%) is gediagnosticeerd — eerst pixel check, dan LP CRO.

### Acties om dit op te lossen
1. Check MCP config voor `pipeboard-meta-ads` en `posthog`, herstart de sessie zodat ze connecten.
2. Overweeg een `scripts/fetch-meta-ads.py` als CLI fallback (zoals `fetch-wix-orders.py`).

Rapport opgeslagen in `Output/Reports/Daily/2026-06-01_ads_report.md`. Geen Google Sheet write (per instructie). Geen funnel-diagnose mogelijk zonder PostHog data.

---

Done. Report saved and pushed.

## SYBB Dagrapport — 31 May 2026

Het rapport staat in `Output/Reports/Daily/2026-05-31_sybb_report.md` en is gecommit + gepusht (`11ef69a8`).

**Belangrijke uitkomst: er was niets te rapporteren, en dat is op zich het signaal.**

**Meta Ads MCP (Pipeboard)** — wél verbonden en bevraagd:
- Campagne **`2026: SYBB`** (`120239435987290239`) staat op **PAUSED** (sinds 19 April).
- **€0 spend / 0 impressions / 0 clicks** op 31 May, en lege dataset over 25–31 May.
- Ook op **accountniveau** geen enkele euro spend gisteren — de campagne levert niet uit.

**PostHog MCP** — **niet beschikbaar** in deze sessie. Er waren geen `mcp__posthog__*` tools (de server is niet verbonden). Landing page health, scroll depth, CTA-clicks en funnel drop-off ontbreken daardoor.

Conform je strikte regel heb ik **geen enkele Google-bron of GA4 als vervanging gebruikt**, en **niet** naar de Meta Ads Tracker Google Sheet geschreven.

**Top acties uit het rapport:**
1. Beslis of `2026: SYBB` weer aan moet (of bevestig dat hij bewust uit staat, zodat dit dagrapport gepauzeerd kan worden).
2. Herstel de PostHog MCP-koppeling — anders blijft de helft van dit rapport leeg.
3. Verifieer tracking op `startyourballoonbusiness.com` zodra PostHog weer werkt.

Wil je dat ik uitzoek waarom de PostHog MCP niet verbond, of de campagne bewust gepauzeerd laten en het dagrapport tijdelijk stilzetten?

Kleine noot over de push: de auto-sync op de repo liep meerdere keren tussendoor, waardoor een gewone push werd geweigerd. Je lokale `main` was flink achtergelopen op de remote (tientallen auto-sync report/log-bestanden ontbraken lokaal), wat merge-conflicten op die gegenereerde bestanden gaf. Ik heb lokaal schoon gereset naar de remote en alleen mijn rapportbestand erbovenop opnieuw toegevoegd, zodat er niets van jouw data is aangetast.

---

## Auto-Optimize Rapport — 1 June 2026

**Conclusie: er was niets te optimaliseren — het hele account staat op pauze.**

Wat ik vond in `act_567892422940728`:

| Campagne | Status | Dagbudget |
|----------|--------|-----------|
| 2026: SYBB | PAUSED | €100,00 |
| 2026: SYBB - Kopie | PAUSED | — |
| Last push Nozzle Up | PAUSED | — |
| Nozzle Up END OF AUGUST | PAUSED | €70,00 |
| Campagne Nozzle Up 2025 1 | PAUSED | €30,00 |

Alle 5 campagnes staan op PAUSED. Daardoor:

- **⚡ Niveau 1 (automatisch):** 0 ads gepauzeerd — de kill-regels (Link CTR < 0.8%, CPC (link) > €1,50) hebben geen live levering om op te triggeren.
- **📊 70-20-10:** niet van toepassing — geen actieve ads om te classificeren.
- **💡 Niveau 2 (voorstellen):** geen data-gedreven voorstellen mogelijk zonder live performance. Geen gokwerk.

Het tweede account `act_607231713057715` is niet toegankelijk met dit token (alleen `act_1489853856181844` en `act_567892422940728` toegestaan) — correct overgeslagen. PostHog was niet nodig: zonder actieve ads valt er niets te kruisen.

**Enige relevante actie:** de hoofdcampagne **2026: SYBB** (€100/dag) staat gepauzeerd sinds 19 Apr 2026. Zolang die uit staat, levert dit dagelijkse rapport geen nieuwe inzichten. Zodra je SYBB weer activeert en er ≥24 u data is, draait de volledige optimalisatie-flow weer.

Rapport opgeslagen in `Output/Reports/Daily/2026-06-01_auto_optimize.md` en gepusht naar GitHub (`9592c929`).

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
