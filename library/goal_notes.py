from library.requests import audit_requests

class GoalNotes():
    def __init__(self):
        pass

    def delete_by_id(self, groupId:str, scorecardId:str, goalId:str, timestamp:str, noteId:str,):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goalnotes_(preview)/delete-by-id
        
        Deletes a goal value check-in note by ID

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal
            timestamp: The timestamp for the value of the goal
            noteId: The unique identifier of the goal check-in note

        >>> Example:
            goalNotes.delete_by_id("bc390256-fa54-4bd8-96a1-2c80df0cf704", "ce4abf44-3c4a-4425-893d-36bcca75a42b", "871f5b6e-e5a3-421f-924d-847b68db239f", "2021-12-14T00:00:00Z", "4370bfc0-4cad-481d-981f-80848016da97")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/goalValues({timestamp})/notes({noteId})"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def patch_by_id(self, groupId:str, scorecardId:str, goalId:str, timestamp:str, noteId:str, body:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goalnotes_(preview)/patch-by-id
        
        Updates a goal value check-in note by ID

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal
            timestamp: The timestamp for the value of the goal
            noteId: The unique identifier of the goal check-in note
            body: The note text

        >>> Example:
            goalNotes.patch_by_id("bc390256-fa54-4bd8-96a1-2c80df0cf704", "ce4abf44-3c4a-4425-893d-36bcca75a42b", "871f5b6e-e5a3-421f-924d-847b68db239f", "2021-12-14T00:00:00Z", "4370bfc0-4cad-481d-981f-80848016da97", "Testing Updated Notes")
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/goalValues({timestamp})/notes({noteId})"

        method = 'patch'

        body= {
            "body": body
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def post(self, groupId:str, scorecardId:str, goalId:str, timestamp:str, body:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/goalnotes_(preview)/post
        
        Adds a new note to a goal value check-in

        >>> Params:
            groupId: The workspace ID
            scorecardId: The unique identifier of the scorecard
            goalId: The unique identifier of the goal
            timestamp: The timestamp for the value of the goal
            body: The note text
        
        >>> Example:
            goalNotes.post("bc390256-fa54-4bd8-96a1-2c80df0cf704", "ce4abf44-3c4a-4425-893d-36bcca75a42b", "871f5b6e-e5a3-421f-924d-847b68db239f", "2021-12-14T00:00:00Z", "Testing Notes")
        
        '''
        endpoint = f"groups/{groupId}/scorecards({scorecardId})/goals({goalId})/goalValues({timestamp})/notes"

        method = 'post'
        
        response = audit_requests(endpoint, method)
        
        return response
