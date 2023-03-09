import requests
from datetime import datetime, timedelta
from library.date_conversion import FormateDate
from library.requests import audit_requests

class Reports():
    def __init__(self):
        pass
    

    def my_workspace_clone_report(self, reportId:str, name:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/reports/clone-report
        ''' Clones the specified report from >>> My workspace
            
        >>> Params:
            reportId: The report ID
            name: The new report name
        
        >>> Example:
            >>> reports.my_workspace_clone_report('f089354e-8366-4e18-aea3-4cb4a3a50b48', 'cloned report')
        '''
        body = {
            "name": f"{name}"
        }

        endpoint = f"reports/{reportId}/Clone"

        method = 'post'

        response = audit_requests(endpoint, method, json=body)

        return response

    def clone_report(self, groupId, reportId:str, name:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/reports/clone-report-in-group
        ''' Clones the specified report from >>> My workspace
            
        >>> Params:
            reportId: The report ID
            name: The new report name
        
        >>> Example:
            >>> reports.clone_report('f089354e-8366-4e18-aea3-4cb4a3a50b48', 'cloned report')
        '''
        body = {
            "name": f"{name}"
        }

        endpoint = f"groups/{groupId}/reports/{reportId}/Clone"

        method = 'post'

        response = audit_requests(endpoint, method, json=body)

        return response


    def get_reports(self, group_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/reports/clone-report-in-group
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
    
    def delete_report_from_my_workspace(self, report_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/reports/delete-report
        ''' Deletes the specified report from >>> My Workspace
        
        >>> Params:
            report_id: The report ID

        >>> Example:
            >>> reports.delete_report_from_my_workspace('5b218778-e7a5-4d73-8187-f10824047715')
        '''
        endpoint = f"reports/{report_id}"

        method = 'delete'

        response = audit_requests(endpoint, method)

        return response
    
    def delete_report(self, group_id:str, report_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/reports/delete-report-in-group
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

    
    def get_report_from_my_workspace(self, report_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-report
        ''' Returns the specified report from >>> My workspace

        >>> Params:
            report_id: The report ID

        >>> Example:
            >>> reports.get_report_from_my_workspace()
        '''
        endpoint = f"reports/{report_id}"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response


    def get_report(self, group_id:str, report_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-report-in-group
        ''' Returns the specified report from >>> specified workspace

        >>> Params:
            group_id: The group ID
            report_id: The report ID
        
        >>> Example:
            >>> reports.get_report('f089354e-8366-4e18-aea3-4cb4a3a50b48', '5b218778-e7a5-4d73-8187-f10824047715')
        '''

        endpoint = f"groups/{group_id}/reports/{report_id}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_reports_from_my_workspace(self):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-reports
        ''' Returns a list of reports from >>> My workspace

        >>> Example:
            >>> reports.get_reports_from_my_workspace()
        '''
        endpoint = f"reports"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    

    def get_reports(self, group_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-reports-in-group
        ''' Returns a list of reports from the specified workspace

        >>> Params:
            group_id: The group ID
            report_id: The report ID
        
        >>> Example:
            >>> reports.get_reports('f089354e-8366-4e18-aea3-4cb4a3a50b48')
        '''

        endpoint = f"groups/{group_id}/reports"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response

    
    
    
    
    
    

