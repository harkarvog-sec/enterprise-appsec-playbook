####  Network Exposure

## Purpose:
- Identify exposed ports, services, TLS configuration, and network security posture.

---

## Tools & Techniques:
- nc / netcat
- ss , lsof
- openssl 
- Firewall and routing analysis  

---

## Methodology:
- Enumerate open ports  
- Check TLS configuration  
- Identify exposed services  
- Document firewall rules and network access

---

## Commands:
### Step 1:
- Open Ports:

ss -tulnp
nc -vz target.com 443
nc -vz target.com 22

---

### Step 2:
- TLS Check:

openssl s_client -connect target.com:443

---

### Output:
- List of open ports and services
- TLS versions and cipher suites
- Firewall & routing insights

----

### Security Impact:
- Detects unnecessary exposure
- Prevents unauthorized access
- Guides secure network configuration
