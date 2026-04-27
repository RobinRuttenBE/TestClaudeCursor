Ik kan het rapport niet draaien zonder live data. De Pipeboard Meta Ads MCP vereist eerst OAuth, en de PostHog MCP-tools zijn niet beschikbaar in deze sessie.

**Wat is nodig om door te gaan:**

1. Open deze URL in je browser om de Meta Ads MCP te autoriseren:

   https://pipeboard.co/oauth/authorize?response_type=code&client_id=0ec17ee6fb82e56ac95edf588a15adcf&code_challenge=WPGZ2zDfnOT7EDoOkGdJ7c2vjLL5DBd4O_8nyLTxfTo&code_challenge_method=S256&redirect_uri=http%3A%2F%2Flocalhost%3A50726%2Fcallback&state=jtSABpZZkg82p71ichKC-I1tBdBFuGw1G55OObj2hoc&scope=mcp%3Aread+mcp%3Awrite+mcp%3Aadmin+claudeai&resource=https%3A%2F%2Fmcp.pipeboard.co%2F

2. Als de redirect-pagina niet laadt, plak de volledige `localhost:50726/callback?code=...&state=...` URL hier zodat ik `complete_authentication` kan callen.

3. Voor PostHog cross-referencing: de PostHog MCP staat niet in de deferred tools-lijst van deze sessie. Wil je dat ik het rapport draai op alleen Meta Ads data (zonder PostHog), of moet de PostHog MCP eerst opnieuw geconnect worden?

**Context (gisteren 2026-04-26):** Geen ACTIVE campagnes — alle 5 campagnes op `act_567892422940728` stonden PAUSED, met `2026: SYBB` als grootste spender (€1.059 over 30d, CPC €0,55, 6 purchases). Ik kan dat snapshot niet hergebruiken voor vandaag, dus zonder live auth kan ik geen vers rapport schrijven.

Wat wil je dat ik doe — wachten op OAuth, of het laatste snapshot van 26-04 als referentie kopiëren naar de vandaag-bestandsnaam?
