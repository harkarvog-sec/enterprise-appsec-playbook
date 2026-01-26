#### Architecture Review
## Purpose:
-  the application architecture, system components, data flows, and interdependencies.  
- This allows for effective security testing and threat modeling.

---

## Tools & Techniques:
- curl, traceroute, dig 
- Browser DevTools  
- Network diagrams  
- Cloud documentation

---

## Methodology:
- Review system diagrams and documentation  
- Identify components (frontend, backend, API, DB, cloud)  
- Map data flows and trust boundaries  
- Identify security controls and gaps  

---

## Commands:

### Step 1:
# API Discovery:
curl https://target.com/.well-known/openapi.json

### Step 2:
# Health Endpoints:
curl https://target.com/actuator/health

### Step 3:
# Network Flow:
traceroute target.com

---

### Output:
- Complete architecture map
- Service and component list
- Data flow diagrams
- Potential security gaps

---

### Security Impact:
- Supports threat modeling
- Reduces blind spots
- Guides testing scope
- Improves security posture
