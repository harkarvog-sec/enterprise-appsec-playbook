# Asset Inventory – Checklist

Purpose:
Provide a concise, repeatable set of steps to build and validate a complete enterprise-grade asset inventory. Ensures consistency, reduces blind spots, and supports risk-based vulnerability management.

Notes:
Only perform on authorized systems.

---

## Pre-Inventory Preparation

- [ ] Define scope: applications, APIs, services, databases, cloud, CI/CD, third-party integrations  
- [ ] Gather system diagrams, deployment docs, and existing inventories  
- [ ] Identify critical data and business context for assets  
- [ ] Collect credentials or read-only access for enumeration where needed  

---

## Domain & DNS Enumeration

- [ ] List all domains and subdomains  
- [ ] Validate DNS records (A, AAAA, MX, TXT, CNAME)  
- [ ] Identify legacy or forgotten subdomains  
- [ ] Document all findings in inventory spreadsheet or CSV  

---

## Host Availability & Exposure

- [ ] Ping or curl all discovered hosts  
- [ ] Record reachable hosts  
- [ ] Note TLS/SSL presence and certificate validity  
- [ ] Flag unexpected or shadow hosts  

---

## Service & Port Identification

- [ ] Scan for open ports/services on all hosts  
- [ ] Validate against expected configuration  
- [ ] Identify non-standard services or versions  
- [ ] Document all host-service mappings  

---

## API & Application Interface Mapping

- [ ] Review API documentation (OpenAPI/Swagger)  
- [ ] Inspect front-end applications or mobile clients  
- [ ] Map endpoints, parameters, and authentication requirements  
- [ ] Note undocumented or hidden APIs  

---

## Cloud & Infrastructure Asset Identification

- [ ] List compute instances, containers, serverless functions  
- [ ] Identify storage (databases, object storage, volumes)  
- [ ] Map network resources (VPCs, load balancers, gateways)  
- [ ] Document IAM roles, service accounts, permissions  

---

## Dependency & Third-Party Mapping

- [ ] Identify external APIs, SaaS integrations, and libraries  
- [ ] Record versioning and update status  
- [ ] Map trust relationships and potential exposure paths  

---

## Asset Classification & Risk Context

- [ ] Record business function per asset  
- [ ] Capture data sensitivity and exposure (public/internal/restricted)  
- [ ] Identify owner or responsible team  
- [ ] Note authentication and authorization requirements  

---

## Documentation & Inventory Maintenance

- [ ] Maintain all findings in structured inventory (CSV, spreadsheet, CMDB)  
- [ ] Version control inventory for tracking changes  
- [ ] Schedule regular reviews and updates  
- [ ] Integrate with vulnerability management or reporting workflows  

---

## Key Takeaways

- Asset inventory is foundational for AppSec 
- Incomplete inventory = blind spots for attackers  
- Continuous updates prevent shadow IT and forgotten systems  
- Provides actionable data for risk-based remediation and reporting
