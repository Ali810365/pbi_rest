import requests
from requests.adapters import HTTPAdapter, Retry
from library.login import headers, authenticated

def audit_requests(endpoint, method, params = None, data = None, json = None):
        if not authenticated():
             return "\nPlease configure Authentication"
        else:
            base_url = 'https://api.powerbi.com/v1.0/myorg/'

            url = base_url + endpoint

            session = requests.session()

            """ 
            re_attempt = Retry(
                        total=5,
                        backoff_factor=0.1,
                        status_forcelist=[ 500, 502, 503, 504 ]
                    )

            session.mount('http://', HTTPAdapter(max_retries=re_attempt)) 
            """

            new_request = requests.Request(
                method=method.upper(),
                headers=headers,
                url=url,
                params=params,
                data=data,
                json=json,
            ).prepare()

            response: requests.Response = session.send(
                request=new_request
            )

            session.close()

            try:
                if response.ok and len(response.content) > 0 and response.headers['Content-Type'] != 'application/zip':
                    
                    return response.json()
            
                elif response.ok and len(response.content) > 0 and response.headers['Content-Type'] == 'application/zip':

                    print('It\'s this one ', response.headers)
                    return response.content

                elif len(response.content) > 0 and response.ok:

                    return {
                        'message': 'response successful',
                        'status_code': response.status_code
                    }

                elif response.ok and len(response.content) == 0:

                    return {
                        'message': 'response successful',
                        'status_code': response.status_code
                    }

                elif not response.ok:

                    return {
                        'status_code': response.status_code,
                        'message': response.text
                    }


            except KeyError as e:
                return e