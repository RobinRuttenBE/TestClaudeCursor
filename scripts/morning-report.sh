#!/bin/bash
# morning-report.sh — Dagelijks Meta Ads rapport + auto-optimize via Claude Code + Gmail
# Draait via launchd elke ochtend om 08:00
# Flow: /ads-report → SYBB daily report → /ads-auto-optimize → email met alle rapporten

set -uo pipefail

# Paden
CLAUDE="/Users/robinrutten/.local/bin/claude"
PYTHON="/usr/bin/python3"
WORKDIR="/Users/robinrutten/TestClaudeCursor"
SEND_SCRIPT="${WORKDIR}/scripts/send-gmail.py"
LOG_DIR="${WORKDIR}/logs"
LOG_FILE="${LOG_DIR}/morning-report-$(date +%Y-%m-%d).log"
RECIPIENT="robin.rutten2@gmail.com"
TODAY=$(date +"%d-%m-%Y")
TODAY_ISO=$(date +"%Y-%m-%d")
REPORT_DIR="${WORKDIR}/output/reports/daily"
ADS_REPORT_FILE="${REPORT_DIR}/${TODAY_ISO}_ads_report.md"
OPTIMIZE_REPORT_FILE="${REPORT_DIR}/${TODAY_ISO}_auto_optimize.md"
FULL_REPORT_FILE="${REPORT_DIR}/${TODAY_ISO}_morning_report_full.md"
FAILURES=0

# Zorg dat log + report directories bestaan
mkdir -p "$LOG_DIR"
mkdir -p "$REPORT_DIR"
cd "$WORKDIR"

echo "=== Morning Report gestart: $(date) ===" >> "$LOG_FILE" 2>&1

# Helper: draai een Claude command met retry
run_claude() {
    local label="$1"
    local prompt="$2"
    local max_attempts=2
    local attempt=1
    local result=""

    while [ $attempt -le $max_attempts ]; do
        echo "  [poging ${attempt}/${max_attempts}] ${label}..." >> "$LOG_FILE" 2>&1
        result=$("$CLAUDE" -p "$prompt" \
            --output-format text \
            --max-turns 30 \
            --dangerously-skip-permissions \
            2>> "$LOG_FILE") && break
        echo "  [poging ${attempt}] mislukt" >> "$LOG_FILE" 2>&1
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

# --- Stap 1/4: /ads-report ---
echo "[1/4] /ads-report uitvoeren..." >> "$LOG_FILE" 2>&1
REPORT=$(run_claude "/ads-report" "/ads-report") || \
    REPORT="Ads rapport niet beschikbaar. Campagnes staan momenteel op pauze."

# Persist deelrapport naar disk vóór de email — als de mail faalt is dit nog terug te vinden
printf '%s\n' "$REPORT" > "$ADS_REPORT_FILE" 2>> "$LOG_FILE"

echo "[1/4] klaar ($(echo "$REPORT" | wc -c | tr -d ' ') bytes, opgeslagen in $ADS_REPORT_FILE)" >> "$LOG_FILE" 2>&1

# --- Stap 2/4: SYBB Daily Report ---
echo "[2/4] SYBB daily report uitvoeren..." >> "$LOG_FILE" 2>&1
SYBB_PROMPT="Genereer het dagelijkse SYBB rapport voor gisteren. Haal Meta Ads data op voor campagne \"2026: SYBB\" via de Meta Ads MCP. Haal PostHog data op voor startyourballoonbusiness.com via de PostHog MCP. Combineer beide databronnen en volg de rapportstructuur uit skills/daily-sybb-report/SKILL.md. Sla het rapport op in output/reports/daily/$(date -v-1d +%Y-%m-%d)_sybb_report.md."

SYBB_REPORT=$(run_claude "SYBB daily report" "$SYBB_PROMPT") || \
    SYBB_REPORT="SYBB rapport niet beschikbaar."

echo "[2/4] klaar ($(echo "$SYBB_REPORT" | wc -c | tr -d ' ') bytes)" >> "$LOG_FILE" 2>&1

# --- Stap 3/4: /ads-auto-optimize ---
echo "[3/4] /ads-auto-optimize uitvoeren..." >> "$LOG_FILE" 2>&1
OPTIMIZE=$(run_claude "/ads-auto-optimize" "/ads-auto-optimize") || \
    OPTIMIZE="Auto-optimize niet beschikbaar. Geen actieve campagnes."

# Persist deelrapport naar disk vóór de email — als de mail faalt is dit nog terug te vinden
printf '%s\n' "$OPTIMIZE" > "$OPTIMIZE_REPORT_FILE" 2>> "$LOG_FILE"

echo "[3/4] klaar ($(echo "$OPTIMIZE" | wc -c | tr -d ' ') bytes, opgeslagen in $OPTIMIZE_REPORT_FILE)" >> "$LOG_FILE" 2>&1

# --- Stap 4/4: Combineer en verstuur ---
echo "[4/4] Email versturen..." >> "$LOG_FILE" 2>&1

# Bouw subject op basis van failures
if [ $FAILURES -eq 0 ]; then
    SUBJECT="Dagelijks Meta Ads + SYBB Rapport — ${TODAY}"
else
    SUBJECT="Dagelijks Rapport (${FAILURES} sectie(s) incompleet) — ${TODAY}"
fi

FULL_REPORT="${REPORT}

---

${SYBB_REPORT}

---

${OPTIMIZE}

---

Dit rapport is automatisch gegenereerd door Claude Code.
Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar."

# Persist gecombineerd rapport naar disk vóór de email — fail-safe voor mail problemen
printf '%s\n' "$FULL_REPORT" > "$FULL_REPORT_FILE" 2>> "$LOG_FILE"
echo "[4/4] gecombineerd rapport opgeslagen in $FULL_REPORT_FILE" >> "$LOG_FILE" 2>&1

"$PYTHON" "$SEND_SCRIPT" \
    "$RECIPIENT" \
    "$SUBJECT" \
    "$FULL_REPORT" \
    >> "$LOG_FILE" 2>&1
MAIL_EXIT=$?

if [ $MAIL_EXIT -ne 0 ]; then
    echo "[4/4] EMAIL FAILED (exit $MAIL_EXIT). Rapport blijft beschikbaar in $FULL_REPORT_FILE — re-send handmatig of fix OAuth token." >> "$LOG_FILE" 2>&1
fi

echo "=== Morning Report afgerond: $(date) — ${FAILURES} failures ===" >> "$LOG_FILE" 2>&1

# Cleanup: verwijder logs ouder dan 30 dagen
find "$LOG_DIR" -name "morning-report-*.log" -mtime +30 -delete 2>/dev/null || true
