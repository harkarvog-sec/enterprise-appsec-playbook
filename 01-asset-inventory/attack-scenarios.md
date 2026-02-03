# Asset Inventory – Attack Scenarios

## Overview

This document highlights realistic attack paths caused by incomplete or inaccurate asset inventories.

Most high-impact breaches begin with:
- forgotten assets
- undocumented services
- misclassified exposure
- unknown third-party dependencies

These scenarios focus on discovery-driven compromise, not exploitation of a single vulnerability.

All scenarios assume authorized assessment environments only.

---

## Scenario 1: Forgotten Subdomain Exposes Legacy Application

### Context
A legacy subdomain remains active but is no longer tracked in the asset inventory.
The application is unpatched and lacks modern security controls.

### Validation Commands

''bash'':

dig target.com any
host legacy.target.com
curl -I https://legacy.target.com

#### What This Validates

- Gaps in DNS and subdomain inventory
- Presence of abandoned or unsupported systems

#### Exploit Path:

- Attacker enumerates subdomains.
- Identifies legacy application.
- Exploits known vulnerabilities or weak authentication.

#### Impact:

- Unauthorized access to sensitive data
- Initial foothold into internal systems
- Reputational and compliance risk

##### Mitigation:

- Continuous DNS inventory
- Decommission unused assets
- Enforce ownership and lifecycle tracking

---

### Scenario 2: Shadow API Endpoint Bypasses Security Controls

#### Context
An internal API endpoint was deployed for testing but never documented or protected.
It lacks authentication and authorization checks.

#### Validation Commands:

curl https://api.target.com/v1/internal/debug

#### What This Validates:

- Undocumented API surface area
- Missing security controls on non-public endpoints

#### Exploit Path:

- Attacker discovers endpoint through enumeration.
- Directly accesses sensitive functionality.
- Bypasses frontend and access control layers.

#### Impact:

- Data exposure
- Privilege escalation
- Business logic abuse

#### Mitigation:

- API inventory tied to CI/CD
- Block undocumented endpoints
- Enforce authentication by default

----

### Scenario 3: Exposed Cloud Resource Due to Missing Inventory

### Context
A cloud storage resource exists outside documented infrastructure.
It is publicly accessible due to default permissions.

#### Validation Commands (Example):

curl https://public-storage.cloudprovider.com/bucket-name

#### What This Validates:

- Incomplete cloud asset visibility
- Misconfigured exposure

#### Exploit Path:

- Attacker scans cloud namespaces.
- Finds exposed storage or service.
- Downloads or modifies sensitive data.

#### Impact:

- Data breach
- Regulatory violations
- Loss of customer trust

#### Mitigation:

- Cloud-native asset discovery
- Least privilege defaults
- Continuous exposure monitoring

----

### Scenario 4: Overlooked Internal Service Enables Lateral Movement

#### Context
An internal service is not included in the asset inventory.
It trusts network location and lacks authentication.

#### Validation Commands:

curl http://internal-service.local/admin/status

#### What This Validates:

- Implicit trust assumptions
- Missing internal service inventory

#### Exploit Path:

- Attacker compromises a low-privilege host.
- Discovers undocumented internal service.
- Moves laterally within the environment.

#### Impact:

- Expanded blast radius
- Escalation to critical systems
- Difficult incident containment

#### Mitigation:

- Inventory all internal services
- Enforce service-to-service authentication
- Monitor internal traffic

----

### Scenario 5: Third-Party Integration Becomes an Attack Vector

####Context
A third-party API integration is undocumented.
Its credentials are shared across services.

#### Validation Commands

grep -R "THIRD_PARTY_API_KEY" .

#### What This Validates

- Untracked external dependencies
- Weak secrets management

#### Exploit Path:

- Attacker finds leaked or reused API keys.
- Abuses third-party service trust.
- Gains indirect access to internal data.

#### Impact:

- Supply chain compromise
- Data leakage
- Loss of partner trust

#### Mitigation:

- Maintain dependency inventory
- Rotate and scope credentials
- Monitor third-party access patterns

----

#### Summary:
- Asset Gap	Risk Introduced	Impact
- Forgotten subdomains	Initial foothold	Data breach
- Undocumented APIs	Control bypass	Privilege escalation
- Untracked cloud assets	Public exposure	Regulatory violation
- Unknown internal services	Lateral movement	Full environment compromise
- Untracked third-party services	Supply chain attack	Indirect data exposure

---

#### Key Takeaway:

Asset inventory failures do not create theoretical risk —
they create real, repeatable attack paths.

#### Attackers win by finding:

- what you forgot
- what you stopped tracking
- what no one owns
