# Morning Report — 2026-09-15

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Het rapport staat in `Output/Reports/Daily/2026-09-15_ads_report.md`, gecommit en gepusht (0b881f93). Alleen Pipeboard (directe JSON-RPC route) en PostHog (directe REST-route) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## Meta Ads Rapport, 15 september 2026

**Er draait nog steeds niets.** Alle 7 campagnes staan op PAUSED, de twee Wholesaler Campagnes sinds 4 september 11:50. Meta geeft voor 8 t/m 14 september nul rijen. PostHog bevestigt dat live: na 4 september nog 5 nalopers (6, 7 en 9 september), nul betaald verkeer op 10 t/m 14 september. Laatste wholesaler-inzending blijft 4 september.

Pipeboard werkte direct, geen weeklimiet. Alle Meta-cijfers zijn vandaag vers opgehaald.

**Overzicht per campagne (last 30d, 16 aug t/m 14 sep)**

| Campagne | Spend | CTR | CPC | CPM | Freq. | Meta leads | PostHog inzendingen | € / inzending |
|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | €562,14 | 1,8% | €0,35 | €6,18 | 3,97 | 11 | 16 | €35,13 |
| Wholesaler (SWE) | €507,24 | 3,2% | €0,41 | €12,92 | 3,29 | 8 | 8 | €63,41 |
| **Totaal** | **€1.069,38** | 2,2% | €0,37 | €8,22 | | 19 | 24 (+11 zonder UTM) | €30,55 all-in |

ROAS is niet van toepassing, het zijn lead-campagnes. Kosten per inzending zijn op PostHog gebaseerd, omdat de Meta pixel structureel te weinig telt.

**Underperformers**

- **Video 2 (SWE)**: CPC €0,69 en CPM €17,07, beide boven drempel. Niet herstarten in deze vorm.
- **Video 1 (SWE)**: CPC €0,53, CPM €15,27, nul inzendingen op 113 sessies. Definitief uit.
- **Campagne LIT**: frequency 3,97, publiek verzadigd. Verse creatives nodig bij herstart.
- **Statisch 2 (LIT)**: goedkoopste clicks (€0,20) maar kortste sessies (52s), 0,7% conversie, €63,63 per inzending. Nieuwe hook testen.
- **Video 2 (LIT)** en **Statisch 1 (LIT)** krijgen een CPC- of CTR-vlag maar zijn de beste converteerders (3,5% en 3,0%). Behouden.

**Top performers**

- Beste CTR: Statisch 2 (SWE), 4,0%
- Laagste CPC: Statisch 2 (LIT), €0,20
- Beste kosten per inzending: Video 2 (LIT) €28,75, dan Video 1 (LIT) €29,38, dan Statisch 2 (SWE) €32,03

**Funnel /become-a-distributor (30d):** 1.744 pageviews, 137 formulierstarts, 21 formulier-fouten, 35 inzendingen. Het grootste lek zit tussen start en inzending: 102 van 137 starters haken af. Dat eerst fixen vóór er weer budget op gaat.

**Aanbeveling (70-20-10)** bij herstart: 70% naar de bewezen set (Video 1 LIT, Video 2 LIT, Statisch 1 LIT, Statisch 2 SWE) met verse creatives, 20% naar een Zweedse variant van Video 2 (LIT), 10% naar een nieuwe hook voor Statisch 2 (LIT). Beide SWE-video's niet meenemen. De herstart-voorstellen van 3 september wachten nog op jouw goedkeuring.

**Wijzigingen t.o.v. gisteren:** geen. Zelfde status, zelfde 30d-cijfers. SWE telt vandaag 8 inzendingen met UTM-match (gisteren 7), een verschil in de sessiekoppeling, niet in het totaal van 35.

**Wil je funnel data toevoegen?** Geef dan de landing page metrics uit Wix Analytics of GA4: bezoekers, opt-in of booking clicks, add to cart, afgeronde aankopen. Dan draai ik de volledige funnel-diagnose.

---

Het rapport staat in `Output/Reports/Daily/2026-09-14_sybb_report.md`, gecommit en gepusht (a8c3e746). Alleen Pipeboard (directe JSON-RPC route, de MCP vroeg om autorisatie) en PostHog (directe REST-route, de MCP gaf HTTP 405) gebruikt. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

## SYBB rapport, 14 september 2026

**Kern:** 8 SYBB sessies op de registratiepagina's, maar 2 daarvan zijn van een Sempertex-medewerker die event-pagina's bewerkte. Er blijven 6 externe bezoekers over (DE 2x, FR, FI, NL, BE) en niemand klikte op Register. Dat is de tweede dag op rij: 12 externe bezoekers in twee dagen zonder één inschrijfpoging, tegen 5 klikken op 30 sessies in de week ervoor.

