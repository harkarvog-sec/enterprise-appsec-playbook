# Architecture Review – Remediation Playbook
Enterprise Application Security Remediation Guide

Audience: Senior / Staff / Principal Application Security Engineers
Usage: Post-review remediation planning, design correction, security architecture refactors
Scope: FAANG / Fortune-50 scale, regulated and hyperscale environments
Philosophy: Fix systemic design flaws, not individual findings. Reduce blast radius permanently.

Overview:

This document provides architecture-level remediation guidance for issues uncovered during architecture reviews, threat modeling, and live assessments.

It focuses on:

- Correcting root-cause architectural failures
- Applying least privilege and explicit trust everywhere
- Avoiding tool-driven, ticket-level patching
- Providing repeatable remediation patterns that scale

Each section includes:

- What to fix (architecture outcome)
- Real-world failure examples
- Manual validation techniques
- How to apply enterprise security tooling correctly
- Python/API automation ideas for enforcement and tracking

---

### 1. mTLS & Service Identity

What to Fix:

- Enforce mTLS for all east-west traffic
- Bind service identity to workload, not node or IP
- Use short-lived certificates with automatic rotation
- Ensure certificate revocation paths exist and are tested

Real-World Failures:

- Services accept requests from any pod in the cluster
- Long-lived certificates allow lateral movement
- Shared service identity enables impersonation

### Manual Validation:
```bash
curl --insecure http://internal-service:8080/admin
```

Expected: connection refused

### Tooling Usage:

CrowdStrike: Detect anomalous lateral traffic
Rapid7: Identify unauthenticated services

### Python / API Automation:
```python
def validate_service_cert(service_cert):
    if not service_cert.is_valid():
        raise Exception("Expired certificate")
    if not service_cert.is_signed_by_trusted_ca():
        raise Exception("Untrusted CA")
```

---

#### 2. Token Scoping & Short-Lived Credentials
What to Fix:

- Tokens are audience-restricted and short-lived
- Authorization context derived server-side, not client-supplied
- Enforce per-service RBAC/ABAC scopes
- Token revocation and rotation implemented

Real-World Failures:

- Reused tokens grant admin access across multiple services
- Client-supplied tenant IDs bypass authorization

### Manual Validation:
```bash
curl -H "Authorization: Bearer <token>" \
  https://internal-api:8080/tenant/other/data
```

Expected: 403 Forbidden

### Tooling Usage:

Snyk: Detect missing or inconsistent authorization checks
HackerOne: IDOR findings highlight systemic token misuse

### Python / API Automation
```python
def enforce_token_scope(token, required_scope):
    if required_scope not in token.scopes:
        raise Exception("Token scope insufficient")
```

---

#### 3. IAM Boundaries & Least Privilege
What to Fix:

- Per-service IAM roles with minimal permissions
- Separation of build, deploy, runtime identities
- Time-bound or just-in-time human access
- Continuous removal of unused permissions

Real-World Failures:

- Wildcard permissions (*) in cloud roles
- CI/CD pipelines with persistent admin access

### Manual Validation:
```bash
aws iam simulate-principal-policy \
  --policy-source-arn <role-arn> \
  --action-names s3:*
````

### Tooling Usage:

Rapid7: Map asset access to role assignments
Snyk: Detect overly permissive IAM policies

## Python / API Automation:
```python
def enforce_iam_policy(role, allowed_actions):
    for action in role.actions:
        if action not in allowed_actions:
            raise Exception(f"Excessive privilege detected: {action}")
```

---

### 4. Secrets Management
What to Fix:

- No shared or embedded secrets
- Short-lived secrets per service
- Centralized secrets management (Vault, Secrets Manager)
- Rotation, revocation, and access logging implemented

Real-World Failures:

- One secret unlocks multiple systems
- Secrets stored in code or images

## Manual Validation:
```bash
aws secretsmanager list-secrets
```

### Tooling Usage:

Snyk: Detect secrets in source or images
CrowdStrike: Monitor secret access patterns

## Python / API Automation:
```python
def check_global_secrets(secrets):
    return [s for s in secrets if s.get("scope") == "global"]
