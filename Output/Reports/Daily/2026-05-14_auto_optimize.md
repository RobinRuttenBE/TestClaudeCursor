# Auto-Optimize Rapport — 2026-05-14

**Status: AFGEBROKEN — geen data beschikbaar, geen acties uitgevoerd.**

## Reden

De Meta Ads MCP (Pipeboard) gaf bij elke call de fout:

> Facebook connection required. Connect your account at https://pipeboard.co/connections to continue.

Beide calls op `act_567892422940728` en `act_607231713057715` faalden op `get_campaigns` met `status_filter: "ACTIVE"`. Zonder campagne-, adset- of ad-data konden de kill-regels (Link CTR < 0.8% bij ≥1.000 impressions, CPC (link) > €1.50 bij ≥500 link clicks) niet geëvalueerd worden.

## Strikte regel deze run

Alleen Meta Ads MCP (Pipeboard) en PostHog MCP toegestaan. Geen Google MCPs (Gmail, Calendar, Drive, Sheets, Docs, Slides). Geen schrijfacties naar de Meta Ads Tracker Google Sheet. Output uitsluitend lokale markdown. Deze regel is gevolgd — er is alleen Pipeboard aangeroepen, die faalde op auth.

## ⚡ Automatische acties uitgevoerd

Geen. De kill-regels zijn niet geëvalueerd omdat er geen insights binnenkwamen.

## ⚠️ Waarschuwingen

Geen. Frequency, CPM en lifetime-vergelijking konden niet berekend worden.

## 📊 70-20-10 Classificatie

Niet uitgevoerd. Vereist ad-niveau insights die niet beschikbaar zijn.

## 💡 Voorstellen (wacht op goedkeuring)

Geen voorstellen — een budget-herverdeling of variatie-suggestie zonder onderliggende data zou speculatie zijn.

## Vervolgactie voor Robin

1. Ga naar https://pipeboard.co/connections en herverbind het Facebook account.
2. Draai `/ads-auto-optimize` opnieuw zodra de verbinding hersteld is.
3. Als de verbinding al hersteld lijkt: controleer of de cached token in de MCP-server nog geldig is — Pipeboard kan een nieuwe handshake nodig hebben na een Facebook token refresh.

## Datakwaliteit

n/a — geen records opgehaald, dus geen min-impressions of min-24h-actief checks toegepast. Geen ads gepauzeerd; de 50%-vangrail is niet geraakt omdat er geen acties zijn ondernomen.
