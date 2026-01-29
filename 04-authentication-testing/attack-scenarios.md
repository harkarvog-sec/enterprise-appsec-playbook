# Authentication Attack Scenarios

This document outlines realistic attack scenarios that arise from weaknesses in authentication logic, session handling, and identity state management. Each scenario reflects common enterprise failure patterns observed in real-world security incidents.

---

## 1. Session Persistence After Password Reset

# Description: 
An attacker gains access to a valid session token prior to a victim resetting their password.

# Attack Flow:
1. Attacker steals or intercepts a valid session token
2. Victim resets account password believing access is revoked
3. Existing sessions remain active server-side
4. Attacker continues to access the account uninterrupted

# Impact:
- Persistent account takeover
- Loss of user trust
- Failure of incident containment procedures

---

## 2. Authentication Bypass via Alternate Client

# Description: 
Authentication enforcement is applied to the web application but inconsistently implemented on API or mobile endpoints.

# Attack Flow:
1. Attacker identifies protected web endpoint
2. Equivalent API endpoint lacks authentication enforcement
3. Attacker accesses sensitive functionality directly via API

# Impact:
- Unauthorized data access
- Full account compromise without credentials

---

## 3. MFA Enforcement Gaps on Sensitive Actions

# Description:
Multi-factor authentication is enforced during login but not revalidated for sensitive account actions.

# Attack Flow:
1. Attacker authenticates using stolen credentials
2. MFA is not re-triggered for critical actions
3. Attacker changes email, password, or security settings

# Impact:
- Privilege escalation
- Permanent account takeover

---

## 4. OAuth Account Misbinding

# Description: 
Improper validation of OAuth `state` parameters allows identity confusion during SSO flows.

# Attack Flow:
1. Attacker initiates OAuth login flow
2. Victim completes authentication using attacker-controlled session
3. Victim’s account becomes linked to attacker identity

# Impact:
- Unauthorized account access
- Identity integrity violation

---

## 5. Token Replay Across Devices and Locations

# Description:
Access tokens are not bound to device, IP, or client context.

# Attack Flow:
1. Attacker captures access token
2. Token reused from different device or location
3. Application fails to detect abnormal token usage

# Impact:
- Silent session hijacking
- Long-term unauthorized access

---

## 6. Account Enumeration via Authentication Responses

# Description:
Authentication and recovery endpoints return distinct responses for valid vs invalid users.

# Attack Flow:
1. Attacker submits password reset or login attempts
2. Response behavior reveals account existence
3. Valid accounts are harvested for targeted attacks

# Impact:
- Credential stuffing
- Targeted phishing campaigns
