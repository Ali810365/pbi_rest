from library.requests import audit_requests

class TemplateApps():
    def __init__(self):
        pass
    
    def create_install_ticket(self, installDetails):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/template-apps/create-install-ticket
        
        Generates an installation ticket for the automated install flow of the specified template app

        >>> Params:
            installDetails: List of install details
        
        >>> Example:
            templateApps.sample("")
        
        '''
        endpoint = f"CreateTemplateAppInstallTicket"

        method = 'post'

        body = {
            "installDetails": installDetails
        }
        
        response = audit_requests(endpoint, method, json=body)
        
        return response