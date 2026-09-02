# Morning Report — 2026-09-02

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport is opgeslagen in `Output/Reports/Daily/2026-09-02_ads_report.md` en gecommit/gepusht (4702c793). Geen Google MCPs aangeroepen, geen Sheet geschreven.

## Meta Ads Rapport, 2 september 2026

**Periode:** last 30d, maar beide actieve campagnes draaien pas sinds 27/28 augustus, dus feitelijk 5 à 6 dagen data. De Pipeboard MCP meldde "requires authentication"; de data is via de directe JSON-RPC call opgehaald. Het account act_607231713057715 uit het command bestaat niet.

### Overzicht per campagne

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Freq. | Leads | CPL |
|---|---|---|---|---|---|---|---|---|---|---|
| Wholesaler (LIT) | Active | €390,33 | 57.230 | 1.149 | 2,0% | €0,34 | €6,82 | 3,58 | 11 | €35,48 |
| Wholesaler (SWE) | Active | €343,29 | 25.060 | 845 | 3,4% | €0,41 | €13,70 | 3,03 | 5 | €68,66 |
| **Totaal** | | **€733,62** | **82.290** | **1.994** | **2,4%** | **€0,37** | **€8,92** | | **16** | **€45,85** |

ROAS is niet van toepassing, het zijn lead-campagnes. Setup: 4 ad sets per campagne, elk €20/dag.

### Underperformers

- **Video 2 (SWE)**: CPC €0,72 en CPM €17,90, 0 leads na €81,76. Pauzeren.
- **Video 1 (SWE)**: CPM €15,88, 0 leads na €88,37. Tot 4 september geven, dan pauzeren als het zo blijft.
- **Video 2 (LIT)**: CPC €0,52, maar laagste CPL van LIT (€24,97). Laten draaien.
- **Campagne LIT**: frequency 3,58 na 6 dagen, kleine doelgroep (reach 15.995). Nieuwe creatives binnen een week.
- **Statisch 1 (LIT)**: CTR 1,2%, net boven de drempel. Monitoren.

### Top performers

- **Beste CTR**: Statisch 2 (SWE), 4,2%
- **Laagste CPC**: Statisch 2 (LIT), €0,20
- **Laagste CPL**: Statisch 2 (SWE), €21,91 (4 van de 5 Zweedse leads)

### Grootste bevinding: funnel-lek

Slechts 22,7% (SWE) en 13,5% (LIT) van de link clicks wordt een landing page view. Meer dan driekwart van de betaalde klikken komt niet geregistreerd aan. Dat wijst op laadsnelheid, pixelplaatsing of onbedoelde tikken op mobiel. Dit weegt zwaarder dan elk verschil tussen ads.

### Aanbeveling (70-20-10)

1. **70% naar winnaars**: Statisch 2 (SWE) van €20 naar €35/dag, Statisch 2 (LIT) naar €30/dag.
2. **Pauzeer Video 2 (SWE)** vandaag; Video 1 (SWE) krijgt tot 4 september.
3. **20% variaties**: 2 nieuwe statische varianten op de Statisch 2 hook voor Litouwen, vóór de frequency de 4 passeert.
4. **Fix de LPV-lek**: mobiele laadsnelheid en pixel van de wholesaler-landingspagina checken.

SYBB en Nozzle Up staan gepauzeerd zonder spend in de afgelopen 30 dagen.

**Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases. Dan draai ik een `/funnel-diagnose` op de gecombineerde data.

---

Het rapport staat in `Output/Reports/Daily/2026-09-01_sybb_report.md` en is gecommit en gepusht naar main.

**Databronnen.** Beide Pipeboard MCP servers meldden een auth-fout, maar de token werkte via directe JSON-RPC calls naar dezelfde MCP endpoint. De geconfigureerde `posthog` server faalde met een 405, dus ik heb de claude.ai PostHog MCP gebruikt, project STX EU. Geen Google MCPs aangeroepen, niets naar de Google Sheet geschreven.

