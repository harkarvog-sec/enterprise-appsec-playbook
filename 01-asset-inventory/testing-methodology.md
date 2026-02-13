# Asset Inventory – Testing Methodology

## Enterprise Application Security Validation Framework (FAANG / Fortune-50 Scale)

> **Audience:** Senior / Staff / Principal Application Security Engineers
> **Usage:** Asset validation, onboarding gates, architecture reviews, governance enforcement
> **Scope:** Multi-cloud (AWS, GCP, Azure), Kubernetes, hybrid, serverless, CI/CD, regulated enterprise environments
> **Philosophy:** Inventory is only trustworthy if independently verified and continuously enforced.

---

# 1. Strategic Objective

This methodology defines how to validate:

* Completeness of asset inventory
* Ownership accountability
* Internet exposure accuracy
* IAM-to-workload mapping
* Data classification integrity
* Drift detection capability
* Governance enforcement

At FAANG / Fortune-50 scale, asset inventory is not documentation —
it is a **foundational security control**.

Inventory is valid only when:

* 100% of production assets are registered
* 100% of internet-facing assets are documented
* 100% IAM roles map to workloads
* Zero ownerless production assets exist
* Drift detection is automated and operational
* Governance enforcement blocks non-compliant deployments

Testing must be performed only in authorized environments.

---

# 2. Hyperscale Enterprise Reality

Large enterprises commonly operate:

* 100+ cloud accounts per provider
* 10k–100k compute workloads
* 1k+ repositories
* Multi-cloud environments
* Hybrid Kubernetes + VM + serverless deployments
* Multiple identity systems
* Federated business units
* Acquisitions with legacy infrastructure

Inventory must unify:

* Domains & DNS
* Public APIs
* Cloud compute
* IAM roles
* Kubernetes workloads
* CI/CD pipelines
* Repositories
* Data stores
* Third-party integrations
* SaaS systems

If enumeration takes more than 60 seconds, control is already degraded.

---

# 3. Core Testing Principles

1. Assume the inventory is incomplete.
2. Independently enumerate infrastructure.
3. Cross-reference multiple sources of truth.
4. Validate ownership accountability.
5. Confirm exposure assumptions.
6. Test governance enforcement.
7. Simulate drift.
8. Verify detection.

Inventory without validation is optimism.
Inventory with enforcement is enterprise control.

---

# 4. Validation Phases

---

# Phase 1 – Cloud Control Plane Reconciliation

## Goal

Ensure all cloud resources are present in central inventory.

## AWS Manual Enumeration

```bash
aws ec2 describe-instances --query 'Reservations[*].Instances[*].InstanceId' --output text
aws elbv2 describe-load-balancers
aws iam list-roles
aws lambda list-functions
aws s3api list-buckets
aws rds describe-db-instances
```

### Validation Questions

* Are all production resources present in inventory?
* Are buckets classified and owned?
* Do IAM roles map to known services?
* Are load balancers tagged and exposure documented?

Failure Condition:
Any production resource missing from inventory.

---

## GCP Validation

```bash
gcloud compute instances list
gcloud iam service-accounts list
gcloud functions list
```

---

## Azure Validation

```bash
az vm list
az functionapp list
az role assignment list
```

---

# Phase 2 – Kubernetes Enumeration

## Goal

Identify undocumented services and exposure paths.

```bash
kubectl get svc -A
kubectl get ingress -A
kubectl get svc -A | grep NodePort
kubectl describe svc <service-name>
```

### Validation Checks

* Does each namespace map to environment?
* Are external IPs documented?
* Are ingress routes approved?
* Does each service map to IAM identity?
* Is owner documented?

Common Failure:
Internal admin service exposed via misconfigured ingress.

---

# Phase 3 – DNS & External Attack Surface Validation

## Goal

Detect shadow domains and forgotten infrastructure.

```bash
dig company.com
nslookup company.com
host company.com
```

Subdomain enumeration (authorized scope only):

```bash
amass enum -d company.com
```

Cross-reference findings with inventory.

Failure Condition:
Externally reachable domain not registered.

---

# Phase 4 – Host & Service Exposure Validation

Validate live hosts:

```bash
ping target.com
curl -I https://target.com
```

Validate exposed ports:

```bash
nc -vz target.com 80
nc -vz target.com 443
```

Look for:

* Unexpected services
* Non-standard ports
* Forgotten infrastructure
* Legacy hosts still reachable

---

# Phase 5 – API & Interface Mapping

Inventory application and API entry points.

```bash
curl https://target.com/.well-known/openapi.json
```

Validation Techniques:

* Inspect OpenAPI/Swagger
* Browser DevTools traffic analysis
* Mobile API inspection
* Review deployment configs
* Inspect CI/CD pipelines

Deliverable:
API endpoint inventory mapped to owners and services.

---

