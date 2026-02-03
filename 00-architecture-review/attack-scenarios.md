# Architecture Review – Attack Scenarios

Overview:

- This document highlights realistic abuse paths and design-level risks discovered during architecture review.
Focus is on systemic impact, not endpoint-level vulnerabilities.

- All scenarios assume authorized assessment environments only.

---

### Scenario 1: Over-Trusted Internal Services

####Context:
Internal microservices assume requests from other services are trustworthy.

#### Validation Commands
- Identify internal service endpoints

curl -k https://internal-api.service.local/health

- Attempt access without service authentication

curl -k https://internal-api.service.local/admin/config

#### What This Validates:
- Whether internal services enforce authentication
- Whether network location is incorrectly treated as trust

#### Exploit Path:
- Compromise a low-privilege service account.
- Send crafted requests to higher-privileged services.
- Access or manipulate sensitive data without further authentication.

#### Impact:
- Unauthorized access to critical data
- Potential privilege escalation across services

#### Mitigation:
- Enforce service-to-service authentication and authorization
- Limit service account privileges
- Monitor anomalous internal traffic

---

### Scenario 2: Missing Authorization Between Services

#### Context:
PIs expose sensitive endpoints internally, relying on perimeter controls.

#### Validation Commands
- Use a low-privilege token to access sensitive endpoints

curl -H "Authorization: Bearer LOW_PRIV_TOKEN" \
     https://api.internal.local/admin/users

#### What This Validates:
- Absence of authorization checks at service boundaries
- Reliance on upstream enforcement only

#### Exploit Path:
- Attacker compromises a service within the network.
- Calls API endpoints without any authorization checks.

#### Impact:
- Lateral movement
- Data exfiltration
- Service disruption

#### Mitigation:
- Implement role-based or attribute-based authorization between services
- Use tokens or mutual TLS for service authentication
- Audit internal API calls

----

### Scenario 3: Misconfigured Cloud IAM Roles

#### Context:
Cloud services (AWS/Azure) assigned broad permissions by default.

#### Validation Commands (AWS Example)
- Identify active IAM role:
  
aws sts get-caller-identity

- List permissions available to the role:

aws iam list-attached-role-policies --role-name AppServiceRole

#### What This Validates:
- Excessive permissions
- Violation of least privilege

#### Exploit Path:
- Attacker gains access to a compromised service account.
- Uses default IAM permissions to escalate privileges across cloud resources.

#### Impact:
- Full tenant compromise
- Data exposure or deletion
- Service availability impact

#### Mitigation:
- Apply principle of least privilege
- Audit IAM roles regularly
- Monitor unusual API calls

----

### Scenario 4: Weak or Missing Audit and Detection

#### Context:
Critical actions are not logged or monitored.

#### Validation Commands
- Perform sensitive action and observe logging

curl -X POST https://api.service.local/admin/reset-password \
     -H "Authorization: Bearer VALID_TOKEN"


Then verify:
- Application logs
- SIEM ingestion
- Alerting behavior

#### What This Validates:
- Logging coverage
- Detection gaps
- Incident response readiness

#### Exploit Path
- Attacker exploits a misconfigured internal service.
- Performs actions without triggering alerts.

#### Impact:
- Extended dwell time
- Difficulty in incident detection and response

#### Mitigation:
- Ensure all critical operations are logged
- Integrate logs into SIEM/monitoring pipeline
- Alert on anomalous patterns

---

### Scenario 5: Implicit Trust in Upstream Identity Providers

#### Context:
- Systems rely solely on upstream identity assertions without internal validation.

##33 Validation Commands
- Replay or modify identity token claims (authorized testing)

curl -H "Authorization: Bearer MODIFIED_TOKEN" \
     https://service.local/privileged/resource

#### What This Validates:
- Token validation enforcement
- Scope and audience verification

#### Exploit Path:
Attacker manipulates token or identity assertion.
Gains unauthorized access to downstream services.

#### Impact:
- Escalation of privilege
- Unauthorized access to sensitive resources

#### Mitigation:
- Validate identity tokens internally
- Apply strict token expiration and scope checks
- Monitor unusual authentication patterns

#### Summary:
| Risk Area	                            | Impact	                                  | Recommended Controls                         |
|---------------------------------------|-------------------------------------------|----------------------------------------------|
| Over-trusted internal services	      | Unauthorized data access	                | Service-to-service auth, least privilege     |
| Missing authorization	                | Lateral movement	                        | Internal API auth, RBAC/ABAC                 | 
| Misconfigured cloud IAM	              | Full tenant compromise	                  | Principle of least privilege, IAM audits     |
| Weak auditing	                        | Delayed detection	                        | Logging, SIEM alerts                         |
| Implicit trust in identity	          | Privilege escalation	                    | Internal token validation, scope enforcement |

---

# Key Takeaway

These scenarios demonstrate that architecture flaws are validated through behavior, not just documentation.

Commands are used to:
- Confirm trust assumptions
- Validate control placement
- Measure blast radius
