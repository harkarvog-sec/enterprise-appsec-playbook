# Session Management

## Purpose:
- Ensure secure session creation, handling, and termination.

------------

## Tools & Techniques:
- curl  
- Cookies and headers analysis  
- Session token validation  

--------

## Methodology:
- Inspect cookies (Secure, HttpOnly, SameSite)  
- Check session expiration  
- Test session fixation  
- Validate token revocation  

--------

## Commands:
# Step 1 :
- Inspect Cookies:

curl -v https://target.com/login

---------

### Step 2:
- Session Reuse:

curl -b cookies.txt https://target.com/profile

-----------

#### Step 3:
- Session Creation:

curl -c cookies.txt https://target.com/login

--------

### Output:
- Session cookie flags
- Token lifespan
- Fixation vulnerabilities

--------

### Security Impact:
- Prevents session hijacking
- Ensures secure session lifecycle
- Strengthens authentication layer