# Phase 6 – IAM Relationship Testing

## Goal

Ensure identity-to-service mapping integrity.

```bash
aws iam list-roles
aws iam get-role --role-name <role-name>
```

Validate:

* Trust policy correctness
* Attached policies minimal
* Role mapped to workload
* Cross-account trust documented
* Unused roles >90 days removed

Failure Conditions:

* Role not mapped
* Excessive privilege
* Undocumented cross-account trust

---

# Phase 7 – Security Tool Cross-Validation

Security tooling provides independent visibility and must reconcile with inventory.

---

## Rapid7 InsightVM

Use to:

* Export discovered assets
* Identify externally reachable IPs
* Detect rogue hosts

Example API Pull:

```python
import requests

url = "https://yourcompany.rapid7.com/api/3/assets"
headers = {"X-Api-Key": "API_KEY"}

response = requests.get(url, headers=headers)
assets = response.json()["resources"]

for asset in assets:
    print(asset["ip"])
```

Failure:
Scanned host not present in inventory.

---

## CrowdStrike

Use to:

* Identify active endpoints
* Detect unmanaged workloads

Validation:
Compare active agent list to inventory dataset.

Failure:
Running workload without inventory registration.

---

## Snyk

Use to:

* Enumerate repositories
* Identify container images
* Map deployed services to source repos

Failure:
Deployed container not linked to repository.

---

## HackerOne

Use to:

* Identify repeated reports referencing unknown APIs
* Detect shadow assets discovered by researchers

Repeated “unknown asset” reports = inventory failure.

---

## Microsoft Power BI

Use BI aggregation to:

* Detect ownerless assets
* Flag public exposure without documentation
* Visualize IAM sprawl
* Track reconciliation metrics

Executive dashboards enforce accountability.

---

# Phase 8 – Ownership & Classification Validation

Each asset must include:

* Business owner
* Engineering owner
* Environment tag
* Data classification
* Exposure status
* Criticality rating
* IAM mapping

## Practical Test

Randomly select 10 production assets:

* Contact listed owner
* Confirm acknowledgment
* Validate classification accuracy

Owner unaware of asset = governance breakdown.

---

# Phase 9 – Automation-Based Reconciliation

Manual validation does not scale at FAANG level.

---

## Example – Detect Untracked Cloud Assets

```python
import boto3

ec2 = boto3.client("ec2")
instances = ec2.describe_instances()

cloud_ids = []
for r in instances["Reservations"]:
    for i in r["Instances"]:
        cloud_ids.append(i["InstanceId"])

inventory_ids = ["i-123", "i-456"]  # pulled from DB

missing = set(cloud_ids) - set(inventory_ids)

for m in missing:
    print("Untracked asset:", m)
```

---

## Example – Detect Ownerless Assets

```python
assets = [
    {"asset_id": "api-prod", "owner": "payments"},
    {"asset_id": "legacy-admin", "owner": None}
]

for asset in assets:
    if not asset["owner"]:
        print("Ownerless:", asset["asset_id"])
```

---

# Phase 10 – Drift Detection Testing

Simulate new asset deployment:

1. Deploy test service
2. Validate CI/CD registration hook fires
3. Confirm automatic tagging
4. Confirm inventory record created
5. Delete resource
6. Confirm removal detected

Detection >24 hours at enterprise scale is unacceptable.

---

# Phase 11 – Governance Gate Testing

Onboarding must fail if:

* Asset not registered
* Owner missing
* IAM role unmapped
* Public exposure undocumented
* Data classification undefined

Test enforcement in:

* CI/CD pipelines
* Infrastructure-as-Code workflows
* Cloud provisioning automation
* Change management process

Governance without enforcement is advisory.

---

# 5. Red Flags During Testing

* Production tagged as dev
* Public load balancer without owner
* IAM role unused but high privilege
* Kubernetes service without ingress documentation
* Container running without linked repository
* Domain resolving to unknown infrastructure
* Repeated bug bounty reports referencing unknown APIs

---

# 6. Exit Criteria (FAANG / Fortune-50 Maturity)

Validation passes when:

* 100% production assets registered
* 100% internet-facing assets documented
* 100% IAM roles mapped to workloads
* Zero ownerless production assets
* Automated reconciliation running daily
* Drift detection operational
* Governance gates enforced

---

# 7. Strategic Outcome

A validated enterprise asset inventory:

* Reduces unknown attack surface
* Improves vulnerability signal accuracy
* Accelerates incident containment
* Prevents shadow infrastructure growth
* Enables enforceable governance
* Supports audit and regulatory requirements
* Strengthens architecture review confidence

You cannot secure what you cannot enumerate.
You cannot govern what you cannot attribute.
You cannot defend what you cannot detect drifting.

**Asset inventory at FAANG / Fortune-50 scale is not a spreadsheet.**
**It is a continuously tested security control.**
