# Auto-Optimize Rapport, 6 augustus 2026

**Status van deze run: geblokkeerd op de databron. Geen enkele automatische actie uitgevoerd.**

De Meta Ads MCP (Pipeboard) is in deze sessie niet geautoriseerd. Beide servers, `claude.ai Pipeboard Meta Ads` en `pipeboard-meta-ads`, vragen om een OAuth flow die in een niet-interactieve sessie niet kan draaien. Daardoor konden stap 1 tot en met 6 van het command niet draaien: geen campagnes, geen ad sets, geen ads, geen insights, geen `update_ad` calls.

Toegestane bronnen deze run: Meta Ads MCP en PostHog MCP. Alle Google MCPs zijn overgeslagen zoals gevraagd. Er is niet naar de Meta Ads Tracker Google Sheet geschreven.

---

## Automatische acties uitgevoerd

**Geen.** Nul ads gepauzeerd, nul ads aangeraakt.

Dit is nadrukkelijk niet hetzelfde als "alles presteert boven de drempelwaarden". De kill-regels konden niet geëvalueerd worden omdat er geen ad-level data beschikbaar was. Zonder `actions.link_click` en `impressions` per ad is Link CTR niet te berekenen, en zonder `spend` per ad is CPC (link) niet te berekenen. Beide kill-regels draaien uitsluitend op die link-varianten, dus er valt niets te toetsen.

| Regel | Drempel | Kon getoetst worden? |
|---|---|---|
| Lage Link CTR | Link CTR < 0,8% bij ≥ 1.000 impressions | Nee, geen ad-level insights |
| Hoge CPC (link) | CPC (link) > €1,50 bij ≥ 500 link clicks | Nee, geen ad-level insights |

---

## Waarschuwingen

Frequency, CPM en Link CTR-verval komen alle drie uit Meta insights. Geen van de drie waarschuwingsregels kon draaien.

---

## Wat PostHog wel bevestigt

PostHog is wel bereikbaar en geeft onafhankelijke bevestiging dat er op dit moment niets te optimaliseren valt.

**Kanaalverdeling laatste 3 dagen (project STX EU):**

| Kanaal | Bezoekers | Pageviews | Bounce rate |
|---|---|---|---|
| Direct | 2.244 | 10.307 | 41,3% |
| Referral | 864 | 3.331 | 76,9% |
| Organic Search | 203 | 4.266 | 3,9% |
| Email | 46 | 260 | 18,8% |
| AI | 29 | 118 | 17,2% |
| Organic Social | 6 | 17 | 16,7% |
| Organic Video | 1 | 1 | 0,0% |

**Er is geen Paid Social kanaal.** Nul bezoekers.

De UTM-uitsplitsing over dezelfde 3 dagen bevestigt dat: geen enkele hit op `utm_source=meta` of `utm_medium=cpc`. De enige getagde bronnen zijn email (`mailjet / email / workshop_tobi_promo_202608` met 35 bezoekers, `newsletter / email / fr_client` met 1, `Klaviyo / email` met 4 ongetagd) en één partner referral (`partner / referral / distributor_evergreen_202607`). De 3 bezoekers via `referrer:www.facebook.com` en 2 via `referrer:facebook.com` zijn organisch verkeer zonder UTM, geen ads.

Dit sluit aan op de meting van 4 augustus en het rapport van vanochtend: alle campagnes staan op PAUSED, de campagne `2026: SYBB` (id `120239435987290239`) sinds 19 april 2026, en de laatste uitgave was april 2026.

---

## 70-20-10 Classificatie

Niet uit te voeren. De classificatie vereist Link CTR en CPC (link) per actieve ad. Met nul actieve ads en nul insights is er niets te classificeren en geen budget te verdelen.

Ter herinnering staat de kalibratie-TODO uit het command nog open: de 70-20-10 drempels zijn nog gebaseerd op all-clicks metrics en moeten door Robin herzien worden voor link metrics. Zolang dat niet gebeurd is, blijven budget-shifts op basis van die getallen sowieso ongeldig.

**Budget mismatch:** niet vast te stellen.

---

## Voorstellen (wacht op goedkeuring)

Er zijn geen data-gedreven voorstellen te doen zonder performance data. Wat wel staat, is de volgorde van blokkades. Deze drie moeten opgelost zijn voordat een auto-optimize run überhaupt zinvol wordt.

**1. Autoriseer Pipeboard**

Dit blokkeert alles. Zonder Meta data draait dit command leeg, elke dag opnieuw.

Actie: autoriseer `claude.ai Pipeboard Meta Ads` via je claude.ai connector instellingen, of draai `/mcp` in een interactieve Claude Code sessie voor `pipeboard-meta-ads`.

**2. Zet de pixel op de juiste funnel voordat budget aangaat**

`CLAUDE.md` en `skills/daily-sybb-report/SKILL.md` gaan uit van `startyourballoonbusiness.com` met `utm_content` varianten en een `/booking` conversie. De werkelijke SYBB funnel loopt sinds 5 augustus via event registratiepagina's op `sempertexeurope.com` (`/event/start-your-balloon-business-professional-7/register` en de Duitse variant). De landing page heeft wel een pixel maar kreeg sinds 31 juli nul verkeer, en mist scroll-, CTA- en booking-events volledig.

Zolang dat niet is rechtgezet, zou een herstart van budget verkeer sturen naar een pagina die niet of verkeerd gemeten wordt. Het auto-optimize command kan dan wel Meta-zijdig pauzeren, maar de landingspagina-kant van de beslissing blijft blind.

Actie: stel eerst met Robin vast welke funnel canoniek is, en richt de tracking daarop in.

**3. Fix de conversiewaarde tracking vóór herstart**

De ROAS van 17,81x uit een eerdere meting is vrijwel zeker een pixelfout. Als die waarde blijft staan, classificeert het 70-20-10 model straks ads als Core (ROAS > 2x) op basis van verzonnen omzet, en verschuift het budget de verkeerde kant op.

---

**Wil je een of meer van deze voorstellen uitvoeren? Geef aan welke nummers.**

Zodra Pipeboard geautoriseerd is, kan deze run zonder wijzigingen opnieuw draaien en levert hij wel echte kill-rule beslissingen op.

---

*Gegenereerd 2026-08-06. Bronnen: PostHog MCP (project STX EU, id 149694). Meta Ads MCP niet beschikbaar.*
