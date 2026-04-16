#!/bin/bash
# morning-report.sh — Dagelijks Meta Ads + PostHog rapport via Claude Code
# Draait via launchd elke ochtend om 08:00 (com.sempertex.morning-report.plist)
#
# Flow: /ads-report → SYBB daily report → /ads-auto-optimize → git push → iMessage
#
# DATA SCOPE (strikt):
#   - Meta Ads MCP (Pipeboard) — campagne, adset, ad insights
#   - PostHog MCP — landing page sessies, bounce, scroll, recordings
#
# DELIVERY:
#   - Markdown rapporten naar Output/Reports/Daily/
#   - Auto-commit + push naar GitHub main
#   - iMessage notificatie naar Robin met link naar de full report op GitHub
#
# GEEN Google integraties:
#   - Geen Gmail send
#   - Geen Google Calendar / Drive / Sheets / Docs / Slides
#   - Geen OAuth tokens, geen refresh-cycle
#
# Authenticatie:
#   - Git push via bestaande SSH/HTTPS credentials in de repo (zelfde als auto-sync cron)
#   - iMessage via macOS Messages.app + Apple ID (al ingelogd)
#   - Geen wachtwoorden of API tokens in dit script

set -uo pipefail

# Harde wall-clock limiet per Claude stap. Voorkomt dat een hangende MCP call
# (zoals 2026-04-14 en 2026-04-15, waar /ads-report 1+ uur bleef plakken) de
# hele chain blokkeert en iMessage nooit wordt verstuurd.
CLAUDE_STEP_TIMEOUT_SEC=600

# Paden
CLAUDE="/Users/robinrutten/.local/bin/claude"
WORKDIR="/Users/robinrutten/TestClaudeCursor"
LOG_DIR="${WORKDIR}/logs"
LOG_FILE="${LOG_DIR}/morning-report-$(date +%Y-%m-%d).log"
TODAY_ISO=$(date +"%Y-%m-%d")
YESTERDAY_ISO=$(date -v-1d +"%Y-%m-%d")

# Idempotency marker — zodra dit bestand voor vandaag bestaat, slaan we de
# volledige run over. Launchd mag het script dus elke paar minuten triggeren
# (StartInterval + RunAtLoad) zonder dat we dubbele rapporten sturen.
DONE_MARKER="${LOG_DIR}/morning-report-${TODAY_ISO}.done"

# Vroeg filteren: niet draaien vóór 08:00 en niet nog een keer als vandaag al
# klaar is. Laat het script stil exit'en zodat launchd logs niet vollopen.
CURRENT_HOUR=$(date +%H)
if [ -f "$DONE_MARKER" ]; then
    exit 0
fi
if [ "$CURRENT_HOUR" -lt 8 ]; then
    exit 0
fi

# Casing van REPORT_DIR matcht git's canonical pad (zie `git ls-files Output/Reports/Daily/`)
REPORT_DIR="${WORKDIR}/Output/Reports/Daily"
ADS_REPORT_FILE="${REPORT_DIR}/${TODAY_ISO}_ads_report.md"
SYBB_REPORT_FILE="${REPORT_DIR}/${YESTERDAY_ISO}_sybb_report.md"
OPTIMIZE_REPORT_FILE="${REPORT_DIR}/${TODAY_ISO}_auto_optimize.md"
FULL_REPORT_FILE="${REPORT_DIR}/${TODAY_ISO}_morning_report_full.md"

# Verified funnel data
WIX_ORDERS_FILE="${LOG_DIR}/morning-report-${TODAY_ISO}.wix-orders.json"
WIX_ORDERS_FALLBACK="${WORKDIR}/data/wix-orders.json"
WIX_SITE_ID="476f7384-3ec8-4157-8440-73bef7409891"
FETCH_WIX_SCRIPT="${WORKDIR}/scripts/fetch-wix-orders.py"
POSTHOG_SESSIONS_FILE="${LOG_DIR}/morning-report-${TODAY_ISO}.posthog-sessions.json"
VERIFIED_FUNNEL_SCRIPT="${WORKDIR}/scripts/verified-funnel.py"
THIRTY_DAYS_AGO=$(date -v-30d +"%Y-%m-%d")

# iMessage delivery
IMESSAGE_RECIPIENT="+32468236146"
IMESSAGE_HELPER="${WORKDIR}/scripts/send-imessage.py"
# Markdown reports: GitHub blob URL rendert .md files netjes met tabellen/headers
GITHUB_BLOB_BASE="https://github.com/RobinRuttenBE/TestClaudeCursor/blob/main/Output/Reports/Daily"
# HTML dashboard: GitHub Pages rendert HTML visueel (niet als source code)
DASHBOARD_URL="https://robinruttenbe.github.io/TestClaudeCursor/SYBB_Dashboard.html"

FAILURES=0

