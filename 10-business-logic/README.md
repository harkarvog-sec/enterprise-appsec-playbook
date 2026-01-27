# Business Logic Testing

## Purpose:
- Detect flaws in workflows and process logic.

-----

## Tools & Techniques:
- curl
- Manual workflow testing
- Transaction replay

------

## Methodology:
- Map workflows
- Modify sequences
- Replay transactions
- Test limits
- Bypass controls

----

## Commands:
# Step 1:
- Replay Transaction:

curl -X POST https://target.com/pay -d "amount=100"

-------

### Step 2:
- Bypass Step:

curl https://target.com/confirm?skip=true

------

#### Output:
- Payment bypass
- Logic flaws
- Workflow abuse

------

### Security Impact:
- Prevents fraud
- Protects revenue
- Improves integrity
