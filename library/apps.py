from library.requests import audit_requests

class Apps():
    def __init__(self):
        pass
    
    def get_app(self, appId:str,):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/apps/get-app
        ''' Returns the specified installed app

        >>> Params:
            appId: The app ID
        
        >>> Example:
            apps.get_app("3b5ca243-47d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"apps/{appId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_apps(self):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/apps/get-apps
        ''' Returns a list of installed apps

        >>> Params:
            appId: The app ID
        
        >>> Example:
            apps.get_app("3b5ca243-47d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"apps"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dashboard(self, appId:str, dashboardId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/apps/get-dashboard
        ''' Returns the specified dashboard from the specified app.

        >>> Params:
            appId: The app ID
            dashboardId: The dashboard ID
        
        >>> Example:
            apps.get_dashboard("3d9b93c6-7b6d-4801-a491-1738910904fd", "03dac094-2ff8-47e8-b2b9-dedbbc4d22ac")
        
        '''
        endpoint = f"apps/{appId}/dashboards/{dashboardId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dashboards(self, appId:str,):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/apps/get-dashboards
        ''' Returns a list of dashboards from the specified app

        >>> Params:
            appId: The app ID
        
        >>> Example:
            
        
        '''
        endpoint = f"apps/{appId}/dashboards"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_report(self, appId:str, reportId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/apps/get-report
        ''' Returns the specified report from the specified app

        >>> Params:
            appId: The app ID
            reportId: The report ID
        
        >>> Example:
            apps.get_report("3d9b93c6-7b6d-4801-a491-1738910904fd", "cfafbeb1-8037-4d0c-896e-a46fb27ff229" )
        
        '''
        endpoint = f"apps/{appId}/reports/{reportId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_reports(self, appId:str,):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/apps/get-reports
        ''' Returns a list of reports from the specified app

        >>> Params:
            appId: The app ID
        
        >>> Example:
            apps.get_reports("3d9b93c6-7b6d-4801-a491-1738910904fd")
        
        '''
        endpoint = f"apps/{appId}/reports"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_tile(self, appId:str, dashboardId:str, tileId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/apps/get-tile
        ''' Returns the specified tile within the specified dashboard from the specified app

        >>> Params:
            appId: The app ID
            dashboardId: The dashboard ID
            tileId: The tile ID
        
        >>> Example:
            apps.get_tile("312fbfe9-2eda-44e0-9ed0-ab5dc571bb4b", "69ffaa6c-b36d-4d01-96f5-1ed67c64d4af&tileId=312fbfe9-2eda-44e0-9ed0-ab5dc571bb4b", "312fbfe9-2eda-44e0-9ed0-ab5dc571bb4b")
        
        '''
        endpoint = f"apps/{appId}/dashboards/{dashboardId}/tiles/{tileId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_tiles(self, appId:str, dashboardId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/apps/get-tiles
        ''' Returns a list of tiles within the specified dashboard from the specified app

        >>> Params:
            appId: The app ID
            dashboardId: The dashboard ID
        
        >>> Example:
            apps.get_tiles("312fbfe9-2eda-44e0-9ed0-ab5dc571bb4b", "69ffaa6c-b36d-4d01-96f5-1ed67c64d4af&tileId=312fbfe9-2eda-44e0-9ed0-ab5dc571bb4b")
        '''
        endpoint = f"apps/{appId}/dashboards/{dashboardId}/tiles"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response


    def sample(self, appId:str,):
        #
        ''' Sample

        >>> Params:
            
        
        >>> Example:
            
        
        '''
        endpoint = f"apps/"

        method = ''
        
        response = audit_requests(endpoint, method)
        
        return response