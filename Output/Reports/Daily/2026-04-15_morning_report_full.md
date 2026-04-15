# Morning Report — 2026-04-15

> 🚨 **PIXEL DATAFOUT — Meta Purchase Tracking**
> Waarde per purchase: **EUR 21386.75** bij 2 purchases (totaal EUR 42773.50).
> Dit past NIET bij de SYBB ticketprijs van EUR 350 ex BTW / EUR 423,50 incl BTW.
> Geldige ranges per purchase (15% marge): EUR 297-488 (1 ticket), EUR 595-977 (2 tickets), EUR 892-1465 (3 tickets), etc.
> ROAS is overschreven met `n.v.t. (pixel datafout)`. Purchase aantal in prose als `? purchases (verifieer Wix)`.
> **Verifieer het echte aantal purchases handmatig in Wix orders.**


Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

Rapport is klaar en gepusht. Hier de samenvatting:

## Meta Ads Rapport -- 15 april 2026

### Campagne: 2026: SYBB (laatste 30 dagen)

| Metric | Waarde |
|--------|--------|
| Spend | EUR 701,76 |
| Impressions | 66.261 |
| Reach | 34.460 |
| CTR | 2,0% |
| CPC | EUR 0,52 (net boven target) |
| Purchases | ? (verifieer Wix) |
|ROAS n.v.t. (pixel datafout) |

### Actieve ads (3 van 21)

| Ad | CPC | CTR | Purchases | Flag |
|----|-----|-----|-----------|------|
| **H12,B3,CTA5** (Kopie 2) | EUR 0,40 | 2,3% | 0 | Beste CPC bij volume |
| **H13,B3,CTA5** (Kopie 3) | EUR 0,61 | 1,9% | 2 (ROAS n.v.t. (pixel datafout)) | CPC boven drempel |
| **H11,B3,CTA5** (Kopie 1) | EUR 0,66 | 2,0% | 0 | CPC boven drempel, 38% van spend |

### PostHog cross-referentie

- **751 Meta-sessies** op de LP (88% van alle traffic)
- **UTM case bug gevonden:** 187 sessies met "META" i.p.v. "meta". Fix nodig.
- **LP bottleneck:** slechts 9% van bezoekers bekijkt een product (LP View -> View Content)

### Top 3 acties

1. **Verschuif budget** van H11 (EUR 0,66 CPC, ? purchases (verifieer Wix)) naar H12 (EUR 0,40 CPC) en H13 (conversies)
2. **Fix UTM casing** in actieve ad sets ("META" -> "meta")
3. **Optimaliseer LP above-the-fold** content: 91% drop-off voor View Content

Rapport opgeslagen in `Output/Reports/Daily/2026-04-15_ads_report.md`.

> **Wil je funnel data toevoegen?** Ik heb PostHog LP data al meegenomen. Voor een volledige `/funnel-diagnose` heb ik nog nodig: scroll depth, CTA click rate, en /booking visits.

---

SYBB rapport voor 14 april 2026 is opgeslagen en gepusht.

**Kernpunten:**
- **Bounce rate 82.7%** is het grootste probleem (target <55%). 4 op 5 bezoekers vertrekken direct.
- **CPC EUR 0.62** ligt boven target (EUR 0.50), gedreven door H11 die 66% van het budget pakt.
- **H12 is de winnaar:** laagste CPC (EUR 0.49), hoogste CTR (3.02%), meeste add-to-carts per euro.
- **Volume daalt:** impressions -23%, /booking bezoeken -38% vs 7d gemiddelde.
- **CTA click rate is positief:** 16.3% (ruim boven 4% target), maar de meeste bezoekers komen nooit tot het punt van een CTA.

**Top acties:** (1) LP hero sectie herzien, (2) budget verschuiven van H11 naar H12, (3) PostHog scroll tracking fixen voor betere diagnose.

---

Rapport opgeslagen, gecommit en gepusht.

## Samenvatting

**0 ads gepauzeerd** - alle 3 actieve ads presteren boven de kill-drempels (Link CTR >= 0,8%).

Belangrijkste bevindingen:

1. **Budget mismatch:** H11 krijgt 59% van het budget maar heeft ? purchases (verifieer Wix). H13 (de enige ad met purchases,ROAS n.v.t. (pixel datafout)) krijgt slechts 24%.

2. **H11 checkout blokkade:** 13 add-to-carts en 13 initiate checkouts maar ? purchases (verifieer Wix). Er zit een probleem in de checkout flow specifiek voor bezoekers via H11.

3. **H12 stijgt:** Beste Link CTR (1,19%, stijgend) en laagste lifetime CPC (link) (EUR 0,84), maar krijgt slechts 11% van het budget.

**5 voorstellen wachten op jouw goedkeuring:**
1. Pauzeer ad set Kopie 1 (H11) om budget naar H13 te sturen
2. Onderzoek checkout flow blokkade bij H11 via PostHog
3. Geef H12 meer ruimte (volgt automatisch als H11 pauzeert)
4. Maak hook variaties op H12 en H13
5. Audience monitoring (geen acute actie nodig)

Welke wil je uitvoeren?

---

Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
