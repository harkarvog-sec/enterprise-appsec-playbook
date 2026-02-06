# Architecture Review
Enterprise Application Security Architecture Review Playbook

Purpose:
This module provides a practical, enterprise-grade approach to application architecture security reviews.

Architecture review focuses on identifying design-level weaknesses that:

- are invisible or poorly contextualized by automated scanners
- affect entire systems rather than individual endpoints
- frequently lead to the most severe real-world security incidents

This module is designed for Senior Application Security Engineers operating in large, regulated, or complex environments and integrates tightly with enterprise vulnerability management, security tooling, reporting, and automation workflows.

--- 

### Why Architecture Review Matters
Real-world breaches rarely start with “missing patches” alone.

They succeed because of:
- over-trusted internal systems
- weak identity and authorization design
- insecure service-to-service trust
- excessive cloud and CI/CD permissions
- poor detection placement

Architecture review addresses these systemic risks early, reducing downstream vulnerability volume and improving the signal quality of security tools.

---

### When to Use This Module

Architecture reviews should be performed:

- During design and pre-implementation
- During major architectural changes
- For high-risk or business-critical applications
- When onboarding apps into:
  - bug bounty programs (HackerOne)
  - cloud or microservices environments
  - regulated domains (healthcare, finance)
- After significant security incidents

---

### Core Objectives

- Identify trust boundaries and attack surfaces
- Understand data flows and sensitive asset exposure
- Detect architectural weaknesses and abuse paths
- Validate correct placement of security controls
- Improve vulnerability prioritization accuracy
- Produce actionable, engineering-aligned remediation
- Feed findings into enterprise workflows (Jira / ServiceNow)

---

### Architecture Review Methodology (High-Level)

This playbook follows a manual-first, attacker-driven approach supported by enterprise tooling.

- System decomposition & asset discovery
- Trust boundary identification
- Data flow & data sensitivity analysis
- Authentication & authorization review
- Threat modeling & abuse path analysis
- Security control placement review
- Failure mode & blast radius analysis
- Risk prioritization & reporting
- Automation & continuous improvement

Detailed steps are documented in testing-methodology.md.

---

### Manual Techniques & Command Examples

System Enumeration:
# Kubernetes service discovery

kubectl get svc -A

# Cloud asset enumeration (AWS):

aws ec2 describe-instances
aws iam list-roles

- Token & Authorization Testing:
# Test token reuse across services

curl -H "Authorization: Bearer <token>" \
https://api.internal.company/service-b/resource

- Internal API Abuse Testing
# Test internal service trust assumptions

curl http://internal-service:8080/admin

These techniques simulate real attacker behavior and help validate whether trust boundaries are actually enforced.

--- 

### Common Architectural Risks Identified

- Over-trusted internal microservices
- Missing authorization between services
- Token reuse across unrelated systems
- Weak tenant isolation
- Secrets shared across components
- Over-privileged cloud IAM roles
- CI/CD pipelines with production-level access
- Logging and detection blind spots

Real-world examples of these risks are documented in attack-scenarios.md.

---

### Using Enterprise Security Tooling

Architecture review does not replace tools — it guides and contextualizes them.

## Rapid7 (InsightVM)

How it’s used:

- Validate infrastructure and service exposure
- Identify attack surface breadth
- Correlate architectural risk with asset criticality

What it misses:

- Authorization logic
- Trust assumptions
- Abuse paths

---

## CrowdStrike

How it’s used:

- Validate runtime visibility of services
- Detect suspicious host and process behavior
- Observe lateral movement attempts

What it misses:

- “Legitimate but malicious” API usage
- Design-level authorization flaws

---

## Snyk

How it’s used:

- Identify vulnerable dependencies
- Flag insecure authentication and crypto patterns
- Detect misconfigurations in CI/CD pipelines

What it misses:

- Runtime trust relationships
- System-level abuse chains

---

## HackerOne

How it’s used:

- External validation of attack surface
- Early signal of authorization and design flaws
- Correlate individual bugs to systemic issues

Senior AppSec Insight:
Multiple similar bug bounty findings often indicate a single architectural root cause.

---

## Jira / ServiceNow

How it’s used:

- Track architecture risks as first-class items
- Assign ownership and remediation timelines
- Link vulnerabilities to architecture findings

---

## Power BI

How it’s used:

- Aggregate architecture risk trends
- Track recurring design weaknesses
- Support executive and compliance reporting

---

## Python & API Automation
Automation is used to reduce friction and improve consistency, not replace judgment.

Example: Create Jira Ticket for Architecture Risk
import requests

JIRA_URL = "https://jira.company.com/rest/api/2/issue"
AUTH = ("email@company.com", "API_TOKEN")

payload = {
    "fields": {
        "project": {"key": "APPSEC"},
        "summary": "Missing authorization between internal services",
        "description": "Architecture review identified implicit trust...",
        "issuetype": {"name": "Security Risk"}
    }
}

requests.post(JIRA_URL, json=payload, auth=AUTH)

# Example: Pull Snyk Findings for Architecture Context
import requests

headers = {"Authorization": "token SNYK_API_TOKEN"}
resp = requests.get(
    "https://api.snyk.io/v1/org/{org_id}/issues",
    headers=headers
)

issues = resp.json()
high_risk = [i for i in issues["issues"] if i["severity"] == "high"]

These scripts allow AppSec engineers to:
- correlate tool output with architecture findings
- automate reporting
- improve prioritization workflows

---

### Output Artifacts

This module produces:

- System and data-flow diagrams
- Trust boundary maps
- Documented architecture weaknesses
- Realistic attack scenarios
- Risk-prioritized findings
- Clear remediation guidance

Supporting documents:

- testing-methodology.md
- attack-scenarios.md
- checklist.md
- remediation.md

---

### Real-World Enterprise Value

Effective architecture review:

- Reduces vulnerability noise
- Prevents entire classes of issues
- Improves detection placement
- Enables secure scaling
- Strengthens compliance posture
- Saves engineering and incident response cost

---

### Notes & Ethics

All activities described in this module assume:

- explicit authorization
- defensive security intent
- secure design and education focus

This playbook is intended for:

- Enterprise Application Security
- Secure system design
- Vulnerability prevention
- AppSec & SecOps collaboration
