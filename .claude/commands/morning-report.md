# Morning Report — Dagelijkse Briefing

Genereer een ochtendrapport voor Robin (Head of Marketing, Sempertex Europe). Haal de volgende informatie op en vat samen in een overzichtelijk Nederlands rapport:

## Stappen

### 1. Agenda vandaag
Gebruik `mcp__google__calendar_events_list` met calendar_id "primary", time_min = vandaag 00:00 (RFC3339), time_max = vandaag 23:59 (RFC3339). Haal max 20 events op.

### 2. Laatste emails
Gebruik `mcp__google__gmail_messages_list` met max_results 5. Lees vervolgens elk bericht met `mcp__google__gmail_message_get` om de inhoud te bekijken.

### 3. Recente Drive activiteit
Gebruik `mcp__google__drive_files_list` met page_size 10 om recent gewijzigde bestanden te zien.

## Output format

Schrijf het rapport in dit format:

```
## ☀️ Ochtendrapport — [datum]

### 📅 Agenda vandaag
- [tijd] — [event naam] (locatie/link indien beschikbaar)
- ...
(of: "Geen afspraken vandaag — focus dag!")

### 📧 Laatste 5 emails
- **[afzender]** — [onderwerp] → [1-zin samenvatting van de inhoud]
- ...

### 📁 Recente Drive activiteit
- [bestandsnaam] — laatst gewijzigd [datum/tijd]
- ...

### 📊 Funnel Diagnose
[Als er een actieve Meta Ads campagne draait: draai automatisch /funnel-diagnose en toon hier de verkorte versie]
- Funnel tabel (6 stappen met status)
- #1 bottleneck
- Belangrijkste actiepunt
(of: "Geen actieve campagnes — geen funnel data")

### 🎯 Suggestie voor vandaag
[Geef op basis van de agenda, emails EN funnel diagnose 1-2 concrete suggesties voor waar Robin vandaag op kan focussen, gerelateerd aan lopende marketing projecten]
```

## Regels
- Schrijf in het Nederlands
- Wees bondig maar informatief
- Markeer urgente items (deadlines, belangrijke meetings) met ⚠️
- Als er geen data beschikbaar is voor een sectie, geef dat netjes aan
