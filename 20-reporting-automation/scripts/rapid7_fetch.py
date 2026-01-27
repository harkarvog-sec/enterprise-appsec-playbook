#!/usr/bin/env python3

"""
Rapid7 Vulnerability Fetcher
Author: Mishack Victor Chinaza

Fetches vulnerability data from Rapid7 InsightVM API.
"""

import os
import requests
import json


# ================= CONFIG ================= #

RAPID7_API_URL = os.getenv("RAPID7_API_URL")
RAPID7_API_KEY = os.getenv("RAPID7_API_KEY")


HEADERS = {
    "X-Api-Key": RAPID7_API_KEY,
    "Accept": "application/json"
}


# ================= FUNCTIONS ================= #

def get_assets():

    url = f"{RAPID7_API_URL}/api/3/assets"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("[-] Failed to fetch assets")
        return []

    return response.json().get("resources", [])


def get_vulnerabilities(asset_id):

    url = f"{RAPID7_API_URL}/api/3/assets/{asset_id}/vulnerabilities"

    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("[-] Failed to fetch vulns")
        return []

    return response.json().get("resources", [])


def main():

    print("[+] Fetching assets...")

    assets = get_assets()

    print(f"[+] Found {len(assets)} assets")

    for asset in assets[:5]:

        asset_id = asset["id"]
        hostname = asset.get("hostName", "unknown")

        print(f"\n[+] Asset: {hostname}")

        vulns = get_vulnerabilities(asset_id)

        for vuln in vulns[:5]:
            print(f" - {vuln['id']} | Severity: {vuln['severity']}")


if __name__ == "__main__":
    main()
