# CI/CD Security Testing Checklist

---

## Repository & Access Control

- [ ] Review repository access permissions
- [ ] Identify users and service accounts with write access
- [ ] Verify branch protection rules
- [ ] Test pull request and fork restrictions
- [ ] Review automation and bot account privileges

---

## Pipeline Configuration

- [ ] Review CI/CD configuration files
- [ ] Identify scripts executed during build and deploy
- [ ] Check for unsafe shell usage
- [ ] Verify pipeline integrity controls

---

## Secrets Management

- [ ] Search for hardcoded secrets in repositories
- [ ] Inspect pipeline logs for secret leakage
- [ ] Verify secret masking in logs
- [ ] Test exposure via failed or debug jobs
- [ ] Review environment variable handling

---

## Runner & Agent Security

- [ ] Identify shared vs dedicated runners
- [ ] Assess job isolation between builds
- [ ] Test filesystem access from runners
- [ ] Test access to cloud metadata services
- [ ] Review permissions of self-hosted runners

---

## Artifacts & Supply Chain

- [ ] Identify artifact storage locations
- [ ] Test artifact reuse across pipelines
- [ ] Verify integrity controls (hashing, signing)
- [ ] Test post-build modification risks

---

## Deployment Controls

- [ ] Review deployment approval mechanisms
- [ ] Test environment separation (dev/staging/prod)
- [ ] Verify deployment trigger permissions
- [ ] Review rollback and audit logging

---

## Documentation

- [ ] Capture pipeline configurations
- [ ] Record evidence of exploitation paths
- [ ] Map findings to business impact
