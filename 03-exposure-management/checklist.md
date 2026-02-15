# 03 – Exposure Management

> **Domain Objective:**  
> Identify, validate, monitor, and control all reachable and exploitable attack surface across internet-facing, cloud, Kubernetes, SaaS, and cross-account environments.
> **Audience:** Senior / Staff / Principal Application Security Engineers  
> **Enterprise Scope:** FAANG / Fortune-50 scale, multi-cloud, multi-account  
> **Guiding Principle:** If it is reachable, it is attackable.

---

# 1. Executive Validation Standard

Exposure control is valid only if:

- [ ] 100% internet-facing assets are identified
- [ ] 100% public assets reconcile to authoritative inventory (Control 01)
- [ ] 100% public assets have assigned owner (Control 02)
- [ ] 0 unknown DNS records exist
- [ ] No unrestricted inbound rules without documented justification
- [ ] Continuous external scanning enabled
- [ ] Exposure drift detection < 1 hour
- [ ] Executive dashboard reflects real-time exposure posture
- [ ] Automated remediation enabled for critical exposure classes

Failure of any condition = attack surface governance failure.

---

# 2. Exposure Definition Model

Exposure includes:

- Internet-facing compute
- Public load balancers
- Public object storage
- API gateways
- Public Kubernetes services
- Cross-account IAM trust
- Public DNS entries
- Third-party SaaS integrations
- Mobile backend APIs
- Shadow APIs
- Unrestricted internal lateral movement paths

Exposure ≠ only public IPs.  
Exposure = any reachable attack surface.

---

# 3. Exposure Classification Model

All exposed systems must be classified:

| Class | Description                | Required Controls            |
|-------|----------------------------|------------------------------|
| P0    | Internet-facing production | WAF + EDR + Logging + Owner  |
| P1    | Internet-facing non-prod   | IP restriction + Monitoring  |
| P2    | Vendor-accessible          | mTLS + Rate limiting         |
| P3    | Internal lateral exposure  | Segmentation + IAM review    |
| P4    | Intentionally public       | Integrity validation + Owner |

No exposure may exist without classification.

---

# 4. External Attack Surface Discovery

## 4.1 DNS Enumeration (Manual)

```bash
dig example.com
host example.com
nslookup example.com
````

Subdomain discovery:

```bash
amass enum -d example.com
subfinder -d example.com
```

Certificate transparency:

```bash
curl https://crt.sh/?q=example.com
```

Validate:

* [ ] All discovered subdomains exist in CMDB
* [ ] Unknown domains escalated
* [ ] Wildcard DNS entries reviewed
* [ ] No stale DNS pointing to decommissioned systems

Real-world failure:
Stale DNS → abandoned cloud asset → subdomain takeover.

---

## 4.2 External Attack Surface Mapping

Cross-validate against:

* External ASM platform
* Bug bounty data
* Red team intelligence
* Historical recon reports

Confirm:

* [ ] Every external IP owned
* [ ] Every open port justified
* [ ] Every TLS certificate owned
* [ ] No shadow APIs detected

---

# 5. Cloud Exposure Validation (AWS Example)

## 5.1 Public EC2

```bash
aws ec2 describe-instances \
  --query 'Reservations[*].Instances[*].[InstanceId,PublicIpAddress]'
```

Validate:

* [ ] Public IP documented
* [ ] Owner assigned
* [ ] Justification recorded
* [ ] Security groups restricted

---

## 5.2 Security Group Audit

```bash
aws ec2 describe-security-groups
```

Flag:

* 0.0.0.0/0 on ports 22, 3389, 3306, 5432
* Wide ephemeral ranges
* Overly permissive internal trust

---

## 5.3 Public S3 Buckets

```bash
aws s3api list-buckets
aws s3api get-bucket-acl --bucket <bucket-name>
```

Validate:

* [ ] No public-read without exception approval
* [ ] Block Public Access enabled
* [ ] Bucket policy reviewed
* [ ] Owner assigned

---

## 5.4 Public RDS

```bash
aws rds describe-db-instances \
  --query 'DBInstances[*].[DBInstanceIdentifier,PubliclyAccessible]'
