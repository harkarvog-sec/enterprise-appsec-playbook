# 01 – Asset Inventory
* Enterprise Application Security Asset Discovery & Ownership Model

> **Audience:** Senior / Staff / Principal Application Security Engineers
> **Usage:** Application onboarding, attack surface mapping, architecture reviews, cloud governance
> **Scope:** FAANG / Fortune-50 scale, multi-cloud, microservices, regulated environments
> **Philosophy:** You cannot secure what you do not know exists.

---

### 1. Purpose

* Asset Inventory is the foundational control layer of Enterprise Application Security.

It enables:

* Accurate vulnerability management
* Effective threat modeling
* Blast radius analysis
* IAM governance
* Incident response scoping
* Regulatory compliance validation

Most large-scale security failures include at least one of:

* Shadow APIs
* Unmonitored internet exposure
* Orphaned cloud resources
* Zombie IAM roles
* Forgotten CI/CD pipelines
* Undocumented data flows

**Asset inventory is not documentation hygiene.**
**It is attack surface control architecture.**

---

### 2. What Counts as an Asset?

* If it processes, stores, authenticates, deploys, or routes data, it is an asset.

**Application Layer**

* APIs (internal and external)
* Microservices
* Web applications
* Background workers
* Mobile backends
* Admin portals

**Infrastructure Layer**

* Kubernetes clusters
* Virtual machines (EC2, GCE, Azure VMs)
* Load balancers
* Serverless functions
* Storage buckets
* Container registries

**Identity Layer**

* IAM roles
* Service accounts
* Managed identities
* OIDC providers
* CI/CD identities
* Federation trusts

**Data Layer**

* Databases
* Data warehouses
* Object storage
* Secrets stores
* Message queues

**Pipeline & Supply Chain**

* CI/CD pipelines
* Artifact repositories
* Container build systems
* IaC state stores

---

### 3. Real-World Failures Caused by Poor Inventory

* Public S3 bucket with no owner
* Orphaned API endpoint exposed to the internet
* Old admin portal not removed after migration
* CI runner with production admin privileges
* Staging environment using production data
* Untracked Kubernetes ingress exposing internal services

**Most major breaches include at least one unknown or unmanaged asset.**

---

### 4. Enterprise Asset Inventory Methodology

**Phase 1 – Identify Sources of Truth**

Primary inventory sources:

* Cloud provider APIs
* Kubernetes control planes
* DNS records
* IAM role inventories
* CI/CD systems
* Vulnerability scanners
* Bug bounty submissions
* CMDB (if mature)

**Do not rely solely on CMDB.**

---

### Phase 2 – Active Enumeration (Manual Validation)

* Automated inventory must be manually verified.
* Inventory without validation becomes drifted metadata.

---

### 5. Manual Asset Enumeration Techniques

**All testing must be performed in authorized environments only.**

# Kubernetes
List all services:
```bash
kubectl get svc -A
```

List ingress objects:
```bash
kubectl get ingress -A
```

Identify NodePorts:
```bash
kubectl get svc -A | grep NodePort
```

Inspect public load balancers:
```bash
kubectl describe svc <service-name>
```

# AWS
List EC2 instances:
```BASH
aws ec2 describe-instances
```

List IAM roles:
```bash
aws iam list-roles
```

List S3 buckets:
```bash
aws s3api list-buckets
```

Check public bucket ACL:
```bash
aws s3api get-bucket-acl --bucket <bucket-name>
```

List Lambda functions:
```bash
aws lambda list-functions
```

**GCP**
```bash
gcloud compute instances list
gcloud iam service-accounts list
gcloud functions list
```

**Azure**
```bash
az vm list
az functionapp list
az role assignment list
```

# DNS & Internet Exposure

Query domain:
```bash
dig company.com
```

Passive enumeration (authorized only):
```bash
amass enum -d company.com
```

**Cross-check discovered domains against known asset inventory.**

---

### 6. Enterprise Security Tool Integration

**Asset inventory must integrate security tooling correctly — not blindly trust it.**

# Rapid7 (InsightVM)

How to Use It:

* Export discovered assets
* Identify externally reachable hosts
* Correlate business criticality
* Detect rogue systems not in CMDB

Provides:

* Infrastructure-level visibility
* OS and service fingerprinting
* Exposure scoring

Does NOT Provide:

* Logical API inventory behind load balancers
* IAM relationship mapping
* Microservice trust graph

