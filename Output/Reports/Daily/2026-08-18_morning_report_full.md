# Morning Report — 2026-08-18

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 18 augustus 2026

**Pipeboard is niet geautoriseerd, elfde dag op rij.** Stap 1 tot en met 4 konden niet draaien. Geen spend, impressions, CTR, CPC, CPM of ROAS. Autoriseren gaat via je claude.ai connector instellingen of `/mcp` in een interactieve sessie, niet vanuit deze sessie. Stap 6 en alle Google MCPs overgeslagen zoals gevraagd.

Totaal spend: **EUR 0,00** over 30 dagen. PostHog bevestigt het: geen Paid Social, geen Paid Search, geen enkele sessie met `utm_source=meta`.

### Correctie op gisteren

Gisteren adviseerde ik je vijf categoriepagina's in incognito te openen omdat ze exact 1,00 pageview per sessie hadden. **Doe dat niet, de pagina's zijn niet stuk.** De 1,00 hoort niet bij die pagina's, hij hoort bij bepaalde landen.

| Land (7d) | Bezoekers | Pageviews | Views per bezoeker |
|---|---|---|---|
| België | 301 | 8.566 | 28,5 |
| Nederland | 365 | 7.579 | 20,8 |
| Duitsland | 271 | 4.350 | 16,1 |
| Brazilië | 448 | 448 | **1,00** |
| **Seychellen** | **287** | **287** | **1,00** |
| Argentinië | 189 | 189 | **1,00** |

De Seychellen zijn het bewijs: 287 bezoekers uit een land met 100.000 inwoners, meer dan Frankrijk (174), voor een Europese B2B ballondistributeur. Bekende VPS en proxy jurisdictie.

Twee checks bevestigen het. **Browsers:** nul Safari, nul mobiel in 687 sessies, terwijl je site 7% mobiel is. Nul is geen toeval. **Firefox** staat op 30% in dit segment tegen 3% in de echte markt.

### Wat dit je cijfers kost

| Metric (7d) | Gerapporteerd | Zonder bots | Verschil |
|---|---|---|---|
| Bezoekers | 5.606 | 3.731 | **33,4% was geen mens** |
| Sessieduur | 223,7s | **406,5s** | **+82%** |
| Bounce rate | 52,3% | **45,6%** | **6,7 punten beter** |

Je site presteert beter dan je dashboard laat zien. Maar zodra je Meta gaat draaien, vergelijk je landingspaginacijfers met een nulmeting die een derde vervuild is. Dan wordt elke conclusie over adprestatie verkeerd, in beide richtingen.

Verder ongewijzigd: 97,5% van je referral verkeer is jezelf (3.381 van 3.466). De UTM pipeline werkt, drie emailcampagnes komen getagd binnen.

**Volgorde:** botfilter in PostHog → referrer exclusies → Pipeboard autoriseren → conversie events SYBB → UTM lowercase. Geen euro naar Meta tot de eerste twee staan.

Rapport staat in `Output/Reports/Daily/2026-08-18_ads_report.md`, gecommit en gepusht (`12c41e90`).

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

---

`SELECT 1` returns instantly, so the connection is fine — the event scans are what's timing out. Trying a minimal aggregation.
API Error: Your computer went to sleep mid-response. The response above may be incomplete.

---

API Error: Your computer went to sleep mid-response. The response above may be incomplete.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
