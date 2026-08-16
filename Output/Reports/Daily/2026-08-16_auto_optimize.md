# Auto-Optimize Rapport, 16 augustus 2026

**Status: niet uitgevoerd. Geen enkele automatische actie ondernomen.**

Twee onafhankelijke redenen, beide blokkerend.

## 1. Pipeboard is niet geautoriseerd, tiende dag op rij

De Meta Ads MCP (Pipeboard) staat als "requires authentication" en levert geen tools. Stap 1 tot en met 6 van dit command draaien volledig op die connector: campagnes ophalen, ad sets, ads, insights op ad-niveau, en `update_ad` om te pauzeren. Zonder die toegang is er geen spend, geen impressions, geen `actions.link_click`, dus ook geen Link CTR of CPC (link) om kill-regels op te draaien.

Deze sessie is niet-interactief, dus autoriseren kan hier niet. Dat gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie.

Beide accounts konden niet bereikt worden: `act_567892422940728` (primair) en `act_607231713057715`.

## 2. Er is niets om te optimaliseren, ook mét toegang

PostHog is wél bereikbaar en die data vertelt het echte verhaal. Laatste 3 dagen, hetzelfde venster dat dit command hanteert:

| Kanaal | Bezoekers | Aandeel |
|---|---|---|
| Direct | 2.590 | 88,7% |
| Referral | 156 | 5,3% |
| Organic Search | 137 | 4,7% |
| AI | 25 | 0,9% |
| Organic Social | 9 | 0,3% |
| Email | 4 | 0,1% |

**Paid Social en Paid Search komen niet voor.** In de volledige UTM-breakdown over 3 dagen staat geen enkele regel met `utm_source=meta` of `utm_medium=cpc`. De enige Meta-gerelateerde bezoekers zijn 6 organische referrals (facebook.com 4, instagram.com 2), zonder UTM's, dus geen ad clicks.

Dit bevestigt wat het ads-rapport van vanochtend al liet zien over 30 dagen: er draait geen betaald verkeer. Er zijn dus nul actieve ads om te beoordelen, te classificeren of te pauzeren.

## Automatische acties uitgevoerd

Geen. Niet omdat alles boven de drempels presteert, maar omdat er geen ads zijn om te meten.

**Totaal gepauzeerd: 0 ads**

## Waarschuwingen

Niet te beoordelen. Frequency, CPM en Link CTR trend vereisen alle drie Meta-data.

## 70-20-10 Classificatie

Niet te maken. Nul actieve ads, dus geen Core, Emerging of Experimental buckets en geen budgetverdeling om tegen af te zetten.

Los daarvan: de 70-20-10 drempels in dit command staan nog steeds op de all-clicks kalibratie. De TODO uit de herziening van 13 april is nog open. Zodra er weer ads draaien op link metrics moet je die drempels vaststellen voordat classificatie een hard oordeel mag zijn.

## Voorstellen

Geen budget-, variatie- of audience-voorstellen. Elk voorstel in dit command leunt op performance-data die er niet is, en een voorstel verzinnen zonder die data is gokken met je budget.

Wat er wel toe doet, in volgorde:

1. **Autoriseer Pipeboard.** Zonder dit blijft elk ads-command leeg draaien, nu tien dagen op rij.
2. **Fix de bouncende categoriepagina's** vóór er budget in gaat. `/en_GB/shop/category/foil-balloons-2915` bouncet op 98,3%, `/folie-ballonnen` op 95,9%, `/de/shop/category/latex-ballons-2911` op 100,0%. Dat zijn precies de bestemmingen waar ads naartoe zouden sturen.
3. **Zet referrer-exclusies aan in PostHog.** 96,0% van je "verwijzend verkeer" is je eigen domein. Zolang dat aanstaat is elke attributie-analyse na een adstart vervuild.
4. **Conversie-events op de SYBB event-pagina's.** Zonder die kan dit command straks wel Link CTR en CPC (link) berekenen, maar geen ROAS, en dan mist de Core-classificatie zijn belangrijkste criterium.

Dit command wordt pas zinvol als punt 1 staat en er daadwerkelijk spend loopt. Tot die tijd levert het elke dag hetzelfde lege rapport op.

---

**Databronnen:** PostHog MCP (project STX EU, 149694). Meta Ads MCP niet beschikbaar. Geen Google MCPs aangeroepen, niet naar de Meta Ads Tracker Google Sheet geschreven, conform de instructie voor deze run.
