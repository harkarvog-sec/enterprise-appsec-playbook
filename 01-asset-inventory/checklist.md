# Asset Inventory – Enterprise Validation Checklist

## FAANG / Fortune-50 Scale Control Standard

> **Audience:** Senior / Staff / Principal Application Security Engineers
> **Usage:** Architecture reviews, onboarding gates, drift validation, red-team informed assessments
> **Philosophy:** Inventory is not documentation — it is a continuously validated security control.

---

# 1. Executive Validation Standard

Inventory is considered **valid** only if:

* [ ] 100% of production cloud assets are registered
* [ ] 100% of internet-facing assets are documented
* [ ] 100% IAM roles map to workloads
* [ ] Zero ownerless production assets
* [ ] Drift detection operational and <24h detection time
* [ ] Governance gates block non-compliant deployments
* [ ] Tool cross-validation performed weekly
* [ ] Third-party integrations documented and scoped

Failure of any condition = control failure.

---

# 2. Phase 1 – Baseline Inventory Construction

Used when:

* Onboarding a new environment
* Post-acquisition integration
* Rebuilding inventory after known gaps
* Migrating infrastructure

---

## 2.1 Scope Definition

* [ ] Applications
* [ ] APIs
* [ ] Databases
* [ ] Cloud infrastructure
* [ ] CI/CD systems
* [ ] Containers & Kubernetes
* [ ] Third-party integrations
* [ ] Internal services
* [ ] IAM roles & service accounts

---

## 2.2 Domain & DNS Enumeration

```bash
dig company.com
host legacy.company.com
nslookup api.company.com
```

Authorized enumeration:

```bash
amass enum -d company.com
```

Validate:

* [ ] All subdomains registered
* [ ] No legacy systems resolving
* [ ] TLS certificates tracked
* [ ] Public APIs documented

Real-world failure:
Forgotten subdomain hosting legacy CRM → unpatched → credential harvesting.

---

## 2.3 Host & Exposure Mapping

```bash
curl -I https://legacy.company.com
```

Optional authorized scanning:

```bash
nmap -sV authorized-host
```

Validate:

* [ ] Reachable hosts documented
* [ ] Public IPs classified
* [ ] Unexpected hosts investigated

---

## 2.4 Service & Port Identification

* [ ] Open ports match expected architecture
* [ ] No shadow admin panels
* [ ] No legacy exposed services

Real-world failure:
Untracked management port exposed → remote access compromise.

---

## 2.5 API & Application Interface Mapping

```bash
curl https://api.company.com/.well-known/openapi.json
curl https://api.company.com/v1/internal/debug
```

Validate:

* [ ] All endpoints tied to CI/CD
* [ ] Authentication enforced
* [ ] Owner documented
* [ ] Business criticality classified

Real-world failure:
Debug endpoint exposed → data exfiltration.

---

## 2.6 Cloud Asset Enumeration

### AWS

```bash
aws ec2 describe-instances
aws elbv2 describe-load-balancers
aws s3api list-buckets
aws rds describe-db-instances
aws lambda list-functions
aws iam list-roles
```

### GCP

```bash
gcloud compute instances list
gcloud iam service-accounts list
gcloud functions list
```

### Azure

```bash
az vm list
az functionapp list
az role assignment list
```

Validate:

* [ ] All assets in inventory DB
* [ ] Buckets classified
* [ ] Load balancers owned
* [ ] Functions mapped to repos
* [ ] IAM roles mapped to workloads

Real-world failure:
Untracked S3 bucket with default public ACL → customer export exposure.

---

## 2.7 Kubernetes Exposure Validation

```bash
kubectl get svc -A
kubectl get ingress -A
kubectl get svc -A | grep NodePort
```

Validate:

* [ ] Namespace mapped to environment
* [ ] Ingress approved
* [ ] Service accounts mapped to IAM
* [ ] Owner assigned

Real-world failure:
Admin dashboard exposed via misconfigured ingress.

---

## 2.8 Dependency & Third-Party Mapping

```bash
grep -R "API_KEY" .
```

Validate:

