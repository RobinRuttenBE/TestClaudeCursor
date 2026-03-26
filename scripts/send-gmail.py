#!/usr/bin/env python3
"""Send an email via Gmail API using google-mcp-server OAuth tokens."""

import sys
import json
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

ACCOUNT_FILE = "/Users/robinrutten/.google-mcp-accounts/robin_rutten2_at_gmail_com.json"
CONFIG_FILE = "/Users/robinrutten/.google-mcp-server/config.json"


def send_email(to: str, subject: str, body: str):
    with open(ACCOUNT_FILE) as f:
        data = json.load(f)
    with open(CONFIG_FILE) as f:
        config = json.load(f)

    creds = Credentials(
        token=data["token"]["access_token"],
        refresh_token=data["token"]["refresh_token"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=config["oauth"]["client_id"],
        client_secret=config["oauth"]["client_secret"],
    )

    service = build("gmail", "v1", credentials=creds)

    message = MIMEText(body, "plain", "utf-8")
    message["to"] = to
    message["subject"] = subject

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    result = service.users().messages().send(userId="me", body={"raw": raw}).execute()
    print(f"Email verstuurd! Message ID: {result['id']}")
    return result


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: send-gmail.py <to> <subject> <body>")
        sys.exit(1)
    send_email(sys.argv[1], sys.argv[2], sys.argv[3])
