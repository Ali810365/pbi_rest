# Power BI Rest Api

## Table of Contents

- [References](#References)
- [Getting Started](#getting-started)
- [Samples](#Samples)
- [Support These Projects](#support-these-projects)

## References

- [Register Appilication in AD Portal ](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Service Principal](https://learn.microsoft.com/en-us/power-bi/developer/embedded/embed-service-principal)
- [Power BI Rest API Documentation](https://docs.microsoft.com/en-us/rest/api/power-bi/)
- [Developer Center](https://powerbi.microsoft.com/en-us/developers/)

## Requirements
Python 3

MSAL

The Microsoft Authentication Library for Python enables applications to integrate with the Microsoft identity platform. It allows you to sign in users or apps with Microsoft identities (Azure AD, Microsoft Accounts and Azure AD B2C accounts) and obtain tokens to call Microsoft APIs such as Microsoft Graph or your own APIs registered with the Microsoft identity platform. It is built using industry standard OAuth2 and OpenID Connect protocols

```
pip install msal
```

## Getting Started
```
git clone https://github.com/Ali810365/pbi_rest
```

## Configuration

In __config__.py fill in empty slots for application_id, application_secret, tenant_id then run file.
Once the proper credentials are in place, your options are service principal or user whichever is your preference method of authenticating.
User requires browser interactivity. 

## Samples

```Python
from library.groups import Groups
from library.reports import Reports
from library.datasets import Datasets
from library.dashboards import Dashboards
from library.admin import Admin()

groups = Groups()
reports = Reports()
dashboards = Dashboards()
datasets = Datasets()
admin = Admin()

#GET all workspaces in organization as Admin
def get_tenant_groups():
    result = admin.get_groups(1000)
    print(result)

#GET all workspaces user has access to
def get_groups():
    result = groups.get_groups(100)
    print(result)

#GET users in a workspace
def get_users():
    result = groups.get_users('f089354e-8366-4e18-aea3-4cb4a3a50b48')
    print(result)

#GET reports in a workspace
def get_reports():
    result = reports.get_reports('f089354e-8366-4e18-aea3-4cb4a3a50b48')
    print(result)

#GET reports in my-workspace
def get_reports_from_my_workspace():
    result = reports.get_reports_from_my_workspace('f089354e-8366-4e18-aea3-4cb4a3a50b48')
    print(result)

#GET dashboards in a workspace
def get_dashboard():
    result = dashboards.get_dashboards('f089354e-8366-4e18-aea3-4cb4a3a50b48')
    print(result)

#GET dashboards in my-workspace
def get_dashboard_from_my_workspace():
    result = dashboards.my_workspace_get_dashboards()
    print(result)

#GET datasets in a workspace
def get_dashboard():
    result = datasets.get_datasets()
    print(result)
```












## Usage

Here is a simple example of using the `powerbi` library.

```python
from pprint import pprint
from configparser import ConfigParser
from powerbi.client import PowerBiClient

# Initialize the Parser.
config = ConfigParser()

# Read the file.
config.read('config/config.ini')

# Get the specified credentials.
client_id = config.get('power_bi_api', 'client_id')
redirect_uri = config.get('power_bi_api', 'redirect_uri')
client_secret = config.get('power_bi_api', 'client_secret')

# Initialize the Client.
power_bi_client = PowerBiClient(
    client_id=client_id,
    client_secret=client_secret,
    scope=['https://analysis.windows.net/powerbi/api/.default'],
    redirect_uri=redirect_uri,
    credentials='config/power_bi_state.jsonc'
)

# Initialize the `Dashboards` service.
dashboard_service = power_bi_client.dashboards()

# Add a dashboard to our Workspace.
dashboard_service.add_dashboard(name='my_new_dashboard')

# Get all the dashboards in our Org.
pprint(dashboard_service.get_dashboards())
```

## Support These Projects

**Patreon:**
Help support this project and future projects by donating to my [Patreon Page](https://www.patreon.com/sigmacoding). I'm
always looking to add more content for individuals like yourself, unfortuantely some of the APIs I would require me to
pay monthly fees.

**YouTube:**
If you'd like to watch more of my content, feel free to visit my YouTube channel [Sigma Coding](https://www.youtube.com/c/SigmaCoding).

**Questions:**
If you have questions please feel free to reach out to me at [coding.sigma@gmail.com](mailto:coding.sigma@gmail.com?subject=[GitHub]%20Fred%20Library)