# Standaard "no-google" instructie die aan elke Claude prompt wordt geplakt
NO_GOOGLE_RULE="STRIKTE REGEL voor deze run: gebruik ALLEEN de Meta Ads MCP (Pipeboard) en de PostHog MCP. Roep GEEN Google MCPs aan: geen Gmail (mcp__google__gmail_*, mcp__claude_ai_Gmail__*), geen Google Calendar (mcp__google__calendar_*, mcp__claude_ai_Google_Calendar__*), geen Google Drive (mcp__google__drive_*), geen Google Sheets (mcp__google__sheets_*), geen Google Docs (mcp__google__docs_*), geen Google Slides (mcp__google__slides_*). Schrijf NIET naar de Meta Ads Tracker Google Sheet. Sla alle output uitsluitend op naar lokale markdown files in output/reports/daily/."

# Zorg dat log + report directories bestaan
mkdir -p "$LOG_DIR"
mkdir -p "$REPORT_DIR"
cd "$WORKDIR"

echo "=== Morning Report gestart: $(date) ===" >> "$LOG_FILE" 2>&1
echo "Scope: Meta Ads MCP + PostHog MCP. Geen Google integraties." >> "$LOG_FILE" 2>&1

# Helper: draai een Claude command met retry
run_claude() {
    local label="$1"
    local prompt="$2"
    local max_attempts=2
    local attempt=1
    local result=""

    while [ $attempt -le $max_attempts ]; do
        echo "  [poging ${attempt}/${max_attempts}] ${label} (timeout ${CLAUDE_STEP_TIMEOUT_SEC}s)..." >> "$LOG_FILE" 2>&1
        # Python wrapper: harde wall-clock timeout met process-group kill.
        # perl alarm+exec werkte niet op macOS omdat alarm(2) timers niet
        # bewaard blijven over exec — SIGALRM vuurde nooit en stap 1 bleef
        # 1+ uur hangen (incidenten 2026-04-14 en 2026-04-15).
        # Exit 124 = timeout hit (matcht GNU coreutils `timeout`).
        result=$(/usr/bin/python3 -c '
import os, signal, subprocess, sys
timeout = int(sys.argv[1])
cmd = sys.argv[2:]
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=sys.stderr, preexec_fn=os.setsid)
try:
    out, _ = p.communicate(timeout=timeout)
    sys.stdout.buffer.write(out)
    sys.exit(p.returncode)
except subprocess.TimeoutExpired:
    try:
        os.killpg(os.getpgid(p.pid), signal.SIGTERM)
    except ProcessLookupError:
        pass
    try:
        p.wait(timeout=5)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(os.getpgid(p.pid), signal.SIGKILL)
        except ProcessLookupError:
            pass
    sys.exit(124)
' "$CLAUDE_STEP_TIMEOUT_SEC" \
            "$CLAUDE" -p "$prompt" \
            --output-format text \
            --max-turns 30 \
            --dangerously-skip-permissions \
            2>> "$LOG_FILE")
        local rc=$?
        if [ $rc -eq 0 ] && [ -n "$result" ]; then
            break
        fi
        if [ $rc -eq 124 ]; then
            echo "  [poging ${attempt}] TIMEOUT na ${CLAUDE_STEP_TIMEOUT_SEC}s (process group gekilled)" >> "$LOG_FILE" 2>&1
        else
            echo "  [poging ${attempt}] mislukt (exit ${rc})" >> "$LOG_FILE" 2>&1
        fi
        attempt=$((attempt + 1))
        [ $attempt -le $max_attempts ] && sleep 5
    done

    if [ -z "$result" ]; then
        FAILURES=$((FAILURES + 1))
        echo "[WARN] ${label} mislukt na ${max_attempts} pogingen" >> "$LOG_FILE" 2>&1
        echo ""
        return 1
    fi

    echo "$result"
}

# --- Stap 1/3: /ads-report (Meta Ads only — geen Google Sheets) ---
echo "[1/6] /ads-report uitvoeren..." >> "$LOG_FILE" 2>&1
ADS_PROMPT="/ads-report

${NO_GOOGLE_RULE}

Aanvullend voor /ads-report: sla stap 6 (Google Sheet write naar Meta Ads Tracker) volledig over. Sla het rapport in plaats daarvan op in ${ADS_REPORT_FILE}."

REPORT=$(run_claude "/ads-report" "$ADS_PROMPT") || \
    REPORT="Ads rapport niet beschikbaar. Campagnes staan momenteel op pauze."

printf '%s\n' "$REPORT" > "$ADS_REPORT_FILE" 2>> "$LOG_FILE"
echo "[1/6] klaar ($(echo "$REPORT" | wc -c | tr -d ' ') bytes, opgeslagen in $ADS_REPORT_FILE)" >> "$LOG_FILE" 2>&1

