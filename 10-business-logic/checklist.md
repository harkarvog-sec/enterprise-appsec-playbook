# Business Logic Testing Checklist

This checklist provides a structured approach for identifying and validating
business logic vulnerabilities that arise from workflow abuse, state manipulation,
and broken trust assumptions.

---

## Workflow Analysis

- [ ] Identify all critical business workflows
- [ ] Map required steps and expected state transitions
- [ ] Identify mandatory vs optional steps
- [ ] Attempt skipping required steps

---

## Transaction & Action Abuse

- [ ] Test duplicate submissions
- [ ] Test replay of completed actions
- [ ] Test concurrent execution (race conditions)

---

## State Management

- [ ] Modify workflow state parameters
- [ ] Reuse expired or completed identifiers
- [ ] Attempt rollback or state reuse

---

## Limits & Quotas

- [ ] Identify business limits (rates, quantities, thresholds)
- [ ] Test enforcement consistency across APIs and clients
- [ ] Attempt limit bypass via parameter manipulation

---

## Trust Assumptions

- [ ] Modify client-controlled values (price, role, status)
- [ ] Test server-side validation of critical values
- [ ] Identify assumptions about request order or timing

---

## Documentation

- [ ] Capture full request/response evidence
- [ ] Document intended vs actual behavior
- [ ] Clearly describe business and security impact
