# Morning Report — 2026-08-17

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 17 augustus 2026

**Pipeboard is niet geautoriseerd, tiende dag op rij.** Stap 1 tot en met 4 konden niet draaien. Geen spend, impressions, CTR, CPC, CPM of ROAS. Autoriseren kan niet vanuit deze niet-interactieve sessie, dat gaat via je claude.ai connector instellingen of `/mcp` in een interactieve sessie. Stap 6 en alle Google MCPs overgeslagen zoals gevraagd.

Totaal spend: **EUR 0,00** over 30 dagen. PostHog bevestigt dat onafhankelijk: nul sessies met `utm_source=meta` of `utm_medium=cpc`, en Paid Social en Paid Search komen niet voor in de kanaaltabel.

### De vondst van vandaag

Gisteren noemde ik de bounce op je categoriepagina's een defect. De entry-page data is scherper dan dat.

| Entry page | Entries (7d) | Pageviews/sessie | Bounce |
|---|---|---|---|
| /en_GB/shop/category/foil-balloons-2915 | 283 | **1,00** | 97,9% |
| /folie-ballonnen | 229 | **1,00** | 96,5% |
| /en_GB/foil-balloons | 70 | **1,00** | 94,3% |
| /de/folienballons | 54 | **1,00** | 90,7% |
| /en_GB/shop/category/printed-latex-2912 | 49 | **1,00** | 95,9% |

Ter vergelijking: homepage 366 entries met **22,9** pageviews per sessie en 3,2% bounce. /en_GB 20,9. /fr/shop 22,8.

Exact 1,00 over vijf pagina's in vier talen betekent nul doorkliks. Geen enkele. Een gewoon slechte pagina geeft spreiding en komt uit op 1,3 of 1,6. Precies 1,00 heeft twee mogelijke verklaringen: de pagina rendert niet, of dit verkeer is niet menselijk en PostHog filtert het niet weg. Beide zijn erg, en ze vragen om verschillende acties.

**Open die vijf URL's zelf in incognito. Twee minuten, en het beslist alles daarna.**

### Punt 2, vierde rapport op rij

3.451 Referral-bezoekers over 30 dagen, waarvan 3.365 van je eigen domeinen (sempertexeurope.com 3.337, Odoo 18, shipping-portal 10). **97,5% van je verwijzend verkeer is jezelf.** Echt extern: circa 86 bezoekers per maand.

### Wat wel werkt

De UTM-pipeline. Drie email-campagnes komen netjes getagd binnen (mailjet 140 en 46, Klaviyo 109). Zodra er spend is, zie je het terug. Nog steeds open: lowercase afdwingen, en Klaviyo mist een campaign-naam.

### Aanbeveling

70-20-10 verdeelt budget over bewezen winnaars. Je hebt er nog geen, en je weet niet of je bestemmingspagina's laden. Dat is geen optimalisatievraag maar een voorwaarde. Geen euro naar Meta tot punt 1 en 2 staan.

Volgorde: vijf URL's openen → referrer-exclusies → Pipeboard autoriseren → conversie-events op de SYBB event-pagina's → UTM opschonen → AI-kanaal (242 gratis bezoekers per maand) onderzoeken.

Rapport staat in `Output/Reports/Daily/2026-08-17_ads_report.md`, gecommit en gepusht (`8a41f98c`).

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

No Meta Ads tools are available. Let me confirm the state and gather context from previous reports while I start on PostHog.
API Error: Your computer went to sleep mid-response. The response above may be incomplete.

---

Both data sources are unavailable. Let me confirm the MCP configuration before writing the report.
API Error: Your computer went to sleep mid-response. The response above may be incomplete.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
