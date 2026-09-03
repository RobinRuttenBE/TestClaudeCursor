# Thank-you pageviews 2026-08-04 t/m 2026-09-02 (PostHog project STX EU, id 149694)

Bron: PostHog MCP, HogQL op `events` waar `$current_url LIKE '%/thank-you%'`.

Context:
- Er bestaat geen PostHog project "Default project" in de organisatie Sempertex Europe. Enige project is STX EU (149694). Query is daarop uitgevoerd.
- www.startyourballoonbusiness.com had in deze periode 4 pageviews in dit project, geen enkele op een /thank-you pagina.
- De 3 gevonden thank-you pageviews zijn productpagina's op www.sempertexeurope.com (folieballonnen "Thank You"), geen SYBB conversies.
- Alle 3 sessies: geen UTM parameters op de thank-you view en ook niet op de eerste pageview van de sessie (referrer $direct).

```json
{"thank_you_sessions": [{"visit_date": "2026-08-08", "visit_time": "09:34:34", "session_id": "019fe0b9-6480-76a5-83a4-c73e912a2f3b", "utm_content": null, "utm_source": null, "country": "Germany", "device": "Desktop"}, {"visit_date": "2026-08-07", "visit_time": "09:06:16", "session_id": "019fdb79-1dac-7fee-8ca4-e1656399f192", "utm_content": null, "utm_source": null, "country": "Germany", "device": "Desktop"}, {"visit_date": "2026-08-04", "visit_time": "19:59:59", "session_id": "019fce5c-717f-7481-bea7-e8ecebc2fadb", "utm_content": null, "utm_source": null, "country": "Germany", "device": "Desktop"}]}
```
