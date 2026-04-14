#!/usr/bin/env python3
"""Send an iMessage via Messages.app using osascript.

Usage:
    send-imessage.py <recipient> <body>

Where <recipient> is a phone number (E.164 like +32468236146) or Apple ID
email, and <body> can contain newlines.

Exits 0 on success, non-zero on failure. Writes errors to stderr.
"""

import subprocess
import sys


def send_imessage(recipient: str, body: str) -> None:
    # Escape body for AppleScript: backslashes, double quotes, newlines.
    escaped = (
        body.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("\n", '" & return & "')
    )

    script = (
        'tell application "Messages"\n'
        '\tset targetService to 1st service whose service type = iMessage\n'
        f'\tset targetBuddy to buddy "{recipient}" of targetService\n'
        f'\tsend "{escaped}" to targetBuddy\n'
        'end tell'
    )

    result = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        sys.stderr.write(
            f"send-imessage: osascript failed (exit {result.returncode})\n"
            f"stderr: {result.stderr}\n"
        )
        sys.exit(result.returncode)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("usage: send-imessage.py <recipient> <body>\n")
        sys.exit(2)
    send_imessage(sys.argv[1], sys.argv[2])
