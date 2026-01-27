#!/usr/bin/env python3

"""
Automated Vulnerability Report Generator
Author: Mishack Victor Chinaza

Generates Markdown vulnerability reports.
"""

import json
from datetime import datetime


# ================= FUNCTIONS ================= #

def load_data():

    with open("vulns.json", "r") as f:
        return json.load(f)


def generate_report(vulns):

    date = datetime.utcnow().strftime("%Y-%m-%d")

    filename = f"vulnerability_report_{date}.md"

    with open(filename, "w") as report:

        report.write("# Security Vulnerability Report\n\n")
        report.write(f"Date: {date}\n\n")

        report.write("| ID | Title | Severity | Status |\n")
        report.write("|----|-------|----------|--------|\n")

        for v in vulns:
            report.write(
                f"| {v['id']} | {v['title']} | {v['severity']} | {v['status']} |\n"
            )

    print(f"[+] Report created: {filename}")


def main():

    vulns = load_data()
    generate_report(vulns)


if __name__ == "__main__":
    main()
