# Network Exposure – Attack Scenarios

Overview:
This document outlines realistic attack scenarios caused by excessive, misconfigured, or undocumented network exposure.

#### The focus is on:
- Internet-facing services that should be internal
- Weak network segmentation
- Over-reliance on perimeter defenses
- Flat internal networks enabling lateral movement

All scenarios assume authorized testing environments only.

---

### Scenario 1: Unintended Internet-Exposed Internal Service

Context:
A service intended for internal use is exposed directly to the internet due to firewall or security group misconfiguration.

#### Validation Commands:

# Check DNS and exposure:

dig internal-api.target.com


# Test reachability:

curl -I https://internal-api.target.com


# Check open ports:

nc -vz internal-api.target.com 443

#### What This Validates:
- Whether internal services are externally reachable
- Missing network-layer access controls

#### Exploit Path:
- Attacker discovers exposed internal service
- Service lacks strong authentication
- Sensitive internal functionality accessed

#### Impact:
- Unauthorized data access
- Bypass of perimeter security controls

#### Mitigation:
- Restrict internal services to private networks
- Enforce network-level allowlists
- Monitor exposure continuously

---

### Scenario 2: Open Management Ports Exposed to the Internet

Context:
Administrative services (SSH, RDP, admin consoles) are accessible from the internet.

#### Validation Commands

Test common management ports:

nc -vz target.com 22
nc -vz target.com 3389

#### What This Validates

- Exposure of high-risk management interfaces

#### Exploit Path

- Attacker brute-forces or uses leaked credentials
- Gains direct system access

#### Impact

- Full host compromise
- Persistence and lateral movement
- Mitigation
- Disable public access to management ports
- Enforce VPN or bastion hosts
- Apply MFA and IP restrictions

---

### Scenario 3: Flat Internal Network Enables Lateral Movement

Context:
Internal services communicate freely without segmentation or filtering.

#### Validation Techniques:

- Review network diagrams
- Test access between internal services from a low-privilege host

Example:

curl http://internal-db.service.local:9200

#### What This Validates:

- Lack of internal segmentation
- Over-trusting internal network traffic

#### Exploit Path

- Attacker compromises one internal service
- Freely scans and accesses others
- Escalates privileges across environment

#### Impact

- Broad internal compromise
- Increased blast radius

#### Mitigation

- Network segmentation (VPCs, subnets)
- Zero Trust networking principles
- Service-to-service authentication

---

#### Scenario 4: Cloud Security Group Allows Excessive Inbound Traffic

Context:
Cloud firewall rules allow unrestricted inbound access (e.g., 0.0.0.0/0).

#### Validation Commands (AWS Example)

List security groups:

aws ec2 describe-security-groups


Review inbound rules:

aws ec2 describe-security-groups --group-ids sg-xxxx

#### What This Validates

- Overly permissive network rules
- Missing least-privilege enforcement

#### Exploit Path

- Attacker scans cloud IP ranges
- Identifies exposed services
- Exploits vulnerable applications

#### Impact

- Service compromise
- Cloud resource abuse

#### Mitigation

- Restrict inbound rules to known sources
- Regularly audit security groups
- Use private endpoints where possible

#### Scenario 5: No Rate Limiting or Network-Level Protection

Context:
Public services lack rate limiting, WAF, or DDoS protections.

#### Validation Commands

Send repeated requests:

for i in {1..100}; do curl https://api.target.com/login; done

#### What This Validates

- Absence of network-layer abuse protections

#### Exploit Path

- Attacker performs brute-force or flooding attack
- Service degradation or account compromise

#### Impact

- Denial of service
- Credential attacks

#### Mitigation

- Enable WAF and rate limiting
- Monitor abnormal traffic patterns
- Apply throttling at network and application layers

---

### Summary Table

| Exposure Issue	               | Impact	                   | Root Cause	               | Recommended Controls |
|--------------------------------|---------------------------|-------------------------- |----------------------|
| Internal services exposed	     | Unauthorized access	     | Weak firewall rules	     | Network isolation    |
| Open management ports	         | Host compromise	         | Poor access control	     | Bastion + VPN        |
| Flat internal network	         | Lateral movement	         | No segmentation	         | Zero Trust           |
| Permissive cloud rules	       | Cloud compromise	         | Over-broad SGs	           | Least privilege      |
| No traffic controls	           | DoS / brute-force	       | Missing protections	     | WAF, rate limiting   |

---

#### Key Takeaway

- Network exposure defines the true attack surface.
- Strong AppSec programs:
- Treat the network as hostile
- Minimize exposure by default
- Assume breach and limit blast radius
  
**Commands in this module validate real reachability, not just documented intent.**
