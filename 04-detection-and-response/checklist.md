# 04 – Identity, Access, and Detection Control

> **Domain Objective:**  
> Ensure all identities, access boundaries, and systems are auditable, least-privileged, and continuously monitored.
> 
> **Guiding Principle:**  
> If access exists, it must be controlled; if exploitation occurs, it must be detected.  
>
> **Enterprise Scope:** FAANG / Fortune-50 scale, multi-cloud, multi-account, globally distributed infrastructure.

---

# 1. Executive Validation Standard

Control domain is considered operationally mature when:

- [ ] 100% IAM roles scoped to least privilege
- [ ] No orphaned identities or service accounts
- [ ] Tokens short-lived and rotated
- [ ] Cross-account trust explicitly approved
- [ ] Kubernetes RBAC validated
- [ ] All critical telemetry is generated and ingested
- [ ] Alert-to-incident SLA < 1 hour
- [ ] Executive dashboard highlights overprivileged identities and detection coverage
- [ ] Quarterly simulation validates response readiness

Failure of any condition = high-risk exposure.

---

# 2. IAM & Identity Access Boundaries

## 2.1 IAM Role Validation – Cloud Control Plane

### AWS CLI

```bash
aws iam list-roles
aws iam get-role --role-name <role-name> --query 'Role.{RoleName:RoleName,AssumeRolePolicyDocument:AssumeRolePolicyDocument,AttachedPolicies:AttachedPolicies}'
aws iam list-attached-role-policies --role-name <role-name>
aws iam list-role-policies --role-name <role-name>
````

Validate:

* [ ] Role mapped to owner/workload
* [ ] Policies enforce least privilege
* [ ] Wildcards (`*`) approved and documented
* [ ] No orphaned roles
* [ ] Cross-account trust explicitly approved

### GCP

```bash
gcloud iam roles list
gcloud projects get-iam-policy <PROJECT_ID>
gcloud service-accounts list
```

### Azure

```bash
az role assignment list --all
az ad user list --query "[].{displayName:displayName,principalName:userPrincipalName}"
```

---

## 2.2 Service Account / Workload Identity Mapping

```bash
aws iam list-users
aws iam list-access-keys --user-name <user>
kubectl get serviceaccounts -A
```

Validate:

* [ ] Service accounts mapped to owner
* [ ] Tokens rotated and scoped
* [ ] Workload separation enforced
* [ ] Cross-cluster/namespace trust documented

---

## 2.3 Kubernetes RBAC Enforcement

```bash
kubectl get clusterrolebinding
kubectl get rolebinding -A
kubectl describe clusterrole <role>
kubectl auth can-i <action> --as <user> --namespace <namespace>
```

Validate:

* [ ] No cluster-admin bindings to non-admin teams
* [ ] Namespaced roles scoped to team / environment
* [ ] Service accounts mapped to workloads
* [ ] Break-glass roles time-limited and monitored

---

## 2.4 Cross-Account / Cross-Project Trust

```bash
aws sts assume-role --role-arn <cross-account-role>
gcloud iam roles describe <role>
az role assignment list --all
```

Validate:

* [ ] Trust explicitly approved
* [ ] Access time-limited or token-based
* [ ] Monitoring enabled

---

## 2.5 CI/CD Token & Secrets Management

Validate:

* [ ] Tokens scoped per repository/project
* [ ] Environment variables do not store plaintext secrets
* [ ] Short-lived tokens enforced
* [ ] Automatic rotation enabled

```bash
vault kv get secret/ci/project-token
aws secretsmanager list-secrets
```

---

# 3. Privilege Escalation & Drift Detection

Automated detection:

```python
for role in roles:
    if role.has_wildcard_privileges() or allows_service_assume():
        alert("Privilege escalation possible:", role.name)

for sa in service_accounts:
    if sa.is_unmapped():
        alert("Orphaned service account:", sa.name)
```

Validate:

* [ ] No role can escalate itself without approval
* [ ] Service account token cannot assume admin roles
* [ ] Drift detected within <24h
* [ ] Auto-remediation or alerting enabled

---

# 4. Telemetry & Detection Requirements

## 4.1 Application Layer

Detect and log:

* Authentication failures
* Privilege escalation events
* Token issuance and refresh
* Sensitive data access
* Admin function usage
* Input validation failures
* SSRF / deserialization / template errors

Validation:

* Events ingested in central SIEM
* Structured logging (JSON)
* User, IP, trace ID included

---

## 4.2 Cloud Control Plane Detection

Detect:

* IAM policy changes
* Role assumptions
* Access key creation
* Security group changes
* Public S3 bucket exposure
* EKS cluster configuration changes

Validation:

* CloudTrail / cloud-native logging
* GuardDuty / detection rules active
* Cross-account monitoring enforced

---

## 4.3 Kubernetes Runtime Detection

Detect:

* Privileged pod creation
* HostPath mounts
* Container escape attempts
* New service exposed as LoadBalancer
* Image pull from untrusted registry

Validation:

* Falco / runtime policy engine logs
* Admission controller audit logs
* Central ingestion to SIEM

---

## 4.4 Identity Abuse Monitoring

Detect:

* Impossible travel
* Token replay
* MFA fatigue
* Service account misuse
* Long-lived token abuse

---

# 5. Logging Governance

All logs must:

* Be immutable
* Have defined retention (≥ 90 days hot, ≥ 1 year cold recommended)
* Be access-controlled
* Queryable within 5 minutes
* Centralized for audit and incident response

---

# 6. Detection Engineering Quality

Each detection rule must have:

* Threat hypothesis
* ATT&CK mapping
* False positive review
* Severity rating
* Runbook link
* Owner

No orphaned alerts.

---

# 7. Response Readiness

* Incident severity model defined
* Escalation matrix published
* Pager/on-call rotation active
* Isolation playbooks documented
* Credential rotation procedure defined
* Evidence preservation workflow established

Test quarterly via tabletop exercises.

---

# 8. Abuse Simulation Validation

Quarterly simulation:

* Account takeover
* Public bucket exposure
* Kubernetes privilege escalation
* API token abuse
* SSRF to metadata endpoint

Validate detection and alert time.

---

# 9. Metrics & Executive Reporting

Track:

* MTTD (Mean Time to Detect)
* MTTR (Mean Time to Remediate)
* Detection coverage %
* Alert-to-incident ratio
* False positive rate
* Drift detection time
* Overprivileged identity count

Report to:

* CISO
* Cloud governance
* Platform engineering
* Enterprise risk

---

# 10. Red Flags Observed in Enterprise Breaches

* Orphaned IAM role with admin access
* Long-lived CI/CD tokens
* Overprivileged Kubernetes cluster-admin roles
* Cross-account trust without approval
* Service accounts without owners
* Lateral movement via default roles
* Missing logging for critical events

---

# 11. Maturity Exit Criteria

Domain is mature when:

* 95%+ critical abuse paths generate telemetry
* Simulated attacks trigger alerts
* Incident response SLAs met ≥ 90%
* No unaudited logging gaps
* IAM drift detected and remediated
* Control plane logging cannot be disabled without detection

---

# Strategic Principle

> Identities, access, and detection are **enforced blast-radius controls**.
> If access exists, it must be controlled.
> If exploitation occurs, it must be detected.

Without these checks, inventory and exposure controls are **theory only**. At FAANG / Fortune-50 scale:

* Explicit access
* Least privilege enforced
* Drift monitored
* Automated detection and response
* Governance enforced
