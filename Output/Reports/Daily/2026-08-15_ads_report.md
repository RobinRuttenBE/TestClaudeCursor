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
