from library.requests import audit_requests

class Groups():
    def __init__(self):
        #self.access_token = access_token
        #self.headers = headers
        pass
    
    def create_temporary_upload_location(self):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/imports/create-temporary-upload-location

        Creates a temporary blob storage upload location for importing large Power BI .pbix files that are between 1 GB and 10 GB in size

        >>> Params:
             
        
        >>> Example:
            imports.create_temporary_upload_location("")
        
        '''
        endpoint = f"imports/createTemporaryUploadLocation"

        method = 'post'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def create_temporary_upload_location_in_group(self, groupId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/imports/create-temporary-upload-location-in-group

        Creates a temporary blob storage upload location for importing large Power BI .pbix files that are between 1 GB and 10 GB in size

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            imports.create_temporary_upload_location_in_group("group id")
        
        '''
        endpoint = f"groups/{groupId}/imports/createTemporaryUploadLocation"

        method = 'post'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_import(self, importId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/imports/get-import

        Returns the specified import from My workspace

        >>> Params:
            importId: The import ID
        
        >>> Example:
            imports.get_import("82d9a37a-2b45-4221-b012-cb109b8e30c7")
        
        '''
        endpoint = f"imports/{importId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_import_in_group(self, importId:str, groupId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/imports/get-import-in-group

        Returns the specified import from the specified workspace

        >>> Params:
            importId: The import ID
            groupId: The workspace ID
        
        >>> Example:
            imports.get_import_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "82d9a37a-2b45-4221-b012-cb109b8e30c7")
        
        '''
        endpoint = f"groups/{groupId}/imports/{importId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_imports(self):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/imports/get-imports

        Returns a list of imports from My workspace

        >>> Params:
           
        
        >>> Example:
            imports.get_imports()
        
        '''
        endpoint = f"imports"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_imports_in_group(self, groupId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/imports/get-imports-in-group

        sample

        >>> Params:
            importId: The import ID
        
        >>> Example:
            imports.sample("")
        
        '''
        endpoint = f"groups/{groupId}/imports"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def post_import(self, datasetDisplayName:str, connectionType, filePath, fileUrl):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/imports/post-import

        Creates new content in My workspace

        >>> Params:
            datasetDisplayName: The display name of the dataset, should include file extension. Not supported when importing from OneDrive for Business
        
        >>> Example:
            imports.post_import(datasetDisplayName)
        
        '''
        endpoint = f"imports?datasetDisplayName={datasetDisplayName}"

        method = 'post'

        body = {
            "connectionType": connectionType,
            "filePath": filePath,
            "fileUrl": fileUrl,
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def post_import_in_group(self, datasetDisplayName:str, groupId:str, connectionType, filePath, fileUrl):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/imports/post-import

        Creates new content in My workspace

        >>> Params:
            datasetDisplayName: The display name of the dataset, should include file extension. Not supported when importing from OneDrive for Business
            groupId: The workspace ID
            connectionType: The import connection type for a OneDrive for Business file
            filePath: The path of the OneDrive for Business Excel (.xlsx) file to import, which can be absolute or relative. Power BI .pbix files aren't supported
            fileUrl: The shared access signature URL of the temporary blob storage used to import large Power BI .pbix files between 1 GB and 10 GB in size
        
        >>> Example:
            imports.post_import(datasetDisplayName)
        
        '''
        endpoint = f"groups/{groupId}/imports?datasetDisplayName={datasetDisplayName}"

        method = 'post'

        body = {
            "connectionType": connectionType,
            "filePath": filePath,
            "fileUrl": fileUrl,
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    