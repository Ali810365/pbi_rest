import requests
import string
from requests.adapters import HTTPAdapter, Retry
from library.requests import audit_requests

class Groups():
    def __init__(self):
        #self.access_token = access_token
        #self.headers = headers
        pass
    
    def add_user(self, groupId:str, groupUserAccessRight:str, identifier:str, principalType:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/groups/add-group-user 
        ''' Grants user permissions to the specified workspace

        >>> Params:
            groupId: The workspace ID
            groupUserAccessRight: Permission level Options : Admin, User, Contributor, Member, Viewer, None
            identifier: Identifier of the principal (generally email)
            principalType: The principal type Options: User, App, Group
        
        >>> Example:
            group.add_user("3b5ca243-47d1-4be5-ac56-57c62291607d", "Admin", "john@contoso.com", "User")
        
        '''
        endpoint = f"groups/{groupId}/users"

        body = {
            "groupUserAccessRight": string.capwords(groupUserAccessRight),
            "identifier": identifier,
            "principalType": string.capwords(principalType)
        }

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        if response['status_code'] == 200:

            return f"\nsuccessfully added {identifier} as {groupUserAccessRight}"
        
        return response
    
    def create_group(self, name, workspaceV2=True):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/groups/create-group
        ''' Create a workspace

        >>> Params:
            workspaceV2: (Preview feature) Whether to create a workspace. The only supported value is true.
        
        >>> Example:
            groups.create_group(name='test_worksapce')
        
        '''
        body = {'name': name}

        endpoint = f"groups?workspaceV2={workspaceV2}"

        method = 'post'

        response = audit_requests(endpoint, method, json=body)

        return response
    
    def delete_group(self, group_id):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/groups/delete-group
        ''' Deletes the specified workspace

        >>> Params:
            group_id: The workspace ID of the to be deleted workspace
        
        >>> Example:
            groups.delete_group('f089354e-8366-4e18-aea3-4cb4a3a50b48')
        
        '''
        endpoint = f"groups/{group_id}"

        method = 'delete'

        response = audit_requests(endpoint, method)

        return response
    
    def delete_user(self, group_id, user=None, profileID=None):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/groups/delete-user-in-group
        ''' Deletes the specified user permissions from the specified workspace

        >>> Params:
            group_id: The workspace ID of the to be deleted workspace
        
        >>> Example:
            groups.delete_user("3b5ca243-47d1-4be5-ac56-57c62291607d", "john@contoso.com")
        
        '''
        endpoint = f"groups/{group_id}/users/{user}"

        body = {
            "user": user,
            "profileID": profileID
        }

        method = "delete"

        response = audit_requests(endpoint, method, json=body)

        return response
    

    def get_users(self, group_id:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/groups/get-group-users
        ''' Returns a list of users that have access to the specified workspace

        >>> Params:
            group_id: The workspace ID
        
        >>> Example:
            groups.get_users('f089354e-8366-4e18-aea3-4cb4a3a50b48')
        
        '''
        endpoint = f"groups/{group_id}/users"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response


    def get_groups(self, top:int):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/groups/get-groups 
        ''' Returns a list of workspaces the user has access to

        >>> Params:
            top: Returns only the first n results
        
        >>> Example:
            groups.get_groups(100)
        
        '''
        endpoint = f"groups?$top={top}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    
    def update_user(self, groupId:str, groupUserAccessRight:str, identifier:str, principalType:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/groups/update-group-user 
        ''' Updates the specified user permissions to the specified workspace

        >>> Params:
            groupId: The workspace ID
            groupUserAccessRight: Permission level Options : Admin, User, Contributor, Member, Viewer, None
            identifier: Identifier of the principal (generally email)
            principalType: The principal type Options: User, App, Group
        
        >>> Example:
            group.add_user("3b5ca243-47d1-4be5-ac56-57c62291607d", "Admin", "john@contoso.com", "User")
        
        '''

        endpoint = f"groups/{groupId}/users"

        body = {
            "groupUserAccessRight": string.capwords(groupUserAccessRight),
            "identifier": identifier,
            "principalType": string.capwords(principalType)
        }

        method = 'put'
        
        response = audit_requests(endpoint, method, json=body)
        
        if response['status_code'] == 200:

            return f"\nsuccessfully updated {identifier} as {groupUserAccessRight}"
        
        return response

    
    

    
    


