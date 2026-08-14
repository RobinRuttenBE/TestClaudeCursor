# Auto-Optimize Rapport, 14 augustus 2026

**Status: niet uitgevoerd. Pipeboard is niet geautoriseerd, zevende dag op rij.**

Stap 1 tot en met 6 van `/ads-auto-optimize` konden niet draaien. Zonder `get_campaigns`, `get_adsets`, `get_ads` en `get_insights` is er geen spend, geen impressions, geen `actions.link_click`, dus geen Link CTR en geen CPC (link). De kill-regels draaien uitsluitend op die link-metrics, dus er is niets om tegen af te wegen.

Autoriseren gaat via je claude.ai connector instellingen, of `/mcp` in een interactieve sessie. Deze sessie is niet interactief, dus ik kan de OAuth-flow niet voor je starten.

Google MCPs en de Tracker Google Sheet zijn overgeslagen zoals gevraagd. Alleen Meta Ads MCP en PostHog MCP zijn aangeroepen.

---

## ⚡ Automatische acties uitgevoerd

**Geen. Nul ads gepauzeerd, nul ads aangeraakt.**

Dit is uitdrukkelijk geen "alles presteert boven de drempelwaarden". Het is "er is geen data en er draait niets". Zie hieronder.

| Ad | Reden | Was | Nu | Performance |
|----|-------|-----|-----|-------------|
| n.v.t. | Geen Meta-data beschikbaar | n.v.t. | n.v.t. | n.v.t. |

---

## 🔎 Wat ik wel kon controleren (PostHog, laatste 3 dagen)

Ik heb de 3-daagse window die de kill-regels zouden gebruiken zelf tegen PostHog gelegd, om vast te stellen of er überhaupt betaald verkeer bestaat.

**Kanaalverdeling, 1.167 bezoekers over 3 dagen:**

| Kanaal | Bezoekers | Aandeel | Pageviews | Bounce rate |
|--------|-----------|---------|-----------|-------------|
| Direct | 646 | 55,4% | 7.623 | 33,8% |
| Referral | 259 | 22,2% | 3.712 | 34,2% |
| Organic Search | 210 | 18,0% | 3.505 | 3,2% |
| AI | 32 | 2,7% | 79 | 18,8% |
| Organic Social | 13 | 1,1% | 48 | 15,4% |
| Email | 7 | 0,6% | 20 | 28,6% |

**Paid Social: afwezig. Paid Search: afwezig. Paid Unknown: afwezig.**

Er is geen enkele rij met een betaald kanaal. In de volledige UTM-uitsplitsing over dezelfde 3 dagen komt `utm_source=meta` niet voor, en `utm_campaign=sybb` evenmin. De enige getagde bron is `mailjet / email / workshop_tobi_promo_202608` met 1 bezoeker, plus Klaviyo met 2.

De acht bezoekers via `facebook.com`, `www.facebook.com` en `instagram.com` zijn ongetagd organisch verkeer, geen advertentieklikken.

**Conclusie: ook mét werkende Pipeboard-toegang zou dit rapport vandaag over nul actieve ads gaan.** Het autorisatieprobleem verbergt op dit moment geen draaiende campagne die geld verbrandt. Dat is het goede nieuws.

---

## ⚠️ Waarschuwingen

| Signaal | Waarde | Actie aanbevolen |
|---------|--------|-----------------|
| Creative fatigue | Niet meetbaar | Vereist Pipeboard |
| Dure reach (CPM) | Niet meetbaar | Vereist Pipeboard |
| Dalende Link CTR | Niet meetbaar | Vereist Pipeboard |
| **Self-referral vervuiling** | **250 bezoekers, 21,5% van al het verkeer** | **Fix vóór budget aan gaat** |

`www.sempertexeurope.com` staat nog steeds als verwijzer naar je eigen site: 250 bezoekers en 3.482 pageviews in 3 dagen. Dat is de tweede grootste "bron" in je hele dataset. Odoo (3), `sempertexeurope.shipping-portal.com` (2), `pay.mollie.nl` (1) en `www.mollie.com` (1) doen hetzelfde op kleinere schaal.

Dit stond ook in het rapport van gisteren en van 13 augustus. Het is nog niet uitgevoerd. Zolang dit staat, wordt Direct kunstmatig opgeblazen naar 55,4% en verdwijnt een deel van je toekomstige Meta-verkeer daarin. Je rekent je eerste campagne dan af op een verzonnen cijfer.

---

## 📊 70-20-10 Classificatie

Niet mogelijk. Classificatie vereist Link CTR en CPC (link) per ad.

Los daarvan staat de kalibratie-TODO uit het command nog open: de 70-20-10 drempels zijn nog gekalibreerd op all-clicks, niet op link metrics. Zodra Pipeboard werkt en er weer ads draaien, moeten die drempels eerst herzien voordat er budget-shifts uit volgen.

---

## 💡 Voorstellen (wacht op goedkeuring)

Budget-, variatie- en audience-voorstellen kan ik niet onderbouwen zonder performance-data. Wat er wel ligt, is een pre-flight lijst. Deze vier punten hebben Pipeboard níét nodig en bepalen of je eerste campagne meetbaar is.

**1. Autoriseer Pipeboard**
Zonder dit blijft dit command zeven dagen op rij leeg draaien. Het is de enige blokkade voor het hele Meta-gedeelte.

**2. Sluit interne domeinen uit als verwijzer in PostHog**
Concreet: `sempertexeurope.com`, `mollie.com`, `pay.mollie.nl`, `rezolvbv-sh-sempertex.odoo.com`, `sempertexeurope.shipping-portal.com`.
Reden: 21,5% van je verkeer wordt nu als Referral geteld terwijl het je eigen checkout- en portalflow is.
Verwachte impact: Direct zakt naar een realistisch niveau, en betaald verkeer blijft straks herkenbaar in plaats van weg te lekken. Instelling van ongeveer vijf minuten.

**3. Zet conversie-events op de SYBB pagina vóór er budget in gaat**
Reden: zonder conversie-event kan geen enkele kill-regel of ROAS-oordeel iets zeggen over wat een klik waard is. Je optimaliseert dan op CTR alleen.

**4. Leg de UTM-conventie vast in de ad-templates voordat je live gaat**
Lowercase, `utm_source=meta`, `utm_medium=cpc`, `utm_campaign=sybb`, `utm_content=hXX_bX_ctaX`, `utm_term=batch_X`. Komma's in `utm_content` vervangen door underscores.
Reden: de vorige batch had hoofdletters en komma's, waardoor `utm_content` niet matchte tegen de tracker.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

Punt 2, 3 en 4 kan ik direct oppakken. Punt 1 moet je zelf doen in een interactieve sessie.
