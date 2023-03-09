import json
import requests
from library.admin import Admin
from library.groups import Groups
from library.dashboards import Dashboards
from library.reports import Reports
from library.datasets import Datasets

dummy = "3b5ca243-47d1-4be5-ac56-57c62291607d"

id = "2b5ca223-46d1-4be5-ac56-57c62291607d" #test
api_id = '5bbd8704-ed60-462d-b4f9-6b7192ff8963'
test_dataset = "709613a9-bb82-46d5-83e0-1570add82f78"
test_dashboard = "0b0f429f-ed67-4a0b-bdd6-1c358d702db7"
test_report = "4e2b0970-4a96-43fb-a961-d9d557830f1b"
api_dashboard = "ce0eac55-b164-463e-ad1d-962d66dadd74"
user = "aabdi@redapt.com"
admin = Admin()
groups = Groups()
dashboards = Dashboards()
reports = Reports()
datasets = Datasets()


def testing_groups():
    #print(groups.add_user(id, "Admin", user, "User"))
    #print(groups.delete_group("5bbd8704-ed60-462d-b4f9-6b7192ff8963"))
    #print(groups.delete_user(id, user))
    #print(groups.get_users(id))
    #print(groups.get_groups(5))
    #print(groups.update_user(id, "member", user, "User"))
    pass

#testing_groups()

def testing_dashboards():
    #print(dashboards.my_workspace_add_dashboard('Sales Marketing'))
    #print(dashboards.add_dashboard(id, 'Sales Marketing'))
    #print(dashboards.delete_dashboard(id, api_dashboard))
    #print(dashboards.get_dashboards(id))
    #print(dashboards.get_dashboard(id, test_dashboard))
    #print(dashboards.get_dashboards(id))
    #print(dashboards.get_tiles(id, test_dashboard))
    pass

#testing_dashboards()

def testing_reports():
    #print(reports.get_reports(id))
    #print(reports.clone_report(id, test_report, 'cloned report' ))
    #print(reports.delete_report(id, '83e25fac-f375-450c-be4f-96a62331ce32'))
    #print(reports.get_report(id, test_report))
    #print(reports.get_reports(id))
    pass

#testing_reports()

def testing_datasets():
    #print(datasets.get_datasets(id))
    #print(datasets.get_dataset(id, test_dataset))
    print(datasets.get_refresh_history(id, test_dataset, 5))
    pass

testing_datasets()