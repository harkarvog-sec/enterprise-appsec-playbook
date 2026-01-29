# Session Management Attack Scenarios

This document outlines common real-world attack scenarios targeting session management weaknesses. These scenarios illustrate the impact of poor session handling and provide reproducible examples for testing.

---

## 1. Session Hijacking

Description:
An attacker steals a valid session token to impersonate a legitimate user.

Attack Flow:
1. Capture session token via XSS, network sniffing, or browser compromise
2. Reuse the token from another client
3. Access protected resources as the victim

Impact:
Account takeover, data exposure, privilege abuse

Mitigation Reference:
Enforce Secure, HttpOnly, SameSite cookies, and token rotation

---

## 2. Session Fixation

Description:
Attacker forces a user to log in using a known session ID.

Attack Flow:
1. Attacker generates a session ID and shares it with the victim
2. Victim logs in using the attacker-controlled session
3. Attacker reuses the session ID to access the account

Impact:
Unauthorized access and account compromise

Mitigation Reference:
Regenerate session IDs immediately after authentication

---

## 3. Token Replay / Theft (JWT / OAuth)

Description:
Tokens reused outside intended session or client context.

Attack Flow:
1. Capture JWT or OAuth token from a client
2. Replay token in another session or device
3. Access sensitive API endpoints

Impact:
Persistent unauthorized access, data leakage

Mitigation Reference:
Enforce token expiry, rotation, and audience/scope validation

---

## 4. Inadequate Session Expiration

Description:
Sessions remain active after logout or extended inactivity.

Attack Flow:
1. Log in and obtain session token
2. Logout or wait for idle timeout
3. Reuse the old session token to gain access

Impact:
Credential abuse, prolonged access for attackers

Mitigation Reference:
Apply idle and absolute timeouts, invalidate tokens on logout

---

## 5. Concurrent Session Abuse

Description:
Exploiting weak concurrency policies to maintain multiple active sessions without control.

Attack Flow:
1. Log in from multiple devices/browsers
2. Terminate one session via logout or password change
3. Observe whether other sessions remain active improperly

Impact:
Unauthorized access, bypassing security controls

Mitigation Reference:
Enforce proper session concurrency policies and session invalidation
