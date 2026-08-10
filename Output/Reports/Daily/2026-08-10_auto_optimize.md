# Auto-Optimize Rapport, 10 augustus 2026

**Status: niet uitgevoerd. De Meta Ads connector (Pipeboard) is in deze sessie niet geautoriseerd.**

Zonder ad-level insights kan geen enkele stap van dit command draaien. Geen impressions, geen link clicks, geen spend, dus geen Link CTR en geen CPC (link). De kill-regels hebben per definitie geen input, en `update_ad` is niet aanroepbaar om iets te pauzeren. Dit is de vierde dag op rij dat de connector blokkeert, zie ook `2026-08-10_ads_report.md`.

Conform de opdracht zijn uitsluitend de Meta Ads MCP en de PostHog MCP benaderd. Geen Google MCPs, niet naar de tracker Sheet geschreven.

---

## ⚡ Automatische acties uitgevoerd

**Geen. Nul ads gepauzeerd.**

Dit is nadrukkelijk geen "alles presteert boven de drempelwaarden". Het is een datablokkade. De kill-regels zijn niet geëvalueerd:

| Regel | Drempel | Minimum data | Status |
|-------|---------|--------------|--------|
| Lage Link CTR | Link CTR < 0,8% | ≥ 1.000 impressions | Niet evalueerbaar, geen data |
| Hoge CPC (link) | CPC (link) > €1,50 | ≥ 500 link clicks | Niet evalueerbaar, geen data |

Beide accounts, `act_567892422940728` en `act_607231713057715`, zijn onbereikbaar.

## ⚠️ Waarschuwingen

Frequency, CPM en Link CTR trend zijn evenmin evalueerbaar. Wel één signaal uit PostHog dat losstaat van de connector.

**Nul betaald verkeer, zeven dagen op rij.** Verkeersverdeling over `$pageview` events, laatste 7 dagen:

| Bron | Medium | Campagne | Pageviews | Personen |
|------|--------|----------|-----------|----------|
| (geen) | (geen) | (geen) | 32.973 | 5.908 |
| chatgpt.com | (geen) | (geen) | 92 | 64 |
| mailjet | email | workshop_tobi_promo_202608 | 59 | 47 |
| youtube | organic | content | 6 | 4 |
| klaviyo | email | (geen) | 5 | 5 |
| mailjet | email | inspiration_promo_202607 | 4 | 3 |
| partner | referral | distributor_evergreen_202607 | 1 | 1 |
| pinterest | organic | (geen) | 1 | 1 |
| newsletter | email | fr_client | 1 | 1 |

Geen enkele `meta` bron en geen enkele `cpc` medium. Nul. De laatste betaalde klik dateert van 1 juli 2026. Dat betekent dat er in het 3-daagse optimalisatievenster hoogstwaarschijnlijk sowieso niets te optimaliseren viel, omdat er niets levert. Dat is een aanname op basis van de landingskant, geen bevestiging vanuit Meta, want die kant is dicht.

Twee mogelijkheden, en het onderscheid is belangrijk:
1. De campagnes staan uit of hebben geen budget. Dan is auto-optimize irrelevant tot ze weer draaien.
2. De campagnes draaien wel en de tracking is stuk. Dan verbrand je geld dat je niet ziet.

Zolang Pipeboard dicht is, kun je niet vaststellen welke van de twee het is. Dat is het echte risico van deze blokkade, niet het gemiste rapport.

Let ook op die 32.973 pageviews zonder enige bron over 5.908 personen. In combinatie met de crawler-bevinding uit het ads rapport van vanochtend, 2.579 diepe instappen zonder referrer sinds 6 augustus, is dat cijfer vervuild. Zet bot filtering aan voordat je hier conclusies aan verbindt.

## 📊 70-20-10 Classificatie

Niet uitgevoerd. Classificatie vereist Link CTR, CPC (link) en impressions per ad.

Los daarvan staat de kalibratie van deze drempels nog open. Het command markeert de 70-20-10 grenzen zelf als TODO sinds de overstap van all-clicks naar link metrics op 13 april. De Core-grens van Link CTR > 1,5% is overgenomen uit de all-clicks periode en valt op link clicks structureel te streng uit. Zodra er weer data is, is dit het eerste wat scheef gaat staan.

## 💡 Voorstellen (wacht op goedkeuring)

Budget-, variatie- en audience-voorstellen zijn allemaal afgeleiden van de performance data. Zonder die data zou elk voorstel verzonnen zijn. Er zijn er dus geen.

Wat wel openstaat, is de blokkade zelf.

**1. Autoriseer Pipeboard**
Dit blokkeert dit command volledig en het ads rapport grotendeels. Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Ik kan dit niet zelf, de sessie is non-interactief.

**2. Controleer handmatig in Meta Ads Manager of er campagnes leveren**
Dit kost twee minuten en beantwoordt de vraag hierboven. Staan de SYBB campagnes op ACTIVE met spend in de laatste drie dagen? Zo ja, dan is er een trackinggat tussen de ads en de site en verlies je nu geld zonder zicht. Zo nee, dan is er niets aan de hand en kan auto-optimize wachten.

**3. Zet bot filtering aan in PostHog**
Onafhankelijk van Pipeboard. Je bounce rate, sessieduur en pageview cijfers zijn nu vervuild door crawlers, wat elke cross-reference tussen ads en landing page onbetrouwbaar maakt zodra de ads wel weer draaien.

---

**Er is niets goed te keuren zolang de connector dicht is. Punt 2 en 3 hebben Pipeboard niet nodig en kun je vandaag doen.**
