# CI/CD Pipeline Security

CI/CD pipelines are a high-value target for attackers because they sit at the intersection of source code, credentials, infrastructure, and deployment.
Compromise of the pipeline often results in full application or cloud takeover. 
This module documents a manual, attacker-driven approach to assessing CI/CD pipeline security in enterprise environments, focusing on trust boundaries, credential exposure, and unsafe automation.

---

## Scope

CI/CD security testing in this playbook includes:
- Source code repository access controls
- Pipeline configuration and secrets handling
- Build and deployment permissions
- Artifact integrity and supply chain risks
- Environment separation (dev, staging, prod)
- Third-party integrations and runners

---

## Objectives

The objectives of this phase are to determine:
- Whether attackers can inject malicious code or artifacts
- Whether secrets can be extracted from pipelines
- Whether pipeline permissions enable privilege escalation
- Whether deployments can be triggered or modified without authorization

---

## Outcome

Successful testing demonstrates:
- Whether CI/CD trust boundaries are enforced
- Whether secrets and credentials are adequately protected
- Whether the pipeline can be abused to compromise production systems
