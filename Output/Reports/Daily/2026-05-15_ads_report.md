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
