# Access Control Testing Checklist

This checklist provides a structured approach to validate access control mechanisms across web, API, and multi-tenant applications. Each item should be manually verified and documented.

---

## Horizontal Access

[ ] Test object ID enumeration  
[ ] Test user ID enumeration  
[ ] Test URL or parameter tampering  

## Vertical Access

[ ] Attempt admin-only functions as a standard user  
[ ] Test hidden UI or API endpoints  

## Role & Attribute Enforcement

[ ] Verify roles and permissions  
[ ] Attempt privilege escalation via attribute modification  

## Multi-Tenant

[ ] Confirm tenant data isolation  
[ ] Test cross-tenant API access  

## Documentation

[ ] Record evidence of all access control bypasses  
[ ] Map findings to user roles and endpoints  

---

## Notes

Repeat the checklist for web, API, and mobile clients
Document request/response evidence for each check  
Perform all tests in *authorized environments only
