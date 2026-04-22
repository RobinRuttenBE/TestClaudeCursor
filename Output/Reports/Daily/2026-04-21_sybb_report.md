# SYBB Daily Report, 2026-04-21

## 1. Samenvatting
Campagne "2026: SYBB" (id 120239435987290239) stond gisteren op PAUSED en draaide niet sinds 19 april, dus geen Meta Ads spend, impressions of clicks op 21 april. Ook PostHog registreerde 0 pageviews op www.startyourballoonbusiness.com op 21 april, wat bevestigt dat er zonder ads geen traffic naar de landing page komt (organisch kanaal levert nihil). De 7d baseline (14 tot 20 april) laat een structureel probleem zien: bounce rate 84,1 procent en CPC 0,62 euro, beide significant boven target.

## 2. Meta Ads Performance

| Metric | Gisteren (21-04) | 7d Periode (14-20 apr) | 7d Gemiddelde /dag | Status |
|--------|------------------|------------------------|---------------------|--------|
| Spend | €0,00 | €453,64 | €64,81 | PAUSED |
| Impressions | 0 | 32.870 | 4.696 | PAUSED |
| Clicks | 0 | 733 | 105 | PAUSED |
| CTR | n.v.t. | 2,23% | 2,23% | gezond |
| CPC | n.v.t. | €0,62 | €0,62 | boven target (<€0,50) |
| Frequency | n.v.t. | 2,06 | 2,06 | acceptabel |
| Reach | n.v.t. | 15.972 | 2.282 | PAUSED |
| Landing Page Views | 0 | 336 | 48 | PAUSED |
| Add to Cart | 0 | 20 | 2,9 | PAUSED |
| Initiate Checkout | 0 | 18 | 2,6 | PAUSED |
| Purchases | 0 | 4 | 0,6 | PAUSED |
| Purchase Value | €0,00 | €1.473,50 | €210,50 | PAUSED |
| Complete Registration | 0 | 4 | 0,6 | PAUSED |

**Status campagne:** PAUSED sinds laatste update 19 april 2026 (14:29 CET). Ad set en ad level insights leveren dus geen data voor 21 april. Er bestaat een duplicaat "2026: SYBB - Kopie" (id 120243293329420239) die ook op PAUSED staat.

### Ad Variant Performance (7d, 14-20 apr, geen data 21 apr)
UTM breakdown uit PostHog laat de traffic-spread zien voor de laatste periode dat de campagne draaide:

| Ad (utm_content) | Pageviews op LP | Sessions op LP |
|------------------|-----------------|----------------|
| h11_b3_cta5 | 449 | 369 |
| h13_b3_cta5 | 176 | 158 |
| h12_b3_cta5 | 106 | 82 |
| h14_b3_cta5 | 1 | 1 |

**Beste variant (7d):** h11_b3_cta5 domineert het verkeer (56% share, 0,82 pv/session ratio).
**Verdacht:** h14_b3_cta5 heeft maar 1 pageview in de hele periode, wat suggereert dat deze variant bijna geen delivery krijgt of pas recent is gelanceerd.

## 3. Landing Page Health

| Metric | Gisteren (21-04) | 7d Gemiddelde | Target | Status |
|--------|------------------|---------------|--------|--------|
| Pageviews | 0 | 113,7 /dag | n.v.t. | 🔴 geen traffic |
| Sessions | 0 | 91,4 /dag | n.v.t. | 🔴 |
| Unique Visitors | 0 | 88,3 /dag | n.v.t. | 🔴 |
| Bounce Rate | n.v.t. | 84,1% | <55% | 🔴 ver boven target |
| Avg Session Duration | n.v.t. | niet tracked | >90s | 🔴 blind spot |
| Scroll 25% | n.v.t. | niet tracked | >80% | 🔴 blind spot |
| Scroll 50% | n.v.t. | niet tracked | >60% | 🔴 blind spot |
| Scroll 75% | n.v.t. | niet tracked | >40% | 🔴 blind spot |
| Scroll 100% | n.v.t. | niet tracked | >20% | 🔴 blind spot |
| CTA Click Rate | n.v.t. | ~5,6% (36 "Go to workshop" / 640 sessies) | >4% | 🟡 schatting |

### 7d Trafficverloop
| Datum | Pageviews | Sessions | Unique |
|-------|-----------|----------|--------|
| 2026-04-14 | 134 | 104 | 100 |
| 2026-04-15 | 97 | 73 | 70 |
| 2026-04-16 | 96 | 76 | 72 |
| 2026-04-17 | 106 | 91 | 89 |
| 2026-04-18 | 135 | 102 | 100 |
| 2026-04-19 | 140 | 119 | 115 |
| 2026-04-20 | 88 | 75 | 72 |
| 2026-04-21 | 0 | 0 | 0 |

Traffic zakte op 20 april (dag na campagnepauze) en is daarna naar nul gegaan. Dit bevestigt dat er praktisch geen organische bron is voor deze landing page.

### 7d Path-distributie
| Path | Pageviews | Sessions |
|------|-----------|----------|
| / | 693 | 627 |
| /product-page/start-your-balloon-business-professional | 48 | 41 |
| /checkout | 30 | 26 |
| /booking | 21 | 18 |
| /thank-you-page (incl. uuid) | 2 | 2 |

### 7d CTA Click Signalen (autocapture, top 10)
| Element tekst | Clicks |
|---------------|--------|
| Go to workshop | 36 |
| Where does the workshop take place? | 14 |
| Book Your Spot | 12 |
| What does my ticket include? | 12 |
| /booking link | 12 |
| Add to Cart | 9 |
| Continue | 7 |
| From what time does it start? | 7 |
| What dates can I book? | 6 |
| Explore Options / Buy Now | 5 elk |

