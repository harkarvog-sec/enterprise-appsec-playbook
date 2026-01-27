# API Security

## Purpose:
- Secure REST and GraphQL APIs against unauthorized access and abuse.

-----

## Tools & Techniques:
- curl
- JSON testing
- Header inspection

-----

## Methodology:
- Identify API endpoints
- Validate authentication
- Test authorization
- Check rate limiting
- Validate schema

----

##  Commands:
# Step 1:
- API Enumeration:

curl https://target.com/api/v1/users

--------

### Step 2:
- Auth Bypass:

curl https://target.com/api/admin -H "Authorization: Bearer fake"

-----

## Step 3:
- Rate Test:

for i in {1..50}; do curl https://target.com/api/login; done

--------

#### Output:
- Broken auth
- IDOR
- Excessive data exposure

-------

#### Security Impact:
- Protects backend services
- Prevents data leakage
- Improves API governance
