from library.requests import audit_requests

class EmbedToken():
    def __init__(self):
        pass
    
    def dashboards_generate_token(self, groupId:str, dashboardId:str, accessLevel, allowSaveAs:bool, datasetId:str, identities, lifetimeInMinutes:int):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/embed-token/dashboards-generate-token-in-group
        ''' Generates an embed token to view the specified dashboard from the specified workspace

        >>> Params:
            dashboardId: The dashboard ID
            groupId: The workspace ID
            accessLevel: The required access level for embed token generation

            allowSaveAs: Whether an embedded report can be saved as a new report. The default value is false. 
                Only applies when you generate an embed token for report embedding,

            datasetId: The dataset ID used for report creation. Only applies when you generate an embed token for report creation
            identities: A list of identities to use for row-level security rules

            lifetimeInMinutes: The maximum lifetime of the token in minutes, starting from the time it was generated. 
                Can be used to shorten the expiration time of a token, but not to extend it. The value must be a positive integer. 
                    Zero (0) is equivalent to null and will be ignored, resulting in the default expiration time


        >>> Example:
            embedToken.get_app("f089354e-8366-4e18-aea3-4cb4a3a50b48", "69ffaa6c-b36d-4d01-96f5-1ed67c64d4af")
        
        '''
        endpoint = f"groups/{groupId}/dashboards/{dashboardId}/GenerateToken"

        method = 'post'

        body = {
            "accessLevel": accessLevel,
            "allowSaveAs": allowSaveAs,
            "datasetId": datasetId,
            "identities": identities,
            "lifetimeInMinutes": lifetimeInMinutes,
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def datasets_generate_token(self, groupId:str, datasetId:str, accessLevel, allowSaveAs:bool, identities, lifetimeInMinutes:int):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/embed-token/dashboards-generate-token-in-group
        ''' Generates an embed token to view the specified dashboard from the specified workspace

        >>> Params:
            dashboardId: The dashboard ID
            groupId: The workspace ID
            accessLevel: The required access level for embed token generation

            allowSaveAs: Whether an embedded report can be saved as a new report. The default value is false. 
                Only applies when you generate an embed token for report embedding,

            datasetId: The dataset ID used for report creation. Only applies when you generate an embed token for report creation
            identities: A list of identities to use for row-level security rules

            lifetimeInMinutes: The maximum lifetime of the token in minutes, starting from the time it was generated. 
                Can be used to shorten the expiration time of a token, but not to extend it. The value must be a positive integer. 
                    Zero (0) is equivalent to null and will be ignored, resulting in the default expiration time


        >>> Example:
            embedToken.get_app("f089354e-8366-4e18-aea3-4cb4a3a50b48", "69ffaa6c-b36d-4d01-96f5-1ed67c64d4af")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/GenerateToken"

        method = 'post'

        body = {
            "accessLevel": accessLevel,
            "allowSaveAs": allowSaveAs,
            "datasetId": datasetId,
            "identities": identities,
            "lifetimeInMinutes": lifetimeInMinutes,
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def generate_token(self, datasets:dict, datasourceIdentities:dict, identities:dict, lifetimeInMinutes:int, reports:dict, targetWorkspaces:dict):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/embed-token/generate-token#generatetokenrequestv2dataset
        ''' Generates an embed token to view the specified dashboard from the specified workspace

        >>> Params:
            datasets: A list of datasets
            datasourceIdentities: List of identities to use when connecting to data sources with Single Sign-On (SSO) enabled
            identities: A list of identities to use for row-level security rules
            lifetimeInMinutes: The maximum lifetime of the token in minutes, starting from the time it was generated. 
                Can be used to shorten the expiration time of a token, but not to extend it. The value must be a positive integer. 
                    Zero (0) is equivalent to null and will be ignored, resulting in the default expiration time
            reports: A list of reports
            targetWorkspaces: The list of workspaces that the embed token will allow saving to

        >>> Example:
            embedToken.get_app("f089354e-8366-4e18-aea3-4cb4a3a50b48", "69ffaa6c-b36d-4d01-96f5-1ed67c64d4af")
        
        '''
        endpoint = f"GenerateToken"

        method = 'post'

        body = {
            "datasets": datasets,
            "datasourceIdentities": datasourceIdentities,
            "reports": reports,
            "identities": identities,
            "lifetimeInMinutes": lifetimeInMinutes,
            "targetWorkspaces": targetWorkspaces,
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def reports_generate_token_for_create_in_group(self, groupId:str, accessLevel:str, allowSaveAs:bool, datasetId:str, identities:dict, lifetimeInMinutes:int):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/embed-token/reports-generate-token-for-create-in-group
        ''' Generates an embed token to allow report creation in the specified workspace based on the specified dataset

        >>> Params:
            groupId: The workspace ID
            accessLevel: The required access level for embed token generation
            allowSaveAs: Whether an embedded report can be saved as a new report. The default value is false. Only applies when you generate an embed token for report embedding
            datasetId: The dataset ID used for report creation. Only applies when you generate an embed token for report creation
            identities: A list of identities to use for row-level security rules
            lifetimeInMinutes: The maximum lifetime of the token in minutes, starting from the time it was generated


        >>> Example:
            embedToken.reports_generate_token_for_create_in_group()
        
        '''
        endpoint = f"groups/{groupId}/reports/GenerateToken"

        method = 'post'

        body = {
            "accessLevel": accessLevel,
            "allowSaveAs": allowSaveAs,
            "datasetId": datasetId,
            "identities": identities,
            "lifetimeInMinutes": lifetimeInMinutes
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def reports_generate_token(self, groupId:str, reportId:str, accessLevel:str, allowSaveAs:bool, datasetId:str, identities:dict, lifetimeInMinutes:int):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/embed-token/reports-generate-token-for-create-in-group
        ''' Generates an embed token to allow report creation in the specified workspace based on the specified dataset

        >>> Params:
            groupId: The workspace ID
            accessLevel: The required access level for embed token generation
            allowSaveAs: Whether an embedded report can be saved as a new report. The default value is false. Only applies when you generate an embed token for report embedding
            datasetId: The dataset ID used for report creation. Only applies when you generate an embed token for report creation
            identities: A list of identities to use for row-level security rules
            lifetimeInMinutes: The maximum lifetime of the token in minutes, starting from the time it was generated


        >>> Example:
            embedToken.reports_generate_token_for_create_in_group()
        
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}/GenerateToken"

        method = 'post'

        body = {
            "accessLevel": accessLevel,
            "allowSaveAs": allowSaveAs,
            "datasetId": datasetId,
            "identities": identities,
            "lifetimeInMinutes": lifetimeInMinutes
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response

    def tiles_generate_token(self, groupId:str, dashboardId:str, reportId:str, tileId:str, accessLevel:str, allowSaveAs:bool, datasetId:str, identities:dict, lifetimeInMinutes:int):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/embed-token/reports-generate-token-for-create-in-group
        ''' Generates an embed token to allow report creation in the specified workspace based on the specified dataset

        >>> Params:
            groupId: The workspace ID
            accessLevel: The required access level for embed token generation
            allowSaveAs: Whether an embedded report can be saved as a new report. The default value is false. Only applies when you generate an embed token for report embedding
            datasetId: The dataset ID used for report creation. Only applies when you generate an embed token for report creation
            identities: A list of identities to use for row-level security rules
            lifetimeInMinutes: The maximum lifetime of the token in minutes, starting from the time it was generated


        >>> Example:
            embedToken.reports_generate_token_for_create_in_group()
        
        '''
        endpoint = f"groups/{groupId}/dashboards/{dashboardId}/tiles/{tileId}/GenerateToken"

        method = 'post'

        body = {
            "accessLevel": accessLevel,
            "allowSaveAs": allowSaveAs,
            "datasetId": datasetId,
            "identities": identities,
            "lifetimeInMinutes": lifetimeInMinutes
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response