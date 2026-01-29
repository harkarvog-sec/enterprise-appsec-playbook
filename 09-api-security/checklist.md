# API Security Testing Checklist

A structured checklist for validating API security controls across REST, GraphQL, and microservice endpoints. Use this as a reference for manual testing and verification.

---

## Authentication & Authorization

- All endpoints require proper authentication
- Role-based access control enforced consistently
- Tokens (JWT, OAuth) validated for scope, expiry, and integrity
- SSO and OAuth flows tested for state and redirect handling

---

## Input Validation & Injection

- Query, header, JSON, and URL parameters validated
- Test for SQL/NoSQL injection, XSS, and command injection
- API responses do not leak sensitive data on errors

---

## Business Logic

- Workflows cannot be bypassed or manipulated
- Critical actions require proper authorization checks
- Abuse cases tested for financial or privilege escalation impact

---

## Data Exposure

- Responses return only required data fields
- Sensitive information (PII, secrets) not exposed
- Pagination, filtering, and ID enumeration checked

---

## Rate Limiting & Abuse Prevention

- Endpoints enforce request throttling
- Account enumeration and brute-force attacks mitigated
- Abuse detection and alerting configured

---

## Logging & Monitoring

- Authentication and authorization failures logged
- Suspicious activity triggers alerts
- Token misuse and anomalous API activity monitored
