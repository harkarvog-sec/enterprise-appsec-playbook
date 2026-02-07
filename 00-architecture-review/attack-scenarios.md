# Architecture Review – Attack Scenarios

---

## Real-World Architecture-Level Attack Scenarios

Overview:
This document captures realistic, high-impact attack scenarios that arise from architectural and trust design flaws, not missing patches or simple misconfigurations.

Each scenario includes:

* Attacker goal and preconditions
* Architectural weakness
* Manual exploitation techniques with command examples
* How enterprise security tools detect (or miss) the issue
* How Senior Application Security Engineers validate, document, and automate response

These scenarios are derived from real enterprise breaches, bug bounty trends, and incident response investigations.

All scenarios assume explicit authorization and defensive security intent.

---

## Scenario 1 – Over-Trusted Internal Microservices

### Attacker Goal

Gain administrative access by abusing implicit trust between internal services.

### Architectural Weakness

* Internal services trust network location
* Missing service-to-service authorization
* No identity validation between microservices

### Real-World Pattern

Attackers compromise a low-privilege service, pivot internally, and access admin APIs with no auth enforcement.

### Manual Exploitation Techniques

'''bash'''
Direct access to internal admin endpoint:
curl http://internal-user-service:8080/admin/users

Replay a stolen service token:
curl -H "Authorization: Bearer <service_token>" \
http://internal-admin-api:8080/config

### Tooling Perspective

* Rapid7: May identify exposed internal services, not trust logic
* CrowdStrike: Often blind to legitimate-looking internal API calls
* Snyk: Can flag missing auth middleware in code

### AppSec Validation Steps

* Enumerate all internal APIs
* Test unauthenticated and cross-service access
* Require explicit service identity and authorization

### Automation Example (Python)

'''python'''

services = ["user", "billing", "admin"]
for s in services:
    r = requests.get(f"http://internal-{s}:8080/admin")
    if r.status_code == 200:
        print(f"[!] Unprotected admin endpoint: {s}")

---

## Scenario 2 – Token Reuse Across Trust Boundaries

### Attacker Goal

Escalate privileges using a valid but mis-scoped token.

### Architectural Weakness

* Same JWT reused across services
* Missing audience (`aud`) validation
* No service-specific authorization

### Manual Exploitation

```bash
curl -H "Authorization: Bearer <user_token>" \
https://api.company.com/internal/admin
```

### Tooling Perspective

* **HackerOne**: Repeated IDOR/auth bypass reports signal design failure
* **Snyk**: May flag missing token validation logic

### AppSec Insight

Multiple auth bugs usually indicate **one broken trust model**.

### Automation Example

```python
def test_token_reuse(token, endpoints):
    for ep in endpoints:
        r = requests.get(ep, headers={"Authorization": f"Bearer {token}"})
        if r.status_code == 200:
            print(f"[!] Token reuse possible: {ep}")
```

---

## Scenario 3 – Broken Tenant Isolation (Multi-Tenant Systems)

### Attacker Goal

Access another tenant’s data.

### Architectural Weakness

* Tenant ID supplied by client
* Backend trusts client-controlled identifiers
* No server-side tenant enforcement

### Manual Exploitation

```bash
curl -H "Authorization: Bearer <tenantA_token>" \
https://api.company.com/tenant/tenantB/data
```

### Tooling Perspective

* **HackerOne**: High-volume IDOR findings
* **Power BI**: Tracks tenant isolation failures across apps

### AppSec Validation

* Ensure tenant context derived server-side
* Test cross-tenant access across all APIs

---

## Scenario 4 – CI/CD Pipeline as a Privilege Escalation Vector

### Attacker Goal

Use CI/CD access to compromise production.

### Architectural Weakness

* CI runners hold production credentials
* Secrets reused across environments
* No approval or segregation gates

### Manual Techniques

```bash
# Dump environment variables from CI job
env | grep AWS
```

### Tooling Perspective

* **CrowdStrike**: Limited visibility into CI/CD runtimes
* **Snyk**: Detects pipeline misconfigurations and secrets

### AppSec Validation

* Review pipeline permissions
* Enforce build vs deploy separation

---

## Scenario 5 – Centralized Secrets with Excessive Access

### Attacker Goal

Extract secrets to access multiple systems.

### Architectural Weakness

* Global secrets store
* Broad access policies
* No per-service scoping

### Manual Exploitation

```bash
aws secretsmanager get-secret-value \
--secret-id prod/global
```

### Tooling Perspective

* **Rapid7**: Detects cloud misconfigurations
* **CrowdStrike**: Detects abuse only if anomalous

### Automation Example

```python
def find_overexposed_secrets(policies):
    return [p for p in policies if p.get("scope") == "*"]
```

---

## Scenario 6 – Logging & Detection Blind Spots

### Attacker Goal

Operate without detection.

### Architectural Weakness

* Missing logs at trust boundaries
* No alerts for auth failures
* Logs not centrally aggregated

### Manual Validation

```bash
curl -H "Authorization: Bearer invalid" \
https://api.company.com/admin
```

### Tooling Perspective

* **CrowdStrike**: Endpoint-focused, misses API abuse
* **Power BI**: Highlights missing telemetry zones

---

## Scenario 7 – Bug Bounty Signal → Architecture Failure

### Attacker Goal

Exploit the same flaw across many endpoints.

### Architectural Weakness

* Shared insecure design pattern
* No systemic remediation

### AppSec Response Pattern

* Aggregate HackerOne reports
* Identify shared root cause
* Fix once, not 50 times

### Automation Example

```python
def group_by_root_cause(reports):
    causes = {}
    for r in reports:
        causes.setdefault(r["pattern"], []).append(r)
    return causes
```

---

## Reporting & Workflow Integration

### Jira / ServiceNow

* Architecture risks logged as design issues
* Linked to multiple vulnerabilities
* Assigned to platform teams

### Power BI

Track:

* Recurring architecture flaws
* Time-to-remediate systemic issues
* Vulnerability reduction after fixes

---

## Key Takeaways for Senior AppSec Engineers

* Architecture flaws amplify attacker impact
* Tools detect symptoms, not root causes
* Manual testing exposes trust failures
* Automation scales insight, not judgment
* Fixing design issues reduces future vuln volume

---

## Ethics & Authorization

All scenarios assume:

* Explicit authorization
* Defensive security intent
* Compliance with organizational policy