**Meta:** campagne `2026: SYBB` staat 148 dagen op PAUSED, alle 7 campagnes gepauzeerd, nul rijen voor 8 t/m 14 september. PostHog bevestigt nul Meta-verkeer en nul Facebook of Instagram referrals. Landing page startyourballoonbusiness.com: zeventiende dag op 0 bezoekers.

**Drie nieuwe bevindingen die de meting zelf raken:**

- **Vals-positieve conversie.** De ene `/shop/confirmation` in een SYBB sessie was een webshoporder van een ingelogde Belgische klant die 7 seconden op de SYBB pagina was. De huidige betaaldefinitie telt dat als workshopticket. Aangescherpt in memory: alleen betaald als er vóór de confirmation een Register-submit of "Go to Payment" klik zit.
- **Intern verkeer zat in de cijfers.** Een medewerker met Odoo-login en 183 pageviews in de vertaal-editor leverde 2 van de 8 sessies, 6 van de 13 pageviews en de twee langste sessies. Persoon-ID en filterregel staan nu in memory; vanaf morgen uitgesloten in de queries.
- **Beide ingelogde klanten sloegen de inschrijving over.** De Finse klant vergeleek professional-47 en 48, de Belgische klant keek 7 seconden. Een account alleen is dus niet genoeg; de account-hypothese blijft open.

**Top 3 acties:**
1. Zelf de inschrijving doorlopen op iPhone, uitgelogd, plus de replay-instellingen controleren (vijfde dag open, negen dagen zonder één opname).
2. Cohort "Sempertex intern" aanmaken in PostHog en als intern markeren in de projectinstellingen.
3. Datum- en locatieoverzicht van SYBB op /events en boven elke registratieknop, omdat bezoekers voor de tweede dag op rij meerdere data openen zonder te kiezen.

Overig: de crawlergolf is voorbij (538 sessies, 8% bot-achtig, tegen 91% op 12 september), rage clicks zaten allemaal op shoppagina's, ChatGPT stuurde 11 sessies site-breed maar geen op SYBB. Nog open uit eerdere rapporten: skill-definitie omzetten van landing page naar event funnel, de vier PostHog actions, en één gecachte Meta-call per dag voor de drie rapporten.

---

Rapport staat in `Output/Reports/Daily/2026-09-15_auto_optimize.md`, gecommit en gepusht (c1df7ff4). Alleen Pipeboard (directe JSON-RPC route, 3 calls, geen weeklimiet) en PostHog (directe REST-route) gebruikt. Beide MCP-servers zelf weigerden opnieuw. Geen Google MCPs aangeroepen, niets naar de Sheet geschreven.

**Geen automatische acties.** Meta geeft over 12 t/m 14 september nul rijen op campagne- en ad-niveau. Alle 7 campagnes staan op PAUSED, de twee Wholesaler campagnes sinds 4 september 11:50. De kill-regels hadden niets om op te draaien, geen `update_ad` calls gedaan.

**PostHog bevestigt de stilstand live.** Nul sessies met een Meta-UTM sinds 12 september, nul wholesaler-inzendingen sinds 8 september. Laatste betaalde inzending blijft 4 september, twaalfde dag zonder levering.

**De zes voorstellen staan ongewijzigd in het rapport en wachten op je goedkeuring:**

1. Herstart Wholesaler (LIT) op €100,00 per dag in 70-20-10 verdeling, Wholesaler (SWE) beperkt op €40,00 per dag zonder de twee SWE-video's.
2. Twee variaties op Statisch 2 (SWE), twee op Video 2 (LIT), en een nieuwe Vraag-hook voor Statisch 2 (LIT).
3. LIT ad sets samenvoegen, Audience Network uitsluiten, SWE audience verbreden, Statisch 1 (LIT) naar 25-65 zonder desktop.
4. Conversie-guard op de kill-regels zodat Statisch 1 (LIT) niet op dag 1 na herstart sneuvelt.
5. Tracking en funnel fix vóór herstart: Meta telt 19 leads tegenover 35 in PostHog, en 102 van 137 formulierstarters haken af.
6. Eén gedeeld Meta-extract per dag cachen voor de drie rapporten, anders valt de gratis Pipeboard weeklimiet later deze week weer dicht.

Zolang niets herstart is, blijft elke run op 0 acties uitkomen. Geef aan welke nummers ik mag uitvoeren.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
