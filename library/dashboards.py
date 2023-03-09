import requests
from datetime import datetime, timedelta
from library.requests import audit_requests

class Dashboards():
    def __init__(self):
        pass

    def my_workspace_add_dashboard(self, name:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/add-dashboard
        ''' Creates a new empty dashboard in >>> My workspace
    
        >>> Params:
            name: The name of the new dashboard
        
        >>> Example:
            >>> dashboards.my_workspace_add_dashboard('Sales Marketing')
        
        '''
        body = {
            "name": name
        }
        endpoint = f"dashboards"

        method = 'post'

        response = audit_requests(endpoint, method, json=body)

        return response

    def add_dashboard(self, group_id:str, name:str, ):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/add-dashboard-in-group
        ''' Creates a new empty dashboard in >>> the specified workspace
        >>> Params:
            name: The name of the new dashboard
            group_id: The group ID
        
        >>> Example:
            >>> dashboards.add_dashboard('cfafbeb1-8037-4d0c-896e-a46fb27ff229', 'Sales Marketing')
        
        '''
        body = {
            "name": name
        }
        endpoint = f"groups/{group_id}/dashboards"

        method = 'post'

        response = audit_requests(endpoint, method, json=body)

        return response
    

    def my_workspace_delete_dashboard(self, dashboard_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/delete-dashboard
        ''' Deletes the specified dashboard from >>> My workspace

        >>> Params:
            dashboard_id: The dashboard ID
        
        >>> Example:
            >>> dashboards.my_workspace_delete_dashboard('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"dashboards/{dashboard_id}"

        method = 'delete'

        response = audit_requests(endpoint, method)

        return response
    
    def delete_dashboard(self, group_id:str, dashboard_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/delete-dashboard-in-group
        ''' Deletes the specified dashboard from >>> the specified workspace

        >>> Params:
            group_id: The group ID
            dashboard_id: The dashboard ID
        
        >>> Example:
            >>> dashboards.my_workspace_delete_dashboard('cfafbeb1-8037-4d0c-896e-a46fb27ff229', bce0auc55-b164-463e-ad1d-962d66dadd74)
        
        '''
        endpoint = f"groups/{group_id}/dashboards/{dashboard_id}"

        method = 'delete'

        response = audit_requests(endpoint, method)

        return response

    
    def my_workspace_get_dashboard(self, dashboard_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-dashboard
        ''' Returns the specified dashboard from >>> My workspace

        >>> Params:
            dashboard_id: The dashboard ID
        
        >>> Example:
            >>> dashboards.my_workspace_get_dashboards('69ffaa6c-b36d-4d01-96f5-1ed67c64d4af')
        
        '''
        endpoint = f"dashboards/{dashboard_id}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dashboard(self, group_id:str, dashboard_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-dashboard-in-group
        ''' Returns the specified dashboard from the specified workspace

        >>> Params:
            group_id: The dataset ID
            dashboard_id: The dashboard ID
        
        >>> Example:
            >>> dashboards.get_dashboard('cfafbeb1-8037-4d0c-896e-a46fb27ff229', '69ffaa6c-b36d-4d01-96f5-1ed67c64d4af')
        
        '''
        endpoint = f"groups/{group_id}/dashboards/{dashboard_id}"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    

    def my_workspace_get_dashboards(self):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-dashboards
        ''' Returns a list of dashboards from >>> My workspace

        >>> Example:
            >>> dashboards.my_workspace_get_dashboards()
        
        '''
        endpoint = f"dashboards"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    
    def get_dashboards(self, group_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-dashboards-in-group
        ''' Returns a list of dashboards from the specified workspace.

        >>> Params:
            group_id: The group ID
        
        >>> Example:
            >>> dashboards.get_dashboards('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{group_id}/dashboards"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response

    def get_tiles(self, group_id:str, dashboard_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-tiles-in-group
        ''' Returns a list of tiles within the specified dashboard from the specified workspace

        >>> Params:
            group_id: The group ID
        
        >>> Example:
            >>> dashboards.get_tiles('cfafbeb1-8037-4d0c-896e-a46fb27ff229', '69ffaa6c-b36d-4d01-96f5-1ed67c64d4af')
        
        '''
        endpoint = f"groups/{group_id}/dashboards/{dashboard_id}/tiles"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    

    
