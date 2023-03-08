#library for accessing admin resources
#https://learn.microsoft.com/en-us/rest/api/power-bi/admin
from library.requests import audit_requests
import string

class Admin():
    def __init__(self):
        #self.access_token = access_token
        #self.headers = headers
        pass

    
    def get_groups(self, top:int): 
        ''' Returns a list of workspaces for the organization

        >>> Params:
            top: Returns only the first n results
        
        >>> Example:
            admin.get_groups(100)
        
        '''
        endpoint = f"admin/groups?$top={top}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_group(self, groupId:str): 
        ''' Returns a workspace for the organization

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            admin.get_group(groupId)
        
        '''
        endpoint = f"admin/groups/{groupId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_users(self, groupId:str): 
        ''' Returns a list of users that have access to the specified workspace

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            admin.get_group(groupId)
        
        '''
        endpoint = f"admin/groups/{groupId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def add_user(self, groupId:str, groupUserAccessRight:str, identifier:str, principalType:str): 
        ''' Grants user permissions to the specified workspace

        >>> Params:
            groupId: The workspace ID
            groupUserAccessRight: Permission level Options : Admin, User, Contributor, Member, Viewer, None
            principalType: The principal type Options: User, App, Group
        
        >>> Example:
            admin.add_users("3b5ca243-47d1-4be5-ac56-57c62291607d", "Admin", "john@contoso.com", "User")
        
        '''
        endpoint = f"admin/groups/{groupId}/users"

        string.capwords(groupUserAccessRight)
        string.capwords(principalType)

        body = {
            "groupUserAccessRight": groupUserAccessRight,
            "identifier": identifier,
            "principalType": principalType
        }

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response

    def delete_user(self, groupId:str, user:str): 
        ''' Returns a list of users that have access to the specified workspace

        >>> Params:
            groupId: The workspace ID
            user: The user principal name (UPN) of the user to remove (likely email address)
        
        >>> Example:
            admin.delete_user("3b5ca243-47d1-4be5-ac56-57c62291607d", "john@contoso.com")
        
        '''
        endpoint = f"admin/groups/{groupId}/users/{user}"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_dashboards(self): 
        ''' Returns a list of dashboards for the organization

        >>> Params:
            
        
        >>> Example:
            admin.get_dashboards()
        
        '''
        endpoint = f"admin/dashboards"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dashboards_in_group(self, groupId): 
        ''' Returns a list of dashboards from the specified workspace

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            admin.get_dashboards("3b5ca243-47d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"admin/groups/{groupId}/dashboards"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dashboards_users(self, dashboardId): 
        ''' Returns a list of users that have access to the specified dashboard

        >>> Params:
            dashboardId: The dashboard ID
        
        >>> Example:
            admin.get_dashboards_users("2b5ca223-46d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"admin/dashboards/{dashboardId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dashboards_subscriptions(self, dashboardId): 
        ''' Returns a list of dashboard subscriptions along with subscriber details. This is a preview API call

        >>> Params:
            dashboardId: The dashboard ID
        
        >>> Example:
            admin.get_dashboards_subscriptions("2b5ca223-46d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"admin/dashboards/{dashboardId}/subscriptions"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dashboards_tiles(self, dashboardId): 
        ''' Returns a list of tiles within the specified dashboard

        >>> Params:
            dashboardId: The dashboard ID
        
        >>> Example:
            admin.get_dashboards_tiles("3b5ca243-47d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"admin/dashboards/{dashboardId}/tiles"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_reports(self): 
        ''' Returns a list of reports for the organization

        >>> Params:
            
        
        >>> Example:
            
        
        '''
        endpoint = f"admin/reports"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_reports_in_group(self, groupId): 
        ''' Returns a list of reports from the specified workspace

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            admin.get_reports_in_group("3b5ca243-47d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"admin/groups/{groupId}/reports"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_report_users(self, reportId): 
        ''' Returns a list of users that have access to the specified report

        >>> Params:
            reportId: The report ID
        
        >>> Example:
            
        
        '''
        endpoint = f"admin/reports/{reportId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_report_subscriptions(self, reportId): 
        ''' Returns a list of report subscriptions along with subscriber details. This is a preview API call

        >>> Params:
            reportId: The report ID
        
        >>> Example:
            
        
        '''
        endpoint = f"admin/reports/{reportId}/subscriptions"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_activity_events(self, startDateTime, endDateTime): 
        ''' Returns a list of audit activity events for a tenant

        Provide either a continuation token or both a start and end date time. 
        StartDateTime and EndDateTime must be in the same UTC day and should be 
        wrapped in single quotes

        >>> Params:
            
        
        >>> Example:
            
        
        '''
        endpoint = f"admin/activityevents?startDateTime={startDateTime}&endDateTime={endDateTime}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response