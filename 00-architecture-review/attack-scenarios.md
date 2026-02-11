# Architecture Review – Attack Scenarios

> **Audience**: Senior / Staff / Principal Application Security Engineers
> **Usage**: Threat modeling, live architecture reviews, red-team informed validation
> **Scope**: FAANG / Fortune-50 scale, regulated and hyperscale environments
> **Philosophy**: Assume breach. Architecture is guilty until proven resilient.

Overview:
This document captures real-world architecture abuse paths observed across large enterprises.

These are not one-off bugs. They are:

* Systemic trust failures
* Identity boundary collapses
* Tenant isolation breakdowns
* CI/CD privilege escalations
* Secrets blast-radius amplifiers
* Detection blind spots

**Each scenario includes**:

* Attacker objective
* Architectural root cause
* Real-world failure pattern
* Manual exploitation validation
* Enterprise tooling signal (and blind spots)
* Python/API automation patterns
* Architectural remediation direction

**All testing assumes explicit authorization.**

---

### 1. Over-Trusted Internal Microservices

**Attacker Objective:**
Pivot from one compromised workload to sensitive internal services.

**Architectural Root Cause:**

* Implicit trust based on network location
* No service-to-service authentication
* Flat cluster or VPC trust model
* Missing authorization on internal admin APIs

**Real-World Failure Pattern:**

* “Internal-only” admin endpoints accessible without authentication
* Any pod can call billing/admin/config APIs
* Compromised sidecar → full environment pivot

**Manual Validation:**
# Enumerate internal services (Kubernetes)
```bash
kubectl get svc -A
```

# Attempt direct access
```bash
curl http://internal-admin:8080/config
```

**Expected secure behavior: mTLS failure or 401/403.**

## Enterprise Tooling Signal

| Tool	            | What It Detects	             | What It Misses                        |
|-------------------|--------------------------------|---------------------------------------|
| Rapid7	        | Open internal ports	         | Trust model logic                     |
| CrowdStrike	    | Lateral movement anomalies	 | Legitimate-looking internal API abuse |
| Snyk	            | Missing auth middleware	     | Runtime network trust collapse        |

**Automation Pattern:**
```python
import requests

def detect_unauth_internal(endpoints):
    for e in endpoints:
        try:
            r = requests.get(e, timeout=3)
            if r.status_code == 200:
                print(f"[!] Over-trusted service: {e}")
        except:
            pass
```

**Architectural Fix:**

- Enforce mTLS with workload identity (SPIFFE / IRSA / Workload Identity)
- Service-level authorization (RBAC/ABAC)
- Zero-trust east-west enforcement

---

### 2. Token Reuse & Audience Confusion

**Attacker Objective**
Reuse a valid token across services or privilege boundaries.

**Architectural Root Cause:**

* aud claim not validated
* Shared JWT middleware across services
* Authorization logic delegated to client
* Long-lived tokens

**Real-World Failure Pattern:**

* User token accesses internal admin API
* One service token valid across all APIs
* Repeated IDOR findings across services

**Manual Validation:**
```bash
curl -H "Authorization: Bearer <user_token>" \
  https://api.company.com/internal/admin
```

**Expected secure behavior: 403 Forbidden.**

## Enterprise Tooling Signal

| Tool	                  | Signal                              |
|-------------------------|-------------------------------------|
| HackerOne	              | Repeated IDOR/auth bypass reports   |
| Snyk	                  | Missing audience validation         |
| Power BI	              | Trend: recurring auth class issues  |

**Automation Pattern:**
```python
def test_token_reuse(token, endpoints):
    for ep in endpoints:
        r = requests.get(ep, headers={"Authorization": f"Bearer {token}"})
        if r.status_code == 200:
            print(f"[!] Token reuse possible: {ep}")
```

**Architectural Fix**

* Enforce strict audience validation
* Service-specific tokens
* Short TTL (minutes, not hours)
* Centralized authorization middleware

---

### 3. Broken Tenant Isolation (Multi-Tenant Systems)

**Attacker Objective**

* Access another tenant’s data.

**Architectural Root Cause:**

* Tenant ID supplied by client
* Backend trusts user-supplied tenant context
* No server-derived tenant binding

**Real-World Failure Pattern:**

* /tenant/{id}/data directly accessible cross-tenant
* Tenant switching via parameter manipulation

**Manual Validation**
```bash
curl -H "Authorization: Bearer <tenantA_token>" \
  https://api.company.com/tenant/tenantB/data
```

**Enterprise Tooling Signal**

| Tool	             | Signal                                    |
|--------------------|-------------------------------------------|
| HackerOne	         | High-volume IDOR findings                 |
| Power BI	         | Tenant isolation trends                   |
| Rapid7	         | Cannot detect logic-level isolation flaws |

**Automation Pattern:**
```python
def test_cross_tenant(token, tenant_ids):
    for t in tenant_ids:
        r = requests.get(
            f"https://api.company.com/tenant/{t}/data",
            headers={"Authorization": f"Bearer {token}"}
        )
        if r.status_code == 200:
            print(f"[!] Cross-tenant access detected: {t}")
```

**Architectural Fix**

