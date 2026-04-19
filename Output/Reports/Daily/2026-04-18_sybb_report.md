# SYBB Daily Report, 18 april 2026

## 1. Samenvatting

Sterke CTR (2,36%) en gezonde Landing Page Views (78), maar **0 purchases** op €94,47 spend. 7 initiate checkouts leverden geen conversie op, wat wijst op een checkout of betalingsprobleem. H11 slokt 71% van het dagbudget op tegen een CPC van €0,73, ruim boven target. H12 is veruit de efficiëntste variant (CPC €0,38, CTR 4,21%) maar krijgt maar 13% van het budget.

## 2. Meta Ads Performance

| Metric | Gisteren (18/4) | 7d Gemiddelde (11-17/4) | Trend |
|--------|-----------------|-------------------------|-------|
| Spend | €94,47 | €104,83/d | → |
| Impressions | 6.435 | 8.408/d | ↓ |
| Clicks | 152 | 174/d | ↓ |
| Link Clicks | 90 | 93/d | → |
| CTR | 2,36% | 2,07% | ↑ |
| CPC | €0,62 | €0,60 | → |
| CPM | €14,68 | €12,47 | ↑ |
| Reach | 4.789 | 3.915/d | ↑ |
| Frequency (dagelijks) | 1,34 | — | — |
| Landing Page Views | 78 | 75/d | → |

### Ad Variant Performance (18/4)

| Ad (utm_content) | Spend | Link Clicks | CTR | CPC | LPV | ATC | IC | Purch. |
|------------------|-------|-------------|-----|-----|-----|-----|----|---------|
| H11,B3,CTA5 (Kopie 1) | €67,43 | 55 | 2,03% | €0,73 | 51 | 3 | 2 | 0 |
| H13,B3,CTA5 (Kopie 3) | €14,58 | 17 | 2,44% | €0,56 | 15 | 0 | 2 | 0 |
| H12,B3,CTA5 (Kopie 2) | €12,46 | 18 | 4,21% | €0,38 | 12 | 3 | 3 | 0 |

**Budgetverdeling:** H11 71% • H13 15% • H12 13%

**Beste variant:** H12,B3,CTA5. Hoogste CTR (4,21%), laagste CPC (€0,38), beste click-to-IC ratio (3/18 = 17%). Efficiëntste spend in de campagne.

**Slechtste variant:** H11,B3,CTA5. Hoogste CPC (€0,73, 46% boven target), krijgt 71% van het dagbudget maar heeft laagste CTR (2,03%) en de laagste check-out ratio per clicks.

### Pixel Conversies (18/4)

| Event | Aantal | Waarde |
|-------|--------|--------|
| View Content | 12 | €42,00 |
| Add to Cart | 6 | €21,00 |
| Initiate Checkout | 7 | €24,50 |
| Add Payment Info | 0 | — |
| Purchase | 0 | — |

### 7d Pixel Conversies (11-17/4, ter referentie)

| Event | 7d Totaal | Daggemiddelde |
|-------|-----------|---------------|
| View Content | 59 | 8,4 |
| Add to Cart | 32 | 4,6 |
| Initiate Checkout | 22 | 3,1 |
| Add Payment Info | 4 | 0,6 |
| Purchase | 6 | 0,86 |
| Complete Registration | 6 | 0,86 |

7d revenue: €442,47 (purchase) + €861,00 (complete registration value) op €733,82 spend.

## 3. Landing Page Health (PostHog)

**Status: GEEN DATA BESCHIKBAAR**

De PostHog MCP is geconfigureerd (`https://mcp.posthog.com/mcp`) maar levert in deze sessie geen tool schemas. Conform de strikte regel voor deze run zijn GA4 en Google MCPs niet geraadpleegd als alternatief.

Ontbrekende metrics:
- Bounce rate
- Avg session duration
- Scroll depth distributie (25/50/75/100%)
- CTA click rate
- Per-UTM segmentatie van on-page gedrag
- Funnel drop-off Pageview → Scroll 50% → CTA → /booking
- Session recording count

**Actie:** verifieer PostHog MCP authenticatie in de Claude Code settings voordat de volgende run draait. Tot die tijd is de cross-reference analyse tussen Meta CTR en on-page gedrag beperkt.

## 4. Funnel Drop-off (Meta-only, 18/4)

Zonder PostHog kunnen we alleen de Meta-attributed funnel reconstrueren:

```
Impressions       6.435 (100%)
    ↓ 97,6% drop-off
Clicks              152 (2,4%)
    ↓ 40,8% drop-off vs clicks
Landing Page View    78 (51,3% of clicks, 1,21% of impr.)
    ↓ 84,6% drop-off vs LPV
View Content         12 (15,4% of LPV)
    ↓ 50,0% drop-off
Add to Cart           6 (50% of VC)
    ↑ 16,7% uplift (tracking noise)
Initiate Checkout     7 (117% of ATC)
    ↓ 100% drop-off
Purchase              0
```

