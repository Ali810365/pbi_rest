import requests
from datetime import datetime, timedelta
from library.date_conversion import FormateDate
from library.login import headers
from library.requests import audit_requests

class Reports():
    def __init__(self):
        self.headers = headers
    
    def clone_report(self, reportId, name):
        ''' Clones the specified report from >>> My workspace
            #If the dataset for a cloned report resides in two different workspaces or in My workspace, 
            #then a shared dataset will be created in the report's workspace.
            #When cloned, reports with a live connection will lose that connection and instead have a direct binding to the target dataset.

        >>> Params:
            reportId: The report ID
            name: The new report name
        
        >>> Example:
            >>> reports.get_reports('f089354e-8366-4e18-aea3-4cb4a3a50b48')
        '''
        body = {
            "name": f"{name}"
        }

        endpoint = f"reports/{reportId}/Clone"

        method = 'post'

        response = audit_requests(endpoint, method, json=body)

        return response


    def get_reports(self, group_id):
        ''' Returns a list of reports from >>> the specified workspace

        >>> Params:
            group_id: The group ID
        
        >>> Example:
            >>> reports.get_reports('f089354e-8366-4e18-aea3-4cb4a3a50b48')
        '''

        endpoint = f"groups/{group_id}/reports"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response

    def get_report(self, group_id, report_id):
        ''' Returns the specified report from >>> specified workspace

        >>> Params:
            group_id: The group ID
            report_id: The report ID
        
        >>> Example:
            >>> reports.get_report('f089354e-8366-4e18-aea3-4cb4a3a50b48', '5b218778-e7a5-4d73-8187-f10824047715)
        '''

        endpoint = f"groups/{group_id}/reports/{report_id}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response

    def get_reports_from_my_workspace(self):
        ''' Returns a list of reports from >>> My workspace

        >>> Example:
            >>> reports.my_workspace_get_reports()
        '''
        endpoint = f"reports"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_report_from_my_workspace(self, report_id):
        ''' Returns the specified report from >>> My workspace

        >>> Params:
            report_id: The report ID

        >>> Example:
            >>> reports.my_workspace_get_reports()
        '''
        endpoint = f"reports/{report_id}"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response

    def delete_report(self, group_id, report_id):
        ''' Deletes the specified report from >>> the specified workspace

        >>> Params:
            group_id: The group ID
            report_id: The report ID

        >>> Example:
            >>> reports.delete_report('f089354e-8366-4e18-aea3-4cb4a3a50b48', '5b218778-e7a5-4d73-8187-f10824047715')
        '''
        endpoint = f"groups/{group_id}/reports/{report_id}"

        method = 'delete'

        response = audit_requests(endpoint, method)

        return response
    
    def delete_report_from_my_workspace(self, report_id):
        ''' Deletes the specified report from >>> My Workspace
        
        >>> Params:
            report_id: The report ID

        >>> Example:
            >>> reports.my_workspace_delete_report('5b218778-e7a5-4d73-8187-f10824047715')
        '''
        endpoint = f"reports/{report_id}"

        method = 'delete'

        response = audit_requests(endpoint, method)

        return response

