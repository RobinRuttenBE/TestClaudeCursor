# Auto-Optimize Rapport, 19 augustus 2026

**Uitgevoerd:** 19 augustus 2026
**Databronnen:** Meta Ads MCP (Pipeboard) en PostHog MCP. Google MCPs en de Tracker Google Sheet zijn niet aangeroepen, conform de instructie voor deze run.

---

## Status: geen optimalisatie mogelijk

**Pipeboard is niet geautoriseerd, twaalfde dag op rij.** Stap 1 tot en met 6 van het command konden niet draaien. Zonder `get_campaigns`, `get_adsets`, `get_ads` en `get_insights` is er geen spend, geen impressions, geen link clicks, geen Link CTR, geen CPC (link), geen frequency en geen CPM.

Autoriseren kan niet vanuit deze sessie (non-interactief, geen OAuth flow). Het gaat via je claude.ai connector instellingen, of via `/mcp` in een interactieve Claude Code sessie.

Beide accounts konden niet worden gelezen:

| Account | Rol | Status |
|---|---|---|
| `act_567892422940728` | Sempertex, primair | Niet bereikbaar, MCP niet geautoriseerd |
| `act_607231713057715` | Secundair | Niet bereikbaar, MCP niet geautoriseerd |

---

## PostHog bevestigt: er draait niets

De autorisatie is niet de enige reden dat er niets te optimaliseren valt. PostHog laat over de afgelopen 3 dagen zien dat er geen enkele betaalde Meta sessie op de site is aangekomen.

**Kanalen, laatste 3 dagen:**

| Kanaal | Bezoekers | Aandeel |
|---|---|---|
| Direct | 4.316 | 89,7% |
| Organic Search | 244 | 5,1% |
| Referral | 203 | 4,2% |
| AI | 36 | 0,7% |
| Organic Social | 9 | 0,2% |
| Email | 4 | 0,1% |
| **Paid Social** | **0** | **0,0%** |
| **Paid Search** | **0** | **0,0%** |

**UTM bronnen, laatste 3 dagen:** `chatgpt.com` (36), `mailjet` (2), `Pinterest` (1), `partner` (1). Nul sessies met `utm_source=meta`. 99,1% van de sessies komt binnen zonder UTM.

Geconfronteerd met beide signalen tegelijk is de conclusie eenduidig: er staan geen actieve ads te draaien die budget verbranden. De kill-regels hebben niets om op te vuren.

---

## Automatische acties uitgevoerd (Niveau 1)

**Geen.** Nul ads gepauzeerd, nul ads aangepast.

Dit is geen "alles presteert boven de drempelwaarden". Het is een lege dataset. De kill-regels (Link CTR < 0,8% bij 1.000+ impressions, CPC (link) > EUR 1,50 bij 500+ link clicks) zijn niet toegepast omdat er geen ads en geen impressions zijn om tegen te toetsen.

Totaal spend beoordeeld: **EUR 0,00**.

---

## Waarschuwingen

Geen ad-niveau waarschuwingen mogelijk (creative fatigue, CPM, dalende Link CTR vereisen alle Meta data).

Wel een datakwaliteitswaarschuwing die de hele optimalisatie raakt zodra Meta wel gaat draaien.

### Botverkeer staat nog steeds in de nulmeting

Het patroon uit het rapport van 18 augustus is niet opgelost. Landen met exact 1,00 pageview per bezoeker, laatste 3 dagen:

| Land | Bezoekers | Pageviews | Views per bezoeker |
|---|---|---|---|
| Brazilië | 294 | 294 | 1,00 |
| Seychellen | 188 | 188 | 1,00 |
| Argentinië | 124 | 124 | 1,00 |
| Bangladesh | 79 | 79 | 1,00 |
| **Totaal** | **685** | **685** | **1,00** |

685 van circa 4.692 bezoekers, **14,6% van je verkeer**, is vrijwel zeker geen mens. Ter vergelijking: België doet 26,3 pageviews per bezoeker, Nederland 19,5.

### Nieuw signaal: Groot-Brittannië

| Land | Bezoekers | Pageviews | Views per bezoeker |
|---|---|---|---|
| **GB** | **1.127** | **1.623** | **1,44** |
| NL | 269 | 5.243 | 19,5 |
| BE | 253 | 6.652 | 26,3 |

GB is met 24,0% opeens je grootste land op bezoekers, maar doet 1,44 pageviews per bezoeker tegen 19,5 voor Nederland. Dat is dertien keer minder diep. Voor een Europese B2B ballondistributeur met de kern in de Benelux is dat een vreemde verhouding.

Dit is nog geen bewijs, 1,44 is niet de harde 1,00 van de andere clusters. Het verdient wel een check op browser- en device-verdeling van dat GB segment voordat je er conclusies aan verbindt. Als GB ook vervuild is, loopt het aandeel niet-menselijk verkeer richting 38%.

**Waarom dit nu telt:** je staat op het punt Meta aan te zetten. Elke landingspaginavergelijking (bounce rate, scroll depth, sessieduur, CTA click rate) wordt straks afgezet tegen deze nulmeting. Met 14,6% tot mogelijk 38% ruis erin wordt elk oordeel over adprestatie verkeerd, en niet voorspelbaar in één richting.

---

## 70-20-10 Classificatie

Niet uitvoerbaar. De classificatie vereist Link CTR, CPC (link) en ROAS per ad.

Ter herinnering voor de volgende run: de 70-20-10 drempels staan in het command nog gemarkeerd als **nog te kalibreren voor link metrics**. Ze waren oorspronkelijk gezet op all-clicks. Zodra Pipeboard werkt en er drie dagen data ligt, moeten die drempels eerst opnieuw vastgesteld worden voordat er budget verschoven wordt.

**Budget mismatch:** niet vast te stellen.

---

## Voorstellen (wacht op goedkeuring)

Geen budget-, variatie- of audiencevoorstellen. Die zijn allemaal afgeleid van performance data die er niet is. Voorstellen doen op basis van een lege dataset zou gokwerk zijn met een rapportopmaak eromheen.

Wat er wel ligt is een volgorde van werk. Ongewijzigd ten opzichte van gisteren, want er is niets afgevinkt:

1. **Botfilter in PostHog.** Sluit BR, SC, AR, BD uit, of filter op het 1,00 pageview patroon. Check eerst GB apart.
2. **Referrer exclusies.** 97,5% van het referral verkeer was jezelf.
3. **Pipeboard autoriseren.** Via claude.ai connector instellingen of `/mcp` in een interactieve sessie.
4. **Conversie events SYBB** inrichten in PostHog.
5. **UTM lowercase** doorvoeren. `Pinterest` staat nu met hoofdletter binnen, tegen de conventie in.

Stap 1 en 2 gaan voor. Zonder schone nulmeting is de eerste week Meta data niet te lezen.

---

## Wat de volgende run nodig heeft

Om dit command normaal te laten draaien:

- Pipeboard geautoriseerd
- Minimaal één actieve campagne met ads die 24 uur hebben gedraaid
- Minimaal 1.000 impressions per ad voor de Link CTR regel, 500 link clicks voor de CPC (link) regel
- Nieuwe 70-20-10 drempels, gekalibreerd op link metrics in plaats van all-clicks
