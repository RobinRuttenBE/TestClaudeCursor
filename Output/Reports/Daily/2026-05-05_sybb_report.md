# SYBB Daily Report, 2026-05-05

## 1. Samenvatting

Campagne "2026: SYBB" stond gisteren PAUSED, dus geen Meta Ads spend, impressies of klikken. De landing page zag toch 8 pageviews uit 6 sessies via Instagram bio link en achtergebleven UTM verkeer (h13_b3_cta5), met 1 zichtbare conversiepad: Book Your Spot klik op de homepage gevolgd door een /checkout bezoek met "Continue" klik. Bounce rate (66,7%) en CTA klik rate (16,7%) zijn beter dan het 7-daags gemiddelde, maar het volume is te klein om iets te concluderen, dus de hoofdactie is: campagne herstarten of strategisch besluiten nemen.

## 2. Meta Ads Performance

Campagne ID: 120239435987290239 (status: PAUSED sinds laatste update 2026-04-19).

| Metric | Gisteren | 7d Gemiddelde | Trend |
|--------|----------|---------------|-------|
| Spend | €0,00 | €0,00 | , |
| Impressions | 0 | 0 | , |
| Clicks | 0 | 0 | , |
| CTR | n/a | n/a | , |
| CPC | n/a | n/a | , |
| Frequency | n/a | n/a | , |

**Status:** Campagne staat al minstens 7 dagen op pause. Geen ad-level data beschikbaar voor 2026-05-05.

### Ad Variant Performance

Geen Meta delivery, dus tabel niet van toepassing. Wel interessant: PostHog ziet nog 2 pageviews / 1 sessie binnenkomen via `utm_content=h13_b3_cta5`, `utm_source=meta`, `utm_campaign=sybb`. Dat duidt op een achtergebleven of gedeelde link die nog circuleert (cache, screenshot, gebookmarked, retargeting pixel firing op oude URL). Verifieer dat alle ads in Meta echt op PAUSED staan en niet via een buiten-platform retargeting actief blijven.

## 3. Landing Page Health

Site: startyourballoonbusiness.com.

| Metric | Gisteren | 7d Gemiddelde | Target | Status |
|--------|----------|---------------|--------|--------|
| Pageviews | 8 | 3,86 | n/a | , |
| Unieke bezoekers | 6 | n/a | n/a | , |
| Sessies | 6 | 3,0 | n/a | , |
| Bounce Rate | 66,7% | 85,7% | <55% | 🟡 |
| Avg Session Duration | 113,2s | 194,3s | >90s | 🟢 |
| Scroll 25% | 16,7% | 19,0% | >80% | 🔴 |
| Scroll 50% | 16,7% | 19,0% | >60% | 🔴 |
| Scroll 75% | 16,7% | 19,0% | >40% | 🔴 |
| Scroll 100% | 16,7% | 14,3% | >20% | 🔴 |
| CTA Click Rate (Book Your Spot) | 16,7% (1/6) | n/a | >4% | 🟢 |

**Caveat scroll depth:** slechts 1 `$pageleave` event geregistreerd op 6 sessies. De andere 5 sessies hebben geen scroll meting, waarschijnlijk omdat ze afhaakten voordat het pageleave event vuurde of omdat scroll tracking niet vuurt voor zeer korte sessies. Cijfer is dus niet betrouwbaar bij dit volume.

### UTM Segmentatie (gisteren)

| utm_source | utm_campaign | utm_content | Pageviews | Sessies |
|------------|--------------|-------------|-----------|---------|
| facebook | sybb | bio_link | 3 | 2 |
| meta | sybb | h13_b3_cta5 | 2 | 1 |
| (geen UTM, direct/referral) | , | , | 3 | 3 |

### Pad Analyse (gisteren)

| Pathname | Pageviews | Sessies |
|----------|-----------|---------|
| / | 6 | 5 |
| /review | 1 | 1 |
| /checkout | 1 | 1 |

### Klik Activiteit (autocapture)

| Pad | Element | Clicks |
|-----|---------|--------|
| / | (onbenoemde elementen) | 3 |
| / | "Book Your Spot" CTA | 1 |
| /checkout | "Continue" | 1 |
| /checkout | "Show items (1)" | 1 |

## 4. Funnel Drop-off

