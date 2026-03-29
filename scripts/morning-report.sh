#!/bin/bash
# morning-report.sh — Dagelijks Meta Ads rapport + auto-optimize via Claude Code + Gmail
# Draait via launchd elke ochtend om 08:00
# Flow: /ads-report → /ads-auto-optimize → email met beide rapporten

set -euo pipefail

# Paden
CLAUDE="/Users/robinrutten/.local/bin/claude"
PYTHON="/usr/bin/python3"
WORKDIR="/Users/robinrutten/TestClaudeCursor"
SEND_SCRIPT="${WORKDIR}/scripts/send-gmail.py"
LOG_DIR="${WORKDIR}/logs"
LOG_FILE="${LOG_DIR}/morning-report-$(date +%Y-%m-%d).log"
RECIPIENT="robin.rutten2@gmail.com"
TODAY=$(date +"%d-%m-%Y")

# Zorg dat log directory bestaat
mkdir -p "$LOG_DIR"
cd "$WORKDIR"

echo "=== Morning Report gestart: $(date) ===" >> "$LOG_FILE" 2>&1

# --- Stap 1: /ads-report ---
echo "[1/5] Claude Code /ads-report uitvoeren..." >> "$LOG_FILE" 2>&1

REPORT=$("$CLAUDE" -p "/ads-report" \
    --output-format text \
    --max-turns 30 \
    --dangerously-skip-permissions \
    2>> "$LOG_FILE") || {
    ERROR_MSG="Claude Code /ads-report is mislukt op ${TODAY}. Check logs: ${LOG_FILE}"
    "$PYTHON" "$SEND_SCRIPT" "$RECIPIENT" "⚠️ Morning Report FAILED — ${TODAY}" "$ERROR_MSG"
    echo "[ERROR] /ads-report failed" >> "$LOG_FILE" 2>&1
    exit 1
}

echo "[2/7] Ads report ontvangen ($(echo "$REPORT" | wc -c | tr -d ' ') bytes)" >> "$LOG_FILE" 2>&1

# --- Stap 2: SYBB Daily Report ---
echo "[3/7] Claude Code SYBB daily report uitvoeren..." >> "$LOG_FILE" 2>&1

SYBB_PROMPT="Genereer het dagelijkse SYBB rapport voor gisteren. Haal Meta Ads data op voor campagne \"2026: SYBB\" via de Meta Ads MCP. Haal PostHog data op voor startyourballoonbusiness.com via de PostHog MCP. Combineer beide databronnen en volg de rapportstructuur uit skills/daily-sybb-report/SKILL.md. Sla het rapport op in output/reports/daily/$(date -v-1d +%Y-%m-%d)_sybb_report.md."

SYBB_REPORT=$("$CLAUDE" -p "$SYBB_PROMPT" \
    --output-format text \
    --max-turns 30 \
    --dangerously-skip-permissions \
    2>> "$LOG_FILE") || {
    SYBB_REPORT="⚠️ SYBB Daily Report kon niet worden gegenereerd. Check logs: ${LOG_FILE}"
    echo "[WARN] SYBB daily report failed, continuing" >> "$LOG_FILE" 2>&1
}

echo "[4/7] SYBB report ontvangen ($(echo "$SYBB_REPORT" | wc -c | tr -d ' ') bytes)" >> "$LOG_FILE" 2>&1

# --- Stap 3: /ads-auto-optimize ---
echo "[5/7] Claude Code /ads-auto-optimize uitvoeren..." >> "$LOG_FILE" 2>&1

OPTIMIZE=$("$CLAUDE" -p "/ads-auto-optimize" \
    --output-format text \
    --max-turns 30 \
    --dangerously-skip-permissions \
    2>> "$LOG_FILE") || {
    # Auto-optimize is niet kritiek — stuur het rapport zonder optimize
    OPTIMIZE="⚠️ Auto-optimize kon niet worden uitgevoerd. Check logs: ${LOG_FILE}"
    echo "[WARN] /ads-auto-optimize failed, continuing with report only" >> "$LOG_FILE" 2>&1
}

echo "[6/7] Auto-optimize ontvangen ($(echo "$OPTIMIZE" | wc -c | tr -d ' ') bytes)" >> "$LOG_FILE" 2>&1

# --- Stap 4: Combineer en verstuur ---
echo "[7/7] Email versturen..." >> "$LOG_FILE" 2>&1

FULL_REPORT="${REPORT}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

${SYBB_REPORT}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

${OPTIMIZE}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dit rapport is automatisch gegenereerd door Claude Code.
Voorstellen uit auto-optimize vereisen je goedkeuring — open Claude Code en bevestig daar."

"$PYTHON" "$SEND_SCRIPT" \
    "$RECIPIENT" \
    "📊 Dagelijks Meta Ads + SYBB Rapport — ${TODAY}" \
    "$FULL_REPORT" \
    >> "$LOG_FILE" 2>&1

echo "=== Morning Report afgerond: $(date) ===" >> "$LOG_FILE" 2>&1

# Cleanup: verwijder logs ouder dan 30 dagen
find "$LOG_DIR" -name "morning-report-*.log" -mtime +30 -delete 2>/dev/null || true
