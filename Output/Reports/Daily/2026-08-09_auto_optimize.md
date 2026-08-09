Het rapport staat in `Output/Reports/Daily/2026-08-09_auto_optimize.md` en is gecommit en gepusht (de auto-sync job pakte het op in commit `2fb8c2bb`).

## Auto-Optimize, 9 augustus 2026

**De run is geblokkeerd.** De Pipeboard Meta Ads connector is niet geautoriseerd in deze sessie, en omdat dit een niet-interactieve sessie is kan ik de OAuth flow hier niet starten. Zonder Meta data kon geen enkele stap van het optimalisatieproces draaien: geen kill regels, geen pauzeringen, geen 70-20-10 classificatie, geen budgetvoorstellen. Derde dag op rij.

**Gepauzeerd: 0 ads.** Let op het verschil: dit is niet "alles presteert goed", dit is "niets is beoordeeld".

### Wat ik wel heb kunnen vaststellen

PostHog bevestigt nul betaald verkeer over de afgelopen 3 dagen. Van 2.662 bezoekers kwam er geen enkele via Paid Social. Het kanaal komt niet eens voor in de verdeling. Direct 72,6%, Referral 18,2%, Organic Search 7,6%. Laatste `meta/cpc/sybb` klik was 1 juli, nu 39 dagen geleden.

Belangrijke beperking daarbij: PostHog ziet klikken, geen spend of impressions. Dus dit bewijst niet dat er nul budget loopt. Een ad kan impressions draaien en geld opmaken zonder een enkele klik, en juist dat scenario is nu onzichtbaar. Dat is precies waar de kill regels voor bestaan.

Daarom staat als voorstel 2 in het rapport: check even handmatig in Ads Manager of er spend loopt op `act_567892422940728` en `act_607231713057715`. Spend groter dan nul met nul klikken betekent direct met de hand pauzeren.

### Wat opviel in de data

De Mailjet campagne `workshop_tobi_promo_202608` bracht 11 bezoekers en is correct getagd op bron, medium en campagne. Klaviyo staat er nog steeds bij als `Klaviyo / email / (none)`, dus zonder `utm_campaign`. Mailjet is hier de standaard die Klaviyo zou moeten volgen.

### Om te ontblokkeren

Autoriseer Pipeboard via je claude.ai connector instellingen, of via `/mcp` in een interactieve sessie. Zolang dat open staat draait dit command elke ochtend leeg en heeft de automatische bewaking geen effect.

Eén ding dat van jou moet komen: de 70-20-10 drempels staan sinds de overstap naar link metrics op 13 april nog gemarkeerd als richtlijn, niet als hard oordeel. Die wil je vastgesteld hebben voordat Pipeboard weer data levert, anders classificeert het systeem op waarden die op een andere metriek zijn geijkt.
