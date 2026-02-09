# Architecture Review – Control Patterns Library

**Enterprise Application Security Control Patterns**

**Audience**: Senior / Staff / Principal Application Security Engineers
**Usage**: Architecture design enforcement, remediation guidance, system hardening
**Scope**: FAANG / Fortune‑50 scale, regulated and hyperscale environments

**Philosophy**
Apply systemic controls consistently to:

* Reduce blast radius
* Enforce least privilege by default
* Eliminate entire *classes* of vulnerabilities rather than individual findings

---

## 1. mTLS & Service Identity

### Purpose

* Ensure service-to-service communication is authenticated and encrypted
* Prevent lateral movement when a workload is compromised

### Architecture Review Checklist

* [ ] All east-west traffic is authenticated (no IP-based trust)
* [ ] mTLS enforced at the service or mesh layer
* [ ] Certificates are short-lived and automatically rotated
* [ ] Service identity is workload-bound
* [ ] Revocation path exists and is tested

### Reject the Design If

* Any internal API trusts network location alone
* mTLS is deferred or optional
* Certificates are long-lived or manually rotated
* Service identities are reused across workloads

### Vulnerability Classes Eliminated

* Lateral movement
* Service impersonation
* Network pivoting
* Credential replay

### Manual Validation

```bash
# Attempt access without a valid client certificate
curl --insecure http://internal-api:8080/admin
```

### Python / API Enforcement

````python
def validate_service_cert(service_cert):
    if not service_cert.is_valid():
        raise Exception("Invalid or expired service certificate")
    if not service_cert.is_signed_by_trusted_ca():
        raise Exception("Untrusted certificate authority")
````

---

## 2. Token Scoping & Short‑Lived Credentials

### Purpose

* Enforce least privilege per token, service, and user
* Reduce impact of token leakage or replay

### Architecture Review Checklist

* [ ] Tokens are short‑lived (minutes, not hours or days)
* [ ] Tokens are audience‑restricted to a single service
* [ ] Authorization context is derived server‑side
* [ ] Scopes/claims are minimal and purpose‑bound
* [ ] Token revocation or expiration is enforced

### Reject the Design If

* One token is used across multiple services
* Tenant or role is derived from client input
* Tokens are long‑lived or non‑expiring
* Authorization relies solely on frontend enforcement

### Manual Validation

```bash
curl -H "Authorization: Bearer <token>" \
  https://internal-api:8080/tenant/other/data
```

Expected result: `403 Forbidden`

### Tooling Usage

* **Snyk**: Detect missing or inconsistent authorization checks
* **HackerOne**: Repeated IDOR findings indicate systemic token misuse

### Python / API Enforcement

```python
def enforce_token_scope(token, required_scope):
    if required_scope not in token.scopes:
        raise Exception("Token scope insufficient")
```

---

## 3. IAM Boundaries & Least Privilege

### Purpose

* Prevent over‑permissioned cloud roles and service accounts
* Limit blast radius of compromised workloads or pipelines

### Architecture Review Checklist

* [ ] Each service has a dedicated IAM role
* [ ] Permissions are minimal and action‑scoped
* [ ] Build, deploy, and runtime identities are separated
* [ ] Human access is time‑bound or JIT
* [ ] Periodic permission audits are automated

### Reject the Design If

* Shared IAM roles are used across services
* Wildcard permissions are granted (`*`)
* CI/CD pipelines have persistent admin access
* There is no process to detect unused permissions

### Manual Validation

```bash
aws iam simulate-principal-policy \
  --policy-source-arn <role-arn> \
  --action-names s3:*
```

### Tooling Usage

* **Rapid7**: Map asset access to role assignments
* **Snyk**: Detect overly permissive IAM policies

### Python / API Enforcement

```python
def enforce_iam_policy(role, allowed_actions):
    for action in role.actions:
        if action not in allowed_actions:
            raise Exception(f"Excessive privilege detected: {action}")
```

---

## 4. Secrets Management

### Purpose

* Eliminate shared secrets and long‑lived credentials
* Enable rapid rotation, revocation, and auditing

### Architecture Review Checklist

* [ ] Secrets are scoped per service
* [ ] Secrets have defined TTLs or rotation policies
* [ ] Secrets are never stored in source code or images
* [ ] Access to secrets is logged and auditable
* [ ] Revocation can occur without redeployments

### Reject the Design If

