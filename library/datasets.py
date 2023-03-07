import requests
from datetime import datetime, timedelta
from library.date_conversion import FormateDate
from library.login import headers
from library.requests import audit_requests

class Datasets():
    def __init__(self):
        self.headers = headers
    
    #GET REQUESTS
    def get_datasets(self, group_id): 
        ''' Returns the specified dataset from >>> specified workspace

        >>> Params:
            dataset_id: The dataset ID
        
        >>> Example:
            >>> datasets.get_datasets_group('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{group_id}/datasets"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dataset(self, group_id, dataset_id): 
        ''' Returns the specified dataset from >>> the specified workspace

        >>> Params:
            group_id: The group ID
            dataset_id: The dataset ID
        
        >>> Example:
            >>> datasets.get_dataset('f089354e-8366-4e18-aea3-4cb4a3a50b48', 'cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{group_id}/datasets/{dataset_id}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response

    def get_my_workspace_datasets(self, dataset_id):
        ''' Only for if you are targetting My Workspace
            Returns the specified dataset from >>> My workspace

        >>> Params:
            dataset_id: The dataset ID
        
        >>> Example:
            >>> datasets.get_dataset('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"datasets/{dataset_id}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
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

    def get_refresh_history(self, group_id, dataset_id, top):
        ''' Returns the refresh history for the specified dataset from >>> specified workspace

        >>> Params:
            dataset_id: The dataset ID
            top: The requested number of entries in the refresh history. 
                    If not provided, the default is the last available 500 entries
        
        >>> Example:
            >>> datasets.get_refresh_history('f089354e-8366-4e18-aea3-4cb4a3a50b48', 'cfafbeb1-8037-4d0c-896e-a46fb27ff229', top=10)
        
        '''
        endpoint = f"groups/{group_id}/datasets/{dataset_id}/refreshes?$top={top}"

        method = 'get'

        response = audit_requests(endpoint, method)
        #if 'error' in response:
            #return [response['error']['message']]
        
        try:
            refresh_history = response
            return refresh_history
        except:
            return []
    
    def get_my_workspace_refresh_history(self, dataset_id, top):
        ''' Returns refresh history for the specified dataset from >>> My workspace

        >>> Params:
            dataset_id: The dataset ID
            top: The requested number of entries in the refresh history. 
                    If not provided, the default is the last available 500 entries
        
        >>> Example:
            >>> datasets.get_datasets_in_group('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"datasets/{dataset_id}/refreshes?$top={top}"

        method = 'get'

        response = audit_requests(endpoint, method)
        
        return response
           

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

    #POST REQUESTS
    def refresh_my_workspace_dataset(self, dataset_id):
        ''' Triggers a refresh for the specified dataset from >>> My workspace
            #Enhanced refresh is still work in progress

        >>> Params:
            dataset_id: The dataset ID
            
        
        >>> Example:
            >>> datasets.refresh_my_workspace_dataset('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"datasets/{dataset_id}/refreshes"
        
        method = 'post'

        response = audit_requests(endpoint, method)
        
        return response

    def refresh_dataset(self, group_id, dataset_id):
        ''' Triggers a refresh for the specified dataset from the specified workspace
            #Enhanced refresh is still work in progress

        >>> Params:
            group_id: The group ID
            dataset_id: The dataset ID
            
        
        >>> Example:
            >>> datasets.refresh_my_workspace_dataset('f089354e-8366-4e18-aea3-4cb4a3a50b48','cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{group_id}/datasets/{dataset_id}/refreshes"

        method = 'post'

        response = audit_requests(endpoint, method)
        
        return response
    
    #DELETE REQUESTS
    def delete_my_workspace_dataset(self, dataset_id):
        ''' Deletes the specified dataset from >>> My workspace.

        >>> Params:
            dataset_id: The dataset ID
            
        >>> Example:
            >>> datasets.delete_my_workspace_dataset('cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"datasets/{dataset_id}"

        method = 'delete'

        response = audit_requests(endpoint, method)
        
        return response
    
    def delete_dataset(self, group_id, dataset_id):
        ''' Deletes the specified dataset from the specified workspace.

        >>> Params:
            group_id: The group ID
            dataset_id: The dataset ID
            
        
        >>> Example:
            >>> datasets.delete_dataset('f089354e-8366-4e18-aea3-4cb4a3a50b48','cfafbeb1-8037-4d0c-896e-a46fb27ff229')
        
        '''
        endpoint = f"groups/{group_id}/datasets/{dataset_id}/refreshes"

        method = 'delete'

        response = audit_requests(endpoint, method)
        
        return response
        




