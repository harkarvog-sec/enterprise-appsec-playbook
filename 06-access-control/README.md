# Access Control

## Purpose:
- Validate role-based access control, authorization checks, and privilege management.

--------

## Tools & Techniques:
- curl  
- HTTP requests analysis  
- Role and permissions enumeration  

-------

## Methodology:
- Attempt access to restricted endpoints  
- Check IDOR (Insecure Direct Object References)  
- Validate API access permissions  

---

## Commands:
### Step 1:
- Admin Access Test:

curl https://target.com/admin

-------

### Step 2:
- API Object Access:

curl https://target.com/api/admin/users

------

### Output:
- Unauthorized access attempts
- Privilege escalation possibilities
- Access control gaps

------

### Security Impact:
- Prevents unauthorized access
- Reduces risk of data leakage
- Supports least privilege enforcement
