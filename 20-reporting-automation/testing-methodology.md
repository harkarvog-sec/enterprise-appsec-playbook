# Reporting Automation Testing Methodology

This document describes the methodology used to validate the accuracy, reliability, and security impact of automated security reporting workflows.

The objective is to ensure that reporting automation produces high-signal, trustworthy outputs that can be consumed by engineering, security leadership, and compliance stakeholders.

---

## 1. Validate Finding Ingestion

### Objective
Ensure findings from multiple sources are ingested correctly and consistently.

### Manual Testing Steps
- Ingest findings from:
  - Manual penetration testing
  - SAST / DAST tools
  - Cloud security tools
  - Vulnerability scanners (e.g., Rapid7)
- Confirm required fields are populated:
  - Title
  - Asset
  - Evidence
  - Severity
  - Source
 
Manual commands / checks:

# Example: Insert a dummy finding via API to test ingestion

curl -X POST https://reporting.target.com/api/findings \
-H "Authorization: Bearer <API_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
  "title": "Test Vulnerability",
  "asset": "test-app.target.com",
  "severity": "Medium",
  "evidence": "curl -I https://test-app.target.com"
}'

- Verify it appears in the system.
- Confirm normalized fields populated correctly.

### Validation Checks
- No data truncation
- No missing critical fields
- No duplication of identical findings

---

## 2. Normalization & Deduplication Testing

### Objective
Verify that findings are normalized into a consistent schema and duplicates are handled correctly.

### Manual Testing Steps
- Submit multiple findings describing the same issue from different sources
- Validate normalization of:
  - Severity labels
  - Asset identifiers
  - Vulnerability categories

Manual commands / checks:

# Submit same vulnerability from two sources

curl -X POST https://reporting.target.com/api/findings \
-d '{...}' # Source A
curl -X POST https://reporting.target.com/api/findings \
-d '{...}' # Source B

# Check API output to see if the system deduplicates

curl https://reporting.target.com/api/findings?title="Test Vulnerability"

- Confirm merged entries, source attribution preserved.

### Validation Checks
- Duplicate findings are merged or linked
- Source attribution is preserved
- Normalized output matches reporting schema

---

## 3. Evidence Integrity & POI Verification

### Objective
Ensure evidence and Proof of Impact (POI) remain intact throughout the reporting pipeline.

### Manual Testing Steps
- Attach evidence:
  - HTTP requests/responses
  - CLI output
  - Screenshots or artifacts
- Generate reports and tickets

Manual commands / checks:

# Attach evidence using CLI

curl -X POST https://reporting.target.com/api/findings/123/evidence \
-F "file=@./exploit_output.txt" \
-H "Authorization: Bearer <API_TOKEN>"

# Validate download / view

curl -O https://reporting.target.com/api/findings/123/evidence/exploit_output.txt

- Ensures PoI stays intact.

### Validation Checks
- Evidence is not altered or lost
- Attachments remain accessible
- POI clearly demonstrates attacker impact

---

## 4. Severity & Risk Accuracy Testing

### Objective
Confirm severity calculations reflect real-world risk.

### Manual Testing Steps
- Submit findings with varying:
  - Exploitability
  - Impact
  - Context (internal vs external)
- Compare automated severity against expected severity

Manual checks:

- Submit findings with intentionally different severity (Critical / Low)
- Compare automated severity mapping

- CLI example for submission:

curl -X POST https://reporting.example.com/api/findings \
-d '{
  "title": "SQLi Test",
  "asset": "app.target.com",
  "severity": "Critical",
  "evidence": "curl -i https://app.target.com/login"
}'

- Confirm scoring aligns with expected risk.

### Validation Checks
- High-impact issues are not under-scored
- Informational issues are not escalated
- Severity logic is consistent across sources

---

## 5. Ticketing & Workflow Integration Testing

### Objective
Ensure seamless integration with remediation workflows.

### Manual Testing Steps
- Automatically create tickets (e.g., Jira, GitHub Issues)
- Validate:
  - Title
  - Description
  - Evidence
  - Severity
  - SLA tags

Manual commands / checks:

# Generate a Jira ticket via reporting automation
python3 scripts/jira_sync.py --finding 123

# Verify ticket created with correct fields

curl -H "Authorization: Bearer <JIRA_TOKEN>" \
https://jira.target.com/rest/api/2/issue/TEST-123

- Ensure evidence, severity, and description propagate correctly.

### Validation Checks
- Tickets contain actionable reproduction steps
- No sensitive data leakage in tickets
- Correct project and assignee routing

---

## 6. Metrics & Reporting Validation

### Objective
Verify accuracy of security metrics and reporting outputs.

### Manual Testing Steps
- Generate reports across time ranges
- Validate metrics such as:
  - Open vs closed findings
  - Severity distribution
  - Time to remediation

Manual commands / checks:

# Generate automated PDF / CSV report
python3 scripts/vuln_report.py --output report_$(date +%F).pdf

# Validate counts and severity distribution
python3 scripts/vuln_report.py --summary

- Cross-check with database / ingestion logs for consistency.

### Validation Checks
- Metrics match raw data
- No calculation errors
- Reports are reproducible

---

## 7. Security & Abuse Testing of Automation

### Objective
Ensure reporting automation does not introduce new security risks.

### Manual Testing Steps
- Attempt to inject:
  - Malicious payloads in finding fields
  - Oversized evidence attachments
- Review access controls on reports and tickets

Manual commands / checks:

# Inject malicious payload in finding title

curl -X POST https://reporting.target.com/api/findings \
-d '{"title": "<script>alert(1)</script>", "severity":"Low"}'

- Validate no XSS or injection occurs in report output
- Check access controls

### Validation Checks
- No injection or rendering issues
- Proper access control enforcement
- Secrets are not exposed in outputs

---

## Documentation & Evidence

- Record test cases and expected outcomes
- Capture screenshots and logs
- Document automation failures and remediation actions
- Map issues to business and operational impact

---

## Outcome

Successful testing ensures reporting automation:
- Produces accurate, high-signal findings
- Preserves evidence and impact
- Supports engineering remediation
- Enables executive and compliance visibility

Automation reduces manual effort and improves security program scalability.
