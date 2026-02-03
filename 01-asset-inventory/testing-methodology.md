# Asset Inventory – Testing Methodology

## Overview:

This methodology describes a manual-first, security-driven approach to building and validating an enterprise asset inventory.

The goal is not just to list assets, but to understand exposure, ownership, trust boundaries, and business criticality, enabling effective vulnerability management and risk prioritization.

All activities assume authorized assessment environments only.

---

## Guiding Principles

- Inventory is continuous, not one-time
- Exposure matters more than raw asset count
- Unknown assets are the highest risk
- Asset context (owner, data, trust level) is as important as existence
- Automation supports — but does not replace — manual validation

---

## Step 1: Define Inventory Scope

Before enumeration begins, define what is in scope:

- Applications (web, mobile, internal)
- APIs (public, private, partner)
- Backend services and microservices
- Databases and data stores
- Cloud resources (compute, storage, IAM)
- CI/CD infrastructure
- Third-party integrations

Deliverable:
- Clear scope definition to avoid blind spots and noise

---

## Step 2: Domain & DNS Enumeration

Identify all domains and subdomains associated with the organization.

### Validation Commands

dig target.com any
nslookup target.com
host target.com

What this validates:

- Public-facing assets
- Legacy or forgotten subdomains
- Mail, auth, and infrastructure records

Deliverable:

- Initial domain and subdomain list

---

### Step 3: Host Availability & Exposure

- Determine which identified hosts are live and reachable.

## Validation Commands:

ping target.com
curl -I https://target.com

### What this validates:

- Reachability
- Internet exposure
- TLS usage

### Deliverable:

- List of live hosts
- Identification of externally exposed assets

---

### Step 4: Service & Port Identification

- Validate which services are exposed and listening.

#### Validation Commands:

nc -vz target.com 80
nc -vz target.com 443

(Automated scanning tools may be used where authorized, but results must be manually reviewed.)

#### What this validates:

- Unexpected exposed services
- Non-standard ports
- Shadow infrastructure

#### Deliverable:

- Service and port inventory per host

---

### Step 5: API & Application Interface Mapping

- Identify application and API entry points.

#### Validation Techniques:

- Review API documentation (OpenAPI / Swagger)
- Inspect browser DevTools
- Analyze mobile or frontend traffic
- Review CI/CD and deployment configs

#### Example:

curl https://target.com/.well-known/openapi.json

#### What this validates:

- API surface area
- Hidden or undocumented endpoints
- Entry points for authentication and authorization testing

#### Deliverable:

- API endpoint inventory
- Application interface map

---

### Step 6: Cloud & Infrastructure Asset Identification

- Identify cloud-native assets and infrastructure components.

#### Areas to Inventory:

- Compute (VMs, containers, serverless)
- Storage (databases, object storage)
- Networking (VPCs, load balancers, gateways)
- Identity (IAM roles, service accounts)

#### Example (AWS):

aws sts get-caller-identity

#### What this validates:

- Cloud footprint
- Identity and permission scope
- Shared or over-privileged resources

Deliverable:

- Cloud asset inventory with ownership and purpose

---

### Step 7: Dependency & Third-Party Mapping

- Identify dependencies that introduce external risk.

#### Includes:

- Third-party APIs
- SaaS integrations
- Libraries and packages
- Managed cloud services

#### What this validates:

- Supply chain exposure
- Trust relationships
- External blast radius

#### Deliverable:

- Dependency inventory with trust classification

### Step 8: Asset Classification & Risk Context

For each asset, capture context:

- Business function
- Data sensitivity
- Exposure level (public, internal, restricted)
- Authentication and authorization requirements
- Asset owner or team

This step transforms inventory into actionable risk data.

#### Deliverable:

- Risk-aware asset inventory

---

### Step 9: Documentation & Inventory Maintenance

- Maintain findings in a structured format (CSV, spreadsheet, or CMDB).

#### Example:

echo "Asset,Type,Exposure,Owner,Notes" > assets.csv
echo "api.target.com,API,Public,Payments Team,Handles PII" >> assets.csv

#### Best practices:

- Version-controlled inventory
- Regular review and updates
- Integration with vulnerability management workflows

#### Outputs:

A complete asset inventory produces:
- Domains and subdomains
- Live hosts and services
- API and application entry points
- Cloud and infrastructure assets
- Third-party dependencies
- Risk and exposure classification

#### Why This Matters:

- You cannot secure what you do not know exists.

A mature asset inventory:
- Reduces attack surface
- Enables accurate vulnerability prioritization
- Supports threat modeling and incident response
- Prevents shadow IT and forgotten assets
- Improves security reporting and leadership visibility

---

#### Notes:

- Asset inventory is a living process
- Re-run regularly and after major changes
- All activities must be explicitly authorized