# --- Stap 2/3: SYBB Daily Report (Meta + PostHog) ---
echo "[2/6] SYBB daily report uitvoeren..." >> "$LOG_FILE" 2>&1
SYBB_PROMPT="Genereer het dagelijkse SYBB rapport voor gisteren. Haal Meta Ads data op voor campagne \"2026: SYBB\" via de Meta Ads MCP. Haal PostHog data op voor startyourballoonbusiness.com via de PostHog MCP. Combineer beide databronnen en volg de rapportstructuur uit skills/daily-sybb-report/SKILL.md. Sla het rapport op in ${SYBB_REPORT_FILE}.

${NO_GOOGLE_RULE}"

SYBB_REPORT=$(run_claude "SYBB daily report" "$SYBB_PROMPT") || \
    SYBB_REPORT="SYBB rapport niet beschikbaar."

echo "[2/6] klaar ($(echo "$SYBB_REPORT" | wc -c | tr -d ' ') bytes, sub-Claude schrijft naar $SYBB_REPORT_FILE)" >> "$LOG_FILE" 2>&1

# --- Stap 3/3: /ads-auto-optimize (Meta only) ---
echo "[3/6] /ads-auto-optimize uitvoeren..." >> "$LOG_FILE" 2>&1
OPTIMIZE_PROMPT="/ads-auto-optimize

${NO_GOOGLE_RULE}

Sla het rapport op in ${OPTIMIZE_REPORT_FILE}."

OPTIMIZE=$(run_claude "/ads-auto-optimize" "$OPTIMIZE_PROMPT") || \
    OPTIMIZE="Auto-optimize niet beschikbaar. Geen actieve campagnes."

printf '%s\n' "$OPTIMIZE" > "$OPTIMIZE_REPORT_FILE" 2>> "$LOG_FILE"
echo "[3/6] klaar ($(echo "$OPTIMIZE" | wc -c | tr -d ' ') bytes, opgeslagen in $OPTIMIZE_REPORT_FILE)" >> "$LOG_FILE" 2>&1

# --- Stap 4/4: Purchase Sanity Check + Link Metrics (HARDCODED) ---
# Deze stap haalt in één narrow JSON call alle campagne-totals op:
# purchase_value/count + spend + impressions + link_clicks. De Python
# evaluator berekent zelf de sanity verdict EN de link CTR / CPC (link),
# en pixel-datafout-rewrite.py overschrijft daarna de kale "CTR" / "CPC"
# cellen in het rapport met de correcte link-based waarden.
#
# Achtergrond:
# - 2026-04-15: /ads-report meldde "ROAS 60,95x" terwijl pv/pc = EUR 21.386
#   per purchase, ~50x de ticketprijs. Sanity check zat alleen als
#   instructie — werd genegeerd door sub-claude.
# - 2026-04-15 (tweede incident): rapport toonde "CTR 2,0% / CPC EUR 0,52"
#   als kale Meta standaard (all clicks) ondanks dat het command expliciet
#   `actions.link_click` voorschrijft. 4e keer dat deze regel werd
#   overgeslagen door sub-claude. Dus nu: link metrics worden eveneens
#   hardcoded berekend en het rapport wordt overschreven.
echo "[4/6] sanity + link metrics fetch (campagne + per-ad + active days)..." >> "$LOG_FILE" 2>&1

PURCHASE_PROMPT="Haal via de Meta Ads MCP (Pipeboard) voor campagne '2026: SYBB' het volgende op over de afgelopen 30 dagen:

A. CAMPAGNE TOTALS (hele periode):
   - purchase_value: som van action_values waar action_type een purchase event is ('purchase', 'omni_purchase', 'offsite_conversion.fb_pixel_purchase')
   - purchase_count: som van actions voor dezelfde action_types
   - spend: totaal spend in EUR
   - impressions: totaal aantal impressions
   - link_clicks: totaal aantal LINK clicks — KRITIEK: gebruik action_type 'link_click' uit de actions array, NIET het standaard 'clicks' veld

B. ACTIVE DAYS COUNT:
   - Haal daily breakdown op met time_increment=1 (dagelijkse spend)
   - Tel het aantal dagen waarop spend > 0
   - Output als 'active_days' integer

C. PER-AD METRICS (alleen ads met spend > 0 in deze periode, ongeacht status):
   - Voor elke ad: name (exact zoals in Meta), spend, impressions, link_clicks (actions.link_click)
   - Output als 'ads' array met per-ad objecten

