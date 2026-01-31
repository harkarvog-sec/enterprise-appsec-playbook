# Enterprise Application Security Playbook

# Author: Mishack Victor Chinaza  
# Role: Application Security Engineer | Penetration Tester  

---

## Overview

This repository is a Manual-first, attacker-driven testing Enterprise Application Security playbook, complemented by automation where appropriate. It documents how I assess, validate, and demonstrate real-world security risks across modern application environments.

The playbook reflects how application security is practiced in production: focusing on logic flaws, trust boundaries, state abuse, and misconfigurations, rather than relying solely on automated tooling.

All techniques documented here are performed exclusively in authorized testing environments.

---

## How to Read This Playbook

This repository is not meant to be read linearly.

Each module can be reviewed independently based on the security area of interest (e.g., authentication, API security, CI/CD).

Hiring managers may find the following modules most representative of my approach:
- 04-authentication-testing
- 06-access-control
- 09-api-security
- 10-business-logic
- 13-ci-cd-security
- 20-reporting-automation

---

## Objectives

- Provide a practical, real-world Application Security reference
- Demonstrate enterprise AppSec and security engineering workflows
- Validate vulnerabilities with clear Proof of Impact (POI)
- Support remediation, retesting, and secure design decisions
- Enable security automation, reporting, and compliance mapping

---

## Scope & Coverage

This playbook covers application security across the full SDLC, including:

- Secure Architecture & Design Review  
- Asset Inventory & Attack Surface Mapping  
- Network Exposure & Entry Point Analysis  
- Authentication & Session Management  
- Access Control & Authorization  
- Input Validation & Injection Risks  
- File Handling & Upload Logic  
- API Security  
- Business Logic & Workflow Abuse  
- Cryptography & Secrets Handling  
- Dependency & Supply Chain Security  
- CI/CD Pipeline Security  
- Cloud Security (AWS / Azure)  
- Runtime Monitoring & Detection  
- Incident Response & Triage  
- Remediation Validation  
- Compliance Mapping  
- Security Reporting & Automation  

---

## Repository Structure

Each module follows a consistent, enterprise-grade structure:

XX-module-name/
├── README.md # Scope, goals, and security context
├── testing-methodology.md # Step-by-step attacker-driven methodology
├── attack-scenarios.md # Realistic exploitation scenarios
├── checklist.md # Practical validation checklist
└── remediation.md # Defensive guidance and fixes


---

## Modules

00-architecture-review  
01-asset-inventory  
02-network-exposure  
03-attack-surface-mapping  
04-authentication-testing  
05-session-management  
06-access-control  
07-input-validation  
08-file-handling  
09-api-security  
10-business-logic  
11-cryptography-review  
12-dependency-security  
13-ci-cd-security  
14-cloud-security  
15-runtime-monitoring  
16-incident-response  
17-bugbounty-triage  
18-remediation-testing  
19-compliance-mapping  
20-reporting-automation  

---

## How to Use This Repository

- Use it as a reference playbook when building or scaling an AppSec program  
- Apply sections independently based on your organization’s maturity  
- Adapt workflows to your tooling (e.g., Jira, ServiceNow, Rapid7, Snyk, HackerOne)  
- Use it to standardize AppSec processes across teams  

---

## Key Automation Scripts

This playbook includes practical automation scripts to support enterprise vulnerability management and reporting:

| Script         |         Description                                                    | Key Features                                                                                                                                                                            |
|----------------|-------------------|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| jira_sync.py    | Automatically creates Jira tickets for discovered vulnerabilities     | Fetches vulnerability data (demo-ready or integrated with Rapid7/Snyk)<br>- Creates tickets with severity, impact, and remediation guidance<br>- Configurable via environment variables |
| rapid7_fetch.py | Fetches vulnerability scan results from Rapid7                        | Pulls asset & vulnerability data via API<br>- Outputs structured JSON/CSV for reporting or ticketing pipelines                                                                          |
| vuln_report.py  | Generates automated vulnerability reports                             | Consolidates vulnerabilities across tools<br>- Produces enterprise-ready reports for teams and leadership<br>- Supports CSV, JSON, or PDF export for dashboards                         |

These scripts are demonstrations of my ability to integrate AppSec tooling into enterprise workflows, reducing manual effort, improving triage speed, and enabling risk-based reporting.

>  All scripts are intended for authorized testing environments only. Never use these scripts on systems you do not own or have explicit permission to test.  

---

## Methodology Philosophy

- Manual-first, attacker-driven testing  
- Focus on logic, state, and trust boundaries  
- Findings validated with exploitation evidence  
- Risks mapped to business and operational impact  
- Remediation aligned with secure engineering practices  

This playbook represents how security assessments are performed in real enterprise environments, not just theoretical labs.

---

## Design Philosophy

- Enterprise-ready: Focused on real operational constraints  
- Tool-agnostic: Concepts apply regardless of vendor  
- Risk-based: Prioritization over noise  
- Automation-friendly: Designed to scale with engineering velocity  

---

## Disclaimer

This project is intended strictly for educational purposes and authorized security testing.  
Unauthorized testing of systems you do not own or have permission to test is illegal and unethical.

---

## Contact

- GitHub: https://github.com/harkarvog-sec  
- Portfolio: https://harkarvogsecurity.com  
- LinkedIn: https://linkedin.com/in/mishack-victor-728783358
- Email: mishackvictor4@gmail.com

> Security is not about whether controls exist — it’s about whether they can be bypassed.
