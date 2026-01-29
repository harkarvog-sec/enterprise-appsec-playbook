# Access Control Attack Scenarios

## 1. Horizontal Privilege Escalation

Description:
A user accesses resources of another user of the same privilege level.  

Attack Flow:
1. Authenticate as User A  
2. Change object IDs in requests to access User B’s data  
3. If access succeeds, report as horizontal access control bypass  

Impact:
Data leakage, privacy violations

---

## 2. Vertical Privilege Escalation

Description: Low-privilege users access admin or privileged functions.  

Attack Flow:
1. Authenticate as standard user  
2. Attempt restricted operations via APIs, UI, or hidden endpoints  
3. If successful, attacker gains higher privileges  

Impact:
Administrative access, resource manipulation, business disruption

---

## 3. Role Misconfiguration

Description:
Users inherit unintended roles or permissions, or attribute-based access is misapplied.  

Attack Flow:
1. Identify user roles and permissions  
2. Attempt to escalate privileges by modifying attributes, parameters, or role identifiers  
3. Verify if unauthorized actions are permitted  

Impact:
Unauthorized access, privilege escalation, operational risk

---

## 4. Multi-Tenant Bypass

Description:
Users from one tenant access another tenant’s data due to weak tenant isolation.  

Attack Flow:
1. Authenticate as a user in Tenant A  
2. Attempt access to Tenant B’s objects or endpoints  
3. Record any successful access or data leakage  

Impact:
Cross-tenant data exposure, compliance violations, reputational risk

---

## Notes

Test both UI and API endpoints for all attack scenarios  
Document all successful unauthorized access attempts with request/response evidence  
Focus on logic flaws, not just missing technical controls
