from typing import List
from typing import Dict
from configparser import ConfigParser
import msal
import urllib
import random
import string
import json
import time


class User():
    AUTHORITY_URL = 'https://login.microsoftonline.com/'
    AUTH_ENDPOINT = '/oauth2/v2.0/authorize?'
    TOKEN_ENDPOINT = '/oauth2/v2.0/token'

    def __init__(
        self,
        application_id: str,
        applicaton_secret: str,
        redirect_uri: str,
        scope: List[str],
        account_type: str = 'common',
        #credentials: str = None
    ):
        letters = string.ascii_lowercase

        #self.credentials = credentials
        self.token_dict = None
        self.application_id = application_id
        self.application_secret = applicaton_secret
        self.api_version = 'v1.0'
        self.account_type = account_type
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.state = ''.join(random.choice(letters) for i in range(10))
        self.access_token = None
        self.refresh_token = None
        self.graph_session = None
        self.id_token = None
        self.graph_url = self.AUTHORITY_URL + self.account_type + self.AUTH_ENDPOINT

        self.client_app = msal.ConfidentialClientApplication(
            client_id= self.application_id,
            authority= self.AUTHORITY_URL + self.account_type,
            client_credential=self.application_secret
        )
    
    def authorization_url(self) -> str:
        auth_url = {
            'response_type':'code',
            'client_id': self.application_id,
            'redirect_uri': self.redirect_uri,
            'resouce': 'https://analysis.windows.net/powerbi/api'
        }

        auth_url = self.client_app.get_authorization_request_url(
            scopes= self.scope,
            state= self.state,
            redirect_uri= self.redirect_uri
        )

        return auth_url

    def login(self) -> None:
        url = self.authorization_url()

        print('Please go to URL provided authorize your account: {}'.format(url))

        my_response = input('Paste the full URL redirect here: ')

        self._redirect_code = my_response

        self.grab_access_token()

        #self.power_bi_session = PowerBiSession(client=self)

    def grab_access_token(self) -> Dict:
        query_dict = urllib.parse.parse_qs(self._redirect_code)

        code = query_dict[self.redirect_uri + '?code']

        token_dict = self.client_app.acquire_token_by_authorization_code(
            code=code,
            scopes=self.scope,
            redirect_uri=self.redirect_uri
        )

        token_dict['expires_in'] = time.time() + int(token_dict['expires_in'])
        token_dict['ext_expires_in'] = time.time() + int(token_dict['ext_expires_in'])
        token_dict['auth_type'] = "user"

        with open('configs/credentials.json', 'w') as f:
            f.write(json.dumps(token_dict, indent=2))

    def silent_login(self, refresh_token):
        token_dict = self.client_app.acquire_token_by_refresh_token(
            refresh_token=refresh_token,
            scopes=self.scope
        )

        if not 'error' in token_dict:
            token_dict['expires_in'] = time.time() + int(token_dict['expires_in'])
            token_dict['ext_expires_in'] = time.time() + int(token_dict['ext_expires_in'])
            token_dict['auth_type'] = "user"

            with open('configs/credentials.json', 'w') as f:
                f.write(json.dumps(token_dict, indent=2))
            
            return token_dict
        else:
            return token_dict

class ServicePrincipal():
    
    def __init__(
        self,
        application_id: str,
        applicaton_secret: str,
        scope: List[str],
        tenant_id: str,
    ):
        self.tenant_id = tenant_id
        self.token_dict = None
        self.application_id = application_id
        self.application_secret = applicaton_secret
        self.api_version = 'v1.0'
        self.scope = scope
        self.access_token = None


        AUTHORITY_URL = 'https://login.microsoftonline.com/{}'.format(self.tenant_id)

        self.client_app = msal.ConfidentialClientApplication(
            client_id= self.application_id,
            client_credential=self.application_secret,
            authority= AUTHORITY_URL
        )
    
    def grab_access_token(self):
        token = self.client_app.acquire_token_for_client(
        scopes=self.scope
        )

        return token
    
    def save_token(self): #saving the token to file
        response = self.grab_access_token()
        credentials = {}
        credentials['token_type'] = response['token_type'] 
        credentials['expires_in'] = time.time() + response['expires_in'] 
        credentials['ext_expires_in'] = time.time() + response['ext_expires_in']
        credentials['access_token'] = response['access_token']
        credentials['auth_type'] = 'service_principal' 

        with open('configs/credentials.json', 'w') as f:
            f.write(json.dumps(credentials, indent=2))


