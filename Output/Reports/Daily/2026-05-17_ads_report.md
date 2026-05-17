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
