# Morning Report — 2026-05-15

> ⚠️ **PURCHASE DATA KON NIET GEVERIFIEERD WORDEN**
> De hardcoded sanity check kon geen purchase data ophalen uit de Meta Ads MCP (NODATA of PARSE_ERROR). Dat betekent ook geen betrouwbare link metrics.
> Dit rapport bevat mogelijk niet-gevalideerde cijfers. Behandel alle purchase getallen, ROAS en CTR/CPC als **onbetrouwbaar** tot je ze handmatig hebt geverifieerd.
> ROAS is uit voorzorg overschreven met `n.v.t. (niet geverifieerd)`.
> **Beter een false warning dan een foutieve metric die budget beslissingen beïnvloedt.**


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

De Meta Ads (Pipeboard) connectie is niet geauthenticeerd. Ik kan het rapport pas draaien als jij de toegang autoriseert.

**Actie nodig van jou:** open deze URL in je browser en log in bij Pipeboard / Meta:

https://pipeboard.co/oauth/authorize?response_type=code&client_id=730e6b319aa5472a75e25f38be1fac5e&code_challenge=W9CTImOsNRyHNwbge2cRrf2Mh4xRKefZ5lXHM5kPZqY&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A53073%2Fcallback&state=c5L4kRVOCz-sHGTsk23tCMiERuB_YfuONiqvwqPdDFM&scope=mcp%3Aread+mcp%3Awrite&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

Zodra je de flow hebt afgerond worden de Meta Ads tools automatisch actief en ga ik direct verder met:

1. Ad accounts ophalen (`act_567892422940728` primair + `act_607231713057715` checken)
2. Actieve campagnes + insights (last 30 days)
3. Ad-level data
4. Underperformers markeren (CPC >€0,50 / CTR <1% / Freq >3,5 / CPM >€15)
5. Rapport opslaan naar `Output/Reports/Daily/2026-05-15_ads_report.md` (Google Sheet stap wordt overgeslagen conform jouw instructie)

Laat het weten als de autorisatie gelukt is, of plak de volledige redirect-URL als de browser een verbindingsfout toont op de callback-pagina.

---

Klaar. Rapport gegenereerd, opgeslagen en gepusht.

## Samenvatting van de run

**Twee blokkades gevonden die het rapport grotendeels leeg maken:**

1. **Meta Ads MCP (Pipeboard) is down** — foutmelding *"Facebook connection required"*. Geen enkele data over campagne `2026: SYBB`. Herstellen via https://pipeboard.co/connections is actie #1.

2. **PostHog instrumentatie-gat** — de site capteert alleen `$pageview` (+ rageclick/dead-click). Geen `$pageleave`, dus **bounce rate, sessieduur en scroll depth zijn structureel niet meetbaar**, en er is geen CTA-click event.

**Wat PostHog wél liet zien voor www.startyourballoonbusiness.com:**
- 14 mei: **1 pageview, 1 unieke bezoeker** (via `utm_content=h11_b3_cta5`, direct op `/booking`)
- 7-daags gemiddelde: ~3,9 pageviews/dag — extreem laag, alle ratio's zijn ruis
- 12 mei piek (14 views, vooral `/review`, geen utm) = waarschijnlijk intern/review-verkeer, geen ad-traffic
- 0 rageclicks, 0 dead clicks

**Top 3 acties** (in het rapport): Meta-verbinding herstellen → `$pageleave`/scroll/CTA tracking instrumenteren → verifiëren of `2026: SYBB` live is en correct getagd (1 getagde ad-bezoeker in 7 dagen wijst op nul spend of gebroken UTM-link).

Conform je instructie: alleen Meta Ads MCP en PostHog MCP gebruikt, geen Google MCP's, niets naar de Google Sheet tracker geschreven.

Eén kanttekening bij de push: de remote meldt dat de repo verhuisd is naar `git@github.com:RobinRuttenBE/TestClaudeCursor.git`. De push slaagde nog via de redirect, maar je wilt de remote-URL waarschijnlijk bijwerken. Wil je dat ik dat doe?

---

De Meta Ads MCP (Pipeboard) is niet geauthenticeerd, dus ik kan nu geen campagne- of insights-data ophalen. Zonder die data kan ik geen kill-regels evalueren, geen 70-20-10 classificatie maken en geen rapport genereren.

**Actie nodig van jou:** open deze URL in je browser en autoriseer de Pipeboard Meta Ads connectie:

https://pipeboard.co/oauth/authorize?response_type=code&client_id=43082e481e332b59e62b2dc4cb1ca807&code_challenge=_31MDJjSGjH-xJBYMn02mCjycvXbr8EYXnwAs3BCq88&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A54044%2Fcallback&state=Jz4p4aOKSqmO140aCrsfh2KLxrbTOBRrEnypfI9CzEY&scope=mcp%3Aread+mcp%3Awrite&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

Na het autoriseren:
- Als de connectie automatisch doorkomt, zeg dat even en ik ga verder.
- Als de redirect-pagina een verbindingsfout toont (lokale poort laadt niet op een remote sessie), kopieer dan de **volledige URL uit de adresbalk** (`http://localhost:54044/callback?code=...&state=...`) en plak die hier — dan rond ik de authenticatie af.

Ik wacht op de authenticatie voordat ik verderga. Zodra Pipeboard verbonden is, draai ik de volledige flow: 3-daagse insights ophalen voor beide accounts (`act_567892422940728` primair, `act_607231713057715`), kill-regels toepassen op **Link CTR / CPC (link)**, automatische pauzes uitvoeren (Niveau 1), de 70-20-10 classificatie maken en Niveau 2 voorstellen genereren — alleen via Pipeboard en PostHog, en het rapport wegschrijven naar `Output/Reports/Daily/2026-05-15_auto_optimize.md`.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