* Derive tenant context server-side
* Enforce tenant binding in shared middleware
* Mandatory tenant assertion validation

---

## 4. CI/CD Pipeline Privilege Escalation

**Attacker Objective**

* Use CI access to deploy malicious artifacts or access production.

**Architectural Root Cause**

* CI runners hold persistent cloud credentials
* No separation between build and deploy identities
* Secrets injected as environment variables
* No artifact signing

**Real-World Failure Pattern**

* Leaked CI credentials → production takeover
* Malicious artifact deployed without review

**Manual Validation:**
# From CI runner:
```bash
env | grep AWS
```

**Expected secure state: ephemeral credentials only.**

## Enterprise Tooling Signal

| Tool	             | Signal                              |
|--------------------|-------------------------------------|
| Snyk	             | Pipeline misconfigurations          |
| CrowdStrike	     | Limited CI runtime visibility       |
| Rapid7	         | Cloud IAM over-permission detection |

**Automation Pattern:**
```python
def detect_ci_secrets(env_vars):
    return [k for k in env_vars if k.startswith("AWS_")]
```

**Architectural Fix:**

* Ephemeral OIDC-based credentials
* Separate build vs deploy roles
* Mandatory approval gates
* Signed artifact enforcement

---

### 5. Secrets Sprawl & Global Credential Abuse

**Attacker Objective**

* Leverage one secret to access multiple systems.

**Architectural Root Cause**

* Shared “global” secrets
* Broad access IAM policies
* Long-lived credentials

**Manual Validation**
```bash
aws secretsmanager list-secrets
aws secretsmanager get-secret-value --secret-id prod/global
```

**Enterprise Tooling Signal**

| Tool	         | Signal                     |
|----------------|----------------------------|
| Rapid7	     | Cloud IAM mapping          |
| CrowdStrike	 | Anomalous access only      |
| Snyk	         | Hardcoded secret detection |

**Automation Pattern**
```python
def find_global_secrets(secrets):
    return [s for s in secrets if s.get("scope") == "global"]
```

**Architectural Fix:**

* Per-service secrets
* Short TTL
* Strict IAM boundaries
* Mandatory rotation

---

### 6. Logging & Detection Blind Spots

**Attacker Objective**

* Operate undetected after compromise.
* Architectural Root Cause
* No logs at trust boundaries
* Auth failures not alerted
* No centralized SIEM ingestion

**Manual Validation**
```bash
curl -H "Authorization: Bearer invalid" \
  https://api.company.com/admin
```

**Expected secure behavior: logged + alert triggered.**

## Enterprise Tooling Signal

| Tool	               | Signal                                  |
|----------------------|-----------------------------------------|
| CrowdStrike	       | Endpoint events only                    |
| Power BI	           | Telemetry coverage gaps                 |
| Rapid7	           | Infrastructure events, not logic events |

**Automation Pattern**
```python
def verify_security_logging(event):
    if not event.get("logged"):
        print("[!] Detection blind spot")
```

**Architectural Fix**

* Mandatory auth logging
* Alerting on privilege escalation
* Centralized log aggregation
* Detection-as-code validation

---

### 7. Bug Bounty Signal → Architecture Failure

**Attacker Objective**

* Exploit the same design flaw across dozens of endpoints.

**Architectural Root Cause**

* Insecure shared pattern
* One-off fixes instead of systemic remediation
* No root cause aggregation

**Enterprise Pattern:**

* Repeated HackerOne IDOR reports across different services = one broken authorization model.

## Automation Pattern
```python
def group_by_root_cause(reports):
    grouped = {}
    for r in reports:
        grouped.setdefault(r["pattern"], []).append(r)
    return grouped
```

**Architectural Fix**

* Identify shared library/design flaw
* Fix once at platform layer
* Mandate adoption via secure framework

**Vulnerability Classes as Symptoms (Mapping Layer)**

These repeat because of the architectural failures above:

| Vulnerability Class	         | Architectural Failure          |
|--------------------------------|--------------------------------|
| IDOR	                         | Broken tenant isolation        |
| Privilege escalation	         | Token audience confusion       |
| Secret leakage	             | Secrets sprawl                 | 
| Lateral movement	             | Over-trusted internal services |
| CI compromise	                 | Pipeline identity collapse     |

---

## Enterprise Workflow Integration

Detection → Triage → Root Cause → Platform Fix

**Detection Sources**

* Snyk (code & pipeline)
* Rapid7 (infrastructure & IAM)
* HackerOne (external signal)
* CrowdStrike (endpoint telemetry)

**Tracking:**

* Jira / ServiceNow as architecture issues (not isolated bugs)

**Reporting**

Power BI dashboards track:

* Recurring architecture flaws
* Mean time to systemic remediation
* Vulnerability class reduction after design fixes

---

## Senior AppSec Engineer Principles

* Architecture flaws create vulnerability classes
* Tools provide signals, not answers
* Manual validation exposes trust assumptions
* Automation scales verification, not judgment
* Fixing design issues reduces future vulnerability volume exponentially

---

## Ethics & Authorization

All scenarios assume:

* Explicit written authorization
* Defensive security intent
* Compliance with organizational policy
