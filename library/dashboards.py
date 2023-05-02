import requests
from datetime import datetime, timedelta
from library.requests import audit_requests

class Dashboards():
    def __init__(self):
        pass

    def add_dashboard(self, name:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/add-dashboard
        
        Creates a new empty dashboard in >>> My workspace
    
        >>> Params:
            name: The name of the new dashboard
        
        >>> Example:
            >>> dashboards.add_dashboard('Sales Marketing')
        
        '''
        body = {
            "name": name
        }
        endpoint = f"dashboards"

        method = 'post'

        response = audit_requests(endpoint, method, json=body)

        return response

    def add_dashboard_in_group(self, groupId:str, name:str, ):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/add-dashboard-in-group
        
        Creates a new empty dashboard in >>> the specified workspace
        >>> Params:
            name: The name of the new dashboard
            groupId: The group ID
        
        >>> Example:
            >>> dashboards.add_dashboard_in_group('cfafbeb1-8037-4d0c-896e-a46fb27ff229', 'Sales Marketing')
        
        '''
        body = {
            "name": name
        }
        endpoint = f"groups/{groupId}/dashboards"

        method = 'post'

        response = audit_requests(endpoint, method, json=body)

        return response
    
    def clone_tile(self, dashboardId:str, tileId:str, targetDashboardId:str=None, request_body=None):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/clone-tile
        
        Clones the specified tile from My workspace

        >>> Params:
            dashboardId: The dashboard ID
        
        >>> Example:
            >>> dashboards.clone_tile()
        
        '''
        endpoint = f"dashboards/{dashboardId}/tiles/{tileId}/Clone"

        method = 'post'

        body = {
            "targetDashboardId": targetDashboardId
        }

        if(request_body):
            body = request_body

        response = audit_requests(endpoint, method, json=body)

        return response
    
    def clone_tile_in_group(self, groupId:str, dashboardId:str, tileId:str, targetDashboardId:str=None, request_body=None):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/clone-tile-in-group
        
        Clones the specified tile from the specified workspace

        >>> Params:
            groupId: The workspace ID
            dashboardId: The dashboard ID
            tileId: The tile ID
            targetDashboardId: The target dashboard ID
        
        >>> Example:
            >>> dashboards.clone_tile_in_group()
        
        '''
        endpoint = f"groups/{groupId}/dashboards/{dashboardId}/tiles/{tileId}/Clone"

        method = 'post'

        body = {
            "targetDashboardId": targetDashboardId
        }

        if(request_body):
            body = request_body

        response = audit_requests(endpoint, method, json=body)

        return response
    
    def delete_dashboard(self, dashboardId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/delete-dashboard
        
        Deletes the specified dashboard from >>> My workspace

        >>> Params:
            dashboardId: The dashboard ID
        
        >>> Example:
            >>> dashboards.delete_dashboard('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"dashboards/{dashboardId}"

        method = 'delete'

        response = audit_requests(endpoint, method)

        return response
    
    def delete_dashboard_in_group(self, groupId:str, dashboardId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/delete-dashboard-in-group
        
        Deletes the specified dashboard from >>> the specified workspace

        >>> Params:
            groupId: The group ID
            dashboardId: The dashboard ID
        
        >>> Example:
            >>> dashboards.delete_dashboard_in_group('cfafbeb1-8037-4d0c-896e-a46fb27ff229', bce0auc55-b164-463e-ad1d-962d66dadd74)
        
        '''
        endpoint = f"groups/{groupId}/dashboards/{dashboardId}"

        method = 'delete'

        response = audit_requests(endpoint, method)

        return response

    
    def get_dashboard(self, dashboardId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-dashboard
        
        Returns the specified dashboard from >>> My workspace

        >>> Params:
            dashboardId: The dashboard ID
        
        >>> Example:
            >>> dashboards.get_dashboards('69ffaa6c-b36d-4d01-96f5-1ed67c64d4af')
        
        '''
        endpoint = f"dashboards/{dashboardId}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dashboard_in_group(self, groupId:str, dashboardId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-dashboard-in-group
        
        Returns the specified dashboard from the specified workspace

        >>> Params:
            groupId: The dataset ID
            dashboardId: The dashboard ID
        
        >>> Example:
            >>> dashboards.get_dashboard_in_group('cfafbeb1-8037-4d0c-896e-a46fb27ff229', '69ffaa6c-b36d-4d01-96f5-1ed67c64d4af')
        
        '''
        endpoint = f"groups/{groupId}/dashboards/{dashboardId}"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_dashboards(self):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-dashboards
        
        Returns a list of dashboards from >>> My workspace

        >>> Example:
            >>> dashboards.get_dashboards()
        
        '''
        endpoint = f"dashboards"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_dashboards_in_group(self, groupId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-dashboards-in-group
        
        Returns a list of dashboards from the specified workspace.

        >>> Params:
            groupId: The group ID
        
        >>> Example:
            >>> dashboards.get_dashboards_in_group('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{groupId}/dashboards"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_tile(self, dashboardId:str, tileId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-tile
        
        Returns the specified tile within the specified dashboard from My workspac

        >>> Params:
            dashboardId: The dashboard ID
            tileId: The tile ID
        
        >>> Example:
            >>> dashboards.get_tile("69ffaa6c-b36d-4d01-96f5-1ed67c64d4af", "312fbfe9-2eda-44e0-9ed0-ab5dc571bb4b")
        
        '''
        endpoint = f"dashboards/{dashboardId}/tiles/{tileId}"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response

    def get_tile_in_group(self, groupId:str, dashboardId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-tiles-in-group
        
        Returns a list of tiles within the specified dashboard from the specified workspace

        >>> Params:
            groupId: The group ID
        
        >>> Example:
            >>> dashboards.get_tiles('cfafbeb1-8037-4d0c-896e-a46fb27ff229', '69ffaa6c-b36d-4d01-96f5-1ed67c64d4af')
        
        '''
        endpoint = f"groups/{groupId}/dashboards/{dashboardId}/tiles"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_tiles(self, dashboardId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-tiles
        
        Returns a list of tiles within the specified dashboard from My workspace

        >>> Params:
            dashboardId: The dashboard ID
        
        >>> Example:
            >>> dashboards.get_tiles("69ffaa6c-b36d-4d01-96f5-1ed67c64d4af")
        
        '''
        endpoint = f"dashboards/{dashboardId}/tiles"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_tiles_in_group(self, groupId:str, dashboardId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-tiles-in-group
        
        Returns a list of tiles within the specified dashboard from the specified workspace

        >>> Params:
            groupId: The workspace ID
            dashboardId: The dashboard ID
        
        >>> Example:
            >>> dashboards.get_tiles_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "69ffaa6c-b36d-4d01-96f5-1ed67c64d4af")
        
        '''
        endpoint = f"groups/{groupId}/dashboards/{dashboardId}/tiles"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response

    
