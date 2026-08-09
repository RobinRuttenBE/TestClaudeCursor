# Auto-Optimize Rapport, 9 augustus 2026

**Status: geblokkeerd.** De Pipeboard Meta Ads connector is in deze sessie niet geautoriseerd. Stap 1 tot en met 6 van het optimalisatieproces konden niet draaien. Er zijn geen ads gepauzeerd, geen classificaties gemaakt en geen budgetvoorstellen berekend. Dit is de derde dag op rij dat de connector ontbreekt.

Alleen de Meta Ads MCP en de PostHog MCP zijn benaderd. Geen Google MCPs, niet naar de tracker Google Sheet geschreven, zoals gevraagd.

---

## Automatische acties uitgevoerd

**Geen.** Niet omdat alles boven de drempelwaarden presteert, maar omdat de data ontbreekt.

| Wat | Status | Reden |
|-----|--------|-------|
| Kill regel Link CTR < 0,8% | Niet uitgevoerd | Geen impressions of link clicks beschikbaar |
| Kill regel CPC (link) > EUR 1,50 | Niet uitgevoerd | Geen spend of link clicks beschikbaar |
| 70-20-10 classificatie | Niet uitgevoerd | Geen ad niveau performance data |
| Budget herverdeling | Niet uitgevoerd | Geen huidige budgetten bekend |

**Totaal gepauzeerd: 0 ads.**

Belangrijk onderscheid: dit is geen "alles is gezond" uitkomst. Het systeem heeft vandaag geen enkele ad kunnen beoordelen. Als er op dit moment ads draaien die geld verbranden, zou dit rapport dat niet zien.

---

## Wat PostHog wel bevestigt

PostHog ziet klikken, geen impressions of spend. Binnen die grens is het beeld eenduidig.

**Nul betaald verkeer over de afgelopen 3 dagen.** Geen enkele sessie met `utm_source=meta` en `utm_medium=cpc`. Het kanaal Paid Social komt in de kanaalverdeling helemaal niet voor.

Kanaalverdeling, 6 tot en met 9 augustus, 2.662 bezoekers totaal:

| Kanaal | Bezoekers | Aandeel |
|--------|-----------|---------|
| Direct | 1.933 | 72,6% |
| Referral | 485 | 18,2% |
| Organic Search | 202 | 7,6% |
| AI | 23 | 0,9% |
| Email | 12 | 0,5% |
| Organic Video | 5 | 0,2% |
| Organic Social | 2 | 0,1% |
| **Paid Social** | **0** | **0,0%** |

De laatste geregistreerde `meta/cpc/sybb` klik dateert van 1 juli 2026. Dat is nu 39 dagen geleden.

### Wat dit wel en niet betekent

**Wel:** er komt geen betaald verkeer op de site aan. Als er ads actief zijn, leveren die nul klikken op.

**Niet:** dit bewijst niet dat er nul spend is. Een ad kan impressions draaien en budget opmaken zonder een enkele klik. Dat scenario, spend zonder klikken, is precies waar de kill regels voor bestaan, en juist dat scenario is nu onzichtbaar. Alleen Pipeboard kan dit onderscheid maken.

---

## Waarschuwingen

| Signaal | Waarde | Actie |
|---------|--------|-------|
| Creative fatigue (frequency > 3,5) | Niet meetbaar | Vereist Pipeboard |
| Dure reach (CPM > EUR 15,00) | Niet meetbaar | Vereist Pipeboard |
| Dalende Link CTR | Niet meetbaar | Vereist Pipeboard |
| Connector uitval | 3 dagen op rij | Autoriseer Pipeboard |

De connector uitval is zelf de belangrijkste waarschuwing. Drie dagen zonder zicht op de ad accounts betekent dat een ad die vandaag ontspoort pas over dagen wordt opgemerkt.

---

## Losse observatie uit de PostHog data

De Mailjet campagne `workshop_tobi_promo_202608` bracht 11 bezoekers in 3 dagen en is netjes getagd op bron, medium en campagne. Dat is de eerste correct getagde email campagne die ik in deze periode zie.

Klaviyo staat er anders bij: `Klaviyo / email / (none)`, dus zonder `utm_campaign`. Die bezoekers zijn niet toewijsbaar aan een specifieke mail. Het Mailjet patroon is de standaard die Klaviyo ook zou moeten volgen.

---

## Voorstellen (wacht op goedkeuring)

Zonder performance data kan ik geen budget of creative voorstellen onderbouwen. Wat ik wel kan voorstellen is het opheffen van de blokkade en het voorbereiden van de meting.

**1. Autoriseer Pipeboard**
Dit blokkeert al het andere. Kan via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Zolang dit open staat draait `/ads-auto-optimize` elke ochtend leeg en heeft de automatische bewaking geen effect.

**2. Controleer handmatig in Meta Ads Manager of er spend loopt**
Dit kost twee minuten en beantwoordt de vraag die PostHog niet kan beantwoorden. Kijk naar spend over de laatste 3 dagen op `act_567892422940728` en `act_607231713057715`. Bij spend groter dan nul met nul link clicks: pauzeer de campagne direct met de hand, want dan verbrandt er budget zonder resultaat. Bij spend gelijk aan nul: er is niets aan de hand behalve dat er niets draait.

**3. Tag Klaviyo mails met utm_campaign**
Volg het Mailjet formaat. Heeft Pipeboard niet nodig en kan vandaag.

**4. Stel de 70-20-10 drempels voor link metrics vast**
De drempels in het command staan nog gemarkeerd als richtlijn, niet als hard oordeel, sinds de overstap van all clicks naar link metrics op 13 april. Zodra Pipeboard weer data levert wil je die getallen scherp hebben, anders classificeert het systeem op waarden die op een andere metriek zijn geijkt. Dit is een beslissing die van jou moet komen.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

---

*Gegenereerd 9 augustus 2026. Databronnen: PostHog MCP (project STX EU, id 149694). Meta Ads MCP niet beschikbaar.*
