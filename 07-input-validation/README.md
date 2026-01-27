# Input Validation

##  Purpose:
- Ensure that all user inputs are properly validated, sanitized, and handled securely to prevent injection and data manipulation attacks.

----

## Tools & Techniques:
- curl
- Manual payload testing
- Browser DevTools

----

## Methodology:
- Identify input fields and parameters
- Test boundary values
- Inject special characters
- Validate server-side enforcement
- Verify error handling

----

## Commands:
### Step 1:
- Parameter Injection:

curl "https://target.com/search?q=' OR 1=1--"

-----

### Step 2:
- Boundary Testing:

curl "https://target.com/api/user?id=9999999999"

----

### Step 3:
- Special Character Testing:

curl "https://target.com/comment?msg=<script>alert(1)</script>"

-------

 #### Output:
- Input validation gaps
- Injection vectors
- Error disclosure

----------

### Security Impact:
- Prevents injection attacks
- Reduces data corruption
- Improves application integrity
