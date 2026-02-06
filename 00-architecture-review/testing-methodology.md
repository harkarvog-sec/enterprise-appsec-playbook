# Architecture Review – Testing Methodology

---

## Enterprise Application Security Architecture Review Methodology

Overview:
This document defines a repeatable, enterprise-ready methodology for performing application security architecture reviews.  

The methodology is:
- Manual-first and attacker-driven
- Tool-informed, not tool-dependent 
- Designed to integrate with enterprise vulnerability management, detection, reporting, and automation workflows 

It reflects real-world attacker behavior and how Senior Application Security Engineers assess systemic risk beyond scanners.

---

## Guiding Principles

- Architecture flaws create systemic risk 
- Automated tools provide signal, not conclusions 
- Trust boundaries are the most critical control points  
- Authorization failures matter more than input validation  
- Findings must translate into engineering action 
- Automation should reduce friction, not thinking

---

## Phase 1 – System Decomposition & Asset Discovery

Objective:
Understand what exists before evaluating how it can be broken.

Manual Techniques:
- Review architecture diagrams (or reconstruct if missing)  
- Interview engineers and SREs  
- Identify major components:
  - Frontend applications  
  - Backend services  
  - APIs  
  - Databases  
  - Message queues  
  - Cloud services  
  - CI/CD systems  
- Document ownership, technology stack, and deployment model  

# Commands & Examples:
'''bash:
# Kubernetes discovery

kubectl get namespaces
kubectl get pods -A
kubectl get svc -A

# AWS asset discovery
aws ec2 describe-instances
aws rds describe-db-instances
aws iam list-roles

# Tooling Integration:

Rapid7 InsightVM: 
enumerate exposed services, internal hosts, validate scanner coverage

CrowdStrike: 
confirm hosts/containers have runtime protection, identify gaps (build agents, jump hosts)

Output: 
Asset inventory, architecture draft diagram, visibility gaps

---

### Phase 2 – Trust Boundary Identification

Objective: 
Identify where trust changes within the system and whether transitions are enforced.

# Manual Techniques:

Map trust boundaries:
- User → Application
- Application → Internal services
- Service → Service
- Application → Cloud provider
- Application → Third parties

Look for implicit trust assumptions:
- Internal services are trusted
- Traffic from VPC is safe
- Authenticated users are authorized

Red flags:
- Authorization based solely on network location
- Shared credentials across services
- Missing identity verification

## Manual Testing Example:

Reuse user token across internal services:

curl -H "Authorization: Bearer <token>" \
https://internal-api.company.local/admin

## Tooling Integration:

Snyk: 
review auth-related code patterns, detect hardcoded secrets

HackerOne: 
analyze prior reports for repeated auth flaws and systemic patterns

# Output: 
Trust boundary map, high-risk trust assumptions

---

### Phase 3 – Data Flow & Sensitivity Analysis

Objective: 
Track sensitive data across the system to identify exposure risks.

## Manual Techniques:
Trace sensitive data: credentials, tokens, PII/PHI, financial data

Map flows:
- In transit
- At rest
- Between services

Validate:
- Encryption
- Access controls
- Data minimization

## Commands & Examples

Search logs for sensitive data exposure:

grep -R "Authorization:" /var/log/

## Tooling Integration

Rapid7: 
correlate data stores with exposure risk

Power BI: 
track regulated data usage and architecture risk trends

# Output: Data flow diagrams, sensitive data exposure risks

---

### Phase 4 – Authentication & Authorization Review

Objective: 
Validate who can do what — and where it breaks.

## Manual Techniques:

- Validate RBAC enforcement
- Validate service-to-service authorization
- Validate tenant isolation
- Attempt privilege escalation with valid tokens

## Manual Testing Example:

Access another tenant’s data:

curl -H "Authorization: Bearer <tenantA_token>" \
https://api.company.com/tenantB/data

## Tooling Integration:

Snyk: 
detect missing authorization checks, insecure middleware

HackerOne:
identify IDOR and auth bypass patterns

# Output: Authorization gaps, tenant isolation risks

---

### Phase 5 – Threat Modeling & Abuse Path Analysis

Objective: 
Identify realistic attacker goals and abuse paths.

## Manual Techniques

Define attacker profiles:

- External unauthenticated attacker
- Authenticated low-privilege user
- Compromised internal service

Map abuse paths:
- Lateral movement
- Privilege escalation
- Data exfiltration

Example Abuse Path:
Compromised API token → internal service trust → admin API → database dump

## Tooling Integration

CrowdStrike:
validate detection coverage along abuse paths, identify blind spots

# Output: Documented abuse scenarios, attack chains

---

### Phase 6 – Security Control Placement Review

Objective:
Validate where controls exist and where they should exist.

## Manual Techniques

Review controls:
- Authentication
- Authorization
- Rate limiting
- Input validation
- Logging & monitoring

Validate placement at:
- Entry points
- Service boundaries
- Privilege boundaries

Identify over-centralized or missing controls

## Tooling Integration:

CrowdStrike: 
validate runtime controls

Rapid7: 
validate infrastructure control coverage

# Output: Control gaps, detection weaknesses

---

### Phase 7 – Failure Mode & Blast Radius Analysis

Objective:
Understand impact when controls fail.

# Manual Techniques

Simulate:
- Token compromise
- Service compromise
- CI/CD breach

Identify:
- Lateral movement paths
- Single points of failure

# Output: Blast radius analysis, worst-case impact scenarios

---

### Phase 8 – Risk Prioritization & Reporting

Objective:
Translate findings into actionable enterprise risk.

Activities:
- Prioritize findings based on impact, exploitability, scope
- Map technical risk to business impact, regulatory, and operational risk

# Tooling Integration

Jira / ServiceNow: 
create architecture risk tickets, assign ownership, track remediation

Python Automation Example:
import requests

payload = {
    "short_description": "Missing authorization between services",
    "impact": "High",
    "description": "Architecture review identified implicit trust..."
}

requests.post(
    "https://servicenow.company.com/api/now/table/incident",
    auth=("user","token"),
    json=payload
)

# Output: Risk-prioritized findings, tickets, actionable remediation

---

### Phase 9 – Continuous Improvement & Automation

Objective: 
Reduce repeat findings and improve security maturity.

Automation Use Cases:
- Auto-tag applications with architecture risk
- Correlate Snyk + Rapid7 findings
- Power BI dashboards for systemic issues

# Python Example – Correlate Findings:

def correlate(vulns, architecture_risks):
    return [v for v in vulns if v["component"] in architecture_risks]

# Deliverables:
- Architecture diagrams
- Trust boundary maps
- Abuse scenarios
- Risk-prioritized findings
- Jira / ServiceNow tickets
- Executive-ready reports

---

### What Senior AppSec Engineers Do Differently
- Focus on design flaws, not just CVEs
- Use tools for signal, not decisions
- Translate security into engineering language
- Automate reporting, not thinking
- Reduce future vulnerability volume

---

### Ethics & Authorization
All activities require:
- Explicit authorization
- Defensive security intent
- Alignment with organizational policy

---

## Notes:
This methodology is intended for defensive security, secure design, and enterprise AppSec programs.
