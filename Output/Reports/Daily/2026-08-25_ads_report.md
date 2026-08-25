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
