#!/usr/bin/env python3

"""
Jira Vulnerability Sync Script
Author: Mishack Victor Chinaza

Fetches vulnerability data and creates Jira tickets automatically.
"""

import os
import requests
import json
from datetime import datetime


# ================= CONFIG ================= #

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USER = os.getenv("JIRA_USER")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

PROJECT_KEY = "SEC"


# ================= HEADERS ================= #

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


# ================= FUNCTIONS ================= #

def create_ticket(summary, description, priority="Medium"):

    url = f"{JIRA_URL}/rest/api/2/issue"

    payload = {
        "fields": {
            "project": {"key": PROJECT_KEY},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Bug"},
            "priority": {"name": priority}
        }
    }

    response = requests.post(
        url,
        headers=HEADERS,
        auth=(JIRA_USER, JIRA_API_TOKEN),
        data=json.dumps(payload)
    )

    if response.status_code == 201:
        print("[+] Ticket created successfully")
    else:
        print("[-] Failed to create ticket")
        print(response.text)


def main():

    vuln = {
        "title": "SQL Injection in /login",
        "severity": "High",
        "endpoint": "/login",
        "impact": "User credential compromise"
    }

    summary = f"[{vuln['severity']}] {vuln['title']}"

    description = f"""
Vulnerability Detected

Endpoint: {vuln['endpoint']}
Severity: {vuln['severity']}
Impact: {vuln['impact']}

Reported: {datetime.utcnow()}
"""

    create_ticket(summary, description, "High")


if __name__ == "__main__":
    main()
