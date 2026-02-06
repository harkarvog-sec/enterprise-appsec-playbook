# Network Exposure – Testing Methodology

## Overview

This methodology defines a manual-first, attacker-minded approach to identifying and validating network exposure risks across enterprise environments.

The goal is not simply to enumerate open ports, but to understand:
- What is reachable
- From where
- By whom
- With what level of trust and blast radius

Automation is used to scale, validate, and operationalize findings discovered through manual analysis.

All activities assume explicit authorization.

---

## Guiding Principles

- Network access is a security control — not a trust guarantee
- Internal networks must be treated as hostile by default
- Exposure + weak identity controls = compromise
- Blast radius matters more than individual findings
- Manual validation precedes automation and reporting

---

## Step 1: Define Network Exposure Scope

Before testing, clearly define:

- Environments (prod, staging, dev, sandbox)
- Network zones (public, private, restricted)
- Cloud vs on-prem infrastructure
- Expected exposure model (what should be reachable)
- Critical systems and sensitive data paths

### Deliverable
- Defined exposure assumptions to validate or break

---

## Step 2: External Network Exposure Identification

Identify all internet-reachable assets.

### Manual Validation

'''bash'''

nc -vz target.com 80
nc -vz target.com 443
curl -I https://target.com

Validate:

- Open ports and listening services
- TLS usage and protocol enforcement
- Unexpected or legacy endpoints
- Admin, debug, or health interfaces

## Automation & Tooling

- Rapid7 InsightVM – Discover externally exposed assets and services

- CrowdStrike – Identify exposed hosts tied to endpoint inventory

- HackerOne – Correlate exposure patterns with historical external reports

## Deliverables

- List of externally exposed hosts, services, and ports
- Identification of unintended public access

---

### Step 3: Internal Network Reachability & Trust Assumptions

Validate assumptions around internal-only access.

## Manual Validation

curl http://internal-service.local/health
curl http://internal-service.local/admin


Check:

- Services relying solely on network location
- Missing authentication on internal APIs
- Over-trusted internal endpoints

### Automation & Tooling

Rapid7 – Internal scanning to validate reachability

CrowdStrike – Detect internal service exposure on endpoints

ServiceNow CMDB – Cross-check discovered services vs documented intent

## Deliverables

- Inventory of internal services lacking proper auth
- Trust boundary violations

---

### Step 4: Segmentation & Lateral Movement Analysis

Assess east-west traffic and blast radius.

## Manual Techniques

- Review subnet layouts and routing
- Validate unrestricted service-to-service access
- Identify pivot paths between environments
- Assess impact of a single compromised host

## Automation & Tooling

Rapid7 – Network segmentation visibility

CrowdStrike – Lateral movement detections

Power BI – Visualize segmentation gaps and exposure paths

## Deliverables

- Lateral movement paths
- Segmentation weaknesses
- Blast radius assessment

### Step 5: Cloud Network Exposure Validation

Review cloud-native network controls.

## Manual Validation (AWS example)

aws ec2 describe-security-groups
aws ec2 describe-network-interfaces

Validate:

- Overly permissive inbound/outbound rules
- Environment separation (prod vs non-prod)
- Public exposure of private services
- Shared network components increasing blast radius

### Automation & Tooling

Rapid7 Cloud Risk – Cloud exposure and misconfigurations

ServiceNow – Track cloud exposure findings

Power BI – Trend cloud network risk over time

## Deliverables

- Cloud network exposure inventory
- High-risk security group or firewall findings

---

### Step 6: Management & Administrative Access Exposure

Identify exposed management interfaces.

## Manual Validation

nc -vz target.com 22
nc -vz target.com 3389

Validate:

- SSH, RDP, admin consoles
- IP allowlisting or VPN enforcement
- MFA coverage
- Weak or legacy access paths

## Automation & Tooling

CrowdStrike – Identify exposed management services on endpoints

Rapid7 – Admin interface discovery

Jira / ServiceNow – Track remediation actions

## Deliverables

- Exposed administrative interfaces
- Identity and access gaps

---

### Step 7: Egress & Outbound Traffic Controls

Assess outbound connectivity risks.

## Manual Validation

- Test arbitrary outbound connections
- Identify unrestricted internet access
- Validate data exfiltration paths

## Automation & Tooling

CrowdStrike – Detect suspicious outbound connections

Rapid7 – Identify systems with unrestricted egress

Power BI – Visualize outbound exposure trends

## Deliverables

- Egress control gaps
- Data exfiltration risk paths

---

### Step 8: Detection, Monitoring & Response Validation

Ensure exposure is visible and actionable.

## Validate:

- Network event logging
- Alerting on unexpected access
- Incident response readiness

## Tooling Integration

CrowdStrike – Real-time detection

Rapid7 – Exposure monitoring

ServiceNow – Incident and vulnerability workflows

Power BI – Executive and operational reporting

## Deliverables

- Detection gaps
- Monitoring coverage assessment

---

### Step 9: Risk Prioritization & Reporting

Prioritize findings based on:

- Exposure level
- Blast radius
- Data sensitivity
- Likelihood of exploitation

# Operational Workflow

- Findings → Jira / ServiceNow
- External patterns → HackerOne
- Risk trends → Power BI
- Validation → Manual re-testing

---

### Outputs

A mature network exposure assessment produces:

- External and internal exposure inventory
- Segmentation and lateral movement paths
- Cloud and on-prem network risks
- Management and egress exposure findings
- Risk-prioritized remediation backlog

---

### Why This Matters

Network exposure failures often:

- Bypass application security controls
- Enable lateral movement and full environment compromise
- Turn low-impact bugs into critical incidents

Strong network exposure validation:
- Reduces attack surface
- Limits blast radius
- Improves detection and response
- Strengthens overall AppSec maturity

---

### Notes

- Network exposure changes constantly — reassess regularly
- Manual validation is mandatory before automation
- Treat internal networks as untrusted
- Never test without explicit authorization
