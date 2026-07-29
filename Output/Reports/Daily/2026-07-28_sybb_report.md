# SYBB Daily Report: 28 juli 2026

## 1. Samenvatting
De SYBB funnel stond op 28 juli volledig stil, net als de dagen daarvoor. De Meta campagne `2026: SYBB` staat op PAUSED sinds 19 april 2026 en heeft sindsdien nul spend, nul impressies en nul clicks geleverd. De landing page `www.startyourballoonbusiness.com` kreeg 0 pageviews. Dit is geen performance-probleem maar een aan/uit-probleem: er is niets om te optimaliseren zolang de campagne uit staat.

Belangrijkste nieuwe observatie deze week: het weinige organische verkeer dat er nog was, droogt ook op. In het venster 22 t/m 28 juli kreeg de landing page in totaal 2 pageviews over 7 dagen, tegen 18 pageviews in het venster daarvoor (15 t/m 21 juli).

> Databronnen: Meta Ads (Pipeboard MCP, account `act_567892422940728`, Sempertex Ad Account) en PostHog (project "Default project", EU, host gefilterd op `www.startyourballoonbusiness.com`). Beide bronnen bevestigen onafhankelijk dat de funnel inactief was.

## 2. Meta Ads Performance
Campagne `2026: SYBB` (ID `120239435987290239`), status **PAUSED**, dagbudget €100,00 (niet actief). Laatste wijziging 19 april 2026.

| Metric | Gisteren (28 jul) | 7d Gemiddelde | Trend |
|--------|-------------------|---------------|-------|
| Spend | €0,00 | €0,00 | → |
| Impressions | 0 | 0 | → |
| Clicks | 0 | 0 | → |
| CTR | n.v.t. | n.v.t. | → |
| CPC | n.v.t. | n.v.t. | → |
| Frequency | n.v.t. | n.v.t. | → |

De Meta Insights API gaf een lege dataset terug voor zowel 28 juli als het dagvenster 22 t/m 28 juli. Ook op accountniveau is er in het venster 1 april t/m 28 juli alleen delivery in april 2026. Mei, juni en juli hebben nul spend over het hele account, dus er draait op dit moment geen enkele campagne.

**Laatste bekende SYBB delivery (april 2026), als referentiepunt bij heractivatie:**

| Metric | April 2026 |
|--------|-----------|
| Spend | €1.059,47 |
| Impressions | 91.839 |
| Clicks | 1.935 |
| CTR | 2,11% |
| CPC | €0,55 |
| Frequency | 2,19 |
| Landing page views | 818 |
| Purchases | 6 |

Ter vergelijking presteerde maart 2026 fors beter: CTR 5,27% en CPC €0,13 bij 189.067 impressies. April liet dus een duidelijke verslechtering zien (CPC ruim 4x hoger, CTR gehalveerd, frequency opgelopen naar 2,19) vlak voordat de campagne werd gepauzeerd. Dat patroon wijst op creative fatigue en is relevant voor de herstart: dezelfde creatives opnieuw aanzetten betekent waarschijnlijk starten op april-niveau, niet op maart-niveau.

### Ad Variant Performance
| Ad (utm_content) | Clicks | CTR | CPC | LP Bounce | LP Scroll 50%+ |
|-------------------|--------|-----|-----|-----------|----------------|
| (geen actieve ads) | 0 | n.v.t. | n.v.t. | n.v.t. | n.v.t. |

**Beste variant:** n.v.t., geen delivery.
**Slechtste variant:** n.v.t., geen delivery.

Er is ook een tweede campagne `2026: SYBB - Kopie` (ID `120243293329420239`), aangemaakt op 19 april 2026, eveneens PAUSED en zonder enige delivery.

## 3. Landing Page Health
Host `www.startyourballoonbusiness.com`. Gisteren 0 pageviews, dus geen sessie-metrics te berekenen.

**Dagpatroon laatste 14 dagen:**

