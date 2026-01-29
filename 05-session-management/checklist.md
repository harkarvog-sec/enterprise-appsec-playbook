# Session Management Testing Checklist

A structured checklist for validating session handling across web, API, and mobile clients. Each item should be verified manually or with controlled tools in authorized environments.

---

## 1. Session ID Properties
[ ] Session IDs are long, random, and unpredictable  
[ ] No sequential or guessable identifiers  
[ ] Unique per user session  
[ ] No sensitive or user-identifiable information embedded in the token

---

## 2. Session Invalidation
[ ] Sessions destroyed immediately on logout  
[ ] Sessions invalidated after password change  
[ ] Idle timeout enforced  
[ ] Absolute timeout enforced  
[ ] Tokens cannot be reused after invalidation

---

## 3. Cookie Security Attributes
[ ] Secure flag set (HTTPS only)  
[ ] HttpOnly flag set (inaccessible to client-side scripts)  
[ ] SameSite flag set (Strict or Lax as appropriate)  
[ ] Session tokens not exposed in URLs, logs, or local storage

---

## 4. Token-Based Authentication
[ ] JWT/OAuth tokens validated for signature, issuer, and claims  
[ ] Tokens expire correctly and are rotated when required  
[ ] Refresh tokens rotated and invalidated after use  
[ ] Token scope and audience enforced

---

## 5. Session Fixation
[ ] Session ID regenerated immediately after login  
[ ] Pre-authentication sessions cannot be reused after login  
[ ] No predictable session IDs prior to authentication

---

## 6. Session Concurrency
[ ] Multiple sessions handled according to policy (allow, block, expire)  
[ ] Logout from one session affects all other sessions if required  
[ ] Session termination triggers proper invalidation across devices

---

## 7. Logging & Monitoring
[ ] Failed session-related operations are logged  
[ ] Unusual session reuse attempts trigger alerts  
[ ] Session events are visible for audit and incident response

---

# Notes: 
Checklists should be repeated for web, API, and mobile clients 
Document evidence for each check (requests, responses, screenshots)  
Testing should be conducted only in authorized environments
