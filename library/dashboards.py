import requests
from datetime import datetime, timedelta
from library.login import headers
from library.requests import audit_requests

class Dashboards():
    def __init__(self):
        self.headers = headers

    #GET REQUESTS
    def my_workspace_get_dashboard(self, dashboard_id):
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
    
    def my_workspace_get_dashboards(self):
        ''' Returns a list of dashboards from >>> My workspace

        >>> Example:
            >>> dashboards.my_workspace_get_dashboards()
        
        '''
        endpoint = f"dashboards"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_dashboard(self, group_id, dashboard_id):
        ''' Returns the specified dashboard from the specified workspace

        >>> Params:
            group_id: The dataset ID
            dashboard_id: The dashboard ID
        
        >>> Example:
            >>> dashboards.get_dashboard('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{group_id}/dashboards/{dashboard_id}"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response

    def get_dashboards(self, group_id):
        ''' Returns a list of dashboards from the specified workspace.

        >>> Params:
            group_id: The dataset ID
        
        >>> Example:
            >>> dashboards.get_dashboards('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{group_id}/dashboards"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response


    #POST REQUESTS
    def my_workspace_add_dashboard(self, name):
        ''' Creates a new empty dashboard in >>> My workspace
        >>> Params:
            name: The name of the new dashboard
        
        >>> Example:
            >>> dashboards.my_workspace_add_dashboard('Sales Marketing')
        
        '''
        params = {
            "name": name
        }
        endpoint = f"dashboards"

        method = 'post'

        response = audit_requests(endpoint, method)

        return response
    
    def add_dashboard(self, name, group_id):
        ''' Creates a new empty dashboard in >>> the specified workspace
        >>> Params:
            name: The name of the new dashboard
            group_id: The group ID
        
        >>> Example:
            >>> dashboards.my_workspace_add_dashboard('Sales Marketing', 'cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        params = {
            "name": name
        }
        endpoint = f"groups/{group_id}/dashboards"

        method = 'post'

        response = audit_requests(endpoint, method)

        return response

    #DELETE
    def my_workspace_delete_dashboard(self, dashboard_id):
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
    
    def delete_dashboard(self, group_id, dashboard_id):
        ''' Deletes the specified dashboard from >>> the specified workspace

        >>> Params:
            group_id: The group ID
            dashboard_id: The dashboard ID
        
        >>> Example:
            >>> dashboards.my_workspace_delete_dashboard('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{group_id}/dashboards/{dashboard_id}"

        method = 'delete'

        response = audit_requests(endpoint, method)

        return response
