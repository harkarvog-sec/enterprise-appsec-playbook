# CI/CD Security Remediation Guidance

---

## Repository & Access Controls

- Enforce least privilege for repository access
- Restrict write access to trusted users only
- Enable branch protection with required reviews
- Limit permissions of automation and bot accounts

---

## Pipeline Hardening

- Avoid dynamic script execution
- Validate all pipeline inputs
- Use fixed, versioned actions and dependencies
- Restrict pipeline modification rights

---

## Secrets Management

- Store secrets in dedicated secret managers
- Prevent secrets from appearing in logs
- Rotate exposed credentials immediately
- Avoid passing secrets via command-line arguments

---

## Runner & Agent Security

- Prefer dedicated runners for sensitive projects
- Isolate jobs and prevent cross-job access
- Block access to cloud metadata services
- Harden self-hosted runners as production assets

---

## Artifact & Supply Chain Protection

- Sign and verify build artifacts
- Prevent artifact reuse across trust boundaries
- Restrict write access to artifact repositories
- Monitor for unexpected artifact changes

---

## Deployment Security

- Enforce approval gates for production deployments
- Separate deployment credentials by environment
- Log and monitor all deployment actions
- Regularly review rollback and emergency access

---

## Continuous Improvement

- Periodically audit CI/CD configurations
- Monitor pipeline activity for abuse
- Incorporate CI/CD findings into threat models
