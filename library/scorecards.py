from library.requests import audit_requests

class Scorecards():
    def __init__(self):
        pass


    def delete_by_id(self, groupId:str, scorecardId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/scorecards_(preview)/delete-by-id
        
        Deletes a scorecard by its ID

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
        
        >>> Example:
            scorecards.delete_by_id("bc390256-fa54-4bd8-96a1-2c80df0cf704", "f74738b3-c62d-4487-838c-918d314556ee")
        
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get(self, groupId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/scorecards_(preview)/get
        
        Returns a list of scorecards from a workspace

        >>> Params:
            groupId: The workspace ID
           
        
        >>> Example:
            scorecards.get("bc390256-fa54-4bd8-96a1-2c80df0cf704")
        
        '''
        endpoint = f"groups/{groupId}/scorecards"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_by_id(self, groupId:str, scorecardId:str):
        ''' #######################
        
        sample

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
        
        >>> Example:
            scorecards.get_by_id("bc390256-fa54-4bd8-96a1-2c80df0cf704", "f74738b3-c62d-4487-838c-918d314556ee")
        
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_scorecard_by_report_id(self, groupId:str, reportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/scorecards_(preview)/get-scorecard-by-report-id
        
        Reads a scorecard associated with an internal report ID

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
        
        >>> Example:
            scorecards.get_scorecard_by_report_id("bc390256-fa54-4bd8-96a1-2c80df0cf704", "312dc8e4-e644-4a3a-93d8-2317c69a86ee")
        
        '''
        endpoint = f"groups/{groupId}/scorecards/GetScorecardByReportId(reportId={reportId})"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def move_goals(self, groupId:str, scorecardId:str, goalToMove):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/scorecards_(preview)/move-goals
        
        Moves goals within the scorecard. Changes their ranks and parents

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
        
        >>> Example:
            scorecards.move_goals("bc390256-fa54-4bd8-96a1-2c80df0cf704", "de582f5f-ac1d-4b9d-8232-d1f5781f46ab")
        
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/MoveGoals()"

        method = 'post'

        body = {
            "goalToMove": goalToMove
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def patch_by_id(self, groupId:str, scorecardId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/scorecards_(preview)/patch-by-id
        
        Updates a scorecard by its ID

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
        
        >>> Example:
            scorecards.patch_by_id("bc390256-fa54-4bd8-96a1-2c80df0cf704", "f74738b3-c62d-4487-838c-918d314556ee")
        
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})"

        method = 'patch'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def post(self, groupId:str, name:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/scorecards_(preview)/post
        
        Creates a new scorecard

        >>> Params:
            groupId: The workspace ID
            name: The scorecard name
        
        >>> Example:
            scorecards.post("bc390256-fa54-4bd8-96a1-2c80df0cf704")
        
        '''
        endpoint = f"groups/{groupId}/scorecards"

        method = 'post'

        body = {
            "name": name
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    


    