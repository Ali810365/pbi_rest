from library.requests import audit_requests

class GoalValues():
    def __init__(self):
        pass
    
    def delete_by_id(self, groupId:str, scorecardId:str, goalId:str, timestamp:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goalvalues_(preview)/delete-by-id
        
        Deletes a goal value check-in by a UTC day timestamp

        >>> Params:
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal
            timestamp: The timestamp for the value of the goal
        
        >>> Example:
            goalValues.delete_by_id("bc390256-fa54-4bd8-96a1-2c80df0cf704", "f74738b3-c62d-4487-838c-918d314556ee", "c07b3600-54be-42ef-9154-39e7922c1bb4", "2021-12-14T00:00:00Z")
        
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/goalValues({timestamp})"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get(self, groupId:str, scorecardId:str, goalId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goalvalues_(preview)/get
        
        Reads goal value check-ins

        >>> Params:
            groupId: The workspace ID
            goalId: The unique identifier of the goal
            scorecardId: The unique identifier of the scorecard
        
        >>> Example:
            goalValues.get("bc390256-fa54-4bd8-96a1-2c80df0cf704", "299759d9-80d3-45a8-8f13-a0624ea7e388", "de3e8b13-1ba6-4806-871f-2fb1658e0837")
        
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/goalValues"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_by_id(self, groupId:str, scorecardId:str, goalId:str, timestamp:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goalvalues_(preview)/get
        
        Reads a goal value check-in by a UTC date timestamp

        >>> Params:
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal
            timestamp: The timestamp for the value of the goal
        
        >>> Example:
            goalValues.get_by_id("bc390256-fa54-4bd8-96a1-2c80df0cf704", "ce4abf44-3c4a-4425-893d-36bcca75a42b", "871f5b6e-e5a3-421f-924d-847b68db239f", "2021-12-14T00:00:00Z")
        
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/goalValues({timestamp})"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def patch_by_id(self, groupId:str, scorecardId:str, goalId:str, timestamp:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goalvalues_(preview)/get
        
        Reads a goal value check-in by a UTC date timestamp

        >>> Params:
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal
            timestamp: The timestamp for the value of the goal
        
        >>> Example:
            goalValues.get_by_id("bc390256-fa54-4bd8-96a1-2c80df0cf704", "ce4abf44-3c4a-4425-893d-36bcca75a42b", "871f5b6e-e5a3-421f-924d-847b68db239f", "2021-12-14T00:00:00Z")
        
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/goalValues({timestamp})"

        method = 'patch'
        
        response = audit_requests(endpoint, method)
        
        return response
    


    def post(self, groupId:str, scorecardId:str, goalId:str,):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goalvalues_(preview)/post
        
        Creates a new goal value check-in

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            goalValues.post("")
        
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/goalValues"

        method = 'post'
        
        response = audit_requests(endpoint, method)
        
        return response