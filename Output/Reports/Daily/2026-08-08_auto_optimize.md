## Auto-Optimize, 8 augustus 2026

**De run is niet uitgevoerd. Nul ads gepauzeerd, en dat is een blokkade, geen goedkeuring.**

De Pipeboard connector is opnieuw niet geautoriseerd, derde dag op rij. Zonder `actions.link_click`, `impressions` en `spend` op ad niveau zijn de kill-regels niet te evalueren. Lees dit dus niet als "alles presteert boven de drempelwaarden".

### Wat PostHog wel bevestigt, en dat verandert de prioriteit

**Er is geen betaald verkeer.** Over 5 tot 8 augustus bestaat het kanaal Paid Social niet in de data, en op UTM niveau staat er geen enkele `meta / cpc` regel.

| Kanaal | Bezoekers | Bounce rate |
|--------|-----------|-------------|
| Direct | 2.053 | 66,3% |
| Referral | 544 | 66,8% |
| Organic Search | 214 | 4,7% |
| Email | 50 | 25,0% |
| **Paid Social** | **0** | n.v.t. |

Er valt dus waarschijnlijk niets te pauzeren omdat er niets draait. De vraag is niet welke ad je stopt, maar wanneer je herstart.

Eén kanttekening die ik niet kan wegnemen zonder Meta data: als er ads liepen met kapotte UTM tags, komen die als Direct binnen. Direct staat op 71,1% met 66,3% bounce, wat hoog is. Sterk signaal, geen bewijs.

### Waar ik geen voorstellen op doe

Budget herverdeling, nieuwe variaties en audience aanpassingen heb ik overgeslagen. Elk concreet bedrag zou verzonnen zijn zonder ad data. Wat er wel toe doet:

1. Autoriseer Pipeboard, dit blokkeert alles
2. Bevestig of er campagnes actief zijn, PostHog zegt van niet sinds 1 juli
3. Fix de UTM casing vóór herstart, `META/cpc/SYBB` splitst nu 14% van je verkeer af
4. Kalibreer de 70-20-10 drempels voor link metrics, die TODO staat nog open in het command en classificeert nu te streng
5. Zet conversie events op de SYBB pagina, de pixel meet alleen pageviews

Geen Google MCPs aangeroepen, niets naar de Tracker Sheet geschreven. Rapport staat in `Output/Reports/Daily/2026-08-08_auto_optimize.md`, gecommit en gepusht.
