# Session Management Testing Methodology

This document defines a manual, attacker-driven methodology for testing session management controls in enterprise applications. The approach focuses on identifying weaknesses in session lifecycle handling that can enable session fixation, hijacking, replay, or unauthorized persistence.

Testing is performed across web, API, and multi-client environments, prioritizing logic flaws and state handling issues over tool-driven scanning.

---

## 1. Session Identifier Generation & Entropy

### Objective
Ensure session identifiers are **unpredictable, unique, and resistant to guessing or enumeration**.

### Method
- Capture multiple session identifiers across different logins
- Compare length, format, and structure
- Look for patterns, static prefixes, or low entropy

### Validation Checks
- Session IDs are sufficiently long
- No sequential or incremental values
- No user-identifiable data embedded in tokens

### Command Example (Manual Verification):

curl -I -b "session=<SESSION_ID>" https://target.com/dashboard

---

### 2. Session Fixation Testing

## Objective
Determine whether the application issues a new session identifier after authentication.

## Method
Establish a session before login
Authenticate using the same session
Observe whether the session ID changes

# Expected Behavior
Session ID must be regenerated immediately after login
Pre-authentication session IDs must be invalidated

----

### 3. Session Invalidation (Logout & Password Change)

## Objective
Verify sessions are destroyed server-side when authentication state changes.

# Method
Capture an active session ID
Perform logout
Reuse the same session ID
Repeat after password change

## Validation Checks
Session cannot be reused after logout
All active sessions are invalidated after credential changes

---

#### 4. Idle Timeout & Absolute Timeout

## Objective
Ensure sessions expire after inactivity or maximum lifetime.

## Method
Leave session idle beyond configured timeout
Attempt reuse
Test absolute timeout regardless of activity

## Validation Checks
Idle sessions are invalidated
Long-lived sessions are forcibly expired

---

#### 5. Cookie Security Attributes

Objective
Protect session tokens from client-side and cross-site attacks.

### Method:
Inspect cookies via browser developer tools.

## Required Attributes
Secure
HttpOnly
SameSite (Strict or Lax, depending on use case)

---

#### 6. Token-Based Session Handling (JWT / OAuth)

### Objective
Validate token lifecycle, scope enforcement, and expiration.

## Method
Inspect token contents (claims, expiry, issuer)
Attempt token reuse after logout
Test refresh token rotation

### Validation Checks
Tokens expire correctly
Refresh tokens are rotated and invalidated
Scope and audience are enforced

----

### 7. Session Concurrency & Reuse

Objective
Assess how the application handles multiple active sessions.

## Method
Log in from multiple devices or browsers
Perform logout or password reset on one session
Observe impact on other sessions

### Validation Checks
Session policies are consistently enforced
Unauthorized session persistence is prevented

### Documentation Requirements
Record session identifiers before and after each action
Capture request/response evidence
Note differences between expected and observed behavior
Map findings to real-world attack scenarios

#### Notes:
All testing must be conducted in authorized environments only
Manual validation is prioritized over automated scanning
Findings should be reproducible and defensible
