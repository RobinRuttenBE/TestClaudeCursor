# Morning Report — 2026-08-25

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-08-25_ads_report.md` en is gecommit en gepusht. De Pipeboard MCP meldde "requires authentication", maar de data was gewoon bereikbaar via de directe JSON-RPC route, dus het rapport is volledig. Geen enkele Google MCP aangeroepen, stap 6 overgeslagen zoals gevraagd.

## Meta Ads Rapport, 25 augustus 2026

**Belangrijkste bevinding: er lopen geen actieve campagnes en er is €0,00 spend in de laatste 30 dagen.** Alle 5 campagnes op het Sempertex Ad Account staan op PAUSED, de meest recente ("2026: SYBB") al sinds 19 april. Het account staat dus 4 maanden volledig stil. Hieronder de lifetime cijfers als referentie.

### Overzicht (lifetime, gesorteerd op spend)

| Campagne | Spend | CTR | CPC | CPM | Purchases | ROAS |
|----------|-------|-----|-----|-----|-----------|------|
| 2026: SYBB | €2.485,04 | 4,1% | €0,21 | €8,36 | 6 | 17,8x* |
| Campagne Nozzle Up 2025 1 | €853,19 | 2,5% | €0,26 | €6,59 | 6 | 8,3x |
| Last push Nozzle Up | €800,78 | 2,5% | €0,29 | €7,29 | 3 | 0,8x |
| Nozzle Up END OF AUGUST | €604,03 | 1,0% | €0,17 | €1,64 | 6 | 6,4x |
| 2026: SYBB - Kopie | €124,42 | 2,6% | €0,64 | €16,34 | 0 | n.v.t. |

\* De SYBB purchase value is €44.247 op 6 purchases, ruim €7.000 per purchase. Dat past niet bij workshop tickets en wijst op B2B webshoporders die via de pixel aan de campagne zijn toegeschreven. Vertrouw deze ROAS niet zonder handmatige check in Ads Manager.

### Kernpunten

- **Top performer:** ad H13,B3,CTA5 in de eerste adset van SYBB: 9,8% CTR en €0,07 CPC op €421 spend. H15 (4,3% CTR, €0,15 CPC) is de runner-up.
- **Structureel probleem gevonden:** de tweede adset van SYBB was voor identieke creatives 2 tot 3x duurder per click (€0,40 tot €0,67 tegenover €0,07 tot €0,31). Die targeting niet hergebruiken.
- **Underperformers:** "2026: SYBB - Kopie" (CPC €0,64, CPM €16,34, nul conversies) en "Last push Nozzle Up" (ROAS 0,8x, de enige verlieslatende campagne).
- **Aanbeveling (70-20-10):** bij herstart 70% budget naar bewezen winnaars H13 en H15 in adset 1 targeting, 20% naar H13-varianten, 10% experimenten. En eerst de pixel purchase-attributie fixen voordat ROAS een stuurmetric wordt.

Twee kanttekeningen bij het command zelf: account act_607231713057715 (Robin Rutten) bestaat niet in Pipeboard (bevestigt mijn eerdere notitie), en het tweede account (AmbitionAvenue) is leeg.

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.** Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik er een volledige funnel-diagnose overheen.

---

Het rapport staat in `Output/Reports/Daily/2026-08-24_sybb_report.md` en is gecommit en gepusht. De kernboodschap: er is gisteren niets uitgegeven aan ads, en het echte SYBB signaal zit op een andere plek dan de skill aanneemt.

**Belangrijkste bevindingen:**

1. **Meta Ads: nul delivery.** De campagne "2026: SYBB" staat sinds 19 april op PAUSED, en ook accountbreed (act_567892422940728) was er de hele afgelopen week geen spend, geen impressies, geen clicks. De ad-variant tabel (h11 t/m h15) is daardoor leeg. De Pipeboard MCP meldde "requires authentication", maar via de opgeslagen directe JSON-RPC procedure kon ik de data gewoon ophalen.

2. **Landing page: geen data.** PostHog bevat alleen verkeer voor www.sempertexeurope.com. Startyourballoonbusiness.com krijgt sinds eind juli nul bezoekers, en scroll depth, CTA clicks en UTM properties bestaan niet in de projecttaxonomie. De LP Health sectie is dus eerlijk gerapporteerd als "geen data" in plaats van met verzonnen nullen.

3. **Het echte SYBB signaal:** de organische event-registratiepagina's op sempertexeurope.com deden gisteren 13 pageviews van 10 unieke bezoekers, de beste dag van de week (7d gemiddelde: 7,9 pageviews per dag). Conversie is niet te berekenen omdat er geen registratie-voltooid event bestaat.

4. **Extra rode vlag:** de hoofdsite had gisteren een opvallende piek: 4.638 bezoekers (2,4x normaal) met 87% bounce en een gehalveerde sessieduur. Dat ruikt naar botverkeer of een bron-mismatch en staat als check-actie in het rapport.

**Top 3 acties in het rapport:** beslissen over reactivatie van de campagne of ombouw van het rapport naar de event funnel, een registratie-conversie-event toevoegen aan de `/event/*/register` pagina's, en de bounce-piek van gisteren onderzoeken.

Er is uitsluitend gebruikgemaakt van Pipeboard (Meta Ads) en PostHog; geen enkele Google MCP is aangeroepen en er is niets naar de Google Sheet tracker geschreven. Overweging voor later: de skill `skills/daily-sybb-report/SKILL.md` aanpassen aan de werkelijke funnel, want in de huidige vorm meet die een stilstaande pagina.

---

Klaar. De auto-optimize run is uitgevoerd, maar er viel niets te optimaliseren: **alle 5 campagnes in het Sempertex account (act_567892422940728) staan op PAUSED en er was nul delivery in de afgelopen 3 dagen** (geen spend, geen impressions). Dat sluit aan bij het SYBB rapport van gisteren dat ook al geen ad delivery meldde.

Wat er is gebeurd:

- **0 ads gepauzeerd, 0 waarschuwingen, geen 70-20-10 classificatie.** Zonder actieve ads zijn de kill-regels en budgetanalyse niet van toepassing.
- De Pipeboard MCP meldde "requires authentication", maar de data was gewoon bereikbaar via directe JSON-RPC calls (bekende workaround uit memory).
- Het rapport staat in `Output/Reports/Daily/2026-08-25_auto_optimize.md` en is gecommit en gepusht (commit `6933ae28`). Geen Google services aangeraakt, conform de run-instructie.

Twee beslispunten voor jou:

1. **Wil je SYBB weer laten draaien?** Er staan twee kandidaten klaar: "2026: SYBB" (dagbudget EUR 100,00) en "2026: SYBB - Kopie". Zolang alles gepauseerd blijft, levert deze dagelijkse run lege rapporten op.
2. **Command opschonen:** het /ads-auto-optimize command verwijst naar account act_607231713057715, maar de token heeft daar geen toegang toe (toegestaan zijn alleen act_567892422940728 en act_1489853856181844, die laatste is leeg). Dat account kan uit het command.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
