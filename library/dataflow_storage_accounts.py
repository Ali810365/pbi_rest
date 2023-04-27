from library.requests import audit_requests

class DataflowStorage():
    def __init__(self):
        pass
    
    def get_dataflow_storage_accounts(self):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dataflow-storage-accounts/get-dataflow-storage-accounts
        ''' Returns a list of dataflow storage accounts that the user has access to.

        >>> Params:
            
        >>> Example:
           dataflowStorage.get_dataflow_storage_accounts()
        
        '''
        endpoint = f"dataflowStorageAccounts"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def groups_assign_to_dataflow_storage(self, groupId:str, dataflowStorageId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/dataflow-storage-accounts/groups-assign-to-dataflow-storage
        ''' Assigns the specified workspace to the specified dataflow storage account

        >>> Params:
            groupId: The workspace ID

        >>> Example:
           dataflowStorage.groups_assign_to_dataflow_storage("f089354e-8366-4e18-aea3-4cb4a3a50b48")
        
        '''
        endpoint = f"groups/{groupId}/AssignToDataflowStorage"

        body = {
            "dataflowStorageId": dataflowStorageId
        }

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response