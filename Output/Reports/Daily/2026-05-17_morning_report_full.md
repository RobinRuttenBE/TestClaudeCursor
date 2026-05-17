# Morning Report — 2026-05-17

> ⚠️ **PURCHASE DATA KON NIET GEVERIFIEERD WORDEN**
> De hardcoded sanity check kon geen purchase data ophalen uit de Meta Ads MCP (NODATA of PARSE_ERROR). Dat betekent ook geen betrouwbare link metrics.
> Dit rapport bevat mogelijk niet-gevalideerde cijfers. Behandel alle purchase getallen, ROAS en CTR/CPC als **onbetrouwbaar** tot je ze handmatig hebt geverifieerd.
> ROAS is uit voorzorg overschreven met `n.v.t. (niet geverifieerd)`.
> **Beter een false warning dan een foutieve metric die budget beslissingen beïnvloedt.**


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Om het Meta Ads rapport te genereren heb ik toegang nodig tot de Pipeboard Meta Ads MCP, maar die vereist eerst authenticatie. Er zijn twee Pipeboard servers geconfigureerd; kies één van deze opties:

**Optie A — claude.ai connector (aanbevolen, simpelst):**
Typ `/mcp` en selecteer **"claude.ai Pipeboard Meta Ads"** om te authenticeren.

**Optie B — OAuth URL:**
Open deze URL in je browser en autoriseer:

```
https://pipeboard.co/oauth/authorize?response_type=code&client_id=d4852bf1f5dc1dabb2c094e4ac494d05&code_challenge=KG4ejvtyGVCc6eAkycP2w7iOiQ2rePOpOjUfb6zKE-s&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A62346%2Fcallback&state=n8j1LRqFvwZyXjT_8J9sfZsCRAqGvPm9QgBJgUHPiGw&scope=mcp%3Aread+mcp%3Awrite&resource=https%3A%2F%2Fmcp.pipeboard.co%2F
```

Als de redirect-pagina een verbindingsfout toont (normaal in een remote sessie), kopieer dan de volledige URL uit de adresbalk en plak die hier — dan rond ik de authenticatie af.

Zodra de authenticatie klaar is, ga ik direct verder met:
1. Ad accounts ophalen (`act_567892422940728` Sempertex + `act_607231713057715` Robin Rutten)
2. Actieve campagnes + insights (last 30 days)
3. Ad-level performance + underperformer flags
4. Rapport opslaan naar `Output/Reports/Daily/2026-05-17_ads_report.md` (Google Sheet stap wordt overgeslagen conform je instructie)

Laat me weten zodra je geautoriseerd bent, dan pak ik het op.

---

I've got all the PostHog data. The Meta Ads connection still needs your authorisation before I can pull campaign data.

**Please open the authorisation URL I shared above in your browser.** When the redirect page loads (or shows a connection error), copy the **full URL from the address bar** and paste it here so I can complete the connection.

While you do that, here's what PostHog shows for **www.startyourballoonbusiness.com** (yesterday, 16 May 2026):

- **7 pageviews, 4 unique visitors** (7d avg ≈ 4 pv / 3 visitors) — traffic is very low
- **Bounce rate 83.3%** (7d avg ≈ 91%) — far above the <55% target 🔴
- **Avg session duration 266s** (7d avg ≈ 71s) — above the >90s target 🟢
- **utm_content breakdown:** `bio_link` (3 pv / 3 visitors), direct/no-tag (4 pv / 1 visitor) — **zero paid SYBB ad-variant traffic** hit the page
- No rage clicks, dead clicks or exceptions

⚠️ One thing to flag now: this PostHog project **does not capture scroll-depth or CTA-click events** (only `$pageview`, `$rageclick`, `$dead_click`, `$web_vitals`). So the report's Scroll Depth, Funnel Drop-off and CTA Click Rate sections can't be filled from real data — I'll mark them explicitly as "not tracked" rather than invent numbers.

Once you paste the callback URL I'll pull the Meta Ads data for "2026: SYBB" and write the combined report.

---

The Meta Ads MCP server needs to be authenticated before I can pull any campaign data. The `/ads-auto-optimize` command depends entirely on live Pipeboard data — without it I cannot fetch insights, evaluate kill-rules, or pause underperformers.

**Actie vereist — kies één van beide:**

1. **Aanbevolen:** Voer `/mcp` uit en selecteer **"claude.ai Pipeboard Meta Ads"** om te authenticeren.
2. **Alternatief:** Open deze URL in je browser om de `pipeboard-meta-ads` server te autoriseren:

   ```
   https://pipeboard.co/oauth/authorize?response_type=code&client_id=ec4e5e3b755cfce2ed7b7543e97cf0be&code_challenge=oDJ6v6yysxW2N_MQL3dvR_GPFf9bjKQyK4Q7GqS4Q6I&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A61387%2Fcallback&state=dO-C50Cdy90cwwmz7KfO2-3fZq3n8_QRDtc149Xq7wA&scope=mcp%3Aread+mcp%3Awrite&resource=https%3A%2F%2Fmcp.pipeboard.co%2F
   ```

   Als de redirect-pagina een verbindingsfout toont, plak de volledige URL uit de adresbalk hier zodat ik `complete_authentication` kan aanroepen.

Zodra de authenticatie rond is, hervat ik automatisch:
- 3 dagen performance data ophalen voor `act_567892422940728` en `act_607231713057715`
- Kill-regels toepassen (Link CTR < 0.8%, CPC link > €1.50) en underperformers pauzeren
- 70-20-10 classificatie + budget/variatie/audience voorstellen
- Rapport opslaan naar `Output/Reports/Daily/2026-05-17_auto_optimize.md`

Ik houd me strikt aan de regel: **alleen Meta Ads MCP en PostHog MCP, geen Google MCPs, niet naar de Google Sheet schrijven.**

Laat me weten zodra je geauthenticeerd bent, of plak de callback-URL.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