Output UITSLUITEND één regel valide JSON, inline (geen newlines in de JSON zelf). Geen prose, geen markdown, geen code fences, geen uitleg. Exact formaat:
{\"purchase_value\": <float>, \"purchase_count\": <int>, \"spend\": <float>, \"impressions\": <int>, \"link_clicks\": <int>, \"active_days\": <int>, \"ads\": [{\"name\": \"<exact name>\", \"spend\": <float>, \"impressions\": <int>, \"link_clicks\": <int>}, ...]}

Als data niet beschikbaar is, gebruik 0 en een lege 'ads' array.

${NO_GOOGLE_RULE}"

PURCHASE_RAW=$(run_claude "sanity + link metrics + per-ad" "$PURCHASE_PROMPT") || PURCHASE_RAW=""

# Schrijf raw output naar een data file, extract vervolgens een geldig JSON
# object via python (handelt nested braces correct af, in tegenstelling tot
# grep dat de 'ads' array niet kan matchen).
PURCHASE_DATA_FILE="${LOG_DIR}/morning-report-${TODAY_ISO}.data.json"
printf '%s' "$PURCHASE_RAW" | /usr/bin/python3 -c '
import json, re, sys

text = sys.stdin.read()
best = ""
for m in re.finditer(r"\{", text):
    start = m.start()
    depth = 0
    for i in range(start, len(text)):
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                cand = text[start:i+1]
                if "purchase_value" in cand:
                    try:
                        json.loads(cand)
                        if len(cand) > len(best):
                            best = cand
                    except Exception:
                        pass
                break
sys.stdout.write(best)
' > "$PURCHASE_DATA_FILE" 2>> "$LOG_FILE"

PURCHASE_DATA_BYTES=$(wc -c < "$PURCHASE_DATA_FILE" | tr -d ' ')
echo "[4/6] extracted JSON: ${PURCHASE_DATA_BYTES} bytes in ${PURCHASE_DATA_FILE}" >> "$LOG_FILE" 2>&1

SANITY_VERDICT=$(/usr/bin/python3 -c '
import json, sys
from pathlib import Path

path = Path(sys.argv[1])
raw = path.read_text(encoding="utf-8").strip() if path.exists() else ""

def fail(status):
    print(f"{status}|0.00|0|0.00|0.00|0|0|0.00|0.00|0|0.00")
    sys.exit(0)

if not raw:
    fail("NODATA")

try:
    d = json.loads(raw)
    pv = float(d.get("purchase_value", 0) or 0)
    pc = int(float(d.get("purchase_count", 0) or 0))
    spend = float(d.get("spend", 0) or 0)
    impressions = int(float(d.get("impressions", 0) or 0))
    link_clicks = int(float(d.get("link_clicks", 0) or 0))
    active_days = int(float(d.get("active_days", 0) or 0))
except Exception:
    fail("PARSE_ERROR")

# Link metrics — onafhankelijk van de purchase sanity check
link_ctr = (link_clicks / impressions * 100) if impressions > 0 else 0.0
link_cpc = (spend / link_clicks) if link_clicks > 0 else 0.0

# Daily spend over ACTIEVE dagen (spend > 0). Vermijd de naieve spend/30
# berekening die de sub-claude soms rapporteert (leidt tot ~1/3 van de
# werkelijke dagspend bij campagnes die slechts deels van de periode actief
# zijn).
avg_daily_spend = (spend / active_days) if active_days > 0 else 0.0

# Purchase sanity verdict
if pc <= 0:
    sanity = "NO_PURCHASES"
    per = 0.0
else:
    per = pv / pc
    # Geldige per-purchase ranges: N tickets * [315, 468] (10% marge rond
    # EUR 350-425). Max N=5 (realistisch max voor groepsboeking).
    # BUG FIX 2026-04-16: N=20 + 15% marge creëerde een aaneengesloten band
    # van EUR 891-9760 waardoor EUR 7374/purchase (n=16) doorglipte.
    valid = any(315 * n <= per <= 468 * n for n in range(1, 6))
    sanity = "PASS" if valid else "FAIL"

print(f"{sanity}|{pv:.2f}|{pc}|{per:.2f}|{spend:.2f}|{impressions}|{link_clicks}|{link_ctr:.2f}|{link_cpc:.2f}|{active_days}|{avg_daily_spend:.2f}")
' "$PURCHASE_DATA_FILE")

SANITY_STATUS=$(echo "$SANITY_VERDICT" | cut -d'|' -f1)
SANITY_PV=$(echo "$SANITY_VERDICT" | cut -d'|' -f2)
SANITY_PC=$(echo "$SANITY_VERDICT" | cut -d'|' -f3)
SANITY_PER=$(echo "$SANITY_VERDICT" | cut -d'|' -f4)
SANITY_SPEND=$(echo "$SANITY_VERDICT" | cut -d'|' -f5)
SANITY_IMP=$(echo "$SANITY_VERDICT" | cut -d'|' -f6)
SANITY_LC=$(echo "$SANITY_VERDICT" | cut -d'|' -f7)
SANITY_LCTR=$(echo "$SANITY_VERDICT" | cut -d'|' -f8)
SANITY_LCPC=$(echo "$SANITY_VERDICT" | cut -d'|' -f9)
SANITY_ADAYS=$(echo "$SANITY_VERDICT" | cut -d'|' -f10)
SANITY_AVG=$(echo "$SANITY_VERDICT" | cut -d'|' -f11)
echo "[4/6] verdict: ${SANITY_VERDICT}" >> "$LOG_FILE" 2>&1

# Mode bepaling — de rewrite helper wordt ALTIJD aangeroepen zodat link
# metrics altijd overschreven worden, maar de mode bepaalt of er ook een
# sanity warning block wordt geplakt.
#   "datafout"   = purchase_value/count past niet bij ticketprijs
#   "unverified" = JSON fetch mislukt/niet parseerbaar (geen link data)
#   "linkfix"    = purchase data OK of geen purchases, alleen link rewrite
REWRITE_MODE="linkfix"
case "$SANITY_STATUS" in
    FAIL)
        REWRITE_MODE="datafout"
        echo "[4/6] 🚨 PIXEL DATAFOUT — EUR ${SANITY_PER}/purchase bij ${SANITY_PC} purchases" >> "$LOG_FILE" 2>&1
        ;;
    NODATA|PARSE_ERROR)
        REWRITE_MODE="unverified"
        echo "[4/6] ⚠️ purchase data niet verifieerbaar (${SANITY_STATUS}) — fail-closed, ROAS wordt gemaskeerd" >> "$LOG_FILE" 2>&1
        ;;
    PASS)
        echo "[4/6] ✅ purchase sanity OK (EUR ${SANITY_PER}/purchase)" >> "$LOG_FILE" 2>&1
        ;;
    NO_PURCHASES)
        echo "[4/6] ✅ geen purchases in periode — niets te verifiëren" >> "$LOG_FILE" 2>&1
        ;;
