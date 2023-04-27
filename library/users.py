from library.requests import audit_requests

class Users():
    def __init__(self):
        pass
    
    def refresh_user_premissions(self, installDetails):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/users/refresh-user-permissions
        
        Refreshes user permissions in Power BI

        When a user is granted permissions to a workspace, app, or Power BI item (such as a report or a dashboard), the new permissions might not be immediately available through API calls. This operation refreshes user permissions to ensure they're fully updated

        >>> Example:
            users.refresh_user_premissions()
        
        '''
        endpoint = f"RefreshUserPermissions"

        method = 'post'
        
        response = audit_requests(endpoint, method)
        
        return response