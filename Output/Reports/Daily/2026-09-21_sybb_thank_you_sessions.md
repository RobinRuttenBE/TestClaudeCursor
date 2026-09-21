# SYBB thank-you sessies 22 aug t/m 20 sep 2026

Run: 21 september 2026. Bron: PostHog project STX EU (149694) via directe REST route (`posthog` MCP server gaf HTTP 405, geen Google MCPs aangeroepen, niets naar Google Sheet geschreven).

## Query 1: pageviews met `$current_url LIKE '%/thank-you%'`

| visit_date | visit_time | session_id | utm_content | utm_source | country | device |
|---|---|---|---|---|---|---|
| 2026-09-20 | 08:55:31 | 01a0be07-166c-7d14-a272-ae55f528c489 | leeg | leeg | Indonesia | Desktop |
| 2026-09-20 | 08:10:54 | 01a0bdde-3701-731f-abb1-e2aeb9fe177a | leeg | leeg | Colombia | Desktop |

## Query 2: alle events per sessie (entry-UTM check)

Beide sessies bestaan uit precies 1 event, referrer `$direct`, geen UTM parameters.

- 01a0bdde-…: `https://www.sempertexeurope.com/de/thank-you/thank-you---square---18-inch---betallic-2`
- 01a0be07-…: `https://www.sempertexeurope.com/de/thank-you/thank-you---fun-type---17-inch---anagram-2`

## Conclusie

Dit zijn geen SYBB bedankpagina's maar Duitse productpagina's van "Thank You" folieballonnen in de webshop van sempertexeurope.com. Het LIKE-filter op `/thank-you` vangt die categorie mee. Het patroon (1 event, direct, 0s, Indonesia en Colombia) past bij link-preview bots of crawlers.

Aantal echte SYBB thank-you sessies in dit venster: 0. Er is geen `startyourballoonbusiness.com` pageview met `/thank-you` in de periode. Aanbeveling: filter op `properties.$current_url LIKE '%startyourballoonbusiness%thank-you%'` of op het custom conversie-event van het SYBB event/checkout traject (zie project-sybb-funnel-location memory).

## JSON output

```json
{"thank_you_sessions": [{"visit_date": "2026-09-20", "visit_time": "08:55:31", "session_id": "01a0be07-166c-7d14-a272-ae55f528c489", "utm_content": null, "utm_source": null, "country": "Indonesia", "device": "Desktop"}, {"visit_date": "2026-09-20", "visit_time": "08:10:54", "session_id": "01a0bdde-3701-731f-abb1-e2aeb9fe177a", "utm_content": null, "utm_source": null, "country": "Colombia", "device": "Desktop"}]}
```
