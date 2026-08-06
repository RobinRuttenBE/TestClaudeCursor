## Auto-Optimize, 6 augustus 2026

**Nul ads gepauzeerd, en dat is geen goed nieuws.** De Meta Ads MCP is niet geautoriseerd, dus de kill-regels konden helemaal niet draaien. Geen campagnes, geen ads, geen insights, geen `update_ad` calls. Autoriseren kan via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie.

Belangrijk onderscheid: "geen acties uitgevoerd" betekent hier **niet** "alles presteert goed". Zonder `actions.link_click` en `impressions` per ad is Link CTR niet te berekenen, zonder `spend` per ad geen CPC (link). Beide kill-regels draaien uitsluitend op die link-varianten, dus er viel niets te toetsen.

### Wat PostHog wel bevestigt

Er is nul betaald verkeer in de laatste 3 dagen. Geen Paid Social kanaal, geen enkele hit op `utm_source=meta` of `utm_medium=cpc`.

| Kanaal | Bezoekers | Bounce rate |
|---|---|---|
| Direct | 2.244 | 41,3% |
| Referral | 864 | 76,9% |
| Organic Search | 203 | 3,9% |
| Email | 46 | 18,8% |

De 5 bezoekers via facebook.com referrer zijn organisch, geen ads. Email presteert opnieuw ver boven gemiddeld: `workshop_tobi_promo_202608` haalt 35 bezoekers.

Dit sluit aan op vanochtend en op 4 augustus: alles PAUSED, campagne `2026: SYBB` sinds 19 april.

### Wat er eerst moet gebeuren

1. **Pipeboard autoriseren.** Dit blokkeert alles, elke dag opnieuw.
2. **Pixel op de juiste funnel** vóór je budget aanzet. SYBB loopt sinds 5 augustus via de event registratiepagina's op sempertexeurope.com, niet via de landing page waar CLAUDE.md en de skill van uitgaan.
3. **Conversiewaarde tracking fixen.** Die ROAS van 17,81x is vrijwel zeker een pixelfout. Blijft die staan, dan classificeert 70-20-10 straks ads als Core op basis van verzonnen omzet.

De 70-20-10 kalibratie-TODO staat overigens nog open: de drempels zijn nog op all-clicks gebaseerd en moeten door jou herzien worden voor link metrics.

Rapport staat in `Output/Reports/Daily/2026-08-06_auto_optimize.md`, gecommit en gepusht. Zodra Pipeboard geautoriseerd is kan deze run ongewijzigd opnieuw en levert hij wel echte beslissingen op.
