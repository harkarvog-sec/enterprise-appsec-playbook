# Architecture Review – Checklist

Purpose:

- This checklist provides actionable steps for conducting an enterprise-grade architecture review.
- It maps to trust boundaries, data flows, control placement, and failure modes to ensure thorough coverage.

Designed for authorized testing environments only.

---

### Pre-Review Preparation

- Gather architecture diagrams (system, data flow, network, cloud)
- Identify all components (frontend, backend, API, DB, queues)
- List external integrations and third-party services
- Collect documentation on authentication, authorization, secrets management
- Identify critical data and its storage/flow

---

### Trust Boundary Review

- Identify all trust boundaries (user → app, app → service, service → service, app → cloud)
- Document implicit vs explicit trust assumptions
- Validate whether controls exist at each boundary
- Flag any boundary with missing or weak authentication/authorization

---

### Data Flow Analysis:

- Map sensitive data flows across all components
- Confirm encryption at rest and in transit
- Verify access controls for sensitive data stores
- Identify potential data leakage points
- Validate logging does not expose sensitive data

---

### Control Placement Validation:

- Confirm authentication is enforced at entry points
- Validate authorization between internal services
- Ensure rate limiting / throttling is applied where needed
- Check input validation and sanitization coverage
- Verify monitoring and alerting are placed appropriately

---

### Threat Modeling / Abuse Paths:

- Define attacker profiles (external, internal, service compromise)
- Identify high-value targets and attack goals
- Map realistic abuse paths using trust boundaries and data flows
- Assess blast radius for each scenario
- Link findings to business and operational impact

---

### Failure & Detection Assessment:

- Simulate failure scenarios (control bypass, credential compromise)
- Determine detection and alerting gaps
- Evaluate lateral movement potential
- Document remediation or mitigation strategies

---

### Risk Prioritization:

- Assign risk ratings based on impact and exploitability
- Map risks to business and operational priorities
- Highlight high-impact systemic issues first

--- 

### Reporting & Deliverables:

- Produce architecture diagrams with annotated risk areas
- Document all abuse paths and validation commands
- Include actionable remediation guidance
- Summarize findings in risk-prioritized format

---

### Notes:

- This checklist is module-specific to architecture review.
- Steps should be adjusted to the environment and application type.
- All testing must be authorized; never test systems without permission.
