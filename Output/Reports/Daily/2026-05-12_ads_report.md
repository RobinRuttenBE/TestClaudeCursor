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
