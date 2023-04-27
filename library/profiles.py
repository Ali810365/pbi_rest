from library.requests import audit_requests

class Profiles():
    def __init__(self):
        pass
    
    def create_profile(self, displayName:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/profiles/create-profile

        Creates a new service principal profile
        
        Creates a new profile that belongs to service principal caller

        >>> Params:
            displayName: 
        
        >>> Example:
            profiles.create_profile("My new profile")
        
        '''
        endpoint = f"profiles"

        method = 'post'

        body = {
            "displayName": displayName
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def delete_profile(self, profileId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/profiles/delete-profile

        Deletes the specified service principal profile

        Deletes the specified profile if it exists and belongs to service principal caller

        >>> Params:
            profileId: The service principal profile ID
        
        >>> Example:
            profiles.delete_profile("b3ded933-57b7-21f4-b072-ed4c1f9d5824")
        
        '''
        endpoint = f"profiles/{profileId}"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_profile(self, profileId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/profiles/get-profile

        Returns the specified service principal profile

        Returns the specified profile if it exists and belongs to service principal caller

        >>> Params:
            profileId: The service principal profile ID
        
        >>> Example:
            profiles.get_profile("b2ded813-54b7-43f4-b072-ed4c1f9d5824")
        
        '''
        endpoint = f"profiles/{profileId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    

    def get_profiles(self):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/profiles/get-profiles

        Returns a list of service principal profiles

        Returns a list of profiles that belongs to service principal caller

        >>> Params:
            displayName: 
        
        >>> Example:
            profiles.get_profiles()
        
        '''
        endpoint = f"get"

        method = 'profiles'
        
        response = audit_requests(endpoint, method)
        
        return response
    

    def update_profile(self, profileId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/profiles/update-profile

        Updates the specified service principal profile name

        Updates the specified profile name if it exists and belongs to service principal caller

        >>> Params:
            profileId: The service principal profile ID
        
        >>> Example:
            profiles.update_profile("b3ded933-57b7-21f4-b072-ed4c1f9d5824")
        
        '''
        endpoint = f"profiles/{profileId}"

        method = 'put'
        
        response = audit_requests(endpoint, method)
        
        return response
    


   