# Auto-Optimize Rapport, 11 August 2026

**Status: niet uitgevoerd. Meta Ads MCP (Pipeboard) is niet geautoriseerd.**

Bronnen deze run: alleen Meta Ads MCP (poging) en PostHog MCP. Geen Google MCPs aangeroepen, niet naar de Meta Ads Tracker Google Sheet geschreven.

---

## Blokkade

De Pipeboard connector vereist autorisatie en deze sessie is non-interactief, dus de OAuth flow kan hier niet draaien. Dit is de vijfde dag op rij met dezelfde blokkade (zie `2026-08-10_auto_optimize.md`). Het `2026-08-11_ads_report.md` van vanochtend is afgebroken op een API fout en bevat geen bruikbare data om op terug te vallen.

Zonder ad-level insights zijn er geen impressions, link clicks of spend. Gevolg:

| Stap | Status |
|------|--------|
| 1. Performance data ophalen (act_567892422940728, act_607231713057715) | Niet uitgevoerd |
| 2. Kill-regels evalueren (Link CTR, CPC link) | Niet geëvalueerd |
| 3. Automatische acties (Niveau 1) | **0 ads gepauzeerd** |
| 4. 70-20-10 classificatie | Vervalt |
| 5. Budget verdeling | Vervalt |
| 6. Voorstellen (Niveau 2) | Vervalt |

**Belangrijk:** nul gepauzeerde ads betekent hier niet dat alles boven de drempelwaarden presteert. Er viel niets te meten.

**Oplossen:** autoriseer de Pipeboard connector via je claude.ai connector instellingen, of via `/mcp` in een interactieve Claude Code sessie. Dat kan alleen jij doen.

---

## Wat PostHog wel laat zien

### UTM medium, laatste 45 dagen

| Medium | Visitors | Pageviews | Aandeel |
|--------|---------:|----------:|--------:|
| (geen UTM) | 16.933 | 115.485 | 98,2% |
| email | 290 | 568 | 1,7% |
| organic | 17 | 26 | 0,1% |
| **cpc** | **1** | **2** | **0,0%** |
| referral | 1 | 2 | 0,0% |

Eén enkele bezoeker met `utm_medium=cpc` in 45 dagen. Dat is ruis, geen campagne.

### UTM bron, laatste 3 dagen (2.332 visitors totaal)

| Bron / medium / campagne | Visitors | Aandeel |
|--------------------------|---------:|--------:|
| direct | 1.662 | 71,3% |
| www.sempertexeurope.com (intern referral) | 362 | 15,5% |
| www.google.com | 216 | 9,3% |
| chatgpt.com | 37 | 1,6% |
| www.bing.com | 11 | 0,5% |
| t-sml.mtrbio.com | 10 | 0,4% |
| mailjet / email / inspiration_promo_202607 | 4 | 0,2% |
| mailjet / email / workshop_tobi_promo_202608 | 3 | 0,1% |
| facebook.com + www.facebook.com (organic referral) | 4 | 0,2% |
| Klaviyo / email | 1 | 0,0% |

**Geen enkele rij met `meta / cpc / sybb`.** De 4 Facebook bezoekers komen binnen als organic referral zonder UTM tagging, niet als betaald verkeer.

---

## Wat dit betekent

Er zijn twee scenario's en je kunt ze op basis van deze data niet uit elkaar houden:

1. **De campagnes staan uit.** Dan valt er niets te optimaliseren en is de MCP blokkade vooral vervelend, niet duur.
2. **De campagnes draaien en de UTM tagging is stuk.** Dan verbrand je dagelijks budget dat je in PostHog niet terugziet, en draait het auto-optimize systeem blind. Elke dag die je wacht kost geld.

Scenario 2 is het dure scenario en het is in twee minuten uit te sluiten, ook zonder Pipeboard: log in op Meta Ads Manager en kijk of campagne `2026: SYBB` actief is en spend heeft over de laatste 3 dagen.

---

## Top acties

1. **Check Meta Ads Manager handmatig** op actieve spend in de laatste 3 dagen. Dit is de enige actie die scenario 1 van scenario 2 scheidt.
2. **Autoriseer de Pipeboard connector.** Vijf dagen zonder ads data betekent vijf dagen zonder kill-regels, dus underperformers draaien ongemoeid door zodra campagnes wel live gaan.
3. **Als er wél spend is:** controleer de UTM tagging op ad-niveau tegen de conventie (`utm_source=meta`, `utm_medium=cpc`, `utm_campaign=sybb`, `utm_content=hXX_bX_ctaX`, `utm_term=batch_X`, alles lowercase). Nul `cpc` sessies bij actieve spend wijst op ontbrekende of verkeerd gespelde parameters in de ad URLs.
4. **Zet bot filtering aan in PostHog** voordat je de cross-reference analyses weer vertrouwt. De 98,2% verkeer zonder UTM over 45 dagen is deels crawler traffic (zie de crawler bevinding van 10 August).

---

## Voorstellen (Niveau 2)

Geen. Alle budget-, variatie- en audience-voorstellen zijn afgeleid van ad performance data en die ontbreekt volledig.
