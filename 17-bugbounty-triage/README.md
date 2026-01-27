# Bug Bounty Triage

## Purpose:
- Validate and manage external vulnerability reports.

---

##  Tools & Techniques:
- HackerOne
- curl
- Reproduction testing

----

## Methodology:
- Validate report
- Reproduce
- Assess severity
- Assign fix

----

## Commands:
# Step 1:
- Reproduce:

curl https://target.com/vuln

------

##Step 2:
- Validate Impact:

curl -v https://target.com/private

-----

### Output:
- Verified vulnerabilities
- Risk ratings

----

## Security Impact:
- Improves external testing
- Reduces false positives
