# Morning Report — 2026-07-23

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Klaar. Rapport opgeslagen in `Output/Reports/Daily/2026-07-23_ads_report.md` en gecommit + gepusht. Alleen de Meta Ads MCP is gebruikt — geen Google MCPs, geen write naar de Tracker Sheet.

## Meta Ads Rapport — 23 juli 2026

⚠️ **Geen actieve campagnes.** Alles staat op PAUSED, €0 spend in de laatste 30 dagen. Ik heb daarom de lifetime data van de 5 meest recente gepauzeerde campagnes getoond (fallback-regel). Het genoemde tweede account `act_607231713057715` is niet toegankelijk onder deze login.

| Campagne | Spend | CTR | CPC | CPM | Aankopen | ROAS* |
|----------|-------|-----|-----|-----|----------|-------|
| 2026: SYBB | €2.485,04 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | €853,19 | 2,5% | €0,26 | €6,59 | 6 | 8,3x* |
| Last push Nozzle Up | €800,78 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | €604,03 | 1,0% | €0,17 | €1,64 | 6 | 6,4x* |
| 2026: SYBB - Kopie | €124,42 | 2,6% | €0,64 | €16,34 | 0 | 0,0x |

**Kernpunten:**
- **Beste performer:** 2026: SYBB — 4,1% CTR, €0,21 CPC, veruit het sterkste verkeer. De hooks werken.
- **Underperformers:** *SYBB - Kopie* (CPC €0,64 + CPM €16,34, 0 aankopen → schrappen) en *Nozzle Up END OF AUGUST* (CTR 1,0%, grensgeval maar economics gezond).
- **ROAS onbetrouwbaar:** €7.374/order en €1.180/order wijzen op een fout in de pixel purchase-waarde. Stuur op aantal aankopen + CPA, niet op ROAS, tot dat geverifieerd is.
- **Echte knelpunt = funnel, niet de ads:** 6.992 LP-views → 6 aankopen op de hoofdcampagne.
- **Aanbeveling (70-20-10):** bij heropstart één bewezen campagne (2026: SYBB), pixel-waarde fixen, en prioriteit op landing page conversie.

---

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4 — visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik automatisch een `/funnel-diagnose`; gezien de 6.992 LP-views → 6 aankopen is dat hier de belangrijkste analyse.

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-07-22_sybb_report.md` en is gecommit + gepusht.

## Belangrijkste bevinding: de SYBB funnel stond gisteren volledig stil

Beide databronnen bevestigen dit onafhankelijk:

- **Meta Ads** — Campagne `2026: SYBB` (ID `120239435987290239`) staat op **PAUSED** (al sinds 19 april). Nul spend, nul impressies, nul clicks op 22-07 én over de laatste 7 dagen. De Insights API gaf een lege dataset.
- **PostHog** — De landing page `www.startyourballoonbusiness.com` kreeg gisteren **0 pageviews**. De laatste bezoeker was 21 juli. Het weinige verkeer van de afgelopen week (1 tot 6 views/dag) is organisch/direct, er stond geen enkele `utm_source=meta` / `utm_campaign=sybb` hit in.

Dit is dus geen performance-probleem maar een aan/uit-probleem: er is geen instroom om te analyseren.

**Twee dingen om te weten:**
1. Er bestaat ook een `2026: SYBB - Kopie` (ID `120243293329420239`), ook PAUSED — mogelijk de bedoelde vervanger.
2. Het PostHog-project meet vooral `www.sempertexeurope.com` (5.086 pageviews gisteren, de corporate site). De SYBB landing page is een aparte, vrijwel slapende host in hetzelfde project. Het rapport filtert daarom expliciet op de SYBB-host.

**Top actie:** beslis of SYBB weer aan moet. Zo ja, activeer de campagne in Meta Ads Manager; zo nee, bevestig dat hij bewust uit staat zodat dit dagrapport geen valse alarmen blijft geven.

Zoals gevraagd: alleen Meta Ads (Pipeboard) en PostHog MCP gebruikt, geen Google-diensten, en niets naar de Google Sheet tracker geschreven.

---

Klaar. Rapport opgeslagen, gecommit en gepusht.

## Auto-Optimize Rapport — 23 juli 2026

**Resultaat: geen actieve campagnes, dus geen optimalisaties uitgevoerd.**

Wat ik vond via de Meta Ads MCP (alleen Meta Ads gebruikt, geen Google MCPs, niets naar de tracker Sheet):

| Account | Toegang | Actieve campagnes |
|---------|---------|-------------------|
| act_567892422940728 (primair) | ✅ | **0** — alle 5 campagnes staan op PAUSED |
| act_1489853856181844 | ✅ | 0 |
| act_607231713057715 | ❌ | Token heeft geen toegang |

**Twee aandachtspunten:**

1. **Alles staat op PAUSED**, inclusief `2026: SYBB` (dagbudget €100.00). Zonder live ads met impressies zijn er geen kill-regels, waarschuwingen of 70-20-10 classificatie mogelijk. Wil je SYBB weer laten lopen, dan is heractiveren de eerste stap, dat doe ik niet automatisch.
2. **Toegangsprobleem:** het account `act_607231713057715` uit het command is niet toegankelijk met de huidige Pipeboard-token. Toegestane accounts zijn `act_1489853856181844` en `act_567892422940728`. Dit account moet opnieuw geautoriseerd worden als het meegenomen moet worden.

Rapport staat in `Output/Reports/Daily/2026-07-23_auto_optimize.md`. Laat weten of je een campagne wilt heractiveren of de account-toegang wilt oplossen, dan draai ik de run opnieuw met echte data.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
