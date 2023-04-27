from library.requests import audit_requests

class Gateways():
    def __init__(self):
        pass


    def add_datasource_user(self, gatewayId:str, datasourceId:str, datasourceAccessRight:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/gateways/add-datasource-user
        
        Grants or updates the permissions required to use the specified data source for the specified user

        >>> Params:
            gatewayId: The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster. In such cases, gateway ID is similar to gateway cluster ID
            datasourceId: The data source ID
            datasourceAccessRight: The access right (permission level) that a user has on the data source

        >>> Example:
            gateways.add_datasource_user("1f69e798-5852-4fdd-ab01-33bb14b6e934", "datasources/252b9de8-d915-4788-aaeb-ec8c2395f970", "Read")
        
        '''
        endpoint = f"gateways/{gatewayId}/datasources/{datasourceId}/users"

        method = 'post'

        body = {
            "datasourceAccessRight": datasourceAccessRight
        }
        
        response = audit_requests(endpoint, method, json=body)

        return response
    

    def create_datasource(self, gatewayId:str, connectionDetails, credentialDetails:str, dataSourceName:str, dataSourceType:str,):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/gateways/create-datasource
        
        Creates a new data source on the specified on-premises gateway

        >>> Params:
            gatewayId: The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster. In such cases, gateway ID is similar to gateway cluster ID
            connectionDetails: The connection details
            credentialDetails: The credential details
            dataSourceName: The data source name
            dataSourceType: The data source type
        
        >>> Example:
            gateways.create_datasource()
        
        '''
        endpoint = f"gateways/{gatewayId}/datasources"

        method = 'post'

        body = {
            "connectionDetails": connectionDetails,
            "credentialDetails": credentialDetails,
            "dataSourceName": dataSourceName,
            "dataSourceType": dataSourceType
        }
        
        response = audit_requests(endpoint, method, json=body)

        return response
    
    def delete_datasource(self, gatewayId:str, datasourceId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/gateways/delete-datasource
        
        Deletes the specified data source from the specified gateway

        >>> Params:
            gatewayId: The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster. In such cases, gateway ID is similar to gateway cluster ID
            datasourceId: The data source ID

        >>> Example:
            gateways.delete_datasource("1f69e798-5852-4fdd-ab01-33bb14b6e934", "252b9de8-d915-4788-aaeb-ec8c2395f970")
        
        '''
        endpoint = f"gateways/{gatewayId}/datasources/{datasourceId}"

        method = 'delete'
        
        response = audit_requests(endpoint, method)

        return response
    
    def delete_datasource_user(self, gatewayId:str, datasourceId:str, emailAdress:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/gateways/delete-datasource-user
        
        Removes the specified user from the specified data source

        >>> Params:
            gatewayId: The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster. In such cases, gateway ID is similar to gateway cluster ID
            datasourceId: The data source ID
            emailAdress: The user's email address or the object ID of the service principal

        >>> Example:
            gateways.delete_datasource_user("gateways/1f69e798-5852-4fdd-ab01-33bb14b6e934", "252b9de8-d915-4788-aaeb-ec8c2395f970", "john@contoso.com")
        
        '''
        endpoint = f"gateways/{gatewayId}/datasources/{datasourceId}/users/{emailAdress}"

        method = 'delete'
        
        response = audit_requests(endpoint, method)

        return response
    
    def get_datasource(self, gatewayId:str, datasourceId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/gateways/get-datasource
        
        Returns the specified data source from the specified gateway

        >>> Params:
            gatewayId: The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster. In such cases, gateway ID is similar to gateway cluster ID
            datasourceId: The data source ID

        >>> Example:
            gateways.get_datasource("1f69e798-5852-4fdd-ab01-33bb14b6e934", "252b9de8-d915-4788-aaeb-ec8c2395f970")
        
        '''
        endpoint = f"gateways/{gatewayId}/datasources/{datasourceId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)

        return response
    
    def get_datasource_status(self, gatewayId:str, datasourceId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/gateways/get-datasource-status
        
        Checks the connectivity status of the specified data source from the specified gateway

        >>> Params:
            gatewayId: The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster. In such cases, gateway ID is similar to gateway cluster ID
            datasourceId: The data source ID

        >>> Example:
            gateways.get_datasource_status("1f69e798-5852-4fdd-ab01-33bb14b6e934", "252b9de8-d915-4788-aaeb-ec8c2395f970")
        
        '''
        endpoint = f"gateways/{gatewayId}/datasources/{datasourceId}/status"

        method = 'get'
        
        response = audit_requests(endpoint, method)

        return response
    
    def get_datasource_users(self, gatewayId:str, datasourceId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/gateways/get-datasource-users
        
        Returns a list of users who have access to the specified data source

        >>> Params:
            gatewayId: The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster. In such cases, gateway ID is similar to gateway cluster ID
            datasourceId: The data source ID

        >>> Example:
            gateways.get_datasource_users("1f69e798-5852-4fdd-ab01-33bb14b6e934", "252b9de8-d915-4788-aaeb-ec8c2395f970")
        
        '''
        endpoint = f"gateways/{gatewayId}/datasources/{datasourceId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)

        return response
    
    def get_datasources(self, gatewayId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/gateways/get-datasources
        
        Returns a list of data sources from the specified gateway

        >>> Params:
            gatewayId: The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster. In such cases, gateway ID is similar to gateway cluster ID
        
        >>> Example:
            gateways.get_datasources("1f69e798-5852-4fdd-ab01-33bb14b6e934")
        
        '''
        endpoint = f"gateways/{gatewayId}/datasources"

        method = 'get'
        
        response = audit_requests(endpoint, method)

        return response
    
    def get_gateway(self, gatewayId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/gateways/get-gateway
        
        Returns the specified gateway

        >>> Params:
            gatewayId: The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster. In such cases, gateway ID is similar to gateway cluster ID
        
        >>> Example:
            gateways.get_gateway("1f69e798-5852-4fdd-ab01-33bb14b6e934")
        
        '''
        endpoint = f"gateways/{gatewayId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)

        return response
    
    def get_gateways(self):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/gateways/get-gateways
        
        Returns a list of gateways for which the user is an admin
           
        >>> Example:
            gateways.get_gateways("")
        
        '''
        endpoint = f"gateways"

        method = 'get'
        
        response = audit_requests(endpoint, method)

        return response
    
    def update_datasource(self, gatewayId:str, datasourceId:str, credentialDetails):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/gateways/update-datasource
        
        Updates the credentials of the specified data source from the specified gateway

        >>> Params:
            gatewayId: The gateway ID. When using a gateway cluster, the gateway ID refers to the primary (first) gateway in the cluster. In such cases, gateway ID is similar to gateway cluster ID
            datasourceId: The data source ID

        >>> Example:
            gateways.update_datasource("")
        
        '''
        endpoint = f"gateways/{gatewayId}/datasources/{datasourceId}"

        method = 'patch'

        body = {
            "credentialDetails": credentialDetails
        }
        
        response = audit_requests(endpoint, method, json=body)

        return response

