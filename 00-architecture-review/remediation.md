# Architecture Review – Remediation Playbook

## Enterprise Application Security Remediation Guide

> **Audience:** Senior / Staff / Principal Application Security Engineers
> **Usage:** Post-review remediation planning, design correction, security architecture refactors
> **Scope:** FAANG / Fortune-50 scale, regulated and hyperscale environments
> **Philosophy:** Fix systemic design flaws, not individual findings. Reduce blast radius permanently.

---

## Overview

This document provides **architecture-level remediation guidance** for issues uncovered during architecture reviews, threat modeling, and live assessments.

It focuses on:

* Correcting **root-cause architectural failures**
* Applying **least privilege and explicit trust** everywhere
* Avoiding tool-driven, ticket-level patching
* Providing **repeatable remediation patterns** that scale

Each section includes:

* What to fix (architecture outcome)
* Real-world failure examples
* Manual validation techniques
* How to apply enterprise security tooling correctly
* Python/API automation ideas for enforcement and tracking

---

## 1. Asset Inventory

---

## Appendix – Issue-to-Remediation Mapping (Canonical)

This section **aligns common architecture findings directly to the remediation patterns above**. It exists to prevent duplication and ensure a single source of truth.

### A1. Over-Trusted Internal Services

**Maps to:** Sections 2, 4, 8

**Canonical Fix:**

* Enforce service identity (mTLS / workload identity)
* Remove network-based trust assumptions
* Apply per-service IAM with least privilege

**Validation Signal:**

* Internal endpoints reject unauthenticated requests
* Lateral movement attempts generate alerts

---

### A2. Missing Authorization Between Services

**Maps to:** Sections 3, 4

**Canonical Fix:**

* Enforce authorization at every service boundary
* Use scoped, audience-restricted tokens
* Centralize authorization logic

**Validation Signal:**

* Cross-tenant and cross-role access attempts fail consistently

---

### A3. Misconfigured Cloud IAM Roles

**Maps to:** Sections 1, 4, 8

**Canonical Fix:**

* Apply least-privilege IAM roles per service
* Remove unused permissions continuously
* Enforce policy via infrastructure-as-code

**Validation Signal:**

* Compromised workload cannot enumerate or modify unrelated resources

---

### A4. Weak or Missing Audit & Detection

**Maps to:** Sections 7, 9

**Canonical Fix:**

* Log all authentication, authorization, and privilege changes
* Centralize logs and alert on anomalies

**Validation Signal:**

* Simulated abuse paths generate detectable signals

---

### A5. Implicit Trust in Upstream Identity Providers

**Maps to:** Sections 2, 3

**Canonical Fix:**

* Validate tokens internally (issuer, audience, scope)
* Enforce short-lived credentials

**Validation Signal:**

* Forged or replayed tokens are rejected

---

## What Is NOT Acceptable Remediation

The following **do not close architectural risk** and should not be accepted as final remediation:

* Adding WAF rules without fixing trust boundaries
* Relying solely on monitoring or alerting
* Documenting risk without blast radius reduction
* Assuming upstream services enforce security

---

## Final Notes

* This remediation playbook is the **authoritative fix layer** for the architecture review module.
* Attack scenarios describe *how systems fail*.
* The checklist validates *where controls are missing*.
* This document defines *how to permanently eliminate the failure class*.

All guidance assumes authorized environments and defensive intent only.
