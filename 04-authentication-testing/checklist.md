# Authentication Testing Checklist

A structured checklist for validating authentication controls across web, API, and mobile clients. Use this as a reference for manual testing and verification.

---

## Login & Authentication Controls

- Login endpoints enforce rate limiting and brute-force protection
- Authentication error messages do not disclose account existence
- MFA enforced on sensitive actions, not only during login
- All authentication paths are protected (web, API, mobile, SSO)
- Credential validation is consistent across clients

---

## Password Reset & Recovery

- Password reset tokens are single-use and time-bound
- Password reset invalidates all active sessions
- Reset flows cannot be abused for account enumeration
- Reset links cannot be replayed or reused
- Reset endpoints enforce rate limiting

---

## Session Handling

- Session identifiers are regenerated after authentication
- Sessions are invalidated server-side on logout
- Sessions are invalidated after password changes
- Concurrent session behavior is defined and enforced
- Idle and absolute session timeouts are applied

---

## Token Security

- Access tokens are short-lived
- Refresh tokens are rotated and protected
- JWT issuer (`iss`) and audience (`aud`) are validated
- Tokens are not exposed via URLs, logs, or client-side storage
- Secure cookie attributes are correctly configured

---

## OAuth / SSO

- Redirect URIs are strictly validated
- OAuth state parameters are implemented and verified
- Token scopes are minimal and enforced
- Account linking logic prevents identity confusion
