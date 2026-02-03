# Architecture Review – Remediation Guidance

Purpose:

- This document provides practical, engineering-aligned mitigations for the risks identified in the architecture review.
- It translates findings into actionable recommendations for development, DevOps, and security teams.

Designed for authorized environments only.

---

### 1. Over-Trusted Internal Services

Issue: Internal services trust requests from other services without authentication.

#### Remediation:
- Implement mutual TLS (mTLS) between internal services
- Enforce service-to-service authentication with unique service accounts
- Apply least-privilege access for internal service accounts
- Monitor internal traffic for anomalous requests

---

### 2. Missing Authorization Between Services

Issue: APIs assume upstream enforcement and lack independent authorization.

#### Remediation:
- Enforce role-based or attribute-based authorization at every service boundary
- Require scoped tokens for all inter-service requests
- Audit internal API calls and enforce policy validation

---

### 3. Misconfigured Cloud IAM Roles

Issue: Cloud workloads have overly permissive roles.

#### Remediation:
- Apply the principle of least privilege to all IAM roles
- Regularly audit role permissions and remove unused privileges
- Monitor API calls for suspicious or excessive activity
- Use automated policy enforcement tools (e.g., AWS Config, Azure Policy)

---

### 4. Weak or Missing Audit & Detection

Issue: Critical actions are not logged or monitored.

#### Remediation:
- Centralize logging for all services and components
- Integrate logs into a SIEM or monitoring pipeline
- Set up alerts for anomalous activity or policy violations
- Test logging coverage regularly and validate detection effectiveness

---

### 5. Implicit Trust in Upstream Identity Providers

Issue: Systems accept identity assertions without internal validation.

#### Remediation:
- Validate identity tokens internally for issuer, audience, and scope
- Apply short-lived tokens and enforce expiration checks
- Monitor authentication activity for anomalies
- Implement multi-factor verification where appropriate

---

### General Recommendations:

- Document all trust boundaries and data flows clearly
- Perform regular architecture reviews and update remediation guidance as systems evolve
- Integrate security into CI/CD pipelines for continuous validation
- Educate developers and DevOps teams on secure architecture principles
- Align remediation with business impact and operational risk

---

### Notes:
- This guidance complements the attack scenarios and checklist in this module.
- All recommendations assume authorized environments.
- Implementation should balance security, usability, and operational constraints.
