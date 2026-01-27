# Authentication Testing

## Purpose:
- Validate login mechanisms, password policies, and authentication controls.

---

## Tools & Techniques:
- curl  
- HTTP clients  
- Browser DevTools  

---

## Methodology:
- Test login workflows  
- Validate password policy  
- Review recovery mechanisms  
- Assess brute-force protection  
- Check MFA enforcement  

-----------

## Commands:
### Step 1:
- Login Validation:

curl -X POST https://target.com/login \
-d "username=test&password=test"

----

### Step 2:
- Password Reset:
- 
curl -I https://target.com/reset-password

----

### Step 3:
- Brute Force Testing:
- 
for i in {1..10}; do
  curl https://target.com/login
done

---------

### Output:
- Authentication weaknesses
- Weak password policies
- MFA gaps

------

#### Security Impact:
- Prevents account takeover
- Reduces credential abuse
- Improves identity security
