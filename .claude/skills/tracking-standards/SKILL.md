---
name: Tracking Standards
description: Alle tracking regels, UTM conventies, pixel requirements en event configuratie voor Sempertex Europe. Gebruikt door /utm-generate, /tracking-check, /ads-deploy, /funnel-diagnose.
---

# Tracking Standards — Sempertex Europe

## Social Media Account IDs (hardcoded)

Gebruik ALTIJD en ALLEEN deze accounts bij Instagram/Facebook MCP calls:

| Platform | Account | ID |
|----------|---------|-----|
| **Instagram Business** | Sempertex Europe | `17841403335662168` |
| **Facebook Page** | Sempertex Europe | `215391235203393` |

**⚠️ NOOIT andere accounts gebruiken.** Er zijn ook Ambition Avenue en Project accounts gekoppeld — deze NEGEREN bij alle commands, reports en API calls.

---

## UTM Naming Conventions

**Globale regels:**
- Altijd lowercase
- Woorden scheiden met streepjes (-)
- Geen spaties, underscores of hoofdletters
- Datums in UTMs: YYYY-MM-DD format
- Elke link die traffic stuurt naar een Sempertex property MOET UTMs bevatten

---

### META ADS (betaald)

```
?utm_source=meta&utm_medium=paid-social&utm_campaign=[campagne]&utm_content=[ad-naam]
```

| Parameter | Waarde | Voorbeeld |
|-----------|--------|-----------|
| utm_source | `meta` | meta |
| utm_medium | `paid-social` | paid-social |
| utm_campaign | `[campagne-slug]` | sybb-workshop, silk-launch, nozzle-up-2027 |
| utm_content | `[hook-type]-[variant]` | statement-pricing-v1, question-dream-v2 |
| utm_term | optioneel, audience segment | eu-women-25-40, interest-balloons |

**Ad naming convention:**
```
[DATUM]_[CAMPAGNE]_[AUDIENCE]_[HOOK-TYPE]
```
Voorbeeld: `2026-03-14_SYBB_EU-Women-25-40_Statement-Hook13`

**Volledige URL voorbeeld:**
```
https://startyourballoonbusiness.com/workshops?utm_source=meta&utm_medium=paid-social&utm_campaign=sybb-workshop&utm_content=statement-pricing-v1&utm_term=eu-women-25-40
```

---

### EMAIL

```
?utm_source=email&utm_medium=email&utm_campaign=[flow-naam]&utm_content=[email-id]
```

| Parameter | Waarde | Voorbeeld |
|-----------|--------|-----------|
| utm_source | `email` | email |
| utm_medium | `email` | email |
| utm_campaign | `[flow-naam]` | sybb-pre-workshop, sybb-post-workshop, newsletter-weekly |
| utm_content | `[email-nummer-of-naam]` | day1-welcome, day3-reviews, reminder-3days |

**Volledige URL voorbeeld:**
```
https://startyourballoonbusiness.com/workshops?utm_source=email&utm_medium=email&utm_campaign=sybb-pre-workshop&utm_content=day2-quick-win
```

---

### SOCIAL MEDIA ORGANISCH

```
?utm_source=[platform]&utm_medium=organic-social&utm_campaign=[content-type]&utm_content=[post-id]
```

| Parameter | Waarde | Voorbeeld |
|-----------|--------|-----------|
| utm_source | `instagram`, `facebook`, `tiktok` | instagram |
| utm_medium | `organic-social` | organic-social |
| utm_campaign | `[content-type]` | link-in-bio, reel-promo, story-swipeup |
| utm_content | `[beschrijving]` | sybb-workshop-promo, silk-launch-teaser |

---

### YOUTUBE

```
?utm_source=youtube&utm_medium=organic-video&utm_campaign=[video-naam]&utm_content=[link-positie]
```

| Parameter | Waarde | Voorbeeld |
|-----------|--------|-----------|
| utm_source | `youtube` | youtube |
| utm_medium | `organic-video` | organic-video |
| utm_campaign | `[video-slug]` | podcast-ep1-denise, sybb-pricing-tips |
| utm_content | `[link-positie]` | description-top, pinned-comment, end-card |

---

### LINKEDIN

