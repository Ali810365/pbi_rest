from library.requests import audit_requests

class PushDatasets():
    def __init__(self):
        pass

    def delete_rows(self, datasetId:str, tableName:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-delete-rows

        Deletes all rows from the specified table within the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            tableName: The table name
        
        >>> Example:
            PushDatasets.delete_rows("cfafbeb1-8037-4d0c-896e-a46fb27ff229", "Product")
        
        '''
        endpoint = f"datasets/{datasetId}/tables/{tableName}/rows"

        method = 'delete'
        
        response = audit_requests(endpoint, method)

        return response
    
    def delete_rows_in_group(self, datasetId:str, groupId:str, tableName:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-delete-rows-in-group

        Deletes all rows from the specified table within the specified dataset from the specified workspace

        >>> Params:
            datasetId: The dataset ID
            groupId: The workspace ID
            tableName: The table name
        
        >>> Example:
            PushDatasets.delete_rows_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229", "Product")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/tables/{tableName}/rows"

        method = 'delete'
        
        response = audit_requests(endpoint, method)

        return response
    
    def get_tables(self, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-get-tables

        Returns a list of tables within the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
        
        >>> Example:
            PushDatasets.get_tables("f089354e-8366-4e18-aea3-4cb4a3a50b48")
        
        '''
        endpoint = f"datasets/{datasetId}/tables"

        method = 'get'
        
        response = audit_requests(endpoint, method)

        return response
    
    def get_tables_in_group(self, groupId:str, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-get-tables-in-group

        Returns a list of tables within the specified dataset from the specified workspace

        >>> Params:
            groupId: The workspace ID
            datasetId: The dataset ID
        
        >>> Example:
            PushDatasets.get_tables_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/tables"

        method = 'get'
        
        response = audit_requests(endpoint, method)

        return response

    def post_dataset(self, name:str, tables):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-post-dataset

        Creates a new dataset on My workspace

        >>> Params:
            name: The dataset name
            tables: The dataset tables
        
        >>> Example:
            PushDatasets.post_dataset("SalesMarketing", tables)
        
        '''
        endpoint = f"datasets"

        method = 'post'

        body = {
            "name": name,
            "tables": tables
        }
        
        response = audit_requests(endpoint, method, json=body)

        return response
    
    def post_dataset_in_group(self, groupId:str, name:str, tables):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-post-dataset-in-group

        Creates a new dataset on My workspace

        >>> Params:
            name: The dataset name
            tables: The dataset tables
        
        >>> Example:
            PushDatasets.post_dataset_in_group("SalesMarketing", tables)
        
        '''
        endpoint = f"groups/{groupId}/datasets"

        method = 'post'

        body = {
            "name": name,
            "tables": tables
        }
        
        response = audit_requests(endpoint, method, json=body)

        return response
    
    def post_rows(self, datasetId:str, tableName:str, rows):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-post-rows

        Adds new data rows to the specified table within the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            tableName: The table name
        
        >>> Example:
            PushDatasets.post_rows("cfafbeb1-8037-4d0c-896e-a46fb27ff229", "Product", rows:list)
        
        '''
        endpoint = f"datasets/{datasetId}/tables/{tableName}/rows"

        method = 'post'

        body = {
            "row": rows
        }
        
        response = audit_requests(endpoint, method, json=body)

        return response
    
    def post_rows_in_group(self, groupId:str, datasetId:str, tableName:str, rows):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-post-rows-in-group

        Adds new data rows to the specified table within the specified dataset from the specified workspace

        >>> Params:
            datasetId: The dataset ID
            tableName: The table name
        
        >>> Example:
            PushDatasets.post_rows("cfafbeb1-8037-4d0c-896e-a46fb27ff229", "Product", rows:list)
        
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/tables/{tableName}/rows"

        method = 'post'

        body = {
            "row": rows
        }
        
        response = audit_requests(endpoint, method, json=body)

        return response
    
    def put_table(self, datasetId:str, tableName:str, columns):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-put-table

        Updates the metadata and schema for the specified table within the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            tableName: The table name
            columns: The column schema for this table
        
        >>> Example:
            PushDatasets.put_table("cfafbeb1-8037-4d0c-896e-a46fb27ff229", "Product", columns)
        
        '''
        endpoint = f"datasets/{datasetId}/tables/{tableName}"

        method = 'put'

        body = {
            "columns": columns,
            "tableName": tableName
        }
        
        response = audit_requests(endpoint, method, json=body)

        return response
    

    def put_table_in_group(self, groupId:str, datasetId:str, tableName:str, columns):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-put-table-in-group

        Updates the metadata and schema for the specified table within the specified dataset from My workspace

        >>> Params:
            datasetId: The dataset ID
            tableName: The table name
            columns: The column schema for this table
        
        >>> Example:
            PushDatasets.put_table_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229", "Product", columns)
        '''
        endpoint = f"groups/{groupId}/datasets/{datasetId}/tables/{tableName}"

        method = 'put'

        body = {
            "columns": columns,
            "tableName": tableName
        }
        
        response = audit_requests(endpoint, method, json=body)

        return response
    