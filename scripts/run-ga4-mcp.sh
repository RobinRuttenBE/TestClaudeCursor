#!/bin/bash
export PATH="/opt/homebrew/bin:$PATH"
exec npx -y mcp-remote@0.1.30 https://mcp-ga.stape.ai/mcp "$@"