**Grootste lek: Initiate Checkout → Purchase (100% drop-off).** 7 mensen startten een checkout, niemand voltooide. Dit is het meest urgente probleem van de dag, sterker dan het Meta-niveau.

**Secundair lek: LPV → View Content (84,6%).** Van de 78 LP bezoekers bekeek maar 15,4% een product. Hier zou PostHog scroll-data en CTA click tracking kritiek zijn.

## 5. Rode Vlaggen

1. **0 Purchases op 7 Initiate Checkouts.** Kans op stuk checkout flow, payment provider issue, of verborgen kosten (shipping, BTW). Vergelijk: 7d had 22 IC → 6 Purchase (27% conversie). Vandaag 7 IC → 0 Purchase. Zelfs rekening houdend met kleine sample, dit is een rode vlag.

2. **H11 CPC €0,73 — 46% boven target (€0,50).** Krijgt 71% van het dagbudget maar heeft laagste CTR (2,03%). Meta optimaliseert op volume, niet op kwaliteit.

3. **Campagne-CPC €0,62 — 24% boven target.** Getrokken door H11.

4. **H12 ondergebudgeteerd.** Beste CTR (4,21%), laagste CPC (€0,38), beste IC-rate, maar slechts 13% van het budget. Meta's auto-verdeling laat performance liggen.

5. **Geen PostHog-data** — cross-reference tussen ad-engagement en LP-engagement niet mogelijk vandaag.

## 6. Cross-Referencing Analyse (Meta-only)

| Pattern | Signaal | Interpretatie |
|---------|---------|---------------|
| H12: hoge CTR (4,21%) + laag CPC (€0,38) + beste IC-rate | Ad-audience match klopt | Hook resoneert met juiste doelgroep; opschalen |
| H11: CTR 2,03% + CPC €0,73 + 71% budget | Meta kiest volume boven kwaliteit | Campagne-level budget control nodig of adset pauzeren |
| LPV 78 + 0 Purchases | Checkout-breuk | Niet Meta's schuld, bottleneck zit op/na /booking |
| 7d Purch rate 0,5% van LP-clicks, vandaag 0% | Afwijking | Eén dag kan ruis zijn, maar in combinatie met 7 IC zonder Purchase is het een signaal |

## 7. Top 3 Acties voor Vandaag

### 1. Checkout flow verifieren. Escalatie: Rood
**Wat:** Test handmatig de volledige booking-flow op startyourballoonbusiness.com/booking, inclusief betaling (gebruik test-card of écht transactie).
**Waarom:** 7 Initiate Checkouts in 1 dag, 0 Purchases. 7d conversie was 27%, dus de kans op toeval is klein. Als de betaalstap stuk is, verlies je alle ROAS.
**Hoe:** Klik door van LP naar /booking, vul het formulier in, doorloop checkout. Check Wix Payments dashboard voor failed transactions. Check of recent update of plugin-conflict de trigger is.
**Verwachte impact:** Als fix, herstelt dagelijks €60-80 verloren revenue (op basis van 7d Purchase-waarde).

### 2. Budget-herverdeling forceren: H11 beperken, H12 opschalen. Escalatie: Geel
**Wat:** Stel ad set budget caps in om H11 te beperken tot max 35% en H12 op te schalen naar min 30% van het dagbudget.
**Waarom:** H11 kost 1,9x zoveel per click als H12 en heeft een lagere CTR. Campagne-CPC zou van €0,62 naar ~€0,50 kunnen dalen.
**Hoe:** Meta Ads Manager > Campaign 2026: SYBB > Ad sets. Switch van CBO naar ABO, of zet budget caps per ad set. Monitor 48u of Meta respecteert.
**Verwachte impact:** CPC richting €0,50 target, 15-25% meer clicks bij gelijk budget.

### 3. PostHog MCP connectie herstellen. Escalatie: Geel
**Wat:** Verifieer dat de PostHog MCP server correct geauthenticeerd is in `.claude/settings.json` of user settings.
**Waarom:** Zonder PostHog mist het rapport scroll depth, bounce rate en per-UTM on-page gedrag. De cross-reference tussen Meta CTR en LP-engagement is de kern van deze skill.
**Hoe:** Check `~/.claude.json` mcpServers.posthog. Herstart Claude Code. Test met een simpele PostHog query in een nieuwe sessie.
**Verwachte impact:** Vanaf morgen weer volledig cross-source rapport.

---

*Rapport gegenereerd op 19 april 2026 | Data bronnen: Meta Ads MCP (Pipeboard). PostHog MCP niet beschikbaar in deze sessie. | Campagne: 2026: SYBB (id 120239435987290239, account act_567892422940728)*
