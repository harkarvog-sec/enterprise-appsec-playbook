# Architecture Review – Security Checklist

## Enterprise Application Security Architecture Review Checklist

> **Audience:** Senior Application Security Engineers
> **Usage:** Design reviews, threat modeling workshops, live architecture assessments
> **Scope:** Enterprise / regulated environments
> **Philosophy:** Manual-first, attacker-driven validation. Tools provide signal—not answers.

---

## Overview

This checklist is a **practical, field-tested validation guide** for conducting enterprise-grade architecture reviews.

It is designed to:

* Support **manual-first, attacker-driven reviews**
* Align directly with `testing-methodology.md`
* Be usable during **design reviews, threat modeling sessions, and live assessments**
* Integrate with **enterprise security tooling and automation workflows**

Each section includes:

* What to validate
* Real-world failure patterns
* Manual techniques and command examples
* How enterprise tools help (and where they don’t)
* Optional Python/API automation ideas

All activities assume **explicit authorization** and **defensive security intent** only.

---

## Pre-Review Preparation

### Validate

* Architecture diagrams collected (system, data flow, network, cloud)
* All components identified (frontend, backend, APIs, databases, queues)
* External integrations and third-party services listed
* Authentication, authorization, and secrets documentation available
* Critical data types and flows identified

**Outcome:** You understand what exists *before* testing assumptions.

---

## 1. System Decomposition & Asset Inventory

### Validate

* All application components are identified and documented
* Ownership is defined for each component
* Internet-facing vs internal assets are clearly distinguished

### Real-World Failures

* “Unknown” internal services become lateral-movement pivot points
* Shadow APIs bypass security review entirely

### Manual Techniques & Commands

```bash
# Kubernetes discovery
kubectl get namespaces
kubectl get svc -A
kubectl get pods -A

# AWS discovery
aws ec2 describe-instances
aws rds describe-db-instances
aws iam list-roles
```

### Tooling Usage

* **Rapid7**: Compare scanner coverage vs actual deployed assets
* **CrowdStrike**: Confirm runtime protection on hosts and containers

### Automation Idea

```python
def find_unowned_assets(assets):
    return [a for a in assets if not a.get("owner")]
```

---

## 2. Trust Boundary Identification

### Validate

* All trust boundaries are explicitly identified
* Network location is not treated as a trust signal
* Service-to-service identity is enforced

### Real-World Failures

* Internal APIs exposed without authentication
* Implicit trust inside VPCs or Kubernetes clusters

### Manual Techniques

```bash
# Test unauthenticated internal access
curl http://internal-api:8080/admin
```

### Tooling Usage

* **Snyk**: Identify missing auth middleware or guardrails
* **HackerOne**: Repeated auth bugs often indicate architectural flaws

### Automation Idea

```python
import requests

def test_internal_endpoints(endpoints):
    for e in endpoints:
        if requests.get(e).status_code == 200:
            print(f"[!] Unprotected endpoint: {e}")
```

---

## 3. Data Flow & Sensitive Data Handling

### Validate

* Sensitive data types identified (PII, PHI, tokens, credentials)
* Encryption enforced in transit and at rest
* Logs do not expose secrets or sensitive data

### Real-World Failures

* Tokens logged in plaintext
* PII flowing to unintended downstream services

### Manual Techniques

```bash
# Search logs for secrets
grep -R "Authorization:" /var/log/
```

### Tooling Usage

* **Rapid7**: Correlate data stores with exposure paths
* **Power BI**: Track regulated data handling across applications

---

## 4. Authentication & Authorization

### Validate

* Authentication and authorization are separate controls
* RBAC / ABAC enforced server-side
* Tokens are scoped, audience-validated, and short-lived

### Real-World Failures

* Token reuse across services
* Client-supplied role or tenant identifiers

### Manual Techniques

```bash
# Attempt cross-tenant access
curl -H "Authorization: Bearer <token>" \
https://api.company.com/tenant/other/data
```

### Tooling Usage

* **Snyk**: Detect missing authorization checks
* **HackerOne**: High IDOR volume signals architectural gaps

### Automation Idea

```python
import requests

def detect_token_reuse(token, endpoints):
    for ep in endpoints:
        r = requests.get(ep, headers={"Authorization": f"Bearer {token}"})
        if r.status_code == 200:
            print(f"[!] Token misuse: {ep}")
```

---

## 5. Service-to-Service Communication

### Validate

* Strong identity between services (mTLS, workload identity)
* Least-privilege permissions enforced
* No shared or long-lived credentials

### Real-World Failures

* One compromised service leads to environment-wide access

### Manual Techniques

```bash
# Replay service token
curl -H "Authorization: Bearer <service_token>" \
http://internal-admin:8080/config
```

### Tooling Usage

* **CrowdStrike**: Detect anomalous lateral movement
* **Rapid7**: Identify overly exposed internal services

---

## 6. CI/CD & Supply Chain Security

### Validate

* CI pipelines cannot access production secrets
* Build and deploy identities are separated
* Manual approvals exist for sensitive stages

### Real-World Failures

* CI runners leaking cloud credentials

### Manual Techniques

```bash
env | grep AWS
```

### Tooling Usage

* **Snyk**: Pipeline misconfigurations and secret detection
* **CrowdStrike**: Limited CI/CD visibility — validate manually

---

## 7. Secrets Management

### Validate

* Secrets scoped per service
* No global or shared secrets
* Rotation and access logging enabled

### Real-World Failures

* One secret unlocks many systems

### Manual Techniques

```bash
aws secretsmanager list-secrets
```

### Automation Idea

```python
def find_global_secrets(secrets):
    return [s for s in secrets if s.get("scope") == "global"]
```

---

## 8. Logging, Monitoring & Detection

### Validate

* Logs exist at trust boundaries
* Authentication failures are logged and alerted
* Logs are centrally aggregated

### Real-World Failures

* Attackers operate without detection

### Manual Techniques

```bash
# Trigger auth failure
curl -H "Authorization: Bearer invalid" https://api.company.com/admin
```

### Tooling Usage

* **CrowdStrike**: Endpoint-focused signals only
* **Power BI**: Identify missing telemetry zones

---

## 9. Failure Modes & Blast Radius

### Validate

* Impact of token or service compromise is understood
* Lateral movement paths identified

### Manual Exercise

* Assume service or token compromise
* Enumerate accessible systems, data, and actions

---

## 10. Risk Prioritization & Reporting

### Validate

* Findings mapped to business impact
* Architecture risks tracked as first-class issues

### Tooling Usage

* **Jira / ServiceNow**: Track architecture-level risks
* **Power BI**: Trend systemic weaknesses

### Automation Example

```python
import requests

payload = {
    "summary": "Missing service authorization",
    "severity": "High"
}

requests.post(JIRA_URL, json=payload, auth=AUTH)
```

---

## How Senior AppSec Engineers Use This Checklist

* Validate design, not just implementation
* Focus on trust boundaries and blast radius
* Use tools for signal, not truth
* Automate reporting, not judgment
* Fix root causes, not individual symptoms

---

## Ethics & Authorization

All checklist activities assume:

* Explicit authorization
* Defensive security intent
* Compliance with organizational policy