esac
echo "[4/6] link metrics: Link CTR ${SANITY_LCTR}% · CPC (link) EUR ${SANITY_LCPC} (spend=${SANITY_SPEND} imp=${SANITY_IMP} lc=${SANITY_LC})" >> "$LOG_FILE" 2>&1
echo "[4/6] daily spend: EUR ${SANITY_AVG} over ${SANITY_ADAYS} actieve dagen (van 30)" >> "$LOG_FILE" 2>&1

# --- Stap 5/6: Wix eCommerce orders via Wix MCP ---
echo "[5/6] Wix orders ophalen via MCP (${THIRTY_DAYS_AGO} t/m ${TODAY_ISO})..." >> "$LOG_FILE" 2>&1
WIX_ORDERS_PROMPT="Haal alle betaalde eCommerce orders op voor de Wix site 'Start Your Balloon Business' (site ID: ${WIX_SITE_ID}).

Gebruik de Wix MCP tool CallWixSiteAPI met deze parameters:
- siteId: ${WIX_SITE_ID}
- url: https://www.wixapis.com/ecom/v1/orders/search
- method: POST
- body: {\"search\": {\"filter\": {\"paymentStatus\": \"PAID\"}, \"sort\": [{\"fieldName\": \"createdDate\", \"order\": \"DESC\"}], \"cursorPaging\": {\"limit\": 50}}}

Output UITSLUITEND de ruwe JSON response van de API call. Geen prose, geen markdown, geen code fences, geen uitleg. Alleen de JSON die de API retourneert.

${NO_GOOGLE_RULE}"

WIX_ORDERS_RAW=$(run_claude "Wix orders fetch" "$WIX_ORDERS_PROMPT") || WIX_ORDERS_RAW=""

# Parse Wix response naar gestandaardiseerd formaat
if [ -n "$WIX_ORDERS_RAW" ]; then
    printf '%s' "$WIX_ORDERS_RAW" | /usr/bin/python3 -c '
import json, re, sys

text = sys.stdin.read()
best = ""
for m in re.finditer(r"\{", text):
    start = m.start()
    depth = 0
    for i in range(start, len(text)):
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                cand = text[start:i+1]
                if "orders" in cand and "lineItems" in cand:
                    try:
                        json.loads(cand)
                        if len(cand) > len(best):
                            best = cand
                    except Exception:
                        pass
                break
sys.stdout.write(best)
' | /usr/bin/python3 "$FETCH_WIX_SCRIPT" "$WIX_ORDERS_FILE" "$THIRTY_DAYS_AGO" "$TODAY_ISO" "$WIX_ORDERS_FALLBACK" 2>> "$LOG_FILE"

    WIX_ORDER_COUNT=$(/usr/bin/python3 -c '
import json, sys
from pathlib import Path
path = Path(sys.argv[1])
if not path.exists(): print(0); sys.exit(0)
try:
    d = json.loads(path.read_text())
    print(len(d.get("orders", [])))
except: print(0)
' "$WIX_ORDERS_FILE")
    echo "[5/6] Wix MCP: ${WIX_ORDER_COUNT} betaalde orders opgehaald" >> "$LOG_FILE" 2>&1
else
    echo "[5/6] Wix MCP fetch mislukt, fallback naar ${WIX_ORDERS_FALLBACK}" >> "$LOG_FILE" 2>&1
    if [ -f "$WIX_ORDERS_FALLBACK" ]; then
        cp "$WIX_ORDERS_FALLBACK" "$WIX_ORDERS_FILE" 2>> "$LOG_FILE"
        echo "[5/6] fallback: handmatige wix-orders.json gekopieerd" >> "$LOG_FILE" 2>&1
    else
        echo "[5/6] geen fallback beschikbaar — verified funnel draait zonder Wix data" >> "$LOG_FILE" 2>&1
        echo '{"orders":[],"source":"fallback_empty"}' > "$WIX_ORDERS_FILE"
    fi
fi

# --- Stap 6/6: PostHog /thank-you-page sessies met UTM data ---
echo "[6/6] PostHog /thank-you sessies ophalen (${THIRTY_DAYS_AGO} t/m ${TODAY_ISO})..." >> "$LOG_FILE" 2>&1
POSTHOG_TY_PROMPT="Voer de volgende HogQL query uit via de PostHog MCP (query-run met DataVisualizationNode + HogQLQuery) voor het project 'Default project' op startyourballoonbusiness.com.

Query:
SELECT
  toDate(timestamp) AS visit_date,
  toString(timestamp) AS visit_time,
  e.\$session_id AS session_id,
  properties.utm_content AS utm_content,
  properties.utm_source AS utm_source,
  properties.\$geoip_country_name AS country,
  properties.\$device_type AS device
FROM events e
WHERE event = '\$pageview'
  AND properties.\$current_url LIKE '%/thank-you%'
  AND timestamp >= toDateTime('${THIRTY_DAYS_AGO} 00:00:00')
  AND timestamp < toDateTime('${TODAY_ISO} 00:00:00')
ORDER BY timestamp DESC

Date range: date_from='${THIRTY_DAYS_AGO}', date_to='${TODAY_ISO}'.

Als utm_content leeg is in het resultaat, doe een TWEEDE query per sessie om de utm_content op te halen van de eerste pageview in die sessie (de landing page met UTM parameters).

Output UITSLUITEND valide JSON, geen prose, geen markdown, geen code fences. Formaat:
{\"thank_you_sessions\": [{\"visit_date\": \"YYYY-MM-DD\", \"visit_time\": \"HH:MM:SS\", \"session_id\": \"...\", \"utm_content\": \"h11_b3_cta5\", \"utm_source\": \"meta\", \"country\": \"...\", \"device\": \"...\"}]}

Als er geen resultaten zijn, output: {\"thank_you_sessions\": []}

${NO_GOOGLE_RULE}"

POSTHOG_TY_RAW=$(run_claude "PostHog /thank-you sessions" "$POSTHOG_TY_PROMPT") || POSTHOG_TY_RAW=""

# Extract JSON
printf '%s' "$POSTHOG_TY_RAW" | /usr/bin/python3 -c '
import json, re, sys

text = sys.stdin.read()
best = ""
for m in re.finditer(r"\{", text):
    start = m.start()
    depth = 0
    for i in range(start, len(text)):
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                cand = text[start:i+1]
                if "thank_you_sessions" in cand:
                    try:
                        json.loads(cand)
                        if len(cand) > len(best):
                            best = cand
                    except Exception:
                        pass
                break
sys.stdout.write(best)
' > "$POSTHOG_SESSIONS_FILE" 2>> "$LOG_FILE"

POSTHOG_SESSIONS_BYTES=$(wc -c < "$POSTHOG_SESSIONS_FILE" | tr -d ' ')
echo "[6/6] extracted JSON: ${POSTHOG_SESSIONS_BYTES} bytes in ${POSTHOG_SESSIONS_FILE}" >> "$LOG_FILE" 2>&1

# Tel /thank-you sessies
TY_COUNT=$(/usr/bin/python3 -c '
import json, sys
from pathlib import Path
path = Path(sys.argv[1])
if not path.exists():
    print(0); sys.exit(0)
raw = path.read_text().strip()
if not raw:
    print(0); sys.exit(0)
try:
    d = json.loads(raw)
    print(len(d.get("thank_you_sessions", [])))
except Exception:
    print(0)
' "$POSTHOG_SESSIONS_FILE")
echo "[6/6] /thank-you sessies gevonden: ${TY_COUNT}" >> "$LOG_FILE" 2>&1

# --- Combineer alle deelrapporten naar 1 markdown bestand ---
{
    echo "# Morning Report — ${TODAY_ISO}"
    echo
    echo "Bronnen: Meta Ads MCP + PostHog MCP. Geen Google integraties."
    echo "Failures: ${FAILURES}"
    echo
    echo "---"
    echo
    echo "$REPORT"
    echo
    echo "---"
    echo
    echo "$SYBB_REPORT"
    echo
    echo "---"
    echo
    echo "$OPTIMIZE"
    echo
    echo "---"
    echo
    echo "Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar."
} > "$FULL_REPORT_FILE" 2>> "$LOG_FILE"

echo "[done] Gecombineerd rapport opgeslagen in $FULL_REPORT_FILE" >> "$LOG_FILE" 2>&1

# --- Rewrite: sanity warnings + link metrics ---
# Draait ALTIJD (REWRITE_MODE is minimaal "linkfix"), vóór push en
# iMessage. Helper doet twee dingen:
#   1. Link metric rewrite: vervangt kale "CTR"/"CPC" in campagne-summary
#      tabellen door de hardcoded link_ctr / link_cpc waarden en plakt een
#      "LINK METRICS" block bovenaan. Dit gebeurt altijd als we link data
#      hebben (mode != unverified en link_clicks > 0).
#   2. Sanity warning: alleen bij datafout (hard mismatch) of unverified
#      (fetch faalde) — plakt PIXEL DATAFOUT / NIET GEVERIFIEERD block +
#      maskeert ROAS en purchase prose.
/usr/bin/python3 "${WORKDIR}/scripts/pixel-datafout-rewrite.py" \
    "$REWRITE_MODE" \
    "$FULL_REPORT_FILE" \
    "$SANITY_PV" \
    "$SANITY_PC" \
    "$SANITY_PER" \
    "$SANITY_SPEND" \
    "$SANITY_IMP" \
    "$SANITY_LC" \
    "$SANITY_LCTR" \
    "$SANITY_LCPC" \
    "$SANITY_ADAYS" \
    "$SANITY_AVG" \
    "$PURCHASE_DATA_FILE" \
    >> "$LOG_FILE" 2>&1 || \
    echo "[pixel-rewrite] helper faalde — rapport blijft ongewijzigd" >> "$LOG_FILE" 2>&1

# --- Verified Funnel: cross-reference Meta + PostHog + Wix ---
echo "[verified-funnel] Cross-referencing Meta Ads + PostHog sessions + Wix orders..." >> "$LOG_FILE" 2>&1
/usr/bin/python3 "$VERIFIED_FUNNEL_SCRIPT" \
    "$FULL_REPORT_FILE" \
    "$PURCHASE_DATA_FILE" \
    "$POSTHOG_SESSIONS_FILE" \
    "$WIX_ORDERS_FILE" \
    "$THIRTY_DAYS_AGO" \
    "$TODAY_ISO" \
    >> "$LOG_FILE" 2>&1 || \
    echo "[verified-funnel] helper faalde — sectie niet toegevoegd" >> "$LOG_FILE" 2>&1

# --- Push naar GitHub zodat de iMessage link direct werkt ---
echo "[push] Commit + push reports naar main..." >> "$LOG_FILE" 2>&1
cd "$WORKDIR"
git add \
    "Output/Reports/Daily/${TODAY_ISO}_ads_report.md" \
    "Output/Reports/Daily/${TODAY_ISO}_auto_optimize.md" \
    "Output/Reports/Daily/${TODAY_ISO}_morning_report_full.md" \
    "Output/Reports/Daily/${YESTERDAY_ISO}_sybb_report.md" \
    2>> "$LOG_FILE" || true

if ! git diff --cached --quiet 2>/dev/null; then
    git commit -m "Morning report: ${TODAY_ISO}" >> "$LOG_FILE" 2>&1 || true
    if ! git push origin main >> "$LOG_FILE" 2>&1; then
        # De auto-sync cron en andere processen pushen tussendoor. Daarnaast
        # heeft de working tree vrijwel altijd onstaged changes (logs/git-sync.log,
        # de remotion-stx submodule pointer). --autostash verbergt die tijdelijk
        # tijdens de rebase en zet ze daarna terug, zodat rebase niet klaagt.
        echo "[push] eerste push failed, retry met rebase --autostash..." >> "$LOG_FILE" 2>&1
        if git pull --rebase --autostash -X theirs origin main >> "$LOG_FILE" 2>&1; then
            git push origin main >> "$LOG_FILE" 2>&1 || echo "[push] FAILED — link in iMessage werkt mogelijk pas na de volgende auto-sync run" >> "$LOG_FILE" 2>&1
        else
            echo "[push] rebase faalde, aborting" >> "$LOG_FILE" 2>&1
            git rebase --abort >> "$LOG_FILE" 2>&1 || true
            echo "[push] FAILED — link in iMessage werkt mogelijk pas na de volgende auto-sync run" >> "$LOG_FILE" 2>&1
        fi
    fi
else
    echo "[push] geen nieuwe report files om te committen" >> "$LOG_FILE" 2>&1
fi

# --- iMessage notificatie naar Robin ---
# Cache-bust query op de dashboard URL zodat Safari/iMessage altijd de verse versie ophaalt
CACHE_BUST=$(date +%s)
DASHBOARD_LINK="${DASHBOARD_URL}?v=${CACHE_BUST}"
SYBB_REPORT_URL="${GITHUB_BLOB_BASE}/${YESTERDAY_ISO}_sybb_report.md"
ADS_REPORT_URL="${GITHUB_BLOB_BASE}/${TODAY_ISO}_ads_report.md"
OPTIMIZE_URL="${GITHUB_BLOB_BASE}/${TODAY_ISO}_auto_optimize.md"

if [ $FAILURES -eq 0 ]; then
    STATUS_LINE="✅ Alles compleet"
else
    STATUS_LINE="⚠️ ${FAILURES} sectie(s) incompleet"
fi

# Dump de volledige rapport-inhoud in de iMessage (Robin update het HTML
# dashboard zelf op basis hiervan). Markdown table-separator rijen ("|---|---|")
# worden eruit gefilterd want die zijn onleesbaar op een telefoonscherm;
# normale tabelrijen blijven staan. De rewrite-stap heeft hierboven al
# eventuele pixel-datafout warning in FULL_REPORT_FILE geplakt, dus die
# reist automatisch mee in REPORT_BODY.
REPORT_BODY=$(sed -E '/^[[:space:]]*\|[-: |]+\|[[:space:]]*$/d' "$FULL_REPORT_FILE" 2>/dev/null)

if [ -z "$REPORT_BODY" ]; then
    REPORT_BODY="(Rapport-inhoud niet beschikbaar — zie log ${LOG_FILE})"
fi

# Explicit warning prefix bovenaan de iMessage, zodat je belangrijke info
# ziet voordat je hoeft te scrollen (naast het warning blok dat via
# REPORT_BODY meekomt).
PIXEL_PREFIX=""
case "$REWRITE_MODE" in
    datafout)
        PIXEL_PREFIX="🚨 PIXEL DATAFOUT — EUR ${SANITY_PER}/purchase bij ${SANITY_PC} purchases past niet bij ticketprijs EUR 350-425. Purchase aantal en ROAS zijn NIET betrouwbaar. Verifieer in Wix.
✅ Link CTR: ${SANITY_LCTR}% · CPC (link): EUR ${SANITY_LCPC}
━━━━━━━━━━━━━━━━━━━━━
"
        ;;
    unverified)
        PIXEL_PREFIX="⚠️ PURCHASE DATA NIET GEVERIFIEERD — sanity check kon geen purchase data ophalen. ROAS gemaskeerd. Link metrics ook niet beschikbaar. Behandel alles als onbetrouwbaar. Verifieer in Wix.
━━━━━━━━━━━━━━━━━━━━━
"
        ;;
    linkfix)
        PIXEL_PREFIX="✅ Link CTR: ${SANITY_LCTR}% · CPC (link): EUR ${SANITY_LCPC} (hardcoded via Meta Ads MCP)
━━━━━━━━━━━━━━━━━━━━━
"
        ;;
esac

IMESSAGE_BODY="${PIXEL_PREFIX}📊 Morning Report ${TODAY_ISO}
${STATUS_LINE} — Bronnen: Meta Ads + PostHog

${REPORT_BODY}

━━━━━━━━━━━━━━━━━━━━━
📈 Dashboard: ${DASHBOARD_LINK}
📄 Ads rapport: ${ADS_REPORT_URL}
📄 SYBB ${YESTERDAY_ISO}: ${SYBB_REPORT_URL}
🔧 Auto-optimize: ${OPTIMIZE_URL}"

if [ -x "$IMESSAGE_HELPER" ]; then
    if /usr/bin/python3 "$IMESSAGE_HELPER" "$IMESSAGE_RECIPIENT" "$IMESSAGE_BODY" >> "$LOG_FILE" 2>&1; then
        echo "[imessage] verstuurd naar ${IMESSAGE_RECIPIENT}" >> "$LOG_FILE" 2>&1
    else
        echo "[imessage] FAILED — check Messages.app permissions of of de helper draait" >> "$LOG_FILE" 2>&1
    fi
else
    echo "[imessage] helper niet gevonden of niet executable: $IMESSAGE_HELPER" >> "$LOG_FILE" 2>&1
fi

echo "=== Morning Report afgerond: $(date) — ${FAILURES} failures ===" >> "$LOG_FILE" 2>&1

# Markeer vandaag als klaar zodat launchd's StartInterval (elke paar minuten)
# het script vandaag niet opnieuw triggert. De marker bevat timestamp + failures
# voor debugging. Verwijder het bestand om handmatig een re-run te forceren.
echo "done=$(date +%s) failures=${FAILURES}" > "$DONE_MARKER"

# Cleanup: verwijder logs + markers ouder dan 30 dagen
find "$LOG_DIR" -name "morning-report-*.log" -mtime +30 -delete 2>/dev/null || true
find "$LOG_DIR" -name "morning-report-*.done" -mtime +30 -delete 2>/dev/null || true
