# Morning Report — 2026-08-19

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

API Error: Can't reach the API server — check your internet or DNS (ENOTFOUND)

---

Request timed out

---

## Auto-Optimize, 19 augustus 2026

**Geen optimalisatie uitgevoerd. Nul ads gepauzeerd.** Niet omdat alles goed presteert, maar omdat er niets is om te optimaliseren.

**Pipeboard is niet geautoriseerd, twaalfde dag op rij.** Ik kon de Meta Ads MCP niet aanroepen, dus stap 1 tot en met 6 van het command konden niet draaien: geen campagnes, geen ad sets, geen ads, geen insights. Beide accounts (`act_567892422940728` en `act_607231713057715`) waren onbereikbaar. Autoriseren kan niet vanuit deze sessie omdat die non-interactief is. Het gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie.

PostHog bevestigt onafhankelijk dat er niets draait. Over 3 dagen: **nul Paid Social sessies, nul Paid Search, nul sessies met `utm_source=meta`**. Verkeer is 89,7% Direct, 5,1% Organic Search. De kill-regels hadden dus sowieso niets om op te vuren.

### Wat ik wel vond

Het botprobleem uit gisteren staat er nog. Brazilië (294), Seychellen (188), Argentinië (124) en Bangladesh (79) hebben alle vier exact 1,00 pageview per bezoeker. Samen 685 bezoekers, **14,6% van je verkeer**.

Nieuw: **Groot-Brittannië is met 1.127 bezoekers opeens 24,0% van je verkeer, op 1,44 pageviews per bezoeker.** Nederland doet 19,5, België 26,3. Dertien keer dieper. Dat is nog geen bewijs, 1,44 is niet de harde 1,00 van de andere clusters, maar het verdient een check op browser- en deviceverdeling voordat je er iets aan ophangt. Als GB ook vervuild is loopt het aandeel niet-menselijk verkeer richting 38%.

Dat telt nu omdat je op het punt staat Meta aan te zetten. Elke landingspaginavergelijking gaat straks tegen deze nulmeting af.

### Geen voorstellen

Ik doe geen budget-, variatie- of audiencevoorstellen. Die zijn allemaal afgeleid van performance data die er niet is. De volgorde van werk is ongewijzigd, want er is niets afgevinkt: botfilter → referrer exclusies → Pipeboard autoriseren → conversie events SYBB → UTM lowercase (`Pinterest` komt nu met hoofdletter binnen).

Eén punt voor als Pipeboard weer werkt: de 70-20-10 drempels in het command staan nog gemarkeerd als niet gekalibreerd voor link metrics. Die moeten opnieuw vastgesteld worden voordat er budget verschuift.

Rapport staat in `Output/Reports/Daily/2026-08-19_auto_optimize.md`, gecommit en gepusht (`8129df95`). Geen Google MCPs aangeroepen, niets naar de Tracker Sheet geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
