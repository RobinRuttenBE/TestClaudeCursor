De Meta Ads MCP (Pipeboard) is niet geauthenticeerd, dus ik kan nu geen campagne- of insights-data ophalen. Zonder die data kan ik geen kill-regels evalueren, geen 70-20-10 classificatie maken en geen rapport genereren.

**Actie nodig van jou:** open deze URL in je browser en autoriseer de Pipeboard Meta Ads connectie:

https://pipeboard.co/oauth/authorize?response_type=code&client_id=43082e481e332b59e62b2dc4cb1ca807&code_challenge=_31MDJjSGjH-xJBYMn02mCjycvXbr8EYXnwAs3BCq88&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A54044%2Fcallback&state=Jz4p4aOKSqmO140aCrsfh2KLxrbTOBRrEnypfI9CzEY&scope=mcp%3Aread+mcp%3Awrite&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

Na het autoriseren:
- Als de connectie automatisch doorkomt, zeg dat even en ik ga verder.
- Als de redirect-pagina een verbindingsfout toont (lokale poort laadt niet op een remote sessie), kopieer dan de **volledige URL uit de adresbalk** (`http://localhost:54044/callback?code=...&state=...`) en plak die hier — dan rond ik de authenticatie af.

Ik wacht op de authenticatie voordat ik verderga. Zodra Pipeboard verbonden is, draai ik de volledige flow: 3-daagse insights ophalen voor beide accounts (`act_567892422940728` primair, `act_607231713057715`), kill-regels toepassen op **Link CTR / CPC (link)**, automatische pauzes uitvoeren (Niveau 1), de 70-20-10 classificatie maken en Niveau 2 voorstellen genereren — alleen via Pipeboard en PostHog, en het rapport wegschrijven naar `Output/Reports/Daily/2026-05-15_auto_optimize.md`.
