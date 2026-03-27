#!/bin/bash
# Auto git sync - commits and pushes changes if any exist
cd /Users/robinrutten/TestClaudeCursor

# Check if there are changes
if [ -n "$(git status --porcelain)" ]; then
    git add -A
    git commit -m "Auto-sync: $(date '+%Y-%m-%d %H:%M')"
    git push origin main
fi