```

Validate:

* [ ] No public RDS without architecture approval

---

# 6. Kubernetes Exposure

## 6.1 Services

```bash
kubectl get svc -A
```

Flag:

* Type=LoadBalancer
* Type=NodePort
* ExternalIPs configured

---

## 6.2 Ingress

```bash
kubectl get ingress -A
```

Validate:

* [ ] Public ingress documented
* [ ] TLS enforced
* [ ] No default backend exposure
* [ ] WAF integrated
* [ ] Rate limiting enabled

---

# 7. Cross-Account & IAM Exposure

```bash
aws iam list-roles
aws iam get-role --role-name <role-name>
```

Validate:

* [ ] External principals documented
* [ ] No wildcard principals
* [ ] Cross-account trust approved
* [ ] Owner aware of trust relationship
* [ ] No unused roles

Real-world failure:
Forgotten cross-account trust → lateral movement → full compromise.

---

# 8. SaaS & API Exposure

Validate:

* [ ] OAuth tokens minimally scoped
* [ ] No permanent API tokens
* [ ] Webhooks validate HMAC signature
* [ ] No undocumented public APIs
* [ ] No debug endpoints exposed
* [ ] Authentication + rate limiting enforced

Manual validation:

```bash
curl -I https://api.example.com/internal/debug
```

---

# 9. Tool Cross-Validation

Exposure must reconcile across platforms:

## Rapid7

* External hosts match inventory

## CrowdStrike

* All external hosts have active EDR agent

## Snyk

* Public container images reconciled to repos

## HackerOne

* Unknown asset reports trigger governance review
* Subdomain takeover reports escalate DNS governance

Repeated “unknown asset” findings = systemic exposure failure.

---

# 10. Automation – Exposure Detection

## 10.1 Detect 0.0.0.0/0 Rules

```python
for sg in security_groups:
    for rule in sg["ingress"]:
        if rule["cidr"] == "0.0.0.0/0":
            print("Open exposure:", sg["id"])
```

---

## 10.2 Detect Public Buckets

```python
if bucket["public"] == True:
    print("Public bucket:", bucket["name"])
```

---

## 10.3 DNS vs Inventory Reconciliation

```python
for record in dns_records:
    if record not in inventory_assets:
        print("Unknown DNS record:", record)
```

Unknown record → automatic investigation ticket.

---

# 11. Governance Gate Enforcement

Provisioning must fail if:

* [ ] Public resource lacks justification tag
* [ ] Owner missing
* [ ] Exposure classification missing
* [ ] Backup owner missing
* [ ] WAF not attached to public service

Enforced via:

* IaC policy engines (OPA / Sentinel)
* CI/CD controls
* Cloud provisioning hooks
* Kubernetes admission controllers

Exposure without enforcement = passive observation.

---

# 12. Drift Detection Simulation

Quarterly validation:

* Create temporary public resource
* Confirm detection < 60 minutes
* Confirm owner notification
* Confirm escalation path
* Confirm remediation ticket
* Confirm dashboard update

Detection > SLA = monitoring failure.

---

# 13. Metrics & Executive Reporting

Track:

* Total public assets
* Unknown public assets
* Mean Time to Detect (MTTD)
* Mean Time to Remediate (MTTR)
* Exposure drift frequency
* Repeat exposure offenders by team

Report monthly to:

* CISO
* Cloud governance
* Platform engineering
* Enterprise risk

---

# 14. Maturity Exit Criteria

Exposure Management is mature when:

* [ ] Zero unknown public assets
* [ ] Continuous external scanning active
* [ ] Drift detection automated
* [ ] Exposure classification enforced
* [ ] All exposure tied to owner (Control 02)
* [ ] Automated remediation active
* [ ] Red team unable to discover unmanaged internet-facing systems
* [ ] Board-level visibility established

---

# Failure Mode Warning

Most breaches do not start with zero-days.

They start with:

* Forgotten staging system
* Orphaned DNS record
* Public storage bucket
* Misconfigured security group
* Undocumented API
* Third-party vendor trust
* “Temporary” exposure left permanent

Exposure Management is breach prevention at scale.

---

# Strategic Principle

Attack surface expands faster than governance.

Exposure must be:

* Continuously enumerated
* Automatically reconciled
* Explicitly justified
* Tied to ownership
* Automatically escalated when ambiguous

> If you don’t know it’s exposed, attackers do.