* [ ] SaaS integrations documented
* [ ] Credentials scoped per service
* [ ] Rotation policy enforced
* [ ] Vendor risk tier assigned

Real-world failure:
Shared SaaS API key leaked → indirect data access.

---

# 3. Phase 2 – Continuous Reconciliation

Baseline inventory is insufficient without automation.

---

## 3.1 Cloud Reconciliation Automation

```python
import boto3

ec2 = boto3.client("ec2")
instances = ec2.describe_instances()

cloud_ids = [i["InstanceId"] for r in instances["Reservations"] for i in r["Instances"]]
inventory_ids = fetch_inventory_ids()

missing = set(cloud_ids) - set(inventory_ids)

for m in missing:
    print("Untracked resource:", m)
```

---

## 3.2 Ownerless Asset Detection

```python
for asset in assets:
    if not asset["owner"]:
        print("Ownerless asset:", asset["asset_id"])
```

---

## 3.3 Public Exposure Drift

```python
if asset["public_ip"] and not asset["documented_public"]:
    print("Undocumented public exposure:", asset["asset_id"])
```

---

# 4. Phase 3 – Independent Tool Cross-Validation

Inventory must be validated against independent sources.

---

## Rapid7 InsightVM

How to use:

1. Pull asset list via API
2. Compare against inventory
3. Alert on delta

```python
import requests

url = "https://company.rapid7.com/api/3/assets"
headers = {"X-Api-Key": "API_KEY"}

assets = requests.get(url, headers=headers).json()["resources"]
rapid7_ips = [a["ip"] for a in assets]
```

Validate:

* [ ] All detected hosts in inventory
* [ ] No unmanaged systems

---

## CrowdStrike

* Pull active agent list
* Compare hostnames against inventory

Validate:

* [ ] All production compute monitored
* [ ] No blind endpoints

---

## Snyk

* Pull project list
* Map repos to deployed containers
* Ensure image ↔ repo ↔ owner linkage

Validate:

* [ ] No orphaned images
* [ ] All repos owned

---

## HackerOne

* Review recurring bug bounty reports
* Identify unknown domains/APIs

Validate:

* [ ] No repeated unknown asset reports
* [ ] Newly discovered assets registered

---

## Executive Dashboard (Power BI)

Dashboard must show:

* Ownerless assets
* Public exposure count
* IAM sprawl
* Drift events
* Reconciliation deltas

---

# 5. Phase 4 – Governance Gate Enforcement

Deployment must fail if:

* [ ] Asset not pre-registered
* [ ] Owner missing
* [ ] IAM role unmapped
* [ ] Public exposure undocumented
* [ ] Data classification undefined

Enforced in:

* CI/CD
* Infrastructure-as-Code
* Cloud provisioning
* Change management workflows

Inventory without enforcement is advisory — not control.

---

# 6. Drift Detection Simulation

Quarterly test:

* [ ] Deploy new resource
* [ ] Confirm auto-registration
* [ ] Confirm tagging
* [ ] Confirm record creation
* [ ] Delete resource
* [ ] Confirm removal detection

Detection latency target: <24 hours.

---

# 7. Red Flags Observed in Enterprise Breaches

* Public load balancer without owner
* DNS resolving to unknown infrastructure
* Kubernetes service without ingress documentation
* Container deployed without linked repository
* IAM role unused but privileged
* Repeated bug bounty reports referencing unknown APIs

These are inventory control failures.

---

# 8. Maturity Exit Criteria

Inventory control is mature when:

* [ ] Zero unknown production assets
* [ ] Zero ownerless production assets
* [ ] 100% IAM-to-workload mapping
* [ ] Daily automated reconciliation
* [ ] Drift detection operational
* [ ] Governance gates blocking
* [ ] Executive dashboard monitored

---

# 9. Strategic Principle

Asset inventory failures do not create theoretical risk.
They create repeatable attack paths.

Attackers exploit:

* What you forgot
* What you stopped tracking
* What no one owns

At FAANG / Fortune-50 scale, inventory must be:

* Continuously validated
* Independently verified
* Automation enforced
* Governance backed

> Asset inventory is not a spreadsheet.
> It is an operational security control.
