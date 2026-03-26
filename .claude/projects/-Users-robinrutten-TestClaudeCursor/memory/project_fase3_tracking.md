---
name: Fase 3 Dag 8 — Funnel Tracking & UTMs
description: Status van GA4 setup, tracking standards, en UTM systeem voor Sempertex Europe. GA4 gekoppeld op 13 maart 2026, events moeten nog geconfigureerd worden.
type: project
---

Fase 3 Dag 8 (Funnel Tracking & UTMs) is gestart op 2026-03-13.

**GA4 Status (property 528249861 — SYBB):**
- GA4 tag gekoppeld op 2026-03-13 — pas vanaf nu wordt data verzameld
- Geen historische data beschikbaar voor de SYBB campagne (jan-mrt 2026)
- Geen custom dimensions ingesteld
- Geen conversie-events geconfigureerd
- Geen e-commerce events (purchase, add_to_cart, etc.)
- Alleen basis enhanced measurement actief (page_view, scroll, first_visit, session_start)
- Meta Pixel staat WEL op de site (events komen binnen via Meta Ads)

**Wat Robin handmatig moet doen in GA4:**
1. Conversie-events markeren (purchase, generate_lead, add_to_cart, sign_up, begin_checkout)
2. Custom dimensions aanmaken (utm_campaign, utm_content, utm_term, content_type, workshop_name)
3. Referral exclusions instellen (betaalproviders)
4. E-commerce events configureren op Wix (add_to_cart, begin_checkout, purchase met parameters)

**Why:** Zonder deze GA4 config kan /funnel-diagnose geen per-ad funnel breakdown tonen en missen we cruciale conversiedata.

**How to apply:** Bij elke campagne-gerelateerde taak checken of GA4 events al geconfigureerd zijn. Als niet: herinneren aan deze setup stappen.
