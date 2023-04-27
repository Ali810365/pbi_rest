from library.requests import audit_requests

class Goals():
    def __init__(self):
        pass

    def delete(self, groupId:str, scorecardId:str, goalId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goalsstatusrules_(preview)/delete
        
        Removes status rule definitions from a goal

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal

        >>> Example:
            goals.delete("bc390256-fa54-4bd8-96a1-2c80df0cf704", "f74738b3-c62d-4487-838c-918d314556ee", "c07b3600-54be-42ef-9154-39e7922c1bb4")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/statusRules"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get(self, groupId:str, scorecardId:str, goalId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goalsstatusrules_(preview)/get
        
        Returns status rules of a goal

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal

        >>> Example:
            goals.get("bc390256-fa54-4bd8-96a1-2c80df0cf704", "bb2b6321-2b84-4b7b-8de3-40f74ca7e586", "62e3794e-6019-4195-8f5e-38d9a6e18c04")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/statusRules"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def post(self, groupId:str, scorecardId:str, goalId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goalsstatusrules_(preview)/post
        
        Creates or updates status rules of a goal

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal

        >>> Example:
            goals.post("")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/statusRules"

        method = 'post'
        
        response = audit_requests(endpoint, method)
        
        return response