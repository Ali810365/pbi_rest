from datetime import datetime, timedelta
from library.date_conversion import FormateDate
from library.requests import audit_requests

class Datasets():
    def __init__(self):
        pass

    def bind_to_gateway(self, datasetId:str, gatewayObjectId:str, datasourceObjectIds:str=None):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/bind-to-gateway
        
        Binds the specified dataset from My workspace to the specified gateway, optionally with a given set of data source IDs.

        If you don't supply a specific data source ID, the dataset will be bound to the first matching data source in the gateway.

        >>> Params:
            datasetId: The dataset ID
            gatewayObjectId: The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster and is similar to the gateway cluster ID
            datasourceObjectIds: The unique identifiers for the data sources in the gateway
            
        >>> Example:
            >>> datasets.bind_to_gateway("cfafbeb1-8037-4d0c-896e-a46fb27ff229", gatewayObjectId)
        
        '''
        endpoint = f"datasets/{datasetId}/Default.BindToGateway"

        body = {
            "gatewayObjectId": gatewayObjectId
        }

        if(datasourceObjectIds):
            body = {
            "gatewayObjectId": gatewayObjectId,
            "datasourceObjectIds": datasourceObjectIds
        }

        method = 'post'

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def bind_to_gateway_in_group(self, groupId:str, datasetId:str, gatewayObjectId:str, datasourceObjectIds:str=None):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/bind-to-gateway-in-group
        
        Binds the specified dataset from My workspace to the specified gateway, optionally with a given set of data source IDs.

        If you don't supply a specific data source ID, the dataset will be bound to the first matching data source in the gateway.

        >>> Params:
            datasetId: The dataset ID
            groupId: The workspace ID
            gatewayObjectId: The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster and is similar to the gateway cluster ID
            datasourceObjectIds: The unique identifiers for the data sources in the gateway
            
        >>> Example:
            >>> datasets.bind_to_gateway_in_group("cfafbeb1-8037-4d0c-896e-a46fb27ff229", gatewayObjectId)
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/Default.BindToGateway"

        body = {
            "gatewayObjectId": gatewayObjectId
        }

        if(datasourceObjectIds):
            body = {
            "gatewayObjectId": gatewayObjectId,
            "datasourceObjectIds": datasourceObjectIds
        }

        method = 'post'

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def cancel_refresh(self, datasetId:str, refreshId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/cancel-refresh
        
        Cancels the specified refresh operation for the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            refreshId: The refresh ID
            
        >>> Example:
            >>> datasets.cancel_refresh("cfafbeb1-8037-4d0c-896e-a46fb27ff229", "87f31ef7-1e3a-4006-9b0b-191693e79e9e")
        
        '''
        endpoint = f"datasets/{datasetId}/refreshes/{refreshId}"

        method = 'delete'

        response = audit_requests(endpoint, method)
        
        return response
    
    def cancel_refresh_in_group(self, groupId:str, datasetId:str, refreshId):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/cancel-refresh-in-group
        
        Cancels the specified refresh operation for the specified dataset from the specified workspace

        >>> Params:
            datasetId: The dataset ID
            groupId: The workspace ID
            refreshId: The refresh ID
            
        >>> Example:
            >>> datasets.cancel_refresh_in_group("fdb91b8f-0a9b-44c1-b6c0-0cb185c6ebfb", "f7fc6510-e151-42a3-850b-d0805a391db0", "87f31ef7-1e3a-4006-9b0b-191693e79e9e")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/refreshes/{refreshId}"

        method = 'delete'

        response = audit_requests(endpoint, method)
        
        return response
    
    def delete_dataset(self, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/delete-dataset
        
        Deletes the specified dataset from >>> My workspace.

        >>> Params:
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.delete_dataset('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"datasets/{datasetId}"

        method = 'delete'

        response = audit_requests(endpoint, method)
        
        return response
    
    def delete_dataset_in_group(self, groupId:str, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/delete-dataset-in-group 
        
        Deletes the specified dataset from the specified workspace.

        >>> Params:
            groupId: The group ID
            datasetId: The dataset ID
            
        
        >>> Example:
            >>> datasets.delete_dataset_in_group('f089354e-8366-4e18-aea3-4cb4a3a50b48','cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}"

        method = 'delete'

        response = audit_requests(endpoint, method)
        
        return response
    
    def discover_gateways(self, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/discover-gateways
        
        Returns a list of gateways that the specified dataset from My workspace can be bound to

        >>> Params:
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.discover_gateways("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"datasets/{datasetId}/Default.DiscoverGateways"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def discover_gateways_in_group(self, groupId:str, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/discover-gateways-in-group
        
        Returns a list of gateways that the specified dataset from the specified workspace can be bound to

        >>> Params:
            datasetId: The dataset ID
            groupId: The workspace ID
            
        >>> Example:
            >>> datasets.discover_gateways_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/Default.DiscoverGateways"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def execute_queries(self, datasetId:str, queries, impersonatedUserName:str=None, serializerSettings=None):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/execute-queries
        
        Executes Data Analysis Expressions (DAX) queries against the provided dataset. The dataset must reside in My workspace or another workspace

        >>> Params:
            datasetId: The dataset ID
            queires: The list of dataset queries to execute
            
        >>> Example:
            >>> datasets.execute_queries("cfafbeb1-8037-4d0c-896e-a46fb27ff229", queries)
        
        '''
        endpoint = f"datasets/{datasetId}/executeQueries"

        method = 'post'

        body = {
            "queries": queries,
            "impersonatedUserName": impersonatedUserName
        }

        if(serializerSettings):
            body = {
            "queries": queries,
            "impersonatedUserName": impersonatedUserName,
            "serializerSettings": serializerSettings
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def execute_queries_in_group(self, groupId:str, datasetId:str, queries, impersonatedUserName:str=None, serializerSettings=None):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/execute-queries-in-group
        
        Executes Data Analysis Expressions (DAX) queries against the provided dataset.

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            queires: The list of dataset queries to execute
            
        >>> Example:
            >>> datasets.execute_queries_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229", queries)
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/executeQueries"

        method = 'post'

        body = {
            "queries": queries,
            "impersonatedUserName": impersonatedUserName
        }

        if(serializerSettings):
            body = {
            "queries": queries,
            "impersonatedUserName": impersonatedUserName,
            "serializerSettings": serializerSettings
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def get_dataset(self, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-dataset

            Returns the specified dataset from >>> My workspace

        >>> Params:
            datasetId: The dataset ID
        
        >>> Example:
            >>> datasets.get_dataset('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"datasets/{datasetId}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dataset_in_group(self, groupId:str, datasetId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-dataset-in-group
        
        Returns the specified dataset from >>> specified workspace

        >>> Params:
            groupId: The group ID
            datasetId: The dataset ID
        
        >>> Example:
            >>> datasets.get_dataset_in_group('f089354e-8366-4e18-aea3-4cb4a3a50b48', 'cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dataset_to_dataflows_links_in_group(self, groupId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-dataset-to-dataflows-links-in-group
        
        Returns a list of upstream dataflows for datasets from the specified workspace

        >>> Params:
            groupId: The workspace ID
            
        >>> Example:
            >>> datasets.get_dataset_to_dataflows_links_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b4")
        
        '''
        endpoint = f"groups/{groupId}/datasets/upstreamDataflows"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dataset_users(self, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-dataset-users
        
        Returns a list of principals that have access to the specified dataset

        >>> Params:
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.get_dataset_users("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"datasets/{datasetId}/users"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dataset_users_in_group(self, groupId:str, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-dataset-users-in-group
        
        Returns a list of principals that have access to the specified dataset

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.get_dataset_users("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/users"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_datasets(self):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-datasets

            Returns a list of datasets from >>> My workspace
            
        >>> Example:
            >>> datasets.get_datasets()
        
        '''
        endpoint = f"datasets"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_datasets_in_group(self, group_id:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-datasets-in-group
        
        Returns a list of datasets from >>> the specified workspace

        >>> Params:
            group_id: The group ID
        
        >>> Example:
            >>> datasets.get_datasets_in_group('f089354e-8366-4e18-aea3-4cb4a3a50b48', 'cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{group_id}/datasets"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_datasources(self, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-datasources
        
        Returns a list of data sources for the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.get_datasources("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"datasets/{datasetId}/datasources"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_datasources_in_group(self, groupId:str, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-datasources-in-group
        
        Returns a list of data sources for the specified dataset from the specified workspace

        >>> Params:
            datasetId: The dataset ID
            groupId: The workspace ID
            
        >>> Example:
            >>> datasets.sample("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/datasources"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_direct_query_refresh_schedule(self, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-direct-query-refresh-schedule
        
        Returns the refresh schedule for a specified DirectQuery or LiveConnection dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.get_direct_query_refresh_schedule("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"datasets/{datasetId}/directQueryRefreshSchedule"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_direct_query_refresh_schedule_in_group(self, groupId:str, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-direct-query-refresh-schedule-in-group
        
        Returns the refresh schedule for a specified DirectQuery or LiveConnection dataset from the specified workspace

        >>> Params:
            datasetId: The dataset ID
            groupId: The workspace ID
            
        >>> Example:
            >>> datasets.get_direct_query_refresh_schedule_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/directQueryRefreshSchedule"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_gateway_datasources(self, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-gateway-datasources
        
        Returns a list of gateway data sources for the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.get_gateway_datasources("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"datasets/{datasetId}/Default.GetBoundGatewayDatasources"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_gateway_datasources_in_group(self, groupId:str, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-gateway-datasources-in-group
        
        Returns a list of gateway data sources for the specified dataset from the specified workspace

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.get_gateway_datasources_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/Default.GetBoundGatewayDatasources"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_parameters(self, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-parameters
        
        Returns a list of parameters for the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.get_parameters("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"datasets/{datasetId}/parameters"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_parameters_in_group(self, groupId:str, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-parameters-in-group
        
        Returns a list of parameters for the specified dataset from the specified workspace

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.get_parameters_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/parameters"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_refresh_execution_details(self, datasetId:str, refreshId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-refresh-execution-details
        
        Returns execution details of an enhanced refresh operation for the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            refreshId: The refresh ID
            
        >>> Example:
            >>> datasets.get_refresh_execution_details("f7fc6510-e151-42a3-850b-d0805a391db0", "87f31ef7-1e3a-4006-9b0b-191693e79e9e")
        
        '''
        endpoint = f"datasets/{datasetId}/refreshes/{refreshId}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_refresh_execution_details_in_group(self, groupId, datasetId:str, refreshId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-refresh-execution-details-in-group
        
        Returns execution details of an enhanced refresh operation for the specified dataset from the specified workspace

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            refreshId: The refresh ID
            
        >>> Example:
            >>> datasets.get_refresh_execution_details_in_group("fdb91b8f-0a9b-44c1-b6c0-0cb185c6ebfb", "f7fc6510-e151-42a3-850b-d0805a391db0", "87f31ef7-1e3a-4006-9b0b-191693e79e9e")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/refreshes/{refreshId}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_refresh_history(self, datasetId:str, top:int=500):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-refresh-history
        
        Returns the refresh history for the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            top: The requested number of entries in the refresh history. If not provided, the default is the last available 500 entries
            
        >>> Example:
            >>> datasets.get_refresh_history("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"datasets/{datasetId}/refreshes?$top={top}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_refresh_history_in_group(self, groupId:str, datasetId:str, top:int=500):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-refresh-history-in-group
        
        Returns the refresh history for the specified dataset from the specified workspace

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            top: The requested number of entries in the refresh history. If not provided, the default is the last available 500 entries
            
        >>> Example:
            >>> datasets.get_refresh_history_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/refreshes?$top={top}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_refresh_schedule(self, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-refresh-schedule
        
        Returns the refresh schedule for the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.get_refresh_schedule("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"datasets/{datasetId}/refreshSchedule"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_refresh_schedule_in_group(self, groupId:str, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-refresh-schedule-in-group
        
        Returns the refresh schedule for the specified dataset from the specified workspace

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.get_refresh_schedule_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/refreshSchedule"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def post_dataset_user(self, datasetId:str, identifier:str, principalType, datasetUserAccessRight):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/post-dataset-user
        
        Grants the specified user's permissions to the specified dataset

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            identifier: For principal type User, provide the UPN. Otherwise provide the object ID of the principal
            principalType: The principal type
            datasetUserAccessRight: Required. The access right to grant to the user for the dataset
            
        >>> Example:
            >>> datasets.post_dataset_user("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"datasets/{datasetId}/users"

        method = 'post'

        body = {
            "identifier": identifier,
            "principalType": principalType,
            "datasetUserAccessRight": datasetUserAccessRight
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def post_dataset_user_in_group(self, groupId:str, datasetId:str, identifier:str, principalType, datasetUserAccessRight):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/post-dataset-user-in-group
        
        Grants the specified user's permissions to the specified dataset

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            identifier: For principal type User, provide the UPN. Otherwise provide the object ID of the principal
            principalType: The principal type
            datasetUserAccessRight: Required. The access right to grant to the user for the dataset
            
        >>> Example:
            >>> datasets.post_dataset_user("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/users"

        method = 'post'

        body = {
            "identifier": identifier,
            "principalType": principalType,
            "datasetUserAccessRight": datasetUserAccessRight
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def put_dataset_user(self, datasetId:str, identifier:str, principalType, datasetUserAccessRight):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/put-dataset-user
        
        Updates the existing dataset permissions of the specified user to the specified permissions

        >>> Params:
            datasetId: The dataset ID
            identifier: For principal type User, provide the UPN. Otherwise provide the object ID of the principal
            principalType: The principal type
            datasetUserAccessRight: Required. The access right to grant to the user for the dataset
            
        >>> Example:
            >>> datasets.put_dataset_user("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"datasets/{datasetId}/users"

        method = 'put'

        body = {
            "identifier": identifier,
            "principalType": principalType,
            "datasetUserAccessRight": datasetUserAccessRight
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def put_dataset_user_in_group(self, groupId:str, datasetId:str, identifier:str, principalType, datasetUserAccessRight):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/put-dataset-user-in-group
        
        Updates the existing dataset permissions of the specified user to the specified permissions

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            identifier: For principal type User, provide the UPN. Otherwise provide the object ID of the principal
            principalType: The principal type
            datasetUserAccessRight: Required. The access right to grant to the user for the dataset
            
        >>> Example:
            >>> datasets.post_dataset_user("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/users"

        method = 'put'

        body = {
            "identifier": identifier,
            "principalType": principalType,
            "datasetUserAccessRight": datasetUserAccessRight
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def refresh_dataset(self, dataset_id:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/refresh-dataset
        
            Triggers a refresh for the specified dataset from >>> My workspace
            #Enhanced refresh is still work in progress

        >>> Params:
            dataset_id: The dataset ID
            
        >>> Example:
            >>> datasets.refresh_dataset('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"datasets/{dataset_id}/refreshes"
        
        method = 'post'

        response = audit_requests(endpoint, method)
        
        return response

    def refresh_dataset_in_group(self, group_id:str, dataset_id:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/refresh-dataset-in-group
        
            Triggers a refresh for the specified dataset from the specified workspace
            #Enhanced refresh is still work in progress

        >>> Params:
            group_id: The group ID
            dataset_id: The dataset ID
            
        >>> Example:
            >>> datasets.refresh_dataset_in_group('f089354e-8366-4e18-aea3-4cb4a3a50b48','cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{group_id}/datasets/{dataset_id}/refreshes"

        method = 'post'

        response = audit_requests(endpoint, method)
        
        return response
    
    def set_all_dataset_connections(self, datasetId:str, connectionString:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/set-all-dataset-connections
        
        Updates all connections for the specified dataset from My workspace. This API call only supports SQL DirectQuery datasets

        >>> Params:
            datasetId: The dataset ID
            connectionString: A dataset connection string
            
        >>> Example:
            >>> datasets.set_all_dataset_connections("cfafbeb1-8037-4d0c-896e-a46fb27ff229", connectionString)
        
        '''
        endpoint = f"datasets/{datasetId}/Default.SetAllConnections"

        method = 'post'

        body = {
            "connectionString": connectionString
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def set_all_dataset_connections_in_group(self, groupId:str, datasetId:str, connectionString:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/set-all-dataset-connections-in-group

        Updates all connections for the specified dataset from the specified workspace. This API call only supports SQL DirectQuery datasets

        >>> Params:
            datasetId: The dataset ID
            connectionString: A dataset connection string
            
        >>> Example:
            >>> datasets.set_all_dataset_connections_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229", connectionString)
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/Default.SetAllConnections"

        method = 'post'

        body = {
            "connectionString": connectionString
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def take_over_in_group(self, groupId:str, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/take-over-in-group
        
        Transfers ownership over the specified dataset to the current authorized user

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            
        >>> Example:
            >>> datasets.take_over_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/Default.TakeOver"

        method = 'post'

        response = audit_requests(endpoint, method)
        
        return response
    
    def update_dataset(self, datasetId:str, targetStorageMode:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/update-dataset
        
        Updates the properties for the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            targetStorageMode: The dataset storage mode
            
        >>> Example:
            >>> datasets.update_dataset("cfafbeb1-8037-4d0c-896e-a46fb27ff229", targetStorageMode)
        
        '''
        endpoint = f"datasets/{datasetId}"

        method = 'patch'

        body = {
            "targetStorageMode": targetStorageMode
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def update_dataset_in_group(self, groupId:str, datasetId:str, targetStorageMode:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/update-dataset-in-group
        
        Updates the properties for the specified dataset from My workspace

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            targetStorageMode: The dataset storage mode
            
        >>> Example:
            >>> datasets.update_dataset_in_group("cfafbeb1-8037-4d0c-896e-a46fb27ff229", targetStorageMode)
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}"

        method = 'patch'

        body = {
            "targetStorageMode": targetStorageMode
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def update_datasources(self, datasetId:str, updateDetails):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/update-datasources
        
        Updates the data sources of the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            updateDetails: An array of data source connection update requests
            
        >>> Example:
            >>> datasets.update_datasources("cfafbeb1-8037-4d0c-896e-a46fb27ff229", updateDetails)
        
        '''
        endpoint = f"datasets/{datasetId}/Default.UpdateDatasources"

        method = 'post'

        body = {
            "updateDetails": updateDetails
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def update_datasources_in_group(self, groupId:str, datasetId:str, updateDetails):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/update-datasources-in-group
        
        Updates the data sources of the specified dataset from the specified workspace

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            updateDetails: An array of data source connection update requests
            
        >>> Example:
            >>> datasets.update_datasources_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229", updateDetails)
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/Default.UpdateDatasources"

        method = 'post'

        body = {
            "updateDetails": updateDetails
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def update_direct_query_refresh_schedule(self, datasetId:str, value):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/update-direct-query-refresh-schedule
        
        Updates the refresh schedule for a specified DirectQuery or LiveConnection dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            value: An object containing the refresh schedule details for DirectQuery or LiveConnection
            
        >>> Example:
            >>> datasets.update_direct_query_refresh_schedule("cfafbeb1-8037-4d0c-896e-a46fb27ff229", value)
        
        '''
        endpoint = f"datasets/{datasetId}/directQueryRefreshSchedule"

        method = 'patch'

        body = {
            "value": value
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def update_direct_query_refresh_schedule_in_group(self, groupId:str, datasetId:str, value):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/update-direct-query-refresh-schedule-in-group
        
        Updates the refresh schedule for a specified DirectQuery or LiveConnection dataset from the specified workspace

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            value: An object containing the refresh schedule details for DirectQuery or LiveConnection
            
        >>> Example:
            >>> datasets.update_direct_query_refresh_schedule("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229", value)
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/directQueryRefreshSchedule"

        method = 'patch'

        body = {
            "value": value
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def update_parameters(self, datasetId:str, updateDetails):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/update-parameters
        
        Updates the parameters values for the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            updateDetails: A list of dataset parameters to update
            
        >>> Example:
            >>> datasets.update_parameters("cfafbeb1-8037-4d0c-896e-a46fb27ff229", updateDetails)
        
        '''
        endpoint = f"datasets/{datasetId}/Default.UpdateParameters"

        method = 'post'

        body = {
            "updateDetails": updateDetails
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def update_parameters_in_group(self, groupId:str, datasetId:str, updateDetails):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/update-parameters-in-group
        
        Updates the parameters values for the specified dataset from the specified workspace

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            updateDetails: A list of dataset parameters to update
            
        >>> Example:
            >>> datasets.update_parameters_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229", updateDetails)
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/Default.UpdateParameters"

        method = 'post'

        body = {
            "updateDetails": updateDetails
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def update_refresh_schedule(self, datasetId:str, value):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/update-refresh-schedule
        
        Updates the refresh schedule for the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            value: An object that contains the details of a refresh schedule
            
        >>> Example:
            >>> datasets.update_refresh_schedule("cfafbeb1-8037-4d0c-896e-a46fb27ff229", value)
        
        '''
        endpoint = f"datasets/{datasetId}/refreshSchedule"

        method = 'patch'

        body = {
            "value": value
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def update_refresh_schedule_in_group(self, groupId:str, datasetId:str, value):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/update-refresh-schedule-in-group
        
        Updates the refresh schedule for the specified dataset from the specified workspace

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
            value: An object that contains the details of a refresh schedule
            
        >>> Example:
            >>> datasets.update_refresh_schedule_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229", value)
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/refreshSchedule"

        method = 'patch'

        body = {
            "value": value
        }

        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def error_filter_refresh_history(self, group_id, dataset_id):
        ''' Returns refresh history of a dataset in a workspace with errors filtered

        >>> Params:
            group_id: workspace ID
            dataset_id: The dataset ID
        
        >>> Example:
            >>> datasets.error_filter_refresh_history('f089354e-8366-4e18-aea3-4cb4a3a50b48', 'cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        invalid_dataset_recent = datetime.today() - timedelta(days=29) #datasets with invalid dataset
        invalid_dataset_old = datetime.today() - timedelta(days=333) #datasets with no metadata or refresh history
        
        invalid_dataset = {
            'value': [{'startTime': f'{invalid_dataset_recent}'}]
        }

        no_history_dataset = {
            'value': [{'startTime': f'{invalid_dataset_old}'}]
        }
        endpoint = f"groups/{group_id}/datasets/{dataset_id}/refreshes?$top=1"

        method = 'get'

        response = audit_requests(endpoint, method)
        #if 'error' in response:
            #return [response['error']['message']]
        
        try:
            if 'error' in response:
                if ('Invalid dataset' in response['error']['message'] ):
                    return invalid_dataset['value']

            if(response['value'] == []):
                return no_history_dataset['value']

            refresh_history = response['value']
            return refresh_history
        except:
            return []
           

    def get_recent_dataset(self, group_id): 
        ''' Returns the most recently refreshed dataset from the specified workspace

        >>> Params:
            group_id: workspace ID
        
        >>> Example:
            >>> datasets.error_filter_recent_dataset('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        determine_difference_by = FormateDate()

        refresh_history = [] 

        endpoint = f"groups/{group_id}/datasets"

        method = 'get'

        response = audit_requests(endpoint, method)
        datasets = response['value']
        for dataset in datasets:
            if(dataset['name'] != 'Report Usage Metrics Model'):
                for history in self.error_filter_refresh_history(group_id, dataset['id']): #get the refresh time of each dataset to determine the most recent refreshed dataset
                    #refresh_history.append([determine_difference_by.formateDate(history['startTime']), [dataset]])
                    refresh_history.append([determine_difference_by.formateDate(history['startTime']), [dataset]])
        
        try:
            return sorted(refresh_history, key=lambda item:item[0], reverse=True)[0][1]
        except:
            return []

    def error_filter_recent_dataset(self, group_id):
        ''' Returns the most recently refreshed dataset from the specified workspace with errors filtered

        >>> Params:
            group_id: workspace ID
        
        >>> Example:
            >>> datasets.error_filter_recent_dataset('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        determine_difference_by = FormateDate()

        refresh_history = []

        endpoint = f"groups/{group_id}/datasets"

        method = 'get'

        response = audit_requests(endpoint, method)
        if(response['value'] == []):
            return ['No Dataset']
        
        datasets = response['value']
        for dataset in datasets:
            if(dataset['name'] != 'Report Usage Metrics Model'):
                for history in self.error_filter_refresh_history(group_id, dataset['id']): #get the refresh time of each dataset to determine the most recent refreshed dataset
                    #refresh_history.append([determine_difference_by.formateDate(history['startTime']), [dataset]])
                    refresh_history.append([determine_difference_by.formateDate(history['startTime']), [dataset]])

        try:
            return sorted(refresh_history, key=lambda item:item[0], reverse=True)[0][1]
        except:
            return []

    
    
        




