# SYBB Daily Report: 1 september 2026

## 1. Samenvatting
De SYBB ad campagne staat nog altijd op PAUSED (sinds 19 april 2026) en de landing page startyourballoonbusiness.com kreeg gisteren 0 bezoekers. De werkelijke SYBB funnel, de event registratiepagina's op sempertexeurope.com, draait wel: 10 bezoekers bekeken gisteren een registratiepagina, bijna dubbel het 7-daags gemiddelde van 5,6 bezoekers per dag. Al dat verkeer is organisch of intern (site navigatie, direct, e-mail), er is nul betaald verkeer richting SYBB. Conversie blijft onmeetbaar omdat er geen registratie-voltooid event bestaat.

## 2. Meta Ads Performance

**Campagne status:** `2026: SYBB` (ID 120239435987290239) staat op **PAUSED**, laatst gewijzigd 19 april 2026. De kopie `2026: SYBB - Kopie` (ID 120243293329420239) staat ook op PAUSED. Beide campagnes leverden over 25 augustus t/m 1 september nul impressies en nul spend. Het ad account zelf (act_567892422940728) is wel actief: gisteren draaide onder andere `Wholesaler Campagne (LIT)` met €101,29 spend, dat is een andere funnel en valt buiten dit rapport.

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

### Ad Variant Performance
Geen data. Zonder delivery zijn er geen variant-metrics (h11 t/m h15) te rapporteren.

Opvallend: op 28 augustus registreerde PostHog 1 pageview op de landing page met `utm_source=meta`, `utm_campaign=sybb`, `utm_content=h11_b3_cta5`, referrer direct. Omdat de campagne niet levert, is dit vrijwel zeker een handmatige test van een getagde URL, geen echte ad click. De tweede LP bezoeker die week kwam via manage.wix.com, dus ook intern.

## 3. Landing Page Health (startyourballoonbusiness.com)

| Metric | Gisteren | Afgelopen 7d | Target | Status |
|--------|----------|--------------|--------|--------|
| Bezoekers | 0 | 2 | n.v.t. | ⚪ |
| Pageviews | 0 | 2 | n.v.t. | ⚪ |
| Bounce Rate | n.v.t. | 0% | <55% | ⚪ |
| Avg Session Duration | n.v.t. | 46s | >90s | ⚪ |
| Scroll 25/50/75/100% | geen events | geen events | >80/60/40/20% | ⚪ |
| CTA Click Rate | geen events | geen events | >4% | ⚪ |

Toelichting: ⚪ = onvoldoende data om een target te beoordelen. Scroll depth en CTA click events bestaan niet in het PostHog project (bevestigd via het event schema: alleen `$pageview`, `$web_vitals`, `$rageclick` en de wholesaler/family/calc events van sempertexeurope.com). Geen rage clicks op SYBB pagina's in de afgelopen 8 dagen.

### Werkelijke SYBB funnel: event registratiepagina's op sempertexeurope.com

| Metric | Gisteren (1 sep) | 7d Gemiddelde (25 t/m 31 aug) | Trend |
|--------|------------------|-------------------------------|-------|
| Bezoekers | 10 | 5,6 | ↑ |
| Sessies | 12 | 6,0 | ↑ |
| Pageviews | 14 | 15,9 (9,9 zonder de uitschieter van 31 aug) | → / ↑ |
| Rage clicks | 0 | 0 | → |

Verdeling gisteren per pagina:

| Registratiepagina | Bezoekers | Land | Herkomst |
|-------------------|-----------|------|----------|
| /fr/.../professionnel-7/register | 2 | FR | site navigatie |
| /event/.../professional-7/register | 4 | BE, NL | site navigatie |
| /event/.../professional-9/register | 2 | BE | site navigatie |
| /event/.../professional-47/register | 1 | NL | site navigatie |
| /en_GB/.../professional-9/register | 1 | US | site navigatie |
| /en_GB/.../professional-english-2/register | 1 | SG | direct |