* A single secret unlocks multiple systems
* Secrets are embedded in code, configs, or logs
* Rotation is manual or undefined
* Secrets are shared across environments

### Manual Validation

```bash
aws secretsmanager list-secrets
```

### Python / API Enforcement

```python
def check_global_secrets(secrets):
    return [s for s in secrets if s.get("scope") == "global"]
```

---

## 5. Logging, Monitoring & Detection

### Purpose

* Detect abnormal access, token abuse, and lateral movement
* Ensure visibility across all trust boundaries

### Architecture Review Checklist

* [ ] AuthN/AuthZ failures are logged
* [ ] Privilege escalation attempts are logged
* [ ] Cross‑tenant access attempts are logged
* [ ] Logs are centralized and tamper‑resistant
* [ ] Alerts exist for high‑risk patterns

### Reject the Design If

* Security‑critical events are not logged
* Logs are stored locally or ephemerally
* Detection relies solely on endpoint telemetry
* Alerting is deferred until after launch

### Manual Validation

```bash
curl -H "Authorization: Bearer invalid" \
  https://internal-api:8080/admin
```

Expected result: failed request *and* a logged security event

### Tooling Usage

* **CrowdStrike**: Endpoint‑level signals only (not sufficient alone)
* **Power BI / Tableau**: Identify telemetry gaps and blind spots

### Python / API Enforcement

```python
def alert_on_anomalous_event(event):
    if event.type in {"unauthorized_access", "privilege_escalation"}:
        send_alert(event)
```

---

## 6. CI/CD Security Controls

### Purpose

* Prevent pipeline compromise from reaching production
* Enforce separation of duties and artifact integrity

### Architecture Review Checklist

* [ ] Build and deploy stages use separate identities
* [ ] Production deploys require human approval
* [ ] Secrets are injected at runtime, not stored
* [ ] Artifacts are signed and verified
* [ ] CI runners are monitored and isolated

### Reject the Design If

* CI systems have direct production access
* Long‑lived secrets are stored in pipeline variables
* Any commit can deploy to production
* Artifact integrity is not verified

### Manual Validation

```bash
env | grep AWS
```

Expected result: no long‑lived or production credentials exposed

### Tooling Usage

* **Snyk**: Detect CI/CD misconfigurations and secret exposure
* **CrowdStrike**: Validate visibility into build and runner environments

---

## 7. Network Egress Controls & Outbound Access

### Purpose

* Prevent data exfiltration and command-and-control callbacks
* Limit blast radius when a service is compromised

### Real-World Failures

* Compromised services freely exfiltrate data to the internet
* Any workload can reach any SaaS, API, or attacker-controlled endpoint

### Implementation Pattern

* Default-deny outbound traffic for workloads
* Explicit allowlists for external destinations (FQDN or IP-based)
* Centralized egress via NAT gateways, proxies, or service mesh egress
* TLS inspection or destination logging where legally permissible

### Architecture Review Checklist

* [ ] Egress is denied by default for workloads
* [ ] External destinations are explicitly allowlisted
* [ ] Egress traffic is observable and logged
* [ ] Changes to egress rules require review and approval

### Reject the Design If

* Any service has unrestricted internet access by default
* Egress control is deferred to “monitoring only”
* There is no inventory of allowed external dependencies

### Manual Validation

```bash
# Attempt outbound access from a restricted workload
curl https://example.com
```

Expected result: connection blocked or logged and alerted

### Tooling Usage

* **CrowdStrike**: Detect suspicious outbound traffic patterns
* **Rapid7**: Identify workloads with unrestricted egress

### Python / API Enforcement

```python
def validate_egress(destination, allowlist):
    if destination not in allowlist:
        raise Exception("Outbound destination not approved")
```

---

## 8. Data Access Controls & Tenant Isolation

### Purpose

* Prevent cross-tenant data access and large-scale data exposure
* Ensure data access follows least privilege and business context

### Real-World Failures

* Missing object-level authorization leads to IDOR at scale
* Shared databases allow cross-tenant queries

### Implementation Pattern

* Strong server-side authorization for every data access
* Tenant context derived from authenticated identity, not client input
* Logical or physical tenant isolation at the data layer
* Mandatory encryption at rest and in transit

### Architecture Review Checklist

* [ ] Every data access path enforces authorization
* [ ] Tenant context is derived server-side
* [ ] Cross-tenant queries are impossible by design
* [ ] Sensitive data is encrypted and access is audited

