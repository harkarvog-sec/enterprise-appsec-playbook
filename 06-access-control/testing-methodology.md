# Access Control Testing Methodology

This document provides a manual, structured approach to testing access controls in enterprise applications.

---

## 1. Horizontal Access Control

### Objective
Identify whether a user can access another user’s data.

### Method
Log in as a regular user
Attempt to access data belonging to another user via:
  - URL manipulation  
  - API parameter tampering  
  - Object identifiers

### Example Command

curl -X GET "https://target.com/api/users/123" -b "session=<SESSION_ID>"


#### 2. Vertical Access Control

## Objective
Check if lower-privileged users can perform higher-privilege actions.

## Method
Attempt admin-only operations as a standard user
Test UI buttons, APIs, and hidden endpoints

### Example Command

curl -X POST "https://target.com/api/admin/delete-user/456" -b "session=<SESSION_ID>"


### 3. Role & Attribute Enforcement
Verify roles, groups, and permissions are correctly applied
Attempt to escalate roles or access restricted attributes


#### 4. Multi-Tenant Isolation
Test whether one tenant can access another tenant’s data
Check database and API access patterns


## Notes
Document every unauthorized access attempt
Test both UI and API endpoints
Focus on logic flaws that automated tools may miss
