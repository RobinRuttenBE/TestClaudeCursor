# Morning Report — 2026-06-23

Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties.
Failures: 0

---

## Meta Ads Rapport, 23 June 2026

⚠️ **Er zijn geen actieve campagnes.** Alle campagnes in het Sempertex Ad Account (`act_567892422940728`) staan op PAUSED. Het account `act_607231713057715` (Robin Rutten) is niet bereikbaar met de huidige token. Hieronder de **laatst bekende lifetime data** van de twee meest recente gepauzeerde campagnes. Spend laatste 30 dagen: **€0,00**.

### Overzicht per campagne (lifetime)

| Campagne | Status | Spend | Impr. | Clicks | CTR | CPC | CPM | Purch. |
|----------|--------|-------|-------|--------|-----|-----|-----|------|
| 2026: SYBB | Paused | €2.485,04 | 297.174 | 12.067 | 4,1% | €0,21 | €8,36 | 6 |
| 2026: SYBB - Kopie | Paused | €124,42 | 7.615 | 195 | 2,6% | €0,64 | €16,34 | 0 |

### Belangrijkste bevindingen

- **Winnaar: hook H13.** In set 1 trok H13 **5.902 clicks tegen €0,07 CPC en 9,8% CTR**, ver boven alle andere hooks. Dit is je bewezen winnaar.
- **Runner-ups:** H15 (CTR 4,3%, CPC €0,15) en H14 (CTR 2,7%, CPC €0,26) zijn gezond.
- **Underperformers:** de "Kopie" campagne (CPC €0,64 + CPM €16,34, beide boven drempel), ad `SYBB w/ Semp (BLACK)` (CTR 1,0%, CPC €0,61), en de dure set-2 varianten van H11 en H13 (CPC €0,63 tot €0,67).
- **Creative fatigue:** geen probleem, frequency max 2,24.

⚠️ **ROAS waarschuwing:** De purchase conversiewaarde van Meta is onbetrouwbaar. De 6 purchases tonen €44.247 totaal, maar dat zit in twee tegenstrijdige ads: één ad rapporteert €42.773 op 2 purchases (duidelijke uitschieter, waarschijnlijk pixel value fout). Naïeve ROAS zou 17,8x zijn, maar dat is vertekend. **Verifieer de echte orderwaarden in Wix/Shop voordat je op ROAS stuurt.** Betrouwbaarder signaal nu: circa €414 cost per purchase.

### Aanbeveling (70-20-10)
Bij heractivatie: **70%** op de bewezen winnaar H13 (set 1 config), **20%** op H13-variaties plus H15/H14, **10%** experimenten. Kill de "BLACK" creative en de dure set-2 varianten.

Rapport opgeslagen in `Output/Reports/Daily/2026-06-23_ads_report.md` (gecommit en gepusht). Google Sheet stap overgeslagen per de strikte regel.

---

> **Wil je funnel data toevoegen? Geef dan de landing page metrics uit Wix Analytics of GA4.**
> Ik heb nodig: landing page visitors, opt-in/booking clicks, add to cart, completed purchases.

(Of, omdat alles gepauzeerd staat, kan ik ook de PostHog landing page health voor startyourballoonbusiness.com erbij halen, alleen die MCP is toegestaan deze run. Zeg maar of je dat wilt.)

---

Klaar. Het rapport staat in `Output/Reports/Daily/2026-06-22_sybb_report.md` en is gecommit + gepusht.

## Belangrijkste bevindingen

Twee zaken maken dat dit geen "gewoon" dagrapport kon worden — beide eerlijk in het rapport verwerkt:

**1. Campagne "2026: SYBB" staat UIT (PAUSED)**
Via de Meta Ads MCP: gisteren (22 juni) **nul** impressies, clicks en spend — en hetzelfde over het hele 7-daagse venster. De campagne draait feitelijk niet meer sinds eind april 2026. Ter referentie heb ik de laatste actieve maanden wél opgenomen (maart 2026 was de topmaand: CTR 5,27%, CPC €0,13).

**2. PostHog MCP is niet verbonden in deze sessie**
Er zijn géén PostHog-tools beschikbaar (wel Meta Ads/Pipeboard, ga4, google, instagram, etc.). Conform jouw strikte regel heb ik **bewust geen** GA4- of andere Google-bron als vervanger gebruikt, en niets naar de Google Sheet geschreven. Alle output is alleen lokale markdown.

## Top 3 acties uit het rapport
1. **Beslis over heractivatie** van "2026: SYBB" — al ~2 maanden stil (strategie/Robin).
2. **Verbind de PostHog MCP** vóór het volgende rapport, anders mist het standaard de helft van zijn data.
3. Overweeg het dagrapport op te schorten zolang de campagne PAUSED blijft, om ruis te vermijden.

Wil je dat ik de campagne-heractivatie verder uitwerk (budget + winnende maart-creatives), of eerst help met het verbinden van de PostHog MCP?

---

Klaar. Rapport opgeslagen en gepusht.

## Samenvatting

**Geen optimalisaties uitgevoerd — er zijn geen actieve campagnes.**

Op het primaire Sempertex-account (`act_567892422940728`) staan alle 5 campagnes op **PAUSED**, inclusief `2026: SYBB`. Er waren dus geen actieve ads om tegen de kill-regels te toetsen of volgens 70-20-10 te classificeren. Dit klopt met het SYBB-dagrapport van 22 juni (campagne gepauzeerd).

Twee aandachtspunten:
- **Tweede account `act_607231713057715` niet toegankelijk** — de API-token geeft alleen toegang tot `act_1489853856181844` en `act_567892422940728`. Dit account kon niet worden geanalyseerd.
- **Geen Niveau 1 acties** (niets te pauzeren) en **geen Niveau 2 voorstellen** mogelijk zonder lopende campagne.

Alleen Meta Ads MCP gebruikt, geen Google MCP's, niet naar de tracker Sheet geschreven. Rapport staat in `Output/Reports/Daily/2026-06-23_auto_optimize.md`.

Wil je dat ik `2026: SYBB` (dagbudget €100,00) heractiveer zodat er weer data opbouwt voor een volgende ronde?

---

## VERIFIED FUNNEL PER AD (30 dagen)

> Geen per-ad Meta data beschikbaar.



Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar.