### Reject the Design If

* Client-supplied tenant IDs are trusted
* Authorization is enforced only at the API layer
* Multiple tenants share data stores without strong isolation

### Manual Validation

```bash
# Attempt cross-tenant access
curl -H "Authorization: Bearer <token>" \
  https://internal-api:8080/tenant/other/data
```

Expected result: `403 Forbidden` and security event logged

### Tooling Usage

* **HackerOne**: Repeated IDOR findings indicate broken isolation
* **Snyk**: Detect missing object-level authorization

### Python / API Enforcement

```python
def enforce_tenant_isolation(request_tenant, token_tenant):
    if request_tenant != token_tenant:
        raise Exception("Cross-tenant access blocked")
```

---

## Automatic Architecture Review Failures

Any design exhibiting **any** of the following fails review by default:

* Network location used as an authentication or authorization signal
* Shared service identities or shared secrets
* Long-lived or non-expiring credentials
* Client-supplied authorization or tenant context
* Unrestricted outbound internet access
* Missing object-level authorization
* CI/CD systems with direct or persistent production access
* Security controls described as “phase two” or post-launch work

---

## Real-World Breach Archetypes This Library Prevents

These controls are designed to eliminate entire *incident classes*, not individual bugs:

* **Lateral Movement Breach** – Single pod or VM compromise leads to full internal access
* **Token Replay / IDOR Breach** – Stolen token grants cross-tenant or admin access
* **Cloud Privilege Explosion** – Over-permissioned IAM role enables account-wide impact
* **Secret Sprawl Incident** – One leaked secret unlocks multiple systems
* **Silent Intrusion** – Attackers operate undetected due to missing logs and alerts
* **Pipeline-to-Prod Compromise** – CI system compromise leads directly to production takeover
* **Data Exfiltration Event** – Workloads freely exfiltrate data to attacker-controlled endpoints

---

## Cloud Provider Enforcement Examples

### AWS

* mTLS / Identity: IRSA + ACM / SPIFFE
* Tokens: Cognito, STS AssumeRole with short session duration
* IAM: Service-specific roles, SCPs to block wildcards
* Secrets: AWS Secrets Manager with rotation
* Logging: CloudTrail, GuardDuty, centralized SIEM
* CI/CD: OIDC for GitHub Actions, no static AWS keys
* Egress: VPC endpoints, NAT allowlisting

### GCP

* mTLS / Identity: Workload Identity + mTLS
* Tokens: OAuth2 with audience restriction
* IAM: Per-service service accounts, IAM Conditions
* Secrets: Secret Manager
* Logging: Cloud Logging + SCC
* CI/CD: Workload Identity Federation
* Egress: VPC Service Controls

### Azure

* mTLS / Identity: Managed Identities
* Tokens: Entra ID tokens with scoped roles
* IAM: RBAC with custom roles
* Secrets: Azure Key Vault
* Logging: Azure Monitor + Sentinel
* CI/CD: Federated credentials for pipelines
* Egress: Azure Firewall / NSGs

---

## Reviewer Cheat Sheet (One-Page)

### Core Review Questions

If compromised, can this component:

* Access more data than it strictly needs?
* Access another service without re-authentication?
* Reach the internet without explicit approval?
* Act on behalf of another tenant or user?
* Modify or deploy production resources?

If the answer to **any** question is **yes**, the design **fails review**.

---

## Printable Architecture Review Checklist

Use this as a go/no-go gate for design approval.

### Identity & Auth

* [ ] All service-to-service traffic uses mTLS
* [ ] No network-location-based trust

### Tokens & Authorization

* [ ] Tokens are short-lived and audience-scoped
* [ ] Authorization context is server-derived

### IAM

* [ ] Per-service IAM roles with minimal permissions
* [ ] No wildcard permissions

### Secrets

* [ ] No shared or long-lived secrets
* [ ] Centralized secrets management with rotation

### Observability

* [ ] Auth failures and privilege escalation are logged
* [ ] Alerts exist for high-risk activity

### CI/CD

* [ ] Build and deploy identities are separated
* [ ] Production deploys require approval

### Network & Data

* [ ] Default-deny egress enforced
* [ ] Strong tenant isolation at the data layer

**Approval Rule:**
All boxes must be checked. Any exception requires documented risk acceptance at VP+ level.

---

**Design Review Rule of Thumb**
If a single compromised component can access more than it absolutely needs, the architecture is already failing.

