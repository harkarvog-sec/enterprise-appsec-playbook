# Business Logic Attack Scenarios

This document describes realistic attack scenarios that exploit weaknesses in application workflows and business rules. These attacks typically bypass traditional security controls and require manual analysis.

---

## 1. Workflow Bypass

# Description:
An attacker skips required steps in a multi-stage process.

# Attack Flow: 
1. Begin a legitimate workflow (e.g., checkout or approval process)  
2. Capture requests using an intercepting proxy  
3. Directly submit the final step without completing prior validations  

## Proof of Exploitation (Example):
# Directly confirm order without completing payment step

curl -X POST https://target.com/api/order/confirm \
-H "Authorization: Bearer <token>" \
-d '{"order_id":123}'

# Impact:
Financial loss, fraud, integrity violations

---

## 2. Race Condition Abuse

# Description:
Exploiting timing issues by submitting multiple concurrent requests.

# Attack Flow:
1. Identify a critical action (refund, transfer, coupon usage)  
2. Send multiple identical requests simultaneously  
3. Observe duplicated or inconsistent processing  

# Impact:
Double spending, balance manipulation, unauthorized credits

---

## 3. Replay Attacks

Description:
Reusing previously valid requests or identifiers.

Attack Flow:
1. Capture a successful transaction request  
2. Replay the same request multiple times  
3. Observe repeated execution  

Impact:
Unauthorized repeated actions, data corruption

---

## 4. Limit & Quota Abuse

# Description:
Bypassing business-imposed limits or thresholds.

# Attack Flow:
1. Identify rate or quantity limits  
2. Test enforcement across APIs and clients  
3. Abuse weak or inconsistent checks  

# Impact:
Resource exhaustion, abuse of promotions, denial of service

---

## 5. Trust Assumption Exploitation

# Description: 
Server trusts client-controlled values.

# Attack Flow: 
1. Modify price, role, or state parameters  
2. Submit manipulated request  
3. Observe unauthorized behavior  

# Impact:
Financial manipulation, privilege escalation