| Dag | Pageviews | Unieke bezoekers |
|-----|-----------|------------------|
| 15 jul | 1 | 1 |
| 16 jul | 2 | 2 |
| 17 jul | 1 | 1 |
| 18 jul | 3 | 3 |
| 19 jul | 2 | 2 |
| 20 jul | 6 | 6 |
| 21 jul | 1 | 1 |
| 22 jul | 0 | 0 |
| 23 jul | 1 | 1 |
| 24 jul | 0 | 0 |
| 25 jul | 0 | 0 |
| 26 jul | 0 | 0 |
| 27 jul | 1 | 1 |
| **28 jul** | **0** | **0** |

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 0 | 0,3 per dag | meten | 🔴 |
| Bounce Rate | n.v.t. | n.v.t. | <55% | ⚪ geen data |
| Avg Session Duration | n.v.t. | n.v.t. | >90s | ⚪ geen data |
| Scroll 25% | n.v.t. | n.v.t. | >80% | ⚪ geen data |
| Scroll 50% | n.v.t. | n.v.t. | >60% | ⚪ geen data |
| Scroll 75% | n.v.t. | n.v.t. | >40% | ⚪ geen data |
| Scroll 100% | n.v.t. | n.v.t. | >20% | ⚪ geen data |
| CTA Click Rate | n.v.t. | n.v.t. | >4% | ⚪ geen data |

**Scroll depth baseline (90 dagen, homepage, n=30 sessies):**

Er is te weinig recent volume voor een dagcijfer, maar over 90 dagen zijn er 30 gemeten homepage-sessies met scrolldata. Behandel dit als indicatie, niet als betrouwbaar cijfer, de steekproef is te klein.

| Bucket | Gemeten (90d) | Target | Status |
|--------|---------------|--------|--------|
| Scroll 25%+ | 70% | >80% | 🟡 |
| Scroll 50%+ | 53% | >60% | 🟡 |
| Scroll 75%+ | 40% | >40% | 🟢 |
| Scroll 100% | 17% | >20% | 🟡 |

De vorm van deze verdeling is opvallend gezond: wie voorbij 50% komt, leest meestal helemaal uit (40% haalt 75%, 17% haalt het einde). De uitval zit vooral bovenaan, ongeveer 30% van de bezoekers scrollt niet eens tot 25%. Dat wijst op een hero-sectie die niet direct overtuigt, niet op een te lange pagina.

**Tracking-instrumentatie:** op deze host vuren alleen `$pageview`, `$autocapture`, `$pageleave` en `$web_vitals`. Er is geen custom CTA-click event en geen conversie-event geconfigureerd. Scroll depth is alleen af te leiden uit `$pageleave`, en dat event is voor het laatst gezien op 10 juli. `$autocapture` stopte eveneens op 10 juli, terwijl `$pageview` nog wel doorloopt tot 27 juli. Dat verschil is een signaal dat er iets mis is met de tracking-configuratie, niet alleen met het verkeersvolume.

## 4. Funnel Drop-off
Pageview (0) → Scroll 50% (0) → CTA Click (0) → /booking (0)

**Grootste lek:** de funnel begint niet. Er is geen instroom bovenaan omdat de betaalde campagne uit staat. Zonder verkeer valt er geen drop-off te analyseren.

**UTM-instroom laatste 90 dagen:**

| utm_source | utm_campaign | utm_content | Pageviews | Laatst gezien |
|------------|--------------|-------------|-----------|---------------|
| (geen UTM) | (geen) | (geen) | 112 | 27 jul |
| instagram | sybb | bio_link | 51 | 14 jul |
| facebook | sybb | bio_link | 19 | 10 jul |
| meta | sybb | h11_b3_cta5 | 4 | 3 jun |
| META | SYBB | H14,B3,CTA5 | 2 | 1 jul |
| meta | sybb | h13_b3_cta5 | 2 | 5 mei |
| youtube | sybb | bio_link | 2 | 28 mei |

Het restant aan SYBB-verkeer komt uit organische bio-links (Instagram, Facebook, YouTube), niet uit ads. De laatste echte ad-klik met `utm_source=meta` dateert van 3 juni.

