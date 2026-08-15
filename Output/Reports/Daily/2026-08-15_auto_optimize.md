# Auto-Optimize Rapport, 15 augustus 2026

**Run:** `/ads-auto-optimize`
**Databronnen deze run:** Meta Ads MCP (Pipeboard) en PostHog MCP. Geen Google MCPs aangeroepen, niet naar de Google Sheet tracker geschreven.

---

## Status: geblokkeerd op Niveau 1

**Pipeboard Meta Ads MCP is niet geautoriseerd, achtste dag op rij.** De server staat als niet-geautoriseerd gemarkeerd en deze sessie is niet interactief, dus de OAuth-flow kan hier niet draaien.

Gevolg voor dit command:

| Stap | Status | Reden |
|------|--------|-------|
| 1. Performance data ophalen (3 dagen) | Niet uitgevoerd | Geen toegang tot `act_567892422940728` of `act_607231713057715` |
| 2. Ads toetsen aan kill-regels | Niet uitgevoerd | Geen impressions, link clicks of spend beschikbaar |
| 3. Automatisch pauzeren (Niveau 1) | Niet uitgevoerd | Geen ads om te beoordelen, `update_ad` niet aanroepbaar |
| 4. 70-20-10 classificatie | Niet uitgevoerd | Vereist Link CTR en CPC (link) per ad |
| 5. Budgetverdeling berekenen | Niet uitgevoerd | Vereist stap 4 |
| 6. Voorstellen genereren | Deels, op PostHog data | Zie hieronder |

**Autoriseren:** via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie.

---

## ⚡ Automatische acties uitgevoerd

**Geen ads gepauzeerd. Niet omdat alles goed presteert, maar omdat er geen data is.**

Dit is een belangrijk verschil met "alles presteert boven de drempelwaarden". Er is nul zicht op Link CTR, CPC (link), frequency en CPM. Behandel dit rapport niet als groen licht.

**Totaal gepauzeerd: 0 ads**

---

## ⚠️ Waarschuwingen

| Signaal | Waarde | Actie aanbevolen |
|---------|--------|-----------------|
| Pipeboard niet geautoriseerd | 8 dagen op rij | Autoriseer via claude.ai connector instellingen |
| Paid Social verkeer in PostHog | 0 bezoekers, 3 dagen | Er draait vermoedelijk geen enkele actieve campagne |
| UTM-getagd advertentieverkeer | 0 sessies, 3 dagen | Geen enkele sessie met `utm_medium=cpc` of `utm_campaign=sybb` |
| Self-referral vervuiling | 95,7% van Referral | Verwijzers uitsluiten in PostHog, staat sinds gisteren open |

---

## 📊 Wat PostHog wel laat zien (laatste 3 dagen)

### Sitebrede KPI's

| Metric | Waarde |
|--------|--------|
| Bezoekers | 841 |
| Pageviews | 12.441 |
| Sessies | 1.106 |
| Gem. sessieduur | 8m38s |
| Bounce rate | 24,6% |

### Kanaalverdeling

| Kanaal | Bezoekers | Pageviews | Aandeel |
|--------|-----------|-----------|---------|
| Direct | 514 | 6.213 | 56,2% |
| Referral | 187 | 3.248 | 20,4% |
| Organic Search | 173 | 2.842 | 18,9% |
| AI | 27 | 84 | 3,0% |
| Organic Social | 10 | 43 | 1,1% |
| Email | 4 | 12 | 0,4% |

**Paid Social: niet aanwezig. Paid Search: niet aanwezig.**

### UTM-controle

Van de twintig grootste bronnen over drie dagen heeft er precies **nul** een `utm_source`, `utm_medium` of `utm_campaign`. Alles staat op `(none) / (none)`. De enige twee die iets van een tag dragen zijn `Pinterest / organic` (2 bezoekers) en dat is organisch, geen paid.

`facebook.com` staat er wel in als verwijzer, met 1 bezoeker en 5 pageviews. Dat is organisch verkeer vanaf de pagina, geen advertentie. Instagram idem, 2 bezoekers.

**Conclusie: er loopt geen betaald Meta-verkeer naar de site. Zelfs met werkende Pipeboard-toegang zou dit rapport over nul actieve ads gaan.**

