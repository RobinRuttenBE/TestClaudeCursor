# SYBB thank-you sessies (26 aug t/m 24 sep 2026)

Bron: PostHog connector (claude.ai Claude Chat Posthog), project STX EU (id 149694, eu.posthog.com). Een apart PostHog project "Default project" bestaat niet in de bereikbare organisaties (Sempertex Europe: STX EU; Ambition Avenue: Ambition Avenue). startyourballoonbusiness.com trackt in project STX EU.

Query: `$pageview` met `properties.$current_url LIKE '%/thank-you%'`, 2026-08-26 00:00 tot 2026-09-25 00:00 UTC.

## Resultaat

Geen enkele thank-you pageview op startyourballoonbusiness.com in deze periode.

De query gaf 2 treffers, beide op Duitse productpagina's van "Thank You" folieballonnen op sempertexeurope.com (geen SYBB conversies):

| datum | tijd (UTC) | session_id | url | land | device | utm_content | utm_source | pageviews in sessie | referrer |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-20 | 08:55:31 | 01a0be07-166c-7d14-a272-ae55f528c489 | /de/thank-you/thank-you---fun-type---17-inch---anagram-2 | Indonesia | Desktop | leeg | leeg | 1 | $direct |
| 2026-09-20 | 08:10:54 | 01a0bdde-3701-731f-abb1-e2aeb9fe177a | /de/thank-you/thank-you---square---18-inch---betallic-2 | Colombia | Desktop | leeg | leeg | 1 | $direct |

Tweede query (eerste pageview per sessie) leverde voor beide sessies ook geen utm_content of utm_source op: elke sessie bestaat uit precies 1 directe pageview, het patroon van link-preview bots.

## JSON output

```json
{"thank_you_sessions": []}
```
