# Morning Report — 2026-08-16

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 16 augustus 2026

**Pipeboard is niet geautoriseerd, negende dag op rij.** Stap 1 tot en met 4 konden niet draaien. Geen spend, impressions, CTR, CPC, CPM of ROAS. De sessie is niet-interactief, dus ik kan hier niet autoriseren. Dat gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs overgeslagen zoals gevraagd.

### Nul advertentieverkeer in 30 dagen

De UTM-breakdown bevat geen enkele regel met `utm_source=meta` of `utm_medium=cpc`. Paid Social en Paid Search komen niet voor in de kanaaltabel. Zelfs met werkende Pipeboard-toegang krijg je een rapport over nul actieve campagnes.

### Nieuw: je tracking werkt wel

Drie email-campagnes komen netjes binnen mét UTM's: `mailjet / email / inspiration_promo_202607` (140 bezoekers), `Klaviyo / email / (none)` (109), `mailjet / email / workshop_tobi_promo_202608` (46). De pipeline van UTM naar PostHog is dus niet stuk, er is alleen geen spend. Zodra je een campagne start zie je die meteen terug.

Wel twee slordigheden: `mailjet`, `Klaviyo` en `Pinterest` zijn niet lowercase, en die 109 Klaviyo-bezoekers hebben geen campaign-naam.

### Punt 2 staat er nu drie rapporten op rij

De referrer-exclusies zijn nog steeds niet aangezet. Van je 451 Referral-bezoekers komen er 433 van je eigen domeinen (sempertexeurope.com 426, Odoo 4, shipping-portal 3). **96,0% van je "verwijzend verkeer" is jezelf.** Echt extern: ongeveer 18 bezoekers.

### Nieuw en dit kost geld

| Pagina | Bezoekers | Bounce |
|---|---|---|
| /en_GB/shop/category/foil-balloons-2915 | 197 | **98,3%** |
| /folie-ballonnen | 149 | **95,9%** |
| /de/shop/category/latex-ballons-2911 | 95 | **100,0%** |
| /shop (NL) | 308 | 43,1% |
| / (homepage) | 376 | 2,9% |

De Engelse en Duitse categoriepagina's bouncen bijna volledig, de Nederlandse `/shop` zit op 43% en de homepage op 3%. Dat is geen seizoen en geen slecht publiek, dat is een kapotte pagina. 570+ bezoekers per week klikken direct weg op precies de pagina's waar je straks ads naartoe stuurt.

### De daling blijft een meetartefact

Bezoekers -33,0%, pageviews maar -13,0%, sessieduur +45,0%, bounce -5,7pp. Was je een derde van je publiek kwijt, dan waren de pageviews meegezakt. Je reële daling is ongeveer 13%.

### Volgorde

1. Autoriseer Pipeboard
2. Referrer-exclusies aan in PostHog, vijf minuten
3. **Open zelf `/en_GB/shop/category/foil-balloons-2915` en `/folie-ballonnen`**, 98% bounce is een defect
4. Conversie-events op de SYBB event-pagina's vóór er budget in gaat
5. UTM lowercase afdwingen, campaign verplicht in Klaviyo
6. AI-kanaal onderzoeken, 242 bezoekers in 30 dagen gratis

**Aanbeveling:** geen euro naar Meta tot punt 2 en 3 staan. Ads op een lekkende bak zetten is de duurste manier om te leren dat de bak lekt.

Rapport staat in `Output/Reports/Daily/2026-08-16_ads_report.md`, gecommit en gepusht (`7230f982`).

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

Rapport staat in `Output/Reports/Daily/2026-08-15_sybb_report.md`, gecommit en gepusht.

**Meta Ads: niet opgehaald.** De Pipeboard MCP vereist autorisatie en deze sessie is niet-interactief, dus de OAuth flow kan hier niet draaien. Tiende dag op rij. Autoriseren gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Sectie 2 staat leeg met die reden erbij.

**De belangrijkste vondst is een correctie op het ads rapport van gisteren.** De 98% bounce op `/en_GB/shop/category/foil-balloons-2915` en 96% op `/folie-ballonnen` zijn geen kapotte pagina's, het is botverkeer. Over 9 tot 15 augustus:

