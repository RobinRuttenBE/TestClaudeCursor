#!/bin/bash
# weekly-social-report.sh — Wekelijks Social Media rapport via Claude Code + Gmail
# Draait via launchd elke maandag om 08:00
# Flow: /social-report → /blort-social-analyze prompt → email met rapport + BLORT prompt

set -euo pipefail

# Paden
CLAUDE="/Users/robinrutten/.local/bin/claude"
PYTHON="/usr/bin/python3"
WORKDIR="/Users/robinrutten/TestClaudeCursor"
SEND_SCRIPT="${WORKDIR}/scripts/send-gmail.py"
LOG_DIR="${WORKDIR}/logs"
LOG_FILE="${LOG_DIR}/weekly-social-report-$(date +%Y-%m-%d).log"
RECIPIENT="robin.rutten2@gmail.com"
TODAY=$(date +"%d-%m-%Y")
WEEK_NR=$(date +"%V")

# Zorg dat log directory bestaat
mkdir -p "$LOG_DIR"
cd "$WORKDIR"

echo "=== Weekly Social Report gestart: $(date) ===" >> "$LOG_FILE" 2>&1

# --- Stap 1: /social-report ---
echo "[1/4] Claude Code /social-report uitvoeren..." >> "$LOG_FILE" 2>&1

REPORT=$("$CLAUDE" -p "/social-report" \
    --output-format text \
    --max-turns 30 \
    --dangerously-skip-permissions \
    2>> "$LOG_FILE") || {
    ERROR_MSG="Claude Code /social-report is mislukt op ${TODAY}. Check logs: ${LOG_FILE}"
    "$PYTHON" "$SEND_SCRIPT" "$RECIPIENT" "⚠️ Weekly Social Report FAILED — Week ${WEEK_NR}" "$ERROR_MSG"
    echo "[ERROR] /social-report failed" >> "$LOG_FILE" 2>&1
    exit 1
}

echo "[2/4] Social report ontvangen ($(echo "$REPORT" | wc -c | tr -d ' ') bytes)" >> "$LOG_FILE" 2>&1

# --- Stap 2: /blort-social-analyze ---
echo "[3/4] Claude Code /blort-social-analyze uitvoeren..." >> "$LOG_FILE" 2>&1

BLORT_PROMPT=$("$CLAUDE" -p "/blort-social-analyze" \
    --output-format text \
    --max-turns 30 \
    --dangerously-skip-permissions \
    2>> "$LOG_FILE") || {
    # BLORT prompt is niet kritiek — stuur het rapport zonder
    BLORT_PROMPT="⚠️ BLORT prompt kon niet worden gegenereerd. Draai /blort-social-analyze handmatig."
    echo "[WARN] /blort-social-analyze failed, continuing with report only" >> "$LOG_FILE" 2>&1
}

echo "[4/4] Email versturen..." >> "$LOG_FILE" 2>&1

# --- Stap 3: Combineer en verstuur ---
FULL_REPORT="${REPORT}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BLORT ANALYSE PROMPT
(Plak onderstaande prompt in BLORT om de video's visueel te analyseren)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

${BLORT_PROMPT}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dit rapport is automatisch gegenereerd door Claude Code.
Data is geschreven naar Google Sheet: Social Media Tracker.
Content Learnings zijn bijgewerkt in Google Doc: Content Learnings."

"$PYTHON" "$SEND_SCRIPT" \
    "$RECIPIENT" \
    "📱 Weekly Social Report — Week ${WEEK_NR} — ${TODAY}" \
    "$FULL_REPORT" \
    >> "$LOG_FILE" 2>&1

echo "=== Weekly Social Report afgerond: $(date) ===" >> "$LOG_FILE" 2>&1

# Cleanup: verwijder logs ouder dan 30 dagen
find "$LOG_DIR" -name "weekly-social-report-*.log" -mtime +30 -delete 2>/dev/null || true
