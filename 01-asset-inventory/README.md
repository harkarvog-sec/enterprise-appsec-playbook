### Asset Inventory

## Purpose:
- Identify and document all assets within the target environment, including domains, subdomains, IP addresses, servers, and services.  
- This provides a foundation for all subsequent security testing and vulnerability management.

---

## Tools & Techniques:
- dig, nslookup, host - (DNS enumeration)  
- curl - (check service availability)  
- ping - (host live check)  
- nc/netcat - (port validation)  
- traceroute - (network path)  
- Spreadsheet or CSV -  (documentation)  

---

## Methodology:
- DNS Enumeration – List all domains and subdomains.
- Host Availability – Check which hosts are live.  
- Service Identification – Confirm which services/ports are exposed.  
- Network Path Analysis – Map network routes and infrastructure.  
- Document Everything – Maintain a CSV or spreadsheet with all findings.  

---

##### Commands:
# Step 1:
- DNS Lookup:

dig target.com any
nslookup target.com
host target.com

# Finds all domain info, mail servers, and name servers.

---

## Step 2: 
- Check Host Availability:

ping target.com

curl -I https://target.com

# Confirms if hosts are live and reachable.

----

### Step 3:
- Service / Port Validation:

nc -vz target.com 80
nc -vz target.com 443

# Checks which ports/services are exposed.

---

## Step 4:
- Network Path:
- 
traceroute target.com

# Maps network hops and connectivity paths.

---

### Step 5:
- Document Findings:
  
# Export results to CSV:

echo "Host,IP,Port,Status" > assets.csv
echo "example.com,93.184.216.34,80,open" >> assets.csv

# Maintains a clear, professional record of all assets.

----

# Output:
- List of domains & subdomains
- Live hosts verified
- Open ports/services identified
- Network infrastructure map
- CSV or spreadsheet inventory

----

### Security Impact:
- Establishes a complete asset baseline
- Reduces blind spots in testing
- Enables accurate vulnerability assessment
- Supports security reporting and remediation planning
