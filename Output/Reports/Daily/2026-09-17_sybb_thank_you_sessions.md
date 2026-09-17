# SYBB thank-you sessies, 18 augustus t/m 16 september 2026

Bron: PostHog, project STX EU (id 149694, eu.posthog.com). Er bestaat geen project "Default project" in de organisatie Sempertex Europe; de pixel van startyourballoonbusiness.com draait in STX EU.
Uitgevoerd via de claude.ai PostHog connector (execute-sql) en ter controle via de REST HogQL endpoint. Beide gaven hetzelfde resultaat.

## Query
```sql
SELECT toDate(timestamp) AS visit_date, toString(timestamp) AS visit_time, e.$session_id AS session_id,
  properties.utm_content AS utm_content, properties.utm_source AS utm_source,
  properties.$geoip_country_name AS country, properties.$device_type AS device
FROM events e
WHERE event = '$pageview' AND properties.$current_url LIKE '%/thank-you%'
  AND timestamp >= toDateTime('2026-08-18 00:00:00') AND timestamp < toDateTime('2026-09-17 00:00:00')
ORDER BY timestamp DESC
```

## Resultaat
0 rijen. Geen enkele pageview op een /thank-you URL in de periode. De tweede query (utm_content per sessie) was daarom niet nodig.

Controle in dezelfde periode:
- Pageviews op startyourballoonbusiness.com: 4 (waarvan 3 met utm_source=meta, zie memo van 17 september over link-preview hits op de oude ad-URL)
- URL's met "thank" in de tekst: 100, allemaal productpagina's en contactformulieren van foil "Thank You" ballonnen op sempertexeurope.com, geen bedankpagina

## JSON
```json
{"thank_you_sessions": []}
```