```
?utm_source=linkedin&utm_medium=organic-social&utm_campaign=[post-type]&utm_content=[beschrijving]
```

| Parameter | Waarde | Voorbeeld |
|-----------|--------|-----------|
| utm_source | `linkedin` | linkedin |
| utm_medium | `organic-social` | organic-social |
| utm_campaign | `[post-type]` | thought-leadership, company-update, event-promo |
| utm_content | `[beschrijving]` | sybb-launch-announcement |

---

## Meta Pixel Requirements

### Waar moet de pixel staan
- Alle landing pages
- Booking/opt-in pages
- Checkout pages
- Thank you / confirmation pages
- Alle pagina's op startyourballoonbusiness.com
- Alle pagina's op sempertexeurope.com (als van toepassing)

### Standaard events te tracken

| Event | Wanneer | Pagina |
|-------|---------|--------|
| PageView | Elke paginalading | Alle pagina's |
| ViewContent | Bezoeker bekijkt workshop/product details | Workshop detail pagina's |
| Lead | Opt-in formulier ingevuld, free value download | Opt-in/lead pagina's |
| AddToCart | Workshop in winkelwagen | Booking pagina |
| InitiateCheckout | Start checkout proces | Checkout pagina |
| Purchase | Betaling voltooid | Thank you pagina |
| CompleteRegistration | Workshop inschrijving bevestigd | Bevestigingspagina |

### Custom conversies

| Conversie | Trigger | Prioriteit |
|-----------|---------|-----------|
| Workshop inschrijving | Purchase event met workshop parameter | Hoog |
| Free value download | Lead event met content_name parameter | Hoog |
| Newsletter signup | Lead event met signup_method parameter | Medium |
| Contact formulier | Lead event met form_type parameter | Medium |

---

## GA4 Event Configuration

### Vereiste events (moeten handmatig ingesteld worden op Wix)

| Event | Parameters | Trigger |
|-------|-----------|---------|
| `page_view` | page_title, page_location | Automatisch (enhanced measurement) |
| `scroll` | percent_scrolled | Automatisch (enhanced measurement) |
| `click` | link_url, link_domain, outbound | Automatisch (enhanced measurement) |
| `view_content` | content_type, content_id, value | Bezoeker bekijkt workshop details |
| `generate_lead` | value, currency, form_type | Formulier ingevuld / opt-in |
| `add_to_cart` | currency, value, items[] | Workshop in winkelwagen |
| `begin_checkout` | currency, value, items[] | Checkout gestart |
| `purchase` | transaction_id, currency, value, items[] | Betaling voltooid |
| `sign_up` | method | Newsletter inschrijving |

### Vereiste custom dimensions in GA4

| Dimensie | Scope | Beschrijving |
|----------|-------|-------------|
| utm_campaign | Event | Campagne naam uit UTM |
| utm_content | Event | Ad/content identifier uit UTM |
| utm_term | Event | Keyword/audience uit UTM |
| content_type | Event | Type content (workshop, free-value, product) |
| workshop_name | Event | Naam van de workshop |
| workshop_date | Event | Datum van de workshop |

### Conversie-events markeren in GA4

De volgende events moeten als **conversie** gemarkeerd worden in GA4 Admin:
1. `purchase` — hoogste prioriteit
2. `generate_lead` — lead captures
3. `add_to_cart` — intent signaal
4. `sign_up` — newsletter groei
5. `begin_checkout` — checkout intent

---

## Referral Exclusions

Stel de volgende domeinen in als referral exclusions in GA4:
- Betaalproviders (Mollie, Stripe, PayPal, iDeal redirect domeinen)
- Wix eigen domeinen (als redirect via wix plaatsvindt)
- startyourballoonbusiness.com (eigen domein)

---

## Validatie Checklist

Voordat een campagne live gaat, MOET het volgende kloppen:

- [ ] Elke ad URL bevat correcte UTM parameters
- [ ] UTMs volgen de naming convention (lowercase, streepjes)
- [ ] Meta Pixel staat op alle funnel pagina's
- [ ] GA4 tag staat op alle pagina's
- [ ] Conversie-events zijn geconfigureerd en getest
- [ ] Referral exclusions zijn ingesteld
- [ ] Test-conversie is succesvol doorlopen (klik ad → LP → checkout → purchase)
