# Business Logic Testing Methodology

This document outlines a step-by-step approach for identifying business logic vulnerabilities through manual analysis and testing.

---

## 1. Understand Intended Workflow

Review application functionality from a legitimate user perspective
Identify critical workflows (signup, checkout, refunds, approvals)
Document expected states and transitions

---

## 2. Identify Trust Assumptions

Assumptions about user behavior
Assumptions about request order
Assumptions about client-side enforcement

---

## 3. Manipulate Workflow Sequence

- Skip steps in multi-stage processes
- Repeat steps that should be single-use
- Reorder requests intentionally

### Example: Skipping Required Payment Step

curl -X POST https://target.com/api/order/confirm \
-H "Authorization: Bearer <token>" \
-d '{"order_id":123}'

---

#### 4. Test Rate & Limit Enforcement

Replay requests rapidly
Abuse retry mechanisms
Test quota enforcement across APIs

---

#### 5. State & Replay Testing

Reuse tokens or IDs after completion
Replay previous valid requests
Attempt state rollback

---

## Documentation & Evidence

Capture full request/response pairs
Document intended vs actual behavior
Demonstrate measurable business impact
