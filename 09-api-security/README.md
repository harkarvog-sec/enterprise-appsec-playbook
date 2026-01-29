# API Security Testing

APIs are a primary attack surface in modern enterprise applications. Weaknesses in authentication, authorization, business logic, and data exposure often lead to critical breaches.

This module documents a manual, attacker-driven approach to API security testing. Focus is on identifying broken access controls, injection points, excessive data exposure, and misconfigured endpoints across REST and GraphQL APIs.

The goal is to validate whether API functionality can be abused by a motivated attacker under realistic conditions.

## Scope

- API authentication and authorization enforcement
- Rate limiting and abuse protection
- Data exposure and sensitive information leaks
- Business logic validation
- Input validation and injection testing
- OAuth, JWT, and token security
- Error handling and response leakage

## Outcome

Successful testing produces validated findings that demonstrate:

- Whether API endpoints enforce proper authentication and authorization
- Whether sensitive data is protected from unauthorized access
- Whether business logic can be manipulated to gain an unfair advantage
- Whether attack paths exist that could lead to data leakage, account compromise, or service abuse
