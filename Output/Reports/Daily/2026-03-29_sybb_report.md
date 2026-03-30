# SYBB Daily Report -- 29 maart 2026

## 1. Samenvatting

De SYBB campagne staat **PAUSED sinds 8 maart**. Er is geen actieve ad spend geweest de afgelopen 21 dagen. Toch kwamen er gisteren 4 unieke bezoekers (7 pageviews) op de landing page, voornamelijk via oude UTM-links (H11, H12, H13). Dit is organisch/resterend verkeer. De campagne moet worden heractief als de SYBB funnel weer prioriteit krijgt.

## 2. Meta Ads Performance

### Campagne Status: PAUSED (sinds 8 maart 2026)

**Geen actieve spend op 29 maart.** Onderstaande data toont de laatste actieve periode (maart 1-8) ter referentie.

| Metric | Laatste actieve dag (8 mrt) | Actieve periode gem. (5 dagen) | Totaal maart |
|--------|---------------------------|-------------------------------|-------------|
| Spend | EUR 307.39 | EUR 264.77/dag | EUR 1,323.83 |
| Impressions | 43,463 | 37,813/dag | 189,067 |
| Clicks | 856 | 1,993/dag | 9,965 |
| CTR | 1.97% | 5.27% | 5.27% |
| CPC | EUR 0.36 | EUR 0.13 | EUR 0.13 |
| Frequency | 1.96 | 1.70 | 1.70 |
| Link Clicks | 600 | 1,941/dag | 9,703 |
| Landing Page Views | 399 | 1,235/dag | 6,174 |
| Leads | 0 | 3/dag | 15 |

### Ad Variant Performance (hele maart, voor paused)

| Ad (utm_content) | Impressions | Link Clicks | CTR | CPC (link click) | LP Views | Spend | Leads |
|-------------------|-------------|-------------|-----|-------------------|----------|-------|-------|
| H13,B3,CTA5 | 60,073 | 6,342 | 9.82% | EUR 0.07 | 4,063 | EUR 421.28 | 3 |
| H15,B3,CTA5 | 34,142 | 1,399 | 4.26% | EUR 0.15 | 842 | EUR 216.64 | 0 |
| H14,B3,CTA5 | 16,684 | 602 | 3.68% | EUR 0.18 | 357 | EUR 109.40 | 1 |
| H11,B3,CTA5 | 31,060 | 684 | 2.56% | EUR 0.30 | 445 | EUR 202.48 | 6 |
| H12,B3,CTA5 | 47,108 | 676 | 2.54% | EUR 0.55 | 467 | EUR 374.03 | 5 |

**Beste variant:** H13 (Hook 13). Verreweg de hoogste CTR (9.82%) en laagste CPC (EUR 0.07). Domineert qua volume met 4,063 landing page views. Meta's algoritme gaf deze ad het meeste bereik.

**Slechtste variant:** H12 (Hook 12). Hoogste CPC (EUR 0.55), laagste CTR (2.54%), en meeste spend (EUR 374.03) voor slechts 467 LP views. Zeer inefficient.

**Opvallend:** H11 heeft de meeste leads (6) ondanks lagere CTR. H13 heeft de meeste LP views maar slechts 3 leads, wat wijst op een mismatch tussen ad-belofte en landing page voor dit publiek.

## 3. Landing Page Health (29 maart)

| Metric | Gisteren | Target | Status |
|--------|----------|--------|--------|
| Pageviews | 7 | n.v.t. | -- |
| Unique Visitors | 4 | n.v.t. | -- |
| Sessions | 5 | n.v.t. | -- |
| Bounce Rate | n.v.t. (te weinig data) | <55% | -- |
| Avg Session Duration | n.v.t. (te weinig data) | >90s | -- |
| CTA Click Rate | n.v.t. (te weinig data) | >4% | -- |

**Opmerking:** Met slechts 4 unieke bezoekers is er onvoldoende data voor betrouwbare bounce rate, scroll depth en session duration analyses. Alle LP metrics zijn niet-significant op dit volume.

### UTM Breakdown (29 maart)