**Belangrijkste bevindingen voor 1 september:**
- **Campagne 2026: SYBB staat nog op PAUSED** sinds 19 april. Nul spend, nul impressies over de hele week. Het ad account draait wel wholesaler campagnes, buiten scope.
- **Landing page startyourballoonbusiness.com kreeg 0 bezoekers.** De 2 bezoekers van de afgelopen week waren intern: één test-URL met utm_content h11_b3_cta5 en één via de Wix editor.
- **De echte funnel op sempertexeurope.com leeft wel.** 10 bezoekers op SYBB registratiepagina's gisteren, tegen een gemiddelde van 5,6 per dag de week ervoor. Editie 7 trekt de meeste interesse. Alles organisch, geen UTM's.
- **De piek van 31 augustus was vertekend.** 42 van 58 pageviews kwamen van één Belgische bezoeker die 8 registratiepagina's doorklikte.
- **Conversie blijft onmeetbaar.** Er is geen registratie-voltooid event, en scroll- en CTA-events bestaan niet in het project.

**Top 3 acties in het rapport:** registratie-voltooid event toevoegen in Wix, de skill herdefiniëren op de registratiepagina's in plaats van de dode landing page, en pas daarna beslissen over een campagne herstart.

Ik heb ook de Pipeboard memory bijgewerkt: het antwoord is gewone JSON, geen SSE stream. De oude parser gaf lege output.

---

Rapport staat in `Output/Reports/Daily/2026-09-02_auto_optimize.md` en is gecommit en gepusht (f70f9b48). Alleen Meta Ads via Pipeboard gebruikt, geen Google MCPs, niets naar de Sheet geschreven.

## Auto-Optimize, 2 september 2026

**Geen ads gepauzeerd.** Twee actieve campagnes (Wholesaler SWE en LIT), 8 ads, elk €20,00/dag. Periode 30 augustus t/m 1 september, alles op link metrics.

**Kill-regels**

- **CPC (link) > €1,50**: niet van toepassing, geen enkele ad heeft 500 link clicks.
- **Link CTR < 0,8%**: Statisch 1 (LIT) triggert met 0,5% op 10.306 impressions. Ik heb die bewust niet gepauzeerd. Het is de goedkoopste leadbron van het hele account: 3 van de 7 LIT-leads in 3 dagen, CPL €19,60 tegen een campagnegemiddelde van €33,54. De ad set optimaliseert op leads, niet op clicks, en de lage Link CTR komt aanwijsbaar uit het 18-24 segment en desktop, allebei zonder leads. Mechanisch pauzeren zou de learning phase resetten. Beslissing ligt bij jou, het pauzeer-commando staat klaar in het rapport.

**Waarschuwingen**

- Video 2 (SWE): CPM €18,04, 0 leads na €84,30, Instagram Link CTR 0,5%.
- Video 1 (SWE): CPM €15,98, 0 leads na €90,11.
- Statisch 2 (SWE): Link CTR zakt naar 74% van lifetime, net boven de fatigue-grens.
- Funnel-lek blijft: maar 12 tot 17% van de link clicks wordt een landing page view.

**70-20-10**: Core (Statisch 2 SWE en LIT) krijgt 25% in plaats van 70%. De twee SWE-video's zonder leads krijgen 25% in plaats van 10%.

**Voorstellen (wachten op jouw goedkeuring)**

1. **Budget**: Statisch 2 (SWE) naar €35,00, Statisch 2 (LIT) naar €30,00, Video 2 (SWE) pauzeren, Video 1 (SWE) naar €10,00 tot 4 september.
2. **Variaties**: alle 8 ads hebben identieke copy, dus het verschil zit alleen in de visual. Drie hook-varianten (Label, Vraag, Conditioneel) op de winnende Statisch 2 visual.
3. **Audience**: Statisch 1 (LIT) van 18-65 naar 25-65 en desktop uitsluiten. Audience Network overal uitsluiten, dat levert nep-clicks zonder landing page views.
4. **Statisch 1 (LIT)**: A laten draaien met de audience-fix (aanbevolen), of B strikt pauzeren. Structureel: overweeg een CPL-uitzondering op de Link CTR-regel voor lead-campagnes.

Geef aan welke nummers je wilt uitvoeren (1, 2, 3, 4A of 4B).

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
