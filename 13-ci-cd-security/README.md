# CI/CD Security

## Purpose:
- Secure build and deployment pipelines.

------

## Tools & Techniques:
- GitHub Actions
- Environment review

----

## Methodology:
- Review pipelines
- Validate secrets
- Restrict access
- Audit logs

------

## Commands:
# Step 1:
- Secrets Review:

grep -R "API_KEY" .

------

### Step 2:
- Pipeline Audit

cat .github/workflows/build.yml

---------- 

### Output:
- Exposed secrets
- Misconfigurations


# Security Impact:
-  Prevents supply attacks
- Protects deployments
