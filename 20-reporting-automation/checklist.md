# Reporting Automation Testing Checklist

This checklist ensures comprehensive testing of automated security reporting workflows.  
Each item includes severity guidance, manual commands, and validation notes.

---

## 1. Finding Ingestion & Normalization

- [ ] Ingest findings from all sources (manual, SAST/DAST, vulnerability scanners, cloud tools)  
 
  - Manual test: 

    curl -X POST https://reporting.target.com/api/findings \
    -H "Authorization: Bearer <API_TOKEN>" \
    -d '{"title":"Test SQLi","asset":"app.target.com","severity":"Medium"}'
  
- [ ] Confirm all required fields populated: title, asset, severity, evidence, source  
- [ ] Validate normalization of severity labels, categories, asset identifiers  

Severity of failure: High  
Exploitability:Medium  

---

## 2. Deduplication & Merge Handling

- [ ] Submit duplicate findings from multiple sources  
- [ ] Verify system merges duplicates correctly  
- [ ] Confirm source attribution is preserved  

Manual check:

curl -X POST https://reporting.target.com/api/findings -d '{...}' # Source A
curl -X POST https://reporting.target.com/api/findings -d '{...}' # Source B
curl https://reporting.target.com/api/findings?title="Test SQLi"

Severity of failure: Medium
Exploitability: Easy

---

#### 3. Evidence / PoI Handling

Attach evidence to findings (logs, CLI output, screenshots)

Validate attachments are retrievable and intact

Check report exports include evidence correctly

# Manual check:

curl -X POST https://reporting.target.com/api/findings/123/evidence \
-F "file=@exploit_output.txt" \
-H "Authorization: Bearer <API_TOKEN>"

curl -O https://reporting.target.com/api/findings/123/evidence/exploit_output.txt

Severity of failure: High
Exploitability: Medium

---

4. Severity Accuracy

Submit findings with varying exploitability and impact
Confirm automated severity aligns with expected risk
Ensure critical findings are not downrated

# Manual check:

curl -X POST https://reporting.target.com/api/findings \
-d '{"title":"Auth Bypass","asset":"api.target.com","severity":"Critical","evidence":"curl -i https://api.target.com/admin"}'

Severity of failure: Critical
Exploitability: Easy

----

5. Ticketing & Workflow Integration

Validate automated ticket creation (Jira, GitHub)
Confirm title, severity, evidence, SLA tags propagate correctly
Verify correct project, assignee, and workflow

# Manual check:

python3 scripts/jira_sync.py --finding 123
curl -H "Authorization: Bearer <JIRA_TOKEN>" https://jira.target.com/rest/api/2/issue/SEC-123

Severity of failure: High
Exploitability: Medium

---

6. Metrics & Reporting Validation

Generate reports across multiple time ranges
Confirm metrics (open/closed findings, severity distribution, time to remediation) match raw data
Validate report exports (PDF/CSV)

# Manual check:

python3 scripts/vuln_report.py --output report_$(date +%F).pdf
python3 scripts/vuln_report.py --summary

Severity of failure: Medium
Exploitability: Easy

---

7. Security & Abuse Testing

Attempt injection via finding fields or evidence
Test oversized attachments or malformed requests
Verify access controls prevent unauthorized report access

# Manual check:

curl -X POST https://reporting.target.com/api/findings \
-d '{"title":"<script>alert(1)</script>","severity":"Low"}'

Severity of failure: Critical
Exploitability: Medium

---

#### Documentation & Evidence

Capture screenshots, CLI output, logs
Document expected vs actual behavior
Map issues to business impact and operational risk
