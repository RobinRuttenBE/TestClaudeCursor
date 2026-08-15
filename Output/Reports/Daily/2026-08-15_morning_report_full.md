# Morning Report — 2026-08-15

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 15 augustus 2026

**Pipeboard is niet geautoriseerd, achtste dag op rij.** Stap 1 tot en met 4 konden niet draaien. Geen spend, impressions, CTR, CPC, CPM of ROAS. Autoriseren gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

### Er draait nog steeds niets

| Kanaal | Bezoekers | Pageviews | Aandeel |
|--------|-----------|-----------|---------|
| Direct | 2.143 | 14.848 | 66,3% |
| Referral | 566 | 6.981 | 17,5% |
| Organic Search | 418 | 7.677 | 12,9% |
| AI | 69 | 251 | 2,1% |
| Email | 18 | 130 | 0,6% |
| Organic Social | 17 | 70 | 0,5% |

**Paid Social komt niet voor. Nul.** Ook geen Paid Search. Zelfs met werkende Pipeboard-toegang krijg je een rapport over nul actieve campagnes.

Nieuw: **AI staat op 69 bezoekers**, vier keer Organic Social en bijna vier keer Email. ChatGPT alleen goed voor 17. Dat kanaal staat nergens in je tracking.

### Punt 2 van gisteren is niet uitgevoerd

`www.sempertexeurope.com` is nog steeds je grootste verwijzer: 539 bezoekers, 6.504 pageviews. Reken mee: Referral heeft 566 bezoekers totaal. **95,2% van je "verwijzend verkeer" is je eigen site.** Echt extern verwijzend verkeer is 27 bezoekers, niet 566.

Odoo staat er ook nog: 5 bezoekers, 279 pageviews, ruim 55 pagina's per bezoeker. Geen klant, wel vervuiling.

### De daling is nu definitief een meetartefact

| Metric | Laatste 7d | Vorige 7d | Verschil |
|--------|-----------|-----------|----------|
| Bezoekers | 3.040 | 6.759 | **-55,0%** |
| **Pageviews** | **29.989** | **35.723** | **-16,0%** |
| Sessies | 3.788 | 7.572 | -50,0% |
| Sessieduur | 6m21s | 3m02s | **+110,0%** |
| Bounce rate | 49,3% | 53,9% | -4,6pp |

Bezoekers min 55%, pageviews maar min 16%, duur plus 110%, bounce omlaag. Was je echt de helft van je publiek kwijt, dan waren pageviews meegezakt. Dezelfde mensen worden nu als één persoon geteld in plaats van als vijf bezoekers. **Je echte daling is ongeveer 16%, grotendeels seizoen.**

### Volgorde

1. Autoriseer Pipeboard
2. **Sluit `sempertexeurope.com`, `mollie.com`, Odoo en shipping-portal uit als verwijzer in PostHog**, vijf minuten werk
3. Conversie-events op de SYBB pagina vóór nieuw budget
4. Herwaardeer de daling pas na stap 2
5. Alles van vóór 13 juli als niet bestaand behandelen
6. UTM lowercase, komma's in `utm_content` naar underscores
7. **Nieuw:** onderzoek het AI-kanaal, 69 bezoekers zonder inspanning

Punt 2 tot en met 7 hebben Pipeboard niet nodig. Je wacht nu acht dagen op een autorisatie terwijl er zes dingen klaarliggen die je vandaag zelf kunt doen.

**Aanbeveling:** geen euro in Meta tot stap 2 en 3 staan. Hormozi 70-20-10 werkt alleen als je kunt zien welke 70% bewezen is.

Rapport staat in `Output/Reports/Daily/2026-08-15_ads_report.md`, gecommit en gepusht.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport staat in `Output/Reports/Daily/2026-08-14_sybb_report.md`, gecommit en gepusht.

**Belangrijk om te weten voor je het leest:**

De Meta Ads MCP (Pipeboard) kon ik niet gebruiken. Die connector vraagt om autorisatie en deze sessie is niet-interactief, dus de OAuth flow kan hier niet draaien. Autoriseren gaat via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Sectie 2 is daardoor leeg. Geen Google MCPs aangeraakt, niets naar de tracker Sheet geschreven.

**Wat de data wél laat zien:**

1. **De landing page is dood, niet slecht.** `startyourballoonbusiness.com` stuurde op 14 augustus nul events naar PostHog. Laatste event: 31 juli, veertien dagen eerder. Over de hele periode 16 tot 31 juli waren het 19 pageviews van 19 bezoekers, allemaal direct, geen UTM.

2. **Pipeboard is niet het echte probleem.** PostHog meet aan de ontvangende kant mee en ziet over 30 dagen nul pageviews met `utm_source=meta`, nul met `utm_medium=cpc`, nul met `utm_campaign=sybb`, op geen enkel domein. Ook met een werkende koppeling zou het antwoord zijn dat de campagne niet draait.

3. **De 47 pageviews op de SYBB event pagina's zijn intern.** Dat lijkt bijna 3x het 7-daags gemiddelde, maar het zijn 3 unieke bezoekers in 4 sessies, allemaal uit België. Eén sessie bekeek 12 taalvarianten van dezelfde registratiepagina in vier minuten. Externe SYBB vraag gisteren: nul.

4. **Vier KPI targets meten structureel niets.** Scroll depth (25/50/75/100%) en CTA clicks bestaan niet als event in de projecttaxonomie. Die zijn nooit geïmplementeerd, dus ze blijven onmeetbaar ook als de tracking morgen weer aan gaat. De funnel uit de skill is om die reden niet te bouwen, en er is geen `/booking` pad.

5. **De funnel eindigt blind.** Er is geen bevestigingsevent voor een voltooide event-registratie. De enige `confirmation` pagina's horen bij de webshop. Conversieratio is dus per definitie niet te berekenen.

**Eén ding buiten scope dat opviel:** sitebrede unieke bezoekers dalen negen dagen op rij, van 900 op 6 augustus naar 250 gisteren, 55% onder het 7-daags gemiddelde. Dat staat los van SYBB maar is het grootste signaal in de dataset. Wil je dat ik daar apart naar kijk?

---

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

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
