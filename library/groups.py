import requests
from requests.adapters import HTTPAdapter, Retry
from library.login import headers
from library.requests import audit_requests

class Groups():
    def __init__(self):
        #self.access_token = access_token
        self.headers = headers
    
    """ def audit_requests(self, endpoint, method, params = None, data = None, json = None):
        base_url = 'https://api.powerbi.com/v1.0/myorg/'

        url = base_url + endpoint

        session = requests.session()

        
        re_attempt = Retry(
                    total=5,
                    backoff_factor=0.1,
                    status_forcelist=[ 500, 502, 503, 504 ]
                )

        session.mount('http://', HTTPAdapter(max_retries=re_attempt)) 
       

        new_request = requests.Request(
            method=method.upper(),
            headers=headers,
            url=url,
            params=params,
            data=data,
            json=json,
        ).prepare()

        response: requests.Response = session.send(
            request=new_request
        )

        session.close()

        try:
            if response.ok:
                return response.json()
            else:
                return response
        except KeyError as e:
            return e
 """
    #GET REQUESTS
    def get_groups(self, top:int): 
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

    def get_users(self, group_id:str):
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
    

    #POST REQUESTS
    def create_group(self, name, workspaceV2=True):
        ''' Create a workspace

        >>> Params:
            workspaceV2: (Preview feature) Whether to create a workspace. The only supported value is true.
        
        >>> Example:
            groups.create_group(name='test_worksapce', workspaceV2 = True)
        
        '''
        body = {'name': name}

        endpoint = f"groups?workspaceV2={workspaceV2}"

        method = 'post'

        response = audit_requests(endpoint, method, json=body)

        return response

    def add_user_as_admin(self, group_id, body):
        ''' Returns a list of users that have access to the specified workspace

        >>> Params:
            groupID: The workspace ID
 
            body: Request Body = {
                "groupUserAccessRight": "Required",
                "principalType": "Required",
                "identifier": "Required",
            }
        
        >>> Example:
            body = {
                "groupUserAccessRight": "Admin",
                "displayName": "API Principle",
                "identifier": "f724c865-ab43-4fb5-81a3-4d937623313e",
                "principalType": "App"
            }
            groups.get_users('f089354e-8366-4e18-aea3-4cb4a3a50b48', body)
        
        '''
        endpoint = f"https://api.powerbi.com/v1.0/myorg/admin/groups/{group_id}/users"

        method = 'post'
        
        response = requests.post(endpoint, headers=self.headers, json=body)

        print(response.status_code)

    #DELETE REQUESTS
    def delete_group(self, group_id):
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

    def delete_user(self, group_id):
        ''' Deletes the specified user permissions from the specified workspace

        >>> Params:
            group_id: The workspace ID of the to be deleted workspace
        
        >>> Example:
            groups.delete_group('f089354e-8366-4e18-aea3-4cb4a3a50b48')
        
        '''
        endpoint = f"groups/{group_id}"

        method = "delete"

        response = audit_requests(endpoint, method)

        return response.status_code
    


