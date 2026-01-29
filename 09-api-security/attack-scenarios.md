# API Security Attack Scenarios

This document outlines realistic attack scenarios that arise from weaknesses in API authentication, authorization, business logic, and data handling. These scenarios reflect common failure patterns observed in real-world enterprise breaches.

---

## 1. Broken Object Level Authorization (BOLA)

# Description: 
An API endpoint fails to properly enforce ownership checks on object identifiers.

**Attack Flow**
1. Attacker authenticates as a low-privileged user
2. Attacker modifies object identifiers in API requests
3. API returns data belonging to other users

**Impact**
- Unauthorized data access
- Privacy violations
- Regulatory exposure

---

## 2. Broken Function Level Authorization (BFLA)

**Description**  
Sensitive API functionality is accessible without proper role validation.

**Attack Flow**
1. Attacker identifies administrative API endpoints
2. API does not enforce role-based authorization
3. Attacker executes privileged actions

**Impact**
- Privilege escalation
- Full system compromise

---

## 3. Excessive Data Exposure

**Description**  
API responses return more data than required by the client.

**Attack Flow**
1. Attacker inspects API responses
2. Sensitive fields are exposed unnecessarily
3. Data is harvested or abused

**Impact**
- Leakage of PII or secrets
- Increased attack surface

---

## 4. Business Logic Abuse

**Description**  
API enforces authentication but fails to validate workflow integrity.

**Attack Flow**
1. Attacker bypasses normal workflow steps
2. Manipulates request parameters
3. Gains unfair advantage or unauthorized outcome

**Impact**
- Financial loss
- Abuse of application functionality

---

## 5. Token Replay and Scope Abuse

**Description**  
Access tokens are reusable across clients or lack proper scope validation.

**Attack Flow**
1. Attacker captures a valid token
2. Token reused outside intended context
3. API fails to detect abnormal usage

**Impact**
- Persistent unauthorized access
- Difficult incident detection

---

## 6. Rate Limiting Bypass

**Description**  
API lacks effective abuse and throttling controls.

**Attack Flow**
1. Attacker performs high-volume requests
2. No throttling or alerting occurs
3. API resources are exhausted or abused

**Impact**
- Denial of service
- Credential stuffing or enumeration
