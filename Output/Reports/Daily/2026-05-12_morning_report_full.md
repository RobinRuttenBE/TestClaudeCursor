# Morning Report — 2026-05-12

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport — 12 mei 2026

**Status: ❌ Data niet opgehaald — authenticatie-fout op Pipeboard**

Alle Meta Ads MCP calls (`get_ad_accounts`, `get_campaigns` voor beide accounts) gaven dezelfde fout:

> Facebook connection required. Connect your account at https://pipeboard.co/connections to continue.

Zonder die verbinding kunnen ad accounts, campagnes, ads en insights niet worden opgehaald, dus stappen 3-5 (insights, ad-level data, underperformers) zijn niet uitgevoerd.

### Aanbeveling
1. Open https://pipeboard.co/connections en log in met het Meta-account dat toegang heeft tot `act_567892422940728`.
2. Run `/ads-report` opnieuw zodra de verbinding hersteld is.
3. Check tussentijds in Meta Ads Manager of de SYBB campagne nog actief is en of het dagbudget niet ontspoort.

### Output
- Rapport opgeslagen op `/Users/robinrutten/TestClaudeCursor/Output/Reports/Daily/2026-05-12_ads_report.md`
- Stap 6 (Google Sheet write) overgeslagen conform run-instructie
- Geen Google MCPs aangeroepen

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
>
> _(Let op: zonder de Meta Ads spend/impressions/clicks data uit Pipeboard wordt de funnel diagnose ééenzijdig — alleen vanaf de landing page af. Volledig diagnose pas na herstel Pipeboard auth.)_

---

Rapport opgeslagen op `Output/Reports/Daily/2026-05-11_sybb_report.md`.

**Belangrijkste bevindingen 11 mei:**
- **Meta Ads MCP storing**: Pipeboard gaf vandaag "Facebook connection required" op alle calls. Geen live ad-data ophaalbaar. Token moet gereconnect worden via https://pipeboard.co/connections.
- **PostHog**: 4 pageviews, 4 sessies, 100% bounce, 0s gemiddelde duur. 22e dag paused campagne.
- **Nieuw signaal**: 2 pageviews op `/review` (een route die in de afgelopen 8 dagen niet voorkwam). Beide $direct, beide bounce, binnen 11 seconden van elkaar. Verdient een Wix-check.
- **Onveranderde meet-gap**: alleen `$pageview` en `$web_vitals` events; geen scroll/CTA tracking.

Top 3 acties: (1) Pipeboard reconnect, (2) `/review` route onderzoeken, (3) relaunch-of-stop beslissing forceren plus scroll/CTA tracking deployen vóór relaunch.

---

Rapport opgeslagen op `Output/Reports/Daily/2026-05-12_auto_optimize.md`.

**Uitkomst:**
- **BLOCKED** — Pipeboard Meta Ads MCP geeft op beide accounts (`act_567892422940728` en `act_607231713057715`) `Facebook connection required`. Geen campagne-, ad set- of ad-data opgehaald.
- **Niveau 1: 0 ads gepauzeerd** — geen data om kill-regels (Link CTR < 0,8%, CPC link > €1,50) op uit te voeren.
- **Niveau 2: geen voorstellen** — kan 70-20-10 niet classificeren zonder live performance data.

**Vereiste actie:** Reauthenticeer Pipeboard via de OAuth URL in het rapport (of via https://pipeboard.co/connections), daarna run je `/ads-auto-optimize` opnieuw. Let op: vorige run (11 mei) had ook 0 actieve campagnes — SYBB staat sinds 2026-04-19 PAUSED. Zelfs na auth-herstel kan de uitkomst nog steeds "geen levering" zijn, waarmee de heropstart-discussie de echte vraag deze week is.

Geen Google MCPs aangeroepen, niets naar de Google Sheet tracker geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