```

---

### 5. Logging, Monitoring & Detection
What to Fix:

- Centralized, tamper-resistant logging
- Mandatory logging for AuthN/AuthZ failures and privilege escalation
- Alerts for anomalous or cross-tenant access
- Visibility into all trust boundaries

Real-World Failures:

- Authentication failures not logged
- Lateral movement remains undetected for months

## Manual Validation:
```bash
curl -H "Authorization: Bearer invalid" \
  https://internal-api:8080/admin
```

Expected: failed request and logged security event

## Tooling Usage:

CrowdStrike: Host-level detection
Power BI / Tableau: Track telemetry gaps

## Python / API Automation:
```python
def alert_on_anomalous_event(event):
    if event.type in {"unauthorized_access", "privilege_escalation"}:
        send_alert(event)
```
---

### 6. CI/CD Security Controls
What to Fix:

- Separate build/deploy identities
- Runtime injection of secrets only
- Signed artifacts and provenance validation
- Human approval for production deploys
- Monitor CI/CD runners

Real-World Failures:

- CI systems have direct production access
- Long-lived secrets stored in pipeline variables

### Manual Validation:
````bash
env | grep AWS
````

Expected: no production credentials exposed

### Tooling Usage:

- Snyk: Detect CI/CD misconfigurations
- CrowdStrike: Monitor runners and build environments

### Python / API Automation:
```python
def validate_pipeline_config(runner_env):
    if runner_env.contains_prod_credentials():
        raise Exception("Pipeline exposure detected")
```

---

### 7. Network Egress Controls & Outbound Access
What to Fix:

- Default-deny egress enforced
- Explicit allowlisting of external destinations
- Centralized egress and logging
- TLS inspection where allowed

Real-World Failures:

- Workloads freely exfiltrate data to attacker endpoints

# Manual Validation:
```bash
curl https://target.com
```

Expected: connection blocked/logged

### Tooling Usage:

- CrowdStrike: Detect anomalous outbound traffic
- Rapid7: Identify unrestricted egress

### Python / API Automation:
```python
def validate_egress(destination, allowlist):
    if destination not in allowlist:
        raise Exception("Outbound destination not approved")
```

---

### 8. Data Access Controls & Tenant Isolation
What to Fix:

- Strong server-side authorization
- Tenant context derived from authenticated identity
- Logical/physical tenant isolation
- Mandatory encryption in transit and at rest

Real-World Failures:

- Shared databases allow cross-tenant access
- Object-level authorization missing (IDOR)

## Manual Validation:
```bash
curl -H "Authorization: Bearer <token>" \
  https://internal-api:8080/tenant/other/data
```

Expected: 403 Forbidden and logged

## Tooling Usage:

- HackerOne: Detect repeated IDORs
- Snyk: Check missing object-level authorization

## Python / API Automation:
```python
def enforce_tenant_isolation(request_tenant, token_tenant):
    if request_tenant != token_tenant:
        raise Exception("Cross-tenant access blocked")
```

---

### Appendix – Issue-to-Remediation Mapping

| Issue	                           | Maps to Section(s)	        | Canonical Fix
| ---------------------------------|----------------------------|--------------------------------------------------------|
| Over-trusted internal services	 | 1,2,8	                    | Enforce mTLS, scoped tokens, tenant isolation          |
| Missing authorization	           | 2,3,8	                    | Server-side enforcement, RBAC/ABAC, audit              |
| Misconfigured IAM roles	         | 3	                        | Least-privilege roles, continuous removal              |
| Weak/missing logging	           | 5	                        | Centralized logs, alerts on anomalies                  |
| Shared secrets	                 | 4	                        | Scoped secrets, rotation, centralized management       |
| CI/CD pipeline risk       	     | 6	                        | Separate identities, runtime secrets, signed artifacts |
| Unrestricted egress	             | 7	                        | Default-deny, allowlists, centralized egress           |
| Client-supplied tenant ID	       | 8	                        | Server-derived tenant context, enforced isolation      |

---

## What Is NOT Acceptable Remediation:

- WAF or firewall rules without fixing trust boundaries
- Monitoring/alerting without privilege reduction
- Documentation only without blast radius reduction
- Assuming upstream services enforce security

---

### Approval Criteria
A remediation is considered complete only if:
- All compromised trust paths are eliminated
- Least privilege is enforced across services, IAM, and tokens
- Secrets are scoped, rotated, and not embedded
- CI/CD pipelines and egress controls are hardened
- Detection/logging is implemented and verified
