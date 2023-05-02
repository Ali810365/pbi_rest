import requests
from datetime import datetime, timedelta
from library.date_conversion import FormateDate
from library.requests import audit_requests

class Reports():
    def __init__(self):
        pass
    
    def clone_report(self, reportId:str, name:str=None, request_body={}):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/clone-report
        
        Clones the specified report from >>> My workspace
            
        >>> Params:
            reportId: The report ID
            name: The new report name (ignore if using request_body)
            request_body: Optional paramaters
        
        >>> Example:
            >>> reports.clone_report('f089354e-8366-4e18-aea3-4cb4a3a50b48', 'cloned report')
        '''
        if(name):
            request_body = {
                "name": f"{name}"
            }

        endpoint = f"reports/{reportId}/Clone"

        method = 'post'

        response = audit_requests(endpoint, method, json=request_body)

        return response

    def clone_report_in_group(self, groupId:str, reportId:str, name:str=None, request_body={}):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/clone-report-in-group
        
        Clones the specified report from the specified workspace
            
        >>> Params:
            groupId: The workspace ID
            reportId: The report ID
            name: The new report name (ignore if using request_body)
            request_body: Optional paramaters 
        
        >>> Example:
            >>> reports.clone_report('f089354e-8366-4e18-aea3-4cb4a3a50b48', 'f089354e-8366-4e18-aea3-4cb4a3a50b48', 'cloned report')
        '''

        if(name):
            request_body = {
                "name": f"{name}"
            }

        endpoint = f"groups/{groupId}/reports/{reportId}/Clone"

        method = 'post'

        response = audit_requests(endpoint, method, json=request_body)

        return response
    
    def delete_report(self, reportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/delete-report
        
        Deletes the specified report from >>> My Workspace
        
        >>> Params:
            reportId: The report ID

        >>> Example:
            >>> reports.delete_report('5b218778-e7a5-4d73-8187-f10824047715')
        '''
        endpoint = f"reports/{reportId}"

        method = 'delete'

        response = audit_requests(endpoint, method)

        return response
    
    def delete_report_in_group(self, groupId:str, reportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/delete-report-in-group
        
        Deletes the specified report from >>> the specified workspace

        >>> Params:
            groupId: The group ID
            reportId: The report ID

        >>> Example:
            >>> reports.delete_report_in_group('f089354e-8366-4e18-aea3-4cb4a3a50b48', '5b218778-e7a5-4d73-8187-f10824047715')
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}"

        method = 'delete'

        response = audit_requests(endpoint, method)

        return response
    
    def export_report(self, reportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/export-report
        
        Exports the specified report from My workspace to a Power BI .pbix or .rdl file

        >>> Params:
            reportId: The report ID

        >>> Example:
            >>> reports.export_report("5b218778-e7a5-4d73-8187-f10824047715")
        '''
        endpoint = f"reports/{reportId}/Export"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def export_report_in_group(self, groupId:str, reportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/export-report
        
        Exports the specified report from My workspace to a Power BI .pbix or .rdl file

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID

        >>> Example:
            >>> reports.export_report("f089354e-8366-4e18-aea3-4cb4a3a50b48", "5b218778-e7a5-4d73-8187-f10824047715")
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}/Export"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def export_to_file(self, reportId:str, format:str=None, request_body={}):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/export-to-file
        
        Exports the specified report from My workspace to the requested file format

        >>> Params:
            reportId: The report ID
            format: The requested format for the exported file
            request_body: Optional paramters

        >>> Example:
            >>> reports.export_to_file()
        '''
        endpoint = f"reports/{reportId}/ExportTo"

        method = 'post'

        if(format):
            request_body = {
                "format": format
            }

        response = audit_requests(endpoint, method, json=request_body)

        return response
    
    def export_to_file_in_group(self, groupId:str, reportId:str, format:str=None, request_body={}):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/export-to-file-in-group
        
        Exports the specified report from the specified workspace to the requested file format

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID
            format: The requested format for the exported file
            request_body: Optional paramters

        >>> Example:
            >>> reports.export_to_file_in_group()
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}/ExportTo"

        method = 'post'

        if(format):
            request_body = {
                "format": format
            }

        response = audit_requests(endpoint, method, json=request_body)

        return response
    
    def get_datasources(self, reportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-datasources
        
        Returns a list of data sources for the specified paginated report (RDL) from My workspace

        >>> Params:
            reportId: The report ID

        >>> Example:
            >>> reports.get_datasources("cfafbeb1-8037-4d0c-896e-a46fb27ff228")
        '''
        endpoint = f"reports/{reportId}/datasources"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_datasources_in_group(self, groupId:str, reportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-datasources-in-group
        
        Returns a list of data sources for the specified paginated report (RDL) from the specified workspace

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID

        >>> Example:
            >>> reports.get_datasources_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}/datasources"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_export_to_file_status(self, reportId:str, exportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-export-to-file-status
        
        Returns the current status of the Export to File job for the specified report from My workspace

        >>> Params:
            reportId: The report ID
            exportId: The export ID

        >>> Example:
            >>> reports.get_export_to_file_status(reportId, exportId)
        '''
        endpoint = f"reports/{reportId}/exports/{exportId}"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_export_to_file_status_in_group(self, groupId:str, reportId:str, exportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-export-to-file-status-in-group
        
        Returns the current status of the Export to File In Group job for the specified report from the specified workspace

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID
            exportId: THe export ID

        >>> Example:
            >>> reports.get_export_to_file_status_in_group(groupId, reportId, exportId)
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}/exports/{exportId}"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_file_of_export_to_file(self, reportId:str, exportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-file-of-export-to-file
        
        Returns the file from the Export to File job for the specified report from My workspace

        >>> Params:
            reportId: The report ID
            exportId: The export ID

        >>> Example:
            >>> reports.get_file_of_export_to_file(reportId, exportId)
        '''
        endpoint = f"reports/{reportId}/exports/{exportId}/file"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_file_of_export_to_file_in_group(self, groupId:str, reportId:str, exportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-file-of-export-to-file-in-group
        
        Returns the file from the Export to File In Group job for the specified report from the specified workspace

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID
            exportId: The export Id

        >>> Example:
            >>> reports.get_file_of_export_to_file_in_group(groupId, reportID, exportId)
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}/exports/{exportId}/file"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_page(self, reportId:str, pageName:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-page
        
        Returns the specified page within the specified report from My workspace

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID
            pageName: The page name

        >>> Example:
            >>> reports.get_page("879445d6-3a9e-4a74-b5ae-7c0ddabf0f11", "ReportSection")
        '''
        endpoint = f"reports/{reportId}/pages/{pageName}"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_page_in_group(self, groupId:str, reportId:str, pageName:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-page-in-group
        
        Returns the specified page within the specified report from the specified workspace

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID
            pageName: The page name

        >>> Example:
            >>> reports.get_page_in_group()
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}/pages/{pageName}"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_pages(self, reportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-pages
        
        Returns a list of pages within the specified report from My workspace

        >>> Params:
            reportId: The report ID

        >>> Example:
            >>> reports.get_pages("879445d6-3a9e-4a74-b5ae-7c0ddabf0f11")
        '''
        endpoint = f"reports/{reportId}/pages"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_pages_in_group(self, groupId:str, reportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-pages-in-group
        
        Returns a list of pages within the specified report from the specified workspace

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID

        >>> Example:
            >>> reports.get_pages_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "879445d6-3a9e-4a74-b5ae-7c0ddabf0f11")
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}/pages"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_report(self, reportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-report
        
        Returns the specified report from My workspace

        >>> Params:
            reportId: The report ID

        >>> Example:
            >>> reports.get_report("879445d6-3a9e-4a74-b5ae-7c0ddabf0f11")
        '''
        endpoint = f"reports/{reportId}"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_report_in_group(self, groupId:str, reportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-report-in-group
        
        Returns the specified report from the specified workspace

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID

        >>> Example:
            >>> reports.get_report_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "879445d6-3a9e-4a74-b5ae-7c0ddabf0f11")
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_reports(self):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-reports
        
        Returns a list of reports from My workspace

        >>> Example:
            >>> reports.get_reports()
        '''
        endpoint = f"reports"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def get_reports_in_group(self, groupId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-reports-in-group
        
        Returns a list of reports from the specified workspace

        >>> Params:
            groupId: The workspace ID

        >>> Example:
            >>> reports.get_reports_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48")
        '''
        endpoint = f"groups/{groupId}/reports"

        method = 'get'

        response = audit_requests(endpoint, method)

        return response
    
    def rebind_report(self, reportId:str, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/rebind-report
        
        Rebinds the specified report from My workspace to the specified dataset

        >>> Params:
            reportId: The report ID
            datasetId: The dataset ID

        >>> Example:
            >>> reports.rebind_report(reportId, datasetId)
        '''
        endpoint = f"reports/{reportId}/Rebind"

        method = 'post'

        request_body = {
            "datasetId": datasetId
        }

        response = audit_requests(endpoint, method, json=request_body)

        return response
    
    def rebind_report_in_group(self, groupId:str, reportId:str, datasetId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/rebind-report-in-group
        
        Rebinds the specified report from the specified workspace to the specified dataset

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID
            datasetId: The dataset ID

        >>> Example:
            >>> reports.rebind_report_in_group(reportId, datasetId)
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}/Rebind"

        method = 'post'

        request_body = {
            "datasetId": datasetId
        }

        response = audit_requests(endpoint, method, json=request_body)

        return response
    
    def take_over_in_group(self, groupId:str, reportId:str):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/take-over-in-group
        
        Transfers ownership of the data sources for the specified paginated report (RDL) to the current authorized user

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID

        >>> Example:
            >>> reports.take_over_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229")
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}/Default.TakeOver"

        method = 'post'

        response = audit_requests(endpoint, method)

        return response
    
    def update_datasources(self, reportId:str, updateDetails):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/update-datasources
        
        Updates the data sources of the specified paginated report (RDL) from My workspace

        >>> Params:
            reportId: The report ID

        >>> Example:
            >>> reports.update_datasources("cfafbeb1-8037-4d0c-896e-a46fb27ff229", updateDetails)
        '''
        endpoint = f"reports/{reportId}/Default.UpdateDatasources"

        method = 'post'

        request_body = {
            "updateDetails": updateDetails
        }

        response = audit_requests(endpoint, method, json=request_body)

        return response
    
    def update_datasources_in_group(self, groupId:str, reportId:str, updateDetails):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/update-datasources-in-group
        
        Updates the data sources of the specified paginated report (RDL) from the specified workspace

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID

        >>> Example:
            >>> reports.update_datasources_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "cfafbeb1-8037-4d0c-896e-a46fb27ff229", updateDetails)
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}/Default.UpdateDatasources"

        method = 'post'

        request_body = {
            "updateDetails": updateDetails
        }

        response = audit_requests(endpoint, method, json=request_body)

        return response
    
    def update_report_content(self, reportId:str, request_body={}):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/update-report-content
        
        Updates the content of the specified report from My workspace with the content of a specified source report

        >>> Params:
            reportId: The report ID
            request_body: Required for sourceReport and sourceType

        >>> Example:
            >>> reports.update_report_content("5b218778-e7a5-4d73-8187-f10824047715", request_body)
        '''
        endpoint = f"reports/{reportId}/UpdateReportContent"

        method = 'post'

        response = audit_requests(endpoint, method, json=request_body)

        return response
    
    def update_report_content_in_group(self, groupId:str, reportId:str, request_body={}):
        ''' https://learn.microsoft.com/en-us/rest/api/power-bi/reports/update-report-content-in-group
        
        Updates the content of the specified report from the specified workspace with the content of a specified source report

        >>> Params:
            groupId: The workspace ID
            reportId: The report ID
            request_body: Required for sourceReport and sourceType

        >>> Example:
            >>> reports.update_report_content_in_group("f089354e-8366-4e18-aea3-4cb4a3a50b48", "5b218778-e7a5-4d73-8187-f10824047715", request_body)
        '''
        endpoint = f"groups/{groupId}/reports/{reportId}/UpdateReportContent"

        method = 'post'

        response = audit_requests(endpoint, method, json=request_body)

        return response
    
    
    
    
    
    

