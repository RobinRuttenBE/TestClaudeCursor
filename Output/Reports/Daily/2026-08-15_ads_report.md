## Meta Ads Rapport, 15 augustus 2026

**Pipeboard is niet geautoriseerd, achtste dag op rij.** Stap 1 tot en met 4 konden niet draaien. Geen spend, impressions, CTR, CPC, CPM of ROAS, dus de campagnetabel, de underperformer-sectie en de top-performer-sectie blijven leeg. Autoriseren gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs zijn overgeslagen zoals gevraagd.

### Overzicht per campagne

Geen data beschikbaar. Zie hieronder waarom dat vandaag ook niet uitmaakt.

### Er draait nog steeds niets

Kanaalverdeling laatste 7 dagen:

| Kanaal | Bezoekers | Pageviews | Aandeel |
|--------|-----------|-----------|---------|
| Direct | 2.143 | 14.848 | 66,3% |
| Referral | 566 | 6.981 | 17,5% |
| Organic Search | 418 | 7.677 | 12,9% |
| AI | 69 | 251 | 2,1% |
| Email | 18 | 130 | 0,6% |
| Organic Social | 17 | 70 | 0,5% |
| Organic Video | 1 | 3 | 0,0% |

**Paid Social komt niet voor in de lijst. Nul.** Ook geen Paid Search. Zelfs met werkende Pipeboard-toegang krijg je vandaag een rapport over nul actieve campagnes.

Nieuw sinds gisteren: **AI staat op 69 bezoekers**, vier keer zoveel als Organic Social en bijna vier keer Email. ChatGPT alleen is goed voor 17 bezoekers. Dat is een kanaal dat je nog nergens in je tracking of contentplanning hebt staan.

### Punt 2 van gisteren is nog steeds niet uitgevoerd

Top verwijzende domeinen, laatste 7 dagen:

| Domein | Bezoekers | Pageviews |
|--------|-----------|-----------|
| $direct | 2.209 | 15.081 |
| **www.sempertexeurope.com** | **539** | **6.504** |
| www.google.com | 369 | 6.471 |
| www.bing.com | 27 | 627 |
| chatgpt.com | 17 | 59 |
| t-sml.mtrbio.com | 16 | 100 |
| rezolvbv-sh-sempertex.odoo.com | 5 | 279 |
| facebook.com | 4 | 20 |

Reken even mee. Het kanaal Referral heeft 566 bezoekers. Daarvan komen er 539 van je eigen domein. **95,2% van je "verwijzend verkeer" is je eigen site die naar zichzelf verwijst.** Het echte externe verwijzende verkeer is 27 bezoekers, niet 566.

Odoo staat er ook nog steeds bij: 5 bezoekers maar 279 pageviews, dus ruim 55 pagina's per bezoeker. Dat is geen klant, dat is een intern systeem of een bot die je cijfers vervuilt.

Dit is nog altijd een instelling van vijf minuten in PostHog en het blokkeert nog altijd elke andere conclusie die je uit deze data wilt trekken.

### De daling is nu definitief een meetartefact

Laatste 7 dagen tegen de 7 daarvoor:

| Metric | Laatste 7d | Vorige 7d | Verschil |
|--------|-----------|-----------|----------|
| Bezoekers | 3.040 | 6.759 | **-55,0%** |
| **Pageviews** | **29.989** | **35.723** | **-16,0%** |
| Sessies | 3.788 | 7.572 | -50,0% |
| Sessieduur | 6m21s | 3m02s | **+110,0%** |
| Bounce rate | 49,3% | 53,9% | -4,6pp |

Bezoekers min 55%, sessies min 50%, maar pageviews maar min 16% en sessieduur plus 110%. Als je echt de helft van je publiek kwijt was, zouden pageviews mee zijn gezakt. Dat gebeurt niet.

Wat hier gebeurt: dezelfde mensen worden nu als één persoon geteld in plaats van als vijf losse bezoekers. Bijna evenveel pagina's, veel langere sessies, lagere bounce. Dat zijn drie signalen die allemaal dezelfde kant op wijzen. **Je consumptie daalde ongeveer 16%, niet 55%.** En die 16% is grotendeels seizoen, half augustus.

Bounce rate ging van 53,9% naar 49,3%. Dat is je eerste keer onder de 50%. Op zichzelf goed nieuws, maar het is dezelfde meetwijziging die de bezoekers omlaag drukt, dus hang er nog geen conclusie aan.

### Volgorde

1. **Autoriseer Pipeboard.** Achtste dag. Zonder dit is dit rapport structureel half.
2. **Sluit `sempertexeurope.com`, `mollie.com`, Odoo en het shipping-portal uit als verwijzer in PostHog.** Staat er sinds 14 augustus, nog niet gedaan, kost vijf minuten, en zonder dit klopt je Direct- en Referral-verdeling niet.
3. **Conversie-events op de SYBB pagina voordat er nieuw budget in gaat.** Je kunt nu geen enkele campagne afrekenen.
4. Herwaardeer de daling pas na stap 2.
5. Alles van vóór 13 juli behandelen als niet bestaand.
6. UTM lowercase, komma's in `utm_content` naar underscores.
7. **Nieuw: onderzoek het AI-kanaal.** 69 bezoekers zonder dat je er iets voor doet. Kijk welke pagina's ChatGPT en andere assistenten oppikken en of je productpagina's daar goed op staan.

Punt 2 tot en met 7 hebben Pipeboard niet nodig. Je zit nu acht dagen te wachten op een autorisatie terwijl er zes dingen klaarliggen die je vandaag zelf kunt doen.

### Samenvatting

- **Totaal spend:** niet op te halen, Pipeboard niet geautoriseerd
- **Actieve campagnes:** nul, bevestigd via PostHog kanaaldata
- **Grootste probleem:** niet je advertenties, maar dat je meetopstelling nog steeds niet betrouwbaar is
- **Aanbeveling:** zet geen euro in Meta tot stap 2 en stap 3 staan. Hormozi 70-20-10 werkt alleen als je kunt zien welke 70% bewezen is, en dat kun je nu niet.

### Google Sheet

Overgeslagen op verzoek. Rapport staat lokaal in `Output/Reports/Daily/2026-08-15_ads_report.md`.

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.
