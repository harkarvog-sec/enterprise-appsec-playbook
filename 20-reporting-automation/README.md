# Reporting & Automation

# Purpose:
- Automate security reporting and workflow management.

-------

#### Tools & Techniques:
- Python
- APIs
- Jira
- ServiceNow

------

##### Methodology:
- Collect data
- Normalize
- Automate reports
- Integrate tools

------

# Commands:
#### Step 1:
- API Data Fetch:

curl https://api.rapid7.com/vm/assets

-------

### Step 2:
# Python Report:

import requests
r = requests.get("https://api.example.com/vulns")
print(r.json())

--------

#### Output:
- Automated dashboards
- KPI reports
- Ticket workflows

--------

### Security Impact:
- Improves visibility
- Saves time
- Enhances governance
