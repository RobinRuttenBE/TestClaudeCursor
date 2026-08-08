# Auto-Optimize Rapport, 8 augustus 2026

**Status: niet uitgevoerd. De run is geblokkeerd op ontbrekende Meta Ads data.**

De Pipeboard Meta Ads connector is in deze sessie niet geautoriseerd. Stap 1 tot en met 3 van `/ads-auto-optimize` konden daardoor niet draaien. Geen campagnes, geen ad sets, geen ads, geen insights. Zonder `actions.link_click`, `impressions` en `spend` op ad niveau zijn de kill-regels niet te evalueren.

Derde dag op rij dat Pipeboard blokkeert. Zie ook `2026-08-08_ads_report.md` en het rapport van 7 augustus.

Autoriseren kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie.

Google MCPs zijn niet aangeroepen. Er is niets naar de Meta Ads Tracker Google Sheet geschreven.

---

## Automatische acties uitgevoerd

**Geen. Er zijn nul ads gepauzeerd.**

Dit is een blokkade, geen goedkeuring. Lees dit nadrukkelijk niet als "alles presteert boven de drempelwaarden". Er is simpelweg geen data om tegen de drempels te leggen.

| Regel | Drempel | Evaluatie |
|-------|---------|-----------|
| Lage Link CTR | Link CTR < 0,8% bij ≥ 1.000 impressions | Niet evalueerbaar, geen ad data |
| Hoge CPC (link) | CPC (link) > €1,50 bij ≥ 500 link clicks | Niet evalueerbaar, geen ad data |

## Waarschuwingen

Frequency en CPM komen uitsluitend uit Meta. Niet evalueerbaar.

## 70-20-10 Classificatie

Niet uitgevoerd. Classificatie vereist Link CTR en CPC (link) per ad.

Los daarvan staat de kalibratie-TODO in het command nog open: de 70-20-10 drempels zijn nog gebaseerd op all-clicks metrics en zijn niet omgezet naar link metrics. Ook met werkende data zou een budget-shift op die drempels voorbarig zijn.

---

## Wat PostHog wel laat zien over dezelfde 3 dagen

Dit is de belangrijkste bevinding van vandaag, en die verandert de prioriteit.

**Er is geen betaald verkeer. Nul sessies.** Over 5 tot 8 augustus bestaat het kanaal Paid Social niet in de PostHog data, en op UTM niveau staat er geen enkele `meta / cpc` regel.

Kanaalverdeling 3 dagen (2.888 bezoekers totaal):

| Kanaal | Bezoekers | Pageviews | Bounce rate | Aandeel |
|--------|-----------|-----------|-------------|---------|
| Direct | 2.053 | 9.035 | 66,3% | 71,1% |
| Referral | 544 | 2.973 | 66,8% | 18,8% |
| Organic Search | 214 | 3.219 | 4,7% | 7,4% |
| Email | 50 | 179 | 25,0% | 1,7% |
| AI | 22 | 102 | 18,2% | 0,8% |
| Organic Video | 4 | 8 | 25,0% | 0,1% |
| Organic Social | 1 | 1 | 100% | 0,0% |
| **Paid Social** | **0** | **0** | n.v.t. | **0,0%** |

De enige campagne-getagde bron van betekenis is `mailjet / email / workshop_tobi_promo_202608` met 43 bezoekers.

Dit betekent dat er in de optimalisatie-window vrijwel zeker geen ads hebben gedraaid. Er valt dus ook niets te pauzeren. De juiste conclusie is niet "de optimizer is stuk", maar "er is geen campagne om te optimaliseren".

Kanttekening: als er ads liepen met kapotte of ontbrekende UTM tags, zou PostHog ze als Direct binnenkrijgen en zou dit beeld misleidend zijn. Direct staat op 71,1% met een bounce rate van 66,3%, wat hoog is. Dat kan ik niet uitsluiten zonder Meta data. Het blijft dus een sterk signaal, geen bewijs.

**Organic Search bounce rate van 4,7%** valt op tegen 66,3% Direct en 56,0% site breed. Dat is een verdacht laag getal. Waarschijnlijk een meetartefact, geen echte performance. Het verdient een aparte controle, niet nu.

---

## Voorstellen (wacht op goedkeuring)

Budget herverdeling, nieuwe variaties en audience aanpassingen zijn niet te onderbouwen zonder ad data. Ieder concreet bedrag zou verzonnen zijn. Wat wel te doen is:

**1. Autoriseer Pipeboard**
Dit blokkeert alles. Drie dagen zonder ads data betekent ook drie dagen zonder kill-regels. Als er wel budget liep in die periode, is er potentieel geld weggelopen op ads die allang gepauzeerd hadden moeten zijn.

**2. Bevestig of er überhaupt campagnes actief zijn**
PostHog wijst op nul betaald verkeer sinds 1 juli. Als de campagnes uit staan, is de eerste vraag niet welke ad je pauzeert maar wanneer je herstart.

**3. Fix de UTM casing voor je herstart**
Er lopen twee varianten naast elkaar, `meta/cpc/sybb` met 1.141 personen en `META/cpc/SYBB` met 189. PostHog telt dat als twee bronnen. Bij herstart zit ongeveer 14% van je betaalde verkeer in een aparte bucket en valt buiten iedere cross-reference tussen Meta en PostHog.

**4. Kalibreer de 70-20-10 drempels voor link metrics**
De TODO in het command staat nog open. Link CTR ligt structureel op ongeveer 50 tot 60% van all-clicks CTR, CPC (link) ligt 1,5 tot 3 keer hoger. De huidige getallen classificeren daardoor te streng. Dit wil je vastgesteld hebben voordat er weer budget loopt, niet erna.

**5. Zet conversie events op de SYBB pagina**
De pixel meet nu alleen pageviews en autocapture. Zonder CTA en booking events is er geen conversiekant om ads tegen af te rekenen, ook niet als Pipeboard weer werkt.

---

## Log

| Tijd | Actie | Resultaat |
|------|-------|-----------|
| 2026-08-08 | Meta Ads MCP (Pipeboard) aangeroepen | Geblokkeerd, niet geautoriseerd |
| 2026-08-08 | PostHog kanaalverdeling 3 dagen | Nul Paid Social sessies |
| 2026-08-08 | PostHog UTM breakdown 3 dagen | Geen `meta / cpc` regel aanwezig |
| 2026-08-08 | Kill-regels geëvalueerd | Niet uitgevoerd, geen data |
| 2026-08-08 | Ads gepauzeerd | 0 |

Bron: PostHog project STX EU (149694). Meta account `act_567892422940728` en `act_607231713057715` niet bereikbaar.
