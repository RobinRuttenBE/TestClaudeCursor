# Auto-Optimize Rapport, 12 augustus 2026

**De run is geblokkeerd. Vijfde dag op rij.**

De Pipeboard Meta Ads connector is in deze sessie niet geautoriseerd, en dit is een niet-interactieve sessie, dus de OAuth flow kan hier niet starten. Zonder ad-level `impressions`, `actions.link_click` en `spend` zijn de kill-regels niet te evalueren.

Stappen 1 tot en met 6 van het command konden niet draaien. Beide ad accounts (`act_567892422940728` en `act_607231713057715`) waren onbereikbaar.

Zoals gevraagd: geen enkele Google MCP aangeroepen, niet naar de Meta Ads Tracker Google Sheet geschreven. Alleen PostHog is gebruikt, plus dit lokale bestand.

---

## ⚡ Automatische acties uitgevoerd

**Gepauzeerd: 0 ads.**

Lees dit niet als "alles presteert boven de drempelwaarden". Er is niets beoordeeld. Het verschil is belangrijk genoeg om elke dag te herhalen.

| Regel | Drempel | Status vandaag |
|-------|---------|----------------|
| Lage Link CTR | Link CTR < 0,8% bij ≥ 1.000 impressions | Niet geëvalueerd, geen data |
| Hoge CPC (link) | CPC (link) > €1,50 bij ≥ 500 link clicks | Niet geëvalueerd, geen data |

---

## ⚠️ Waarschuwingen

Creative fatigue, CPM en Link CTR verval zijn allemaal Meta-metrics. Geen van de drie is te controleren zonder Pipeboard.

Wel één waarschuwing die niet uit Meta komt:

| Signaal | Waarde | Actie aanbevolen |
|---------|--------|------------------|
| Sessiedaling zet door | Negen dagen op rij, min 59,6% | Onderzoek de bron voordat je ads herstart |

---

## 📊 70-20-10 Classificatie

Niet uitvoerbaar. De classificatie is volledig afgeleid van Link CTR, CPC (link) en ROAS per ad.

**Budget mismatch:** onbekend.

---

## Wat PostHog wel bevestigt

### Nul betaald verkeer, nog steeds

Over de afgelopen 3 dagen bestaat het kanaal Paid Social niet in de kanaalverdeling. Op UTM niveau staat er over 30 dagen geen enkele `meta / cpc / sybb` regel.

| Kanaal | Bezoekers (3d) | Aandeel | Bounce rate |
|--------|---------------|---------|-------------|
| Direct | 1.167 | 67,9% | 67,4% |
| Referral | 285 | 16,6% | 43,2% |
| Organic Search | 212 | 12,3% | 1,7% |
| AI | 36 | 2,1% | 2,7% |
| Email | 13 | 0,8% | 15,4% |
| Organic Social | 6 | 0,3% | 16,7% |
| **Paid Social** | **0** | **0,0%** | n.v.t. |

Site breed over 3 dagen: 1.636 bezoekers, 14.840 pageviews, 1.882 sessies, sessieduur 5m44s, bounce 53,0%.

De enige betaalde regels in de UTM verdeling over 30 dagen zijn email, geen ads:

| Bron / medium / campagne | Bezoekers |
|--------------------------|-----------|
| mailjet / email / inspiration_promo_202607 | 140 |
| Klaviyo / email / (none) | 109 |
| mailjet / email / workshop_tobi_promo_202608 | 46 |

Klaviyo staat nog steeds zonder `utm_campaign`. 109 bezoekers die je niet kunt toewijzen aan een mail.

### De sessiedaling is niet gestopt

Negen dagen ononderbroken, geen enkele dag omhoog:

| Datum | Sessies |
|-------|---------|
| 3 aug | 1.271 |
| 4 aug | 1.137 |
| 5 aug | 1.022 |
| 6 aug | 964 |
| 7 aug | 893 |
| 8 aug | 827 |
| 9 aug | 713 |
| 10 aug | 631 |
| 11 aug | 514 |

Van 1.271 naar 514, min 59,6%. Gisteren stond de teller op acht dagen, vandaag op negen. Dit is geen ruis meer, dit is een trend met een oorzaak.

Direct is 67,9% van je volume en tegelijk je slechtste bounce rate (67,4%). Daar zit het verlies, en daar begint het onderzoek.

Organic Search blijft de uitschieter: 212 bezoekers met 1,7% bounce rate. Dat is verkeer dat precies vindt wat het zoekt, en het kost geen budget.

---

## 💡 Voorstellen (wacht op goedkeuring)

Budget-, variatie- en audience-voorstellen vervallen. Alle drie zijn afgeleid van performance data die er niet is. Ik verzin geen voorstellen op basis van niets.

Wat er wel ligt, in volgorde:

**1. Autoriseer Pipeboard.** Via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Dit blokkeert nu vijf dagen op rij het volledige optimalisatieproces. Zolang dit dicht staat is een dagelijkse auto-optimize run zinloos.

**2. Onderzoek de sessiedaling.** Begin bij Direct, 67,9% van je volume. Check wat er rond 3 augustus veranderde op de site of in de tracking. Negen dagen min 59,6% is groter dan elk ad-optimalisatie effect dat je hierna zou boeken.

**3. Zet conversie events op de SYBB landing page** voordat je ads herstart. Zonder conversie events meet je straks alleen klikken, geen resultaat.

**4. Tag de Klaviyo mails met `utm_campaign`.** 109 bezoekers over 30 dagen die je nu niet kunt toewijzen.

**5. Fix de UTM casing naar lowercase** volgens de conventie in `CLAUDE.md`, en vervang komma's in `utm_content` door underscores.

**6. Zet Organic Search harder in.** 1,7% bounce rate, nul kosten. Dit is het goedkoopste kanaal dat je nu hebt.

**7. Pas daarna herstarten volgens 70-20-10.**

Punt 2 tot en met 6 hebben Pipeboard niet nodig. Daar kun je vandaag mee beginnen.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

---

### Databronnen

- PostHog MCP, project STX EU (149694), tijdzone UTC
- Meta Ads MCP (Pipeboard): **niet beschikbaar, niet geautoriseerd**
- Geen Google MCPs aangeroepen, geen schrijfacties naar Google Sheets

*Opmerking bij de cijfers: het sessie-aantal in de dagtabel komt uit unieke sessies op `$pageview` en telt iets anders dan de web analytics sessies in het 3-daagse overzicht. De trend is in beide identiek, het niveau verschilt door de sessiedefinitie en de UTC dagafbakening. 12 augustus is nog niet compleet en staat daarom niet in de tabel.*
