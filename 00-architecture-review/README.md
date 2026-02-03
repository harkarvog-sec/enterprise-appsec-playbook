### Architecture Review

Purpose:

This module focuses on security-focused architecture review of applications and platforms before (and during) implementation.
The goal is to identify design-level weaknesses that cannot be reliably detected by scanners or surface-level testing.

Architecture flaws are often the highest-impact vulnerabilities because they affect entire systems, not just individual endpoints.

---

## Objectives
- Understand the system’s trust boundaries, data flows, and dependencies
- Identify architectural weaknesses that enable large-scale compromise
- Validate whether security controls are correctly placed and enforced
- Surface risks early, before they become expensive to remediate
- Provide actionable, engineering-aligned security guidance

---

## Scope

This module applies to:

- Monolithic and microservices architectures
- Web applications, APIs, and backend services
- Cloud-native and hybrid environments
- CI/CD-integrated application architectures
- Areas reviewed include:
- Authentication and authorization boundaries
- Service-to-service trust assumptions
- Data flow and data classification
- External integrations and third-party dependencies
- Secrets management and key handling
- Logging, monitoring, and detection placement
- Failure modes and abuse scenarios

----

### Architecture Review Methodology

This playbook follows a manual-first, attacker-driven architecture review approach:

1. System Decomposition
- Identify major components, services, and data stores
- Map external and internal dependencies

2. Trust Boundary Identification
- Determine where trust changes (user → app, app → service, service → cloud)
- Identify implicit vs explicit trust assumptions

3. Data Flow Analysis
- Track sensitive data across components
- Validate encryption, access controls, and exposure points

4. Threat Modeling (Lightweight & Practical)
- Identify realistic attacker goals
- Focus on abuse paths, not theoretical threats

5. Control Placement Review
- Validate where security controls exist
- Identify missing, misplaced, or overly trusted controls

6. Failure & Abuse Analysis
- Analyze what happens when controls fail
- Identify blast radius and lateral movement paths

---

### Common Architectural Risks Identified

- Over-trusted internal services
- Missing authorization checks between microservices
- Insecure service-to-service authentication
- Centralized secrets accessible to multiple components
- Lack of tenant isolation in multi-tenant systems
- Excessive permissions in cloud IAM roles
- Blind trust in upstream identity providers
- Weak or missing audit and detection mechanisms

---

### Deliverables

- An architecture review typically produces:
- High-level system and data flow diagrams (conceptual)
- Identified trust boundaries and risk zones
- Documented architectural weaknesses
- Abuse and attack scenarios with real impact
- Risk-prioritized findings
- Clear remediation and design recommendations

---

### Output Artifacts
This module is supported by:

- testing-methodology.md – Step-by-step architecture review process
- attack-scenarios.md – Realistic architecture abuse cases
- checklist.md – Practical validation checklist
- remediation.md – Secure design and mitigation guidance

---

### Why This Matters in Enterprise AppSec

Most critical breaches are not caused by missing patches — 
they are caused by bad assumptions baked into system design.

Effective AppSec programs invest in architecture review to:

- Reduce systemic risk
- Prevent classes of vulnerabilities
- Enable secure scaling
- Support informed engineering decisions

---

### Notes
All architecture reviews documented in this playbook are based on authorized testing and assessment scenarios only.
This content is intended for defensive security, secure design, and education
