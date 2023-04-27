from library.requests import audit_requests

class Goals():
    def __init__(self):
        pass

    def delete_by_id(self, groupId:str, scorecardId:str, goalId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goals_(preview)/delete-by-id
        
        Deletes a goal from a scorecard by goal ID

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal

        >>> Example:
            goalNotes.delete_by_id("bc390256-fa54-4bd8-96a1-2c80df0cf704", "f74738b3-c62d-4487-838c-918d314556ee", "c07b3600-54be-42ef-9154-39e7922c1bb4")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def delete_goal_current_value(self, groupId:str, scorecardId:str, goalId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goals_(preview)/delete-goal-current-value-connection
        
        Disconnects the current value of a goal

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal

        >>> Example:
            goals.delete_goal_current_value("bc390256-fa54-4bd8-96a1-2c80df0cf704", "f74738b3-c62d-4487-838c-918d314556ee", "c07b3600-54be-42ef-9154-39e7922c1bb4")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/DeleteGoalCurrentValueConnection()"

        method = 'post'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def delete_goal_target_value(self, groupId:str, scorecardId:str, goalId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goals_(preview)/delete-goal-target-value-connection
        
        Disconnects the target value of a goal

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal

        >>> Example:
            goals.delete_goal_target_value("bc390256-fa54-4bd8-96a1-2c80df0cf704", "f74738b3-c62d-4487-838c-918d314556ee", "c07b3600-54be-42ef-9154-39e7922c1bb4")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/DeleteGoalTargetValueConnection()"

        method = 'post'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get(self, groupId:str, scorecardId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goals_(preview)/get
        
        Returns a list of goals from a scorecard

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard

        >>> Example:
            goals.get("bc390256-fa54-4bd8-96a1-2c80df0cf704", "bc390256-fa54-4bd8-96a1-2c80df0cf704)")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_by_id(self, groupId:str, scorecardId:str, goalId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goals_(preview)/get-by-id
        
        Returns a goal by ID from a scorecard

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal

        >>> Example:
            goals.get_by_id("bc390256-fa54-4bd8-96a1-2c80df0cf704", "bb2b6321-2b84-4b7b-8de3-40f74ca7e586", "62e3794e-6019-4195-8f5e-38d9a6e18c04")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_refresh_history(self, groupId:str, scorecardId:str, goalId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goals_(preview)/get-refresh-history
        
        Reads refresh history of a connected goal

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal

        >>> Example:
            goals.get_refresh_history("bc390256-fa54-4bd8-96a1-2c80df0cf704", "bb2b6321-2b84-4b7b-8de3-40f74ca7e586", "62e3794e-6019-4195-8f5e-38d9a6e18c04")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/GetRefreshHistory()"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def patch_by_id(self, groupId:str, scorecardId:str, goalId:str, body:None):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goals_(preview)/patch-by-id
        
        Updates a goal by ID

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal

        >>> Example:
            goals.patch_by_id("bc390256-fa54-4bd8-96a1-2c80df0cf704", "bb2b6321-2b84-4b7b-8de3-40f74ca7e586", "62e3794e-6019-4195-8f5e-38d9a6e18c04", request_body)
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})"

        method = 'patch'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def post(self, groupId:str, scorecardId:str, body:None):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goals_(preview)/post
        
        Adds a new goal to a scorecard

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard

        >>> Example:
            goals.post("bc390256-fa54-4bd8-96a1-2c80df0cf704", "bb2b6321-2b84-4b7b-8de3-40f74ca7e586")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals"

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def refresh_goal_current(self, groupId:str, scorecardId:str, goalId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goals_(preview)/refresh-goal-current-value
        
        Schedules a refresh of the connected value of a goal

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal

        >>> Example:
            goals.refresh_goal_current("bc390256-fa54-4bd8-96a1-2c80df0cf704", "bb2b6321-2b84-4b7b-8de3-40f74ca7e586", "62e3794e-6019-4195-8f5e-38d9a6e18c04")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/RefreshGoalCurrentValue()"

        method = 'post'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def refresh_goal_target(self, groupId:str, scorecardId:str, goalId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goals_(preview)/refresh-goal-current-value
        
        Schedules a refresh of the connected value of a goal

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal

        >>> Example:
            goals.refresh_goal_target("bc390256-fa54-4bd8-96a1-2c80df0cf704", "bb2b6321-2b84-4b7b-8de3-40f74ca7e586", "62e3794e-6019-4195-8f5e-38d9a6e18c04")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/RefreshGoalTargetValue()"

        method = 'post'
        
        response = audit_requests(endpoint, method)
        
        return response
    

    