**Use as infrastructure breadth detection, not authoritative inventory.**

---

# CrowdStrike

How to Use It:

* Identify running hosts and containers
* Detect unmanaged endpoints
* Correlate runtime telemetry with applications

Provides:

* Real-time workload visibility
* Endpoint inventory
* Runtime process detection

Does NOT Provide:

* Serverless visibility
* Logical architecture mapping
* IAM trust boundaries

---

# Snyk

How to Use It:

* Identify onboarded repositories
* Detect container images
* Correlate IaC-defined infrastructure

Provides:

* Code-level inventory
* Dependency visibility
* Container asset awareness

Does NOT Provide:

* Runtime exposure mapping
* Orphaned cloud resources
* Non-scanned repositories

---

# HackerOne

How to Use It:

* Identify externally exposed domains
* Track recurring shadow assets
* Detect unmanaged APIs

**Repeated “unknown API” submissions = inventory failure.**

---

# Microsoft Power BI (or equivalent BI platform)

Aggregate:

* Cloud inventories
* Scanner exports
* IAM role listings
* Repository metadata

Build dashboards for:

* Orphaned assets
* Owner-less services
* Public exposure
* IAM sprawl
* Drift detection

**This enables executive-level governance visibility.**

---

### 7. Ownership & Classification Model

Each asset must have:

* Business owner
* Engineering owner
* Environment (dev/stage/prod)
* Data classification
* Internet exposure status
* Authentication model
* Criticality rating
* IAM role mapping

**If an asset has no owner → it is high risk by default.**

## 8. Python / API Automation

**Manual enumeration does not scale.**

**Automate aggregation and normalization.**

---

**Example – AWS EC2 Inventory**
```python
import boto3

ec2 = boto3.client('ec2')
instances = ec2.describe_instances()

for reservation in instances["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["InstanceId"], instance["State"]["Name"])
```

**Example – IAM Role Inventory**
```python
import boto3

iam = boto3.client('iam')
roles = iam.list_roles()

for role in roles["Roles"]:
    print(role["RoleName"])
```

**Example – Detect Public S3 Buckets**
```python
import boto3

s3 = boto3.client('s3')
buckets = s3.list_buckets()

for bucket in buckets["Buckets"]:
    acl = s3.get_bucket_acl(Bucket=bucket["Name"])
    for grant in acl["Grants"]:
        if "AllUsers" in str(grant):
            print("Public bucket:", bucket["Name"])
```

**Example – Rapid7 API Pull**
```python
import requests

R7_URL = "https://yourcompany.rapid7.com/api/3/assets"
API_KEY = "YOUR_API_KEY"

headers = {
    "X-Api-Key": API_KEY,
    "Content-Type": "application/json"
}

response = requests.get(R7_URL, headers=headers)
assets = response.json()

for asset in assets["resources"]:
    print(asset["ip"])
```

**Normalized Asset Model Example**
```python
asset = {
    "asset_id": "api-gateway-prod",
    "cloud": "AWS",
    "environment": "prod",
    "owner": "payments-team",
    "internet_exposed": True,
    "criticality": "high",
    "data_classification": "PCI"
}
```

Store centrally in:

* Inventory database
* SIEM enrichment layer
* CMDB sync process
* Governance reporting system

---

### 9. Continuous Inventory Enforcement

* Inventory must be continuous.

Enforce:

* Daily cloud API reconciliation
* CI/CD hooks for new service registration
* Automatic tagging policies
* Owner validation enforcement
* Orphan detection alerts
* Drift monitoring

**Untracked asset creation must generate alerts.**

---

### 10. Architecture Review Integration

Before architecture review begins:

* Asset inventory must be complete
* Trust boundaries must map to real services
* IAM roles must be enumerated
* Internet exposure validated
* Owners confirmed

**Architecture review without inventory is guesswork.**

---

### 11. Go / No-Go Enforcement Rules

Fail onboarding if:

* Asset has no owner
* Public exposure undocumented
* IAM role unmapped
* Data classification unknown
* Service not registered in inventory

---

### 12. Strategic Outcome

Effective asset inventory:

* Shrinks attack surface
* Eliminates shadow IT
* Improves scanner signal quality
* Reduces incident scope
* Enables accurate risk prioritization
* Supports regulatory compliance

**Asset inventory is not operational hygiene.**
**It is foundational AppSec architecture control.**
