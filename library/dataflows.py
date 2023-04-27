from library.requests import audit_requests

class Dataflows():
    def __init__(self):
        pass
    
    def cancel_dataflow_transaction(self, groupId:str, transactionId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/cancel-dataflow-transaction
        ''' Attempts to cancel the specified transactions

        >>> Params:
            groupId: The workspace ID
            transactionId: The transaction ID
            
        >>> Example:
           dataflows.get_dataflow("51e47fc5-48fd-4826-89f0-021111110abd", "2020-09-11T19:21:52.8778432Z@9cc7a369-6112-4dba-97b6-b07ff5699568$1374282")
        
        '''
        endpoint = f"groups/{groupId}/dataflows/transactions/{transactionId}/cancel"

        method = 'post'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def delete_dataflow(self, groupId:str, dataflowId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/delete-dataflow
        ''' Deletes a dataflow from Power BI data prep storage, including its definition file and model

        >>> Params:
            groupId: The workspace ID
            dataflowId: The dataflow ID
        
        >>> Example:
           dataflows.delete_dataflow("51e47fc5-48fd-4826-89f0-021bd3a80abd", "928228ba-008d-4fd9-864a-92d2752ee5ce")
        
        '''
        endpoint = f"groups/{groupId}/dataflows/{dataflowId}"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_dataflow(self, groupId:str, dataflowId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/get-dataflow 
        ''' Exports the specified dataflow definition to a JSON file

        >>> Params:
            groupId: The workspace ID
            dataflowId: The dataflow ID
        
        >>> Example:
           dataflows.get_dataflow("51e47fc5-48fd-4826-89f0-021111110abd", "928228ba-008d-4fd9-864a-92d2752ee5ce")
        
        '''
        endpoint = f"groups/{groupId}/dataflows/{dataflowId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dataflow_data_sources(self, groupId:str, dataflowId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/get-dataflow-data-sources
        ''' Returns a list of data sources for the specified dataflow

        >>> Params:
            groupId: The workspace ID
            dataflowId: The dataflow ID
        
        >>> Example:
           dataflows.get_dataflow_data_sources("51e47fc5-48fd-4826-89f0-021111110abd", "928228ba-008d-4fd9-864a-92d2752ee5ce")
        
        '''
        endpoint = f"groups/{groupId}/dataflows/{dataflowId}/datasources"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dataflow_transactions(self, groupId:str, dataflowId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/get-dataflow-transactions
        ''' Returns a list of transactions for the specified dataflow

        >>> Params:
            groupId: The workspace ID
            dataflowId: The dataflow ID
        
        >>> Example:
           dataflows.get_dataflow_transactions("51e47fc5-48fd-4826-89f0-021111110abd", "928228ba-008d-4fd9-864a-92d2752ee5ce")

        '''
        endpoint = f"groups/{groupId}/dataflows/{dataflowId}/transactions"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dataflows(self, groupId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/get-dataflows
        ''' Returns a list of all dataflows from the specified workspace

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
           dataflows.get_dataflows("a2f89923-421a-464e-bf4c-25eab39bb09f")

        '''
        endpoint = f"groups/{groupId}/dataflows"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
        
    def get_upstream_dataflows_in_group(self, groupId:str, dataflowId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/get-upstream-dataflows-in-group
        ''' Returns a list of upstream dataflows for the specified dataflow

        >>> Params:
            groupId: The workspace ID
            dataflowId: The dataflow ID
        
        >>> Example:
           dataflows.get_upstream_dataflows_in_group("51e47fc5-48fd-4826-89f0-021111110abd", "928228ba-008d-4fd9-864a-92d2752ee5ce")

        '''
        endpoint = f"groups/{groupId}/dataflows/{dataflowId}/upstreamDataflows"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def refresh_dataflow(self, groupId:str, dataflowId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/refresh-dataflow
        ''' Triggers a refresh for the specified dataflow

        >>> Params:
            groupId: The workspace ID
            dataflowId: The dataflow ID
        
        >>> Example:
           dataflows.refresh_dataflow("51e47fc5-48fd-4826-89f0-021111110abd", "928228ba-008d-4fd9-864a-92d2752ee5ce")

        '''
        endpoint = f"groups/{groupId}/dataflows/{dataflowId}/refreshes"

        method = 'post'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def update_dataflow(self, groupId:str, dataflowId:str, json:object):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/update-dataflow
        ''' Updates dataflow properties, capabilities and settings

        >>> Params:
            groupId: The workspace ID
            dataflowId: The dataflow ID
        
        >>> Example:
           dataflows.update_dataflow("51e47fc5-48fd-4826-89f0-021111110abd", "928228ba-008d-4fd9-864a-92d2752ee5ce")

        '''
        endpoint = f"groups/{groupId}/dataflows/{dataflowId}"

        method = 'patch'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def update_refresh_schedule(self, groupId:str, dataflowId:str, RefreshSchedule:object):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/update-refresh-schedule
        ''' Creates or updates the refresh schedule for a specified dataflow

        >>> Params:
            groupId: The workspace ID
            dataflowId: The dataflow ID
            RefreshSchedule: An object that contains the details of a refresh schedule
        
        >>> Example:
           dataflows.

        '''
        endpoint = f"groups/{groupId}/dataflows/{dataflowId}/refreshSchedule"

        method = 'patch'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def sample(self, groupId:str, dataflowId:str):
        #
        ''' Sample

        >>> Params:
            groupId: The workspace ID
            dataflowId: The dataflow ID
            
        
        >>> Example:
           dataflows.

        '''
        endpoint = f"groups/"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response