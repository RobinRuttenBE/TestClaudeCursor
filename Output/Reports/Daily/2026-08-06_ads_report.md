# Meta Ads Rapport, 6 augustus 2026

**Status: geen live Meta Ads data beschikbaar.** De Pipeboard Meta Ads MCP is in deze sessie niet geautoriseerd, dus stappen 1 tot en met 4 van `/ads-report` konden niet draaien. Wat hieronder staat is PostHog data die ik wel kon ophalen, plus een expliciet gemarkeerde historische referentie.

Stap 6 (Google Sheet write) is volledig overgeslagen zoals gevraagd. Geen enkele Google MCP is aangeroepen.

---

## 1. Wat niet gelukt is

| Onderdeel | Status | Oorzaak |
|-----------|--------|---------|
| Ad accounts ophalen | Mislukt | Pipeboard MCP niet geautoriseerd |
| Campagnes (ACTIVE/PAUSED) | Mislukt | idem |
| Campagne insights (spend, CTR, CPC, CPM, ROAS) | Mislukt | idem |
| Ad-level insights | Mislukt | idem |
| PostHog landing page data | Gelukt | |

De connector "claude.ai Pipeboard Meta Ads" vraagt om een OAuth flow die in deze non-interactieve sessie niet kan draaien. Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Tot dat gebeurt is er geen live spend, CTR, CPC of ROAS beschikbaar.

---

## 2. Indirect bewijs uit PostHog: er draait niets

Ik kan de ad-status niet direct lezen, maar PostHog geeft wel een onafhankelijke bevestiging. In de laatste 30 dagen is er **nul betaald verkeer** op sempertexeurope.com.

**Kanaalverdeling, laatste 30 dagen (13.844 bezoekers)**

| Kanaal | Bezoekers | Aandeel | Bounce rate |
|--------|-----------|---------|-------------|
| Direct | 9.870 | 68,1% | 60,9% |
| Referral | 2.788 | 19,2% | 63,5% |
| Organic Search | 1.281 | 8,8% | 5,1% |
| Email | 298 | 2,1% | 17,8% |
| AI | 162 | 1,1% | 16,7% |
| Organic Social | 94 | 0,6% | 17,8% |
| Organic Video | 3 | 0,0% | 0,0% |

Er is geen enkele rij "Paid Search" of "Paid Social". In de UTM breakdown staat geen enkele hit op `utm_source=meta` of `utm_medium=cpc`. Dat is consistent met de laatste geverifieerde meting van 4 augustus: alle 5 campagnes op PAUSED, laatste uitgave april 2026.

**Conclusie:** het account ligt vrijwel zeker nog steeds stil. Dat kan ik pas hard bevestigen als de Pipeboard connector werkt.

---

## 3. Landing page performance, laatste 30 dagen

| Metric | Waarde | Target 30d | Oordeel |
|--------|--------|-----------|---------|
| Bezoekers | 13.844 | n.v.t. | |
| Pageviews | 90.089 | n.v.t. | |
| Sessies | 16.732 | n.v.t. | |
| Gem. sessieduur | 288,6s (4m49s) | >90s | Ruim gehaald |
| Bounce rate | 54,5% | <55% | Net gehaald |

De periode-op-periode vergelijking die PostHog teruggeeft (+32.862% bezoekers) is **niet bruikbaar**. De vorige periode telde maar 42 bezoekers, wat betekent dat de tracking ongeveer een maand geleden pas live ging. Vanaf volgende maand is de vergelijking wel betekenisvol.

### Getagde campagnes die wel verkeer brachten

| Campagne | Bezoekers | Pageviews | Bounce rate |
|----------|-----------|-----------|-------------|
| mailjet / email / inspiration_promo_202607 | 136 | 293 | 15,2% |
| Klaviyo / email / (none) | 107 | 174 | 22,5% |
| mailjet / email / workshop_tobi_promo_202608 | 35 | 63 | 22,2% |

Email is op dit moment het enige actieve betaalde-achtige kanaal, en het presteert goed. Bounce rate van 15,2% tot 22,5% tegenover 54,5% site-breed. Dat verkeer is drie keer zo betrokken als gemiddeld.

Twee kanttekeningen. De Klaviyo rij heeft geen `utm_campaign`, dus die 107 bezoekers zijn niet toewijsbaar aan een specifieke mail. En `inspiration_promo_202607` is een juli campagne die in augustus nog steeds verkeer levert, wat suggereert dat de mail nog wordt doorgeklikt of ergens gedeeld is.

### Opvallend: AI verkeer

