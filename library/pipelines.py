from library.requests import audit_requests

class Pipelines():
    def __init__(self):
        #self.access_token = access_token
        #self.headers = headers
        pass
    
    def assign_workspace(self, pipelineId:str, stageOrder:str, workspaceId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/assign-workspace
        ''' Assigns the specified workspace to the specified deployment pipeline stage

        >>> Params:
            pipelineId: The deployment pipeline ID
            stageOrder: The deployment pipeline stage order. Development (0), Test (1), Production (2)
            workspaceId: The workspace ID
        
        >>> Example:
            pipelines.assign_workspace("a5ded933-57b7-41f4-b072-ed4c1f9d582", "0", "4de5bcc4-2c88-4efe-b827-4ee7b289b496")
        
        '''
        endpoint = f"pipelines/{pipelineId}/stages/{stageOrder}/assignWorkspace"

        body = {
            "workspaceId": workspaceId
            
        }

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def create_pipeline(self, displayName:str, description:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/create-pipeline
        ''' Creates a new deployment pipeline

        >>> Params:
            displayName: The display name for the new deployment pipeline
            description: The description for the new deployment pipeline
            
        
        >>> Example:
            pipelines.sample()
        
        '''
        endpoint = f"pipelines"

        body = {
            "displayName": displayName,
            "description": description
        }

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response

    def delete_pipeline(self, pipelineId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/delete-pipeline
        ''' Deletes the specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
            
        
        >>> Example:
            pipelines.sample("a5ded933-57b7-41f4-b072-ed4c1f9d5824")
        
        '''
        endpoint = f"pipelines/{pipelineId}"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def delete_pipeline_user(self, pipelineId:str, identifier:str,):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/delete-pipeline-user
        ''' Removes user permissions from the specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
            identifier: To delete user pipeline permissions, provide the user principal name (UPN) of the user.
            
        
        >>> Example:
            pipelines.delete_pipeline_user("8ce96c50-85a0-4db3-85c6-7ccc3ed46523", "5dba60b0-d9a7-42a3-b12c-6d9d51e7739a")
        
        '''
        endpoint = f"pipelines/{pipelineId}/users/{identifier}"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def deploy_all(self, pipelineId:str, sourceStageOrder:int):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/deploy-all
        ''' Deploys all supported items from the source stage of the specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
            sourceStageOrder: The numeric identifier of the pipeline deployment stage that the content should be deployed from. Development (0), Test (1), Production (2)
            
        
        >>> Example:
            pipelines.deploy_all("a5ded933-57b7-41f4-b072-ed4c1f9d5824", 0)
        
        '''
        endpoint = f"pipelines/{pipelineId}/deployAll"

        body = {
            "sourceStageOrder": sourceStageOrder
        }

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    

    def get_pipeline(self, pipelineId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/get-pipeline
        ''' Returns the specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
            
        
        >>> Example:
            pipelines.get_pipeline("a5ded933-57b7-41f4-b072-ed4c1f9d5824")
        
        '''
        endpoint = f"pipelines/{pipelineId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_pipeline_operation(self, pipelineId:str, operationId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/get-pipeline-operation
        ''' Returns the details of the specified deploy operation performed on the specified deployment pipeline, including the deployment execution plan

        >>> Params:
            pipelineId: The deployment pipeline ID
            operationId: The operation ID
            
        
        >>> Example:
            pipelines.get_pipeline_operation("a5ded933-57b7-41f4-b072-ed4c1f9d5824", "1065e6a3-a020-4c0c-ada7-92b5fe99eec5")
        
        '''
        endpoint = f"pipelines/{pipelineId}/operations/{operationId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_pipeline_operations(self, pipelineId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/get-pipeline-operations
        ''' Returns a list of the up-to-20 most recent deploy operations performed on the specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
            
        >>> Example:
            pipelines.get_pipeline_operations("a5ded933-57b7-41f4-b072-ed4c1f9d5824")
        
        '''
        endpoint = f"pipelines/{pipelineId}/operations"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_pipeline_stage_artifacts(self, pipelineId:str, stageOrder:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/get-pipeline-stage-artifacts
        ''' Returns the supported items from the workspace assigned to the specified stage of the specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
            stageOrder: The deployment pipeline stage order. Development (0), Test (1), Production (2)
            
        
        >>> Example:
            pipelines.get_pipeline_stage_artifacts("a5ded933-57b7-41f4-b072-ed4c1f9d5824", 1)
        
        '''
        endpoint = f"pipelines/{pipelineId}/stages/{stageOrder}/artifacts"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_pipeline_stages(self, pipelineId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/get-pipeline-stages
        ''' Returns the stages of the specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
            
            
        
        >>> Example:
            pipelines.get_pipeline_stages("a5ded933-57b7-41f4-b072-ed4c1f9d5824")
        
        '''
        endpoint = f"pipelines/{pipelineId}/stages"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_pipeline_users(self, pipelineId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/get-pipeline-users
        ''' Returns a list of users that have access to the specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
            
        
        >>> Example:
            pipelines.get_pipeline_users("8ce96c50-85a0-4db3-85c6-7ccc3ed46523")
        
        '''
        endpoint = f"pipelines/{pipelineId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_pipelines(self):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/get-pipelines
        ''' Returns a list of deployment pipelines that the user has access to

        >>> Params:
        
        >>> Example:
            pipelines.get_pipelines()
        
        '''
        endpoint = f"pipelines"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def selective_deploy(self, pipelineId:str, sourceStageOrder:int):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/selective-deploy
        ''' Deploys the specified items from the source stage of the specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
            sourceStageOrder: The numeric identifier of the pipeline deployment stage that the content should be deployed from. Development (0), Test (1), Production (2)
            
        >>> Example:
            pipelines.selective_deploy("a5ded933-57b7-41f4-b072-ed4c1f9d5824", 0)
        
        '''
        endpoint = f"pipelines/{pipelineId}/deploy"

        body = {
            "sourceStageOrder": sourceStageOrder
        }

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def unassign_workspace(self, pipelineId:str, stageOrder:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/unassign-workspace
        ''' Unassigns the workspace from the specified stage in the specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
            stageOrder: The deployment pipeline stage order. Development (0), Test (1), Production (2)
            
        
        >>> Example:
            pipelines.unassign_workspace("a5ded933-57b7-41f4-b072-ed4c1f9d5824". 0)
        
        '''
        endpoint = f"pipelines/{pipelineId}/stages/{stageOrder}/unassignWorkspace"

        body = {
            "stageOrder": stageOrder
            
        }

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def update_pipeline(self, pipelineId:str, description:str, displayName:str):
        
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/update-pipeline
        
        Updates the specified deployment pipeline.

        >>> Params:
            pipelineId: The deployment pipeline ID
            description: The updated description for the deployment pipeline
            displayName: The updated display name for the deployment pipeline
            
        >>> Example:
            pipelines.update_pipeline("a5ded933-57b7-41f4-b072-ed4c1f9d5824", description, displayName)
        
        '''
        endpoint = f"pipelines/{pipelineId}"

        body = {
            "description": description,
            "displayName": displayName
        }

        method = 'patch'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def update_pipeline_user(self, pipelineId:str, identifier:str, principalType:str, accessRight:str):
        ''' 
        https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/update-pipeline-user

        Grants user permissions to the specified deployment pipeline
        
        >>> Params:
            pipelineId: The deployment pipeline ID
            identifier: For principal type User, provide the UPN. Otherwise provide the object ID of the principal
            principalType: The principal type
            accessRight: Required. The access right a user has for the deployment pipeline
            
        
        >>> Example:
            pipelines.sample()
        
        '''
        endpoint = f"pipelines/{pipelineId}/users"

        body = {
            "identifier": identifier,
            "principalType": principalType,
            "accessRight": accessRight
            
        }

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response

