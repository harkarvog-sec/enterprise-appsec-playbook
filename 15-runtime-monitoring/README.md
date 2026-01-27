# Runtime Monitoring

## Purpose:
- Detect threats during application execution.

-----

## Tools & Techniques:
- Logs
- SIEM
- EDR

----

## Methodology:
- Review logs
- Monitor alerts
- Analyze patterns

-----

## Commands:
# Step 1:
- Log Review:

tail -f /var/log/app.log

---------

### Step 2:
- Search Events:

grep "ERROR" app.log

------

## Output:
- Attack indicators
- Anomalies

------

### Security Impact:
- Early detection
- Faster response
