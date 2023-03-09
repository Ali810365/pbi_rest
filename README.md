# Power BI Rest Api

## Table of Contents

- [References](#References)
- [Getting Started](#getting-started)
- [Samples](#Samples)


## References

- [Register Appilication in AD Portal ](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Service Principal](https://learn.microsoft.com/en-us/power-bi/developer/embedded/embed-service-principal)
- [Power BI Rest API Documentation](https://docs.microsoft.com/en-us/rest/api/power-bi/)
- [Developer Center](https://powerbi.microsoft.com/en-us/developers/)

## Requirements


## Getting Started
```
git clone https://github.com/Ali810365/pbi_rest
```

### Python 3

MSAL

The Microsoft Authentication Library for Python enables applications to integrate with the Microsoft identity platform. It allows you to sign in users or apps with Microsoft identities (Azure AD, Microsoft Accounts and Azure AD B2C accounts) and obtain tokens to call Microsoft APIs such as Microsoft Graph or your own APIs registered with the Microsoft identity platform. It is built using industry standard OAuth2 and OpenID Connect protocols

```
pip install msal
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