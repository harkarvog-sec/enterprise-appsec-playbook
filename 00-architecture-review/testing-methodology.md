### Architecture Review – Testing Methodology

Overview:

This document outlines a manual-first, attacker-driven methodology for conducting application architecture reviews in enterprise environments.

The goal is to identify design-level security weaknesses that create systemic risk and cannot be reliably detected through automated scanning or endpoint-focused testing.

This methodology reflects how architecture reviews are performed in real-world AppSec programs — balancing depth, practicality, and engineering alignment.

---

## Guiding Principles

- Manual-first, not scanner-driven
- Focus on trust boundaries and assumptions
- Prioritize realistic attacker abuse paths
- Validate security controls at design level
- Optimize for impact, not volume of findings

---

### Step 1: System Decomposition

Objective:
- Understand what exists before evaluating how it can be broken.

Activities:
- Identify all major system components:
- Frontend applications
- Backend services
- APIs
- Databases
- Message queues
- Cloud services

Document:
- Ownership
- Technology stack
- Deployment model

Key Questions:
- What components are internet-facing?
- Which services communicate internally?
- Where does sensitive data reside?

---

## Step 2: Trust Boundary Identification

Objective:
Identify where trust changes within the system.

Activities:
- Map trust boundaries between:
- User → application
- Application → internal services
- Service → service
- Application → cloud provider
- Application → third parties

Identify implicit trust assumptions:
- Internal services are trusted
- Traffic from VPC is safe
- Authenticated users are authorized

Red Flags:
- Authorization based solely on network location
- Shared credentials across services
- Missing identity verification between components

---

## Step 3: Data Flow Analysis

Objective:
Track sensitive data across the system to identify exposure and misuse risks.

Activities:
- Identify sensitive data types:
- Credentials
- Tokens
- PII / PHI
- Financial data

Map how data flows:

- In transit
- At rest
- Between services

Validate:

- Encryption usage
- Access control enforcement
- Data minimization

Key Questions:

- Where can data be intercepted or leaked?
- Are least-privilege principles applied?
- Are logs exposing sensitive data?

---

### Step 4: Control Placement Review

Objective:

- Evaluate whether security controls are correctly placed and enforced.
- Activities
- Identify security controls:
- Authentication
- Authorization
- Rate limiting
- Input validation
- Monitoring and logging

Validate control placement:

- At entry points
- Between services
- At privilege boundaries

Common Issues:

- Controls enforced only at the frontend
- Missing authorization between microservices
- Over-reliance on perimeter defenses

---

### Step 5: Threat Modeling (Lightweight & Practical)

Objective:
Identify realistic attacker goals and abuse paths.

# Activities
Define attacker profiles:
- External unauthenticated attacker
- Authenticated low-privilege user
- Compromised internal service

Identify attacker goals:
- Data access
- Privilege escalation
- Lateral movement
- Service disruption

Focus on how controls can be bypassed, not theoretical threats

Output:
- Documented abuse paths
- High-impact attack scenarios

----

### Step 6: Failure & Abuse Analysis

Objective:
Understand what happens when controls fail.

# Activities
Analyze:
- Control misconfigurations
- Credential compromise scenarios
- Dependency failures

Identify:
- Blast radius
- Lateral movement paths
- Single points of failure

Key Questions:

- If this control fails, what can an attacker access?
- How far can an attacker move?
- Is detection likely or unlikely?

---

### Step 7: Risk Prioritization

Objective:
Ensure findings are meaningful and actionable.

# Activities:

Prioritize findings based on:

- Impact
- Exploitability
- Scope of exposure

Map technical risk to:
- Business impact
- Regulatory risk
- Operational risk

Outcome:
- Fewer findings
- Higher quality
- Clear remediation direction

---

### Step 8: Reporting & Communication

Objective:
Communicate architectural risk effectively to stakeholders.

# Activities:

Document:
- Affected components
- Trust boundaries involved
- Attack scenarios
- Business impact

Provide:
- Clear remediation guidance
- Design-level recommendations

Best Practices:
- Avoid tool-centric language
- Use diagrams and flow descriptions
- Align recommendations with engineering realities

Expected Outputs:
- High-level architecture diagrams
- Trust boundary mapping
- Documented architectural weaknesses
- Realistic attack scenarios
- Risk-prioritized findings
- Actionable remediation guidance

---

## Notes:
This methodology is designed for authorized security assessments only.
It is intended to support defensive security, secure design, and enterprise AppSec programs.
