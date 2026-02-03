# Asset Inventory – Remediation Guidance

Purpose:  
Provide actionable guidance to remediate gaps identified during asset inventory. Ensures all assets are tracked, monitored, and properly secured, forming a strong foundation for enterprise AppSec.

Notes:
Apply only to authorized environments. Unauthorized access or testing is prohibited.

---

## 1. Missing or Incomplete Assets

Issue: Some assets are undocumented or missing from the inventory, creating blind spots.

#### Remediation Steps:

- Conduct comprehensive DNS and network scans to discover all domains, subdomains, and hosts.
- Review cloud environments (AWS, Azure, GCP) for untracked resources.
- Check CI/CD pipelines for deployed but undocumented services.
- Regularly reconcile inventory with DevOps and infrastructure teams.
- Implement automated asset discovery where possible (e.g., API queries, cloud SDKs).

---

## 2. Unmonitored or Shadow Services

Issue: Internal services, APIs, or endpoints exist but are not monitored or documented.

#### Remediation Steps:

- Document all internal services, APIs, and endpoints in the central inventory.
- Ensure service owners are assigned for each asset.
- Implement logging and monitoring for each service.
- Validate authentication and authorization controls on internal APIs.

---

## 3. Untracked Cloud Resources or IAM Misconfigurations

Issue: Cloud services and IAM roles not inventoried, leading to over-privileged or forgotten resources.

#### Remediation Steps:

- List all IAM users, roles, and service accounts.
- Apply **least privilege principle**: remove unnecessary permissions.
- Tag resources with ownership, purpose, and sensitivity.
- Schedule regular cloud audits and automated alerts for untracked resources.
- Monitor and log access to critical cloud resources.

---

## 4. Third-Party Dependencies

Issue: External APIs, libraries, or SaaS integrations are not tracked, increasing supply chain risk.

#### Remediation Steps:

- Maintain a complete dependency inventory.
- Track versioning, update frequency, and security advisories.
- Require vulnerability checks on all third-party components.
- Limit integration to authorized, reviewed services only.

---

## 5. Asset Classification and Context Gaps

Issue: Assets exist but lack risk classification or business context.

#### Remediation Steps:

- Classify assets by criticality and exposure (public, internal, restricted).
- Associate asset owners or teams for accountability.
- Identify sensitive data stored or processed by each asset.
- Document authentication and authorization requirements.

---

## 6. Inventory Maintenance

Issue: Asset inventory is outdated or not regularly updated.

#### Remediation Steps:

- Maintain inventory in a version-controlled system (CSV, CMDB, database).
- Schedule regular inventory reviews (monthly/quarterly).
- Integrate inventory updates into DevOps and deployment workflows.
- Automate alerts for newly deployed or modified assets.

---

## Key Takeaways

- An accurate, maintained asset inventory reduces blind spots and strengthens overall security posture.  
- Gaps in tracking, monitoring, or classification directly increase risk exposure.  
- Regular audits, automation, and cross-team collaboration are critical to long-term success.  

#### Deliverables after remediation:  
- Updated, complete asset inventory  
- Assigned owners for all assets  
- Documented dependencies and cloud resources  
- Risk-aware classification and monitoring controls
