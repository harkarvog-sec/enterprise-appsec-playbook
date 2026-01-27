# Dependency Security

##  Purpose:
- Identify vulnerable third-party libraries.

-------

## Tools & Techniques:
- package managers
- Manual CVE review

----

# Methodology:
- Enumerate dependencies
- Check versions
- Review CVEs
- Patch updates

-----

## Commands:
# Step 1:
- List Packages:

pip freeze
npm list

------

### Step 2 :
- Check Versions:

pip show requests

-------

 ### Output:
- Vulnerable libraries
- Outdated packages

----------

#Security Impact:
- Reduces supply-chain risk
- Improves stability
