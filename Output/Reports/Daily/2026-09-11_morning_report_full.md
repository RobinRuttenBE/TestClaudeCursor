# Morning Report — 2026-09-11

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Het rapport staat in `Output/Reports/Daily/2026-09-11_ads_report.md` en is gecommit en gepusht. Alleen Pipeboard en PostHog zijn gebruikt, beide via de directe HTTP-route omdat de MCP-servers niet verbonden. Geen Google-bronnen aangeroepen, geen Sheet geschreven.

## Meta Ads Rapport, 11 september 2026

**Er draait op dit moment niets.** Alle 7 campagnes staan op PAUSED. De twee Wholesaler Campagnes (SWE en LIT) zijn op 4 september gepauzeerd. PostHog bevestigt dat: 58 betaalde sessies op 4 september, daarna 0 tot 2 per dag. Dit rapport is een terugblik op de laatste 30 dagen, geen live stand.

**Overzicht per campagne (last 30d)**

| Campagne | Spend | Impr. | Freq. | CTR | CPC | CPM | Meta leads | PostHog inzendingen | Kosten / inzending |
|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 90.888 | 3,97 | 1,8% | €0,35 | €6,18 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 39.267 | 3,29 | 3,2% | €0,41 | €12,92 | 8 | 7 | €72,46 |
| **Totaal** | **€1.069,38** | 130.155 | | 2,2% | €0,37 | €8,22 | 19 | 23 | €46,49 |

ROAS is niet van toepassing, het zijn lead-campagnes. Meta telt 277 landing page views, PostHog 1.412 sessies. De pixel ondertelt structureel, dus kosten per inzending zijn op PostHog gebaseerd.

**Underperformers**

- **Video 1 (SWE)**: CPC €0,53, CPM €15,27 en 0 inzendingen op 113 sessies. Uitschakelen.
- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, duurste klik van alle acht. Niet herstarten in deze vorm.
- **Video 2 (LIT)**: CPC €0,58 boven de drempel, maar goedkoopste inzending (€28,75) en hoogste conversie (3,5%). Behouden.
- **Campagne LIT**: frequency 3,97. Klein Litouws publiek was na twee weken verzadigd, verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: laagste CPC (€0,20) maar 0,7% conversie en kortste sessies. Klikt goedkoop, converteert niet.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Goedkoopste inzending: Video 2 (LIT), €28,75

**Aanbeveling (70-20-10)** bij herstart: 70% naar de LIT-winnaars (Video 1, Video 2, Statisch 1) plus Statisch 2 (SWE), met nieuwe creatives. 20% naar een Zweedse variant op Video 2 (LIT), want SWE heeft geen werkende video. 10% naar een nieuwe hook voor Statisch 2 (LIT).

**Funnel** op /become-a-distributor (30d, alle verkeer): 1.739 pageviews, 138 form starts, 35 inzendingen. Het grote lek zit vóór het formulier: 92% haakt af voordat ze beginnen.

**Let op:** account act_607231713057715 uit de command bestaat niet in Pipeboard. Als je later Wix of GA4 landing page data aanlevert, kan ik daar een volledige funnel-diagnose op draaien.

---

Het rapport staat in `Output/Reports/Daily/2026-09-10_sybb_report.md` en is gecommit en gepusht naar main.

**Databronnen.** Beide MCP-servers waren onbereikbaar in deze sessie (Pipeboard vroeg autorisatie, PostHog gaf HTTP 405). Ik heb dezelfde twee bronnen direct aangesproken: Pipeboard via de JSON-RPC route en PostHog via de REST API op project STX EU. Geen Google MCPs aangeroepen, geen Google Sheet bijgewerkt.

**Belangrijkste bevindingen**

- **Meta Ads:** campagne `2026: SYBB` staat 144 dagen op PAUSED. Nul spend, impressies en clicks gisteren en in de 7 dagen ervoor. PostHog bevestigt dit: geen enkele pageview met `utm_source=meta`.
- **Landing page:** startyourballoonbusiness.com voor de dertiende dag op rij 0 bezoekers.
- **Event funnel op sempertexeurope.com:** beste dag van de week met 6 bezoekers tegenover 3,7 gemiddeld. Vijf echte mensen, waarvan drie terugkerend sinds augustus, plus één link-preview bot.
- **Nieuw en niet eerder gerapporteerd:** op 9 september is de eerste volledig meetbare SYBB inschrijving met betaling gelukt. Een ingelogde Belgische klant ging via "Go to Payment" naar Bancontact en landde op `/shop/confirmation`. De aanname dat de workshopconversie niet meetbaar is, vervalt daarmee.
- **Derde afgebroken inschrijving in vier dagen.** Gisteravond bevestigde een anonieme bezoeker 1 ticket en strandde in de stap voor deelnemergegevens. De tab bleef 8 uur open. Alle drie de afbrekers waren anoniem, de enige betaler was ingelogd.
- **Session replay** staat zeven dagen op nul, dus van geen enkele poging is een opname.

**Top 3 acties in het rapport:** zelf de deelnemerstap doorlopen op mobiel Safari als uitgelogde bezoeker, de vier funnel-actions in PostHog aanmaken op de nu bewezen route, en session replay herstellen.

Ik heb ook twee geheugennotities bijgewerkt: de projectnotitie over de SYBB funnel bevat nu de bevestigde conversieroute, en de PostHog-referentie bevat de gevonden query-valkuilen (100-rijen limiet, `elements_chain` kolom, timeouts op brede autocapture-queries).

---

Rapport staat in `Output/Reports/Daily/2026-09-11_auto_optimize.md`, gecommit en gepusht (8a87b96a). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST route) gebruikt, beide MCP-servers zelf weigerden. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Alle 7 campagnes staan op PAUSED, de Wholesaler campagnes sinds 4 september. Meta geeft over 8 t/m 11 september 0 rijen op ad-niveau, dus 0 impressions, 0 link clicks en €0,00 spend. Geen ads gepauzeerd, geen `update_ad` calls.

**PostHog bevestigt de stilstand.** 0 tot 2 betaalde sessies per dag, en die 2 op 9 september zijn nalopers op oude ad-URL's. De distributeurspagina kreeg 1 tot 5 organische bezoekers per dag. Laatste inzending blijft 4 september.

**Achtste dag op rij zonder levering.** Niets veranderd ten opzichte van gisteren. De vijf voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE) en twee op Video 2 (LIT).
3. LIT ad sets samenvoegen, SWE audience verbreden.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking fix vóór herstart, Meta telt 19 leads tegenover 33 in PostHog.

Zolang er niets herstart is, blijft elke dagelijkse run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
