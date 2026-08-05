# Morning Report — 2026-08-05

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Connectie viel weg. Ik probeer opnieuw.
API Error: Connection closed mid-response. The response above may be incomplete.

---

Rapport staat in `Output/Reports/Daily/2026-08-04_sybb_report.md`, gecommit en gepusht.

**De uitkomst is niet wat je zou verwachten van een performance rapport: er was op 4 augustus geen enkele SYBB activiteit.**

Wat beide bronnen bevestigen:

- **Meta Ads:** campagne `2026: SYBB` staat op PAUSED, laatst gewijzigd 19 april 2026. Alle 7 dagen in het venster 29 juli t/m 4 augustus geven een lege dataset terug. Ook accountbreed nul spend op 4 augustus. De laatste maand met delivery was april (€1.059,47, CTR 2,11%, CPC €0,55).
- **PostHog:** startyourballoonbusiness.com kreeg 0 pageviews. Laatste bezoeker was 31 juli, 1 pageview. In 30 dagen totaal 42 pageviews.

Ik heb de rapportstructuur uit de skill volledig aangehouden, maar de tabellen gevuld met nullen en "geen data" in plaats van er iets van te maken. Bounce rate, scroll depth en CTA click rate staan bewust op ⚪ (niet meetbaar) en niet op 🔴, want nul sessies is iets anders dan slecht presteren.

Twee dingen die ik onderweg tegenkwam en die verder gaan dan de dagvraag:

1. **De tracking op de landing page kan dit rapport sowieso niet vullen.** Op die host vuren alleen `$pageview`, `$pageleave`, `$autocapture` en `$web_vitals`. Geen custom events voor CTA clicks, scroll milestones of `/booking`. En slechts 3 pageleave events in 30 dagen. Ook ná een herstart blijven secties 3 en 4 dus leeg tot dit gerepareerd is.
2. **De pixel waardes zijn intern inconsistent.** April toont 6 purchases met een waarde die neerkomt op ruim €7.000 per stuk, terwijl add_to_cart events op €350 staan. Waarschijnlijk mengt de gedeelde Sempertex pixel webshop orders met workshop boekingen. Elke ROAS op deze campagne is daarmee nu onbruikbaar als stuurinformatie.

Beide staan als rode vlag plus actiepunt in het rapport. De hoofdvraag die eruit volgt is er één die ik niet voor je kan beantwoorden: is die pauze sinds april bewust, of is dit blijven liggen?

Geen Google MCPs aangeroepen, niets weggeschreven naar de tracker Sheet.

---

Auto-optimize niet beschikbaar. Geen actieve campagnes.

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
