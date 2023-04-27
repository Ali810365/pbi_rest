from library.requests import audit_requests

class Capacities():
    def __init__(self):
        pass
    
    def get_app(self):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/capacities/get-capacities
        ''' Returns a list of capacities that the user has access to

        >>> Params:
            
        
        >>> Example:
            apps.get_app("3b5ca243-47d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"capacities"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_refreshable_for_capacity(self, capacityId:str, refreshableId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/capacities/get-capacities   ----!A
        ''' Returns the specified refreshable for the specified capacity that the user has access to

        >>> Params:
            capacityId: The capacity ID
            refreshableId: The refreshable ID
        >>> Example:
            capacities.get_refreshable_for_capacity("cfafbeb1-8037-4d0c-896e-a46fb27ff229", "9399bb89-25d1-44f8-8576-136d7e9014b1")
        
        '''
        endpoint = f"capacities/{capacityId}/refreshables/{refreshableId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_refreshables(self, capacityId:str, top:int):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/capacities/get-refreshables  !!!!!----!A
        ''' Returns a list of refreshables for all capacities that the user has access to

        >>> Params:
            top: Returns only the first n results
            
        >>> Example:
            capacities.get_refreshables(10)
        
        '''
        endpoint = f"capacities/refreshables?$top={top}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_refreshables_for_capacity(self, capacityId:str, top:int):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/capacities/get-refreshables-for-capacity
        ''' Returns a list of refreshables for the specified capacity that the user has access to

        >>> Params:
            capacityId: The capacity ID
            top: Returns only the first n results
            
        >>> Example:
            capacities.get_refreshables_for_capacity("cfafbeb1-8037-4d0c-896e-a46fb27ff229", 10)
        
        '''
        endpoint = f"capacities/{capacityId}/refreshables"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_workload(self, capacityId:str, workloadName:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/capacities/get-workload
        ''' Returns the current state of a workload. If the workload is enabled, the percentage of maximum memory that the workload can consume is also returned

        >>> Params:
            capacityId: The capacity ID
            workloadName: The name of the workload
            
        >>> Example:
            capacities.get_workload("0f084df7-c13d-451b-af5f-ed0c466403b2", "Dataflows")
        
        '''
        endpoint = f"capacities/{capacityId}/Workloads/{workloadName}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_workloads(self, capacityId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/capacities/get-workloads
        ''' Returns the current state of the specified capacity workloads. If a workload is enabled, the percentage of maximum memory that the workload can consume is also returned

        >>> Params:
            capacityId: The capacity ID
            
        >>> Example:
            capacities.get_workloads("0f084df7-c13d-451b-af5f-ed0c466403b2")
        
        '''
        endpoint = f"capacities/{capacityId}/Workloads"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def assign_my_workspace_to_capacity(self, capacityId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/capacities/groups-assign-my-workspace-to-capacity
        ''' Assigns My workspace to the specified capacity
            
        >>> Params:
            capacityId: The capacity ID. To unassign from a capacity, use an empty GUID (00000000-0000-0000-0000-000000000000).
            
        >>> Example:
            capacities.assign_my_workspace_to_capacity("0f084df7-c13d-451b-af5f-ed0c466403b2")
        
        '''
        endpoint = f"AssignToCapacity"

        body = {
            "capacityid": capacityId
        }

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def assign_group_to_capacity(self, groupId:str, capacityId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/capacities/groups-assign-to-capacity
        ''' Assigns the specified workspace to the specified capacity

        >>> Params:
            groupId: The workspace ID
            
        >>> Example:
            capacities.assign_group_to_capacity("f089354e-8366-4e18-aea3-4cb4a3a50b48", "0f084df7-c13d-451b-af5f-ed0c466403b2")
        
        '''
        endpoint = f"groups/{groupId}/AssignToCapacity"

        body = {
            "capacityid": capacityId
        }

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def get_group_capacity_assignment_status(self, groupId:str):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/capacities/groups-capacity-assignment-status
        ''' Gets the status of the assignment-to-capacity operation for the specified workspace

        >>> Params:
            groupId: The workspace ID
            
        >>> Example:
            capacities.get_group_capacity_assignment_status("f089354e-8366-4e18-aea3-4cb4a3a50b48")
        
        '''
        endpoint = f"groups/{groupId}/CapacityAssignmentStatus"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_my_workspace_capacity_assignment_status(self):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/capacities/groups-capacity-assignment-status-my-workspace
        ''' Gets the status of the My workspace assignment-to-capacity operation

        >>> Params:
            
            
        >>> Example:
            capacities.get_my_workspace_capacity_assignment_status()
        
        '''
        endpoint = f"CapacityAssignmentStatus"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def patch_workload(self, capacityId:str, workloadName:str, state:str, percentage:int):
        #https://learn.microsoft.com/en-us/rest/api/power-bi/capacities/patch-workload
        ''' Changes the state of a specific workload to Enabled or Disabled. When enabling a workload, specify the percentage of maximum memory that the workload can consume

        >>> Params:
            capacityId: The capacity ID
            workloadName: The name of the workload
            state: The capacity workload state, either Enabled or Disabled
            percentage: The percentage of the maximum memory that a workload can consume (set by the user)
            
        >>> Example:
            capacities.patch_workload("0f084df7-c13d-451b-af5f-ed0c466403b2", "Dataflows", "Enabled", 66)
        
        '''
        endpoint = f"capacities/{capacityId}/Workloads/{workloadName}"

        body = {
            "state": state,
            "maxMemoryPercentageSetByUser": percentage
        }

        method = 'patch'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response

    def sample(self, capacityId:str):
        #
        ''' Sample

        >>> Params:
            capacityId: The capacity ID
            
        >>> Example:
            capacities.
        
        '''
        endpoint = f"capacities/"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    

    