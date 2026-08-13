# Auto-Optimize Rapport, 13 augustus 2026

**Status: niet uitgevoerd. Meta Ads MCP (Pipeboard) is niet geautoriseerd in deze sessie.**

Stap 1 tot en met 6 van `/ads-auto-optimize` konden niet draaien. Zonder campagne-, ad set- en ad-data zijn er geen impressions, geen `actions.link_click` en geen spend, dus de kill-regels hebben geen invoer. Er is ook geen schrijftoegang tot `update_ad`, dus zelfs bij een terechte pauze-beslissing kon die niet worden doorgevoerd.

Alleen de PostHog MCP was beschikbaar. Google MCPs zijn niet aangeroepen en er is niet naar de Google Sheet tracker geschreven, conform de instructie voor deze run.

---

## ⚡ Automatische acties uitgevoerd

**Geen. Nul ads geëvalueerd, nul ads gepauzeerd.**

> Let op het verschil: dit is **niet** "alles presteert boven de drempelwaarden". Er is geen enkele ad beoordeeld. Lees dit rapport niet als goedkeuring van de huidige ad-set.

| Kill-regel | Drempel | Minimum data | Resultaat |
|---|---|---|---|
| Lage Link CTR | Link CTR < 0.8% | ≥ 1.000 impressions | Niet evalueerbaar, geen data |
| Hoge CPC (link) | CPC (link) > €1.50 | ≥ 500 link clicks | Niet evalueerbaar, geen data |

**Totaal gepauzeerd: 0 ads**

---

## ⚠️ Waarschuwingen

De waarschuwingsregels (frequency > 3.5, CPM > €15, dalende Link CTR) draaien allemaal op Meta-velden en zijn dus niet berekenbaar.

Wat PostHog wél laat zien over de laatste 3 dagen:

| Signaal | Waarde | Betekenis |
|---|---|---|
| Paid Social sessies | 0 | Geen enkele betaalde klik binnengekomen |
| Paid Search sessies | 0 | Kanaal ontbreekt volledig in de verdeling |
| `meta / cpc / sybb` getagde sessies | 0 | Geen SYBB campagneverkeer |
| Facebook verwijzingen | 5 sessies | Organisch, geen ad-clicks |
| Self-referral `www.sempertexeurope.com` | 236 sessies (18,2%) | Attributie nog steeds kapot |

Kanaalverdeling laatste 3 dagen, 1.299 sessies totaal: Direct 766 (59,0%), Referral 253 (19,5%), Organic Search 227 (17,5%), AI 35 (2,7%), Email 9 (0,7%), Organic Social 9 (0,7%).

**Er draait geen betaald verkeer.** Dat is consistent met het ads-rapport van vanochtend: laatste betaalde klik 14 juli 2026. Of er nog ACTIVE ads in Meta staan die budget verbranden zonder clicks te leveren, kan ik niet zien zonder Pipeboard. Dat is precies het scenario waarvoor dit command bestaat, en precies wat nu blind is.

---

## 📊 70-20-10 Classificatie

Niet uitvoerbaar. Classificatie vereist Link CTR en CPC (link) per ad.

Ter herinnering, uit de command-definitie: de 70-20-10 drempels staan sowieso nog als **TODO, nog te kalibreren voor link metrics**. Ze waren gezet op all-clicks. Ook mét Pipeboard zou de classificatie vandaag richtinggevend zijn geweest, geen hard oordeel, en zouden er geen budget-shifts op zijn uitgevoerd.

**Budget mismatch:** onbekend.

---

## 💡 Voorstellen (wacht op goedkeuring)

Budget-, variatie- en audience-voorstellen vragen allemaal om performance-data en vervallen daarmee. Wat overblijft zijn de blokkades die vóór een herstart opgelost moeten zijn.

**1. Autoriseer Pipeboard**
Zonder dit blijft `/ads-auto-optimize` zes dagen op rij een lege huls. Autoriseren via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Ik kan dit niet zelf.

**2. Zet de referral exclusions in PostHog**
Sluit uit als verwijzer: `sempertexeurope.com`, `mollie.com` (inclusief `pay.mollie.nl` en `payment-links.mollie.com`), `rezolvbv-sh-sempertex.odoo.com`, `sempertexeurope.shipping-portal.com`.
Reden: 236 self-referral sessies in 3 dagen, plus Mollie en Odoo terugkeerverkeer. Sessies breken op, de oorspronkelijke bron verdwijnt naar Direct.
Verwachte impact: Direct zakt fors onder de huidige 59,0%, en Meta-clicks krijgen straks een eerlijke attributie. Doe je dit niet vóór de herstart, dan reken je Meta af op cijfers die het systeem zelf verzint.

**3. Conversie events op de SYBB pagina vóór herstart**
Zonder conversie-events blijft ROAS leeg en werkt de 70% Core regel ("ads met ROAS > 2x") niet, ook niet ná autorisatie.

**4. Herzie de 70-20-10 drempels voor link metrics**
De TODO in het command staat nog open. Link CTR ligt structureel op ongeveer 50 tot 60% van all-clicks CTR, CPC (link) ligt 1,5 tot 3 keer hoger. Stel nieuwe waarden vast, dan kan de volgende run wél classificeren en budget verschuiven.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.** Punt 2, 3 en 4 hebben Pipeboard niet nodig.

---

## Log

| Timestamp | Actie | Reden |
|---|---|---|
| 2026-08-13 | Kill-regels overgeslagen | Pipeboard niet geautoriseerd, geen ad-data |
| 2026-08-13 | 70-20-10 classificatie overgeslagen | Geen Link CTR of CPC (link) beschikbaar |
| 2026-08-13 | PostHog kanaal- en UTM-analyse uitgevoerd, 3 dagen | Enige beschikbare bron, bevestigt 0 betaalde sessies |
| 2026-08-13 | Google MCPs niet aangeroepen, Sheet niet beschreven | Instructie voor deze run |
