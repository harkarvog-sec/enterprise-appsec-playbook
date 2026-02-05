# Network Exposure – Testing Methodology

Overview:

This methodology describes a structured approach to identifying network-exposed assets, mapping network reachability, and assessing the potential attack surface.  
The focus is on understanding both external and internal exposure, ensuring that critical assets are identified and prioritized for remediation.

All activities assume authorized testing environments only.

---

## Guiding Principles

- External and internal network exposure must be considered together  
- Automation supports, but does not replace, manual verification  
- Discover shadow or forgotten infrastructure that may increase risk  
- Validate firewalls, VPNs, and segmentation controls
- Document everything in a structured inventory

---

## Step 1: Define Scope

Determine which network segments, hosts, and services are in scope:

- Public IPs and DNS domains  
- Internal subnets and VLANs  
- Cloud-hosted services and endpoints  
- VPN, DMZ, and hybrid network zones

Deliverable: Clear scope definition to avoid blind spots

---

## Step 2: External Network Discovery

- Identify all externally reachable hosts and services

### Commands

'''bash
# Ping known domains/IPs
ping target.com

# Check HTTP/HTTPS availability
curl -I https://target.com

# Port scan common services
nc -vz target.com 80
nc -vz target.com 443

# Discover open TCP ports (authorized only)
nmap -Pn target.com

#### What this validates:

- Public-facing hosts and endpoints
- Open ports and services
- TLS/HTTPS configuration
- Potential attack vectors for external attackers

## Deliverable:
External host and service inventory

---

#### Step 3: Internal Network Discovery

- Map internal network segments, live hosts, and services

### Commands:

# Ping internal hosts
ping 10.0.0.5

# Test service availability
nc -vz 10.0.0.5 22
nc -vz 10.0.0.5 443

# Trace network path
traceroute 10.0.0.5

# List connected devices (example for authorized LAN)
arp -a

#### What this validates:

- Internal host reachability
- Network segmentation and trust boundaries
- Shadow services or unmanaged hosts

### Deliverable: 
Internal network map with reachable hosts

---

#### Step 4: Firewall and Segmentation Verification

- Validate whether firewall rules, ACLs, and segmentation controls are effective

### Commands:

# Test restricted port access from different network segments
nc -vz 10.0.1.10 3306

# Verify VPN access limitations
curl --interface tun0 https://internal-service.local

#### What this validates:

- Enforcement of network segmentation
- Restricted access between zones
- Potential lateral movement paths

#### Deliverable:
Firewall and segmentation validation report

---

### Step 5: Cloud and Hybrid Exposure

- Identify cloud-hosted endpoints and services

#### Commands / Tools:

# List cloud instances and IPs (AWS example)
aws ec2 describe-instances --query "Reservations[*].Instances[*].[InstanceId,PublicIpAddress,PrivateIpAddress]"

# Check security groups / network ACLs
aws ec2 describe-security-groups

#### What this validates:

- Publicly exposed cloud assets
- Misconfigured security groups or network rules
- Overly permissive access

#### Deliverable:
Cloud network exposure map

---

### Step 6: Reporting & Risk Assessment

- Document all findings in a structured format (CSV, spreadsheet, CMDB)

Example CSV format:

Host, IP, Network Zone, Open Ports, Service, Exposure, Owner
webapp.target.com, 203.0.113.10, DMZ, 80, HTTP, External, Web Team
db.internal.local, 10.0.1.5, Internal, 3306, MySQL, Internal, DB Team

### Deliverable: 
Complete network exposure inventory with risk classification

---

### Key Takeaways:

- Network exposure mapping identifies critical entry points
- Validates segmentation and access controls
- Provides data to prioritize remediation and vulnerability scanning
- Supports enterprise-level threat modeling and security reporting

---

### Notes:

- Re-run scans after network changes or new deployments
- Use authorized testing only; never scan external or third-party networks without permission
- Combine automated tools (nmap, cloud APIs) with manual verification for accuracy