## 5. Rode Vlaggen 🚩
- 🚩 **Campagne staat op PAUSE, inmiddels 100 dagen.** `2026: SYBB` levert sinds 19 april 2026 niets uit. Elke dag zonder delivery is een dag zonder leads voor de workshop.
- 🚩 **Nul LP-verkeer, en de trend gaat verder omlaag.** 2 pageviews in de week 22 t/m 28 juli tegen 18 in de week ervoor, een daling van 89%. Ook de organische bio-link instroom is opgedroogd (laatste Instagram-hit 14 juli).
- 🚩 **Tracking is deels stukgelopen.** `$autocapture` en `$pageleave` zijn na 10 juli niet meer gezien terwijl `$pageview` doorloopt. Zonder die events zijn bounce rate, scroll depth en CTA clicks straks niet te meten, ook niet als de campagne weer aan gaat.
- 🚩 **Geen CTA-click event geïnstrumenteerd.** De KPI "CTA Click Rate >4%" uit de skill is op dit moment structureel niet meetbaar, want er bestaat geen event dat CTA-clicks registreert.
- 🚩 **UTM-conventie geschonden.** De hit `META / SYBB / H14,B3,CTA5` staat in hoofdletters met komma's, terwijl de standaard lowercase met underscores is (`meta`, `sybb`, `h14_b3_cta5`). PostHog behandelt dit als een aparte waarde, waardoor deze klikken bij rapportage buiten de `meta`-groep vallen.
- ℹ️ Ter info: het PostHog-project meet vooral `www.sempertexeurope.com` (51.218 pageviews over 30 dagen). Dat is de corporate B2B-site, niet de SYBB-funnel. De SYBB landing page haalde in dezelfde 30 dagen 49 pageviews.

## 6. Top 3 Acties voor Vandaag

**1. Beslis of SYBB weer aan moet, en met welke creatives.**
- **Wat:** neem een expliciete go/no-go op `2026: SYBB`. Bij go: activeer niet blind de bestaande ads, maar vervang eerst de creatives.
- **Waarom:** april 2026 liet CPC €0,55 zien tegen €0,13 in maart, CTR gehalveerd naar 2,11% en frequency opgelopen naar 2,19. Dat is het klassieke fatigue-patroon. De campagne is precies op dat punt gepauzeerd.
- **Hoe:** Meta Ads Manager, campagne `120239435987290239`. Volg de 70-20-10 regel: 70% van het budget op de bewezen maart-hooks, 20% variaties daarop, 10% nieuwe experimenten.
- **Verwachte impact:** herstart richting maart-niveau (CPC onder de target van €0,50) in plaats van april-niveau.
- **Escalatie:** 🔴 Rood, strategiebeslissing, vereist jouw goedkeuring.

**2. Repareer de landing page tracking voordat de campagne aan gaat.**
- **Wat:** onderzoek waarom `$autocapture` en `$pageleave` na 10 juli zijn gestopt terwijl `$pageview` doorloopt, en voeg een expliciet CTA-click event toe.
- **Waarom:** zonder deze events zijn 5 van de 7 KPI's uit de skill (bounce rate, scroll 25/50/75/100%, CTA click rate) niet te berekenen. Dan betaal je straks voor verkeer dat je niet kunt analyseren.
- **Hoe:** controleer de PostHog snippet-configuratie op de Wix-site (autocapture en pageleave capture aan), en definieer een custom event op de "Book Now" knop.
- **Verwachte impact:** volledige funnel-meting vanaf dag 1 van de heractivatie in plaats van pas weken later.
- **Escalatie:** 🟠 Oranje, vereist Wix Editor toegang.

**3. Corrigeer de UTM-conventie en documenteer die.**
- **Wat:** zet alle SYBB ad-URL's om naar lowercase met underscores (`utm_source=meta`, `utm_campaign=sybb`, `utm_content=h14_b3_cta5`) en verwijder de hoofdletter/komma-variant.
- **Waarom:** de hit `META / SYBB / H14,B3,CTA5` splitst zich af als aparte waarde in PostHog, wat de per-variant rapportage vervuilt zodra er weer volume is.
- **Hoe:** Meta Ads Manager, URL-parameters per ad, of via `update_ad_url_tags`. Leg de conventie vast in `.claude/skills/tracking-standards`.
- **Verwachte impact:** schone per-variant vergelijking (welke hook drijft de diepste engagement) zodra de campagne draait.
- **Escalatie:** 🟢 Groen, administratief, kan direct.

---
*Rapport gegenereerd op 29 juli 2026 voor rapportagedatum 28 juli 2026. Databronnen: Meta Ads MCP (Pipeboard) en PostHog MCP. Geen Google-diensten geraadpleegd, geen schrijfacties naar de Meta Ads Tracker Google Sheet.*