| UTM Content | Pageviews | Unique Visitors |
|-------------|-----------|-----------------|
| H11,B3,CTA5 / h11_b3_cta5 | 4 | 3 |
| H12,B3,CTA5 | 1 | 1 |
| h13_b3_cta5 | 1 | 1 |
| (geen UTM) | 1 | 1 |

**Let op:** Er zijn twee UTM-varianten voor dezelfde ad: `H11,B3,CTA5` (uppercase, komma's) en `h11_b3_cta5` (lowercase, underscores). Dit wijst op inconsistente UTM-tagging. Moet worden gestandaardiseerd voor correcte tracking.

## 4. Funnel Drop-off

Geen actieve funnel analyse mogelijk. De campagne is gepauzeerd en het verkeer van gisteren (7 pageviews) is te laag voor significante funnel data.

**Referentie uit actieve periode (maart 1-8):**
```
Ad Impressions (189,067) --> Link Clicks (9,703, 5.1%) --> LP Views (6,174, 63.6% van clicks) --> Leads (15, 0.24% van LP views)
```

**Grootste lek:** LP View naar Lead conversie is slechts 0.24%. Slechts 15 leads uit 6,174 landing page views. Dit is het kritieke punt in de funnel.

## 5. Rode Vlaggen

- **CAMPAGNE PAUSED** -- Al 21 dagen geen actieve ads. Alle momentum en learnings van Meta's algoritme gaan verloren.
- **UTM inconsistentie** -- Verschillende formaten voor dezelfde ad (H11,B3,CTA5 vs h11_b3_cta5). Maakt data-analyse onbetrouwbaar.
- **H12 was extreem duur** -- EUR 0.55 CPC bij slechts 2.54% CTR. Bij herstart moet deze variant niet meer draaien.
- **LP-naar-Lead conversie is 0.24%** -- Ver onder het target van >5%. Landing page of offer moet worden verbeterd voor herstart.
- **H13 paradox** -- Beste CTR en volume, maar slechts 3 leads. Hoge CTR met lage conversie = ad-pagina mismatch. De hook trekt verkeer aan dat niet converteert.

## 6. Top 3 Acties voor Vandaag

1. **Besluit nemen over herstart SYBB campagne**
   - **Waarom:** 21 dagen paused. Algoritmische learnings vervagen na 7 dagen inactiviteit.
   - **Hoe:** Robin moet beslissen: heractiveren met aangepaste ads of wachten op LP-optimalisatie.
   - **Verwachte impact:** Elke dag paused = verloren bereik en learnings.
   - **Escalatie:** Rood (strategie)

2. **Fix UTM-tagging voor alle ad varianten**
   - **Waarom:** PostHog toont mixed casing en delimiters (komma vs underscore). Dit maakt UTM-analyse onbetrouwbaar.
   - **Hoe:** Standaardiseer alle utm_content naar lowercase met underscores (h11_b3_cta5 formaat) conform CLAUDE.md tracking standards.
   - **Verwachte impact:** Correcte attributie en betrouwbare funnel data.
   - **Escalatie:** Groen (direct uitvoerbaar bij herstart)

3. **Analyseer LP conversie bottleneck voor herstart**
   - **Waarom:** 0.24% LP-naar-Lead conversie bij 6,174 views. Target is >5%. Dit is het #1 probleem.
   - **Hoe:** Review landing page copy, CTA-positie, en aanbod. Cross-refereer H11 (meeste leads ondanks lagere CTR) vs H13 (beste CTR, weinig leads) om te begrijpen welk type bezoeker converteert.
   - **Verwachte impact:** Verdubbeling van conversie rate = 30 leads i.p.v. 15 bij dezelfde spend.
   - **Escalatie:** Oranje (Wix Editor + strategie)

---

*Cross-referentie analyse:*
- **H13: Hoge CTR + Lage Conversie** = misleading hook of verkeerde doelgroep. De ad trekt kijkers maar geen kopers.
- **H11: Lagere CTR + Meeste Leads** = betere targeting ondanks minder volume. Overweeg H11-stijl hooks als basis voor nieuwe batch.
- **H12: Hoge spend + Lage alles** = direct uitschakelen bij herstart.

*Rapport gegenereerd: 30 maart 2026, 08:00*
*Data bronnen: Meta Ads (Pipeboard MCP) + PostHog (EU instance, project 149694)*