Editie 7 trekt de meeste interesse (6 van de 10 bezoekers), gevolgd door editie 9. Verkeer is verdeeld over desktop en mobiel, alles uit organische site navigatie of direct. Geen enkele bezoeker had UTM parameters, dus geen ads, geen e-mail tagging.

Over de hele week (25 aug t/m 1 sep): 49 unieke bezoekers op registratiepagina's, waarvan 2 via chatgpt.com (utm_source) en 1 via mail.telenet.be. De piek van 58 pageviews op 31 augustus is vertekend: 42 daarvan kwamen van 1 Belgische bezoeker die in 19 minuten 8 verschillende registratiepagina's doorklikte, waarschijnlijk intern of iemand die edities vergeleek.

## 4. Funnel Drop-off
Landing page: niet van toepassing, geen verkeer.

Event funnel sempertexeurope.com:
Registratiepagina view (10 bezoekers, 100%) → registratie voltooid (onbekend, geen event)

**Grootste lek:** onmeetbaar. Tussen de registratiepagina en de bevestiging staat geen enkel meetpunt in PostHog. De enige harde conversie in het project is `/shop/confirmation` en dat is de webshop, niet de workshop.

## 5. Rode Vlaggen 🚩
Geen performance-anomalieën in de ads (er draait niets voor SYBB). Wel drie structurele signalen:

1. **Rapport meet de verkeerde pagina.** De skill kijkt naar startyourballoonbusiness.com (0 bezoekers), terwijl de registratiepagina's op sempertexeurope.com wel dagelijks bezoekers krijgen. Dit is nu voor de derde opeenvolgende rapportage het geval.
2. **Nul conversiemeting op de werkelijke funnel.** 49 bezoekers per week bekijken een registratiepagina en niemand weet hoeveel er inschrijven.
3. **Geen scroll- of CTA-events.** Bij een herstart van de ads is er geen enkel on-page engagement signaal beschikbaar.

## 6. Top 3 Acties voor Vandaag

1. **Voeg een registratie-voltooid event toe aan de event funnel.**
   Wat: een PostHog custom event (bijvoorbeeld `sybb_registration_submit`) op de bevestigingsstap van de Wix event registratie, met editie en taal als properties.
   Waarom: gisteren 10 bezoekers op registratiepagina's, 49 in een week, en nul zicht op inschrijvingen. Dit is het enige ontbrekende meetpunt om conversie te kunnen rapporteren.
   Hoe: Wix event registratie thank-you stap of form submit hook, volgens `tracking-standards`.
   Verwachte impact: het rapport kan vanaf dan conversie per editie en per taal tonen.
   Escalatie: Oranje (Wix aanpassing nodig).

2. **Herdefinieer de daily-sybb-report skill op de event registratiepagina's.**
   Wat: pas `skills/daily-sybb-report/SKILL.md` aan zodat sectie 3 en 4 standaard de paden `/event/start-your-balloon-business-*/register` (alle talen) meten, en de oude landing page alleen nog als bijlage.
   Waarom: het rapport meet nu een dode pagina en de bruikbare data zit in een voetnoot.
   Hoe: skill-bestand aanpassen, kan direct.
   Escalatie: Geel (Robin goedkeuring op de nieuwe meetdefinitie).

3. **Beslis over de SYBB campagne herstart en de bestemming.**
   Wat: bepaal of `2026: SYBB` weer live gaat, en zo ja, naar welke registratiepagina (editie 7 heeft nu de meeste organische interesse).
   Waarom: campagne staat 4,5 maand op PAUSED terwijl de organische vraag naar registratiepagina's aantrekt (10 bezoekers gisteren vs 5,6 gemiddeld).
   Hoe: strategiebeslissing Robin, daarna Meta Ads Manager. Pas na actie 1, anders draait de campagne opnieuw blind.
   Escalatie: Rood (strategie).

---
*Databronnen: Meta Ads via Pipeboard MCP (directe JSON-RPC, account act_567892422940728) en PostHog MCP project "STX EU" (eu.posthog.com, project 149694, tijdzone UTC). Geen Google bronnen gebruikt. Gegenereerd op 2 september 2026.*
