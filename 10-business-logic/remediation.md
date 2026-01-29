# Business Logic Remediation Guidance

This document outlines recommended remediation strategies for business logic vulnerabilities identified during testing. These issues often require design-level fixes rather than simple input validation or configuration changes.

---

## 1. Enforce Workflow State Server-Side

- Do not rely on client-side workflow enforcement
- Track workflow state on the server
- Validate state transitions on every request
- Reject requests that violate expected order

---

## 2. Implement Idempotency & Replay Protection

- Use idempotency keys for critical operations (payments, refunds, approvals)
- Prevent duplicate processing of identical requests
- Invalidate tokens, IDs, or references after use

---

## 3. Protect Against Race Conditions

- Apply locking or transactional controls for critical actions
- Ensure operations are atomic where required
- Validate final state before committing changes

---

## 4. Enforce Limits & Quotas Consistently

- Apply rate limits and quotas server-side
- Enforce limits consistently across web, API, and mobile clients
- Monitor for abnormal usage patterns

---

## 5. Validate Trust Boundaries

- Never trust client-controlled values for critical decisions
- Recalculate prices, roles, and permissions server-side
- Validate all security-relevant parameters on every request

---

## 6. Logging, Monitoring & Alerting

- Log critical business actions and failures
- Alert on abnormal workflows or repeated failures
- Retain logs for forensic and audit purposes

---

## 7. Verification

- Retest all identified abuse scenarios after remediation
- Confirm fixes eliminate the demonstrated business impact
- Document verification evidence for audit and compliance

---

## Notes

- Business logic fixes often require collaboration with product and engineering
- Validate fixes against real attacker behavior, not just happy paths
