#Import library
from library.admin import Admin

admin = Admin()

def add_user_to_all_workspaces():
    #load all workspaces in tenant
    workspaces = admin.get_groups(1000)
    
    #iterate through workspaces and add with desired access rights
    for workspace in workspaces:
        admin.add_user(workspace['id'], 'Admin', 'john@contoso.com', 'User')
    