```
Pageview /                  6 sessies   100%
       ↓
"Book Your Spot" klik       1 sessie     16,7%   (drop-off 83,3%)
       ↓
Pageview /checkout          1 sessie    100% van CTA klikkers
       ↓
"Continue" klik /checkout   1 sessie    100% van /checkout
```

**Grootste lek:** stap 1 → stap 2, van homepage view naar CTA klik. 5 van de 6 sessies klikken niet door op Book Your Spot. Met dit volume is dat statistisch ruis, maar het patroon spoort wel met het 7-daags gemiddelde van slechts 19% scroll voorbij 25%, dus mensen scrollen niet ver genoeg om de CTA te overwegen.

## 5. Rode Vlaggen 🚩

1. **Campagne PAUSED, geen verse traffic:** SYBB campagne draait niet en heeft minstens 7 dagen niet gedraaid. Alle geobserveerde landing page activiteit komt uit organisch / bio link / legacy URLs. Funnel staat effectief stil.
2. **Pageviews via `utm_content=h13_b3_cta5` ondanks paused campagne:** 1 sessie kwam via een Meta UTM binnen op een dag dat geen ads draaiden. Mogelijke oorzaken: gedeelde link, oude bookmark, tracking pixel uit een retargeting flow buiten deze campagne. Verifieer in Ads Manager dat geen enkele adset / ad nog op ACTIVE staat.
3. **Scroll depth onder elk target:** 25/50/75/100% scroll lopen alle vier op 16,7% gisteren en ongeveer 19% over 7 dagen, ver onder de targets (80/60/40/20%). Hero sectie houdt de aandacht niet vast. Caveat: bij <10 sessies/dag niet betrouwbaar, maar het 7-daags patroon bevestigt het signaal.
4. **Bounce rate boven target (66,7% vs <55%):** beter dan 7d gemiddelde van 85,7%, maar nog steeds in de gele zone.

## 6. Top 3 Acties voor Vandaag

1. **Beslis: campagne herstarten of strategie heroverwegen.** SYBB ad campagne staat sinds minstens 7 dagen op pause. Zonder paid traffic kan dit rapport geen ad performance meten en blijft de landing page op organische ruis draaien. Concrete keuze: (a) campagne unpausen met huidige creatives en 24-48 uur observeren, (b) eerst nieuwe creatives klaarzetten op basis van de h11 t/m h15 batch leerpunten en daarna unpausen, of (c) campagne formeel beëindigen in dit rapport en een nieuwe campagne strategie definiëren. *Waarom:* zonder beslissing genereren de dagelijkse rapporten geen actionable signaal. *Verwachte impact:* hoog, want dit deblokkeert de hele meetketen.

2. **Audit waarom `h13_b3_cta5` UTM verkeer nog binnenkomt.** Open Meta Ads Manager, filter campagne "2026: SYBB" op alle adsets en ads, controleer dat statusniveau écht PAUSED is op campaign + adset + ad niveau. Check ook of er een retargeting campagne buiten "2026: SYBB" deze creative nog gebruikt. *Waarom:* attributie en data hygiëne. Als er stilletjes ergens nog spend zit, zien we dat niet in dit rapport. *Verwachte impact:* laag op opbrengst, hoog op vertrouwen in de cijfers.

3. **Onderzoek de /checkout sessie van gisteren via session recording.** Eén bezoeker doorliep gisteren / → Book Your Spot → /checkout → Continue → Show items. Dat is een complete CTA → checkout flow. Open de session recording in PostHog (sessie ID 019df75b-9edf-7cf1-8cdd-d14bd71a9839, de enige met max_scroll = 1.0) en verifieer of de booking is afgerond, op welk veld er werd afgehaakt, of waar fricion zat. *Waarom:* met zo weinig sessies is elk conversie-pad puur goud aan kwalitatieve data. *Verwachte impact:* één concrete UX inzicht geeft meer leverage dan 100 visits aan ruisige aggregaten.

---

**Data bronnen:** Meta Ads MCP (Pipeboard, account `act_567892422940728`, campaign ID `120239435987290239`), PostHog MCP (project ID 149694, host filter ILIKE startyourballoonbusiness). Periodes: gisteren = 2026-05-05 00:00 tot 2026-05-06 00:00 UTC. 7d baseline = 2026-04-28 tot 2026-05-04 inclusief.
