### Attack Surface Mapping

## Purpose:
- Identify all accessible endpoints, pages, APIs, and entry points exposed by the application to understand the attack surface.

---

## Tools & Techniques:
- curl
- wget
- Browser DevTools
- Linux utilities

---

## Methodology:
- Enumerate publicly available paths
- Identify hidden or undocumented endpoints
- Review client-side routes
- Analyze exposed files
- Document all entry points

------

## Commands:

### Step 1:
- Robots & Sitemap Review

curl https://target.com/robots.txt
curl https://target.com/sitemap.xml

----

#### Step 2:
- Website Mirroring:

wget --mirror https://target.com

-----

#### Step 3:
- Header Analysis:
  
curl -I https://taarget.com

------

### Step 4:
- Cookie Inspection:

curl -v https://targeet.com

---------

### Output:
- Endpoint inventory
- API route list
- Admin interfaces
- Testing targets

------

### Security Impact:
- Reduces blind spots
- Prevents forgotten endpoints
- Improves vulnerability coverage
- Strengthens perimeter defense