### Referral is grotendeels je eigen site

| Verwijzer | Bezoekers | Pageviews |
|-----------|-----------|-----------|
| www.sempertexeurope.com | 179 | 3.164 |
| overige externe verwijzers | 8 | 84 |

179 van 187 Referral-bezoekers is **95,7% self-referral**. Je echte externe verwijzend verkeer is 8 bezoekers over drie dagen, niet 187. Odoo (2 bezoekers, 43 pageviews) en Mollie (1 bezoeker) staan er ook nog in.

Dit is punt 2 uit het rapport van gisteren, nog steeds niet uitgevoerd.

### AI blijft groeien zonder inspanning

ChatGPT levert 28 bezoekers over drie dagen, bijna drie keer Organic Social en zeven keer Email. Het kanaal wordt nergens actief bediend of gemeten.

---

## 📊 70-20-10 Classificatie

**Niet mogelijk.** De classificatie draait op Link CTR en CPC (link) per ad. Beide vereisen `get_insights` op ad-niveau via Pipeboard.

Ter herinnering voor als de toegang terug is: de drempels in het command zijn per 13 april 2026 herzien naar link-metrics (Link CTR < 0,8% en CPC (link) > €1,50 als kill-regels), maar de 70-20-10 grenzen zelf zijn nog gekalibreerd op all-clicks. Die staan nog als TODO open. Bij de eerste run met echte data: rapporteer de classificatie, voer geen budget-shifts uit tot jij nieuwe drempels vaststelt.

**Budget mismatch:** niet vast te stellen.

---

## 💡 Voorstellen (wacht op goedkeuring)

Geen budget- of variatievoorstellen deze run, die vereisen ad-performance data. Wat er wel ligt, is het fundament dat af moet zijn vóór de eerste euro:

**1. Autoriseer Pipeboard**
Via je claude.ai connector instellingen. Zonder dit blijft `/ads-auto-optimize` acht dagen op rij een leeg rapport produceren. Dit is de enige actie die het command zelf deblokkeert.

**2. Sluit interne verwijzers uit in PostHog**
Uitsluiten: `sempertexeurope.com`, `rezolvbv-sh-sempertex.odoo.com`, `mollie.com` en de shipping-portal. Reden: 95,7% van je Referral-cijfer is ruis, waardoor elke kanaalvergelijking scheef staat. Verwachte impact: Referral zakt van 187 naar ongeveer 8 bezoekers, en pas dan zie je wat externe verwijzing echt oplevert. Vijf minuten werk.

**3. Zet conversie-events op de SYBB pagina's**
Zonder conversie-event is er geen ROAS, en zonder ROAS werkt de 70-20-10 regel niet. De Core-categorie kent twee ingangen: Link CTR met CPC (link), of ROAS > 2x. Nu heb je er nul van de twee. Let op de bevinding uit het geheugen: SYBB verkoopt via de event pagina's op sempertexeurope.com, niet via de landing page, dus meet daar.

**4. Fix de UTM-conventie voordat er verkeer komt**
Alles lowercase, `utm_content` met underscores in plaats van komma's, format `utm_source=meta`, `utm_medium=cpc`, `utm_campaign=sybb`. Als je nu launcht zonder dit, is de eerste week aan data alsnog niet toe te wijzen aan een ad.

**5. Onderzoek het AI-kanaal**
28 bezoekers over drie dagen vanuit ChatGPT, zonder budget en zonder inspanning. Dat is meer dan Organic Social en Email samen. Losstaand van Meta, maar het is gratis verkeer dat je niet meet.

---

## Aanbeveling

Geen euro naar Meta tot voorstel 2, 3 en 4 staan. De kill-regels van dit command zijn precies zo goed als de data die eronder ligt, en op dit moment ligt er niets.

Voorstel 2 tot en met 5 hebben Pipeboard niet nodig. Die kun je vandaag zelf uitvoeren.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

---

*Log: run uitgevoerd 15 augustus 2026. Niveau 1 acties: 0 uitgevoerd, reden: Pipeboard Meta Ads MCP niet geautoriseerd. Niveau 2 voorstellen: 5, allen wachtend op goedkeuring.*
