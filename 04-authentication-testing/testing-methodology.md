# Authentication Testing Methodology

Authentication testing is performed manually to identify logic flaws, state handling issues, and abuse paths that automated scanners frequently miss. This methodology applies to web, API, and mobile clients in enterprise environments.

## Preparation

- Identify all authentication mechanisms (credentials, tokens, SSO)
- Map authentication flows across web, API, and mobile clients
- Document session and token lifecycles
- Understand sensitive actions and privilege boundaries
- Prepare authorized testing environment and test accounts

## Manual Testing Approach

1. **Login Workflow Validation**
   - Intercept and replay authentication requests
   - Test correct and incorrect credentials
   - Confirm proper error handling and account lockout
   
  ## Command example:
  
  curl -X POST https://target.com/login -d "username=test&password=test"
  

2. **Password Reset & Recovery Testing**
   - Verify token invalidation after reset
   - Test for account enumeration
   - Confirm session termination on password change
   -
## Command example:

 curl -I https://target.com/reset-password
     

3. **Session & Token Manipulation**
   - Modify, replay, or reuse session tokens
   - Attempt session fixation and hijacking
   - Test concurrent session behavior

4. **MFA / 2FA Validation**
   - Test bypass scenarios for protected actions
   - Verify enforcement consistency across endpoints

5. **Privilege Escalation & Forced Browsing**
   - Attempt access to restricted endpoints without proper authentication
   - Confirm role-based enforcement

6. **OAuth & SSO Checks**
   - Validate redirect URI enforcement
   - Confirm state parameter validation
   - Test account linking logic

## Validation

- Confirm unauthorized access to protected resources
- Verify session persistence after logout, password reset, or token expiration
- Assess impact across multiple clients (web, API, mobile)

## Notes

- Automated tools are used as a signal only; all findings must be manually validated
- Testing should always be performed in authorized environments
- Focus is on realistic abuse paths, not just “scanning for vulnerabilities”