## 4. Funnel Drop-off (7d, geen data 21 apr)

```
Home / (627 sessies, 100%)
  → Productpagina (41 sessies, 6,5%)
     → /checkout (26 sessies, 4,1% vanaf home)
        → /booking (18 sessies, 2,9% vanaf home)
           → /thank-you-page (2 sessies, 0,3% vanaf home)
```

**Alternatieve route (direct naar /booking):** 21 sessies landen op /booking (3,3% van home sessies). CTA "Book Your Spot" (12) + "Go to workshop" (36) bieden beide paden richting de booking flow.

**Grootste lek:** Home → Productpagina. 94% van de bezoekers verlaat zonder ooit door te klikken. Bounce rate 84% bevestigt dit: meer dan 4 op de 5 sessies zijn single-page.

**Purchase ratio cross-check:** PostHog telt 2 thank-you bezoeken in 7d, Meta telt 4 purchases. De mismatch komt waarschijnlijk door Wix-routing naar een externe bevestigingspagina of door ads-attributie buiten on-site tracking.

## 5. Rode Vlaggen 🚩

1. **Campagne PAUSED sinds 19 april** — nu 3 dagen zonder delivery richting workshop. Geen zichtbare reden in data (CTR 2,23% is gezond, frequency 2,06 is niet verzadigd). Risico: leadgeneratie voor workshop stopt volledig terwijl sign-ups per dag gemiddeld <1 waren.
2. **Bounce rate 84,1% over 7d** — ver boven de 55% target en boven de 70% red-flag drempel. Indicatief voor hero/eerste sectie die niet matcht met de advertentiebelofte.
3. **CPC €0,62 (+24% boven target van €0,50)** — ondanks gezonde CTR. Wijst op dure doelgroep of lage relevance score per impressie.
4. **Scroll depth tracking ontbreekt volledig** — geen $scroll of $scroll_depth events in PostHog. Zonder deze data kunnen hero- en sectieprestaties niet worden gediagnosticeerd.
5. **h14_b3_cta5 krijgt bijna geen delivery** (1 pageview in 7d) — óf de variant staat aan maar wint geen auction, óf is pas zeer recent toegevoegd. Budget wordt niet efficiënt verdeeld.
6. **Lage conversion naar /booking** — 2,9% vanaf home (18 van 627 sessies). Kosten per booking: €453,64 / 18 = €25,20 per /booking visit, exclusief booking-to-purchase drop-off.

## 6. Top 3 Acties voor Vandaag

### 1. Beslis bewust over status van campagne "2026: SYBB" (🔴 hoogste prioriteit)
- **Wat:** Heropen de campagne of documenteer waarom deze paused blijft. Check ook "2026: SYBB - Kopie" (duplicaat, ook paused).
- **Waarom:** 3 dagen volledige stilstand, geen leadgeneratie voor workshop, geen data om op te optimaliseren. 7d baseline laat zien dat campagne nog 4 purchases (€1.473,50) genereerde, dus er is bewezen conversie-waarde.
- **Hoe:** Meta Ads Manager → campagne 120239435987290239 → status ACTIVE. Of documenteer in ads-auto-optimize log waarom pauze bewust is (budget-stop, creative refresh, workshop datum-block).
- **Verwachte impact:** Herstel van ~48 LP views en 0,6 purchases per dag. Herstart van dataflow voor rapport.
- **Escalatie:** Geel, Robin-goedkeuring.

### 2. Diagnose bounce rate 84% op www.startyourballoonbusiness.com (🔴 kritiek)
- **Wat:** Review hero sectie en eerste 2 secties. Vergelijk ad-copy (h11/h12/h13 varianten) met de headline op de pagina. Zoek ad-pagina mismatch.
- **Waarom:** 4 op 5 bezoekers vertrekt zonder tweede pageview. Bounce rate is +53% boven target.
- **Hoe:** Open Wix editor, vergelijk H1 met ad-headlines uit de h11_b3_cta5 en h13_b3_cta5 creatives. Controleer load-snelheid en CTA zichtbaarheid boven de fold.
- **Verwachte impact:** Bounce rate daling van 84% → 65% zou +30% LP engagement opleveren bij gelijke traffic.
- **Escalatie:** Oranje, Wix Editor.

### 3. Installeer scroll depth tracking in PostHog (🟡 blind spot fixen)
- **Wat:** Zet scroll depth events aan (25%, 50%, 75%, 100%) voor www.startyourballoonbusiness.com.
- **Waarom:** Zonder scroll data is de helft van de KPI-targets uit SKILL.md niet meetbaar. Rapport kan niet echt diagnosticeren waar secties falen.
- **Hoe:** PostHog Toolbar of Wix custom code toevoegen aan de SYBB site met scroll event tracking via posthog.capture("$scroll_depth_25"), etc.
- **Verwachte impact:** Volledige funnel visibility, mogelijkheid om sectie-skip rate te meten en te optimaliseren.
- **Escalatie:** Groen, technisch uitvoerbaar zonder strategie-beslissing.

---

**Data bronnen:**
- Meta Ads: Pipeboard MCP, account act_567892422940728 "Sempertex Ad Account", campaign 120239435987290239
- PostHog: Default project 149694, host www.startyourballoonbusiness.com

**Gegenereerd:** 2026-04-22 voor rapportagedatum 2026-04-21
