## Auto-Optimize Rapport, 15 augustus 2026

**Niveau 1 acties: 0 uitgevoerd. Niet omdat alles goed presteert, maar omdat er geen data is.**

De Pipeboard Meta Ads MCP is niet geautoriseerd, achtste dag op rij, en deze sessie is niet interactief dus de OAuth-flow kan hier niet draaien. Stap 1 tot en met 5 van het command konden niet draaien: geen impressions, geen link clicks, geen spend, dus geen kill-regels, geen 70-20-10 classificatie en geen budgetberekening. Autoriseren gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie.

### Wat PostHog wel laat zien (3 dagen)

841 bezoekers, 12.441 pageviews, 1.106 sessies, bounce 24,6%, gemiddelde sessieduur 8m38s.

| Kanaal | Bezoekers | Aandeel |
|--------|-----------|---------|
| Direct | 514 | 56,2% |
| Referral | 187 | 20,4% |
| Organic Search | 173 | 18,9% |
| AI | 27 | 3,0% |
| Organic Social | 10 | 1,1% |
| Email | 4 | 0,4% |

**Paid Social en Paid Search komen niet voor.** Van de twintig grootste bronnen heeft er precies nul een `utm_source`, `utm_medium` of `utm_campaign`. Alles staat op `(none)`. Zelfs met werkende Pipeboard-toegang zou dit rapport over nul actieve ads gaan.

Self-referral is onveranderd: 179 van de 187 Referral-bezoekers komt van `www.sempertexeurope.com`, dus 95,7%. Echt extern verwijzend verkeer is 8 bezoekers over drie dagen. Odoo en Mollie staan er ook nog in. Dat was punt 2 van gisteren.

ChatGPT levert 28 bezoekers, bijna drie keer Organic Social en zeven keer Email.

### Voorstellen (wachten op goedkeuring)

1. Autoriseer Pipeboard, de enige actie die dit command deblokkeert
2. Sluit `sempertexeurope.com`, Odoo, Mollie en de shipping-portal uit als verwijzer in PostHog, vijf minuten
3. Conversie-events op de SYBB event pagina's, zonder ROAS werkt 70-20-10 niet
4. UTM-conventie fixen vóór er verkeer komt, lowercase en underscores
5. Onderzoek het AI-kanaal

Voorstel 2 tot en met 5 hebben Pipeboard niet nodig.

Rapport staat in `Output/Reports/Daily/2026-08-15_auto_optimize.md`, gecommit en gepusht. Geen Google MCPs aangeroepen, niets naar de tracker Sheet geschreven.

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**
