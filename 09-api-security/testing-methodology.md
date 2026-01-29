# API Security Testing Methodology

API security testing is performed manually to identify authentication, authorization, and business logic flaws that automated scanners often miss. This methodology applies to REST, GraphQL, and microservice endpoints.

## Preparation

- Enumerate all API endpoints and available methods (GET, POST, PUT, DELETE)
- Map authentication and authorization requirements per endpoint
- Identify sensitive data exposure and privilege boundaries
- Collect API documentation, Swagger/OpenAPI specs, or client SDKs
- Prepare authorized test accounts and tokens

## Manual Testing Approach

1. Authentication & Authorization:
   - Test each endpoint with valid, invalid, expired, and missing tokens
   - Verify role-based access control is enforced
   - Attempt horizontal and vertical privilege escalation

# Command example:

 curl -H "Authorization: Bearer <token>" https://api.target.com/users


2. Input Validation & Injection Testing:
   - Manipulate JSON, query parameters, headers, and URL paths
   - Test for SQL, NoSQL, command injection, and XSS via API inputs
   - Validate error responses and server-side handling

3. Business Logic Testing
   - Attempt bypass of workflow restrictions (e.g., order approvals, funds transfer)
   - Modify request data to escalate privileges or manipulate resources
   - Confirm that workflow integrity is maintained

4. Data Exposure
   - Verify sensitive fields are not exposed in responses
   - Check pagination and filtering for data leakage
   - Test enumeration attacks on object IDs or user identifiers

5. Rate Limiting & Abuse
   - Test brute-force or enumeration protection
   - Evaluate request throttling, IP restrictions, and alerting mechanisms

6. OAuth & Token Validation
   - Test token replay, expiry, scope, and binding to users/clients
   - Confirm refresh token rotation and revocation

## Validation

- Confirm unauthorized access is blocked
- Verify sensitive data is protected
- Validate business logic constraints are enforced
- Test across multiple clients and platforms

## Notes

- Manual testing is prioritized over automated scans
- All findings must be reproducible and documented
- Testing performed in authorized environments only