| Pagina | Sessies | Echte sessies | Bounce echt |
|---|---|---|---|
| /folie-ballonnen | 74 | **0** | n.v.t. |
| /en_GB/shop/category/foil-balloons-2915 | 115 | **3** | **0,0%** |

Actiepunt 3 uit dat rapport ("open zelf die pagina's, 98% bounce is een defect") kun je schrappen.

Gisteren spoot dezelfde bron een piek van **1.247 bots** in je data, vier keer het weekgemiddelde van 312. Signatuur: één pageview per persoon, referrer direct, verspreid over Brazilië, Seychellen, Colombia, Argentinië, India en Irak. Ruw meet je 1.321 bezoekers en 91,5% bounce; gefilterd blijven er 126 bezoekers, 135 sessies en 16,3% bounce over.

Dat verklaart ook de "daling" die drie rapporten op rij is gemeld. Gefilterd bewoog je echte publiek van ~257 naar ~251 bezoekers. Er was geen daling, het botverkeer ebde weg.

Voor SYBB zelf: landing page vijftien dagen zonder één event (laatste op 31 juli), nul UTM verkeer met `meta`, `cpc` of `sybb` projectbreed, en de SYBB event pagina's kregen gisteren 1 pageview van 1 bezoeker. De funnel uit de skill is niet te bouwen, drie van de vier stappen bestaan niet als event.

Top 3 acties: bot filtering en referrer exclusies aanzetten in PostHog (~10 min, maakt al je rapportage bruikbaar), Pipeboard autoriseren, en conversie-events op de SYBB registratiepagina's zetten vóór er budget in gaat.

---

## Auto-Optimize, 16 augustus 2026: niet uitgevoerd

**Geen enkele ad gepauzeerd, geen voorstel gedaan.** Twee redenen, beide blokkerend.

**1. Pipeboard is nog steeds niet geautoriseerd, tiende dag.** De Meta Ads MCP levert geen tools. Alle zes stappen van dit command draaien erop: campagnes, ad sets, ads, insights, en `update_ad` om te pauzeren. Zonder `actions.link_click` is er geen Link CTR of CPC (link), dus geen kill-regel om op te triggeren. Deze sessie is niet-interactief, autoriseren gaat via je claude.ai connector instellingen of `/mcp` in een interactieve sessie.

**2. Er is niets om te optimaliseren, ook mét toegang.** PostHog werkt wel, en die data is duidelijk. Laatste 3 dagen, hetzelfde venster als dit command:

| Kanaal | Bezoekers | Aandeel |
|---|---|---|
| Direct | 2.590 | 88,7% |
| Referral | 156 | 5,3% |
| Organic Search | 137 | 4,7% |
| AI | 25 | 0,9% |
| Organic Social | 9 | 0,3% |
| Email | 4 | 0,1% |

Paid Social en Paid Search komen niet voor. Geen enkele UTM-regel met `utm_source=meta` of `utm_medium=cpc`. De 6 Meta-bezoekers die er zijn komen van facebook.com en instagram.com zonder UTM's, dus organisch.

Dat is de bevestiging over 3 dagen van wat het ads-rapport van vanochtend over 30 dagen liet zien: **er draait geen betaald verkeer.** Nul actieve ads betekent nul classificatie, nul budgetverdeling, nul voorstellen. Een 70-20-10 analyse op een lege set is een verzinsel, dus die heb ik niet gemaakt.

**Eén ding om te weten voor straks:** de 70-20-10 drempels in dit command staan nog op de oude all-clicks kalibratie. De TODO van 13 april is open. Zodra er weer ads draaien moet je die vaststellen, anders classificeert het command systematisch te streng.

Prioriteit blijft ongewijzigd: Pipeboard autoriseren, dan de bouncende categoriepagina's (98,3% / 95,9% / 100,0%) en de referrer-exclusies, dan pas budget.

Rapport staat in `Output/Reports/Daily/2026-08-16_auto_optimize.md`, gecommit en gepusht (`cb3ff82b`). Geen Google MCPs aangeroepen, niet naar de tracker Sheet geschreven.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
