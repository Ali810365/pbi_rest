#library for accessing admin resources
#https://learn.microsoft.com/en-us/rest/api/power-bi/admin
from library.requests import audit_requests
import string

class Admin():
    def __init__(self):
        pass

    def add_power_bi_encryption_key(self, name:str, keyVaultKeyIdentifier:str, activate:bool, isDefault:bool): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/add-power-bi-encryption-key

        Adds an encryption key for Power BI workspaces assigned to a capacity

        >>> Params:
            top: Returns only the first n results
            name: The name of the encryption key
            keyVaultKeyIdentifier: The URI that uniquely specifies an encryption key in Azure Key Vault
            activate: Whether to activate any inactivated capacities and to use this key for its encryption
            isDefault: Whether an encryption key is the default key for the entire tenant. Any newly created capacity inherits the default key
        
        >>> Example:
            admin.add_power_bi_encryption_key("Contoso Sales", "https://contoso-vault2.vault.azure.net/keys/ContosoKeyVault/b2ab4ba1c7b341eea5ecaaa2wb54c4d2", "True", "True")
        
        '''
        endpoint = f"admin/tenantKeys"

        method = 'post'

        body = {
            "activate": activate,
            "isDefault": isDefault,
            "keyVaultKeyIdentifier": keyVaultKeyIdentifier,
            "name": name
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def get_app_users_as_admin(self, appId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/apps-get-app-users-as-admin

        Returns a list of users that have access to the specified app

        >>> Params:
            appId: The app ID
        
        >>> Example:
            admin.get_app_users_as_admin("f089354e-8366-4e18-aea3-4cb4a3a50b48")
        
        '''
        endpoint = f"admin/apps/{appId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_apps_as_admin(self, top:int): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/apps-get-apps-as-admin

        Returns a list of apps in the organization

        >>> Params:
            top: Returns only the first n results
        
        >>> Example:
            admin.get_apps_as_admin(100)
        
        '''
        endpoint = f"admin/apps?$top={top}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response 
    
    def assign_workspaces_to_capacity(self, request_body): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/capacities-assign-workspaces-to-capacity

        Assigns the specified workspaces to the specified Premium capacity

        >>> Params:
            request_body: capacityMigrationAssignments -> Assignment contract for migrating workspaces to a premium capacity as tenant admin
        
        >>> Example:
            admin.assign_workspaces_to_capacity(request_body)
        
        '''
        endpoint = f"admin/capacities/AssignWorkspaces"

        method = 'post'
        
        response = audit_requests(endpoint, method, json=request_body)
        
        return response

    def get_capacity_users_as_admin(self, capacityId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/capacities-get-capacity-users-as-admin

        Returns a list of users that have access to the specified workspace

        >>> Params:
            capacityId: The capacity ID
        
        >>> Example:
            admin.get_capacity_users_as_admin(capacityId)
        
        '''
        endpoint = f"admin/capacities/{capacityId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def unassign_workspaces_from_capcity(self, request_body,): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/capacities-unassign-workspaces-from-capacity

        Unassigns the specified workspaces from capacity

        >>> Params:
            request_body: list of workspaces to unsassign
        
        >>> Example:
            admin.unassign_workspaces_from_capcity(request_body)
        
        '''
        endpoint = f"admin/capacities/UnassignWorkspaces"

        method = 'get'
        
        response = audit_requests(endpoint, method, json=request_body)
        
        return response

    def get_dashboards_subscriptions(self, dashboardId): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/dashboards-get-dashboard-subscriptions-as-admin
        
        Returns a list of dashboard subscriptions along with subscriber details. This is a preview API call

        >>> Params:
            dashboardId: The dashboard ID
        
        >>> Example:
            admin.get_dashboards_subscriptions("2b5ca223-46d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"admin/dashboards/{dashboardId}/subscriptions"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dashboards_users(self, dashboardId): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/dashboards-get-dashboard-users-as-admin
        
        Returns a list of users that have access to the specified dashboard

        >>> Params:
            dashboardId: The dashboard ID
        
        >>> Example:
            admin.get_dashboards_users("2b5ca223-46d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"admin/dashboards/{dashboardId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_dashboards(self, skip:int=0, top:int=5000, expand:str=None, filter:str=None): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/dashboards-get-dashboards-as-admin
        
        Returns a list of dashboards for the organization

        >>> Params:
            skip: Skips the first n results default value 0
            top: Returns only the first n results, if not specified default value 5000
            expand: Accepts a comma-separated list of data types, which will be expanded inline in the response. Supports tiles
            filter: Filters the results, based on a boolean condition
        
        >>> Example:
            admin.get_dashboards(filter="contains(displayName, 'IT Spend Analysis Sample')")
        
        '''
        endpoint = f"admin/dashboards?$skip={skip}&$top={top}"

        if(expand):
            endpoint = f"admin/dashboards?$expand={expand}&$skip={skip}&$top={top}"
        if(filter):
            endpoint = f"admin/dashboards?$filter={filter}&$skip={skip}&$top={top}"
        if(filter and expand):
            endpoint = f"admin/dashboards?$expand={expand}&$filter={filter}&$skip={skip}&$top={top}"

        print(endpoint)

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dashboards_in_group(self, groupId, skip:int=0, top:int=5000, expand:str=None, filter:str=None): 
        ''' Returns a list of dashboards from the specified workspace

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            admin.get_dashboards("3b5ca243-47d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"admin/groups/{groupId}/dashboards?$skip={skip}&$top={top}"
        
        if(filter):
            endpoint = f"admin/groups/{groupId}/dashboards?$filter={filter}&$skip={skip}&$top={top}"
        

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_dashboards_tiles(self, dashboardId): 
        ''' Returns a list of tiles within the specified dashboard

        >>> Params:
            dashboardId: The dashboard ID
        
        >>> Example:
            admin.get_dashboards_tiles("3b5ca243-47d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"admin/dashboards/{dashboardId}/tiles"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def export_dataflow_as_admin(self, dataflowId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/dataflows-export-dataflow-as-admin

        Exports the definition for the specified dataflow to a JSON file

        >>> Params:
            dataflowId: The dataflow ID
        
        >>> Example:
            admin.export_dataflow_as_admin("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"admin/dataflows/{dataflowId}/export"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_dataflow_datasources_as_admin(self, dataflowId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/dataflows-get-dataflow-datasources-as-admin

        Returns a list of data sources for the specified dataflow

        >>> Params:
            dataflowId: The dataflow ID
        
        >>> Example:
            admin.get_dataflow_datasources_as_admin("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"admin/dataflows/{dataflowId}/datasources"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_dataflow_users_as_admin(self, dataflowId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/dataflows-get-dataflow-users-as-admin

        Returns a list of users that have access to the specified dataflow

        >>> Params:
            dataflowId: The dataflow ID
        
        >>> Example:
            admin.get_dataflow_users_as_admin("cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"admin/dataflows/{dataflowId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_dataflows_as_admin(self): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/dataflows-get-dataflows-as-admin

        Returns a list of dataflows for the organization

        >>> Params:
            top: Returns only the first n results
        
        >>> Example:
            admin.get_dataflows_as_admin()
        
        '''
        endpoint = f"admin/dataflows"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_dataflows_in_group_as_admin(self, groupId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/dataflows-get-dataflows-in-group-as-admin

        Returns a list of dataflows from the specified workspace

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            admin.get_dataflows_in_group_as_admin("f089354e-8366-4e18-aea3-4cb4a3a50b48")
        
        '''
        endpoint = f"admin/groups/{groupId}/dataflows"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_upstream_dataflows_in_group_as_admin(self, groupId:str, dataflowId:str,): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/dataflows-get-upstream-dataflows-in-group-as-admin

        Returns a list of upstream dataflows for the specified dataflow

        >>> Params:
            groupId: The workspace ID
            dataflowId: The dataflow ID
        
        >>> Example:
            admin.get_upstream_dataflows_in_group_as_admin("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        
        '''
        endpoint = f"admin/groups/{groupId}/dataflows/{dataflowId}/upstreamDataflows"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_dataset_users_as_admin(self, datasetId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/datasets-get-dataset-users-as-admin

        Returns a list of users that have access to the specified dataset

        >>> Params:
            datasetId: The dataset ID
        
        >>> Example:
            admin.get_dataset_users_as_admin("f089354e-8366-4e18-aea3-4cb4a3a50b48")
        
        '''
        endpoint = f"admin/datasets/{datasetId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_datasets_as_admin(self): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/datasets-get-datasets-as-admin

        Returns a list of datasets for the organization
        
        >>> Example:
            admin.get_datasets_as_admin()
        
        '''
        endpoint = f"admin/datasets"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_datasets_in_group_as_admin(self, groupId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/datasets-get-datasets-in-group-as-admin

        Returns a list of datasets from the specified workspace

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            admin.get_datasets_in_group_as_admin("f089354e-8366-4e18-aea3-4cb4a3a50b48")
        
        '''
        endpoint = f"admin/groups/{groupId}/datasets"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_datasources_as_admin(self, datasetId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/datasets-get-datasources-as-admin

        Returns a list of data sources for the specified dataset

        >>> Params:
            datasetId: The dataset ID
        
        >>> Example:
            admin.get_datasources_as_admin("f089354e-8366-4e18-aea3-4cb4a3a50b48")
        
        '''
        endpoint = f"admin/datasets/{datasetId}/datasources"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_activity_events(self, startDateTime, endDateTime): 
        ''' Returns a list of audit activity events for a tenant

        Provide either a continuation token or both a start and end date time. 
        StartDateTime and EndDateTime must be in the same UTC day and should be 
        wrapped in single quotes

        >>> Params:
            
        
        >>> Example:
            
        
        '''
        endpoint = f"admin/activityevents?startDateTime={startDateTime}&endDateTime={endDateTime}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_capacities_as_admin(self): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/get-capacities-as-admin

        Returns a list of capacities for the organization
        
        >>> Example:
            admin.get_capacities_as_admin(100)
        
        '''
        endpoint = f"admin/capacities"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_power_bi_encryption_keys(self): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/get-power-bi-encryption-keys

        Returns the encryption keys for the tenant
        
        >>> Example:
            admin.get_power_bi_encryption_keys()
        
        '''
        endpoint = f"admin/tenantKeys"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_refreshable_for_capacity(self, capacityId:str, refreshableId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/get-refreshable-for-capacity

        Returns the specified refreshable for the specified capacity that the user has access to

        Power BI retains a seven-day refresh history for each dataset, up to a maximum of sixty refreshes.

        >>> Params:
            capacityId: The capacity ID
            refreshableId: The refreshable ID
        
        >>> Example:
            admin.get_refreshable_for_capacity(capacityId, refreshableId)
        
        '''
        endpoint = f"admin/capacities/{capacityId}/refreshables/{refreshableId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_refreshables(self, top:int): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/get-refreshables

        Returns a list of refreshables for the organization within a capacity
    
        Power BI retains a seven-day refresh history for each dataset, up to a maximum of sixty refreshes

        >>> Params:
            top: Returns only the first n results
        
        >>> Example:
            admin.get_refreshables(10)
        
        '''
        endpoint = f"admin/capacities/refreshables?$top={top}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def get_refreshables_for_capacity(self, capacityId:str, top:int, ): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/get-refreshables-for-capacity

        Returns a list of refreshables for the specified capacity that the user has access to

        Power BI retains a seven-day refresh history for each dataset, up to a maximum of sixty refreshes

        >>> Params:
            capacityId: The capacity ID
            top: Returns only the first n results
        
        >>> Example:
            admin.get_refreshables_for_capacity(10)
        
        '''
        endpoint = f"admin/capacities/{capacityId}/refreshables?$top={top}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response               

    def add_user(self, groupId:str, groupUserAccessRight:str, identifier:str, principalType:str): 
        ''' Grants user permissions to the specified workspace

        >>> Params:
            groupId: The workspace ID
            groupUserAccessRight: Permission level Options : Admin, User, Contributor, Member, Viewer, None
            principalType: The principal type Options: User, App, Group
        
        >>> Example:
            admin.add_user("3b5ca243-47d1-4be5-ac56-57c62291607d", "Admin", "john@contoso.com", "User")
        
        '''
        endpoint = f"admin/groups/{groupId}/users"

        string.capwords(groupUserAccessRight)
        string.capwords(principalType)

        body = {
            "groupUserAccessRight": groupUserAccessRight,
            "identifier": identifier,
            "principalType": principalType
        }

        method = 'post'
        
        response = audit_requests(endpoint, method, json=body)
        
        return response

    def delete_user(self, groupId:str, user:str): 
        ''' Returns a list of users that have access to the specified workspace

        >>> Params:
            groupId: The workspace ID
            user: The user principal name (UPN) of the user to remove (likely email address)
        
        >>> Example:
            admin.delete_user("3b5ca243-47d1-4be5-ac56-57c62291607d", "john@contoso.com")
        
        '''
        endpoint = f"admin/groups/{groupId}/users/{user}"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_group(self, groupId:str): 
        ''' Returns a workspace for the organization

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            admin.get_group(groupId)
        
        '''
        endpoint = f"admin/groups/{groupId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_users(self, groupId:str): 
        ''' Returns a list of users that have access to the specified workspace

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            admin.get_group(groupId)
        
        '''
        endpoint = f"admin/groups/{groupId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_groups(self, top:int): 
        ''' Returns a list of workspaces for the organization

        >>> Params:
            top: Returns only the first n results
        
        >>> Example:
            admin.get_groups(100)
        
        '''
        endpoint = f"admin/groups?$top={top}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_unused_artifacts_as_admin(self, groupId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/groups-get-unused-artifacts-as-admin

        Returns a list of datasets, reports, and dashboards that have not been used within 30 days for the specified workspace. This is a preview API call

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            admin.get_unused_artifacts_as_admin("f089354e-8366-4e18-aea3-4cb4a3a50b48")
        
        '''
        endpoint = f"admin/groups/{groupId}/unused"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def restore_deleted_group_as_admin(self, groupId:str, emailAddress:str, name:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/groups-restore-deleted-group-as-admin

        Restores a deleted workspace

        >>> Params:
            groupId: The workspace ID
            emailAddress: The email address of the owner of the group to be restored
            name: The name of the group to be restored
        
        >>> Example:
            admin.restore_deleted_group_as_admin("3bec11ee-48a9-490c-8e4d-1ebba90d491a", "john@contoso.com", "Restored Workspace")
        
        '''
        endpoint = f"admin/groups/{groupId}/restore"

        method = 'post'

        body = {
            "emailAddress": emailAddress,
            "name": name
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def update_group_as_admin(self, groupId:str, name:str, description:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/groups-update-group-as-admin

        Updates the properties of the specified workspace

        Only the name and description can be updated. The name must be unique inside an organization.

        >>> Params:
            groupId: The workspace ID
            name: The group name
            description: Group description
        
        >>> Example:
            admin.update_group_as_admin("e2284830-c8dc-416b-b19a-8cdcd2729332", "Updated Sales Results", "Refreshed sales numbers")
        
        '''
        endpoint = f"admin/groups/{groupId}"

        method = 'patch'

        body = {
            "name": name,
            "description": description
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def get_imports_as_admin(self): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/imports-get-imports-as-admin

        Returns a list of imports for the organization

        >>> Params:
            filter: 
        
        >>> Example:
            admin.get_imports_as_admin()
        
        '''
        endpoint = f"admin/imports"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def remove_label_as_admin(self, request_body): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/information-protection-remove-labels-as-admin

        Remove sensitivity labels from Power BI items (such as reports or dashboards) by item ID

        >>> Params:
            request_body: 
        
        >>> Example:
            admin.remove_label_as_admin()
        
        '''
        endpoint = f"admin/informationprotection/removeLabels"

        method = 'post'
        
        response = audit_requests(endpoint, method, json=request_body)
        
        return response
    
    def set_labels_as_admin(self, request_body): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/information-protection-set-labels-as-admin

        Set sensitivity labels on Power BI items (such as reports or dashboards) by item ID

        >>> Params:
            request_body: 
        
        >>> Example:
            admin.set_labels_as_admin()
        
        '''
        endpoint = f"admin/informationprotection/setLabels"

        method = 'post'
        
        response = audit_requests(endpoint, method, json=request_body)
        
        return response
    
    def patch_capacity_as_admin(self, capacityId:str, tenantKeyId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/patch-capacity-as-admin

        Changes specific capacity information. Currently, this API call only supports changing the capacity's encryption key

        >>> Params:
            capacityId: The capacity ID
            tenantKeyId: The ID of the encryption key 
        
        >>> Example:
            admin.patch_capacity_as_admin("0f084df7-c13d-451b-af5f-ed0c466403b2", "82d9a37a-2b45-4221-b012-cb109b8e30c7")
        
        '''
        endpoint = f"admin/capacities/{capacityId}"

        method = 'patch'

        body = {
            "tenantKeyId": tenantKeyId,
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def pipelines_delete_user_as_admin(self, pipelineId:str, identifier:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/pipelines-delete-user-as-admin

        Removes user permissions from a specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
            identifier: For the principal type User, provide the user principal name (UPN). Otherwise, provide the Object ID of the principal
        
        >>> Example:
            admin.pipelines_delete_user_as_admin("8ce96c50-85a0-4db3-85c6-7ccc3ed46523", "5dba60b0-d9a7-42a3-b12c-6d9d51e7739a")
        
        '''
        endpoint = f"admin/pipelines/{pipelineId}/users/{identifier}"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_pipeline_users_as_admin(self, pipelineId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/pipelines-get-pipeline-users-as-admin

        Returns a list of users that have access to a specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
        
        >>> Example:
            admin.get_pipeline_users_as_admin("8ce96c50-85a0-4db3-85c6-7ccc3ed4652")
        
        '''
        endpoint = f"admin/pipelines/{pipelineId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_pipelines_as_admin(self): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/pipelines-get-pipelines-as-admin

        Returns a list of deployment pipelines for the organization

        >>> Params:
            filter: 
        
        >>> Example:
            admin.get_pipelines_as_admin()
        
        '''
        endpoint = f"admin/pipelines"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def update_user_as_admin(self, pipelineId:str, request_body): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/pipelines-update-user-as-admin

        Grants user permissions to a specified deployment pipeline

        >>> Params:
            pipelineId: The deployment pipeline ID
        
        >>> Example:
            admin.update_user_as_admin("8ce96c50-85a0-4db3-85c6-7ccc3ed46523")
        
        '''
        endpoint = f"admin/pipelines/{pipelineId}/users"

        method = 'post'
        
        response = audit_requests(endpoint, method, json=request_body)
        
        return response
    
    def delete_profile_as_admin(self, profileId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/profiles-delete-profile-as-admin

        Deletes the specified service principal profile

        >>> Params:
            profileId: The service principal profile ID
        
        >>> Example:
            admin.delete_profile_as_admin("8ce96c50-85a0-4db3-85c6-7ccc3ed46523")
        
        '''
        endpoint = f"admin/profiles/{profileId}"

        method = 'delete'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_profiles_as_admin(self): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/profiles-get-profiles-as-admin

        Returns a list of service principal profiles for the organization

        >>> Params:
            filter: 
        
        >>> Example:
            admin.get_profiles_as_admin()
        
        '''
        endpoint = f"admin/profiles"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_report_subscriptions(self, reportId): 
        ''' Returns a list of report subscriptions along with subscriber details. This is a preview API call

        >>> Params:
            reportId: The report ID
        
        >>> Example:
            
        
        '''
        endpoint = f"admin/reports/{reportId}/subscriptions"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_report_users(self, reportId): 
        ''' Returns a list of users that have access to the specified report

        >>> Params:
            reportId: The report ID
        
        >>> Example:
            
        
        '''
        endpoint = f"admin/reports/{reportId}/users"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_reports(self): 
        ''' Returns a list of reports for the organization

        >>> Params:
            
        
        >>> Example:
            
        
        '''
        endpoint = f"admin/reports"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_reports_in_group(self, groupId): 
        ''' Returns a list of reports from the specified workspace

        >>> Params:
            groupId: The workspace ID
        
        >>> Example:
            admin.get_reports_in_group("3b5ca243-47d1-4be5-ac56-57c62291607d")
        
        '''
        endpoint = f"admin/groups/{groupId}/reports"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response

    def rotate_power_bi_encryption_key(self, tenantKeyId:str, keyVaultKeyIdentifier:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/rotate-power-bi-encryption-key

        Rotate the encryption key for Power BI workspaces assigned to a capacity

        >>> Params:
            tenantKeyId: The tenant key ID
        
        >>> Example:
            admin.rotate_power_bi_encryption_key("82d9a37a-2b45-4221-b012-cb109b8e30c7", keyVaultKeyIdentifier)
        
        '''
        endpoint = f"admin/tenantKeys/{tenantKeyId}/Default.Rotate"

        method = 'post'
        
        body = {
            "keyVaultKeyIdentifier": keyVaultKeyIdentifier
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response
    
    def get_user_artifact_access_as_admin(self, userId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/users-get-user-artifact-access-as-admin

        Returns a list of Power BI items (such as reports or dashboards) that the specified user has access to

        >>> Params:
            userId: The graph ID or user principal name (UPN) of the user
        
        >>> Example:
            admin.sample(100)
        
        '''
        endpoint = f"admin/users/{userId}/artifactAccess"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_user_subscriptions_as_admin(self, userId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/users-get-user-subscriptions-as-admin

        Returns a list of subscriptions for the specified user. This is a preview API call

        >>> Params:
            userId: The graph ID or user principal name (UPN) of the user
        
        >>> Example:
            admin.get_user_subscriptions_as_admin("f089354e-8366-4e18-aea3-4cb4a3a50b48")
        
        '''
        endpoint = f"admin/users/{userId}/subscriptions"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def links_shared_to_whole_organization(self): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/widely-shared-artifacts-links-shared-to-whole-organization

        Returns a list of Power BI items (such as reports or dashboards) that are shared with the whole organization through links

        >>> Params:
            filter: 
        
        >>> Example:
            admin.links_shared_to_whole_organization()
        
        '''
        endpoint = f"admin/widelySharedArtifacts/linksSharedToWholeOrganization"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def published_to_web(self): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/widely-shared-artifacts-published-to-web

        Returns a list of Power BI items (such as reports or dashboards) that are published to the web

        >>> Params:
            filter: 
        
        >>> Example:
            admin.published_to_web()
        
        '''
        endpoint = f"admin/widelySharedArtifacts/publishedToWeb"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_modified_workspaces(self): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-modified-workspaces

        Gets a list of workspace IDs in the organization

        >>> Params:
            filter: 
        
        >>> Example:
            admin.get_modified_workspaces()
        
        '''
        endpoint = f"admin/workspaces/modified"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_scan_result(self, scanId:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-scan-result

        Gets the scan result for the specified scan

        >>> Params:
            scanId: The scan ID, which is included in the response from the workspaces or the Admin - WorkspaceInfo PostWorkspaceInfo API call that triggered the scan
        
        >>> Example:
            admin.get_scan_result("e7d03602-4873-4760-b37e-1563ef5358e3")
        
        '''
        endpoint = f"admin/workspaces/scanResult/{scanId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    def get_scan_status(self, sample:str): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-scan-status

        The user must have administrator rights (such as Microsoft 365 Global Administrator or Power BI Service Administrator) or authenticate using a service principal

        >>> Params:
            scanId: 
        
        >>> Example:
            admin.get_scan_status("e7d03602-4873-4760-b37e-1563ef5358e3")
        
        '''
        endpoint = f"admin/workspaces/scanStatus/{scanId}"

        method = 'get'
        
        response = audit_requests(endpoint, method)
        
        return response
    
    
    def post_workspace_info(self, request_body): 
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-post-workspace-info

        Initiates a call to receive metadata for the requested list of workspaces

        >>> Params:
            request_body: 
        
        >>> Example:
            admin.post_workspace_info(request_body)
        
        '''
        endpoint = f"admin/workspaces/getInfo"

        method = 'post'
        
        response = audit_requests(endpoint, method, json=request_body)
        
        return response
    
    
    
    
    
    