162 bezoekers kwamen binnen via AI assistenten, waarvan 158 via chatgpt.com, met een bounce rate van 16,7%. Dat is meer verkeer dan Organic Social (94) en het converteert beter dan bijna elk ander kanaal. Klein maar de moeite waard om in de gaten te houden.

---

## 4. Blokkade gevonden: SYBB wordt niet gemeten

Bij het ophalen van de landing page data liep ik tegen iets aan dat losstaat van de Meta Ads storing.

`CLAUDE.md` en de SYBB skill gaan ervan uit dat PostHog de site **startyourballoonbusiness.com** meet. Dat klopt niet. Dit is de enige PostHog organisatie en het enige project (STX EU, id 149694), en de hosts die daadwerkelijk data sturen zijn:

- `www.sempertexeurope.com`
- `rezolvbv-sh-sempertex.odoo.com`

**startyourballoonbusiness.com staat er niet tussen.** Er is dus op dit moment geen PostHog meting op de SYBB landingspagina. Alle SYBB KPI targets uit `CLAUDE.md` (LP bounce rate, scroll depth, CTA click rate, conversie) kunnen niet gemeten worden zolang dit zo staat.

Dat is belangrijker dan het lijkt. Uit het rapport van 4 augustus bleek dat SYBB 0,5% van bezoeker naar checkout converteerde tegenover 19,0% bij Nozzle Up. Precies die pagina is nu blind. Als je het budget weer aanzet zonder de pixel op SYBB, kun je opnieuw niet zien waar het verkeer verdampt.

---

## 5. Laatste geverifieerde ads data (historisch, 4 augustus 2026)

Ter referentie, niet als actuele meting. Deze cijfers komen uit `2026-08-04_ads_report.md` en gaan over de laatste 30 dagen vóór die datum.

| Campagne | Spend | CTR | CPC | CPM | Aankopen | ROAS |
|----------|-------|-----|-----|-----|----------|------|
| 2026: SYBB | €2.485,04 | 4,1% | €0,21 | €8,36 | 6 | 17,81x (verdacht) |
| Campagne Nozzle Up 2025 1 | €853,19 | 2,5% | €0,26 | €6,59 | 6 | 8,30x |
| Last push Nozzle Up | €800,78 | 2,5% | €0,29 | €7,29 | 3 | 0,78x |
| Nozzle Up END OF AUGUST | €604,03 | 1,0% | €0,17 | €1,64 | 6 | 6,37x |
| 2026: SYBB, Kopie | €124,42 | 2,6% | €0,64 | €16,34 | 0 | 0,00x |

De openstaande punten uit dat rapport staan nog steeds open: de SYBB ROAS van 17,81x is vrijwel zeker een pixelfout (€42.773,50 van de €44.247 kwam uit 2 aankopen op één ad, dus €21.386 per aankoop op een starter landingspagina), en `act_607231713057715` was niet toegankelijk met de Pipeboard token.

---

## 6. Aanbevelingen

Op volgorde van wat je eerst moet doen.

**1. Autoriseer de Pipeboard connector.** Zonder die verbinding is `/ads-report` een leeg rapport en draait ook de morning report automation blind op de Meta kant. Dit blokkeert alles hieronder.

**2. Zet de PostHog pixel op startyourballoonbusiness.com.** Dit is de stille blokkade. Doe dit vóór je budget aanzet, niet erna. Anders herhaal je de situatie waarin ads goed presteren en je niet kunt zien waarom de pagina niet converteert.

**3. Fix de conversiewaarde tracking.** Op een ROAS van 17,81x kun je niet sturen, en Meta optimaliseert zelf ook op die ruis. Zolang dit niet klopt is elke budgetbeslissing een gok.

**4. Pas daarna herstarten volgens 70-20-10.** 70% op H13 (9,8% CTR, €0,07 CPC) en H11, 20% varianten op H15, 10% nieuw. Video, niet statisch, dat is al getest.

**5. Tag de Klaviyo mails met utm_campaign.** 107 bezoekers zijn nu niet toewijsbaar. Format volgens de conventie: lowercase, `utm_source=klaviyo`, `utm_medium=email`, `utm_campaign=<naam>`.

Punt 1 en 2 zijn allebei infrastructuur. Zolang die openstaan is er geen betrouwbare data om campagnebeslissingen op te baseren, hoe goed de creatives ook zijn.

---

## Google Sheet

Overgeslagen op verzoek. Geen Google MCP aangeroepen tijdens deze run.

---

*Gegenereerd 6 augustus 2026. Databronnen: PostHog MCP (project STX EU, id 149694). Meta Ads MCP niet beschikbaar.*
