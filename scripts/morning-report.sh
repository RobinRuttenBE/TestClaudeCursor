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
# (zoals op 2026-04-14, waar /ads-report 1.5 uur bleef plakken) de hele chain
# blokkeert en iMessage nooit wordt verstuurd.
CLAUDE_STEP_TIMEOUT_SEC=600

# Paden
CLAUDE="/Users/robinrutten/.local/bin/claude"
WORKDIR="/Users/robinrutten/TestClaudeCursor"
LOG_DIR="${WORKDIR}/logs"
LOG_FILE="${LOG_DIR}/morning-report-$(date +%Y-%m-%d).log"
TODAY_ISO=$(date +"%Y-%m-%d")
YESTERDAY_ISO=$(date -v-1d +"%Y-%m-%d")

# Casing van REPORT_DIR matcht git's canonical pad (zie `git ls-files Output/Reports/Daily/`)
REPORT_DIR="${WORKDIR}/Output/Reports/Daily"
ADS_REPORT_FILE="${REPORT_DIR}/${TODAY_ISO}_ads_report.md"
SYBB_REPORT_FILE="${REPORT_DIR}/${YESTERDAY_ISO}_sybb_report.md"
OPTIMIZE_REPORT_FILE="${REPORT_DIR}/${TODAY_ISO}_auto_optimize.md"
FULL_REPORT_FILE="${REPORT_DIR}/${TODAY_ISO}_morning_report_full.md"

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
        # perl alarm+exec: harde wall-clock timeout. Bij SIGALRM wordt het
        # claude subprocess met default-dispositie getermineerd.
        result=$(/usr/bin/perl -e 'alarm shift; exec @ARGV or die "exec: $!"' "$CLAUDE_STEP_TIMEOUT_SEC" \
            "$CLAUDE" -p "$prompt" \
            --output-format text \
            --max-turns 30 \
            --dangerously-skip-permissions \
            2>> "$LOG_FILE")
        local rc=$?
        if [ $rc -eq 0 ] && [ -n "$result" ]; then
            break
        fi
        if [ $rc -eq 142 ] || [ $rc -eq 14 ]; then
            echo "  [poging ${attempt}] TIMEOUT na ${CLAUDE_STEP_TIMEOUT_SEC}s" >> "$LOG_FILE" 2>&1
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
echo "[1/3] /ads-report uitvoeren..." >> "$LOG_FILE" 2>&1
ADS_PROMPT="/ads-report

${NO_GOOGLE_RULE}

Aanvullend voor /ads-report: sla stap 6 (Google Sheet write naar Meta Ads Tracker) volledig over. Sla het rapport in plaats daarvan op in ${ADS_REPORT_FILE}."

REPORT=$(run_claude "/ads-report" "$ADS_PROMPT") || \
    REPORT="Ads rapport niet beschikbaar. Campagnes staan momenteel op pauze."

printf '%s\n' "$REPORT" > "$ADS_REPORT_FILE" 2>> "$LOG_FILE"
echo "[1/3] klaar ($(echo "$REPORT" | wc -c | tr -d ' ') bytes, opgeslagen in $ADS_REPORT_FILE)" >> "$LOG_FILE" 2>&1

# --- Stap 2/3: SYBB Daily Report (Meta + PostHog) ---
echo "[2/3] SYBB daily report uitvoeren..." >> "$LOG_FILE" 2>&1
SYBB_PROMPT="Genereer het dagelijkse SYBB rapport voor gisteren. Haal Meta Ads data op voor campagne \"2026: SYBB\" via de Meta Ads MCP. Haal PostHog data op voor startyourballoonbusiness.com via de PostHog MCP. Combineer beide databronnen en volg de rapportstructuur uit skills/daily-sybb-report/SKILL.md. Sla het rapport op in ${SYBB_REPORT_FILE}.

${NO_GOOGLE_RULE}"

SYBB_REPORT=$(run_claude "SYBB daily report" "$SYBB_PROMPT") || \
    SYBB_REPORT="SYBB rapport niet beschikbaar."

echo "[2/3] klaar ($(echo "$SYBB_REPORT" | wc -c | tr -d ' ') bytes, sub-Claude schrijft naar $SYBB_REPORT_FILE)" >> "$LOG_FILE" 2>&1

# --- Stap 3/3: /ads-auto-optimize (Meta only) ---
echo "[3/3] /ads-auto-optimize uitvoeren..." >> "$LOG_FILE" 2>&1
OPTIMIZE_PROMPT="/ads-auto-optimize

${NO_GOOGLE_RULE}

Sla het rapport op in ${OPTIMIZE_REPORT_FILE}."

OPTIMIZE=$(run_claude "/ads-auto-optimize" "$OPTIMIZE_PROMPT") || \
    OPTIMIZE="Auto-optimize niet beschikbaar. Geen actieve campagnes."

printf '%s\n' "$OPTIMIZE" > "$OPTIMIZE_REPORT_FILE" 2>> "$LOG_FILE"
echo "[3/3] klaar ($(echo "$OPTIMIZE" | wc -c | tr -d ' ') bytes, opgeslagen in $OPTIMIZE_REPORT_FILE)" >> "$LOG_FILE" 2>&1

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
        # Auto-sync cron kan tussendoor pushen — pull rebase met theirs voor log conflicts
        echo "[push] eerste push failed, retry met rebase..." >> "$LOG_FILE" 2>&1
        git pull --rebase -X theirs origin main >> "$LOG_FILE" 2>&1 || git rebase --abort >> "$LOG_FILE" 2>&1
        git push origin main >> "$LOG_FILE" 2>&1 || echo "[push] FAILED — link in iMessage werkt mogelijk pas na de volgende auto-sync run" >> "$LOG_FILE" 2>&1
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

IMESSAGE_BODY="📊 Morning Report ${TODAY_ISO}
${STATUS_LINE}
Bronnen: Meta Ads + PostHog

📈 Dashboard (visueel):
${DASHBOARD_LINK}

📄 SYBB ${YESTERDAY_ISO} (details):
${SYBB_REPORT_URL}

📄 Ads rapport:
${ADS_REPORT_URL}

🔧 Auto-optimize voorstellen:
${OPTIMIZE_URL}"

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

# Cleanup: verwijder logs ouder dan 30 dagen
find "$LOG_DIR" -name "morning-report-*.log" -mtime +30 -delete 2>/dev/null || true
